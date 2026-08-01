# Espionage Actions & Treaty Articles

## Diplomatic actions (`common/diplomatic_actions/`)

All are one-sided pacts: `is_two_sided_pact = no`, `requires_approval = no`,
`should_notify_third_parties = no`, `groups = { general }`. The `potential` gate always
includes an `institution_investment_level` check on `institution_espionage`.

| Action key | File | Tech | Esp. lvl | Pact cost | Extra gates | Fires |
|---|---|---|---|---|---|---|
| `sow_discontent` | `a01` | `labor_movement` | ≥5 | 250 | — | `adv_dip_event.11` (1/33 mo) |
| `support_nationalists` | `a02` | `nationalism` | ≥4 | 200 | rank ≥ great_power | `adv_dip_event.21` |
| `agitate_for_liberty` | `a03` | `nationalism` | ≥3 | 200 | — | `adv_dip_event.31` |
| `steal_technology` | `a04` | `rationalism` | ≥1 | 150 | target rank > minor_power; game rule `enable_tech_stealing`; target `techs_researched > root` | `adv_dip_event.91` (1/17 mo) |
| `election_interference` | `a08` | `mass_communication` | ≥4 | 250 | target has party IGs | `adv_dip_event.81` (1/3 mo, only `in_election_campaign`) |
| `fund_piracy` | `a10` | `admiralty` | ≥4 | 200 | rank ≥ minor_power | `adv_dip_event.101` |
| `support_slaves` | `a18` | `empiricism` | ≥3 | 150 | rank ≥ great_power; target < great_power | `adv_dip_event.120` |
| `assassinate_political_leader` | `a46` | `general_staff` | ≥5 | 250 | + `colonization` tech; ≥3 generals/admirals; `NOT has_variable = active_assassination`; target lacks `recent_assassination_modifier` | `adv_dip_assassination_event.100` (deterministic) |

### Shared patterns

- **Monthly dice:** `pact = { monthly_effect = { custom_tooltip = { text = <action>_monthly_effect random_list = { N = {} 1 = { root = { trigger_event = ... } } } } } }`.
- **Income bleed:** several actions add `income_transfer` to target pops (sow_discontent
  0.15, assassinate 0.1, election_interference 0.05; weighted 0.8 upper / 0.2 middle strata).
- **`should_invalidate`:** bankruptcy, decentralized target, war between the two,
  tech-lead vanishing (steal_technology), resolution reached (assassination).

## Treaty articles (`common/treaty_articles/`) — 1.9+ system

Three near-identical clones (271 lines each; they differ only in key, icon, and one
modifier line): `military_attache`, `cultural_exchange`, `send_advisors`.

Common shape: `kind = directed`, `cost = 100`, tech `empiricism`, esp. lvl ≥1,
`usage_limit = once_per_treaty`, `country_rank >= rank_value:great_power`,
`NOT has_law = law_type:law_isolationism`, `has_dlc_feature = mp1_treaties`.

- `military_attache` → target `country_military_tech_spread_mult = 0.5`
- `cultural_exchange` → target `country_society_tech_spread_mult = 0.5`
- `send_advisors` → target production tech spread
- All: `source_modifier = { country_leverage_generation_add = 5 }`;
  target also gets `country_leverage_resistance_mult = -0.25`.

**Known defect:** every article's `can_ratify` duplicate-check is hardcoded to
`has_type = send_advisors` (lines 63/75 of each file) — Military Attaché and Cultural
Exchange check for a duplicate *Send Advisors* article instead of themselves. When editing
one article, remember they are unreviewed clones: fix all three or diff them first.

Localization needs vanilla-shaped keys: `TREATY_ARTICLE_FLAG_IS_<key>_EFFECT` and
`TREATY_DRAFT_ARTICLE_FLAG_IS_<key>_EFFECT`.

## v4.0 additions & completions

| Action key | File | Tech | Esp. lvl | Cost | Notes |
|---|---|---|---|---|---|
| `sabotage_recruitment` | `a06` | `nationalism` | ≥3 | 150 | Completed: gates, war guard, full loc; events `.41`/`.42` |
| `steal_commander` | `a09` | `standing_army` | ≥2 | 150 | Completed: one-shot defection heist — `.131` transfers the actual character (`transfer_character`), asset-in-place alternative, 1/3 detection (`.132`), pact burns on success + 60-mo cooldown `recently_stole_commander` |
| `naval_intelligence` | `a11` | `battlefleet_tactics` | ≥3 | 200 | Flagship feature: deterministic `.140` start → JE mini-game → capstone `.148` (codes / flagship sabotage [ep2] / landing charts) or exposure `.149`; 36-mo cooldown |
| `steal_ship_designs` | `a12` | `ironclad_tech` | ≥2 | 150 | Requires target `naval_combat_power > root`; 1/17 dice → `.135` (construction efficiency + military tech spread), 1/6 detection `.136` |
| `develop_nation` | `a17` | — | ≥5 | 200 | Completed: JE finishes correctly; reward = recognition + 50 relations + obligation + gratitude/prestige modifiers |

`sabotage_industry` was **removed** in v4.0 (redundant with 1.13 naval mechanics).

## Blackmailed Concession (treaty article, v4.0)

`common/treaty_articles/adv_dip_blackmail.txt` — `kind = directed`, cost 50, source
pays maintenance, esp. lvl ≥ 4 to see. **Ratifiable only while the source holds any
espionage pact against the target** (the dossier); a weekly `non_fulfillment` check
withdraws the article if the network dies. Source: +10 leverage generation; target:
−50% leverage resistance. AI: target side gets +40 acceptance from the dossier, −20 if
it outranks the source. Enforceability + gunboat-acceptance integration deliberately
deferred.

## v4.1 Shadow War (see spec `2026-08-01-v4.1-shadow-war-design.md`)

New actions: `clandestine_arms_pipeline` (a13, war sponsorship with interception/
ultimatum chain, events `.150`–`.153`), `sealed_train` (a15, instant, `.170`–`.172`),
`false_flag_directive` (a16, instant, sets the patsy; detections reroute via
`.175`/`.176`). Systems: turned networks (X2 option c on `.12`/`.82`/`.92`, poisoned
generic success `.163`, yearly review `.160`/`.161`), the Great Game (JE + score
variables + `.165`/`.166`), kompromat (yearly dossiers, `.180`/`.181`), and dynamic
odds (edge-scaled factor stacks on every pact die and detection roll).
