# Fact-check log: fc1 (Oct 13 2026)

Checker: fc1 (did not write these pages). Searches used: 18 of 20. WebFetch/curl unavailable; verdicts rest on
search results, mostly restricted to official domains (tdi.texas.gov, twia.org, weather.gov, noaa.gov,
texasattorneygeneral.gov).

## Search evidence used (S1 to S16)
- S1 HB 3344 (89R, 2025): LegiScan and capitol.texas.gov bill history: filed Feb 25 2025 (Rep. Pat Curry), heard by House Trade, Workforce and Economic Development Apr 15 2025, committee report sent to Calendars May 8 2025, died in chamber; no floor vote. Licensing of reroofing contractors by TDLR.
- S2 TDI "Roofing and insurance: know the law", B-0008-24, B-0007-25: illegal for a contractor to offer to waive, rebate or absorb a deductible; contracts of $1,000 or more involving an insurance settlement must carry the deductible notice; contractor may not act as public adjuster on a property where it provides or may provide contracting services (Insurance Code 4102.163); public adjusters are TDI-licensed; Bus. and Com. Code 27.02.
- S3 TDI windstorm general questions, TWIA FAQ, TDI order 96-1468: catastrophe area = 14 first-tier coastal counties + in Harris County La Porte, Morgan's Point, Pasadena, Seabrook, Shoreacres, inside city limits and east of SH 146. Baytown not listed.
- S4 TDI/TWIA WPI-8: certificate of compliance for ongoing construction, required for TWIA eligibility; roof-covering repairs under 100 sq ft not involving decking are exempt.
- S5 TWIA claims page and FAQ: one year (365 days) from date of damage; 180-day good-cause extension.
- S6 Houston Permitting Center HPWCODE1140: re-roof or overlay permit, plan review and inspection; roof covering up to 100 sq ft (aggregate) exempt.
- S7 NWS HGX May 2024 Regional Climate Summary: May 16 derecho, swath of 100+ mph winds through the Houston metro.
- S8 Beryl: landfall near Matagorda about 4 a.m. July 8 2024 as Category 1; 2.2 million+ CenterPoint customers out (S&P Global, Houston Chronicle, Wikipedia).
- S9 Tex. Prop. Code 202.011 (HB 362, 2011): POA may not prohibit wind/hail resistant, energy-efficient or solar shingles that resemble those used/allowed, are at least as durable and of equal or better quality, and match the neighborhood aesthetics.
- S10 Harris County unincorporated re-roof permits: no official county statement found; only third-party guides. Montgomery County FAQ (cited on the Spring page) says residential roof replacement needs no county permit.
- S11 Sugar Land: city permit FAQ (permits online, 180-day expiry, stop-work orders); no official re-roof page found in this search.
- S12 NHC: Atlantic hurricane season June 1 to November 30.
- S13 Texas AG: Texas Data Privacy and Security Act in effect July 1 2024; rights to access, correct, delete.
- S14 TDI "five things your home policy won't cover": flood not covered by home policies; separate flood policy.
- S15 Gloeocapsa magma: dark roof streaks are algae, mainly cosmetic (ARMA cited: no evidence of direct damage).
- S16 League City in Galveston and Harris counties (mostly Galveston). S16b City of Katy at the Harris/Fort Bend/Waller tripoint.
- S17 IRC R908.3.1.1: recover not permitted over two or more existing layers. (Total: 18 searches.)

## / (src/pages/index.html)
| Claim | Verdict | Source or reason |
|---|---|---|
| Hurricane season June 1 to Nov 30 | confirmed | S12 |
| May 16 2024 derecho, swath of winds over 100 mph per NWS | confirmed | S7 |
| Beryl landfall near Matagorda July 8 2024, Category 1 | confirmed | S8 |
| More than two million CenterPoint customers without power | confirmed | S8 (2.2 million) |
| No state roofing license in Texas | confirmed | S1 (licensing bill died) |
| Contractor may not waive, rebate or absorb deductible | confirmed | S2 |
| $1,000+ insurance-paid contract must carry deductible notice | confirmed | S2 |
| Roofer may not act as public adjuster on a property it works on | confirmed | S2 (Ins. Code 4102.163) |
| "On the coast, roof work must pass a TDI windstorm inspection" | corrected | Now "In the coastal catastrophe area, most roof work must pass..."; S3, S4 (only the designated area; small repairs exempt) |
| Six counties served; 28 town pages | kept without a search | Business facts from INTAKE.md and site.json (28 areas counted) |
| Hail bruises not visible from the driveway; heat dries seals | kept without a search | General roofing description, no figure |
| Source labels (NWS PDF, Community Impact 2.2M, NHC climo, TDI x2, RCAT HB 3344) | confirmed | Labels match S7, S8, S12, S2, S3, S1 |

