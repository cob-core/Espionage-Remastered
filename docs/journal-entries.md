# Journal Entries, Buttons & Progress Bars

Group: `je_group_espionage` (`common/journal_entry_groups/adv_dip_journal_entries.txt`).
All JEs: `weight = 200`, `transferable = no`, `should_be_pinned_by_default = yes`.

## Assassination (`adv_dip_je_assassination`) — the flagship mini-game

- Two opposed bars from `common/scripted_progress_bars/adv_dip_progress_bars.txt`:
  `assassination_progress_bar` (0→8, green, success track) and
  `assassination_risk_progress_bar` (0→8, bad, exposure track).
- `on_monthly_pulse` runs a ~20-entry weighted `random_events` table (weight 40 = nothing)
  of flavor events (`adv_dip_assassination_event.110`–`.135`) that nudge the bars via the
  scripted effects in `common/scripted_effects/adv_dip_assassination_effects.txt`.
- `complete` (progress ≥ 8) → `.198` success: `kill_character` on the target,
  `modifier_successful_assassination` (+10% influence, +25 prestige, 13 mo decaying),
  pact removed, target gets `recent_assassination_modifier` + `add_radicals = 0.2`.
- `fail` (risk ≥ 8, or pact/variable lost) → `.199`: `modifier_failed_assassination`
  (−10% influence, −25 prestige), same cleanup.
- Cleanup is centralized in `remove_assassination_events_effect`: removes
  `active_assassination`, `ongoing_plans`, `assassination_cost_modifier`, un-busies the
  leader character, clears `assassination_leader_var`/`assassination_target_var`.
  **Always route teardown through this effect** — never clean up piecemeal.

### Scripted-effect roster (all follow guard-mutate-tooltip)

```
assassination_great_progress_effect = {
    if = {
        limit = { has_journal_entry = adv_dip_je_assassination }
        je:adv_dip_je_assassination ?= {
            add_progress = { value = 4 name = assassination_progress_bar }
        }
    }
    custom_tooltip = assassination_great_progress_tt
}
```

Progress: `assassination_minor/moderate/great_progress_effect` (+1/+2/+4),
`assassination_lose_progress_effect` (−1), `assassination_success` (+10 → forces complete).
Risk: `add_small/medium/large_assassination_risk_effect` (+1/+3/+5),
`assassination_risk_decrease_small/medium_effect` (−1/−2),
`assassination_failure` (+10 → forces fail).

## Piracy (`adv_dip_je_pirates`)

Added to the **victim** by `adv_dip_event.102`. No progress bar; completes when the
`fund_piracy` pact ends. Four scripted buttons, cooldown variable
`recently_fought_pirates` (6 mo):
`je_disrupt_pirates`, `je_extort_subjects`, `je_add_port_security`, `je_modernise_ports`.

## Development (`adv_dip_je_development`)

Added by `adv_dip_event.110` **with `target = scope:development_target`** (sets
`ongoing_development` and `development_target_var`); `on_complete`/`on_fail` are
`.111`/`.112`, which clean up both variables. Declares `scripted_progress_bar = development_progress_bar` (0→100,
`monthly_progress` +3/mo while relations > `relations_threshold:poor`). Four buttons,
cooldown `recently_developed_country` (7 mo), cost value `development_funding`:
`je_expand_infrastructure`, `je_share_technologies`, `je_encourage_settlers`,
`je_garner_influence`.

Fixed in v3.6: complete reads `development_progress_bar >= 100`; fail is pact-loss
only (checked against `scope:target`); the misnamed duplicate JE file was deleted.

## Scripted-button template

All 8 buttons are structurally identical — cooldown variable + benefit modifier + cost
modifier:

```
je_disrupt_pirates = {
    name = adv_dip_je_pirates_disrupt
    visible = { always = yes }
    ai_chance = { base = 5  modifier = { trigger = { bureaucracy > 0 } add = 5 } }
    possible = { not = { has_variable = recently_fought_pirates } }
    effect = {
        set_variable = { name = recently_fought_pirates months = 6 }
        add_modifier = { name = piracy_disruption_modifier months = 24 }
        add_modifier = { name = piracy_cost months = 13 multiplier = piracy_cost_multiplier }
    }
}
```

`piracy_cost_multiplier` is defined in `adv_dip_values.txt` as of v3.6 (0.015% own GDP).

## Naval Intelligence (`adv_dip_je_naval_intelligence`, v4.0)

Added by `.140` with `target =`; two bars (`naval_intel_progress_bar` 0→10 green,
`naval_intel_risk_bar` 0→10 bad); monthly table (weight 30 quiet) over `.141`–`.146`;
buttons `je_fund_informants` (+2 progress, cost `naval_intel_funding` from
`naval_intel_target_var`, 6-mo cooldown) and `je_burn_contacts` (−3 risk −1 progress,
12-mo cooldown; AI rushes it at risk ≥ 6). Complete (≥10) → `.148` capstone choice;
fail (risk ≥10 or pact gone) → `.149`. Cleanup centralized in
`remove_naval_intel_effect` (vars + pact + 36-mo cooldown) — never tear down piecemeal.
Scripted effects live in `common/scripted_effects/adv_dip_naval_intel_effects.txt`.

## The Great Game (`adv_dip_je_great_game`, v4.1)

Permanent JE for any country with the Spy Agency law. Scores live in
`great_game_score` (country variable, +1 minor / +3 major via the shared scoring
effects, ×0.9 yearly decay); `global_var:great_game_leader` holds the current Master
(`master_of_the_great_game_modifier`), swapped by the leadership-check effect with
crowned/deposed events `.165`/`.166`.
