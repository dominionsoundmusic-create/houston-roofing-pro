# Houston Expert Roofers (houstonexpertroofers.com): PLAYBOOK 2.0 REBUILD. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding Maurice Johnson's Houston roofing referral-line site from scratch by running
Dominic & Dalton's Website Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in full.

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not watching this session and cannot approve anything. Do NOT pause at the end of each
playbook phase, do NOT ask "continue?", do NOT wait for input. Make reasonable decisions yourself,
write them down in docs/decisions.md, and keep going until Prompt 20 is finished and every check
below passes. The only reasons to stop early: something would cost money, deploy, merge to main,
or change a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts. It wins over anything else. UNKNOWN means leave it off the site.
- PLAYBOOK.md: the playbook (Operating Rules, then Prompts 1 to 20). It was written for GHL AI
  Studio; apply its rules and its 20 steps to this static build system.
- keywords/Houston-Roofing-Keywords.xlsx: Ubersuggest, United States, pulled Oct 12 2026. 937
  unique keywords, a tab per seed (15 service seeds, 30 town seeds) plus an ALL tab, each row typed
  Suggestion or Question. Every Houston-area keyword with a volume of 10 or more must be assigned
  to a page as a target or supporting keyword, or listed in docs/keyword-plan.md as deliberately
  unused with a one-line reason. "Near me" terms are national volume: supporting keywords only,
  never proof of Houston demand. Rows about other states or metros (Kansas City, Stafford VA,
  Webster NY, Pasadena CA, Richmond VA and so on), rows naming a specific roofing company, and
  off-topic rows go in the unused list (summarize by group).
- The CURRENT site in this repo: every existing page holds research (Houston weather, the May 2024
  derecho, Hurricane Beryl, TDI windstorm rules for Pasadena east of SH 146, roof replacement cost
  factors, hail claim steps). Read every page before writing. Keep the facts that check out, verify
  them again, and improve them for each page's keyword. Never copy the old pages' layout.

## Copy the build system from Houston Power Washing Pro (NOT its words)
Clone dominionsoundmusic-create/houston-powerwashing-pro, branch `build` (the live branch of a
finished Playbook 2.0 site, with the Oct 12 2026 full-width fix). Copy its BUILD SYSTEM: build.py
(Jinja2, writes dist/), scripts/check.py, scripts/similarity.py if present, src/templates/,
src/static/css/site.css and JS, the macros, the site.json structure, netlify.toml
(publish = "dist") and the docs/ document set as a pattern. Also look at
dominionsoundmusic-create/water-damage-pro-houston, branch `build`, for the image placeholder
pattern and the old-URL check pattern. Adapt every value to Houston Expert Roofers and roofing.
NEVER copy page text, paragraphs, FAQs or sentence runs from any other site.
Keep the speed fix exactly (WebP 480/800/1200/1600/1920 srcset, preloaded hero with fetchpriority
high, self-hosted woff2 font) and the full-width layout (`--rail: clamp(22px, 5.5vw, 140px)`;
header, hero content, bands, text, photos, cards and footer all on the same left and right edge).
Card rows: 3 / 2 / 1 columns, any short last row CENTERED, never a hole on the right.

## OLD URLS MUST KEEP WORKING
Every URL the live site has today must still return a page or a 301 to the closest new page:
/, /about/, /contact/, /contact/thanks/, /faq/, /services/, /free-roof-inspection/,
/hail-claim-checklist/, /hail-claim-checklist/thanks/, /hail-damage-roof-insurance.html,
/hail-damage-roof-repair/, /roof-flashing-repair.html, /roof-leak-repair/,
/roof-repair-emergency.html, /roof-repair/, /roof-replacement-cost.html, /roof-replacement/,
/storm-damage-roof-repair/, /wind-damage-roof.html, /privacy-policy.html, /terms.html,
/baytown-roofing/, /conroe-roofer/, /friendswood-roofing/, /humble-roofing/,
/league-city-roofing-company/, /pasadena-roofing-contractors/, /roofing-companies-cypress-tx/,
/roofing-companies-katy-tx/, /roofing-companies-richmond-tx/, /roofing-companies-spring-tx/,
/roofing-companies-sugar-land-tx/, /roofing-companies-the-woodlands-tx/,
/roofing-company-missouri-city/, /roofing-company-tomball-tx/, /roofing-kingwood-tx/,
/roofing-pearland-tx/, /files/houston-hail-storm-claim-checklist.pdf, plus every rule in the
current _redirects (keep them). Keep a URL where it already ranks for its keyword; otherwise 301 it.
Write scripts/check_old_urls.py that lists every old URL and proves it resolves in dist/ or has a
redirect. Move the old page files into docs/old-site/ with `git mv` so they are not published.
Keep images/ (logo.svg, the 12 roof photos), favicons and files/ in the new static folder.

