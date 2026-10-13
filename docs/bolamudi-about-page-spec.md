# Bolamudi Enterprise — About Page
## Complete Design, Content & SEO Specification

Version 1.0 · Prepared for build in Next.js / TypeScript / Tailwind / shadcn/ui / Framer Motion

---

# PART 0 — STRATEGIC PREFACE (READ THIS FIRST)

You asked me not to assume and to explain every decision. Five decisions were made before a single section was designed. If you disagree with these, the rest of the document changes.

## 0.1 The actual constraint

Confirmed inputs: **founder-only entity, no nameable clients, no nameable projects, no nameable former employer, no published MW figures.**

Your audience is IPPs, infrastructure companies and investment firms. These buyers run diligence. They will search the company name, look for a CIN, look for past project credits, and find a firm with no track record attached to it.

This means the standard credibility playbook — logo walls, MW counters, case studies, awards, team grids — is entirely unavailable to you. Any attempt to simulate it will be detected and will cost you the deal.

**Blunt version: a page that looks like AECOM but has nothing behind it is more damaging than a modest page. Scale-signalling without scale is the single fastest way to get filed as "not serious."**

## 0.2 The strategic substitution — proof through procedural specificity

If you cannot prove *track record*, you prove *command of the machinery*.

Nobody who has not spent twenty years doing this work can write accurately and unprompted about: the Section 109 exemption route under the Karnataka Land Reforms Act 1961 and its seven-year transfer restriction; the practical difference between deemed conversion for renewable projects under the Karnataka Land Revenue (Amendment) Rules 2025 and the pre-2025 DC conversion path; KREDL scrutiny and the SLAC allotment route; how a KPTCL evacuation scheme approval actually gets communicated to an IPP; what Gomala land means for an aggregation plan; how RoW compensation is negotiated tower-by-tower rather than corridor-wide.

A developer's project head reads three lines of that and knows instantly whether he is talking to an operator or a broker. **Domain specificity is your credibility currency. It is the entire spine of this page.**

Every generic sentence you allow onto this page ("we are committed to excellence in renewable energy") dilutes that currency. Generic language is what a firm with nothing to say uses. You have something to say — say the specific version of it.

## 0.3 The timeline contradiction — resolved

You asked for "credibility instead of company history" **and** for a "Timeline." These are in direct conflict. Bolamudi Enterprise is a new entity. A company-history timeline would show a single dot marked "Founded," which is an own goal.

**Resolution — two timelines, neither of which is a company history:**

| Timeline | What it shows | Why it builds credibility |
|---|---|---|
| **Development Lifecycle Timeline** (Section 05, primary, horizontal) | The seven real stages of a Karnataka utility-scale RE project, with Bolamudi's intervention points marked | Demonstrates mastery of the process and simultaneously functions as a scope diagram. Reads as a timeline visually, is honest factually. |
| **Capability Timeline** (inside Section 06, secondary, compact vertical) | The founder's twenty years organised by *asset-class era* — wind, then solar, then hybrid, then pumped storage — with no employer or project named | Conveys duration and technology breadth without claiming institutional credit that belongs to a former employer. |

This is the most important structural decision in the document. It converts your weakest asset (no history) into your strongest one (process command).

## 0.4 Visual reference — correct the brief

Your reference set (Black & Veatch, AECOM, Arup, WSP, Jacobs) is right in *discipline* and wrong in *device*.

**Adopt from them:** typographic hierarchy over decoration; large whitespace; muted, low-saturation palette; documentary photography; dense factual copy; near-zero ornament; slow, minimal motion; no gradients, no glassmorphism, no emoji, no rounded-pill "startup" chrome.

**Reject from them:** global office maps, "operating in 150 countries" counters, animated statistic tickers, large multi-person leadership grids, awards carousels. Every one of these is a scale signal. A single-principal firm deploying scale signals reads as inflation.

**The design target is not "large firm." It is "senior, restrained, unmistakably technical."** A page with fewer claims, set beautifully, with precise domain language, outperforms an imitation of a 10,000-person consultancy. Restraint is the trust signal available to you.

## 0.5 Two blind spots you did not ask about

**Key-man risk.** Every sophisticated buyer reading a single-principal page thinks the same thing within ten seconds: *what happens if this one person is unavailable, or is already committed to another project?* Most solo consultancies hide from this. Hiding from it does not remove the thought — it removes your chance to answer it. Section 08 addresses it directly and explicitly. Naming the objection before the reader does is a strong trust move; it is also the section most likely to differentiate you.

**The company name.** "Bolamudi Enterprise" — in Indian commercial naming convention, "Enterprise(s)" reads as a proprietorship trading firm, not an engineering or advisory practice. It works against the entire positioning before anyone reads a word. You did not ask, but you should consider "Bolamudi Energy Advisory," "Bolamudi Renewables," "Bolamudi Project Development" or similar before the site is built, because retrofitting a name after launch costs domain authority. Flagging once; your call.

---

# PART 1 — PAGE ARCHITECTURE

## 1.1 Section order and the reasoning behind it

Ten sections. The order follows the buyer's actual decision sequence, not a narrative arc.

| # | Section | Buyer question it answers | Why it sits here |
|---|---|---|---|
| 01 | Hero | "What is this firm?" | Positioning must land in one screen. No welcome copy. |
| 02 | Credibility Strip | "Is this real?" | Immediately after the claim, before scroll commitment. Four facts, no invented numbers. |
| 03 | The Position | "What do they actually do — and not do?" | Negative-space definition. Firms that over-claim never state what they don't do; stating it is itself a credibility act. |
| 04 | Domain Command | "Do they actually know this?" | The proof engine. Placed early — before Leadership — because expertise must be established before the person is introduced, otherwise the page reads as a personal profile. |
| 05 | Development Lifecycle | "Where do they plug in?" | Converts abstract expertise into a placeable scope. Doubles as the requested timeline. |
| 06 | Leadership | "Who is this?" | Only now. The reader has already accepted the competence; the person becomes the guarantor of it, not the pitch. |
| 07 | Core Values | "How do they behave under pressure?" | Post-competence. Values before competence read as filler. |
| 08 | Why Bolamudi | "Why not a large consultancy, or my own team?" | Objection handling, including key-man risk. |
| 09 | How We Engage | "How do I start, and what is the commercial shape?" | Removes procurement ambiguity — the last friction before contact. |
| 10 | Closing CTA | "What now?" | Single action. |

