# Bolamudi Enterprise — Services Page
## Complete Design, Content & SEO Specification

Version 1.0 · August 2026
Prepared as: Product Strategy · UX · UI · Creative Direction · Content Strategy · SEO · Frontend Architecture

---

# PART 0 — THE STRATEGIC PROBLEM, STATED HONESTLY

Before any layout decision, this has to be settled, because everything downstream depends on it.

**Bolamudi is a single-promoter firm selling a service that is easy to confuse with brokerage.**

"Land aggregation" and "government liaison" are, to a sceptical developer, the two phrases most associated with informal middlemen. A Head of Project Development at a serious IPP has been burned by a "consultant with contacts" at least once. They are not asking *can you do this*. They are asking *are you a firm or are you a person with a phone*.

Every design decision in this document serves one objective:

> **Prove that Bolamudi runs a documented, auditable process — not a relationship.**

That single objective produces the design language:

| Because we must prove... | The page does... | Not... |
|---|---|---|
| Process, not influence | Numbered stages, named forms, named acts, deliverable checklists | Vague "we handle everything" claims |
| Institutional permanence | Restrained typography, near-zero motion, sharp corners, generous whitespace | Gradients, glass cards, animated counters, illustrations |
| Domain depth | Real statute names, real thresholds, real timelines | Generic renewable-energy stock language |
| Auditability | Weekly registers, status reports, handover files as named artefacts | "Regular updates" |
| Scale competence | Acres, MW, districts, spans, survey numbers | "Trusted by many" |

**The single highest-leverage creative decision on this page: show the paperwork.**
Nobody in this category does it. Competitors show solar panels at sunset. Bolamudi shows a parcel register, a corridor risk map, a statutory register. That is the entire differentiation, and it is free.

---

# PART 1 — INFORMATION ARCHITECTURE

## 1.1 The structural correction

You listed nine services. They are not nine services. They are **five capabilities applied across four asset classes.**

- **Capabilities (what we do):** Land Aggregation · Government Liaison · Statutory Approvals · Transmission ROW · Project Development Support
- **Sectors (what we do it on):** Solar · Wind · Hybrid · Pumped Storage

**Why this matters, concretely:**

1. **Positioning.** A flat grid of nine says "we do nine unrelated things" — the signature of a small firm padding a list. A 5×4 matrix says "we have a repeatable methodology that scales across technologies." That is the AECOM / Black & Veatch / Arup grammar.
2. **SEO.** Nine flat `/services/*` pages would put `/services/solar` in direct keyword competition with `/services/land-aggregation` — both would target "solar land Karnataka." Separating the axes gives each page a distinct intent to own.
3. **Sales.** The matrix creates a natural cross-sell: a developer arriving for Wind ROW discovers four adjacent capabilities on the same page.

**Nothing is lost.** All nine items still appear on the Services page. Five as primary capability cards, four as a Sectors band directly below. The user's full list is intact; only the hierarchy is corrected.

## 1.2 Routing

```
/services                              ← Hub. All nine items visible.
/services/land-aggregation
/services/government-liaison
/services/statutory-approvals
/services/transmission-right-of-way
/services/project-development-support

/sectors/solar
/sectors/wind
/sectors/hybrid
/sectors/pumped-storage
```

**Why `/sectors/*` and not `/services/*` for the four technologies:**
URL semantics should match content semantics. Google reads the path as a topical signal. `/services/solar` tells the crawler "solar is a service we sell," which is false and dilutes the service cluster. `/sectors/solar` reads correctly and lets the two clusters rank independently.

**Why hub + children and not one long page:**
Nine full Problem→Solution→Process→Deliverables blocks on a single page is roughly 9,000 words and a 25-screen scroll. Two failures: (a) a buyer researching only ROW must scroll past six irrelevant sections, (b) one page cannot rank for nine distinct queries — Google will pick one H2 and ignore the rest. Nine SSG pages, each 900–1,400 words, is nine rankable assets and nine linkable sales assets you can send individually in an email.

## 1.3 The internal link mesh

This is the part most agencies skip and it is worth more than the design.

- Every `/sectors/*` page links to all five `/services/*` pages, contextualised ("Land aggregation for wind — ridge access and crane pad corridors →")
- Every `/services/*` page links to all four `/sectors/*` pages
- Both link back to `/services` hub and forward to `/contact`
- Result: **~72 contextual internal links** forming a tight topical cluster. This is how a nine-page site outranks a fifty-page competitor site on niche terms.

## 1.4 Global navigation change required

The header `Services` item becomes a **NavigationMenu mega-panel** on desktop:

```
┌─ SERVICES ─────────────────┬─ SECTORS ──────────┬──────────────────┐
│ Land Aggregation           │ Solar              │  All Services →  │
│ Government Liaison         │ Wind               │                  │
│ Statutory Approvals        │ Hybrid             │  20+ years of    │
│ Transmission Right of Way  │ Pumped Storage     │  Karnataka       │
│ Project Development Support│                    │  execution       │
└────────────────────────────┴────────────────────┴──────────────────┘
```
Each item shows title + one-line descriptor. Mobile: `Sheet` drawer with two collapsible groups.

---

# PART 2 — CONTENT MODEL

## 2.1 The section sequence you specified, with two additions

You specified: **Problem → Solution → Process → Deliverables → CTA**. That is correct and I am keeping it. I am adding two sections, and here is why each earns its place:

| # | Section | Status | Rationale |
|---|---|---|---|
| 1 | **Problem** | yours | Must be written in the buyer's language, naming specific failure modes. Generic problem statements ("land acquisition is complex") are worse than no problem statement — they signal you have never done it. |
| 2 | **Solution** | yours | One paragraph. The commitment, not the description. |
| 3 | **Scale & Context** | **added** | Between Solution and Process. Without it, Process reads as theory. This band carries acreage, districts, MW, spans — the numbers that make the Process credible. Without proof, a process diagram is just a flowchart anyone could draw. |
| 4 | **Process** | yours | The core of the page. Numbered, named, with statutory references. |
| 5 | **Deliverables** | yours | A checklist of physical artefacts. This is what converts. |
| 6 | **Engagement Model** | **added** | Between Deliverables and CTA. This buyer needs to know whether it is retainer, per-acre, milestone-linked or success fee *before* they contact you. Omitting it produces unqualified enquiries and quiet drop-off. It also signals commercial maturity — vague pricing reads as "depends who's asking." |
| 7 | **CTA** | yours | Specific, low-commitment, time-bound. |

## 2.2 CTA doctrine

**Never "Contact Us."** It asks the buyer to do the work of deciding what to say.

Every CTA on this site follows: **specific artefact + specific timeframe.**

- "Send us your project polygon. We'll return a land feasibility read in 10 working days."
- "Share your approval schedule. We'll mark where it will slip."
- "Send us your line route. We'll walk it and report in three weeks."

Three CTA tiers used consistently:
- **Primary (solid ink button):** the offer above — one per section end
- **Secondary (ghost + underline):** "Download the [X] method note (PDF)" — captures the 90% not ready to talk
- **Persistent (mobile sticky bar, desktop header):** "Discuss a project" + a `tel:` link, because this buyer calls

---

# PART 3 — THE SERVICES HUB PAGE (`/services`)

