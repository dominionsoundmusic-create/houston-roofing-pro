# Independent fact-check (Oct 13 2026)

**What was run.** After all 58 pages were written, ten separate fact-check sub-agents (fc1 to fc10) checked
the factual claims and cited sources on every page, plus the shared notes in src/templates/macros.html, the
town and service summaries in src/data/site.json and the checklist PDF. None of them wrote any page it
checked (pages were written by fifteen writer agents and, for the core pages and the roof repair model page,
by the coordinator). Each checker followed docs/fact-check/BRIEF.md: list every non-obvious claim (laws,
TDI and TWIA rules, permits, fees, phone numbers, storm facts, statistics, prices, code sections, utilities,
neighborhoods), verify it, then correct, soften or remove it in place, rebuild, re-run check.py,
similarity.py and grep_check.py, and log every claim. Claim-by-claim tables: docs/fact-check/fc1.md to
fc10.md.

**Method limit (read this).** In this environment web search is capped at 200 calls per turn shared by
every agent, and WebFetch and curl cannot reach outside sites. Claims were verified against search results,
usually restricted to the official domain, not by opening the page. Each checker had a fixed search budget
(20 to 32), so a claim that could not be confirmed was softened or removed rather than kept. Items marked
"kept without a search" are listed with a reason in each log: mostly INTAKE.md business facts, general
roofing practice, facts another checker had already confirmed by search in the same turn, or city office
details the writer cited to the city's own page.

| Checker | Pages | Confirmed | Corrected | Softened | Removed | Kept without a search |
|---|---|---:|---:|---:|---:|---:|
| fc1 | /, services, service areas, how it works, about, FAQ, contact, checklist, thanks pages, privacy, terms, 404, shared macros, site.json summaries, PDF | 33 | 5 | 3 | 0 | 18 |
| fc2 | roof replacement cost, roof insurance claims, do roofers need a license | 47 | 5 | 5 | 1 | 19 |
| fc3 | roof repair, replacement, leak, flashing, inspection, roof lifespan guide, storm-steps guide | 41 | 6 | 7 | 3 | 26 |
| fc4 | storm, hail, wind, emergency, commercial, flat roof, metal roofing | 22 | 6 | 5 | 3 | 24 |
| fc5 | Katy, Cypress, Richmond, Rosenberg, Sugar Land | 37 | 7 | 4 | 2 | 13 |
| fc6 | Missouri City, Stafford, Pearland, Alvin, Texas City | 41 | 6 | 7 | 1 | 19 |
| fc7 | The Woodlands, Spring, Conroe, Magnolia, Tomball | 33 | 7 | 5 | 5 | 21 |
| fc8 | Humble, Kingwood, Atascocita, Channelview, Deer Park | 31 | 15 | 4 | 2 | 14 |
| fc9 | League City, Friendswood, Webster, Seabrook | 37 | 8 | 0 | 2 | 7 |
| fc10 | Galveston, La Porte, Pasadena, Baytown | 52 | 5 | 2 | 0 | 11 |
| **Total** | **58 pages** | **374** | **70** | **42** | **19** | **172** |

17 new facts were added during the check, each verified and sourced: InterNACHI typical lifespans and the
NAHB summary on the lifespan guide, FEMA Operation Blue Roof on the emergency page, TDI's Sept 29 2026
roof-age underwriting rule announcement on the insurance guide, and local history for Deer Park,
Channelview, League City, Friendswood and Seabrook (thin pages deepened).

**Most important corrections.**
- The 2019 out-of-area contractor bill (SB 985) was not shown to have passed; pages now cite current law,
  Business and Commerce Code Chapter 58 (no payment may be required before disaster repair work begins).
- Windstorm area: in Harris County only Morgan's Point and the parts of La Porte, Pasadena, Seabrook and
  Shoreacres inside city limits and east of SH 146; TDI exempts repairs to less than 100 square feet of
  roof covering that do not touch the decking. Only the coastal-county parts of Baytown, Pearland,
  Friendswood and League City are in the area.
- Electric utility per town: Entergy Texas (The Woodlands villages in Montgomery County, Conroe),
  Texas-New Mexico Power (Texas City, Alvin, League City, Friendswood), CenterPoint Energy elsewhere.
- Hurricane Ike figures follow the National Hurricane Center report; unconfirmed hail rows from a
  compiled hail log were confirmed against NWS/SPC data or removed; a river-gauge record carried over from
  the sister site (69.18 ft) could not be confirmed and was removed.
- Phone numbers that could not be found (a Stafford department line, a Conroe permit line, a Rosenberg
  email) were replaced with verified city contacts or removed. HomeAdvisor cost ranges updated to the
  current page; the LegiScan HB 3344 URL corrected.

**Outside this repository.** fc8 found the same unconfirmed 69.18 ft gauge figure on the water damage
sister site (water-damage-restoration-kingwood-tx and -humble-tx). That repository was not edited.