**Key UX reasoning — why Leadership is section 06, not 02.** The instinct on a single-founder site is to lead with the founder. That is wrong for this audience. A page that opens with a person reads as a CV and invites the reader to evaluate *an individual*. A page that opens with capability reads as a firm and invites the reader to evaluate *a service*. By the time the founder appears in 06, the reader has already accepted the expertise; the portrait then confirms rather than persuades. This is exactly the sequencing Arup and Black & Veatch use for practice-lead pages.

## 1.2 What is deliberately absent, and why

| Omitted | Reason |
|---|---|
| Company history / "Our Story" | No history to tell. You asked for credibility over history — this is the enforcement of that. |
| Mission & Vision statements | Unverifiable, universally identical across every RE company site, zero decision value. Values as *operating commitments* (Section 07) replace them. |
| Animated statistic counters | Requires numbers you cannot substantiate, and the count-up animation is a consumer-startup device. |
| Client logo wall | None available. An empty or "coming soon" logo strip is worse than no strip. |
| Team grid | One person. A grid of one is conspicuous. |
| Stock photography of generic solar farms | The single clearest tell of an unbacked consultancy. Handled in Part 4. |
| Testimonial carousel | None available yet. Leave the slot architecturally open (Section 08 can absorb it later). |

---

# PART 2 — SECTION-BY-SECTION SPECIFICATION

Design tokens are referenced **semantically** (`surface`, `surface-alt`, `ink`, `ink-muted`, `rule`, `accent`) because your system is already locked. Map them to your existing variables at build. No hard-coded hex appears in this spec by design — that is what keeps it conformant to a system I have not seen.

---

## SECTION 01 — HERO

### Purpose
Establish category, geography and seniority in under four seconds. Not a greeting.

### Desktop layout (≥1280px)
- Full-bleed section, height `min-h-[72vh]`, **not** 100vh. Reason below.
- Split grid: 12 columns. Text block spans columns 1–6. Image spans 7–12, full-bleed to the right viewport edge, no right container padding.
- Vertical alignment: text block centred against the image.
- Image treated with a subtle single-direction dark scrim from left, so the type block's edge does not collide visually with image detail.

**Why 72vh and not 100vh:** a full-viewport hero on a B2B credibility page wastes the most valuable pixels. At 72vh the top edge of Section 02 is visible above the fold, which signals depth and pulls the scroll. Full-bleed 100vh heroes are a marketing-site convention and read as brochureware to a technical reader.

**Why the image is full-bleed right and not a background behind the text:** text over photography reduces legibility and forces heavy overlays, which is the visual language of consumer landing pages. A hard split — solid surface left, photograph right — is the editorial convention used by engineering consultancies and reads as document, not advertisement.

### Content

**Eyebrow** (uppercase, tracked, `ink-muted`, small)
> ABOUT BOLAMUDI ENTERPRISE

**H1** (single H1 on the page; large display, tight leading ~1.05, max ~14 words per line)
> Two decades inside Karnataka's renewable energy development machinery.

**Deck** (body-large, `ink-muted`, max-width ~52ch)
> Bolamudi Enterprise is a project development support firm. We handle the land, statutory and liaison work that decides whether a sanctioned renewable project reaches construction — and when.

**Rule** — 1px `rule` line, ~64px wide, above the eyebrow. Standard consultancy device; costs nothing, signals category immediately.

**No CTA button in the hero.** Reason: an About page reader is in evaluation mode, not action mode. A "Contact Us" button 300ms into an evaluation reads as sales pressure and slightly undercuts the seniority the page is trying to establish. The CTA is earned at Section 10.

### Copy reasoning, line by line
- *"Two decades inside"* — "inside" not "in." Implies operational proximity, not observation. This is the difference between a practitioner and an advisor, and your entire value is that you are the former.
- *"machinery"* — deliberate. Land, revenue, KREDL, KPTCL and RoW are a bureaucratic machine. Naming it as such tells a developer you understand the thing that actually delays his project.
- *"decides whether… and when"* — schedule risk is the developer's real anxiety. Not cost, not quality. Timeline. Every line on this page should orbit schedule certainty.
- No adjectives. No "leading," "trusted," "premier." Those words are load-bearing only when a third party says them.

### Mobile (<768px)
- Stack: image first at `h-[42vh]`, then text block below on `surface`.
- H1 drops one full step on the type scale; leading loosens to ~1.15.
- Deck truncates to the first sentence plus "We handle the land, statutory and liaison work that decides whether a sanctioned project reaches construction." (Second clause dropped — mobile readers do not parse compound clauses well at that width.)
- Section padding 72px top / 56px bottom.

**Why image-first on mobile:** the LCP element should be a single decisive visual, and a wall of text as the first mobile impression has measurably worse engagement on B2B pages. It also keeps the LCP element identical across breakpoints, which simplifies performance work.

### Motion
`fadeUp` on the text block only, staggered: eyebrow → H1 → deck, 60ms apart. Image does **not** animate. Total sequence under 700ms.

**Why the image doesn't animate:** the hero image is the LCP element. Animating opacity or transform on the LCP element delays the measured paint and degrades Core Web Vitals for zero design benefit.

---

## SECTION 02 — CREDIBILITY STRIP

### Purpose
Four verifiable facts, immediately after the positioning claim. This is the section where a dishonest site would put invented numbers. Yours will not.

### Desktop layout
- Full-width band on `surface-alt`, section padding 64px vertical.
- 4-column grid, 1px `rule` vertical dividers between columns (not borders on cards — no cards).
- Each cell: large figure/word in `ink`, label beneath in `ink-muted` uppercase small.

### Content

| Cell | Primary | Label |
|---|---|---|
| 1 | **20+** | Years in utility-scale renewable project execution |
| 2 | **4** | Asset classes — Solar, Wind, Hybrid, Pumped Storage |
| 3 | **Karnataka** | Statewide revenue district and DISCOM coverage |
| 4 | **Pre-construction** | Full scope — land, approvals, evacuation, right of way |