## Pages to build (decide the exact list from the keywords, then follow it)
- Home, services overview, service areas overview, how it works, about, FAQ, contact, the hail
  claim checklist page, privacy, terms, 404.
- Service pages: one per real service with Houston demand (roof repair, roof replacement, roof
  leak repair, storm damage, hail damage, roof inspection, emergency roof repair and tarping,
  commercial roofing, flat roof repair, metal roofing, plus anything else the data supports, such
  as wind damage and flashing repair, which already exist).
- Guide pages for the strongest question keywords: roof replacement cost in Houston, roof
  insurance claims in Texas (hail and wind, deductibles, ACV vs replacement cost, what a roofer may
  and may not do under Texas law), how to check a roofer before hiring (Texas has no state roofing
  license: research and state it correctly), how long a roof lasts in Houston, emergency steps
  after storm damage. Each researched and sourced. Keep the existing guide URLs.
- Town pages: Maurice's rule is ANY Houston-area town with 10 or more searches a month on a
  roofing term gets its own page. From a first pass of the data that is about 29 towns: Katy,
  Sugar Land, Cypress, The Woodlands, Spring, Pearland, League City, Pasadena, Conroe, Humble,
  Kingwood, Tomball, Missouri City, Richmond, Friendswood, Baytown, Atascocita, Galveston,
  Magnolia, Rosenberg, Webster, Alvin, La Porte, Seabrook, Deer Park, Bellaire, Stafford,
  Channelview, Texas City. Fulshear showed zero: no page. Check each town in the data yourself:
  count only Texas rows, and do not count rows that name a specific roofing company. A town whose
  only 10+ rows are company names gets no page. Record the exact keyword and volume per town in
  SERVICES.md. Keep the existing town URLs for the towns that already have pages.
- Write SERVICES.md (every page, URL, target keyword with volume/SEO difficulty) and
  docs/keyword-plan.md before writing pages.

## Hard rules for every page
1. Never "our roofers", "our crew", "our team", "we repair", "we replace", "we inspect", "we
   install", "we are licensed/insured/certified" or anything implying the line does roofing work.
2. Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business,
   team members, job counts, guarantees, response times, awards or statistics. Tell readers what
   to ask a roofer for.
3. Never name a specific roofing company (partner or not). Shingle brands may be named only as
   general product information, never as a partner certification.
4. Only greater-Houston places. No other Texas metros.
5. No em dashes or en dashes in visible copy (except the Duplantis credit). No eyebrow labels.
   American spelling.
6. Safety first, no DIY roof work: never tell a homeowner to climb on a roof. Safe steps only:
   stay off the roof, move belongings away from a leak, catch drips, photograph damage from the
   ground and inside, stay away from downed lines (call CenterPoint), call the insurer.
7. No prices presented as the line's prices. Cost guides cite published, sourced ranges and say
   real quotes vary. Never say insurance will pay; say what to ask the insurer. Never suggest a
   roofer can waive or cover a deductible (research the Texas law on this and state it correctly).
8. Every page except privacy, terms and 404 has 3 to 6 FAQs written the way people ask (use the
   Question rows), rendered visibly AND as FAQPage JSON-LD.
