# Event Index

Two namespaces across `events/` (v3.6 removed `adv_dip_separate_events`). Convention: **`X1` = "hit" event on the initiator
(fired by the pact's `monthly_effect`), `X2` = notification/consequence on the target.**
Events locate the spymaster via `has_diplomatic_pact = { who = prev type = <action> }`
scans and save the victim as `scope:spy_target_country`.

## `adv_dip_events.txt` (~3,100 lines) — namespace `adv_dip_event`

| ID | Role |
|---|---|
| `.11`/`.12` | **Sow Discontent** — initiator pays `spy_network_cost_modifier` ×`spy_cost_multiplier_medium` (25 mo), −10 relations; target gets `sow_discontent_modifier` + `add_radicals = 0.05` |
| `.21`/`.22` | **Support Nationalists** — 5 branches pick a discriminated culture → `adv_nationalist_culture` |
| `.31`/`.32`/`.33` | **Agitate for Liberty** — can `create_diplomatic_play` or set `liberty_target_country` |
| `.41`/`.42` | Sabotage Recruitment (action in `TODO/`, still loaded) |
| `.51`/`.52` | Sabotage Industry (same) |
| `.64`/`.65`/`.66` | Fund Armaments family |
| `.71` | Fund Armaments variant (scans for a `fund_armaments` pact). **Steal Commander has no events** — its `monthly_effect` fires `.91` (Steal Technology) as a placeholder |
| `.81`/`.82` | **Election Interference** — `.81` is ~680 lines: 13 near-identical per-IG branches setting `adv_loyal_government_leader` |
| `.91`/`.92` | **Steal Technology** — 3 options (production/military/society) granting `stolen_technology_*_modifier` (24 mo) + cost; 1-in-6 detection chance fires `.92` at target, −5 relations |
| `.101`/`.102`/`.103` | **Fund Piracy** — `.102` saves `piracy_target`, applies `local_piracy_modifier`, adds `adv_dip_je_pirates` to the victim |
| `.110`/`.111`/`.112` | **Develop Nation** — `.110` sets `ongoing_development`, saves the target as `development_target_var`, and adds the JE **with a target**; `.111`/`.112` (JE complete/fail) restore the scope from the variable and clean both variables up |
| `.120` | **Support Slaves** |


## `adv_dip_assassination_events.txt` (~1,650 lines) — namespace `adv_dip_assassination_event`

- **Setup chain:** `.100` start (sets `ongoing_plans`) → `.101` select commander (saves
  up to 3 non-busy generals/admirals as `assassination_leader_1/2/3`; chosen one gets
  `assassination_leader_var` + `set_character_busy_and_immortal = yes`; sets
  `active_assassination`) → `.102` select target (~580 lines; tags
  `assassination_target_var`) → `.103` plot begins.
- **Flavor loop:** `.110`–`.129`, `.134`, `.135` — fired from the JE's monthly table;
  each calls scripted effects to move the progress/risk bars. (Named in JE comments:
  Sandwich Shop, INTEL-Cat, Chambermaid, Witch, Poisoned Chalice, Opera, Body Double, …)
- **Resolution:** `.198` success (kill, buffs, cleanup) / `.199` failure — both end with
  `remove_assassination_events_effect = yes`.

Option names use character interpolation:
`"[SCOPE.sCharacter('assassination_leader_1').GetFullName]"`.

## Localization key shape

`<namespace>.<N>.t` / `.d` / `.f` (title/desc/flavor) and `.a`–`.g` for options.
