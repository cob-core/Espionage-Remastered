# Known Issues & Defect History

## Fixed in the error.log remediation (2026-08-01, first real launch)

The 01:23 launch produced 155 mod-related error lines. Fixed:
1. **`should_invalidate` / `should_auto_break` do not exist in 1.13** — every pact's
   auto-cancel logic was silently dead. All 13 actions converted to
   `requirement_to_maintain = { trigger = { NOT = {...} } }` (a17/a18's warning blocks
   became `show_about_to_break_warning`).
2. **`has_role = general/admiral` fails PostValidate** (1.13 role rework) → 16 sites
   renamed to `has_role_of_type`; commander selection in assassination and steal
   commander was broken without this.
3. **`is_ruler` unknown** → `is_ruler_of_own_country` (5 sites).
4. **`weekly_net_fixed_income` unknown** (1.12 rename) → `fixed_net_income` (5 sites).
5. **`should_be_pinned_by_default` renamed** → `_involved` variant (4 JEs).
6. **`damage_ship_percent` is not a real effect** (effect-loc entry only) — flagship
   sabotage now applies `humiliated_navy_modifier` (prestige + readiness + supply
   debuffs) instead.
7. Blackmail article: `unlocking_technologies` → `unlocked_by_technologies`; invalid
   `category` ai field removed.
8. `is_decaying` invalid in static modifier definitions → moved to the `.111`
   `add_modifier` call site (valid there).
9. `on_secession_start` `effect` blocks don't merge with vanilla's — ours moved to an
   appended `adv_dip_secession_hook` on_action (compat fix).
10. Dead pre-1.12 law-group fields (`progressive/regressive_movement_chance`) removed.
11. Missing `adv_dip_je_expand_infrastructure(_desc)` button loc added (en+fr).
12. Checker now bans all error.log-proven legacy tokens.

## Remaining runtime checks

1. Blackmail article AI acceptance and the `non_fulfillment` weekly check.
2. `transfer_character` on a commander (vanilla uses it on IG leaders/agitators).
3. Re-launch and confirm the error.log deltas are gone; `.120` orphan warning should
   clear now that a18 parses fully.

## Known legacy errors NOT yet fixed (need a scoping decision)

1. **Fund Armaments cluster is dead code**: no action defines the `fund_armaments`
   pact type, events `.64`–`.66`/`.71` are orphaned, `.64` uses the removed
   `create_trade_route` effect, and its two modifiers use a script value as a
   magnitude ("Malformed token") plus removed `building_output_*_mult` types.
   Recommend full removal (same principle as Sabotage Industry) or a rebuild.
2. `sow_discontent_modifier` still carries `state_radicals_from_discrimination_mult`
   (removed in the 1.10 discrimination rework) — needs a modern replacement choice.
3. `suppress_government_modifier` region uses removed `country_party_whip_impact_mult`.
4. Event-option `ai_chance` blocks using `modifier = { add = ... }` log "unknown
   command 'add' for MTTH" (~25 sites, election interference + support nationalists) —
   the AI ignores those weights; needs a rewrite to the supported form.
5. ~15 events lack a `default_option = yes` (warnings only).

### ep2 console test checklist
`event adv_dip_event.148` on a country with an active naval-intel JE against a
flagship-owning navy → pick option b, confirm the flagship takes damage and no
error.log entries; `event adv_dip_event.101` → option b visible, corsair modifier
applies; ratify a Blackmailed Concession with and without an active espionage pact.

## Open

1. Election Interference may not auto-end if the country removes voting.
2. AI makes no specific decision on election interference; party choice is random.
3. Assassination success/failure does not notify the target country (roadmap).
4. `catalyst_pact_formed` exists but is not wired to espionage pacts (roadmap).
5. New lens icons for naval_intelligence / steal_ship_designs are placeholder copies.

## Fixed in v3.6 (2026-07-31) — kept as history

All verified fixed; static gates pass. In-game confirmation via the release gate
(deploy → `-debug_mode` → error.log → console-fire events).

1. **Duplicate JE key** — `adv_dip_je_sow_discontent.txt` declared a second, broken
   `adv_dip_je_development` (nonexistent buttons, piracy events on complete/fail).
   *Fixed: file deleted.*
2. **Wrong progress bar** — development JE read
   `scripted_bar_progress(assassination_progress_bar)`; its `= 0` fail check would
   also have failed instantly. *Fixed: complete reads `development_progress_bar >= 100`;
   fail is pact-loss only.*
3. **Transient target scope** — `development_target` was saved with `save_scope_as`
   (event-lifetime) but read months later by JE loc and `development_funding`.
   *Fixed: JE now gets a real `target =`; loc uses `gsCountry('target')`; the initiator
   carries `development_target_var`, cleaned up in `.111`/`.112`.*
4. **`scope:root_country` never set** — the dedup triggers of `.110`–`.112` and
   `.120`'s port-state selection silently no-opped. *Fixed: direct scope checks /
   `root`.*
5. **Malformed guard in a17** — empty-bodied `IF` let `.110` re-fire during ongoing
   development. *Fixed: proper `if = { limit = { ... } ... }`.*
6. **Game-rule options never parsed** — all five options in
   `adv_dip_game_rules.txt` were missing `=`, so the espionage cost setting and
   tech-stealing toggle checks never matched. *Fixed.* (Same defect class as the 32
   static modifiers fixed in the same release.)
7. **Undefined script values** — `piracy_cost_multiplier` (5 call sites) now defined
   (0.015% own GDP); `counter_piracy` removed from `development_funding` (redundant
   with 1.13 naval piracy — per project principle, redundant features are removed).
8. **Treaty-article clone bug** — Military Attaché / Cultural Exchange `can_ratify`
   checked `send_advisors`. *Fixed to self-checks.*
9. **Stray `c` token** in `adv_dip_assassination_event.103`; **`NOT {` missing `=`**
   in `a08` `should_invalidate`; **`cancellation_trigger {`** missing `=` in `.81`;
   **`NOT {`** missing `=` in `.82`. *All fixed.*
10. **Inverted notifications** — target-side `_action_notification_desc` texts
    rewritten recipient-relative (vanilla style, no `TARGET_COUNTRY` dependence).
11. **Dead content removed** — "Comet Sighted" stub event + empty game concept +
    yearly random_events hook; unrelated landlocked-subject independence event
    (`adv_dip_separate_events`); de/ja/ru/es placeholder loc stubs; stray `.idea/`
    copies; seven inert vanilla doc copies.
12. **32 silently unparsed static modifiers** (missing `=`) and the wholesale ideology
    override (now `INJECT:` patches) — committed from the pre-existing working tree.
13. **Metadata** — id `com.github.cob-core.espionage-remastered`, version 3.6,
    supported_game_version `1.13.*`.

## Lesson encoded

Paradox script fails silently: `foo {` instead of `foo = {` drops the block with no
error at load. The `grep -rnE '^\s*[a-zA-Z_]+ \{' common/ events/` gate is mandatory
before any release — it caught three separate defect families in this release alone.