## 3.1 Section-by-section, desktop

### S1 · Hero

**Layout:** Full-bleed, 78vh (not 100vh — a partial next-section reveal proves there is substance below and lifts scroll rate materially). 12-col grid, content in cols 1–7, left-aligned.

**Background:** One wide, desaturated photograph of Karnataka project terrain — open scrubland with a transmission line receding to the horizon, or a Chitradurga ridge with turbines at distance. Ink scrim at 72% left → 25% right, plus a subtle bottom vignette so the scroll cue stays legible.

**Why terrain and not equipment:** Your product is *ground* — the ability to assemble, clear and connect land. A close-up of a solar module says "we install panels." Land says "we secure the ground your project stands on." It also visually differentiates from every RE company website in India, which all use the same three module-array photographs.

**Content:**
- Eyebrow (mono, 12px, letter-spaced, ochre): `SERVICES`
- H1 (56px desktop, tracking -0.02em, 3 lines max): *"Land, approvals and grid access for Karnataka's utility-scale renewable projects."*
- Sub (19px, 60ch, 78% opacity): *"Twenty years of executing solar, wind, hybrid and pumped storage development across Karnataka's revenue districts — from first survey number to corridor clearance."*
- Buttons: `[ Discuss a project ]` solid · `[ Download capability statement ]` ghost
- Bottom rule with four inline stats, mono numerals, separated by hairlines: `20+ YEARS` · `9 DISTRICTS` · `UTILITY-SCALE ONLY` · `SOLAR · WIND · HYBRID · PSP`

**Why the stat rule sits inside the hero:** it front-loads proof before the buyer has decided whether to keep scrolling. Stats parked in a later band are seen by ~40% fewer visitors.

### S2 · Positioning statement

**Layout:** Bone background, single centred column, max 720px, 100px vertical padding. No image, no card, no icon. Deliberately austere.

**Content:** 55–70 words at 24px, then a 3px ochre rule beneath.

> "Renewable projects in Karnataka do not fail on technology. They fail on land title, on a file waiting at a Taluk office, and on one landowner in the middle of a forty-kilometre corridor. We remove those three failures. Everything we do is documented, submitted through official channels, and handed over in a form your lender's counsel can audit."

**Why this section exists:** it is the thesis. It also pre-empts the influence-peddling objection in the last sentence, before the buyer forms it. Placing it immediately after the hero — before any service card — means it is read by nearly everyone.

### S3 · Capability grid (the five services)

**Layout:** 12-col, `md:grid-cols-2 lg:grid-cols-3`. Five cards. **The sixth cell is not empty and not a stretched card** — it is a bordered panel containing a short "How we're engaged" note and a link to Engagement Models. Leaving an orphan gap or stretching card 5 to double width both look like accidents.

**Card anatomy (top → bottom):**
1. Mono index numeral, ochre, 12px: `01`
2. Lucide icon, 24px, 1.5px stroke, ink, top-left, **never in a coloured circle**
3. Title, 22px semibold
4. One-line descriptor, 15px, 68% ink
5. Hairline separator
6. `THE PROBLEM IT SOLVES` — mono micro-label + one sentence. **This is the differentiating element.** Every competitor card describes the service; this one names the buyer's pain on the card itself, so value is understood without a click.
7. `Explore →` ghost link

**Card styling:** 1px border `#E2DDD6`, radius 2px, **no shadow**, background Bone. Hover: border darkens to ink, a 3px ochre bar wipes in along the top edge over 180ms, `translateY(-2px)`. Nothing else moves.

**Why 2px radius and no shadow:** border-radius is one of the strongest unconscious signals of category. `rounded-2xl` + soft shadow is the visual signature of SaaS and startups. Sharp, bordered, flat surfaces read as institutional documents. This one token does more brand work than any other decision on the page.

### S4 · The Development Sequence — **the section that wins the page**

**Layout:** Ink background (dark band — the only one on the page, which is why it is memorable). Full-bleed, 140px padding.

A horizontal 5-stage rail across the project lifecycle, showing **where each capability sits in time**:

```
SITE           LAND            STATUTORY        GRID &           CONSTRUCTION
SELECTION      CONTROL         CLEARANCE        EVACUATION       READINESS
─────●───────────●────────────────●────────────────●─────────────────●─────
Land Agg.      Land Agg.       Statutory        Transmission     Project Dev.
Screening      Title & Reg.    Approvals        ROW              Support
               Govt Liaison    Govt Liaison     Statutory        Govt Liaison
                                                (GNA/CTU)
Wk 0–6         Wk 4–28         Wk 12–40         Wk 20–52         Wk 40–COD
```

- Horizontal hairline rail in ochre at 40% opacity; nodes are 10px ink squares with ochre borders (squares, not circles — squares read technical)
- Indicative week ranges in mono beneath each stage
- Service names are links to their pages
- On section entry: rail draws left→right over 700ms, nodes fade in staggered 80ms — **the only choreographed motion on the entire site**

**Why this is the most valuable section:** it answers the question the capability grid cannot — *how do these fit together and when do I need you?* It converts nine disconnected offerings into one methodology. It is also the section a developer will screenshot and paste into an internal email, which is the highest-value outcome a B2B page can produce.

### S5 · Sectors band

**Layout:** Bone background, four columns (`lg:grid-cols-4`, `md:grid-cols-2`).

Each sector tile: 4:5 desaturated duotone image, mono label, title, one line on the *Karnataka-specific* land/development challenge, `→` link.

- **Solar** — "4–5 acres per MW, and contiguity matters more than price."
- **Wind** — "Small footprints, hard access. The crane path is the real land problem."
- **Hybrid** — "Two resource regimes, one land polygon, one evacuation point."
- **Pumped Storage** — "Head differential, geotechnics and forest overlap, screened before the DPR."

**Why images here but not on capability cards:** the sectors are *physical* and instantly recognisable; the capabilities are *procedural* and any image would be generic filler. Mixing image-tiles and icon-cards on the same page also creates a useful visual distinction between the two axes without needing a label to explain it.

### S6 · Engagement models

**Layout:** Three bordered columns, Bone.

| Model | When it fits | Basis |
|---|---|---|
| **Feasibility Mandate** | Pre-bid / site screening | Fixed fee, 4–6 weeks |
| **Development Retainer** | LOA → financial close | Monthly retainer + milestone-linked component |
| **Scope Mandate** | A single defined outcome — ROW clearance, land aggregation to registration | Per-acre / per-km, milestone-linked |

Footer line: *"We do not work on undefined success fees. Every mandate has a written scope, a deliverable list and a milestone schedule."*

**Why that footer line matters more than the table:** it is the single sentence that most separates a firm from a fixer. It should be there even though it costs you optionality.

### S7 · Experience & credibility band

**Layout:** Split 5/7. Left: a portrait-orientation photograph — the founder on site, or a documents/survey-instrument detail shot. Right: text.

**Copy (employer not named, per your decision):**

> **Twenty years on Karnataka ground.**
>
> Bolamudi Enterprise is led by a project development professional with over twenty years of experience executing utility-scale solar, wind, hybrid and pumped storage projects across Karnataka — through land aggregation, revenue and energy department processes, transmission corridors and district administrations.
>
> That work was done inside one of India's established renewable energy developers. The relationships are with departments and districts, not with a former employer's letterhead.

