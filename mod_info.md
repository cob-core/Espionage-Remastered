# Espionage Remastered
[Link to Workshop](https://steamcommunity.com/sharedfiles/filedetails/?id=3432409401)  

## Latest Changelog (v3.6 — Stabilization)
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
### Current Goals (v4.0 — Completion)
+ Finish and officially ship the four TODO/ actions (Sabotage Recruitment, Sabotage Industry, Steal Commander, Develop Nation).
+ Incorporate diplomatic catalysts.
+ Write assassination success/failure to notify the target country.
+ Flesh out Agitate for Liberty with journal entries and buttons.
+ Add liberty desire to Agitate for Liberty.
+ Flesh out Sow Discontent.
+ Election Interference auto-end when voting is removed; targeted AI party choice.
+ Rework Fund Piracy onto the 1.13 naval piracy mechanics (redundant-with-vanilla features get removed, not maintained).
+ Add loading screen tips.

### Long-Term Goals
+ Create a custom GUI.
+ Hide espionage actions.
+ Merge 'New Frontiers: A Colonization Helper' into the mod.

### Community Suggestions
+ Steal Commander events, localisation, and action.
+ Develop Nation events and action.
+ Level of Espionage institution affects outcome of diplomatic actions.

## Contributers
> cob
