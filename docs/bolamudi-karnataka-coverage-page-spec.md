# Karnataka Coverage — Page Design Specification
### Bolamudi Enterprise · Signature Page · v1.0

---

## 0. Read this before anything else

You asked for the signature page of the site. Then you told me three things that change what that page can honestly be:

- **No hard numbers.** No MW, no acres, no approval counts attributable per district.
- **Fully anonymised.** No client names, no named projects.
- **The 20 years of experience belongs to the founder, earned while employed at another company.** It is not Bolamudi Enterprise's corporate track record.

### The blunt part

The obvious version of this page — a hoverable Karnataka map where all 31 districts light up and each says "Land Aggregation · Government Liaison · Statutory Approvals" — is the single most damaging thing you could put on this website.

Here is why. Your audience is land heads at IPPs, BD leads at EPCs, and diligence analysts at investment firms. These people have personally walked Pavagada, Koppal and Gadag. They can tell within eight seconds whether the person who wrote a district page has been to the sub-registrar's office in that taluk or has been to Wikipedia. A map with 31 identical districts and no verifiable substance reads as **padding**, and padding on your signature page poisons the credibility of every other page on the site. Black & Veatch and Arup never claim coverage they cannot substantiate. That restraint *is* the professionalism you are trying to imitate.

Second problem, and this one is legal, not aesthetic: implying that projects executed under a previous employer's mandate constitute Bolamudi Enterprise's coverage is misrepresentation. If an investment firm runs diligence and finds the projects belong to a former employer, you lose the mandate and possibly more. This has to be structurally impossible in the page's content model, not just handled carefully in copy.

### The reframe

**This page is not a track record. It is a demonstration of ground knowledge.**

Your genuine, unfakeable, non-confidential asset is that the founder knows, district by district, *how land and approvals actually behave in Karnataka*. Which taluks have fragmented holdings that make aggregation a two-year exercise. Where gomala and inam land will stall you. Which DC offices move and which do not. Where the 220kV bays are already full. That knowledge requires no client name, no MW figure, and no NDA breach to publish — and no competitor can copy it, because they would have to have lived it.

So the page becomes:

> **Karnataka Ground Intelligence** — a district-by-district map of what it actually takes to develop here.

This inverts the credibility problem. Instead of asking the visitor to *believe* a claim, you hand them something useful before they have paid you anything. A land head who reads your Koppal entry and thinks *"this is correct, and it's more specific than my own internal note"* has already decided to call you. That is the conversion mechanism. Not the map. The map is the index.

**Everything below is designed for that page. If you want the version that just claims coverage, you don't need an agency for it and I'd advise against shipping it.**

---

## 1. Page role in the site

| Dimension | Decision | Reasoning |
|---|---|---|
| URL | `/karnataka` | Short, memorable, brandable in a pitch ("look at bolamudi.com/karnataka"). Not `/coverage` — coverage is a claim; Karnataka is a place, and place is the asset. |
| Nav label | **Karnataka** | A single proper noun in a nav of abstractions (Services, About, Contact) is visually and semantically dominant. It signals specialisation. Consultancies that say "Global" are commodities; consultancies that say "Karnataka" are experts. |
| Nav position | Second item, after Services | Services answers *what*; Karnataka answers *where and how well*. That is the order the buyer asks in. |
| Funnel stage | Mid-funnel evaluation → qualified enquiry | Not awareness (that's the homepage), not conversion (that's Contact). This page's job is to convert *interest* into *conviction*. |
| Primary conversion | "Request a district briefing" | Not "Contact us". A district-specific, named, low-commitment offer converts several times better than a generic form because it maps to the visitor's live problem. |
| Secondary conversion | Download the Karnataka RE Land & Approvals Primer (gated PDF) | Captures the researcher who is not yet ready to talk. Also your best B2B lead-capture asset. |

---

## 2. The credibility model (what replaces numbers)

Since you cannot prove *outcomes*, you must prove *process knowledge*. Four proof types, in descending order of persuasive power, all of which survive full anonymisation:

**1. Procedural specificity.** Naming the actual instrument, form, office and typical duration. "Conversion under Section 95 of the Karnataka Land Revenue Act, routed through the Deputy Commissioner's office; realistic 5–9 months in this district where the parcel carries no gomala overlap." Nobody bluffs this. It is the single highest-trust sentence type available to you.

**2. Failure-mode knowledge.** Naming what goes wrong locally. "Bhoomi records here frequently show unpartitioned joint holdings across three generations; expect to trace 20–40 legal heirs per 50-acre block." Only operators know failure modes. Salespeople only know benefits.

**3. Sequencing judgement.** Saying what to do in what order and why. "Do not sign land agreements before confirming bay availability at the nearest 220kV station — in this district that ordering error has stranded more land than any legal problem."

**4. Honest exclusion.** Saying where you *don't* operate and why. This is counter-intuitive and it is the strongest trust signal on the page. A consultancy that voluntarily marks a district "not RE-viable — we will refer you elsewhere" is instantly more believable on the districts it *does* claim.

**Explicitly banned from this page:** any MW figure, any acreage figure, any client logo, any phrase of the form "we have successfully delivered". Any past-tense delivery claim must be attributed in the founder's voice on the About page, framed as prior professional experience, never as company coverage. This is enforced at the CMS schema level (§13).

---