Right column below: four hairline-separated rows —
`UTILITY-SCALE ONLY` · `KARNATAKA-FOCUSED` · `DOCUMENTED PROCESS` · `LENDER-FORMAT HANDOVER`

**Blunt note on this section:** anonymity costs you. Buyers of liaison services buy a *person's* track record. "A professional with 20 years" is materially weaker than a named individual with a photograph and a LinkedIn link. You chose not to name the employer, which is defensible — but **name the founder**. Withholding both the name and the employer makes the strongest asset in the business invisible. I have written the copy to work either way; strongly recommend adding the name.

### S8 · Operating context (Karnataka regulatory band)

**Layout:** Ink-tinted panel (5% ink over Bone), two columns of hairline-separated rows.

Short factual rows naming the actual regime you operate in:

- `KREDL` — state nodal agency, Karnataka Renewable Energy Policy 2022–27
- `KLR ACT s.109` — company acquisition of agricultural land; 4-hectare threshold post-2025 amendment
- `LAND REVENUE RULES 2025` — Forms 21B/21C, 30-day deemed conversion; automatic conversion route for renewable projects
- `KUM / SLSWCC` — single-window clearance, ₹15 Cr–₹500 Cr; SHLCC above ₹500 Cr
- `MoP RoW GUIDELINES 2024` — 200% tower base / 30% corridor, ≥66 kV, determined by the Deputy Commissioner
- `CERC GNA` — Stage-I / Stage-II connectivity, GNA within 6 months, ₹10 lakh/MW connectivity BG
- `CEA` — DPR concurrence pathway for pumped storage

**Why this band exists and why it is the second-best section on the page:** it is unfakeable. A generalist agency writing this site cannot produce it. A developer reading it knows within ten seconds that the author has actually filed these applications. It costs one section of space and buys more credibility than any amount of design polish.

*(Maintenance risk, stated plainly: this content dates. Assign an owner and review it every six months, or it becomes evidence against you.)*

### S9 · FAQ

`Accordion`, 6–8 items, single column, max 820px. Serves objection-handling and `FAQPage` schema simultaneously.

1. Do you work outside Karnataka?
2. Do you take on projects below 50 MW?
3. How do you charge?
4. Do you buy land in your own name?
5. What happens if a landowner refuses to sell?
6. Who owns the documentation you produce?
7. Do you provide the title opinion yourself?
8. What is your typical timeline from mandate to registered land?

Answers 60–90 words, specific, no hedging. **Q5 and Q4 are the two questions every serious buyer has and nobody's website answers.** Answering them directly is worth more than the rest of the FAQ combined.

### S10 · Closing CTA

Ink background, centred, 140px padding.
H2: *"Send us your project. We'll tell you where it will stall."*
Sub: *"Share a polygon, a capacity target or an approval schedule. You'll get a written read from someone who has done this in the district you're asking about."*
`[ Discuss a project ]` solid ochre · `[ +91 XXXXX XXXXX ]` ghost with phone icon

## 3.2 Mobile specification (< 768px)

Mobile is not a narrowing of desktop. Four rules:

**1. Nothing is removed.** The instinct to truncate cards on mobile is wrong here. A developer will read this on a phone between site visits. Cards keep the full "Problem it solves" line.

**2. The Development Sequence rotates, it does not carousel.** Horizontal rail → vertical rail down the left edge with stage nodes and content to the right. **Explicitly reject a swipe carousel:** carousels hide 80% of content behind an interaction most users never perform, and this is the most important section on the page. A vertical rail keeps all five stages scannable.

**3. Sticky bottom action bar.** Appears after 40% scroll. Two 50/50 targets, 56px tall: `Discuss a project` (solid) and a phone icon `tel:` link. Rationale: this buyer calls. A form-only mobile experience loses the highest-intent 15%.

**4. Deliverables never become horizontal-scroll tables.** On child pages, deliverable tables reflow to stacked definition lists. Horizontal scroll inside a page is a known comprehension killer.

**Other mobile rules:**
- Hero: 68vh, H1 32px, stat rule wraps to a 2×2 grid
- All grids → single column; section padding 120px → 64px
- Body 16px / line-height 1.6; measure naturally constrained
- Minimum tap target 44×44px; 16px minimum gap between adjacent targets
- Nav → `Sheet` drawer, two collapsible groups (Services, Sectors), CTA pinned at drawer bottom
- Images: `next/image` with mobile-specific crops (4:5), never a desktop 21:9 crop letterboxed

---

# PART 4 — CHILD PAGE TEMPLATE (`/services/[slug]`)

Identical structure for all five capability pages. Consistency is itself a credibility signal — it demonstrates a methodology rather than ad-hoc offerings.

| # | Section | Spec |
|---|---|---|
| **C0** | Breadcrumb | `Home / Services / Land Aggregation` — mono, 12px. Also drives `BreadcrumbList` schema. |
| **C1** | Page hero | 42vh. Ink background, no photograph (photograph is reserved for the hub — restraint on inner pages reads as institutional). Eyebrow `SERVICES / 01`, H1, 2-line intro, `[ Discuss a project ]`. |
| **C2** | Problem | Bone. Two columns 5/7. Left: sticky mono label `THE PROBLEM`. Right: 2–3 paragraphs naming specific failure modes, followed by 3–4 hairline-separated "failure mode" rows in ochre-marked list form. |
| **C3** | Solution | Ink-tinted panel. Single 720px column, 22px type. One paragraph — the commitment. Followed by 3 short pillar statements. |
| **C4** | Scale & Context | Four stat cells, mono numerals, hairline dividers. Anonymised and honest — see Part 8 risk note. |
| **C5** | Process | **The page's centre of gravity.** Vertical numbered rail, 6–8 stages. Each stage: mono index `01`, title, 2–3 line description, and where applicable a mono `statute chip` (e.g. `KLR ACT s.109`, `FORM 21B`, `MoP RoW 14.06.2024`). Left column sticky on desktop showing overall stage progress. |
| **C6** | Deliverables | Bordered panel, Bone. Checklist with square ochre tick marks, grouped under 2–3 subheads. Mono `Format:` tag per group (e.g. `SHP / KML`, `PDF, lender format`). Reflows to definition list on mobile. |
| **C7** | Sector applicability | 4 compact tiles linking to `/sectors/*`, each with one line on how this capability differs for that technology. Powers the internal link mesh. |
| **C8** | Adjacent services | 3 cards linking to sibling capability pages. |
| **C9** | Engagement + CTA | Engagement basis for this specific service, then the service-specific CTA. Ink background. |

**Sector pages (`/sectors/[slug]`)** use a variant: Hero (with photograph) → What makes this asset class hard in Karnataka → How our five capabilities apply (5 rows, each linking to the service page) → Typical development timeline → Deliverables → CTA.

---

# PART 5 — PRODUCTION COPY

Voice: declarative, specific, unhedged. Short sentences. Numbers wherever a number exists. No adjectives that cannot be evidenced. Never "cutting-edge," "seamless," "end-to-end solutions," "one-stop shop," "passionate."

---

