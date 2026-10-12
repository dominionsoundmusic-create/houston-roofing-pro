# Decisions log (Playbook 2.0 rebuild of houstonexpertroofers.com, Oct 12 2026)

Maurice was not available to approve anything during this run (CLAUDE.md: run straight through). Each
decision below was made from INTAKE.md, CLAUDE.md and the keyword data, and can be reversed later.

## Build system and structure
1. **Build system copied, words not copied.** CLAUDE.md names Houston Power Washing Pro (`build`) as the
   source of the build system. Its `build` branch does not contain the speed fix CLAUDE.md asks to keep
   (WebP 480/800/1200/1600/1920 srcset, preloaded hero with fetchpriority high, self-hosted woff2 font):
   that version only exists in Water Damage Pro Houston (`build`), which is the same build system one
   generation later, with the brand-color placeholder pattern and the old-URL check pattern CLAUDE.md also
   points to. So build.py, the Jinja layouts and partials, site.css, site.js, the Inter woff2 font,
   check.py, similarity.py, grep_check.py, keyword_plan.py, responsive_check.js and netlify.toml
   (`publish = "dist"`) come from Water Damage Pro Houston, and the centered card rows (3 / 2 / 1 columns,
   a short last row centered) come from Houston Power Washing Pro's Oct 12 full-width fix. Every value was
   changed to Houston Expert Roofers and roofing, and every shared sentence (macros, call band, footer,
   how-it-works strip, notes) was written new. `scripts/similarity.py --other` fails any page that shares an
   8-word run with either source site.
2. **Full-width layout kept exactly**: `--rail: clamp(22px, 5.5vw, 140px)` for the header, hero content,
   bands, text, photos, cards and footer. Photos standing alone in the text are capped at 560px tall.
3. **Brand.** INTAKE.md palette: navy #1a1a2e (header, first color band, call band), gold #c9a84c (buttons
   and the second color band, always with navy text because white on gold fails contrast), red #c1121f
   only for the header Call button. Plain sections are pure white. Small note boxes use a cool gray
   (#eceef4) with a navy edge; the call box is white with a gold frame, so there is no cream anywhere.
   Links on white are dark gold (#6e5410, about 7:1) and underlined.
4. **Old site moved, not deleted.** Every old page, the old css/, sitemap.xml, robots.txt and _redirects
   were moved with `git mv` into docs/old-site/ so they are not published. images/, files/ and the three
   favicons were moved with `git mv` into src/static/ so they publish unchanged at the same URLs.
5. **dist/ is committed.** Netlify publishes `dist` with no build command, as on the sister sites.

## URLs
6. **Every existing URL that still fits its keyword is kept**, including the five `.html` pages
   (/roof-repair-emergency.html, /wind-damage-roof.html, /roof-flashing-repair.html,
   /roof-replacement-cost.html, /hail-damage-roof-insurance.html) and /privacy-policy.html and /terms.html.
   build.py supports a `url:` front-matter value for these. Old canonicals that ended in `/index.html`
   now canonicalize to the folder URL.
7. **/free-roof-inspection/ becomes /roof-inspection/ (301).** "Free inspection" is on the INTAKE.md list of
   words to avoid, so the page cannot target "free roof inspection". The new page targets "roof inspection
   houston" (320). The old URL and its wildcard rule now 301 to /roof-inspection/.
8. **Old _redirects rules are all kept**, with targets updated to the closest new page: the old storm blog
   post now goes to the new storm-steps guide, the two metal-vs-asphalt posts to /metal-roofing/, and the
   targets that pointed at extensionless URLs (/roof-replacement-cost, /hail-damage-roof-insurance) now
   point at the canonical .html URLs.
9. **New town pages use /roofing-<town>-tx/**, matching the most common keyword pattern ("roofing alvin tx").
   The 16 existing town URLs are kept unchanged.
10. **The insurance guide keeps /hail-damage-roof-insurance.html** (indexed) but now covers roof insurance
    claims in Texas generally (hail and wind, deductibles, ACV vs replacement cost, what a roofer may do).

## Pages and keywords
11. **28 town pages.** Each qualifying town was checked in the data (Texas rows only, company-name rows
    excluded). Bellaire does not qualify: its only 10+ row, "bellaire roofing" (50), is the name of a
    Houston roofing company (Bellaire Roofing Company, Inc.), and "roofing bellaire tx" is 0. Fulshear shows
    0. The other 28 towns on CLAUDE.md's first-pass list all qualify; exact keyword and volume per town are
    in SERVICES.md.
12. **12 service pages**: the ten CLAUDE.md lists plus wind damage and flashing repair (both live URLs).
    Wind damage has no row in the Oct 12 pull; it is kept because the URL is indexed and wind is the main
    cause of Houston roof claims. Flashing targets "where does flashing go on a roof" (210).
13. **5 guides**: replacement cost, insurance claims, checking a roofer (Texas license question), roof
    lifespan in Houston, and storm-damage steps. Their targets and supporting rows are in SERVICES.md and
    docs/keyword-plan.md.
14. **Ambiguous place rows** ("roofing pasadena" 590, "richmond roofing contractor" 40) are unused: the
    much larger Pasadena CA and Richmond VA dominate those searches, and only Texas rows count.
15. **No "near me" row is a target.** They are supporting keywords only (national volume).

## Business data and rules
16. **Phone** lives once in src/data/site.json; build.py derives the display and tel forms. check.py fails
    the build if the number is typed into any page or template source.
17. **GA4 G-KBRNTW0VQP** with the live site's `phone_call_click` event (every tel: link click) on every page.
18. **Forms**: only the two live Netlify forms, rendered in the static HTML with their exact names, actions
    and fields: `houston-roofing-contact` on /contact/ (thanks /contact/thanks/) and `houston-hail-checklist`
    on /hail-claim-checklist/ (thanks /hail-claim-checklist/thanks/, which links the PDF). check.py verifies
    names, fields and the select options, and fails if a form appears anywhere else.
19. **The checklist PDF is unchanged.** It already says Houston Expert Roofers, calls the line a referral
    service, makes no license, insurance, price or response-time claims, tells people to stay off the roof,
    and states the deductible rule correctly.
20. **Texas roofing license.** Texas has no state license for roofing contractors. A 2025 bill (HB 3344) to
    create a TDLR reroofing license passed a House committee but did not reach a floor vote before the
    session ended on June 2, 2025 (RCAT advocacy page; Texas Legislature bill analysis). The site says so.
21. **Deductibles and adjusting.** TDI: it is illegal for a contractor to waive, rebate or absorb a
    deductible, a contract of $1,000 or more paid from insurance must carry a notice saying the insured must
    pay it, and a contractor may not act as a public adjuster on a property it works on (Insurance Code
    4102.163). TWIA claims must be filed within one year of the storm.
22. **Safety**: the site never tells anyone to climb a roof, tarp it themselves, pierce a ceiling or work
    at the breaker panel. The safe steps are the CLAUDE.md list (stay off the roof, move belongings, catch
    drips, photograph from the ground and inside, stay away from downed lines and call CenterPoint, call the
    insurer). The old pages' "pierce a bulging ceiling" and "cut power at the breaker" advice was dropped.
23. **No eyebrow labels**, no em or en dashes (the Duplantis credit dash is drawn by CSS), American spelling.