## 3. Coverage tiering — the honesty architecture

Do not render 31 equal districts. Render a truthful hierarchy. This is the design decision that makes the whole page work.

| Tier | Label shown to user | Count | Map treatment | Card depth |
|---|---|---|---|---|
| **1** | Core Operating Districts | 8–10 | Full brand fill, elevated, subtle inner texture | Full dossier: 400–700 words, land profile, approval profile, evacuation profile, failure modes |
| **2** | Active Coverage | 8–10 | Mid-tone fill, flat | Medium: 150–250 words, land + approval notes |
| **3** | Statewide Capability | remainder of RE-relevant | Light neutral fill, outline only | Short: one paragraph + contact CTA |
| **0** | Limited RE relevance | coastal/Malnad/urban | Very light grey, no fill, thin stroke, non-interactive by default | Tooltip only: honest one-line reason |

**Reasoning.** Karnataka's utility-scale RE reality is geographically lopsided and everyone in your audience knows it. The solar and wind resource sits in the northern and central dry belt — Tumakuru, Chitradurga, Koppal, Gadag, Ballari, Vijayanagara, Vijayapura, Bagalkot, Bidar, Kalaburagi, Yadgir, Raichur, Davanagere, Haveri, Belagavi. Pumped storage sits in the Western Ghats belt — Shivamogga, Uttara Kannada, Chikkamagaluru, Hassan. Dakshina Kannada, Udupi, Kodagu, Bengaluru Urban and Chamarajanagar are, for utility-scale purposes, largely not the conversation. ([Vijayapura leads state wind capacity at ~1.06 GW with Gadag second at ~694 MW](https://www.statista.com/statistics/1454270/installed-wind-capacity-by-district-karnataka-india/); [Pavagada in Tumakuru is 2,050 MW with 3 GW expansion planned](https://en.wikipedia.org/wiki/Pavagada_Solar_Park); [2,500 MW ultra-mega solar parks are planned in Bidar, Koppal and Gadag](https://kredl.karnataka.gov.in/new-page/Pavagada%20Solar%20Park/en); [the 2,000 MW Sharavathi PSP sits in Shivamogga](https://en.wikipedia.org/wiki/Sharavathi_Pumped_Storage_Hydropower_Project).)

A map that lights up Udupi with the same intensity as Koppal tells an informed visitor you don't know the state. A map that greys out Udupi with the tooltip *"Coastal — no utility-scale solar or wind resource. Not a market we claim."* tells them you do. **The grey districts sell the coloured ones.**

**You must personally decide the Tier 1 list.** I will not assign it for you — that is exactly the kind of assumption that produces a fake page. My recommended starting shape, for you to correct: Tumakuru, Chitradurga, Koppal, Gadag, Ballari, Vijayanagara, Vijayapura, Bagalkot as Tier 1; Bidar, Kalaburagi, Yadgir, Raichur, Davanagere, Haveri, Belagavi, Shivamogga as Tier 2.

---

## 4. Page skeleton (desktop, top to bottom)

```
Z1  Hero — statement + Karnataka silhouette, no chrome
Z2  Orientation strip — how to read this map (4 short items)
Z3  THE MAP MODULE — filter rail · map canvas · district panel   ← the signature
Z4  Coverage matrix — the same data as a scannable table
Z5  Ground Intelligence — 3 featured district dossiers as editorial cards
Z6  What we do in every district — the 6 services, mapped to the map's vocabulary
Z7  Method — the 5-stage development sequence, with district-specific variance called out
Z8  Honest limits — where we don't operate, and why
Z9  Conversion — request a district briefing
```

**Why the map is in position 3, not position 1.** An interactive map with no explanation is a toy. Two seconds of orientation (Z2) converts it into an instrument. Agencies that put the interactive artefact at the absolute top consistently see it ignored, because the visitor doesn't yet know what question it answers. Z1 gives them the question; Z3 lets them answer it.

**Why Z4 duplicates Z3 as a table.** Roughly a third of your audience — diligence analysts especially — will not play with a map. They want to scan, compare and copy. Serving the same data in two modalities is not redundancy, it is respect for two different reading behaviours. It is also your SEO safety net (§12) and your accessibility fallback (§14).

**Why Z8 exists.** See §2, proof type 4. This section is where the page earns its trust. Do not let anyone talk you out of it.

---

## 5. The map

### 5.1 Technology decision

**Build a static, build-time-generated inline SVG. Not Mapbox, not Leaflet, not a runtime GeoJSON renderer.**

| Option | Verdict | Reasoning |
|---|---|---|
| Mapbox / MapLibre + tiles | **Reject** | API keys, usage billing, ~200KB+ JS, a basemap you don't want, and it renders roads and labels that are noise. You are not doing wayfinding. |
| Runtime `d3-geo` + GeoJSON fetch | **Reject** | Ships a projection library and a geometry payload to every visitor to draw a shape that never changes. Pure waste. |
| **Build-time projection → inline `<svg>` with 31 `<path>`** | **Adopt** | Zero runtime geo dependency. Paths are in the initial HTML, so Google indexes district names. Every path is a real DOM node — hoverable, focusable, ARIA-labellable, CSS-themeable, animatable by Framer Motion. Total cost after simplification: ~35–60 KB of markup, gzipped to ~12–18 KB. |