## 5.1 LAND AGGREGATION

**Icon:** `LandPlot`
**Descriptor:** Contiguous, title-clean, registered land — assembled parcel by parcel.
**Problem it solves (card line):** Projects don't fail on the last parcel. They fail on the parcel nobody checked properly.

### Problem
A 300 MW solar project needs roughly 1,200 to 1,500 acres. In Karnataka that is almost never one seller. It is 80 to 200 khatedars across four or five villages, with fragmented holdings, undivided family shares, minors' interests, tenancy exposure, grant and inam restrictions, and RTC entries that do not match who is actually farming the land.

Most developers discover this in the wrong order. Parcels are tied up on the strength of a broker's assurance, advances are paid, and the title problem surfaces during lender due diligence — eight weeks before financial close, when the cost of a gap in the chain is the entire drawdown schedule.

The second failure is geometric. Parcels get bought where they are available, not where the array needs them, and the project ends up with a polygon it cannot build on efficiently or evacuate from economically.

**Failure modes we are hired to prevent**
- A 30-year title flow with an unresolved partition or an unrecorded mutation
- Hold-out parcels sitting inside the array boundary, discovered after 80% acquisition
- Land tied up at a price set before anyone benchmarked guidance value
- Section 109 permission or conversion started after registration instead of before
- A land file that a lender's counsel cannot audit

### Solution
We assemble contiguous, encumbrance-free, connectivity-viable land and hand it over in a condition that survives lender diligence. Title is verified before money moves, not after. Every parcel enters a register at first contact and stays in it through registration, khata and mutation — so at any point in the mandate you can see exactly which survey numbers are clean, which are consented, which are executed and which are at risk.

### Process

| # | Stage | What happens |
|---|---|---|
| 01 | **Site screening & terrain assessment** | Polygon shortlisting against resource, slope, evacuation distance, forest and wildlife buffers, water bodies, habitations and existing infrastructure. |
| 02 | **Survey number mapping** | Village cadastral overlay; Bhoomi RTC pull for every survey number in the polygon; tippan/Mojini sketch reconciled to ground. |
| 03 | **Title due diligence** `30-YEAR FLOW` | Title chain, encumbrance certificate, mutation register chain, partition status, minors' interest, PTCL / inam / grant restrictions, tenancy exposure. Conducted with empanelled counsel. |
| 04 | **Owner engagement & rate discovery** | Village-level engagement, guidance value versus prevailing market benchmarking, consent mapping, early identification of hold-out risk inside the array boundary. |
| 05 | **Agreement execution** | Registered Agreement to Sale or lease deed, power of attorney where appropriate, advance schedule tied to documentary milestones. |
| 06 | **Statutory pathway** `KLR ACT s.109` | Section 109 permission where the acquirer is a company — threshold raised to four hectares under the 2025 amendment; conversion via the Deputy Commissioner or the automatic conversion route available to renewable energy projects under the 2025 Land Revenue Rules. |
| 07 | **Registration & mutation** | Sub-registrar execution, khata transfer, mutation into the SPV's name, updated RTC reflecting the project entity. |
| 08 | **Handover** | Consolidated land dossier issued to developer and lender in audit format. |

### Deliverables
**Spatial** `SHP / KML / PDF`
- Village-wise project polygon with survey-number-level GIS layer
- Array-boundary overlay showing acquired, consented, in-progress and at-risk parcels

**Register & diligence** `XLSX / PDF`
- Parcel register — survey number, extent, khatedar, RTC status, encumbrance status, consent status, execution status
- 30-year title opinion pack per parcel
- Risk log for restricted, disputed and hold-out parcels

**Executed documents** `PDF, lender format`
- Registered Agreements to Sale / lease deeds
- Section 109 permission order
- Conversion order or deemed-conversion acknowledgement
- Registered sale deeds, khata certificates and mutated RTCs in the SPV's name
- Land Due Diligence Handover File

### CTA
**Send us your polygon or your capacity target.**
We'll return a land feasibility read — village coverage, likely title complexity, indicative rate band and aggregation risk — within 10 working days.
`[ Request a land feasibility read ]` · `[ Download the land diligence checklist ]`

---

## 5.2 GOVERNMENT LIAISON

**Icon:** `Landmark`
**Descriptor:** Continuous, documented follow-through with the departments that decide.
**Problem it solves (card line):** Files don't get rejected. They wait — and your COD date moves with them.

### Problem
Approvals in Karnataka are rarely refused. They stall. A file reaches a desk with one annexure missing or one affidavit in the wrong format, a query is raised, and nobody is physically present to answer it. Two weeks become two months.

A developer's Bengaluru or Delhi team cannot sit in a Taluk office in Koppal for three weeks. So the file waits. Nobody is at fault, and the schedule slips anyway.

### Solution
We hold the file. Continuous, documented follow-through with Revenue (Deputy Commissioner, Assistant Commissioner, Tahsildar), the Energy Department, KREDL, KPTCL and the ESCOMs, KSPCB, Forest, Gram Panchayat and District Administration — with escalation through Karnataka Udyog Mitra and the single-window committees where the investment threshold allows.

**We do this through documentation, not influence.** Every submission is a complete, compliant application file. Every step is recorded in a status register you can audit. If a file is stuck, you will know which desk, since when, and on what query.

### Process

| # | Stage | What happens |
|---|---|---|
| 01 | **Approval mapping** | Department matrix built for your specific project type, capacity, land classification and district. |
| 02 | **File preparation** | Annexure-complete applications assembled and pre-checked against the receiving officer's checklist, not a generic one. |
| 03 | **Submission & acknowledgement** | Physical and portal submission with dated acknowledgements captured for every filing. |
| 04 | **Departmental follow-through** | Scheduled desk-level follow-up. Queries answered in writing within 72 hours of being raised. |
| 05 | **Committee representation** `SLSWCC / SHLCC` | Representation through Karnataka Udyog Mitra — State Level Single Window Clearance Committee for ₹15 Cr–₹500 Cr, State High Level Clearance Committee above ₹500 Cr. |
| 06 | **Escalation** | Defined escalation ladder with recorded dates, used when a file exceeds its statutory or normal timeline. |
| 07 | **Weekly status reporting** | One register, one owner, one weekly report. Every open file, its desk, its age and its next action. |

### Deliverables
- Project-specific approval matrix with department, officer level, statutory timeline and dependency
- Application dossiers for every filing, with annexure index
- Dated acknowledgement register
- Query–response log with turnaround times
- Weekly status register (open files, desk, age, next action, risk flag)
- Committee submissions, minutes and approval orders
- Closure pack on completion

### CTA
**Share your approval schedule. We'll mark where it will slip.**
Send your current department list and target dates. We'll return a marked-up matrix showing which items are mis-sequenced, which are missing, and which will not meet your COD.
`[ Get your schedule reviewed ]` · `[ Download the Karnataka approval matrix ]`

---

## 5.3 STATUTORY APPROVALS

**Icon:** `Stamp`
**Descriptor:** A project-specific statutory register, owned from application to closure.
**Problem it solves (card line):** The approval list you're working from is probably wrong for your project.

