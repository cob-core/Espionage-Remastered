# Cost Engine — Script Values, Modifiers & Game Rules

## Script values (`common/script_values/adv_dip_values.txt`)

All espionage costs scale off **target GDP**, then off the cost game rule:

```
# 0.05% of GDP, rounded to nearest 100
spy_cost_multiplier_medium = {
    value = scope:spy_target_country.gdp
    divide = 100000
    multiply = 0.25
    round = yes
    multiply = 100
    if = { limit = { has_game_rule = low_espionage_event_costs } multiply = low_espionage_event_costs_value }
    ...
}
```

| Value | % of target GDP |
|---|---|
| `spy_cost_multiplier_very_small` | 0.015% |
| `spy_cost_multiplier_small` | 0.025% |
| `spy_cost_multiplier_medium` (+ `_negative`) | 0.05% |
| `spy_cost_multiplier_large` | 0.1% |
| `spy_cost_multiplier_very_large` | 0.5% |

Others: `counterespionage_value`/`_modifier`/`_cost`, `piracy_loot_value`,
`piracy_naval_modifier` (ratio of `naval_power_projection`, clamped ~0.5×–1.5×),
`military_cost`, `send_armaments_cost`, `development_funding`, `technology_theft_cost`,
and rule constants `low/medium/high_espionage_event_costs_value` = 0.5 / 1 / 2.

`piracy_cost_multiplier` (counter-piracy button cost, 0.015% of **own** GDP — runs on
the piracy victim) was defined in v3.6; the undefined `counter_piracy` divisor was
removed from `development_funding` (redundant with 1.13 naval piracy).
`development_funding` now reads `var:development_target_var.gdp` (persistent variable,
not a transient saved scope).

## Static modifiers (`common/static_modifiers/adv_dip_modifier.txt`, ~60 defs)

- **Cost sinks** — `country_expenses_add = 1` scaled at the call site via
  `add_modifier = { name = X multiplier = <script_value> }`: `spy_network_cost_modifier`,
  `assassination_cost_modifier`, `counterespionage_modifier`, `piracy_cost`,
  `development_cost_modifier`, `stolen_technology_cost_modifier`, `armaments_cost_modifier`.
- **Effect modifiers**: `sow_discontent_modifier`, `support_nationalists_modifier`,
  `agitate_for_liberty_modifier`, `sabotage_recruitment/industry_modifier`,
  `overthrower/overthrown_modifier`, `modifier_successful_assassination` (+10% influence,
  +25 prestige) / `modifier_failed_assassination` (mirror), `recent_assassination_modifier`
  (cooldown flag), `local_piracy_modifier`, `increased_port_security`,
  `modernised_ports_modifier`, `stolen_technology_production/military/society_modifier`,
  four `development_*_modifier`s.
- **Flavor**: `cleaned_the_cat_modifier`, `paid_a_witch_modifier`,
  `blamed_for_poisoning_modifier`, `assassin_paid_off_modifier`, `rescue_mission_modifier`.

History note: half this file (everything from `armaments_cost_modifier` onward) was
silently unparsed for a long time because 32 definitions were missing their `=`
(`foo {` instead of `foo = {`). Fixed in the working tree — when adding modifiers,
the `=` is mandatory and its absence fails **silently** (check `error.log`).

## Modifier type definitions (`common/modifier_type_definitions/`)

Custom types required by the institution:
`country_institution_espionage_max_investment_add`,
`country_institution_size_change_speed_institution_espionage_mult`,
`country_institution_cost_institution_espionage_mult`.

## Game rules (`common/game_rules/adv_dip_game_rules.txt`)

- `espionage_event_cost`: `low_/medium_/high_espionage_event_costs` (default medium) —
  multiplies every `spy_cost_multiplier_*` by 0.5/1/2. (Options were silently unparsed
  until v3.6 — the rule never applied before then.)
- `espionage_tech_stealing`: `enable_/disable_tech_stealing` (default enabled) — gates the
  `steal_technology` action's `potential`.
