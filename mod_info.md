# Espionage Remastered
[Link to Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3432409401)  

## Latest Changelog (v5.0 — Operatives)
+ ESPIONAGE IS NOW SECRET. Operations no longer create diplomatic pacts, so nothing appears in anyone's diplomacy panel and targets receive no notification. The only way anyone learns of your work is if your agents are caught.
+ NEW: Operatives — recruit named spies with tradecraft traits from the Shadow War journal entry. Every operation asks which operative to send and cannot run without one; the matching specialist raises the monthly odds (cryptographers steal technology, saboteurs wreck recruitment, and so on); a failed assassination risks the operative's capture or execution; debriefing an idle agent feeds the Shadow War score.
+ NEW: The Intelligence Console — a custom panel in the Shadow War journal entry: portraits, an appointable (and dismissable) Director of Intelligence with a service-wide bonus, the roster with live status (available / on assignment / captured), hire-and-fire buttons, and every active operation with its target's flag and a wind-down control.
+ Fund Black Market Slavery retargeted — the slave-import modifier (renamed adv_dip_black_market_modifier) now applies to the initiator; slavery-law requirement moved from target to root; the modifier persists until the last black-market route stops; a14's hidden selectable block removed.
+ Clandestine Arms Pipeline success ping — monthly rolls split into a delivery event (.157: minor score, +5 relations with the client) and the interception gauntlet (.150).
+ Election interference redesign — backing a party grants momentum_large (stacking with monthly operation hits) instead of set_ruling_party; no relations cost, no target-visible modifier, no target-side event; 15% discovery per backing fires a target event with adv_dip_tainted_election_modifier (−10 legitimacy, +radicalism, 24 mo), radicals, −30 relations, and the flip-agent option; event .82 and the overthrown/suppress-government modifiers removed.
+ Directors with teeth — the Director of Intelligence is hired to a vacant post (Recruit Director button); firing one angers their interest group (−2 approval, 24 months) and risks a 25% defection to a hostile power that rolls up one of your networks. Election interference now uses a console ballot section listing every active party in the target country. Operation upkeep rescaled to 0.02/0.04% of target GDP monthly; total agency budget shown atop the console; taller, full-width character rows; the repatriation article is now visible in the article browser (scoped visibility never matched); False Flag Directive appears in the lens again; Fund Black Market Slavery got its icon.
+ Console polish — bounded rows (no more overflow), per-operative tier and wage, per-operation upkeep with the assigned agent's portrait, and an institution tooltip listing the operations unlocked at each investment level.
+ NEW: Careers and wages — operatives gain experience tiers (Seasoned/Veteran/Master Spy) from time on assignment, shown as traits in the console; each tier raises operation odds (+15/30/45%), veterans halve capture risk, masters never talk under interrogation, and wages scale accordingly. All espionage costs now charge the treasury directly (no more public cost modifiers revealing operations); the console shows the monthly budget. The recruit popup event is gone — the console button hires directly.
+ NEW: Counterespionage coups — detection events offer "Move against their agent" (success odds by espionage edge): leave them in place as a turned network, parade them (infamy, relations, capture), or jail them quietly (capture, ransom leverage); failure lets the agent escape but still rolls up the network.
+ NEW: Prisoners and ransoms — capture records the captor; held operatives face yearly interrogation (captor gains Shadow War score, 25% chance a network against them is rolled up); the Operative Repatriation treaty article buys them back (captor AI demands compensation); disavowal or a five-year wait are the alternatives.
+ NEW: Three additional External Security laws — Consular Intelligence (early, limited), Directorate of State Security (inward-facing counterespionage), and Deniable Assets (private networks, less infamy).
+ Removed Steal Ship Designs.
+ The Shadow War journal entry (formerly The Great Game) is now pinned by default.
+ NOTE: v5.0 is not save-compatible with earlier versions; please start a new campaign.

## Previous Changelog (v4.1 — Shadow War)
+ NEW: Clandestine Arms Pipeline — covertly bankroll a belligerent's war without joining it; run the blockade gauntlet, survive the ultimatum when named, and collect an obligation from the survivor.
+ NEW: Turned Networks — victims with superior espionage can secretly turn sow-discontent, election and tech-theft networks: the spymaster keeps paying while receiving nothing (or poisoned technology); counterintelligence reviews eventually smell the rot.
+ NEW: The Great Game — a global intelligence scoreboard; every operation scores, scores decay, and the leading service holds Master of the Great Game.
+ NEW: The Sealed Train — smuggle a revolutionary into a rival power: massive radicalism surge and possible spark, or a border arrest that rallies their loyalists.
+ NEW: False Flag Directive — route detections through a patsy of your choice; if the forgery unravels, both powers turn on you.
+ NEW: Kompromat — active networks compile dossiers on enemy commanders: disgrace them for a year, end their career, or humiliate their government.
+ NEW: Fund Black Market Slavery — covertly finance the contraband slave trade supplying a slaver power, doubling vanilla's import ceiling, with suppression-squadron interceptions, abolitionist backlash, and a lobby game rule to disable it.
+ NEW: Dynamic odds — every operation's monthly success odds now scale with the espionage institution differential, fulfilling the long-standing community suggestion.
+ Fund Piracy removed — superseded by the 1.13 naval piracy mechanics and the new espionage systems.
+ Fixed a bug as old as the mod: running operations against multiple countries at once could resolve events against the wrong target — each operation now carries its own target through its event chain.
+ Post-test polish: vanilla lens icons for the new actions, hover effect descriptions, Smuggle Revolutionary rename, journal entries correctly country-scoped, and a full error.log cleanup.