### Problem
Approval checklists circulate as PDFs between developers. They are usually wrong for the specific case, because the requirement changes with capacity, land classification, district, distance to a forest boundary, whether you are ISTS or intra-state connected, and whether storage is involved.

The consequence is always the same and always late: a missing consent discovered at commissioning, when a CEIG charging approval or a KSPCB consent is the only thing standing between a built asset and first revenue.

### Solution
We build the statutory register for your project specifically — not from a template — and own every item in it from application through to the compliance calendar we hand you at the end. Nothing is "assumed applicable." Every item is either filed, closed as not applicable with a recorded reason, or flagged as at risk.

### Process

| # | Stage | What happens |
|---|---|---|
| 01 | **Statutory register build** | Case-specific register derived from capacity, technology, land classification, district and connectivity route. Each item carries applicability reasoning. |
| 02 | **Pre-condition clearing** | Khata, RTC correction and NOCs that are prerequisites to the main applications — cleared first, because filing out of sequence is the most common cause of rejection. |
| 03 | **Land use & conversion** `s.95 KLR ACT 1964` · `FORM 21B/21C` | Conversion via the Deputy Commissioner or the automatic conversion route available to renewable projects under the 2025 Land Revenue Rules. Notarised affidavits in Forms 21B/21C, RTC extracts, mutation register extracts, pre-conversion sketch, khata and master plan extract. 30-day deemed-approval clock tracked. |
| 04 | **Energy-side approvals** `KREDL` | KREDL registration and commissioning formalities under the Karnataka Renewable Energy Policy 2022–27; KERC filings where applicable; KPTCL/ESCOM evacuation approval; CEIG charging approval. |
| 05 | **Environmental & local** `KSPCB` | Consent to Establish and Consent to Operate; Forest and Wildlife clearances where the alignment or footprint requires; Gram Panchayat NOC; fire NOC where applicable. |
| 06 | **Grid-side** `CERC GNA` | CTU Stage-I and Stage-II connectivity, GNA application within six months of Stage-II grant, and management of the connectivity bank guarantee — ₹10 lakh per MW for renewable generating stations — including validity tracking so it is never allowed to lapse. |
| 07 | **Compliance calendar handover** | Every approval with its validity, renewal date, renewal lead time and responsible party. |

### Deliverables
- Project statutory register with applicability reasoning per item
- Filed application dossiers and dated acknowledgements
- Conversion order or deemed-conversion acknowledgement
- KREDL registration and commissioning documents
- KSPCB Consent to Establish and Consent to Operate
- CEIG charging approval
- Evacuation approval from KPTCL / ESCOM
- Connectivity and GNA grant letters, with bank guarantee validity tracker
- Compliance calendar with renewal dates and lead times

### CTA
**Tell us the project. We'll tell you the actual list.**
Send capacity, district, land classification and connectivity route. We'll return the statutory register for that specific project — including the items that are commonly missed.
`[ Get your statutory register ]` · `[ Download a sample register ]`

---

## 5.4 TRANSMISSION RIGHT OF WAY

**Icon:** `TowerControl`
**Descriptor:** Corridor walked, optimised, compensated and cleared — span by span.
**Problem it solves (card line):** One orchard in the middle of a 40 km corridor can hold an entire commissioned project.

### Problem
Right of way is where good projects die quietly. The route is drawn in an office on a map. Then the line meets a village, a mango orchard, a borewell, or a landowner in the middle of a forty-kilometre corridor who has no reason to cooperate and every reason to wait.

Every week of ROW delay after mechanical completion is generation that is never sold. Unlike land acquisition, there is no alternative parcel — the corridor either clears or the asset sits idle.

The compounding error is sequence: routes are finalised before anyone walks them, so the corridor is legally fixed before its actual obstructions are known.

### Solution
We walk the corridor before it is finalised, and we clear it village by village. Route optimisation to design out the hardest crossings, landowner engagement ahead of survey rather than after, compensation determined under the Ministry of Power's June 2024 guidelines, and objections closed through the District Administration on record.

### Process

| # | Stage | What happens |
|---|---|---|
| 01 | **Corridor reconnaissance** | Physical walk-down of the proposed alignment. Habitations, orchards, structures, borewells, water bodies, forest patches, existing line crossings and access constraints recorded span by span. |
| 02 | **Route optimisation** | Alternative alignments modelled to minimise habitation and orchard crossings and rationalise angle points. Design changes here cost days; changes after finalisation cost months. |
| 03 | **Village-level engagement** | Prior notice, Gram Panchayat briefing, and crop-season sequencing so survey and stringing avoid standing crops. |
| 04 | **Compensation determination** `MoP RoW 14.06.2024` | Under the Ministry of Power guidelines dated 14 June 2024, applicable to lines of 66 kV and above: 200% of land value for the tower base area (including a one-metre extension on each side), and 30% of land value for the RoW corridor. Valuation on guidance/circle rate, or prevailing market rate where it is higher. Determined by the Deputy Commissioner; paid one-time and upfront. |
| 05 | **Objection handling** | Objections recorded, verified on site, and resolved through the District Administration with a written trail. |
| 06 | **Disbursement & documentation** | Payment records, receipts and indemnities compiled per landowner and per span. |
| 07 | **Stringing support** | Crop compensation, access track arrangement and on-ground escalation cover through the construction window. |

### Deliverables
- Corridor walk-down report with span-wise risk map
- Optimised route alignment with angle-point schedule and rationale for each deviation
- Landowner register per span — extent affected, tower base area, corridor area, contact and consent status
- Compensation working per landowner, computed under the MoP 2024 guidelines
- Deputy Commissioner's compensation determination order
- Objection log with resolution status and dates
- Disbursement records, receipts and indemnity documents
- Corridor clearance certificate pack

### CTA
**Send us your line route. We'll walk it and report in three weeks.**
You'll get a span-wise risk map, an optimised alignment proposal, and an indicative compensation exposure under the current MoP guidelines.
`[ Request a corridor walk-down ]` · `[ Download the ROW compensation note ]`

---

## 5.5 PROJECT DEVELOPMENT SUPPORT

**Icon:** `Workflow`
**Descriptor:** The Karnataka-side development desk — one interface, one register, one weekly report.
**Problem it solves (card line):** Slippage gets discovered in the review meeting, not before it.

### Problem
Between letter of award and financial close there are roughly two hundred open items across land, approvals, grid, EPC and lender conditions precedent. In most organisations these live in a spreadsheet that nobody owns, updated before review meetings rather than continuously.

The result is not that things go wrong. It is that they go wrong invisibly, and are discovered in the meeting where the schedule is being reported as on track.

### Solution
We run the Karnataka-side development desk: a single accountable interface for land, revenue, energy, grid and district matters, a live milestone register, and a weekly report that tells you what will slip before it slips — with the reason and the recovery option, not just the red flag.

### Process