### Reasoning
Cells 2, 3 and 4 are *categorical*, not numerical. This is intentional. Four numbers in a row is the animated-counter pattern; two numbers and two words is an editorial fact strip. The second reads as considered, the first as templated.

**Explicitly do not add:** "MW facilitated," "acres aggregated," "projects delivered," "clients served." You confirmed you have none of these that are nameable. An unsubstantiated MW number is the exact claim a diligence team will ask you to evidence in the first meeting. **Leave the slot open — this strip is architecturally designed to accept two more cells later, when you have figures you can defend.** Build it as a `grid-cols-4 lg:grid-cols-6` ready component.

### Mobile
2×2 grid. Horizontal `rule` dividers between rows, vertical between columns. Figures drop one type step. No horizontal scroll — a scrollable stat strip hides half its content and half of your credibility.

### Motion
Stagger `fadeUp`, 80ms apart, `viewport={{ once: true, margin: "-80px" }}`. **No count-up animation on "20+".** Count-up is a consumer conversion device; it also makes the number feel like a metric rather than a fact.

---

## SECTION 03 — THE POSITION

### Purpose
Define the firm by boundary. The most under-used trust device in professional services.

### Desktop layout
- Container-width (max 1200px), 2-column asymmetric split: left column 5/12 holds the section label and H2; right column 6/12 (offset 1) holds body copy. Wide gutter between.
- Section padding 128px vertical, `surface`.

**Why asymmetric and offset:** a centred single column reads as a blog post; a symmetric 50/50 split reads as a template. The 5/6 offset grid is the editorial signature of engineering and legal practice sites and creates a deliberate reading rhythm — the eye lands on the heading, then travels right and down.

### Content

**Section label:** `01 — THE POSITION` (uppercase, tracked, `ink-muted`)

**H2:**
> We occupy the stage most developers underestimate.

**Body:**
> A utility-scale renewable project rarely fails on technology. It fails, or slips by eighteen months, in the pre-construction stage — where land title is imperfect, where a statutory file sits unmoved on a desk, where an evacuation approval is contingent on a bay that has already been allocated, where a transmission corridor crosses forty parcels and thirty-nine owners agree.
>
> That stage is our entire practice. We do not build, and we do not advise on what to build. We take a project from allocation to a construction-ready position: land consolidated and clean, approvals held, evacuation secured, corridor cleared.

**"What we are not" block** — three items, `rule`-separated rows, each with a strikethrough-free but muted treatment:

| Not | Clarification |
|---|---|
| Not an EPC contractor | We do not construct or procure. |
| Not a technical or DPR consultant | We do not size plants, model yield or prepare engineering reports. |
| Not a land broker | We are retained by the developer, we are not paid by the landowner, and we do not hold positions in land we aggregate. |

### Reasoning
The third exclusion is the most commercially valuable sentence on the entire page. **Conflict of interest is the number one unspoken concern a developer has about a land aggregation partner in India.** Every developer has been burned by an aggregator who was quietly on both sides of a transaction. Stating the position unprompted, in plain language, removes an objection that would otherwise be raised in a meeting you may never get.

The "what we are not" device also does silent SEO and qualification work: it repels EPC and DPR enquiries you cannot service, which improves lead quality and reduces wasted sales time.

### Mobile
Single column. Section label → H2 → body → exclusion rows stacked. Exclusion rows become stacked pairs (bold "Not…" line, muted clarification beneath) with 1px `rule` above each.

### Motion
`fadeUp` on the heading block; exclusion rows stagger 70ms. Nothing else.

---

## SECTION 04 — DOMAIN COMMAND

### Purpose
**The proof engine of the page.** This section does more credibility work than every other section combined.

### Desktop layout
- `surface-alt` band, section padding 128px.
- Intro block: container-width, left-aligned, max 60ch.
- Below: 2×2 grid of four capability blocks. Generous gutter (~64px). **No cards, no shadows, no borders.** Each block separated by a 1px `rule` on its top edge only.
- Within each block: domain title (H3), one-line framing sentence, then a list of 6–8 specific line items in `ink-muted`, each preceded by a small 1px horizontal tick mark rather than a bullet glyph.

**Why no cards:** shadowed rounded cards are the visual grammar of SaaS. A 1px rule over a text column is the grammar of technical documentation. You are trying to look like the second. This one choice does more to differentiate the page from a startup site than any other.

**Why 2×2 and not 4-across:** four columns forces each list to a narrow measure and truncates the line items, which are the actual proof. The content dictates the grid, not the reverse.

### Content

**Section label:** `02 — DOMAIN COMMAND`

**H2:**
> The work, stated precisely.

**Intro:**
> Development support is a term wide enough to mean nothing. Below is what it means here — the specific instruments, authorities and procedures we work through in Karnataka.

**Block A — Land Aggregation & Title**
> Aggregation is a title problem before it is a negotiation problem.
- Village-level identification and survey-number-wise feasibility screening
- RTC, mutation register and encumbrance chain verification
- Joint measurement and boundary reconciliation with survey authorities
- Structuring for purchase, long-lease and hybrid tenure
- Section 109 exemption route under the Karnataka Land Reforms Act, 1961
- Ceiling-limit and non-agriculturist acquisition constraints
- Seven-year transfer restriction and its effect on downstream project sale
- Gomala, government and inam land classification and grant pathways

**Block B — Land Use & Statutory Approvals**
> Approvals are sequence-dependent. Filing in the wrong order costs quarters.
- Conversion and land-use position, including the deemed and automatic conversion route now available to renewable projects under the Karnataka Land Revenue (Amendment) Rules, 2025
- KREDL registration, scrutiny and the SLAC allotment route
- Incentive and reimbursement claims under the Karnataka Renewable Energy Policy 2022–27
- District administration and Deputy Commissioner office liaison
- Single-window and Udyog Mitra coordination where applicable
- Forest, environmental and wildlife clearance interfaces where the site demands it
- Panchayat, local body and NOC coordination