**Pipeline.** Take verified district boundaries → confirm the file has **31** districts including **Vijayanagara** (carved out of Ballari in 2020; a very large share of freely available Karnataka SVGs are stale at 30 or even 27 districts, and shipping a stale map to people who work in Vijayanagara is an unforced credibility error) → simplify in `mapshaper` to roughly 4–6% of original vertices, preserving shared topology so no gaps open between neighbours → project offline with `d3-geo` using a conic conformal projection centred on Karnataka (~76.5°E, 15°N) rather than Mercator, because Mercator visibly distorts a 700 km north–south state and a distorted state map is the kind of detail your audience notices → emit a typed `districts.ts` of `{ id, name, slug, tier, path, centroid, layers[] }`.

Karnataka is entirely interior to India, so no international boundary is rendered and none of the associated depiction rules apply. Worth knowing, since it removes a real legal hazard that an all-India map would carry.

### 5.2 Projection and canvas

Karnataka's bounding box is roughly 11.5°–18.5°N by 74.0°–78.6°E — approximately 750 km tall by 450 km wide, a distinctly portrait shape. Design the SVG viewBox at **860 × 1080** and let the portrait map occupy the left half of a wide canvas, with the district panel filling the right. This is the only layout in which the map is large enough to be usable *and* the panel is wide enough to hold real editorial content. Attempts to make the map landscape-dominant force the panel into a narrow column and the content becomes unreadable.

### 5.3 Visual language

Not a data-viz choropleth. This is an engineering drawing.

- **Fill.** Four flat tiers only (per §3). No continuous colour ramp — a ramp implies a measured quantity, and you have no measured quantity. Using a ramp would be a visual lie.
- **Stroke.** District borders at 1px in a light neutral. Karnataka's outer boundary at 2px in near-black. Division boundaries (Bengaluru, Mysuru, Belagavi, Kalaburagi) available as an optional 1.5px dashed overlay — this is a genuine insider touch, because approvals route through divisional offices and your audience's project managers think in divisions.
- **Texture.** Tier 1 districts carry a barely-visible 4px diagonal hatch at ~6% opacity. It reads as technical drafting, not decoration, and it distinguishes Tier 1 even in greyscale print.
- **Labels.** Do not label all 31 on the base map — it becomes noise at any realistic size. Label Tier 1 only, in 11px uppercase with generous tracking, positioned at pole-of-inaccessibility rather than centroid so labels never fall outside irregular shapes. Tier 2 and 3 reveal their names on hover.
- **Overlay markers.** Small technical glyphs, not pins. Solar = a filled square rotated 45°. Wind = a three-stroke asterisk. PSP = two stacked chevrons. Transmission = a dashed polyline along corridor geometry. Pins are consumer-map language; glyphs are engineering-drawing language, and the difference is most of the perceived seriousness of the page.

### 5.4 Filter layers

Five toggles in the left rail, each an independent switch (not radio buttons — a developer evaluating a hybrid park needs Solar *and* Wind simultaneously):

`Solar` · `Wind` · `Hybrid` · `Pumped Storage` · `Transmission & RoW`

**Behaviour on filter.** Districts that do not carry the active layer desaturate to 25% opacity over 220 ms — they do **not** disappear. Keeping the full state silhouette intact preserves spatial orientation; districts popping out of existence destroys it and forces the user to re-orient on every toggle. This is the most common failure in interactive-map design and the easiest to avoid.

A live count sits under the rail: **"14 districts · Solar + Wind"**. It confirms the filter did something, which matters because a desaturation change is subtle by design.

### 5.5 Map interaction states

| State | Trigger | Visual response | Duration / easing |
|---|---|---|---|
| Rest | — | Tier fill, no elevation | — |
| Hover | pointer enter | Fill lightens ~8%, stroke → brand accent at 1.5px, district lifts 2px via `translateY(-2px)` + a soft drop shadow, name label fades in if not already shown | 160 ms, `ease-out` |
| Hover (neighbours) | pointer enter | All other districts drop to 55% opacity | 160 ms |
| Focus (keyboard) | `Tab` / arrow keys | Same as hover **plus** a 2px offset focus ring | instant ring, 160 ms fill |
| Selected | click / `Enter` | Fill → brand primary, stroke 2px near-black, district stays lifted, panel populates | 240 ms, `ease-out` |
| Filtered out | layer toggle | 25% opacity, `pointer-events: none`, `aria-hidden` | 220 ms |
| Tier 0 | — | Non-interactive; cursor `default`; tooltip on hover only | 120 ms |

**Deliberate omission: no pan and no zoom.** A single Indian state at this canvas size needs neither, and adding them introduces lost-viewport states, a reset-view affordance, awkward touch gesture conflicts on mobile, and a whole class of bugs — for zero user benefit. Restraint here is a design decision, not laziness. Award juries notice the absence of unnecessary mechanics far more reliably than they notice their presence.

### 5.6 Hover tooltip

Follows the cursor with a 12px offset, flips at viewport edges, 120 ms fade, and is suppressed entirely on touch. Contents: district name, tier label, and up to four layer glyphs. Nothing more — a tooltip that tries to summarise the dossier makes the click feel pointless, and the click is the conversion event of this module.

---

## 6. District cards / the panel

### 6.1 Two different objects — do not conflate them

