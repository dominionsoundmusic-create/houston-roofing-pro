# Writing guide for houstonexpertroofers.com pages (Playbook 2.0 rebuild, Oct 12 2026)

Repo: /home/user/houston-roofing-pro (branch `build`). Read these first, in full:
1. `CLAUDE.md` (the hard rules) and `INTAKE.md` (the facts; it wins over everything; read "WHAT THE
   BUSINESS ACTUALLY IS" twice).
2. `SERVICES.md` and `docs/keyword-plan.md` (your page's URL, TARGET keyword and supporting keywords,
   including the Question rows to turn into FAQs).
3. `src/data/site.json` (names, URLs and slugs of services, guides and areas; card summaries).
4. `src/templates/macros.html` (service_cards, guide_cards, area_cards, area_pills, related, call_box,
   how_it_works_short, disclosure, license_check, deductible_note, safety_box, windstorm_note, sources).
5. STRUCTURE MODEL: `src/pages/roof-repair.html` (a finished service page: front matter, section rhythm,
   panels, a comparison table, the steps list, how the macros are used, the sources list). Copy its
   STRUCTURE, never its sentences.
6. YOUR PAGE'S OLD VERSION in `docs/old-site/` (if it exists). It holds research worth keeping. Re-verify
   every fact before you reuse it, rewrite it in new words for the page's keyword, and never copy its layout.
   Some old advice is now banned (piercing a ceiling, cutting power at the breaker, "tarp from the ground").
7. DEPTH REFERENCE (never copy words or facts; it is a water damage site): the sister site
   `/home/user/water-damage-pro-houston/src/pages/water-damage-restoration-katy-tx.html` shows the depth
   expected of a town page. `scripts/similarity.py --other` fails any page sharing an 8-word run with it.

## The business, in one paragraph
Houston Expert Roofers is a FREE PHONE LINE and website, NOT a roofing company. An automated assistant
answers any hour, asks which service the caller needs (the same number also serves air conditioning and
heating, pressure washing and water damage) and briefly what is going on with the roof, then transfers
the call to an independent, locally owned Houston-area roofing company, which hears a short summary before
it picks up. If that company cannot answer, the caller's name, callback number, city, need and urgency are
passed along for a call back. The roofing company inspects, quotes, does the work and is paid directly by
the customer (or the customer's insurer, as the customer arranges). The line never climbs a roof, inspects,
sells shingles, quotes, repairs, replaces, tarps, files claims or schedules anything; it holds no license,
never charges the caller, and companies may pay it a referral fee. Write "the roofing company you are
connected with", "the roofer", "a careful roofer", "a roofing company that works in Katy". NEVER "our
roofers", "our crew", "our team", "we repair/replace/inspect/install/tarp", "we'll send someone",
"we are licensed/insured/certified". Never say the connected companies are licensed, insured, certified
(GAF, Owens Corning, CertainTeed or any program), rated, reviewed, fast or experienced. Never name any
roofing company, supply house or contractor, partner or not. Shingle brands may be named only as general
product information, never as a certification.
The phone number is NEVER typed in a page. Use `{{ site.business.phone_display }}` and
`tel:{{ site.business.phone_tel }}`, or `{{ site.cta.primary_label }}` for a call button label.
Public agency numbers (CenterPoint, TDI, 311, a city permit office) are fine when sourced.

## Hard rules (scripts/check.py enforces most of them; it must report 0 errors for your pages)
- No em dashes or en dashes anywhere (copy, titles, descriptions, FAQs, alt text, source labels). Use
  commas, colons, periods or "to" ("15 to 20 years"). American spelling. No eyebrow labels or badges.
- Only greater-Houston places (Harris, Fort Bend, Montgomery, Brazoria, Galveston, Chambers, Waller,
  Liberty counties). NEVER name Dallas, Fort Worth, DFW, Austin, San Antonio, El Paso, Beaumont, Corpus
  Christi, Waco, any other Texas metro, Louisiana, Florida or another state, not even as a comparison or
  inside a source label. If a source title names one, shorten the label.
- Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business, team
  members, job counts, guarantees, response times, awards or statistics. Public statistics are fine with
  the source named in the sentence and listed in Sources. Prices: explain what drives price; a published
  range only with its source named on the page and a note that real quotes vary. Never present a price as
  the line's price. Never say insurance will pay; say what to ask the insurer.
- Banned words and phrases (checker fails): "free estimate(s)", "free inspection", "free roof inspection",
  "same-day", "same day", "guarantee" in ANY form (also "guaranteed", "no guarantee": use "promise" or
  "warranty" instead), "best price", "cheapest", "top-rated", "years of experience", "#1", "number one",
  "licensed and insured", "fully insured", "GAF certified", "certified roofer/contractor/installer",
  "we work with all insurance", "we handle your claim", "no out of pocket", "we pay your deductible",
  "deductible waived", "insurance will pay/cover", any response-time promise ("within 2 hours"),
  "your trusted partner", "one-stop solution", "look no further", "unmatched excellence",
  "we've got you covered", "our team", "our crew", "our roofers", "Houston Roofing Pro", and "we + any
  work verb". Say "many roofers inspect at no charge; confirm that on the call" instead of "free inspection".
- SAFETY FIRST, NO DIY ROOF WORK. Never tell a homeowner to climb on a roof, use a ladder to reach the
  roof, tarp it themselves, pierce a ceiling, or work at the breaker panel. The only safe steps:
  stay off the roof; move belongings away from a leak; catch drips (bucket, towels); keep people out of a
  room with a sagging ceiling; photograph damage from the ground and inside; stay away from downed lines
  and report them to CenterPoint Energy (or the local utility) or 911; call the insurer. The macro
  `m.safety_box()` says this; use it on storm, leak, emergency and town pages.
- Insurance law (verified Oct 12 2026, use `m.deductible_note()` where relevant): TDI says it is illegal
  for a contractor to offer to waive, rebate or absorb a deductible; a contract of $1,000 or more paid
  with insurance money must include a notice that the insured must pay the deductible; insurers may ask
  for proof it was paid; a contractor may not act as a public adjuster or advertise to adjust claims on a
  property where it provides or may provide contracting services (Insurance Code 4102.163). Public
  adjusters are licensed by TDI. TWIA wind and hail claims must be filed within one year of the storm.
  TDI consumer help line: 800-252-3439.
- Texas has NO state roofing license (`m.license_check()` says so, with HB 3344 of 2025 failing). Some
  cities require contractor registration or permits: research your city, do not assume.
- TDI windstorm (use `m.windstorm_note()` on coastal pages): the designated catastrophe area is the 14
  first-tier coastal counties (in greater Houston: Brazoria, Chambers, Galveston) plus, in Harris County,
  Morgan's Point and the parts of La Porte, Pasadena, Seabrook and Shoreacres inside city limits and east
  of SH 146 (TDI order 96-1468; west of SH 146 these cities are outside the program). Roof work there must meet the
  windstorm code and be inspected during installation; TDI issues a WPI-8 certificate of compliance, which
  TWIA uses for eligibility. Verify details for your town (for example, which part of a split city is in
  which county).
- City of Houston (verified): roof covering up to 100 sq ft in aggregate is exempt from a permit; a
  re-roof or overlay needs a residential roofing permit (Houston Permitting Center, HPWCODE1140).
  Kingwood is inside the City of Houston.
- Facts must be real and current. Research every page on the web (WebSearch works; WebFetch and curl to
  most sites fail in this environment, so verify against search results restricted to the official
  domain where possible). Cite every source in the page's `m.sources([...])` list with a plain label and
  the URL. If you cannot verify a fact, leave it out. Do not name a source you did not see.
- Each page is written for its own keyword. Never reuse paragraphs between pages with names swapped.
  Avoid stock sentences that other pages would also use. `scripts/similarity.py` must show your page
  below 15% Jaccard (5-word shingles) against every other page of the same type.

## Page format
Front matter (YAML) then `{% block content %} ... {% endblock %}`. Required front matter:
- `type`: service | guide | area (towns) | page
- `title`: 50 to 65 characters, contains the target keyword or a close form, unique, no dashes.
- `description`: 120 to 160 characters, unique, contains the keyword.
- `h1`: one clear H1 (the hero renders it). Town H1s name the town; service H1s name the service.
- `crumb`, `keyword` (the exact target keyword).
- `url:` ONLY for pages whose live URL ends in .html (for example `url: /wind-damage-roof.html`). Folder
  pages get their URL from the file name: `src/pages/roofing-companies-katy-tx.html` -> /roofing-companies-katy-tx/.
- `city_name:` on town pages (plain town name), and `schema_service:` with `name` and `type`
  ("Roofing referral").
- `hero`: `image` (file name), `alt`, `desc` (the Artistly prompt, see Images), `lead` (one or two
  sentences, under 260 characters), `secondary_label` and `secondary_href` (a useful in-page anchor such
  as "#permits" or another page). Optional `position` (CSS object-position) for existing photos.
- `cta_title` (optional): a page-specific heading for the closing call band.
- `faqs`: 3 to 6 items, `q` written the way people ask (use the Question rows from keyword-plan.md), `a`
  as HTML (`<p>...</p>`), 50 to 110 words, with at least one internal link across the set. They render
  visibly and as FAQPage JSON-LD automatically.

## Sections
Mix plain white sections (`<section class="prose">`) with at most two color bands per page
(`<section class="band band--tint"><div class="wide">...</div></section>`: the first becomes navy, the
second gold, automatically; the FAQ band after the content is always gold, so keep body bands to one or
two). Never put two bands next to each other. Useful parts: `.split` (text + image side by side),
`.grid-2` / `.grid-3` with `.panel`, `.steps` (numbered), `.checks` (tick list), `.facts`, a
`.table-wrap` table with `<thead>`, `.note`, `m.call_box()`. Use H2 for sections and H3 inside them.
Pick at least one design treatment that suits the page (a comparison table, a process, a checklist, a
timeline of storms), not the same pattern on every page.

### Service page (Prompt 9), about 1,500 to 2,200 words of page copy
What the service is; who it is for; common problems in Houston; how a careful roofer handles it (the
line's own "approach" is only: answer, connect, pass details); what to expect and the options; questions
to ask; related services (`m.related([...])`); `m.how_it_works_short()`, `m.license_check()`,
`m.disclosure()`; town pills (`m.area_pills()`); Sources. Unique H1, title, description, headings.

### Town page (Prompt 11), about 1,500 to 2,200 words of page copy
Research THAT town: county or counties; city or unincorporated (and what that means for permits);
the permit office and whether a roofing permit or contractor registration applies (cite the city's own
page and fee only if found); whether it is in the TDI catastrophe area; storm history that actually hit it
(Harvey 2017, the May 16 2024 derecho, Hurricane Beryl July 8 2024, Ike 2008 near the coast, documented
hail events with date and source); housing age and roof types; HOA or covenant rules where relevant
(Texas Property Code 202.011 bars an HOA from prohibiting impact-resistant or energy-efficient shingles
that look like allowed ones); real neighborhoods residents would recognize (verify each exists in or
near that town). Structure: a localized H2 with two local paragraphs and an image beside them (`.split`);
services genuinely available there (`m.service_cards([...])` with 3 to 6 slugs that fit the town);
a "Why [Town] homeowners call the line" section with four distinct local reasons (four `.panel`s); local
context; questions to ask a roofer in that town; area FAQs; `m.how_it_works_short()`, `m.disclosure()`,
`m.related([...])` with nearby towns (`'area:slug'`) and guides (`'guide:slug'`); "Other greater Houston
areas" with `m.area_pills(exclude='slug')`; Sources. Do not invent an office, address, customer count,
project history or travel time. Say "a roofing company that takes calls in [Town]", never "our [Town]
roofers".

### Guide page, about 1,800 to 2,500 words of page copy
Answer the target question in the first paragraph, then go deep: sourced facts, a table or checklist,
what to ask, mistakes to avoid. Include `m.disclosure()` and a call to action that fits. `type: guide`
(adds Article JSON-LD).

## Images (CLAUDE.md rule 9)
Every page has a full-width hero image plus at least two in-body images, all through the build:
- Hero: `hero.image`. Use one of the 12 existing photos only where it genuinely fits: roof-01-hero.jpg
  (crew laying new shingles: replacement), roof-02-hero.jpg (roofer by broken shingles: repair, wind),
  roof-03-hero.jpg (two roofers on a storm-damaged slope of a white-sided house: storm), roof-04-hero.jpg
  (roofer inspecting shingles: inspection), roof-05-hero.jpg (sealing a vent boot: leak, flashing),
  roof-06-hero.jpg (white TPO commercial flat roof: commercial, flat). Card versions are roof-0N-card.jpg
  (1200x675). Do not reuse a hero already used by another page for the same purpose; town pages get their
  own NEW hero. A new hero is a planned file: name it descriptively in lowercase-hyphens ending -hero.jpg
  (for example `katy-two-story-brick-home-roof-hero.jpg`) and write the Artistly prompt in `hero.desc`.
  The service pages listed in site.json with a planned `card_image` (hail, emergency, flat, metal, wind,
  flashing) must use exactly that file name as their hero image.
- In-body: `{{ img('file.jpg', 'alt text', 1200, 800, desc='Artistly prompt') }}` (in-body size
  1200x800). It adds width, height, loading="lazy" and a WebP srcset. A file that does not exist yet is
  listed in docs/image-list.md and shows as a navy block until it is generated. Never a broken image.
- Artistly prompt (`desc`) for every NEW image: start with "Wide cinematic landscape shot, subject
  positioned on right third of frame, well lit." then describe a bright, clearly visible Houston-area
  scene (house type and roof material true to that town, trees, flat Gulf Coast land, sky), and end with
  "Realistic photo, no text, no logos, no house numbers, no recognizable faces." No people climbing on a
  homeowner's roof as an instruction; roofers at work are fine.
- Alt text describes what is in the picture, no dashes, not keyword-stuffed.
- File names must be unique across the site (prefix town pages with the town slug).

## Before you report back
1. Build to YOUR OWN folder so you never collide with other writers:
   `python3 build.py --out /tmp/hxr-<your-name>` (this does not touch dist/ or docs/).
2. `python3 scripts/check.py --dist /tmp/hxr-<your-name> --skip-links --only <your url>` for each of
   your pages: 0 errors. Read the warnings and fix real ones (word count, heading jumps, DIY wording).
3. `python3 scripts/similarity.py --dist /tmp/hxr-<your-name> --other /home/user/water-damage-pro-houston/dist`
   and confirm none of your pages is above 15% against a page of the same type and none shares an 8-word
   run with the water damage site.
4. `python3 scripts/grep_check.py --dist /tmp/hxr-<your-name>`: no hits on your pages.
5. Do not edit any shared file (site.json, macros, templates, CSS, build.py, scripts, other pages). If you
   need a shared change, say so in your report. Do not commit or push; the coordinator commits.
6. Write your research notes (each fact, its source URL, and anything you left out because it could not
   be verified) to `docs/research/<your-name>.md`.
