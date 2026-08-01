# Known Issues & Defect History

## Runtime-unverified (v4.0, flag for first play-test)

1. `damage_ship_percent = 0.5` syntax in `.148.b` — effect exists (effect-localization)
   but has zero vanilla usages; verify in-game with The Great Wave.
2. All `has_dlc_feature = ep2_content` paths (flagship sabotage, corsair patronage) —
   statically verified only; The Great Wave is not installed locally.
3. Blackmail article AI acceptance behavior and the `non_fulfillment` weekly check.
4. `transfer_character` on a commander (vanilla uses it on IG leaders/agitators).

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