| # | Stage | What happens |
|---|---|---|
| 01 | **Development baseline** | Integrated schedule across land, statutory, grid, EPC and finance workstreams, with dependencies made explicit. |
| 02 | **Critical path & CP mapping** | Critical path identified, and lender conditions precedent mapped onto it so financing constraints are visible from week one. |
| 03 | **Weekly milestone register** | Every milestone with owner, baseline date, forecast date and variance. Variance is reported the week it appears. |
| 04 | **Risk register** | Named risks with owner, likelihood, schedule impact and mitigation. Reviewed weekly, not quarterly. |
| 05 | **Local interface management** | District administration, Gram Panchayat, community, local vendors and site security handled as a standing responsibility rather than an escalation. |
| 06 | **Diligence support** | Lender and investor data room populated and maintained, site visits coordinated, diligence queries answered from source documents. |
| 07 | **Construction handover** | Structured handover to the EPC and O&M interface with an open-items register and accountability transferred in writing. |

### Deliverables
- Integrated development schedule with dependency map
- Weekly status report — milestones, variance, risks, next actions
- Conditions precedent tracker mapped to the financing timetable
- Live risk register with owners and mitigations
- Data room index and maintained document set
- Diligence Q&A log
- Site visit coordination and briefing packs
- Monthly steering pack for management and investors
- Construction handover file with open-items register

### CTA
**Send us your development schedule. We'll return it marked up.**
We'll show you which items are on the critical path, which dependencies are mis-sequenced, and which will not hold.
`[ Get your schedule stress-tested ]` · `[ Download a sample weekly report ]`

---

## 5.6 SECTOR PAGES — POSITIONING COPY

### Solar `Sun`
**Line:** 4–5 acres per MW, and contiguity matters more than price.
**What makes it hard in Karnataka:** A utility-scale solar project is a land-assembly problem before it is an engineering problem. The active belts — Pavagada, Koppal, Gadag, Bagalkot, Vijayapura, Ballari — have fragmented holdings and steadily rising expectations. Contiguity, not rate, is the binding constraint: a cheap non-contiguous polygon costs more in cabling, land loss and evacuation distance than the saving. Rising guidance values and the seven-year transfer restriction on land acquired under Section 109 make acquisition sequencing a commercial decision, not an administrative one.

### Wind `Wind`
**Line:** Small footprints, hard access. The crane path is the real land problem.
**What makes it hard in Karnataka:** The turbine footprint is small; everything around it is not. Ridge-line micro-siting drives WTG positions, and the land you actually need is the access road, the crane pad and the internal line corridor — often across owners who see no turbine on their land and no reason to agree. Chitradurga, Gadag, Davanagere, Haveri, Koppal and Belagavi each behave differently. Repowering adds a second problem: legacy land arrangements from the 2000s that were never documented to today's standard.

### Hybrid `Combine`
**Line:** Two resource regimes, one land polygon, one evacuation point.
**What makes it hard in Karnataka:** Hybrid projects are attractive because they raise CUF against a single evacuation asset. They are hard because the land has to satisfy two resource regimes at once. Turbine footprints, crane paths and array blocks must coexist on the same polygon, which raises the contiguity requirement sharply — you cannot substitute a distant parcel. Land aggregation for hybrid should be planned against the combined layout from the start, not solved twice.

### Pumped Storage `Waves`
**Line:** Head differential, geotechnics and forest overlap, screened before the DPR.
**What makes it hard in Karnataka:** Pumped storage is the longest and least forgiving development cycle we work on. A viable site needs 200–600 m of head differential between two reservoir locations at a workable horizontal distance, with geotechnics that support the waterway and powerhouse. In Karnataka, the sites that satisfy the topography frequently sit in or near ecologically sensitive Western Ghats terrain — and environmental and forest overlap must be screened as a first-order filter, not discovered after DPR spend. Land is typically a mix of revenue, forest and private holdings, each on a different legal track. Central Electricity Authority DPR concurrence sits on the critical path throughout.

---

# PART 6 — DESIGN SYSTEM

## 6.1 Colour

```
INK           #0B1B2B    Primary. Headings, dark bands, buttons.
SLATE         #1E293B    Secondary surfaces.
GRAPHITE      #475569    Body text on light.
MIST          #94A3B8    Meta, captions, disabled.
HAIRLINE      #E2DDD6    All borders and rules.
BONE          #F7F5F2    Page background.
WHITE         #FFFFFF    Cards on Bone only.
LATERITE      #B4622D    Accent. THE ONLY ACCENT.
LATERITE-DK   #8F4C22    Accent hover.
```