**Block C — Evacuation & Grid Connectivity**
> A project without a confirmed bay is a project without a date.
- Evacuation scheme application and approval through KPTCL
- Substation and bay availability assessment prior to land commitment
- ESCOM interface — BESCOM, HESCOM, GESCOM, MESCOM, CESC
- Intra-state and ISTS connectivity coordination and long-term access
- Interconnection and metering point coordination with the developer's technical team

**Block D — Transmission Right of Way**
> The corridor is negotiated parcel by parcel, not corridor by corridor.
- Route optimisation against land cost, crop pattern and habitation
- Tower footing and corridor consent from individual landowners
- Crop and structure compensation assessment and settlement
- Objection handling and district administration escalation
- Sequencing RoW against the construction and stringing programme

### Reasoning
Read that list as a project head at an IPP. Every line is a thing that has actually cost him money. "Substation and bay availability assessment **prior to land commitment**" is a sentence that only someone who has watched a developer buy 400 acres next to a full substation would think to write. That is the proof.

**Instruction to whoever writes the final copy: do not soften any of these lines.** Each abstraction ("regulatory approvals," "government coordination") removes a unit of credibility. If a line is too specific for a generalist reader, that is correct — the generalist reader is not your buyer.

**Accuracy warning:** these references are current as at the date of this document. The 2025 Land Revenue Rules amendment materially changed the conversion pathway for renewable projects. **Set a calendar review of this section every six months.** A stale statutory reference on the page that proves your expertise is worse than no page.

### Mobile
Blocks stack single-column, full width, 1px `rule` above each, 56px separation. Line items remain full lists — **do not** collapse them into accordions. An accordion hides your only proof behind a tap; the cost of a long scroll is far lower than the cost of unseen evidence.

### Motion
Per-block `fadeUp` as each enters viewport. Line items do **not** stagger individually — 27 staggered items reads as a loading state.

---

## SECTION 05 — THE DEVELOPMENT LIFECYCLE (TIMELINE)

### Purpose
The requested timeline, reframed as process mastery. Also functions as a scope diagram so a developer can point at a stage and say "we need you from here."

### Desktop layout
- `surface`, section padding 128px.
- Horizontal timeline: a single 1px `rule` running the full container width at mid-height.
- Seven nodes evenly distributed on the rule. Node = 9px filled circle in `accent` for stages Bolamudi **owns**; 9px hollow ring in `rule` colour for stages we **support**.
- Content alternates above and below the rule to avoid vertical crowding: stages 1, 3, 5, 7 above; 2, 4, 6 below. Each: stage number (small, `ink-muted`), stage title (H4), one-line description (small, `ink-muted`, max 22ch).
- Legend beneath: ● Led by Bolamudi ○ Supported

**Why alternating above/below:** seven nodes across 1200px gives ~170px per node. A single row forces 3-line text wraps and collides. Alternating doubles the available width per label. This is the standard solution and it is why process diagrams in engineering reports use it.

### Content

| # | Stage | Description | Role |
|---|---|---|---|
| 01 | Site identification | Terrain, resource, access and evacuation proximity screening | ○ Supported |
| 02 | Land aggregation | Title verification, owner negotiation, consolidation | ● Led |
| 03 | Land use & exemption | Conversion position, Section 109 exemption, tenure structuring | ● Led |
| 04 | Statutory approvals | KREDL, SLAC, district administration, sectoral clearances | ● Led |
| 05 | Evacuation & connectivity | KPTCL scheme approval, bay allocation, ESCOM interface | ● Led |
| 06 | Transmission right of way | Corridor consent, compensation, objection resolution | ● Led |
| 07 | Construction & COD | Continuity support, residual approvals, local interface | ○ Supported |

### Reasoning
Marking two of seven stages as "supported" rather than "led" is deliberate and counterintuitive. **A firm that claims to lead every stage of a project it has no track record in is not believable.** Claiming five and explicitly ceding two makes the five credible. This is the same mechanism as the "what we are not" block — bounded claims read as true claims.

The stage list also becomes your internal linking spine: stages 02–06 map directly to your service pages. Each node title should be a link.

### Mobile
**Converts to a vertical stepper, not a horizontal scroll.** Vertical 1px `rule` on the left at ~20px inset, nodes on the line, content right-aligned to it, stages stacked top to bottom.

**Why not horizontal scroll on mobile:** horizontally scrolling timelines have poor affordance — a large share of users never discover there is content to the right, and on this page the content to the right is stages 04–07, which is where your entire value sits. A long vertical scroll costs nothing; an undiscovered stage costs the enquiry.

### Motion
The connecting rule draws in via `scaleX` (desktop) / `scaleY` (mobile) from origin, 700ms, followed by nodes appearing in sequence 90ms apart, then labels fading. This is the one place on the page where slightly more elaborate motion is justified — it encodes sequence, which is the section's actual meaning. `once: true`. Disabled entirely under `prefers-reduced-motion` (rule and nodes render statically).

---

## SECTION 06 — LEADERSHIP

### Purpose
Introduce the principal as the guarantor of everything above. Convert single-founder structure from a liability into a stated model.

### Desktop layout
- `surface-alt`, section padding 128px.
- 12-column grid. Portrait spans columns 1–4, full-height, aspect ratio 4:5, no rounded corners, no border. Content spans columns 6–12.
- Content order: section label → name (H3) → role line → philosophy body (3 short paragraphs) → 1px `rule` → Capability Timeline (compact vertical, 4 rows).

**Why 4:5 portrait and square corners:** circular avatars are a social-media and SaaS convention. A 4:5 rectangular editorial portrait is the convention of professional practice profiles. It also permits a proper environmental portrait rather than a cropped headshot.

### Content

> **[FOUNDER NAME — REQUIRED INPUT]**
> Founder & Principal

**Leadership philosophy — three paragraphs:**

> **On why this practice exists.** Twenty years of executing utility-scale solar, wind, hybrid and pumped storage projects in Karnataka taught me one thing repeatedly: the difference between a project that commissions on schedule and one that slips two years is almost never engineering. It is land, statute and relationships, handled early and handled properly.

> **On how the work is done.** Development support is not a document exercise. It is field work — village visits, survey records, taluk offices, individual landowners, and the same officials over years rather than weeks. It cannot be delegated to someone learning it on your project. Every engagement here is led by me personally.

