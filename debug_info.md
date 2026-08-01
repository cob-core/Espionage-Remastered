# Debug & Testing Guide — Espionage Remastered

How to properly test the mod. All console commands need the game launched with
`-debug_mode` (Steam launch options, or toggle in-session with the `debug_mode`
console command). Open the console with backtick (`` ` ``).

## Before every test session

1. **Deploy the repo** — the launcher loads a *copy*, not this folder:
   ```
   rsync -a --delete --exclude .git --exclude .idea --exclude docs --exclude tools \
     "/home/caleb/Documents/mods/Espionage Remastered/" \
     "/home/caleb/.local/share/Paradox Interactive/Victoria 3/mod/Espionage-Remastered/"
   ```
2. **Static gates** (catch silent parse failures before launching):
   ```
   python3 tools/check_refs.py
   grep -rnE '^\s*[a-zA-Z_]+ \{' common/ events/    # must return nothing
   ```
3. **After loading in-game**, check for new lines in
   `~/.local/share/Paradox Interactive/Victoria 3/logs/error.log`.
   Paradox script fails silently — the log is the only compiler you get.

## Hotloading

`-debug_mode` hot-reloads most files on save; `reload <file>` forces it.
**Exceptions:** on_actions and diplomatic action definitions generally need a return
to main menu. `switchlanguage english` re-reads localization in place.
`script_docs` / `dump_data_types` dump authoritative effect/trigger references to
`~/.local/share/Paradox Interactive/Victoria 3/docs/`.

## General commands

| Command | Use |
|---|---|
| `event <id> [TAG]` | Fire any event, optionally on another country — the main testing tool; bypasses the monthly dice entirely |
| `observe` | Release your country to the AI and watch (good for AI-usage checks) |
| `money [amount]` | Afford the pacts and event costs |
| `add_relations <TAG> <amount>` | Hit relations thresholds (e.g. auto-break at poor) |
| `research <tech>` | Unlock action tech requirements quickly |
| `activate_law <law_key> [TAG]` | Instantly enact a law — e.g. `activate_law law_spy_agency` skips the whole enactment cycle (the required Spy Agency law in one command) |
| `tweak` | Tweaker GUI — inspect country variables (the `ongoing_*`/`recently_*` cooldowns live here) |

## Setup for espionage testing

Every action gates on the espionage institution. Fast path:
```
research international_relations
activate_law law_spy_agency
```
then invest bureaucracy until the institution reaches the level you're testing
(1–5; see docs/espionage-actions.md for the per-action table).

Pact auto-cancel logic uses `requirement_to_maintain` (since the error.log
remediation): to test it, violate a maintenance condition (e.g. declare war on the
target) and confirm the pact breaks on the next tick.

## Per-feature test recipes

Convention: `X1` events fire on **you** (the spymaster); fire `X2` notification events
on the target with `event <id> <TAG>`. Most `X1` immediates locate their victim by
scanning for the pact, so **establish the pact first** or the event's target scope
comes up empty.

### Steal Technology + the game rule
- `event adv_dip_event.91` → 3 options (production/military/society); confirm the cost
  modifier and, on detection (1/6 within the option), `.92` arriving at the target.
- **Game rule check:** in the lobby set Technology Stealing to *Players Only* → as any
  AI (via `observe`) the action must not appear; as you it must. Set *Disable* → gone
  for everyone. Mid-save rule changes also invalidate existing AI pacts.

### Assassination
- Pact on a target, then `event adv_dip_assassination_event.100` → chain `.101`
  (commander pick) → `.102` (victim pick) → `.103`. Flavor loop: fire any of
  `.110`–`.129`. Force outcomes: `.198` success (target character dies) / `.199` failure.
- Cleanup check: after resolution, `tweak` should show `active_assassination` and
  `ongoing_plans` gone, and the commander un-busied.

### Steal Commander (v4.0)
- Pact, then `event adv_dip_event.131`. Option A: **verify the named commander appears
  on your military roster** (`transfer_character` — vanilla-unprecedented on
  commanders, priority check), pact auto-removes, `recently_stole_commander` set
  (60 mo; visible in `tweak`). Detection is 1-in-3 → `.132` at the target with
  `recent_defection_modifier`.
- Option B: no transfer, you get the military tech-spread modifier, pact persists.
- Edge case: target with zero eligible commanders — pact should invalidate.

### Sabotage Recruitment (v4.0)
- Pact, then `event adv_dip_event.41` → fund it → `.42` lands on the target with the
  conscription/training debuff; target's option A adds lower-strata radicals.

### Develop Nation
- Pact on a decentralized/minor target, `event adv_dip_event.110` → journal entry with
  progress bar appears **with the target attached** (tooltips must name the country —
  they read the JE target, not a stale event scope). Buttons cost `development_funding`
  (from `development_target_var`) — verify a nonzero cost months after the start event.
- Force the ending: complete → `.111` (recognition + relations + obligation +
  gratitude/prestige modifiers); fail by breaking the pact → `.112`. Both must clear
  `ongoing_development` and `development_target_var` in `tweak`.

### Naval Intelligence Network (v4.0 flagship)
- Pact (target needs `navy_size >= 5`), then `event adv_dip_event.140` → JE with
  Infiltration/Exposure bars. Flavor: fire `.141`–`.146` and watch the bars move per
  their options. Buttons: Fund Informants (+2 progress, cost, 6-mo cooldown), Burn
  Contacts (−3 risk/−1 progress, 12-mo cooldown).
- Capstone: `event adv_dip_event.148` — option A codes modifier; option B **(needs The
  Great Wave + target flagship)**: target navy takes the `humiliated_navy_modifier`
  readiness/supply/prestige debuff (`damage_ship_percent` turned out not to exist —
  the error.log remediation replaced it); option C landing-charts modifier.
- Exposure: `event adv_dip_event.149` → −30 relations, `exposed_spy_ring_modifier`.
- All endings: pact removed, `recently_ran_naval_intel` (36 mo) in `tweak`.

### Steal Ship Designs (v4.0)
- Needs target `naval_combat_power` above yours. `event adv_dip_event.135` → option A:
  construction-efficiency + tech-spread modifiers, 1/6 detection → `.136` at target.
- Invalidation: build your navy past theirs — pact should self-cancel.

### Fund Piracy (+ corsair option)
- Pact, `event adv_dip_event.101` → option A classic; **option B only visible with The
  Great Wave**: `corsair_patron_modifier` (a cut of real piracy income — check the
  budget screen), higher cost, extra −5 relations. `.102` gives the victim the piracy
  JE with its four counterplay buttons.

### Blackmailed Concession (v4.0 treaty article)
No console shortcut — test through the treaty UI:
1. Without any espionage pact on the target: article visible (esp. lvl ≥ 4) but **not
   ratifiable** — tooltip should show the dossier requirement.
2. With any espionage pact: ratifiable; AI target noticeably more willing (+40 accept).
3. **The collapse check:** after ratifying, cancel the underlying espionage pact and
   let 1–2 weeks tick — the article must withdraw itself (`non_fulfillment`).

### v4.1 Shadow War recipes
- **Pipeline:** pact on a country at war, `event adv_dip_event.150` three times → `.151`
  should reach their enemy, then `.152`'s ultimatum reaches you. Peace out the war →
  `.153` payoff (obligation + prestige).
- **Turned networks:** as a high-espionage victim, take option c on `.12`/`.82`/`.92`;
  as the spymaster confirm dice now route to `.163` (fake success) and the yearly
  review (`event adv_dip_event.160`) can expose it.
- **Great Game:** any success option now scores; check `great_game_score` in `tweak`;
  crowning fires `.165`.
- **Sealed Train / False flags / Kompromat:** `event adv_dip_event.170` (roll),
  `.180` (dossier spend); set a patsy with the False Flag Directive action, then force
  a detection (`event adv_dip_event.91`) and confirm `.175` blames the patsy.
- **Dynamic odds:** compare monthly hit rates at institution 5-vs-1 and 1-vs-5 — the
  differential should be visibly decisive over a decade.

## Multiplayer note

`.metadata` declares `multiplayer_synchronized: true`. Console testing desyncs MP —
test in singleplayer; the *Players Only* tech-stealing rule covers all human players
in an MP session.