**Why Bone (#F7F5F2) and not white:** pure white is the default of every SaaS template. A warm off-white reads as paper and stock, which is the register we want.

**Why Laterite ochre and not green:** every renewable energy company in India uses green. It is completely commoditised and carries an eco-marketing connotation that undermines an engineering positioning. Laterite is the actual colour of the soil in the districts you work in — Chitradurga, Koppal, Gadag. It is distinctive, warm, earned, and reads as engineering rather than environmentalism.

**Accent discipline — this is a hard rule.** Laterite appears only as: index numerals, section rules, the hover bar on cards, checklist ticks, statute chips, and the primary button on ink backgrounds. It must never be a background fill for a large area. Target: under 4% of pixels. Restraint in accent usage is one of the clearest visual separators between a serious firm and a startup.

**Semantic status colours** (registers, risk flags only, never decorative):
`OPEN #475569` · `AT RISK #B4622D` · `CLEARED #15803D` · `BLOCKED #991B1B`

## 6.2 Typography

| Role | Font | Spec |
|---|---|---|
| Display / H1 | **Inter Tight** (or licensed Söhne) | 56/60px desktop, 32/38px mobile, weight 600, tracking −0.022em |
| H2 | Inter Tight | 36/44 · 26/32 mobile · 600 · −0.018em |
| H3 | Inter Tight | 22/30 · 20/28 · 600 · −0.01em |
| Body | **Inter** | 17/28 desktop, 16/26 mobile, 400, max 68ch |
| Lead | Inter | 19/32, 400, Graphite |
| Mono / labels | **JetBrains Mono** (or IBM Plex Mono) | 12/16, 500, tracking +0.09em, uppercase |

**Do not use** Poppins, Montserrat, Nunito, Raleway or any geometric sans. Geometric sans-serifs read as consumer-startup — this is one of the fastest ways to undo the entire positioning. Neo-grotesques (Inter, Söhne, Suisse, Helvetica Now) read institutional.

**The monospace layer is a deliberate device, not decoration.** Applied to stage indices, statute references (`KLR ACT s.109`, `FORM 21B`), deliverable formats and stat numerals, it makes the page feel like it was produced by people who handle documents for a living. It is a low-cost, high-signal move and no competitor in this category uses it.

Numerals: `font-variant-numeric: tabular-nums` on all stats and registers.

## 6.3 Layout & spacing

- Container 1440px max, content 1280px, prose 720px
- 12-column grid, 24px gutter desktop / 16px mobile
- Spacing scale (4px base): 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 120 · 160
- Section padding: 120px desktop / 64px mobile. Hero and closing CTA: 160px / 96px
- Border radius: **2px everywhere.** Buttons 2px. Cards 2px. Inputs 2px. Images 0px.
- Elevation: **none.** No box-shadows anywhere. Separation is achieved with 1px hairlines and background steps only.

## 6.4 Iconography

**Set:** Lucide (ships with shadcn/ui).
**Rules:** 24px, 1.5px stroke, single colour (Ink; Laterite on dark bands only), never filled, never inside a coloured circle or rounded square badge, always top-left aligned in a card, never centred above a heading.

| Item | Lucide icon |
|---|---|
| Land Aggregation | `LandPlot` |
| Government Liaison | `Landmark` |
| Statutory Approvals | `Stamp` |
| Transmission ROW | `TowerControl` |
| Project Development Support | `Workflow` |
| Solar | `Sun` |
| Wind | `Wind` |
| Hybrid | `Combine` |
| Pumped Storage | `Waves` |
| Deliverable tick | `Check` in a 2px square |
| Statute chip | `FileText` at 14px |

**Honest assessment:** Lucide is competent and free, but it is generic — a developer will have seen these exact glyphs on fifty sites. **Phase 2 recommendation:** commission a bespoke nine-icon set on a shared 24px grid with a consistent motif (a terrain baseline running through every glyph, tying land, tower, turbine and reservoir into one visual family). Roughly ₹40,000–₹80,000 from a good Indian illustrator, and it is the cheapest way to make the site feel commissioned rather than assembled. Ship with Lucide, upgrade in Phase 2.

## 6.5 Photography direction

**Three permitted categories, and nothing else:**

1. **Terrain** — wide, horizon-dominant Karnataka landscape. Scrubland, red soil, ridge lines, a transmission line receding into distance. 21:9 for hero, 16:9 for bands.
2. **Infrastructure detail** — a tower against sky, a substation gantry, a met mast, a turbine nacelle at distance. Never a full turbine hero shot; it is the most over-used image in the sector.
3. **Documents and instruments** — a total station on a tripod on red soil, a cadastral map on a bonnet, a survey sketch, a stack of registered deeds. **This is the most differentiating category and the least used by competitors.** Use it for the credibility band and the child-page Problem sections.

**Banned:** people in hard hats pointing at panels · handshakes · glowing globes with circuit lines · anything with lens flare · anyone smiling at the camera · drone shots of arrays with a saturated blue sky. These are the visual grammar of an EPC brochure from 2014 and they cost you credibility instantly with a technical buyer.

**Grade (must be applied uniformly):** desaturate to ~35%, lift shadows ~8%, apply a 6% Ink duotone in the shadows and a 4% Laterite lift in the highlights, reduce contrast slightly. Consistency of grade across all images matters more than the quality of any single image — a mixed-grade gallery reads as stock-sourced no matter how good the individual photos are.

**Sourcing, in order of preference:**
1. **Commission a photographer for two days** across Chitradurga / Koppal / Gadag. ₹30,000–₹60,000 all-in. This is the single highest-return spend on the entire website — genuine local terrain is unmistakable and unfakeable.
2. Licensed Indian stock (IndiaPicture, Dinodia) for terrain fill.
3. Unsplash / Pexels with strict filtering — Indian semi-arid landscape only.

**Do not use AI-generated imagery of Indian rural land or documents.** It produces artefacts a domain buyer spots immediately — malformed Kannada text, impossible cadastral geometry, wrong crop types — and being caught doing it on a trust-driven page is worse than having no image.

**Text over image:** always a scrim. Minimum 65% Ink at the text edge. Never rely on the image being dark enough.

## 6.6 Motion (Framer Motion)

Motion volume is inversely correlated with perceived seniority. The budget is deliberately tiny.

**Permitted:**
1. **Section entry** — `opacity 0→1`, `y 8→0`, 400ms, `cubic-bezier(0.16, 1, 0.3, 1)`, `viewport={{ once: true, margin: "-80px" }}`, 60ms stagger on grid children.
2. **Card hover** — border colour 180ms, 3px top bar scaleX 0→1 180ms, `translateY(-2px)`.
3. **Development Sequence rail** — the single choreographed moment on the site: rail draws left→right 700ms, nodes fade in staggered 80ms. Once only.
4. **Mobile sticky bar** — slide up 240ms after 40% scroll.
5. **Accordion** — height auto, 200ms.

**Prohibited:** parallax · scroll-jacking · counting-up statistics · text scrambling or typewriter effects · magnetic cursors · 3D tilt on cards · looping background video · marquee scrollers · page transition curtains.

**Accessibility (non-negotiable):** `@media (prefers-reduced-motion: reduce)` disables all transforms and transitions; content renders in final state immediately.

## 6.7 shadcn/ui component mapping

| Component | Use | Required restyling |
|---|---|---|
| `Card` | Capability cards, engagement columns | radius 2px, remove shadow, 1px Hairline border, Bone/White bg |
| `Accordion` | FAQ only | Hairline dividers, `Plus`/`Minus` (not chevron), no bg fill |
| `Button` | Two variants only | `default` = Ink solid, 2px radius, 15px medium, 48px height. `ghost` = text + 1px underline offset 4px |
| `Badge` | Statute chips, deliverable formats | Square (0px radius), mono 11px, 1px border, transparent bg |
| `Separator` | All rules | Hairline colour only |
| `NavigationMenu` | Desktop mega-menu | Flat panel, no shadow, 1px border |
| `Sheet` | Mobile nav | Full-height, Ink bg |
| `Breadcrumb` | All child pages | Mono 12px, `/` separator |
| `Tabs` | Sector applicability (optional) | Underline-only indicator in Laterite |
| `Tooltip` | Statute chip expansion | Ink bg, 2px radius |

**Do not use:** `Carousel` (hides the most important content), `Dialog` for anything marketing-related, `HoverCard`, `Progress`, `Skeleton` on SSG pages.

---

# PART 7 — SEO SPECIFICATION

## 7.1 The honest framing first

These are low-volume, high-intent B2B queries. Realistic combined organic volume across all nine target terms is likely a few hundred searches a month in India, possibly fewer. **Anyone promising traffic growth on this site is selling you something.**

But the economics are unusual: a single enquiry from "land aggregation solar Karnataka" is potentially a multi-crore mandate. Ranking for ten queries a month can be worth more than ranking for ten thousand in most industries.

So the SEO strategy has two jobs, in this priority order:
1. **Convert and qualify the visitor who arrives from a referral, a LinkedIn profile, or a branded search.** This is 80%+ of traffic. Page quality, not keywords, does this work.
2. **Own the handful of high-intent transactional queries.** Achievable with nine well-structured pages and the internal link mesh, because the competition is thin — most competitors are either large consultancies not targeting Karnataka specifically, or firms with no web presence.

## 7.2 Keyword map

| Page | Primary | Secondary |
|---|---|---|
| `/services` | renewable energy project development services Karnataka | solar wind project development support Karnataka |
| `/services/land-aggregation` | land aggregation for solar projects Karnataka | land acquisition solar wind Karnataka · agricultural land purchase for solar Section 109 |
| `/services/government-liaison` | government liaison renewable energy Karnataka | KREDL liaison consultant · single window clearance renewable Karnataka |
| `/services/statutory-approvals` | solar project approvals Karnataka | land conversion for solar project Karnataka · KREDL approval process |
| `/services/transmission-right-of-way` | transmission line right of way Karnataka | ROW compensation transmission line India · transmission corridor clearance |
| `/services/project-development-support` | renewable energy project development consultant Karnataka | project development support IPP Karnataka |
| `/sectors/solar` | solar project development Karnataka | utility scale solar land Karnataka |
| `/sectors/wind` | wind project development Karnataka | wind farm land aggregation Karnataka · wind repowering Karnataka |
| `/sectors/hybrid` | wind solar hybrid project Karnataka | hybrid renewable project development |
| `/sectors/pumped-storage` | pumped storage project development Karnataka | PSP site development India · pumped storage land acquisition |

## 7.3 Metadata

Format: `{Service} in Karnataka — {benefit} | Bolamudi Enterprise` · Titles ≤ 60 chars, descriptions 150–158 chars.

| Page | Title | Description |
|---|---|---|
| `/services` | Renewable Project Development Services, Karnataka \| Bolamudi | Land aggregation, government liaison, statutory approvals and transmission ROW for utility-scale solar, wind, hybrid and pumped storage projects in Karnataka. |
| land-aggregation | Land Aggregation for Solar & Wind Projects in Karnataka | Contiguous, title-verified, registered land for utility-scale renewable projects. Survey-number diligence, Section 109 permission, conversion and mutation. |
| government-liaison | Government Liaison for Renewable Projects in Karnataka | Documented follow-through with Revenue, KREDL, KPTCL, KSPCB and district administration. Weekly status registers, single-window representation, no guesswork. |
| statutory-approvals | Statutory Approvals for Solar & Wind Projects, Karnataka | Project-specific statutory register from land conversion and KSPCB consents to CEIG charging approval and CTU connectivity. Owned to closure. |
| transmission-row | Transmission Right of Way Clearance in Karnataka | Corridor walk-downs, route optimisation, landowner engagement and compensation under the 2024 MoP RoW guidelines. Span-by-span corridor clearance. |
| project-dev-support | Renewable Project Development Support in Karnataka | A single Karnataka-side development desk. Integrated schedule, weekly milestone register, CP tracking and lender diligence support from LOA to financial close. |

**H-tag discipline:** exactly one H1 per page. Section titles are H2. Process stage titles are H3. Never style a `<div>` to look like a heading — the crawler reads structure, not size.

## 7.4 Structured data (JSON-LD)

- **All pages:** `Organization` — legal name, `areaServed: Karnataka, IN`, `founder`, `knowsAbout: [...]`, `sameAs: [LinkedIn]`
- **`/services` hub:** `ProfessionalService` + `ItemList` of the nine offerings + `FAQPage` for the accordion
- **Each child page:** `Service` with `serviceType`, `provider`, `areaServed`, `hasOfferCatalog` listing the deliverables
- **All child pages:** `BreadcrumbList`

`FAQPage` markup is the highest-return item here — it is the only realistic path to a rich result in this category.

## 7.5 Technical

- **Rendering:** all nine pages fully static (`generateStaticParams` + SSG). Zero client-side data fetching. No `use client` above the fold except the mobile sticky bar.
- **Images:** `next/image`, AVIF with WebP fallback, hero `priority` + `preload`, explicit `sizes` per breakpoint, art-directed mobile crops.
- **Fonts:** `next/font/local`, subset to `latin`, `display: swap`, preload the two weights actually used. Self-host — no Google Fonts CDN request.
- **Core Web Vitals targets:** LCP < 2.0s on 4G · CLS < 0.05 · INP < 150ms.
- **Canonicals** on every page. `sitemap.xml` and `robots.txt` generated at build.
- **OG images:** per-page, generated via `next/og` — Ink background, service title, Laterite rule, wordmark. Matters more than usual here because these URLs get pasted into LinkedIn and email.
- **Accessibility:** WCAG 2.2 AA. Contrast ≥ 4.5:1 for body (verify Graphite on Bone = 8.1:1 ✓; Mist on Bone fails — restrict Mist to ≥18px). Visible 2px Laterite focus rings. Full keyboard operability on the mega-menu.
- **Analytics:** track CTA clicks per service, method-note PDF downloads, `tel:` taps, and scroll depth past the Development Sequence. The PDF downloads are your real lead indicator — most of this audience will not fill a form on the first visit.

---

# PART 8 — RISKS AND WEAK POINTS

Stated plainly, because pretending they do not exist will cost you more than reading them.

**1. No named clients is your biggest weakness, and design cannot fix it.**
Anonymised metrics ("2,400 acres across six districts") are unverifiable and every buyer knows it. If a single past client will permit being named — even as "a leading IPP" with a project name — that is worth more than the entire visual design. Pursue this before launch.

**2. Key-man risk is the unasked question that kills deals silently.**
A single-promoter firm taking a 30-month development mandate invites the question "what happens if you are unavailable?" It will rarely be asked aloud; it will be decided silently. Add one honest line to the credibility band describing your delivery bench — associates, empanelled counsel, survey teams, district-level resources. Even a modest, truthful answer beats an unanswered question.

**3. "Government Liaison" is a phrase with connotations.**
The copy in Part 5.2 is deliberately scrupulous — process, documentation, official channels, auditable registers, and the explicit sentence "we do this through documentation, not influence." Do not let anyone soften or remove that line for being defensive. It is doing more commercial work than any headline on the page. It is also the correct thing to say.

**4. The regulatory content in S8 will date.**
Section 109 thresholds, the 2025 Land Revenue Rules, CERC GNA regulations (reform proposals were live as of mid-2026) and MoP RoW rates all change. Stale statutory content on a page that claims regulatory expertise is actively damaging. Assign an owner and a six-month review cycle before you publish it.

**5. Do not put a chatbot, a live-chat widget, or an exit-intent popup on this site.**
They are the fastest available way to make an engineering consultancy look like a lead-generation funnel. This audience does not convert through them and will discount you for having them.

**6. Sequencing recommendation.**
Ship the hub page plus the two highest-value child pages (Land Aggregation, Transmission ROW) first. Those two carry the highest-intent queries and the sharpest differentiation. Add the remaining seven within four weeks. Do not launch nine thin pages simultaneously — a page with 300 words of filler under a Process heading damages you more than its absence.

---

# PART 9 — BUILD NOTES

**Route structure**
```
app/
  services/
    page.tsx                      # hub, SSG
    [slug]/page.tsx               # generateStaticParams over 5 services
  sectors/
    [slug]/page.tsx               # generateStaticParams over 4 sectors
content/
  services/*.ts                   # typed content objects
  sectors/*.ts
components/
  services/CapabilityCard.tsx
  services/DevelopmentSequence.tsx    # only client component of consequence
  services/ProcessRail.tsx
  services/DeliverablesList.tsx
  services/StatuteChip.tsx
  services/EngagementModels.tsx
  layout/MobileStickyCTA.tsx
```

**Content typing** — enforce the model in TypeScript so no page can ship incomplete:

```ts
type Service = {
  slug: string; index: string; title: string; icon: LucideIcon;
  descriptor: string; problemLine: string;
  problem: { body: string[]; failureModes: string[] };
  solution: { lead: string; pillars: string[] };
  scale: { value: string; label: string }[];        // exactly 4
  process: { n: string; title: string; body: string; statute?: string }[];
  deliverables: { group: string; format: string; items: string[] }[];
  engagement: string;
  cta: { headline: string; body: string; primary: string; secondary: string };
  seo: { title: string; description: string; primaryKw: string };
};
```

This is the mechanism that makes consistency structural rather than a matter of discipline.

---

*End of specification.*