> **On what I will not do.** I will not commit to an aggregation timeline before title and owner consent have been tested on the ground. I will not report a statutory position I have not confirmed at source. A developer who is told the truth late has lost a year; a developer who is told the truth early has lost a week.

**Capability Timeline** (compact vertical, 4 rows — **PLACEHOLDER ERAS, FILL WITH ACTUALS**):

| Period | Focus |
|---|---|
| [20XX–20XX] | Wind — site development, micro-siting support, land and right of way |
| [20XX–20XX] | Utility-scale solar — park-scale land aggregation and statutory approvals |
| [20XX–20XX] | Hybrid and evacuation-constrained projects — connectivity and corridor work |
| [20XX–Present] | Pumped storage and large-footprint project development support |

### Reasoning
The third paragraph is the highest-value copy on the page. **A vendor who states in advance what he will refuse to do is the only kind a project head actually trusts.** It also pre-frames the commercial relationship: when you later tell a client a timeline is not achievable, you are being consistent with a published position rather than delivering bad news.

"Every engagement here is led by me personally" reframes the constraint. Large consultancies sell with partners and deliver with associates — this is a real and widely-felt grievance among Indian developers. Principal-led delivery is a genuine differentiator, but only if stated as a *model* rather than confessed as a *limitation*.

**Photography requirement — non-negotiable.** This must be a commissioned photograph of the actual founder, ideally on site or in a field context, in natural light, business-formal or field-appropriate dress, neutral background, looking to camera. A stock portrait, an AI-generated portrait, a cropped phone photo or a blank silhouette placeholder will destroy the credibility of the entire page. **If a proper portrait is not available, delay the launch of this section rather than substitute.** An About page with a fake face is unrecoverable.

**Required inputs before build:** founder full name; exact year ranges for the capability timeline; confirmation of which asset classes to name in each era.

### Mobile
Portrait full-width at 4:5, name and role beneath, then philosophy paragraphs, then capability timeline as stacked rows with `rule` dividers. Philosophy paragraph headings ("On why this practice exists") stay — they give the mobile reader scan anchors in an otherwise long text block.

### Motion
Portrait: `fadeUp` with a subtle 1.02→1.00 scale over 800ms — the only scale transform permitted on the page, and only because a static portrait entering flat looks abrupt. Text block staggers 70ms.

---

## SECTION 07 — CORE VALUES

### Purpose
Behaviour under pressure. Written as operating commitments, not adjectives.

### Desktop layout
- `surface`, section padding 128px.
- Numbered list, full container width, each value as a row: large number (`01`, muted, ~48px, left) + value statement (H4) + supporting line (`ink-muted`).
- 1px `rule` between rows. Single column, wide measure. **Not a card grid.**

**Why a numbered list and not a 3-column icon grid:** icon-and-card value grids are the single most templated pattern on the web and are visually indistinguishable across every company that uses them. A numbered editorial list at full width reads as considered and forces the reader to actually read the sentences — which is the entire point, because the sentences are the value.

**No icons anywhere in this section.** Icons on abstract values are decorative filler and are a startup tell.

### Content

**01 — Verified before reported.**
No status reaches a client that has not been confirmed at source. We do not relay assurances we have not tested.

**02 — Land first, promises second.**
No aggregation timeline is committed until title and owner consent have been tested in the field. Optimistic land schedules are the most expensive error in Indian renewable development.

**03 — The landowner is a stakeholder, not an obstacle.**
Fair, transparent, documented dealing at village level. Every acre acquired badly becomes a litigation, an agitation or a stalled tower three years later — and it becomes the developer's problem, not the aggregator's.

**04 — Compliance over speed.**
We will not take a route that clears a file faster and leaves a title or statutory defect behind. Defects surface at diligence, refinancing or sale, when they cost the most.

**05 — One principal, one accountable owner.**
The person who assessed your site is the person in the taluk office and the person on your call. No handoffs, no account-management layer.

### Reasoning
Value 03 is the strategic centrepiece and is worth the whole section. Land agitation and litigation are among the top project-killing risks in Indian renewables, and every experienced developer has lived it. Framing landowner fairness as *the developer's risk mitigation* rather than as corporate social responsibility is both true and commercially precise — it converts an ethics statement into a de-risking statement. That is the difference between a value a buyer skims and one that makes him lean in.

Value 04's second sentence explicitly names diligence, refinancing and sale — the three moments an investment firm or IPP cares about. This section is written for the investor in the room, not the engineer.

### Mobile
Same numbered list, single column. Number moves above the statement rather than beside it, at a reduced size. `rule` dividers retained.

### Motion
Row-by-row `fadeUp`, 80ms stagger.

---

## SECTION 08 — WHY BOLAMUDI

### Purpose
Direct objection handling, including the key-man question the reader is already holding.

### Desktop layout
- `surface-alt`, section padding 128px.
- Intro block, then a 3-column comparison — **not** a competitor comparison table (naming or implying competitors is aggressive and looks insecure). Instead: three "the alternative / the difficulty / our position" reasoning columns.
- Below the columns, separated by a `rule`: the **Continuity** block, full width, 2-column (heading left, answer right).

### Content

**Section label:** `05 — WHY BOLAMUDI`

**H2:**
> Three honest reasons, and one honest answer.

**Column 1 — Against a large consultancy**
> Large firms sell with partners and deliver with associates. On development support, the value is entirely in the relationships and the field knowledge of the person actually doing it. Here, the person who sells the work is the person who does the work.

**Column 2 — Against an in-house team**
> An internal development team is built for a pipeline, not a project. For a developer entering Karnataka, or running one or two assets here, twenty years of district-level relationships cannot be hired in a quarter and cannot be justified as permanent overhead.

**Column 3 — Against a local aggregator**
> A land aggregator solves land and stops. Land solved in isolation from evacuation, statutory sequence and right of way produces a site you own and cannot build on. The stages are interdependent and are handled here as one scope.

**Continuity block:**