## /services/ (src/pages/services.html)
| Claim | Verdict | Source or reason |
|---|---|---|
| Texas law requires you to pay your own deductible | confirmed | S2 (Ins. Code ch. 707 / B&C 27.02) |
| TDI licenses public adjusters; roofer may not act as one on a property it works on | confirmed | S2 |
| Low-slope roofs use membranes/coatings, fail at seams, drains, ponding | kept without a search | General trade description |
| Symptom table (stain = leak, etc.) | kept without a search | General guidance, no facts |

## /service-areas/ (src/pages/service-areas.html)
| Claim | Verdict | Source or reason |
|---|---|---|
| Catastrophe area: all of Brazoria, Chambers, Galveston; Morgan's Point plus parts of La Porte, Pasadena, Seabrook, Shoreacres east of SH 146 | confirmed | S3 |
| Roof work there must pass windstorm inspection for TWIA eligibility; WPI-8 | confirmed | S4 (added "most roof work": sub-100 sq ft repairs exempt) |
| "a re-roof in Sugar Land or Kingwood (inside the City of Houston) is permitted and inspected, while the same job in much of Cypress or Spring is not" | corrected | Read as if Sugar Land were in Houston; Sugar Land re-roof rule not confirmed by an official source (S11). Rewritten: Houston incl. Kingwood needs a re-roof permit (S6); Montgomery County says no county permit for residential roof replacement (S10, mctx FAQ); Harris County Engineer lists no separate re-roof permit |
| "Harris County does not permit an ordinary shingle replacement" | softened | Only third-party sources (S10); now "no city permit office and the Harris County Engineer lists no separate re-roof permit" (matches the Cypress/Spring pages' sourced wording) |
| "in unincorporated county areas a shingle replacement usually needs no permit at all" | softened | Now "no city permit office at all, so the county's rules apply" |
| Windstorm section put Baytown, Pearland, Friendswood under "these counties are in the catastrophe area" | corrected | Added: these cross county lines and only their Brazoria/Galveston/Chambers parts are in the area; Baytown is not on TDI's Harris County list (S3) |
| Katy spans three counties | confirmed | S16b; source added |
| Kingwood inside City of Houston | kept without a search | Annexed 1996; covered by the Kingwood page and its fact-checker |
| The Woodlands runs on covenants rather than city permits | kept without a search | Unincorporated; covered by The Woodlands page |
| Sources added | n/a | Montgomery County permitting FAQ, Harris County OCE Permits A to Z, TWIA FAQ, City of Katy About |

## /how-it-works/ (src/pages/how-it-works.html)
| Claim | Verdict | Source or reason |
|---|---|---|
| Texas has no state roofing license | confirmed | S1 |
| Contractor may not act as public adjuster | confirmed | S2 |
| Illegal to waive, rebate or absorb deductible | confirmed | S2 |
| Line process (assistant, transfer, callback) | kept without a search | Business facts from INTAKE.md |

## /about/ (src/pages/about.html)
| Claim | Verdict | Source or reason |
|---|---|---|
| d/b/a of Dominion Digital Group; shared line | kept without a search | INTAKE.md |
| Texas does not license roofing contractors | confirmed | S1 |
| "every big Houston storm brings a wave of crews that leave when the claims run out" | kept without a search | General characterization echoed by TDI storm-chaser warnings (S2); no figure. Note for coordinator: INTAKE says "do not name an owner"; the page names the owning company (not a person), consistent with the footer. |

## /faq/ (src/pages/faq.html)
| Claim | Verdict | Source or reason |
|---|---|---|
| No Texas roofing license; 2025 bill did not pass | confirmed | S1 |
| Deductible waiver illegal; $1,000 notice | confirmed | S2 |
| Houston re-roof/overlay permit | confirmed | S6 |
| "unincorporated county areas usually do not" (permit) | softened | "often have no re-roof permit" (S10) |
| TWIA claims within one year of the storm | confirmed | S5 (one year from date of damage) |
| Codes limit how many layers | confirmed | IRC R908.3.1.1 search |
| Dark streaks usually algae, mainly cosmetic | confirmed | S15 |
| Prop. Code 202.011 | corrected | Added the statute's other conditions (at least as durable, equal or better quality, fit neighborhood look); S9 |
| Flooding generally not covered by homeowners policy | confirmed | S14; TDI source added |
| Contractor may not act as public adjuster | confirmed | S2 |

## /contact/ and /contact/thanks/
| Claim | Verdict | Source or reason |
|---|---|---|
| No email or office; assistant answers any hour | kept without a search | INTAKE.md |
| Report downed lines to CenterPoint Energy or 911 | kept without a search | CenterPoint is the Houston electric delivery utility (S8 coverage); safety rule from CLAUDE.md |
| "many roofers inspect at no charge, but policies differ" | kept without a search | Hedged general statement, no figure |
| Netlify forms intact | n/a | Not edited; check.py 0 errors |

## /hail-claim-checklist/ and /hail-claim-checklist/thanks/
| Claim | Verdict | Source or reason |
|---|---|---|
| Hurricane season June 1 to Nov 30 | confirmed | S12 |
| Texas rule against waiving deductibles | confirmed | S2 |
| Percentage deductibles, ACV vs RCV, held-back depreciation | kept without a search | General insurance mechanics, hedged ("your policy") |

## /privacy-policy.html, /terms.html, /404.html
| Claim | Verdict | Source or reason |
|---|---|---|
| TDPSA "may give you more rights" | confirmed | S13 (hedged correctly: applies to covered businesses) |
| Netlify hosting, Google Analytics, Google Translate cookie | kept without a search | Site build facts |
| Terms: "Whether you phone or fill in a form, an automated assistant handles the request" | corrected | The form is not handled by the phone assistant; reworded so calls go to the assistant and form requests go to a company for a call back |
| Terms: no state license; pay own deductible; contractor not a public adjuster | confirmed | S1, S2 |
| 404: navigation only | kept without a search | No claims |

## PDF (src/static/files/houston-hail-storm-claim-checklist.pdf), not edited
| Claim | Verdict | Source or reason |
|---|---|---|
| Wind/hail deductible often a percentage in Texas | kept without a search | General, hedged ("often") |
| Texas does not issue a state license for roofers | confirmed | S1 |
| Contractor may not pay, waive or rebate deductible | confirmed | S2 |
| Roofer "should not negotiate the claim on your behalf" | confirmed | S2 (may not act as public adjuster; may discuss its estimate with the insurer) |
| Ask insurer whether Class 4 shingles earn a discount | kept without a search | Phrased as a question to ask |
| "a local, owner-run roofing company" | kept without a search | Matches INTAKE "independent, locally owned". No issues found in the PDF. |

## Shared-file corrections (not edited; for the coordinator)
1. src/data/site.json, areas `league-city`, `county`: "Galveston" -> "Galveston and Harris" (city is mostly Galveston County with a small area north of Clear Creek in Harris; S16). Summary text can stay.
2. src/templates/macros.html, `windstorm_note`: "roof work must meet the windstorm building code and be inspected while it is under way" -> "most roof work must meet the windstorm building code and be inspected while it is under way (repairs to less than 100 square feet of roof covering that do not touch the decking are exempt)". Source S4 (TDI "What you need to know about windstorm inspections", https://www.tdi.texas.gov/tips/need-windstorm-inspection.html).
3. macros `license_check`: "a 2025 bill to create one (HB 3344) did not reach a vote of the full House before the session ended" CONFIRMED (S1: committee report sent to Calendars May 8 2025, died in chamber). Consider citing https://legiscan.com/TX/bill/HB3344/2160 or the capitol.texas.gov bill history alongside the RCAT page, since the RCAT advocacy page was not seen in search results.
4. macros `deductible_note`: CONFIRMED as written (S2).
5. macros `safety_box`, `how_it_works_short`: no factual issues (utility default CenterPoint is right for Houston; per-town utility is for the town checkers).
6. site.json area counties: all 28 checked against general knowledge and the town pages; Katy (Harris, Fort Bend, Waller) confirmed by S16b. Only League City needs a change. Tomball "Harris and Montgomery" describes the mailing area (the City of Tomball itself is in Harris County); acceptable because the summary and page explain it, but "Harris" alone would be the strict city answer. Kingwood "Harris and Montgomery" kept without a search.
7. site.json service and guide summaries: no checkable figures; none need changes.

## Totals (rows above)
- confirmed: 33
- corrected: 5
- softened: 3
- removed: 0
- kept without a search: 18
(plus 1 n/a row: sources added on /service-areas/; and 1 n/a row: forms intact)

Build/check after edits: build OK; check.py 0 errors 0 warnings; grep_check 0 hits; similarity: no FAIL lines on fc1 pages (the only FAILs seen are on /how-long-does-a-roof-last-in-houston/, not an fc1 page).
