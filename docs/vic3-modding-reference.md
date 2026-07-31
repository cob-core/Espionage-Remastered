# Victoria 3 Modding Reference (current as of 1.13.9, 2026-07)

Game version: **1.13.9 "Matcha"** (2026-06-25). The wiki's per-version effect/trigger
lists lag behind — regenerate `script_docs` / `dump_data_types` locally instead of
trusting them.

## Patch history that matters to this mod

| Patch | Date | Mod-relevant impact |
|---|---|---|
| **1.9 "Lady Grey"** | 2025-06 | **Treaty rework**: vanilla diplomatic pacts replaced by Treaties composed of Articles; several wargoals became enforceable articles. Custom pact-based `diplomatic_actions` still load (this mod is proof), but treaty articles are the forward direction. [Patch 1.9](https://vic3.paradoxwikis.com/Patch_1.9) · [Treaty modding](https://vic3.paradoxwikis.com/Treaty_modding) |
| **1.10 "Kaffee"** | 2025-09 | Discrimination/culture-traits rework + Cultural Fervor; "Support Separatism" hostile action (espionage-adjacent); events gained `after = {}` block. [Patch 1.10](https://vic3.paradoxwikis.com/Patch_1.10) |
| **1.11 "Chamomile"** | 2025-10 | Music pack; no notable modding changes. |
| **1.12 "Chá de Tília"** | 2025-12 | **`INJECT:`/`REPLACE:` expandable databases** (the modern compat mechanism); contextless (global-scope) journal entries; law amendments; income/expense trigger renames (**legacy names deprecated**). [Patch 1.12](https://vic3.paradoxwikis.com/Patch_1.12) |
| **1.13 "Matcha"** | 2026-04 | Naval overhaul (The Great Wave): ship designer, supply, port bombardment/piracy missions, **Gunboat Diplomacy** (treaty-negotiation coercion); `has_role` split into `has_role_type` (**old usage may break**); scriptable character role archetypes; law groups hideable via `enable { }`. [Patch 1.13](https://vic3.paradoxwikis.com/Patch_1.13) |

## Override & load-order rules (critical)

- **Same filename as vanilla → whole vanilla file replaced.** Avoid; use unique
  `adv_dip_`-prefixed filenames.
- **Different filename, same key:** files load ASCII-ordered by filename; for standard
  databases **last-loaded wins**. **Exception: events and GUI types — first-loaded wins.**
- **Localization never last-wins.** To override a vanilla key, place it in
  `localization/<lang>/replace/`.
- **On_actions merge append-only** for `on_actions`/`events`/`random_events` lists;
  `trigger`/`effect` blocks cannot be replaced additively.
- **Subfolders load after parent folders — and are always loaded.** A `TODO/` subfolder
  does not disable content.
- **`INJECT:` system (1.12+, prefer over any wholesale override):** top-level keys only.
  `INJECT:` (append, errors if entry missing), `REPLACE:`, `TRY_INJECT:`/`TRY_REPLACE:`
  (silent if missing), `INJECT_OR_CREATE:`/`REPLACE_OR_CREATE:`. Caveat: `INJECT:` on
  scripted effects/triggers behaves as `REPLACE:`. Supported in 130+ `common/` folders.
  [Mod compatibility](https://vic3.paradoxwikis.com/Mod_compatibility)

## Debug & test workflow

- Launch with `-debug_mode` → file **hotloading** + console (backtick). On_actions do
  **not** hotload — return to main menu or restart.
- `error.log`: `~/.local/share/Paradox Interactive/Victoria 3/logs/error.log` (Linux).
- Console: `event <namespace.id> [target]`, `reload [file]`, `switchlanguage english`
  (re-reads loc), `observe`, `money`, `add_relations`, `tweak`, `debug_mode` (toggle).
- Docs dumps: console `script_docs` and `dump_data_types` → files in
  `~/.local/share/Paradox Interactive/Victoria 3/docs`. These are the authoritative
  per-version effect/trigger/DataType references.
- Parse failures are **silent at runtime** — a malformed block (e.g. missing `=`) just
  drops content. Always check `error.log` after script changes.
  [Console commands](https://vic3.paradoxwikis.com/Console_commands)

## Structure & metadata

- Mods live in `~/.local/share/Paradox Interactive/Victoria 3/mod/<name>/`, mirroring
  `game/` contents without the `game/` level. Folder names exact & plural
  (exception: `common/technology`).
- `.metadata/metadata.json` fields: `name`, `id` (unique, stable), `version`,
  `game_id: "victoria3"`, `supported_game_version` (wildcards ok — use `"1.13.*"`),
  `short_description`, `tags` (≤5), `relationships`
  (`dependency`/`incompatible_with`/`load_before`/`load_after`),
  `game_custom_data.multiplayer_synchronized`. Optional `_thumbnail.png` alongside.
  [Mod structure](https://vic3.paradoxwikis.com/Mod_structure)

## Format essentials

- **Localization:** folder `localization/<language>/`, filename must end
  `_l_<language>.yml`, **UTF-8 with BOM** or silently ignored, header `l_<language>:`,
  entries `key:0 "text"`. Formatting: `$key$`, `[concept_x]`, `#b ...#!`, `@money!`.
  [Localization](https://vic3.paradoxwikis.com/Localization)
- **Events:** UTF-8-BOM, `namespace = x` header; `country_event`/`state_event`/
  `character_event`; `hidden = yes` for covert mechanics; `after = {}` for post-option
  cleanup (1.10+). [Event modding](https://vic3.paradoxwikis.com/Event_modding)
- **Journal entries:** progress via `current_value`/`goal_add_value`/`progressbar` or
  `scripted_progress_bar`; pulses `on_weekly/monthly/yearly_pulse`; contextless JEs
  since 1.12. [Journal entry modding](https://vic3.paradoxwikis.com/Journal_entry_modding)
- **Treaty articles:** `kind = directed|mutual`, `cost`, `usage_limit`,
  `visible`/`possible`/`can_ratify`/`requirement_to_maintain`, `on_entry_into_force`/
  `on_enforced`/`on_withdrawal`/`on_break`, contravention `conditions` blocks, typed
  `inputs` with `_valid_trigger`s, AI `usage`/accept-score script values, and
  `wargoal_data` for enforceable articles.
  [Treaty modding](https://vic3.paradoxwikis.com/Treaty_modding)

## Espionage-adjacent vanilla scaffolding worth building on

- Hidden events + contextless JEs (1.12) for covert-op state machines.
- Support Separatism action (1.10) — overlaps Support Nationalists' design space.
- Gunboat Diplomacy (1.13) — coercion during treaty negotiation.
- Enforceable custom treaty articles with contravention/consequence mechanics (1.9) —
  the canonical way to add wargoal-backed diplomacy now.
- Diplomatic catalysts — mod has one (`catalyst_pact_formed`) not yet wired to
  espionage pacts (roadmap item).

## Reference URL index

Modding hub: https://vic3.paradoxwikis.com/Modding ·
Patches: https://vic3.paradoxwikis.com/Patches ·
Effects: https://vic3.paradoxwikis.com/Effect ·
Modifier types: https://vic3.paradoxwikis.com/Modifier_types ·
Script values: https://vic3.paradoxwikis.com/Script_value ·
Variables: https://vic3.paradoxwikis.com/Variable ·
Scripted functions: https://vic3.paradoxwikis.com/Scripted_function_modding ·
On actions: https://vic3.paradoxwikis.com/On_actions ·
Dev diaries: https://vic3.paradoxwikis.com/Developer_diaries