**The Panel** is the right half of the map module. It is not a card. It is a persistent reading surface that swaps contents when the selection changes. It never overlays the map, because an overlay would hide the geography the user is reasoning about, and comparing "this district versus its neighbour" is the core task here.

**District Cards** are the grid objects used in Z5 (featured dossiers) and on the `/karnataka/[district]` index. They are static, linkable, and SEO-relevant.

### 6.2 Panel states

**Empty (default on load).** Not a "select a district" placeholder — placeholders waste the most valuable real estate on the page. Instead the panel loads with a **Karnataka Overview**: the four divisions, the three resource belts, the state's stated 19.2 GW-by-2030 addition target as market context, and one sentence on why land and approvals — not equipment or finance — are the binding constraint on Karnataka RE timelines. This makes the panel valuable before the user does anything, and it gives the page a meaningful first paint for anyone who never interacts.

**Populated (district selected).** Fixed section order, always identical, because a consistent structure is what makes 31 entries comparable — and comparability is the whole point of a coverage page:

```
1  District name  ·  Division  ·  Tier badge
2  Resource profile        Which layers apply, in one line
3  Land character          Holding patterns, typical parcel size, terrain,
                           classification issues to expect
4  Approvals character     Which clearances dominate here, realistic
                           sequencing, where the queue forms
5  Evacuation character    Grid context in qualitative terms
6  What we do here         2–4 of the six services, described in
                           district-specific language, never generic
7  Watch-outs              2–3 named failure modes. The trust engine.
8  CTA                     "Request a briefing on <District>"
```

Sections 3–5 are qualitative by design. That constraint is doing real work: qualitative language is where your genuine expertise lives, and it happens to be exactly what you can publish under full anonymisation. The constraint and the differentiator are the same thing.

**Loading.** Never a spinner. All district content is statically generated and pre-bundled at build time, so the swap is synchronous. A spinner on a 40 KB static payload signals an amateur build.

### 6.3 Panel transition

Old content fades out and lifts 8px over 120 ms; new content fades in from 8px below over 200 ms with a 60 ms stagger across sections. Total 320 ms. The stagger is what makes it feel authored rather than mechanical. Header does not animate — it cross-fades in place, so the user's eye has a fixed anchor and never loses its position.

### 6.4 Card anatomy (Z5 and the district index)

Aspect 4:3 image top, then eyebrow (Division), then district name in the display face, then a 2-line qualitative summary, then up to four layer glyphs, then a text link. On hover: image scales to 1.04 over 400 ms with `ease-out` while the card itself lifts 4px and the border darkens. **The image scales inside a fixed-overflow container** — the card frame must never change size, because a card grid that reflows on hover is the visual signature of a cheap template.

---

## 7. Filtering — full specification

Three independent controls, combined with AND:

1. **Layer toggles** (5, multi-select) — see §5.4
2. **Tier filter** (4, multi-select) — lets a serious buyer say "show me only where you're actually deep"
3. **Division filter** (4, single-select + All) — Bengaluru / Mysuru / Belagavi / Kalaburagi

Every filter change writes to the URL query string (`?layer=solar,wind&tier=1&div=kalaburagi`). This is not a technical nicety — it means a land head can send a filtered view to a colleague in Slack, and that shared link is free qualified distribution. Serialise to the URL with `replaceState` so the browser back button steps out of the module rather than unwinding twenty filter changes.

Filter state must survive a district selection and a panel scroll. The single most irritating bug in this class of interface is filters silently resetting; specify it explicitly so it gets tested.

An empty result set is a designed state, not an error: the map holds its full silhouette at 25% opacity and the panel says *"No districts match this combination. Nearest alternative: Solar + Tier 1 (8 districts)."* with the alternative as a live button.

---

## 8. Micro-interactions (complete inventory)

| # | Element | Trigger | Behaviour | Rationale |
|---|---|---|---|---|
| 1 | Hero silhouette | page load | Karnataka outline draws via `stroke-dashoffset` 0→100% over 1400 ms, then fill washes in over 600 ms | One deliberate, slow, technical gesture. Reads as a drawing being made. Never repeats. |
| 2 | Map module | scroll into view | Districts fade in with a 12 ms stagger ordered north→south, 500 ms total | Signals the map is composed of parts, which primes interaction |
| 3 | District | hover | §5.5 | — |
| 4 | District | click | §5.5 + panel swap | — |
| 5 | Layer toggle | click | Switch travels 180 ms; glyph legend item brightens; count number rolls with a 200 ms digit transition | The rolling count is the one piece of delight permitted; it confirms the filter fired |
| 6 | Panel sections | content change | 60 ms stagger, §6.3 | — |
| 7 | Tier badge | hover | Tooltip explains what the tier means | Tier labels are your vocabulary, not the industry's; define them in place |
| 8 | Watch-outs | scroll into view | Left border draws downward over 400 ms | Draws the eye to the highest-trust content on the page |
| 9 | Coverage matrix row | hover | Row tints; the corresponding district pulses once on the map above | **Cross-modal linking.** Small effort, disproportionate perceived sophistication. |
| 10 | CTA button | hover | Background fills left→right over 240 ms | — |
| 11 | Card image | hover | §6.4 | — |
| 12 | Section headings | scroll into view | Fade + 16px rise, 400 ms, once | — |