> **On continuity and single-principal risk**
>
> The reasonable question about a principal-led practice is what happens if the principal is unavailable or already committed. We answer it directly rather than leave it unasked.
>
> Engagements are accepted against declared capacity — if a project cannot be given proper attention in the window you need, we say so before contracting rather than after. Field execution is supported by an established network of district-level associates who have worked with us for years, under our direction and our accountability. Every engagement maintains a documented file — title chain, application status, authority correspondence, contact map — held with the client, so that project knowledge sits with your organisation and not only in our heads.

### Reasoning
This is the section that separates a serious single-principal practice from a freelancer. Three specific mechanisms are offered — capacity honesty, a named support structure, and client-held documentation — rather than reassurance. **Reassurance without mechanism is what an unserious firm offers; the mechanism is the answer.**

The third mechanism (documented file held with the client) is also a genuine commercial concession that costs you little and buys a lot: it directly answers the investor's key-man concern by asserting that project knowledge is transferable.

The comparison columns deliberately do not name competitors and do not use a checkmark/cross table. Checkmark tables are adversarial and read as insecure; three reasoned paragraphs read as senior.

**Architectural note:** when you have your first client testimonial, it belongs directly beneath this section, before the CTA. Build the slot now.

### Mobile
Columns stack. Continuity block stacks heading over body. Retain the `rule` above the Continuity block — it is doing important work signalling "this is a different kind of statement."

### Motion
Columns stagger 90ms. Continuity block `fadeUp` as one unit.

---

## SECTION 09 — HOW WE ENGAGE

### Purpose
Remove commercial ambiguity. This is the section most B2B service sites omit, and its absence is a common reason a qualified enquiry never gets sent.

### Desktop layout
- `surface`, section padding 128px.
- 3-column grid, each column: engagement model title (H4), one-line definition, then 3–4 "typical scope" lines. `rule` on top edge of each column.

### Content

**Section label:** `06 — HOW WE ENGAGE`

**H2:**
> Three ways engagements are structured.

| Model | Definition | Typical scope |
|---|---|---|
| **Pre-acquisition assessment** | A bounded, short-duration review before you commit capital to a site. | Evacuation and bay availability check · Title and classification screening across the target survey numbers · Statutory pathway and realistic timeline · Go / no-go position |
| **Stage mandate** | Retained for a defined stage — land, approvals, evacuation or right of way. | Defined deliverable and completion criteria · Fixed reporting cadence · Priced against scope, not time |
| **Full development support** | Retained from site identification to construction-ready handover. | All stages 02–06 of the development lifecycle · Single accountable point of contact · Continuous status file held with the client |

**Closing line beneath the grid:**
> Commercial terms are discussed against a specific site and a specific timeline. We do not quote development support against a brief.

### Reasoning
The final line does two jobs. It protects you from unpriceable scope, and it signals seniority — junior firms quote anything, senior firms qualify first. It also sets the expectation that the first conversation is a technical discussion about a site, which is the conversation where your twenty years actually show, rather than a price conversation where you have no track record to defend a rate.

"Pre-acquisition assessment" as the first, smallest, lowest-commitment model is the most important commercial design choice on the page. **A developer will not hand a full mandate to a firm with no visible track record — but he will absolutely pay for a bounded evacuation-and-title check on a site he is about to buy.** That is your realistic entry product, and the page should make it the easiest thing to ask for.

### Mobile
Columns stack with `rule` dividers. Scope lines become a proper bulleted list rather than middot-separated inline text — inline middots wrap badly at narrow widths.

---

## SECTION 10 — CLOSING CTA

### Purpose
One action.

### Desktop layout
- Full-width band, inverted (`ink` background, `surface` text) — the only inverted section on the page, which is why it reads as terminal.
- Centred content, max 60ch. Section padding 112px.

### Content

**H2:**
> If you are assessing a site in Karnataka, start with the questions that decide the project.

**Body:**
> Is the land clean, is the bay available, and is the corridor realistic. We will tell you before you commit capital, not after.

**Primary button:** `Start a site discussion` → `/contact`
**Secondary text link:** `View development support services` → `/services`

### Reasoning
"Start a site discussion" outperforms "Contact us" because it names the shape of the conversation and lowers perceived commitment — the reader is agreeing to a technical discussion about a site, not to a sales call. Two actions only: one for ready buyers, one for readers who need more evidence. A third option reduces both.

**One CTA per page.** Repeated mid-page CTAs on an About page interrupt an evaluation the reader is trying to complete.

### Mobile
Full-width primary button, secondary link beneath. Padding 80px.

---

# PART 3 — RESPONSIVE & LAYOUT SYSTEM

## 3.1 Breakpoints and grid

| Breakpoint | Width | Grid | Container | Gutter | Section padding (y) |
|---|---|---|---|---|---|
| Mobile | <640px | 4 col | 100% − 40px | 16px | 72px |
| Tablet | 640–1023px | 8 col | 100% − 80px | 24px | 96px |
| Desktop | 1024–1439px | 12 col | max 1120px | 32px | 112px |
| Wide | ≥1440px | 12 col | max 1200px | 32px | 128px |

**Container caps at 1200px and does not scale further.** Reason: measure. Body text beyond ~75 characters per line degrades reading speed measurably, and this page is text-heavy by design. On ultra-wide displays the correct behaviour is more whitespace, not longer lines. Full-bleed treatments are reserved for the hero image and the two inverted/alt bands.

## 3.2 Vertical rhythm

All vertical spacing on an 8px base. Section padding, block gaps and rule offsets must be multiples of 8. Inconsistent vertical rhythm is the most common reason a technically-correct build still reads as amateur — it is felt before it is noticed.

## 3.3 Type scale (ratios, not pixels — map to your locked system)

| Role | Desktop | Mobile | Leading | Tracking |
|---|---|---|---|---|
| H1 display | 1.00× base display | 0.62× | 1.05 | −0.02em |
| H2 | 0.58× | 0.44× | 1.15 | −0.01em |
| H3 | 0.40× | 0.34× | 1.25 | −0.01em |
| H4 | 0.30× | 0.28× | 1.35 | 0 |
| Body large (deck) | 0.24× | 0.22× | 1.55 | 0 |
| Body | 0.20× | 0.20× | 1.65 | 0 |
| Small / label | 0.16× | 0.16× | 1.45 | +0.08em uppercase |

