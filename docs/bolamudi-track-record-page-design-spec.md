# Bolamudi Enterprise — Projects / Track Record Page

**Design specification & strategic review**
Date: 30 August 2026
Scope: Projects page within the larger Bolamudi Enterprise website project
Roles applied: Product Strategist · UX Designer · UI Designer · Creative Director · Content Strategist · SEO Consultant · Frontend Architect

---

## 0. Project context

**Company:** Bolamudi Enterprise — renewable energy project development support, based in Karnataka, India.

**Asset:** Founder with 20+ years executing utility-scale Solar, Wind, Hybrid and Pumped Storage projects across Karnataka, gained while employed at a reputed company.

**Services:** Land Aggregation · Government Liaison · Statutory Approvals · Renewable Energy Project Facilitation · Transmission Right of Way · Project Development Support

**Target audience:** Renewable Energy Developers · IPPs · Infrastructure Companies · Investment Firms · EPC Companies

**Required perception:** Trust · Professionalism · Experience · Execution Capability · Engineering Excellence

**Reference tier:** Black & Veatch, AECOM, Arup, WSP, Jacobs, Siemens Energy, ReNew. Explicitly NOT a startup aesthetic.

**Stack:** Next.js · TypeScript · Tailwind CSS · shadcn/ui · Framer Motion · Responsive

**Constraints discovered during briefing:**

- No projects documented yet — no written case studies, no compiled data
- No photography of any kind
- Client names are confidential

---

## 1. Blunt assessment — read before anything else

The design is not the hard part. Three problems outrank it.

### 1.1 Attribution is a legal risk, not a copy problem

The brief states the founder's experience was gained *"while working for a reputed company."* Those projects were executed under that company's contracts, under NDAs the founder almost certainly signed. Presenting them on a Bolamudi page as "our projects" is misrepresentation, and any developer running diligence will surface it in the first meeting.

This must be handled explicitly, on the page, or the page should not ship.

### 1.2 Stock photography will actively damage the brand

The target audience — IPP project heads, EPC business development teams — has seen the same stock solar array hundreds of times. A generic hero image is a louder "we are new and small" signal than having no image at all. Photography cannot be faked at this tier.

### 1.3 The bottleneck is the founder's time, not the design budget

Twelve engagements × roughly 350 words of Challenge / Approach / Outcome is approximately two full working days of the founder's effort. If that time is not committed, this page cannot exist in any premium form. Decide this before commissioning design or development.

---

## 2. Strategic reframe — "Track record", not "Projects"

| Item | Decision |
| --- | --- |
| Nav label | Track record |
| Index URL | `/track-record` |
| Detail URL | `/track-record/220-mw-solar-koppal-karnataka` |
| Content unit | "Engagement", not "case study" or "project" |

**Reasoning.** "Projects" promises company-delivered work with client logos and site photography. Bolamudi has neither. Black & Veatch uses "Projects" because they have ten thousand of them. Boutique advisory firms built on founder-led experience use "Track record" or "Experience" — it is the established convention for exactly this situation. Using the honest word costs nothing and pre-empts the diligence question.

### 2.1 The attribution statement

Placed immediately **before** the grid — not in a footer, not in fine print:

> Engagements listed were executed by our founder in senior project development roles prior to founding Bolamudi Enterprise. Client identities are withheld under confidentiality obligations. All figures are verifiable on request.

**Why this builds trust rather than undermining it.** Sophisticated buyers reward disclosed limitations and punish discovered ones. The load-bearing clause is *"verifiable on request"* — it converts an unverifiable claim into a standing offer, which is a materially different thing.

---

## 3. Solving the zero-photography problem

Four visual layers. Built once, reused across every card. No photography required.

| Layer | Description | Rationale |
| --- | --- | --- |
| **Cartographic** | Stylised Karnataka district SVG with project location marked, rendered in brand navy | Honest, ownable, perfectly consistent, unmistakably technical. Built from open district boundary data. |
| **Data plate** | Oversized capacity numeral with spec table as the visual element | The numbers are the asset. Reads as an engineering datasheet. |
| **Line schematic** | Single-weight isometric line drawings: solar block, wind turbine, PSP reservoir pair, transmission tower | Custom set, not an icon library. Four drawings cover the entire portfolio. |
| **Contour wash** | Muted elevation-contour texture as card background | Ties visually to land, which is the actual differentiator. |

Rotate layers by project type so the grid reads as varied and deliberate rather than broken.

**Architectural rule:** design the card with the image as a **slot, not a dependency**. When real site photography exists in 12–18 months, layer 1 is swapped and nothing else in the system changes.

---

## 4. Page architecture (desktop)

### 4.1 Hero — 52vh, not full viewport