**Global motion rules.** Every duration between 120 ms and 500 ms except the hero draw. Easing is `ease-out` for entrances and `ease-in-out` for state changes; never `bounce`, never `spring` with visible overshoot — overshoot is playful, and playful is the opposite of what an EPC procurement head wants to feel. Every animation respects `prefers-reduced-motion`, collapsing to instant state changes with opacity-only transitions. Nothing loops. Nothing autoplays. Nothing pulses for attention. **An established consultancy's website does not fidget.**

---

## 9. Desktop layout (≥1280px)

```
┌──────────────────────────────────────────────────────────────────┐
│ Z1  HERO — 72vh                                                  │
│     Left 55%: eyebrow / H1 / 2-line standfirst / 2 CTAs          │
│     Right 45%: Karnataka silhouette, self-drawing, 8% opacity    │
│                brand wash, bleeding off the right edge           │
├──────────────────────────────────────────────────────────────────┤
│ Z2  ORIENTATION — 4 columns, 1px top rule, 120px tall            │
├──────────────────────────────────────────────────────────────────┤
│ Z3  MAP MODULE — 12-col grid, min-height 900px                   │
│  ┌────────┬─────────────────────────┬─────────────────────────┐  │
│  │ RAIL   │  MAP CANVAS             │  DISTRICT PANEL         │  │
│  │ 2 col  │  5 col   sticky         │  5 col   scrolls        │  │
│  │        │                         │                         │  │
│  │ Layers │   [Karnataka SVG]       │  Overview → District    │  │
│  │ Tiers  │    portrait, centred    │  dossier, §6.2 order    │  │
│  │ Divs   │                         │                         │  │
│  │ Count  │   Legend beneath        │  CTA pinned at bottom   │  │
│  └────────┴─────────────────────────┴─────────────────────────┘  │
├──────────────────────────────────────────────────────────────────┤
│ Z4  COVERAGE MATRIX — full width, sticky header, sortable        │
├──────────────────────────────────────────────────────────────────┤
│ Z5  GROUND INTELLIGENCE — 3 cards, equal columns                 │
├──────────────────────────────────────────────────────────────────┤
│ Z6  SERVICES IN CONTEXT — 6 items, 3×2                           │
├──────────────────────────────────────────────────────────────────┤
│ Z7  METHOD — 5 stages, horizontal, connected by a 1px rule       │
├──────────────────────────────────────────────────────────────────┤
│ Z8  HONEST LIMITS — 8 col text, 4 col grey mini-map              │
├──────────────────────────────────────────────────────────────────┤
│ Z9  CTA — full-bleed dark band                                   │
└──────────────────────────────────────────────────────────────────┘
```

**The map canvas is `position: sticky` within the module while the panel scrolls independently.** This is the central layout decision. District dossiers run to 700 words; if the map scrolled away, the user would lose the spatial context that gives the text meaning, and would have to scroll back up to change districts. Sticky map + scrolling panel keeps both the instrument and the reading surface live simultaneously. Constrain the sticky region to the module so the map releases cleanly at Z4 — an unbounded sticky element that follows the user into the footer is a classic and very visible bug.

**Container 1440px max with 80px gutters.** Wider feels like a marketing site; narrower wastes the panel. At ≥1600px, add whitespace rather than growing the map — an oversized state map starts to look like a tourism board.

---

## 10. Mobile (<768px)

**The desktop map does not survive the transition and should not be forced to.** A 375px-wide Karnataka gives Yadgir a tap target of roughly 18×22px against a 44px minimum. Shipping that is choosing to look sophisticated over being usable, and everyone can tell.

**Mobile architecture — list-first, map-second:**

```
Z1   Hero, stacked, silhouette moves behind the text at 6% opacity
Z2   Orientation, 2×2
Z3M  COVERAGE, restructured:
     ├─ Horizontal chip scroller: Solar Wind Hybrid PSP Transmission
     ├─ Segmented control: All | Core | Active | Statewide
     ├─ Collapsed Karnataka map — 240px tall, non-interactive,
     │  used purely as an orientation graphic. Filtered districts
     │  highlight in response to the chips above.
     │  A single text link: "Open full map ↗"
     ├─ Grouped district list, headed by division. Each row:
     │     District name · tier dot · layer glyphs · chevron
     └─ Tap → full-screen district sheet, slides up 280 ms,
        swipe-down or × to dismiss, ‹ › to step to adjacent districts
Z4M  Matrix becomes an accordion by division
Z5M  Cards stack, or a snap-scroll carousel
Z6M  Services as an accordion
Z7M  Method as a vertical timeline
Z8M  Honest limits, text only
Z9M  CTA, plus a sticky bottom bar appearing after 60% scroll depth
```

**"Open full map"** launches a full-screen landscape-oriented map view with pinch-zoom enabled — here zoom is justified, because the constraint is real. It is an opt-in mode, not the default, so it costs nothing to the majority who will never use it.

**The `‹ ›` stepper in the district sheet** replicates the desktop affordance of glancing at a neighbouring district. On mobile the user cannot see the map behind the sheet, so the adjacency has to be provided explicitly. Order the stepper geographically, not alphabetically — Koppal should step to Gadag and Ballari, not to Kodagu.

**Tablet (768–1279px):** map at 100% width above a full-width panel; filter rail becomes a horizontal bar. Do not attempt the three-column desktop layout below 1280px — the panel drops under ~380px and the dossier becomes unreadable.

---

## 11. Art direction and image selection

