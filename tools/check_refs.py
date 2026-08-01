#!/usr/bin/env python3
"""Reference-integrity checker for Espionage Remastered.

Verifies, across the mod (with vanilla as a fallback definition source):
  1. every trigger_event id resolves to a defined event
  2. every add_modifier name resolves to a defined static modifier
  3. every non-numeric add_modifier multiplier resolves to a defined script value
  4. every defined event's t/d/f and option-name loc keys exist in english AND french
  5. every diplomatic action has its core loc key set in english AND french
  6. every referenced .dds icon path exists in the mod or vanilla gfx tree

Exit 0 = clean; exit 1 = failures printed. Excluded from deployment (tools/).
"""
import pathlib
import re
import sys

MOD = pathlib.Path(__file__).resolve().parent.parent
VANILLA = pathlib.Path.home() / ".steam/steam/steamapps/common/Victoria 3/game"
assert VANILLA.is_dir(), f"vanilla not found at {VANILLA}"

failures: list[str] = []


def read(p: pathlib.Path) -> str:
    return p.read_text(encoding="utf-8-sig", errors="replace")


def strip_comments(text: str) -> str:
    return "\n".join(line.split("#", 1)[0] for line in text.split("\n"))


def script_files(root: pathlib.Path, sub: str) -> list[pathlib.Path]:
    d = root / sub
    return sorted(d.rglob("*.txt")) if d.is_dir() else []