Full-viewport heroes on interior pages are a SaaS convention. Established consultancies use short, dense interior heroes.

- Background: muted Karnataka map with **all** project markers plotted
- Effect: geographic depth is communicated before a single word is read
- H1: "Track record"; supporting line beneath

### 4.2 Aggregate metrics band

The single most important element on the page. A visitor who reads only this band must leave convinced.

| Metric | Example value |
| --- | --- |
| Acres aggregated | 11,280 |
| Landowners engaged | 4,100+ |
| MW facilitated | 2,437 |
| Districts | 9 |
| Years | 20 |

**Two decisions:**

1. **Lead with acres and landowners, not MW.** Anyone can claim MW. Nobody can fake 4,100 landowner negotiations in Karnataka — that is the moat, and it is the number the buyer is actually afraid of.
2. **Use unrounded figures.** "2,437 MW" is credible. "2,500+ MW" reads as marketing. Precision is the trust signal. Every figure must be defensible in a first meeting.

### 4.3 Attribution statement

Bordered, restrained, one paragraph. Frames everything below it. (Copy in §2.1.)

### 4.4 Filter bar

Sticky on scroll. See §6.

### 4.5 Engagement grid

- 3-up desktop (≥1280px) · 2-up tablet · 1-up mobile
- 24px gutters, 12px radius
- **0.5px hairline borders, not drop shadows.** Shadow-heavy cards read consumer/startup; hairline borders read engineering drawing.

### 4.6 Capability matrix (optional, high leverage)

A table with services down the side and project types across the top, marked where delivery occurred. This is a Black & Veatch move, takes minimal effort to build, and converts a thin portfolio into a demonstration of breadth.

### 4.7 Close — founder CTA, not a form

Named human, photograph, LinkedIn, direct line. On a page whose entire purpose is trust, the founder is the only asset available. Hiding him behind a generic "Contact us" form wastes it.

---

## 5. Engagement data model

### 5.1 Fields specified in the brief

Location · Capacity · Services · Project Type · Status · Images · Timeline · Challenges · Solutions · Impact

### 5.2 Fields to add (higher value than several of the above)

| Field | Why it matters |
| --- | --- |
| **Acres aggregated** | The difficulty signal. Land is the real product. |
| **Landowners engaged** | Proves the genuinely hard part of the work. |
| **Evacuation voltage** (110 / 220 / 400 kV) | Speaks the buyer's technical language immediately. |
| **Approvals secured** — named specifically | The strongest trust device on the entire site. |

Name the actual approvals: KREDL registration, Section 109 land conversion, KPTCL evacuation approval, CEIG clearance, forest clearance, KERC filings.

**Reasoning:** the audience screens consultants on whether they actually know the process. Naming the correct statutes and authorities is more persuasive than any testimonial that could realistically be obtained.

### 5.3 Confidentiality rules

- Location resolution: **district-level only**. Village-level identifies the client.
- Titles are anonymised and descriptive: "220 MW solar park — Koppal district, Karnataka"
- No client logos. No named testimonials.
- If one anonymised quote can be obtained, attribute by role: *"Project Head, 500 MW IPP"*. Worth more than five named-but-generic ones.

### 5.4 Narrative structure

Challenge / Approach / Outcome, approximately 120 words each.

Written in specifics:

> "Seventeen landowners held inherited undivided titles; resolved via family settlement deeds over nine months."

Not in abstractions:

> "We overcame complex land challenges."

---

## 6. Filtering

**Facets:** Project type · Service · District · Status · Capacity band

| Decision | Reasoning |
| --- | --- |
| **Chips, not dropdowns** | Dropdowns hide the taxonomy behind a click; chips display it. On a page whose purpose is proving breadth, the filter UI is itself a credibility exhibit — a visitor who never filters still sees "Solar / Wind / Hybrid / Pumped storage / Transmission". |
| **Multi-select; OR within a facet, AND across facets** | Matches how users actually reason about the choice. |
| **State in URL query params** (`?type=solar&district=koppal`) | Non-negotiable. Makes filtered views shareable, linkable from service pages, and indexable. |
| **Client-side filtering** | Under 50 records. No API, zero latency. |
| **Live result count** — "Showing 7 of 14 engagements" | Removes uncertainty about whether the filter fired. |
| **Empty state offers an exit** | "No engagements match these filters" + Clear all + "Tell us about your project." Never a dead end. |

### 6.1 Mobile filtering

Sticky bottom-right Filter button carrying an active-count badge → full bottom sheet with accordion facets and Apply / Clear actions.

**Do not** use a horizontally-scrolling chip strip. Options past the fold go unused; the bottom sheet shows everything.

---

## 7. Detail page