Negative tracking on display sizes and positive tracking on uppercase labels. Both are required — display type set at default tracking looks loose and consumer; uppercase labels at default tracking look cramped and cheap.

## 3.4 Rules and dividers

1px, `rule` token, never 2px, never dashed. The 1px hairline used consistently across sections is the primary structural device of this design and the main visual carrier of "engineering document" rather than "marketing page."

## 3.5 Mobile-specific decisions and their reasons

| Decision | Reason |
|---|---|
| Lifecycle timeline becomes vertical stepper | Horizontal scroll hides stages 04–07, which contain your core value |
| Domain Command lists stay fully expanded, no accordions | The lists are the proof; hiding proof behind a tap is a net loss even at the cost of scroll length |
| Credibility strip 2×2, never horizontal scroll | Half a credibility strip is worse than none |
| Hero image before hero text | Consistent LCP element across breakpoints; better first-impression engagement |
| Philosophy paragraphs keep their bold lead-ins | Scan anchors in a long mobile text block |
| Body text never below 16px | Below 16px triggers iOS input zoom behaviour patterns and reads as unserious on a professional site |
| Tap targets minimum 44×44px | Standard accessibility floor; the timeline nodes are links and are the most likely violation |

---

# PART 4 — IMAGERY DIRECTION

## 4.1 The rule

**Every photograph on this site must be capable of being true.** Your audience knows what a Karnataka RE site looks like. They also know what a Shutterstock solar farm looks like — panels in an unnaturally green field under a European sky, or a hard-hatted model pointing at a turbine. That image is the single most reliable indicator of a company without projects, and using one undoes the credibility that Section 04 spent 27 line items building.

## 4.2 Required shot list

| Slot | Subject | Treatment |
|---|---|---|
| Hero | Karnataka RE terrain — dry Deccan plateau scrub, red laterite soil, transmission line receding into distance, low sun | Wide, documentary, natural colour, no lens flare, no HDR, no colour grade toward teal/orange |
| Leadership | Commissioned founder portrait, 4:5, on-site or field context, natural light | Neutral, direct, no studio background, no retouching beyond correction |
| Optional Section 05 background | Transmission corridor or substation bay, near-abstract crop | Heavily desaturated, low contrast, used only behind whitespace, never behind text |

## 4.3 Prohibited

Stock renewable imagery of any kind · turbines in Northern-European landscapes · people in hard hats holding tablets · handshake photographs · glass-and-steel office exteriors · AI-generated imagery of any kind (including the founder portrait) · overlaid gradient meshes on photographs · any image containing a facility you did not work on.

## 4.4 Treatment consistency

All photography: consistent desaturation of roughly 10–15%, no vignettes, no duotone. Consistency across a small image set reads as art direction. Three differently-graded images read as sourced from three different places, which is what they will be if unmanaged.

## 4.5 Non-photographic visuals

Prefer them. A precisely-set Karnataka district map showing coverage, or the lifecycle diagram, carries more credibility than any photograph, because a diagram cannot be stock. **If the photography budget is constrained, spend it entirely on the founder portrait and make everything else typographic and diagrammatic.** That is a legitimate, senior-looking design direction — and it is measurably safer than bad photography.

## 4.6 Performance

`next/image` throughout. Hero: `priority`, AVIF with WebP fallback, `sizes` set per breakpoint, explicit width/height to reserve layout space (CLS). Every non-hero image lazy-loaded. Hero image budget: under 180KB at 1440px. Descriptive alt text on all images — decorative-only images get `alt=""`, never a missing alt attribute.

---

# PART 5 — MOTION SPECIFICATION (FRAMER MOTION)

## 5.1 Principle

**Motion on this page confirms hierarchy. It does not entertain.** The reader is evaluating a firm's seriousness. Every animation that delays content acquisition costs credibility with this audience specifically. The target is that a reader who scrolls fast never once waits for anything.

## 5.2 The only two primitives

```
fadeUp:   { opacity: 0, y: 16 } → { opacity: 1, y: 0 }
          duration 0.5s, ease [0.16, 1, 0.3, 1]

stagger:  staggerChildren 0.06–0.09, delayChildren 0
```

Every section on this page uses one or both. Nothing else, with two documented exceptions: the lifecycle rule draw (Section 05) and the portrait's 1.02→1.00 scale (Section 06).

**Why y:16 and not y:40:** a large travel distance means content is visibly out of position when it enters, which on a fast scroll produces a lurching sensation. 16px is enough to register as arrival and small enough to never be perceived as movement-for-its-own-sake.

**Why that easing curve:** heavy front-loaded deceleration. It settles rather than eases. Linear or `easeInOut` on entrance animations reads as a template default.

## 5.3 Viewport configuration

`viewport={{ once: true, margin: "-80px" }}` on every scroll-triggered element.

`once: true` is non-negotiable. Re-animating on scroll-up is the most irritating pattern in modern web design and is disproportionately noticed by senior readers who scroll back to re-read — which is exactly what your buyer does on a page like this.

## 5.4 Prohibited

Parallax · scroll-jacking or pinned sections · count-up number animations · text reveal by character or word · marquees · auto-playing carousels · hover transforms that lift or scale cards (there are no cards) · cursor followers · any animation exceeding 800ms · any animation on the LCP element.

## 5.5 Accessibility

```
prefers-reduced-motion: reduce
→ all transforms disabled, opacity transitions capped at 0.15s,
  timeline rule and nodes render statically at final state
```

Implement via a `useReducedMotion()` guard at the variant level, not by disabling components. Content must always render.

## 5.6 Page transitions

None. Route-level page transitions add perceived latency and this audience navigates deliberately. Scroll restoration on back-navigation must work correctly.

---

# PART 6 — SEO SPECIFICATION

## 6.1 Search reality check

You will not rank for "renewable energy consultant India" or "solar EPC company." Those are dominated by national players with years of domain authority. Competing there is wasted budget.

**You will rank, quickly and cheaply, for long-tail geo-and-procedure queries with near-zero competition and extremely high commercial intent.** Someone searching "Section 109 exemption for solar project Karnataka" is not browsing. That is your entire SEO strategy: own the procedural long tail.

