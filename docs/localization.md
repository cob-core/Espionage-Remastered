# Localization

Standard Paradox YAML: `l_<lang>:` header, UTF-8 **with BOM**, keys as `key:0 "text"`.
Each file is 644 lines / ~85 KB.

## Language state

| Folder | File | Status |
|---|---|---|
| `english/` | `adv_dip_l_english.yml` | Canonical |
| `french/` | `adv_dip_l_french.yml` | Genuinely translated |

Only english and french ship (the de/ja/ru/es placeholder stubs were removed in v3.6 —
they had wrong filenames and `l_english:` headers and never loaded). To add a language:
`localization/<lang>/adv_dip_l_<lang>.yml`, header `l_<lang>:`, UTF-8-BOM.

## Key conventions

- **Events:** `adv_dip_event.<N>.t` / `.d` / `.f` (title/desc/flavor), options `.a`–`.g`.
  108 `adv_dip_event.*` keys, 127 `adv_dip_assassination_event.*` keys.
- **Diplomatic actions** (per action): `<action>_action_name`, `_action_propose_name`,
  `_action_break_name`, `_action_notification_name`/`_desc`,
  `_action_notification_break_name`/`_desc`, plus `<action>`, `<action>_desc`,
  `<action>_pact_desc`, `<action>_monthly_effect`.
- **Trigger tooltips** use vanilla's first/third/global triad:
  `<action>_trigger_desc_first` / `_third` / `_global`, with matching
  `_trigger_false_desc_*` and `_effect_desc_*`.
- **Scripted-effect tooltips** end `_tt` (`assassination_great_progress_tt`).
- **Treaty articles** need vanilla-shaped keys:
  `TREATY_ARTICLE_FLAG_IS_<key>_EFFECT`, `TREATY_DRAFT_ARTICLE_FLAG_IS_<key>_EFFECT`.
- **Modifiers/laws/institutions** localize by bare key
  (`sow_discontent_modifier`, `law_spy_agency`, `law_spy_agency_desc`).
- Character interpolation in options:
  `"[SCOPE.sCharacter('assassination_leader_1').GetFullName]"`.

## Notification style (since v3.6)

Target-side `_action_notification_desc`/`_break_desc` texts are recipient-relative
(vanilla style): they use `[INITIATOR_COUNTRY.GetName]` and phrase the victim as
"our" ("Agents of X have been discovered sowing discontent among our population."),
with no `TARGET_COUNTRY` dependence. JE-context keys use `[SCOPE.gsCountry('target')...]`
(the JE's real target), never event-saved scopes.