**URL:** `/track-record/[slug]` — descriptive, keyword-bearing, no client name.

**Layout:** sticky specification sidebar alongside scrolling narrative. The sidebar keeps hard data visible while the narrative is read, mirroring how technical readers cross-check claims against numbers.

**Section order:** Overview → Scope of services → Challenge → Approach → Outcome → Timeline (horizontal milestone rail) → Related engagements

---

## 8. SEO

### 8.1 Real search demand

Long-tail and geographic, not "renewable energy company":

- land aggregation for solar projects Karnataka
- solar project land acquisition consultant Karnataka
- KPTCL evacuation approval consultant
- pumped storage project development India
- renewable energy government liaison Karnataka

### 8.2 Why this page is the highest-value SEO asset on the site

It is the only page where district names, technologies, capacities and kV levels naturally co-occur. That co-occurrence is the entity signal Google needs in order to associate Bolamudi Enterprise with Karnataka renewable development.

### 8.3 Implementation

| Item | Specification |
| --- | --- |
| **Title** | Track record — utility-scale solar, wind and pumped storage projects in Karnataka \| Bolamudi Enterprise |
| **Schema — index** | `ItemList` |
| **Schema — sitewide** | `BreadcrumbList`, `Organization` |
| **Schema — detail** | `CreativeWork` with `about` and `spatialCoverage` (Place, addressRegion: Karnataka) |
| **Do not** | Fake `Product` or `Review` markup. There is no clean schema.org type for a consulting engagement; inventing one is a manual-action risk. |

**Filter URL handling.** Canonical filtered permutations back to `/track-record` to prevent index bloat — **except** approximately 8 curated combinations (one per technology, one per major district). Those receive self-canonical URLs, unique H1s and ~80 words of unique intro copy, becoming geo landing pages.

**Internal linking.** Each service page links to its filtered track-record view; each detail page links back to the services used. Bidirectional.

**Images.**

- SVG maps require real alt text: *"Location of the 220 MW solar park in Koppal district, Karnataka"*
- Every detail page needs a build-time generated OG image via `next/og`. Without it, WhatsApp shares — which is how deals actually circulate in this market — render as grey boxes.

---

## 9. Animation (Framer Motion)

Restraint is itself the brand signal. Established engineering firms animate almost nothing.

| Element | Motion specification |
| --- | --- |
| Cards on scroll | opacity 0→1, y 12px→0, 400ms, `cubic-bezier(0.22, 1, 0.36, 1)`, 40ms stagger, `once: true`, viewport margin −80px |
| Metric counters | count up once, 1200ms ease-out |
| Filter changes | Framer Motion `layout` prop on grid items, 250ms — cards reposition rather than pop |
| Card hover | border-colour shift + 2px lift, 150ms; no scale beyond 1.02 |
| Page transitions | none, or 150ms crossfade |

The metric counter is the single permitted flourish, and it is on-brand because the numbers **are** the argument.

**`prefers-reduced-motion`:** disable all transforms, retain opacity transitions only.

**Explicitly banned** — every one of these reads "startup", the named failure mode:

scroll-jacking · horizontal scroll sections · parallax · 3D tilt · animated gradients · marquees · re-triggering counters

---

## 10. Trust-building mechanisms, ranked

1. **Disclosed confidentiality and attribution statement** — owning the limitation
2. **Quantified, unrounded metrics** — 2,437 acres beats "2,500+ acres"
3. **Founder attribution** — name, photograph, LinkedIn, direct line
4. **Regulatory literacy on display** — naming KERC, KREDL, Section 109, KPTCL, CEIG, forest clearance
5. **Status honesty** — "In development" marked as such, never softened
6. **No client logos, no fabricated testimonials** — one anonymised role-attributed quote beats five generic named ones

---

## 11. Open dependencies

| # | Item | Owner |
| --- | --- | --- |
| 1 | Content capture questionnaire completed for each engagement | Founder |
| 2 | Verification of every aggregate metric (must survive a first-meeting challenge) | Founder |
| 3 | Legal comfort on attribution language vs. prior employment terms | Founder / counsel |
| 4 | Karnataka district boundary SVG asset | Design |
| 5 | Four-drawing technical line-schematic set | Design |
| 6 | Founder portrait photograph | Photography |

**Content capture fields required per engagement:** district · capacity · technology · date range · acres aggregated · landowner count · evacuation voltage · approvals list · Challenge / Approach / Outcome paragraphs

---

## 12. Sequencing recommendation

Do not build the Track record page first. Priority order:

1. Services pages — establishes what is sold
2. Founder / About page — establishes who is selling it
3. Track record page — establishes proof

Proof without a claim to prove is wasted. The Track record page also depends on the services taxonomy existing, since filters and internal links reference it.