### Rules

Every image must be **real, Indian, and Karnataka-plausible**. One American desert solar farm with a Joshua tree in frame destroys the entire premise of a Karnataka specialisation page. Your audience has been to these sites.

**Get original photography.** A single two-day shoot across Pavagada, Koppal and Gadag — at ₹40,000–₹80,000 all-in, which is nothing against what this website is meant to win — produces the one asset no competitor can buy off a stock site. Ninety percent of Indian RE consultancy websites use the same six Shutterstock solar images, and a buyer who has seen those six images fifty times registers yours as different in under a second. **This is the highest-leverage spend on the entire project.** If the budget genuinely cannot stretch, use Unsplash/Pexels with strict Indian-terrain filtering and accept a materially weaker page.

### Subject hierarchy

| Priority | Subject | Why |
|---|---|---|
| 1 | **Land before development** — red-soil scrub, boundary stones, field bunds, dry rocky terrain | This is literally your product. Everyone else photographs finished plants; you photograph the thing you actually solve. Instantly differentiating. |
| 2 | **People at work in the field** — survey equipment, documents on a bonnet, a discussion at a field boundary | Land aggregation is a human process. Shows the work, shows Indian context, shows you were there. |
| 3 | **Infrastructure in landscape** — transmission towers crossing farmland, a substation at distance | Communicates the RoW and evacuation competency without a stock-photo feel |
| 4 | **Wide RE at distance** — a wind row along a ridgeline, panels to the horizon | Necessary scale-setting, but the most commoditised imagery. Use sparingly. |
| 5 | Close-ups of panels, blue sky, lens flare, glossy renders | **Never.** This is renewable-energy stock-photo cliché and it reads as startup. |

### Treatment

Consistent grade across every image: slightly desaturated, warm-neutral, high micro-contrast, no HDR, no heavy vignette. Hero and band images carry a subtle brand-tinted duotone at low intensity so photography and interface feel like one system. **No people looking at the camera. No smiling stock businesspeople. No handshakes.** Those three things are the visual signature of a template, and they are also the specific things Black & Veatch and Arup never do.

### Per-zone assignment

- **Z1 Hero:** no photograph. Type and the drawing map only. This is a confidence move — a hero that does not need an image reads as more senior than one that does. It also makes the hero fast, which is your Largest Contentful Paint.
- **Z3 Map module:** no imagery at all. The map is the image.
- **Z5 Cards:** one land-character photograph per featured district, tonally matched.
- **Z7 Method:** an abstract line-diagram, not photography.
- **Z8 Honest limits:** the Western Ghats or the coast — a landscape that visually explains *why* those districts are excluded.
- **Z9 CTA:** a dark, wide, low-contrast landscape at heavy overlay.

---

## 12. Content

### Z1 Hero

> **KARNATAKA** *(eyebrow, tracked uppercase)*
>
> # We know this ground.
>
> Bolamudi Enterprise develops the land, approvals and right of way that utility-scale renewable projects in Karnataka stand on. This is a district-by-district account of how that actually works here — what the land looks like, where the approvals slow down, and what stops projects.
>
> `[ Explore the map ]`  `[ Request a district briefing ]`

**Why "We know this ground."** Four words, one syllable each. It is a knowledge claim, not a capability claim — which is precisely the claim you can substantiate. It is unusable by any competitor who has not done the work, because the page underneath either proves it or exposes it. And it doubles as a pun on land that a land-aggregation firm has earned the right to make.

**Why the standfirst names limitations.** "Where the approvals slow down, and what stops projects" tells the reader in the first six seconds that this page contains uncomfortable truths. That framing is what buys attention from a cynical buyer who has read forty consultancy homepages this quarter.

### Z2 Orientation strip

> **How to read this map**
>
> **Core Operating Districts** — where we work continuously and hold current ground knowledge.
> **Active Coverage** — where we operate on project mandate.
> **Statewide Capability** — where we can mobilise, with lead time.
> **Not claimed** — districts without meaningful utility-scale renewable potential. We would rather say so.

That last line is the most valuable copy on the page. It reframes every other claim as considered rather than promotional.

### Z8 Honest limits — full draft

> ### Where we don't operate
>
> Karnataka's renewable resource is not evenly distributed, and neither is useful expertise.
>
> The coastal districts and much of the Malnad belt do not support utility-scale solar or wind at competitive tariffs — rainfall, forest cover, terrain and land fragmentation all work against it. Pumped storage is a different question in that geography, and one we follow closely, but hydrological and forest clearance work there is a specialist discipline with its own institutional relationships. We will say honestly where our knowledge ends.
>
> We also do not take on land aggregation where the parcel structure or the local situation means the timeline we would have to quote is one no developer should accept. It is faster and cheaper for everyone to learn that in the first conversation.
>
> If a district is outside what we claim, we will usually still know who to point you to.

That final line converts an admission into a demonstration of network depth. The section that appears to give away business is the one that earns it.

### Sample dossier — structure demonstrated