## Previous Changelog (v4.0 — Completion & The Great Wave)
+ NEW: Naval Intelligence Network — an assassination-style journal-entry operation: infiltrate an admiralty, balance Infiltration against Exposure through flavor events and buttons, then choose your coup: crack their codes, cripple their flagship (The Great Wave), or copy their coastal surveys.
+ NEW: Blackmailed Concession treaty article — an intelligence dossier (any active espionage pact) compels the target's cooperation; the article collapses if your spy network is rolled up.
+ Steal Commander completed — true defection via character transfer, with its own event chain, an asset-in-place alternative, and a five-year cooldown. No longer fires the Steal Technology placeholder.
+ Sabotage Recruitment completed — espionage gate, full localization (it had none), conscript unrest.
+ Develop Nation completed — sweetened ending: recognition plus relations, an obligation, gratitude and prestige rewards.
+ Fund Piracy reworked — victim modifiers re-expressed with real 1.13 effects (port throughput, power-projection prestige); with The Great Wave, a new "Arm the corsairs" option pays you a cut of real piracy income.
+ Sabotage Industry fully removed (redundant with 1.13 naval mechanics).
+ Fixed two more invalid modifier types (navy offense, icon paths) and added a reference-integrity checker to the release process.
+ Technology Stealing game rule gains a 'Players Only' setting — humans may steal technology, the AI never will.
+ Removed the dead Fund Armaments remnants (orphaned events, malformed modifiers); fixed all remaining legacy modifier types, scripted-button AI weights, event AI weights, missing default options, and — significantly — the original treaty articles' misplaced war-goal blocks, whose enforcement was silently dead.
+ Error.log remediation: modernized every 1.13-invalid token the first real launch exposed — pact auto-cancel logic (dead since the treaty rework) now uses requirement_to_maintain; character role and ruler triggers, income triggers, and journal pinning fields renamed; flagship sabotage re-expressed with real effects; on_secession_start made compatibility-safe.

## Previous Changelog (v3.6 — Stabilization)
+ Fixed 32 modifiers that silently never parsed (missing `=`), restoring all assassination-flavor, piracy, development, and stolen-technology modifiers.
+ Fixed the espionage cost game rule never applying — its options were also silently unparsed. Low/Medium/High cost settings now work for the first time.
+ Fixed Develop Nation: the journal entry was hijacked by a misnamed duplicate, read the wrong progress bar, and lost its target country between events. It now has a proper JE target and completes/fails correctly.
+ Fixed the development buttons' funding cost (previously computed from a scope that no longer existed).
+ Fixed Military Attaché and Cultural Exchange checking for a duplicate *Send Advisors* article instead of themselves.
+ Fixed Support Slaves silently skipping its port-state selection.
+ Fixed the espionage-network duplicate-prevention triggers (`ongoing_development` guard) which never worked due to an unset scope.
+ Fixed target-side notifications reading as if the *victim* were the spy — texts are now written from the recipient's perspective.
+ Fixed a syntax error in Election Interference's invalidation trigger and a stray token in the assassination chain.
+ Defined the missing counter-piracy button cost value (buttons previously applied a cost of nothing).
+ Removed the placeholder "Comet Sighted" event, an unrelated hidden landlocked-subject independence event, and non-loading localization stubs (de/ja/ru/es).
+ Converted the ideology override to an `INJECT:` patch — greatly improves compatibility with politics mods.
+ Metadata now declares a stable mod id and supported game version 1.13.*.

## Known Issues & Bugs
+ Election Interference may not auto-end if the country removes voting.
+ AI does not make any specific decision regarding election interference, its choice of party is random.  

## Changes in Victoria 3 1.9+
+ Some actions have now been converted into treaty articles.


## To-Do 
### Current Goals
+ Incorporate diplomatic catalysts.
+ Write assassination success/failure to notify the target country.
+ Flesh out Agitate for Liberty with journal entries and buttons.
+ Add liberty desire to Agitate for Liberty.
+ Flesh out Sow Discontent.
+ Election Interference auto-end when voting is removed; targeted AI party choice.
+ Add loading screen tips.
+ Real lens icons for Naval Intelligence and Steal Ship Designs (placeholders reuse existing art).
+ In-game verification of the ep2-gated paths (flagship sabotage, corsair patronage) — DLC now installed, pending a play-test.

### Long-Term Goals
+ Create a custom GUI.
+ Hide espionage actions.
+ Merge 'New Frontiers: A Colonization Helper' into the mod.

### Community Suggestions
+ ~~Level of Espionage institution affects outcome of diplomatic actions.~~ **Shipped in v4.1 as dynamic odds.**

## Contributers
> cob
