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
| `.41`/`.42` | **Sabotage Recruitment** — cost + detection; `.42` offers endure (×2 debuff + conscript radicals) vs counter-fund |
| `.81`/`.82` | **Election Interference** — `.81` is ~680 lines: 13 near-identical per-IG branches setting `adv_loyal_government_leader` |
| `.91`/`.92` | **Steal Technology** — 3 options (production/military/society) granting `stolen_technology_*_modifier` (24 mo) + cost; 1-in-6 detection chance fires `.92` at target, −5 relations |
| `.101`/`.102`/`.103` | **Fund Piracy** — `.102` saves `piracy_target`, applies `local_piracy_modifier`, adds `adv_dip_je_pirates` to the victim; `.101.b` (ep2 only) = "Arm the corsairs": `corsair_patron_modifier` cut of real piracy income at higher cost |
| `.110`/`.111`/`.112` | **Develop Nation** — `.110` sets `ongoing_development`, saves the target as `development_target_var`, and adds the JE **with a target**; `.111`/`.112` (JE complete/fail) restore the scope from the variable and clean both variables up |
| `.120` | **Support Slaves** |
| `.131`/`.132` | **Steal Commander** — `.131` picks an eligible commander (`steal_commander_target`), options: defect (`transfer_character`, pact burns, 1/3 detection) / asset-in-place / abort; `.132` target notification + `recent_defection_modifier` |
| `.135`/`.136` | **Steal Ship Designs** — stolen construction efficiency + tech spread; 1/6 detection |
| `.140` | **Naval Intelligence start** — sets `ongoing_naval_intel` + `naval_intel_target_var`, adds JE with target |
| `.141`–`.146` | Naval intel flavor loop (clerk, signals, valet, counterintel sweep, drunken attaché, photographer) — nudge the two bars |
| `.148` | Naval intel capstone — codes / flagship sabotage (ep2, `damage_ship_percent` **runtime-unverified**) / landing charts |
| `.149` | Naval intel exposure — −30 relations, `exposed_spy_ring_modifier`, cleanup |
| `.150`–`.153` | **Pipeline** — interception (attribution +1), enemy reveal, ultimatum (comply/refuse), survivor payoff (obligation + prestige) |
| `.160`/`.161`/`.163` | **Turned networks** — spymaster's audit (edge-weighted), defender's exposure notice, generic poisoned "success" |
| `.165`/`.166` | **Great Game** — crowned / deposed |
| `.170`–`.172` | **Sealed Train** — edge-weighted roll, ferment + spark, crackdown |
| `.175`/`.176` | **False flags** — patsy blamed (with unravel roll), forgery exposed |
| `.180`/`.181` | **Kompromat** — dossier spend (disgrace/ruin/scandal), scandal fades |


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