> ## Koppal
> *Kalaburagi Division · Core Operating District · Solar · Wind · Transmission*
>
> **Resource profile.** Strong direct normal irradiance across the northern taluks with a workable wind regime on the higher ground; among the districts the state has identified for ultra-mega solar development.
>
> **Land character.** *[Holding patterns, typical contiguous block achievable, terrain and soil constraints, the classification issues that recur here.]*
>
> **Approvals character.** *[Which clearances dominate, realistic sequencing, where the queue actually forms.]*
>
> **Evacuation character.** *[Qualitative grid context, corridor geography, what to confirm before committing to land.]*
>
> **What we do here.** *[2–4 services in district-specific language.]*
>
> **Watch-outs.** *[2–3 named failure modes, in the founder's voice.]*
>
> `[ Request a briefing on Koppal ]`

**The bracketed sections must be written by the founder, in his own words, and lightly edited — not written by a copywriter and not written by me.** This is not a process preference; it is the entire value proposition of the page. A copywriter will produce fluent, plausible, generic text, and generic text on this page is worse than no page. Practical method: interview him for forty minutes per Tier 1 district, record it, transcribe, and edit for structure while preserving his phrasing and his hedges. The hedges are the credibility. "Usually about four months, but I've seen it take a year when the joint holding is contested" is worth more than any polished sentence.

**Honest warning about effort.** Ten Tier 1 dossiers at 500 genuine words each is roughly seven hours of the founder's time and two weeks of editorial work. **This is the step where this project most likely fails** — not in the build. If that time is not committed, cut Tier 1 to four districts and ship four excellent dossiers. Four real ones beat thirty-one hollow ones by a margin that is not close.

---

## 13. SEO architecture

### Structure

The map alone is a poor SEO asset — one URL, and search intent in this market is district-specific. So the page is the hub of a cluster:

```
/karnataka                          Hub. Target: "renewable energy land
                                    acquisition Karnataka",
                                    "solar land aggregation Karnataka"
/karnataka/[district]               Spoke, Tier 1 + Tier 2 only.
                                    Target: "solar project land Koppal",
                                    "land aggregation Gadag",
                                    "wind project land Vijayapura"
/insights/[topic]                   Supporting: land conversion process,
                                    RoW procedure, approvals sequencing
```

**Only generate spoke pages for districts with genuine dossier content.** Thirty-one thin auto-generated district pages is textbook programmatic doorway-page behaviour and is exactly what Google's helpful-content systems demote. Ten strong pages will outrank thirty-one weak ones, and will not put the domain at risk.

### Per-page

**Title:** `Renewable Energy Land & Approvals in Koppal | Bolamudi Enterprise` — the district first, because that is the query.

**Meta description:** lead with the specific and useful, not the promotional. `Land character, approvals sequencing and evacuation context for utility-scale solar and wind development in Koppal district, Karnataka.`

**H1:** exactly one per page. On the hub, "We know this ground." Do not make the H1 a keyword string — the copy is a stronger asset than the marginal ranking signal, and Google has been fine with this for a decade.

**Schema.org:** `Organization` with `areaServed` as an array of `AdministrativeArea`, plus `Service` entities for the six offerings, plus `BreadcrumbList` on spokes, plus `FAQPage` where a district page carries genuine Q&A. Do not mark up anything not visible on the page.

**Crawlability of the map.** Because the SVG is inline in server-rendered HTML with `<title>` on each path and real district names in the DOM, the map itself is indexable. The Z4 coverage matrix is the real workhorse though — it is plain semantic HTML containing every district name and its layer assignments, which is precisely what a crawler wants and precisely why building it was not redundant.

**Internal linking.** Every district panel deep-links to its spoke. Every spoke links back to the hub and laterally to two geographic neighbours. That lateral link pattern builds a genuine topical cluster rather than a hub-and-spoke star, and it mirrors how the user actually thinks — a developer looking at Koppal is looking at Gadag next.

**Local signals.** NAP consistency, a Google Business Profile with the Karnataka service area, and — highest value of all — get the RE Land & Approvals Primer cited by Indian energy trade press. One link from a Mercom India or JMK Research citation outperforms a hundred directory listings.

**Realistic expectation.** These are low-volume, extremely high-intent queries. "Land aggregation Koppal" might see thirty searches a month. Thirty visits from people who need exactly this is a better commercial outcome than three thousand from people who don't. Do not let anyone benchmark this page on traffic volume.

---

## 14. Accessibility

Non-negotiable, and in this sector it is also a procurement checkbox — large IPPs and infrastructure firms increasingly run vendor website accessibility checks.

- Every district `<path>` is `role="button"`, `tabIndex={0}`, with `aria-label="Koppal, Core Operating District, solar and wind"`.
- Arrow keys move between districts in **geographic** order, not DOM order. Requires a precomputed adjacency map, generated at build time from the topology. Alphabetical or DOM-order tabbing through a map is disorienting.
- Selection change announces via an `aria-live="polite"` region: "Koppal selected. Core Operating District."
- Contrast: all four tier fills against both their strokes and their label text must clear 4.5:1 for text and 3:1 for the graphical boundary. **Test this before finalising the palette** — tier ramps are where contrast failures always appear, because designers pick them for aesthetic separation rather than measured separation.
- Colour is never the only channel: tier is also encoded by hatch texture and by an explicit text badge in the panel.
- The Z4 matrix is a genuine `<table>` with `<caption>` and `scope` attributes, and it is the declared accessible alternative to the map. Link to it from a skip-link inside the map module.
- `prefers-reduced-motion` collapses all motion to instant, opacity-only transitions.

---

## 15. Performance targets

| Metric | Target | Notes |
|---|---|---|
| LCP | < 1.8 s | Text hero with no image makes this easy — one more reason for that decision |
| CLS | < 0.05 | Reserve the map's aspect ratio in CSS before hydration |
| INP | < 150 ms | Hover state changes must be pure CSS, never React state. A React re-render per `mousemove` over 31 paths will feel sticky and is the most likely performance bug in this build. |
| Map payload | < 60 KB uncompressed | Enforce in CI: fail the build if `districts.ts` exceeds budget |
| Total JS | < 180 KB gzipped | Framer Motion is ~34 KB; import selectively via `LazyMotion` + `domAnimation` |

All district content is statically generated. Nothing on this page needs a runtime data fetch, and adding one would be an architectural mistake.

---

## 16. Future scalability

Design the data model now so these are content changes, not rebuilds.

**Phase 1 (launch).** Static tiers, static dossiers, five layers, 8–10 Tier 1 districts.

**Phase 2 (6 months).** Promote districts between tiers as engagements accumulate — pure CMS field change. Add a sixth layer (`BESS` or `Green Hydrogen`) — the layer array is open, so no schema migration. Add per-district `/insights` cross-links.

**Phase 3 (12 months).** **Taluk drill-down** for Tier 1 districts only. This is the natural next escalation of the same "we know this ground" argument and it will be genuinely unmatched by any competitor. Build it as an optional `subRegions[]` array on the district record so the same components render both levels; a district with no `subRegions` simply renders as it does today. Doing it for all 31 would be unmaintainable and dishonest — restricting it to Tier 1 is both feasible and *more* persuasive, because the asymmetry itself proves the tiering is real.

**Phase 4 (18 months+).** Anonymised engagement markers ("mandate active", "completed 2027") once you have your own track record independent of the founder's prior employment. **This is the moment the page finally becomes a genuine track-record map** — which is where you wanted to start. Design the schema for it now with a nullable `engagements[]` field, so the transition is additive and the page you ship today grows into the page you actually want without a redesign.

**Phase 5.** Other states, if the strategy ever changes. The entire system is `{ state, regions[] }` — a Karnataka-only page today, an Andhra Pradesh page later, with zero component changes. Do not build it now; just don't hardcode "Karnataka" into component internals.

**Content model to lock at build time:**

```ts
type District = {
  id: string; name: string; slug: string;
  division: 'Bengaluru'|'Mysuru'|'Belagavi'|'Kalaburagi';
  tier: 0 | 1 | 2 | 3;
  layers: Layer[];              // open union — extensible
  path: string; centroid: [number, number];
  adjacency: string[];          // for keyboard nav + lateral SEO links
  dossier?: Dossier;            // absent ⇒ no spoke page generated
  subRegions?: District[];      // Phase 3
  engagements?: Engagement[];   // Phase 4 — nullable by design
};
```

**Two hard schema constraints, enforced in code review:** `Dossier` has no numeric fields, and `Engagement` has no client-name field. Make the misrepresentation risk in §0 a type error, not a copywriting guideline. Guidelines get forgotten in eighteen months; types don't.

---

## 17. What will kill this page

Ordered by likelihood.

1. **The dossiers never get written properly.** By far the most probable failure. Mitigation: cut Tier 1 to four districts and ship those four excellently.
2. **Someone insists on numbers.** A stakeholder will want "20+ years · 5 GW · 10,000 acres" on the hero. It is unverifiable, it belongs to a former employer, and a diligence analyst will ask for the breakdown. Refuse it.
3. **Tier 0 gets deleted for looking negative.** Someone will say the grey districts look like weakness. They are the reason the coloured ones are believed. Refuse this too.
4. **The map gets built with a stale 27- or 30-district boundary file.** Verify Vijayanagara is present before a single line of component code is written.
5. **Mobile ships as a shrunk desktop map.** Roughly half your traffic, unusable, and unusable in exactly the way that reads as unprofessional.
6. **Hover is wired to React state** and the map feels laggy. Pure CSS for hover; React state only for selection.
7. **Legal exposure from procedural content.** The dossiers describe statutory processes. Add a short, plain footer note: this is general information about development processes in Karnataka, not legal advice, and land and approval requirements are parcel-specific. One sentence, low prominence, real protection.

---

*Sources for factual grounding: [List of districts of Karnataka](https://en.wikipedia.org/wiki/List_of_districts_of_Karnataka) · [Installed wind capacity by district, Karnataka](https://www.statista.com/statistics/1454270/installed-wind-capacity-by-district-karnataka-india/) · [Pavagada Solar Park](https://en.wikipedia.org/wiki/Pavagada_Solar_Park) · [KREDL — Pavagada Solar Park](https://kredl.karnataka.gov.in/new-page/Pavagada%20Solar%20Park/en) · [Sharavathi Pumped Storage Hydropower Project](https://en.wikipedia.org/wiki/Sharavathi_Pumped_Storage_Hydropower_Project) · [Karnataka aiming to add 19.2 GW renewable energy by 2030](https://www.deccanherald.com/india/karnataka/karnataka-aiming-to-add-19-2gw-in-renewable-energy-by-2030-3193399) · [Karnataka Land Reforms (Amendment) Ordinance, 2020](https://www.mondaq.com/india/corporate-and-company-law/969618/the-karnataka-land-reforms-amendment-ordinance-2020-a-brief-note)*