## 6.2 Target queries for this page

**Primary:** renewable energy project development support Karnataka · land aggregation for solar projects Karnataka

**Secondary:** government liaison renewable energy Karnataka · statutory approvals solar wind project Karnataka · transmission right of way consultant Karnataka · KREDL approval consultant · pumped storage project development support Karnataka · land acquisition consultant for IPP Karnataka

**Long-tail (highest conversion, lowest competition — these should be served by dedicated service or insight pages that link back to this About page):** Section 109 Karnataka Land Reforms Act solar project · land conversion for renewable energy projects Karnataka 2025 rules · KPTCL evacuation scheme approval process · Gomala land renewable energy project

## 6.3 Metadata

```
Title:       About Bolamudi Enterprise | Renewable Energy Project
             Development Support, Karnataka
             (71 characters)

Description: Bolamudi Enterprise provides land aggregation, statutory
             approvals, government liaison and transmission right of way
             support for utility-scale solar, wind, hybrid and pumped
             storage projects across Karnataka. Led by a principal with
             20+ years of execution experience.
             (Trim to 155 characters for display; full version acceptable
             as og:description)

Canonical:   https://[domain]/about
OG image:    1200×630, hero photograph with wordmark, no marketing text
```

## 6.4 Heading structure

Exactly one H1 (hero). Ten H2s, one per section. H3 for domain blocks and founder name. H4 for lifecycle stages, values and engagement models. **Never skip a level for styling** — use a class, not a heading tag.

## 6.5 Structured data

Two JSON-LD blocks. Do **not** use `LocalBusiness` — it implies walk-in premises and is the wrong entity type for an advisory practice.

```
1. Organization
   name, url, logo, description,
   areaServed: { "@type": "State", "name": "Karnataka" },
   founder: { "@type": "Person", ... },
   knowsAbout: [
     "Renewable energy project development",
     "Land aggregation",
     "Statutory approvals",
     "Transmission right of way",
     "Pumped storage projects",
     "Government liaison"
   ],
   sameAs: [ LinkedIn company page ]

2. Person (founder)
   name, jobTitle: "Founder & Principal",
   worksFor: { "@id": Organization },
   knowsAbout: [ ... ],
   sameAs: [ LinkedIn profile ]
```

`BreadcrumbList` if the site uses a breadcrumb pattern; omit it if not — do not mark up a breadcrumb that is not visible on the page.

## 6.6 Internal linking

The About page should be a hub, not a leaf.

- Each lifecycle stage node (02–06) links to its service page
- Each Domain Command block heading links to its service page
- Engagement models link to `/contact`
- Descriptive anchor text throughout — never "learn more" or "click here"

**A link from `/about` carries meaningful internal authority because About is typically the second-most-linked page on a small site.** Currently most sites waste it entirely. Wiring five contextual links from here into your service pages is free ranking benefit.

## 6.7 Technical

Server-render this page. It is static content with zero dynamic requirements — there is no justification for client-side rendering. Framer Motion components must be isolated as client components so the surrounding content remains server-rendered.

Targets: LCP under 2.0s · CLS under 0.05 · INP under 200ms. Font strategy: `next/font` with `display: swap` and preloaded subsets. A late-loading webfont on a page whose entire visual identity is typographic is a first-impression failure.

## 6.8 Content freshness

Add a `dateModified` to the Organization schema and review Section 04 every six months. Statutory references are your credibility mechanism and also your maintenance liability — the 2025 conversion rules amendment is a live example of a change that would have silently dated this page.

---

# PART 7 — ACCESSIBILITY

| Requirement | Application here |
|---|---|
| Contrast | All body text ≥ 4.5:1, large display ≥ 3:1. `ink-muted` on `surface-alt` is the likeliest failure — test it specifically. |
| Semantic HTML | `<section>` with `aria-labelledby` pointing at each H2. Lifecycle as an ordered list, not a div stack. |
| Focus states | Visible 2px focus ring on all interactive elements. Do not remove default outlines without replacement. |
| Reduced motion | Per Part 5.5. |
| Alt text | Descriptive on all content images. Founder portrait: name and context, not "portrait." |
| Keyboard | Full page traversable; logical tab order; timeline node links reachable in sequence. |
| Zoom | No horizontal scroll at 200% zoom at 1280px. The horizontal timeline is the risk — it must collapse to the vertical stepper at that effective width. |

---

# PART 8 — REQUIRED INPUTS BEFORE BUILD

The page cannot ship without these. Everything else in this document is decided.

1. **Founder full name** and preferred title
2. **Commissioned founder portrait** — see Part 4.2. Blocking. Do not substitute.
3. **Capability timeline year ranges** — the four era rows in Section 06
4. **Confirmation of asset-class claims per era** — which of solar / wind / hybrid / PSP in which period
5. **Locked design tokens** — the semantic names used here mapped to your existing variables
6. **Legal confirmation** on Section 03's "we are not paid by the landowner" statement — it must be operationally true, because it will be quoted back to you
7. **Any figure at all that can be defended** — even one ("over 3,000 acres assessed," "projects across 7 districts"). One defensible number materially strengthens Section 02. Do not invent one.

---

# PART 9 — HONEST SUMMARY

This page is designed to do one thing: make a project head at an IPP think *this person has actually done this*, within ninety seconds, without a single case study.

It achieves that through four mechanisms:

1. **Procedural specificity** as a substitute for track record (Section 04)
2. **Bounded claims** — stating what you do not do, and which stages you do not lead (Sections 03 and 05)
3. **Pre-emptive objection handling** — conflict of interest and key-man risk named before the reader raises them (Sections 03 and 08)
4. **Visual restraint** — hairline rules, editorial grid and typographic discipline instead of the scale signals you have not earned

The weakest point in the plan remains what you told me at the outset: no nameable proof. Design cannot fully solve that. **The single highest-return action available to you is not on this page — it is securing one client, of any size, who will let you name them, or one defensible number.** The moment you have either, Section 02 and the slot beneath Section 08 are already built to receive it, and this page becomes roughly twice as effective.

Build the page. Then go get the number.