KEY_OPEN = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_.:]*)\s*=\s*\{")


def depth0_keys(text: str) -> list[str]:
    """Keys opened at brace depth 0, tolerating tab-indented top-level entries."""
    keys, depth = [], 0
    for line in text.split("\n"):
        m = KEY_OPEN.match(line)
        if m and depth == 0:
            keys.append(m.group(1))
        depth += line.count("{") - line.count("}")
        depth = max(depth, 0)
    return keys

mod_script = {p: strip_comments(read(p)) for p in script_files(MOD, "common") + script_files(MOD, "events")}

# --- 1. events ---
defined_events: set[str] = set()
for p, t in mod_script.items():
    if p.parts[-2] != "events" and "events" not in p.parts:
        continue
    defined_events |= set(re.findall(r"^([a-z_]+\.\d+)\s*=\s*\{", t, re.M))
for p, t in mod_script.items():
    for eid in re.findall(r"trigger_event\s*=\s*\{\s*id\s*=\s*([a-z_.0-9]+)", t):
        if eid not in defined_events:
            failures.append(f"[event] {p.relative_to(MOD)}: trigger_event id '{eid}' undefined")

# --- 2/3. modifiers and multipliers ---
def toplevel_keys(root: pathlib.Path, sub: str) -> set[str]:
    keys: set[str] = set()
    for p in script_files(root, sub):
        keys |= {k.split(":")[-1] for k in depth0_keys(strip_comments(read(p)))}
    return keys

defined_modifiers = toplevel_keys(MOD, "common/static_modifiers") | toplevel_keys(VANILLA, "common/static_modifiers")
defined_values = toplevel_keys(MOD, "common/script_values") | toplevel_keys(VANILLA, "common/script_values")

for p, t in mod_script.items():
    for block in re.findall(r"add_modifier\s*=\s*\{([^{}]*)\}", t):
        m = re.search(r"name\s*=\s*([a-z_0-9]+)", block)
        if m and m.group(1) not in defined_modifiers:
            failures.append(f"[modifier] {p.relative_to(MOD)}: add_modifier name '{m.group(1)}' undefined")
        mult = re.search(r"multiplier\s*=\s*([A-Za-z_][A-Za-z_0-9]*)", block)
        if mult and mult.group(1) not in defined_values:
            failures.append(f"[value] {p.relative_to(MOD)}: multiplier '{mult.group(1)}' undefined")

# --- 4/5. localization coverage ---
def loc_keys(path: pathlib.Path) -> set[str]:
    keys = set()
    for line in read(path).split("\n"):
        m = re.match(r"\s*([A-Za-z_0-9.]+):\d*\s+\"", line)
        if m:
            keys.add(m.group(1))
    return keys

en = loc_keys(MOD / "localization/english/adv_dip_l_english.yml")
fr = loc_keys(MOD / "localization/french/adv_dip_l_french.yml")

vanilla_loc: set[str] = set()
for p in sorted((VANILLA / "localization/english").rglob("*_l_english.yml")):
    vanilla_loc |= loc_keys(p)

def need(key: str, where: str) -> None:
    if key in vanilla_loc:
        return
    if key not in en:
        failures.append(f"[loc-en] {where}: missing '{key}'")
    if key not in fr:
        failures.append(f"[loc-fr] {where}: missing '{key}'")

for p, t in mod_script.items():
    if "events" not in p.parts:
        continue
    for eid in re.findall(r"^([a-z_]+\.\d+)\s*=\s*\{", t, re.M):
        block_m = re.search(rf"^{re.escape(eid)}\s*=\s*\{{(.*?)^\}}", t, re.M | re.S)
        block = block_m.group(1) if block_m else ""
        for field in ("title", "desc", "flavor"):
            for key in re.findall(rf"{field}\s*=\s*([A-Za-z_0-9.]+)", block):
                need(key, eid)
        for key in re.findall(r"name\s*=\s*([a-z_]+\.\d+\.[a-z]+)", block):
            need(key, eid)

ACTION_KEYS = ["", "_desc", "_action_name", "_action_notification_name", "_action_notification_desc", "_monthly_effect"]
for p in script_files(MOD, "common/diplomatic_actions"):
    t = strip_comments(read(p))
    for action in depth0_keys(t):
        if "monthly_effect" not in t:
            continue
        for suffix in ACTION_KEYS:
            need(action + suffix, f"action {action}")

# --- 5a2. every modifier type used in static definitions must exist ---
valid_types = toplevel_keys(MOD, "common/modifier_type_definitions") | toplevel_keys(VANILLA, "common/modifier_type_definitions")
NON_TYPE_KEYS = {"icon"}
for p in script_files(MOD, "common/static_modifiers"):
    text = strip_comments(read(p))
    depth = 0
    for i, line in enumerate(text.split("\n"), 1):
        m = re.match(r"^\s*([a-z_0-9]+)\s*=", line)
        if m and depth == 1 and m.group(1) not in NON_TYPE_KEYS and m.group(1) not in valid_types:
            failures.append(f"[modtype] {p.relative_to(MOD)}:{i}: unknown modifier type '{m.group(1)}'")
        depth += line.count("{") - line.count("}")

# --- 5b. banned legacy tokens (proven invalid in 1.13 via error.log) ---
LEGACY = ["has_diplomatic_pact = { who = root type = adv_dip",
          "GetDiplomaticPact", "should_invalidate", "should_auto_break", "is_about_to_auto_break",
          "has_role = general", "has_role = admiral", "is_ruler = ",
          "weekly_net_fixed_income", "fixed_net_income <", "fixed_net_income >", "should_be_pinned_by_default = ",
          "damage_ship_percent", "unlocking_technologies = {"]
for p, t in mod_script.items():
    hay = t
    for tok in LEGACY:
        if tok == "unlocking_technologies = {" and "treaty_articles" not in str(p):
            continue
        if tok in hay:
            failures.append(f"[legacy] {p.relative_to(MOD)}: banned 1.13-invalid token '{tok.strip()}'")

# --- 6. icons ---
for p, t in mod_script.items():
    for icon in re.findall(r"[a-zA-Z_/]+\.dds", t):
        rel = icon.lstrip("/")
        if not (MOD / rel).is_file() and not (VANILLA / rel).is_file():
            failures.append(f"[icon] {p.relative_to(MOD)}: '{rel}' not found in mod or vanilla")

# --- 7. v5 secrecy invariants ---
for p, t in mod_script.items():
    if "diplomatic_actions" in str(p):
        if re.search(r"^\s*pact\s*=\s*\{", t, re.M):
            failures.append(f"[secrecy] {p.relative_to(MOD)}: still defines a pact block (operations must be secret)")

loc_all = en | fr
for p in script_files(MOD, "common/diplomatic_actions"):
    text = strip_comments(read(p))
    for action in depth0_keys(text):
        for suffix in ("_action_notification_name", "_action_notification_desc"):
            if action + suffix in loc_all:
                failures.append(f"[secrecy] {action}{suffix} exists in localization — would break silence")

sgui_dir = MOD / "common/scripted_guis"
gui_file = MOD / "gui/journal_entry_widgets/adv_dip_console_widgets.gui"
if sgui_dir.is_dir() and gui_file.is_file():
    defined_sguis = set()
    for p in sorted(sgui_dir.glob("*.txt")):
        defined_sguis |= set(depth0_keys(strip_comments(read(p))))
    for name in set(re.findall(r"GetScriptedGui\('([a-z_0-9]+)'\)", read(gui_file))):
        if name not in defined_sguis:
            failures.append(f"[gui] console references undefined scripted gui '{name}'")

# --- 8. journal-entry widget bindings must resolve (crash-class bug) ---
for p in script_files(MOD, "common/journal_entries"):
    text = strip_comments(read(p))
    for gui_rel, widget_name in re.findall(r'widget\s*=\s*\{[^}]*?gui\s*=\s*"([^"]+)"[^}]*?name\s*=\s*"([^"]+)"', text, re.S):
        gui_path = MOD / gui_rel
        if not gui_path.is_file():
            failures.append(f"[widget] {p.relative_to(MOD)}: gui file '{gui_rel}' not found")
            continue
        if not re.search(rf'name\s*=\s*"{re.escape(widget_name)}"', read(gui_path)):
            failures.append(f"[widget] {p.relative_to(MOD)}: widget '{widget_name}' not defined in {gui_rel} (CRASHES the game)")

if failures:
    print(f"{len(failures)} reference failures:")
    for f in failures:
        print(" ", f)
    sys.exit(1)
print(f"clean: {len(defined_events)} events, {len(mod_script)} script files checked")