9. Every page has a full-width hero image plus at least two in-body images, each with filename,
   alt, width, height and loading="lazy" (hero eager). Use the 12 existing photos first. Every new
   image goes in docs/image-list.md and shows as a brand-color block until it arrives, never broken.
10. Facts must be real and current. Research each page on the web and cite every source in the
    page's sources list. If you cannot verify a fact, leave it out.
11. Each page is written for its own keyword. Never reuse paragraphs between pages with names
    swapped. Measure Jaccard similarity on 5-word shingles between every pair of pages of the same
    type; any pair above 15% gets rewritten. Record the numbers in docs/qa.md. Town pages must be
    researched for THAT town: its county, its storm history (Harvey, Beryl, the May 2024 derecho,
    hail events), whether it is in the TDI windstorm catastrophe area, its housing age and roof
    types, its permit office and whether a roofing permit or registration applies, HOA rules where
    relevant, and real neighborhoods residents would recognize.
12. The referral disclosure appears on every page (wording in INTAKE.md).
13. Banned phrases: "your trusted partner", "one-stop solution", "look no further", "unmatched
    excellence", "we've got you covered", plus the WORDS TO AVOID in INTAKE.md.
14. Mark every page with the HTML comment `dwdp:handwritten 2026-10-12` in the first 4KB.

## Design (Maurice's standing rules, check each one)
- Header/menu bar in a real brand color (the navy), never dull gray. Phone visible with
  tap-to-call. EN/ES Google Translate toggle in the header on every page, in brand colors.
- Hero stretches edge to edge on every page: full-strength photo, dark left-to-right fade behind
  the headline, logo/headline/buttons aligned to the left rail at 1440, 1920 and 2560 wide. Hero
  stays above the fold (max-height about 700px) with the call button visible.
- Body text, photos and cards run FULL WIDTH on the rail. Never box text into a narrow center strip.
  A photo standing alone in the text run is capped at about 560px tall (object-fit: cover).
- Mostly WHITE sections broken by occasional bold color bands (hero, white, navy band, white, a
  second band in gold). Never pale off-white or cream tints. Never every section tinted.
- No white text or white boxes on white. Every card, box, form field and button has clear contrast.

## Before you finish (all must pass)
- `python3 build.py` then `python3 scripts/check.py`: 0 errors.
- `python3 scripts/check_old_urls.py`: every old URL resolves or redirects.
- Grep the built site for: em/en dashes in visible text (except the Duplantis credit), "we
  repair", "we replace", "we inspect", "our roofers", "our crew", "our team", "licensed and
  insured", "free estimate", "free inspection", "same-day", "guarantee", "GAF certified",
  "Houston Roofing Pro", "Dallas", "Fort Worth", "Austin", "(903)", "(214)", "(469)". Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px wide (do not hide overflow to pass).
  Screenshot the home page and one town page at 1440, 1920 and 2560, scroll so every photo loads,
  and look at each section yourself: hero content near the left edge, nothing invisible, no white
  on white, card rows centered, no broken images.
- Both Netlify forms present in the static HTML with their exact names and fields.
- Independent fact-check: start separate sub-agents that did not write the pages, have them check
  every factual claim and source on every page, and fix what they find. Record it in
  docs/fact-check.md. Never say "fact-checked" unless this was actually run.
- docs/image-list.md lists every image still needed, heroes first: File name, Size (heroes
  1920x1080, in-body 1200x800), then an Artistly prompt (bright, clearly visible, Houston-area homes
  and roofs, no text, no logos, no recognizable faces, "wide cinematic landscape shot, subject
  positioned on right third of frame, well lit").

## Git
- Work on the branch `build`. Commit as you go with clear messages.
- Push to origin `build` at the end. The live site deploys from `main`, so pushing `build` does not
  go live. Do NOT merge to main, do NOT push to main, do NOT change Netlify settings, do NOT pay
  for anything. Maurice decides when it goes live.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built (count by type), checks passed, old URLs all resolving (yes/no), duplication range,
fact-check result, how many images need Artistly, and the one thing Maurice must do next.
