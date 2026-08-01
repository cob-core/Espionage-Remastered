# Architecture — Espionage Remastered

Victoria 3 mod (Workshop ID 3432409401, GitHub `cob-core/Espionage-Remastered`), v4.1.
A revival of koa's "Espionage" mod. Adds an espionage system built entirely from
vanilla-moddable primitives — **no custom GUI, no code, no vanilla file overrides by filename**.

## The core gameplay loop

**Progression gate → pact → monthly dice → event → modifier tug-of-war.**

1. **Unlock.** Research `international_relations` → enact `law_spy_agency` (new
   `lawgroup_external_security`) → adopts `institution_espionage` with
   `country_institution_espionage_max_investment_add = 5`.
2. **Gate.** Every espionage action's `potential` checks
   `institution_investment_level = { institution = institution_espionage value >= N }`.
   Institution investment (1–5) *is* the espionage tech tree:
   lvl 1 Steal Technology · lvl 2 Steal Commander (latent) · lvl 3 Agitate for Liberty,
   Support Slaves · lvl 4 Support Nationalists, Election Interference, Fund Piracy ·
   lvl 5 Sow Discontent, Assassinate, Develop Nation (latent).
3. **Pact.** Each action is a **one-sided diplomatic pact** (`is_two_sided_pact = no`,
   `requires_approval = no`, `should_notify_third_parties = no`) costing 150–250
   diplomatic capital upkeep, often plus an `income_transfer` bleed to the target's pops.
4. **Monthly dice.** The pact's `monthly_effect` wraps a `random_list` in a
   `custom_tooltip` — e.g. sow_discontent 1/33, steal_technology 1/17,
   election_interference 1/3 (only while `in_election_campaign`). Assassination fires
   deterministically, gated on `NOT has_variable = ongoing_plans`.
5. **Event pair.** Initiator gets event `X1` (pays a GDP-scaled cost modifier, gains the
   benefit); target gets `X2` (debuff, notification, relations hit). Events find the pact
   holder via `has_diplomatic_pact = { who = prev type = <action> }` scans.
6. **Mini-game layer.** Assassination / piracy / development escalate into journal
   entries with scripted buttons, `on_monthly_pulse` flavor-event tables, and opposed
   progress bars (progress vs risk, first to 8 resolves).
7. **Teardown.** Every pact has `should_invalidate` (bankruptcy, war, decentralization,
   resolution reached) so networks self-cancel.

## Content inventory

| System | Files | Content |
|---|---|---|
| Institution | `common/institutions/adv_dip_institutions.txt` | `institution_espionage` — the central resource |
| Laws | `common/law_groups/`, `common/laws/` | `lawgroup_external_security`, `law_no_external_security`, `law_spy_agency` |
| Diplomatic actions | `common/diplomatic_actions/aNN_*.txt` | 16 actions (v4.1 adds clandestine_arms_pipeline, sealed_train, false_flag_directive) |
| Treaty articles | `common/treaty_articles/` (4 files) | Military Attaché, Cultural Exchange, Send Advisors, **Blackmailed Concession** (espionage-network-gated, self-collapsing) |
| Journal entries | `common/journal_entries/`, `journal_entry_groups/` | `je_group_espionage`: assassination, pirates, development, naval intelligence, **the Great Game** |
| Scripted buttons | `common/scripted_buttons/` (10 files) | Piracy ×4, development ×4, naval intel ×2 (fund informants / burn contacts) |
| Progress bars | `common/scripted_progress_bars/` | assassination progress/risk (0–8), development (0–100), naval intel infiltration/exposure (0–10) |
| Scripted effects | `common/scripted_effects/` (3 files) | assassination + naval-intel bar mutators, Great Game scoring/leadership, cleanup effects |
| Script values | `common/script_values/adv_dip_values.txt` | GDP-scaled cost engine (see `economy.md`) |
| Static modifiers | `common/static_modifiers/adv_dip_modifier.txt` | ~60 modifiers: cost sinks, effect debuffs, flavor |
| Modifier types | `common/modifier_type_definitions/` | 3 custom types for the institution |
| Game rules | `common/game_rules/adv_dip_game_rules.txt` | `espionage_event_cost` (low/med/high), `espionage_tech_stealing` (on/off) |
| On-actions | `common/on_actions/adv_dip_onactions.txt` | appended hooks: secession payoff, yearly espionage pulse (Great Game decay, kompromat, turned-network reviews) |
| Ideologies | `common/ideologies/adv_dip_ig_ideologies.txt` | `INJECT:` patches adding law-group stances to 7 vanilla ideologies |
| Catalysts | `common/diplomatic_catalysts/` | `catalyst_pact_formed` — not yet wired to espionage pacts (TODO) |
| Defines | `common/defines/adv_dip_defines.txt` | One live override: `NPolitics.SECESSION_WEEKLY_BASE_CHANCE = 0.01` |
| Events | `events/` (2 files, ~4,700 lines) | See `events.md` |
| Localization | `localization/` (english + french) | See `localization.md` |
| Art | `gfx/interface/icons/` | 23 .dds (lens toolbar + treaty article icons); everything else reuses vanilla paths |

## Naming conventions

| Element | Convention | Example |
|---|---|---|
| File prefix | `adv_dip_` (legacy "advanced diplomacy" identity) | `adv_dip_values.txt` |
| Action files | `aNN_<action>.txt` — numbered, not contiguous | `a46_assassinate.txt` |
| Event namespaces | `adv_dip_event`, `adv_dip_assassination_event` | `adv_dip_event.91` |
| Event pairing | initiator `X1`, target `X2` | `.91`/`.92` |
| Journal entries | `adv_dip_je_<topic>`; group `je_group_espionage` | `adv_dip_je_assassination` |
| Scripted buttons | `je_<verb>` | `je_garner_influence` |
| Static modifiers | `<action>_modifier`; costs `<thing>_cost_modifier` | `spy_network_cost_modifier` |
| Script values | `spy_cost_multiplier_<size>` | `spy_cost_multiplier_medium` |
| Scripted effects | `assassination_<magnitude>_<progress\|risk>_effect` | `assassination_great_progress_effect` |
| Saved scopes | `spy_target_country`, `piracy_target`, `development_target`, `assassination_leader/_target` | |
| Variables | `active_assassination`, `ongoing_plans`, `ongoing_development`, cooldowns `recently_*`, character tags `*_var` | |
| Loc tooltips | suffix `_tt` | `assassination_costs_tt` |

There is **no** `ER_`/`esp_` prefix; identifiers are bare descriptive names. New content must
follow `adv_dip_` file naming to stay conflict-free.

## Load-order & override posture

- No file matches a vanilla filename — everything merges additively.
- The only by-key vanilla touches: ideology `INJECT:` patches and the single define override.
- v4.0 dissolved `TODO/` — every action is intentional and live. Disable content by
  removing it, never by moving it to a subfolder (subfolders are loaded recursively).
