# Espionage Remastered
[Link to Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3432409401)  

## Latest Changelog (v4.1 — Loose Ends)
+ Owner-side notifications for every operative fate: captured (captor named when known), executed, or escaped home after a failed counter-intelligence move.
+ Target-side assassination notifications: a successful plot is recognised as murder, a foiled plot is announced — the sponsor stays unnamed.
+ Steal Technology requires the target to lead in total technologies (visible tooltip); reaching parity mid-operation recalls the agent with a "Nothing Left to Steal" event instead of ending silently.
+ Director of Intelligence bonus is permanent while seated — no monthly re-application or countdown.
+ External Security laws re-laddered: Consular Intelligence (International Relations), Spy Agency (Central Archives), Directorate of State Security (Identification Documents), Deniable Assets (Political Agitation). Enacted laws are kept.
+ AI election interference backs an opposition party (falls back to any party only when the whole slate is in government).
+ Clandestine Arms Pipeline defiance payoff is judged at wind-down, only if the recipient survived the war intact.
+ Kompromat: disgraced commanders are released after twelve months even if the scheduled release event is lost.
+ Naval Intelligence Network lens icon replaced (was a copy of Sow Discontent's).
+ Removed the pact-formed diplomatic catalyst, unreachable since pacts were removed.
+ Save-compatible with 4.0.

## Previous Changelog (v4.0 — Operatives)
+ ESPIONAGE IS NOW SECRET. Operations no longer create diplomatic pacts and no cost modifiers reveal your spending: everything charges the treasury directly, and targets learn nothing until agents are caught.
+ NEW: Operatives — named agents with tradecraft specialties (cryptographer/saboteur/master of disguise/silver tongue) carry out every operation; each launch asks who goes and requires someone free. Experience tiers (Seasoned 1yr / Veteran 3yr / Master Spy 6yr) raise odds (+15/30/45%), halve capture risk (Veteran+), and grant interrogation immunity (Master).
+ NEW: The Intelligence Console — roster with portraits, live status and wages; Director of Intelligence (promoted from the ranks; firing one angers their interest group and risks a 25% defection); operations with per-row cost and agent portrait; total agency budget; election ballots; sealed-train manifest; false-flag row with cancel.
+ NEW: Wages follow the government wage level (×0.7 very low … ×1.4 very high). At Low, idle operatives risk 6%/year defection; at Very Low, 12%. The buyer chooses: pay for the dossier (ALL networks against them rolled up), pay-and-poach (agent joins their roster; requires an espionage law), or refuse (50% the spymaster catches the traitor coming home — cashier them or pay their arrears).
+ NEW: Counterespionage coups — detection events offer a move against the discovered agent (odds by espionage edge): turn in place, parade publicly (infamy + capture), or a quiet cell; failure lets the agent escape but the network still rolls up.
+ NEW: Prisoners and ransoms — capture records the captor; yearly interrogation risks a network roll-up (Masters never talk); release via the Operative Repatriation treaty article, disavowal, or five-year escape. Dismissed rank-and-file operatives carry a lesser echo: 12-month grudge, 10% defection.
+ Election interference redesign — one console ballot per campaign (opens immediately if a campaign is live), monthly momentum_medium to the backed party with 8% discovery per payment; exposure closes the channel and fires scandal events both ways; victory grants major standing plus a 36-month well-disposed government (−25% leverage resistance); defeat is noted. AI picks inline.
+ Sealed train manifest — choose the passenger (real exiles, or three seeded firebrands of the target's culture) by portrait/ideology/interest group in a two-column console section; per-target 60-month route burn; sponsor result events for delivery and border arrest.
+ Fund Black Market Slavery retargeted — the import boost lands on the initiator (the buyer), gated by the initiator's slavery laws, persisting until the last route ends.
+ Clandestine Arms Pipeline success pings — delivery events alongside the interception gauntlet.
+ False Flag Directive made visible — confirmation event, console row with patsy + agent, small-network upkeep, early cancel, legible one-directive gate.
+ Kompromat dossiers can be filed away unused (safe default option).
+ NEW: Three additional External Security laws — Consular Intelligence, Directorate of State Security, Deniable Assets; the institution tooltip lists per-level action unlocks.
+ Operation upkeep scales with the target economy (0.2%/0.4% of target GDP monthly, floors £600/£1,200).
+ Removed Steal Ship Designs; Shadow War journal entry (formerly The Great Game) pinned by default.
+ NOTE: v4.0 is not save-compatible with 3.x; please start a new campaign.

## Older Changelog (v3.6 — Stabilization)
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
+ None currently tracked. Report bugs on the Workshop page or GitHub.

## Changes in Victoria 3 1.9+
+ Some actions have now been converted into treaty articles.


## To-Do 
### Current Goals
+ Flesh out Agitate for Liberty with journal entries and buttons.
+ Add liberty desire to Agitate for Liberty.
+ Flesh out Sow Discontent.
+ Add loading screen tips.
+ In-game verification of the flagship sabotage path (The Great Wave) — DLC installed, pending a play-test.

### Long-Term Goals
+ Create a custom GUI.
+ Hide espionage actions.
+ Merge 'New Frontiers: A Colonization Helper' into the mod.

### Community Suggestions
+ ~~Level of Espionage institution affects outcome of diplomatic actions.~~ **Shipped in v4.0 as dynamic odds.**

## Contributers
> cob
