# Bolamudi Enterprise — Information Architecture

**Project:** Corporate website
**Stack:** Next.js · TypeScript · Tailwind · shadcn/ui · Framer Motion
**Document:** Information Architecture, Navigation, Wireframes, Visual System
**Version:** v1.0 — Locked
**Date:** August 2026
**Precedes:** Visual design → Design system → Build

---

## 0. Governing Constraints

This IA is shaped by five confirmed inputs. Every structural decision below traces to one of them.

| # | Constraint | Structural consequence |
|---|---|---|
| C1 | All prior projects under NDA. No nameable clients, no case studies. | No `/projects`, no `/experience`, no testimonials, no logo bar. |
| C2 | Sole proprietorship. One person. | No team page, no careers. "Principal", not "Leadership". |
| C3 | No owned photography. | Cartographic, diagrammatic and typographic visual system. Zero stock. |
| C4 | No articles will be written. | No `/insights` at launch. Domain knowledge relocated into `/about` and `/karnataka`. |
| C5 | Fee structure not published; conflict-of-interest position undeclared. | No `/approach` page. Process compressed to a homepage strip. Conflict slot reserved in `/about`. |

**Honest scope statement.** With no clients, projects, photography, published content or engagement model, this site cannot generate cold inbound business. Its realistic and achievable job is **referral validation** — a buyer receives the name, checks the site, and finds no reason to disqualify. The IA is optimised for that job and no other.

**Open risk (unresolved):** the conflict-of-interest position. The firm brokers and facilitates. A developer's default assumption is that the intermediary may also be taking seller-side value. One published line closes this. A slot is reserved in `/about` §04. Until filled, this is the site's largest remaining credibility gap.

---

## 1. Sitemap

12 pages. Maximum depth: 2 levels, and only under Services.

```
/
├── /about                                   ← primary proof asset
├── /services                                [hub]
│   ├── /services/land-aggregation           ★ flagship
│   ├── /services/government-liaison
│   ├── /services/statutory-approvals
│   ├── /services/transmission-row
│   └── /services/project-development-support
├── /sectors                                 [single page, not a hub]
├── /karnataka                               ★ only demonstrable asset
├── /contact
├── /privacy-policy
└── /terms
```

### 1.1 Why this shape

**Shallow and dense, not deep and thin.** Enterprise credibility comes from substance per page, not page count. A 40-page site with 200-word pages reads as an abandoned template. A 12-page site with genuine density reads as deliberate. Reference firms (Arup, Black & Veatch) have depth because they have decades of published evidence. Copying their *structure* without their *evidence* exposes the gap rather than concealing it.

### 1.2 Deletions and their rationale

| Deleted | Reason |
|---|---|
| `/projects` `/experience` | Nothing to populate them. A page promising a track record and delivering adjectives destroys more trust than its absence. |
| `/insights` + articles | No content commitment. A blog with zero or two posts is the loudest possible "abandoned project" signal. Route reserved, not built. |
| `/approach` (standalone) | Without fee structure or conflict position it reduces to a process diagram. Insufficient to hold a page. Diagram relocated to homepage §06. |
| `/about/principal` (separate) | One person, no team. Splitting produces two thin pages instead of one solid one. Merged into `/about`. |
| 4 × sector pages | Each would be ~200 words of generic technology description with no projects to anchor them. Four thin pages read as padding. Consolidated into one `/sectors` page with four substantive sections. |
| `/careers` | An empty careers page states "we have no employees." Add at 5+ staff. |
| `/news` | No news. |

### 1.3 Retentions and their rationale

| Retained | Reason |
|---|---|
| Government Liaison as a separate service page | Distinct buyer intent and distinct search behaviour from Statutory Approvals. Liaison = revenue department, district administration, land records. Approvals = KREDL, KERC, CEIG, forest, NOCs. Merging halves the addressable surface. **Content note:** the page describes departments and process, never relationships or access. See §9.2. |
| `/karnataka` as a top-level page | The only content on the site that demonstrates rather than asserts. District-level operational knowledge is not confidential and cannot be faked by a broker. |
| Transmission RoW as its own page | Highest-specificity service, distinct buyer (transmission contractors, EPC), and the one term with genuine search intent. |
| "RE Project Facilitation" **not** given a page | Umbrella term overlapping every other service. Becomes a positioning line on `/services`, not a destination. Vague pages dilute authority and cannibalise. |

---

## 2. Page Hierarchy

| Level | Pages | Function |
|---|---|---|
| **L0** | Home | Complete summary of the firm. Routes to all L1. |
| **L1** | About · Services · Sectors · Karnataka · Contact | Browse destinations. Each self-sufficient. |
| **L2** | 5 × service detail | Depth. Entered from hub, nav dropdown, or cross-links. |
| **Utility** | Privacy · Terms | Footer only. Excluded from nav and sitemap priority. |

**Weighting.** Not all L1 pages are equal. Ranked by load-bearing importance:

1. `/about` — carries the entire proof burden. The person is the product.
2. `/karnataka` — the only demonstrable expertise asset.
3. `/services/land-aggregation` — flagship commercial page; the actual product.
4. `/services` hub — routing and process demonstration.
5. Remaining service pages.
6. `/sectors` — qualification only, deliberately light.
7. `/contact` — terminal node.

---

## 3. Content Hierarchy

Two independent axes, never duplicated:

- **Services** = *what is done*. Commercial and search weight. 900–1,400 words each.
- **Sectors** = *what it is done for*. Positioning and qualification. Single page, four sections.

**Enforced rule:** a sector section never explains a service, and a service page never explains a technology. They cross-link instead. This prevents the internal cannibalisation that degrades small consultancy sites.

### 3.1 Word targets

| Page | Words | Note |
|---|---|---|
| Home | 500–700 | Structural, not narrative |
| About | 900–1,200 | Densest page on the site |
| Services (hub) | 400 + cards | Includes process strip |
| Land Aggregation | 1,200–1,400 | Flagship |
| Government Liaison | 900–1,100 | Process-framed only |
| Statutory Approvals | 1,000–1,200 | Authority-by-authority |
| Transmission RoW | 900–1,100 | Highest search intent |
| Project Development Support | 700–900 | |
| Sectors | 800–1,000 | Four sections |
| Karnataka | 1,000 + map + tables | Second-densest |
| Contact | 200 | |

---

## 4. Navigation

### 4.1 Desktop

Sticky header, 64px, no shadow until scroll (then 1px hairline, no drop shadow).

```
┌──────────────────────────────────────────────────────────────────┐
│ BOLAMUDI ENTERPRISE   About  Services ▾  Sectors  Karnataka      │
│                                        [ Discuss a Project → ]   │
└──────────────────────────────────────────────────────────────────┘
```

**Five items. Ceiling is six, permanently.**

| Decision | Rationale |
|---|---|
| Contact is not a nav link | It is the CTA button. Two paths to one destination dilutes; one dominant path converts. |
| Karnataka promoted into nav | With Insights and Experience cut, it is now the second-strongest page. Browse destinations must be the strongest pages available. |
| Services dropdown = simple 5-item list with one-line descriptors | A mega panel had nothing left to fill its right rail. An under-filled mega panel looks worse than a clean list. |
| Sectors has no dropdown | Single page. |
| Active-state underline on current section | With breadcrumbs only on L2, nav state is the primary orientation cue on L1. |
| No search | 12 pages. An empty result set destroys trust faster than a missing feature. |
| No language toggle | Buyers read English. Kannada capability belongs in the field, not the website. |

### 4.2 Mobile

- **Full-screen overlay drawer.** Not a half-panel slide-in — half-panels are a consumer-app pattern.
- **Services accordion, closed by default.** Shows hierarchy exists; lets the thumb decide.
- **Order identical to desktop.** Divergent mobile IA is the most common credibility leak in agency work.
- **Sticky bottom bar, 56px:** `Call` (50%) / `Enquire` (50%).
- Header CTA collapses to an icon; the bottom bar carries conversion.
- Logo returns to home. No hamburger-only header.

**Why the bottom bar is the single highest-value component on the site:** the buyer is frequently a land or project manager standing in a field in Ballari or Koppal with poor connectivity. A `tel:` tap outperforms every form on the site.

### 4.3 Breadcrumbs

| | |
|---|---|
| **Shown on** | `/services/*` only (the only L2 pages) |
| **Hidden on** | Home, all L1 pages |
| **Format** | `Home / Services / Land Aggregation` — plain text, above H1, small caps, muted, no chevron icons, no colour |
| **Last item** | Unlinked text. Prevents self-referential loops. |
| **Schema** | `BreadcrumbList` JSON-LD on all breadcrumbed pages |

**Rationale.** Breadcrumbs at depth 1 are visual noise — the nav active state already communicates position. At 12 pages the *user* value is low, but the *schema* value is high: BreadcrumbList markup is the cheapest way to make Google render hierarchy in results, which makes a small site appear structured.

---

## 5. Footer

Three columns plus legal bar. Three, not four — a thin fourth column looks unbalanced at this content volume.

```
┌─────────────────────────────────────────────────────────────────┐
│ BOLAMUDI ENTERPRISE   │  SERVICES        │  COMPANY             │
│ One-line positioning  │  Land Aggregation│  About               │
│ Karnataka, India      │  Government      │  Karnataka           │
│                       │    Liaison       │  Sectors             │
│ Udyam Reg. No.        │  Statutory       │  Contact             │
│ GSTIN                 │    Approvals     │  LinkedIn            │
│ [Registered address]  │  Transmission RoW│                      │
│ +91 XXXXX XXXXX       │  Project Dev     │                      │
│ email@domain          │    Support       │                      │
│─────────────────────────────────────────────────────────────────│
│ © 2026 Bolamudi Enterprise          Privacy · Terms             │
└─────────────────────────────────────────────────────────────────┘
```

| Decision | Rationale |
|---|---|
| Registration numbers in footer | Cheapest, highest-yield trust signal in Indian B2B. Serious buyers check. With no clients or projects, verifiable registration is the strongest hard evidence available. |
| Full postal address, not "Bengaluru, India" | Geographic vagueness is the defining signal of an intermediary. Specificity is the opposite claim. |
| No newsletter signup | Nothing to send. A dead signup form is worse than none. |
| LinkedIn only | Instagram or X on an infrastructure consultancy site is a category downgrade. |
| Footer is the secondary navigation | With five nav items, the footer carries the pages nav cannot. |

---

## 6. CTA Strategy

Two tiers. Never more than one primary CTA per viewport.

| Tier | CTA | Destination | Placement |
|---|---|---|---|
| **Primary** | Discuss a Project | `/contact` | Header (persistent) · Home hero · End of every service page · CTA band on every page |
| **Tertiary** | Direct call / email | `tel:` / `mailto:` | Footer · Mobile sticky bar · Contact page · Homepage CTA band |

### 6.1 Deleted CTA — and why

**Gated capability PDF: removed.** With no clients, projects, fee structure or methodology detail, the document would be three pages of adjectives. Gating weak content behind an email form is worse than not offering it, and it burns the highest-intent moment on the site. Reinstate when there is substance to put in it.

### 6.2 Placement rules

- Hero CTA above the fold on the homepage only.
- Service pages: CTA after the process section, never after the intro. Let the page earn the ask.
- **Banned outright:** exit-intent popups, chat bubbles, scroll-triggered modals, sticky promo bars, countdown or scarcity devices. Each is an explicit startup/SaaS signal and directly contradicts the stated positioning.
- CTA copy is specific, never generic. "Discuss a Project" — not "Get Started", "Learn More", or "Let's Talk".

---

## 7. User Flows

Only one flow converts at meaningful volume. Design for it; do not model the others.

### Flow A — Referral validation (primary, ~80% of value)

```
Name heard from a contact
        ↓
Google search "Bolamudi Enterprise" / direct URL
        ↓
HOME or /ABOUT          → Is this person real and senior?
        ↓
/ABOUT                  → 20 years, departments, districts
        ↓
/services/land-aggregation → Does he handle my specific problem?
        ↓
/karnataka              → Does he know my district?
        ↓
CALL  (not form)
```

**IA requirements this generates:**
- `/about` must be reachable in one click from every page. It is the credential.
- The homepage must push toward `/about` harder than conventional design allows — the person *is* the product.
- Entry may be `/about` directly (LinkedIn, forwarded link). It must stand alone as a complete document with no homepage context assumed.
- Termination is a phone call, not a form. Phone must be visible at every scroll position on mobile.

### Flow B — Service-specific search (secondary, low volume)

```
Google "transmission right of way Karnataka" / "land conversion 109 solar"
        ↓
/services/transmission-row  (deep entry)
        ↓
/about   (who is this?)     ← mandatory detour
        ↓
/karnataka
        ↓
CALL
```

**IA requirement:** deep entry is the norm, not the exception. Every service page must establish *who Bolamudi is* in its first screen, not merely describe the service. No page may assume the homepage has been seen.

### Flow C — Diligence / procurement check (rare, high stakes)

```
LinkedIn or forwarded link
        ↓
/about → career record, departments, entity registration details
        ↓
Footer → Udyam, GSTIN, registered address
        ↓
Exit (no conversion event)
```

**IA requirement:** this flow never touches a service page and never converts. It is still decisive — it determines whether a champion inside the buyer organisation can defend the recommendation. `/about` and the footer must satisfy it without any commercial framing.

### Flow D — Not designed for

Cold inbound from generic search. It will not convert at present content depth. Excluded deliberately rather than served badly.

---

## 8. Internal Linking Strategy

Hub-and-spoke, with three enforced rules that override editorial preference.

### 8.1 Enforced rules

1. **Every service page links to `/about`** in its closing section. In a one-person firm the credential is the person; the link graph must reflect that.
2. **Every service page links to `/karnataka`** inline in body copy. The proof is the geography.
3. **`/karnataka` links to all five service pages.** It is the topical hub and must distribute authority.

### 8.2 Link graph

```
                       ┌──────────┐
                       │   HOME   │
                       └────┬─────┘
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
      ┌───────┐      ┌────────────┐     ┌───────────┐
      │ ABOUT │◄─────│  SERVICES  │────►│ KARNATAKA │
      └───┬───┘      │    (hub)   │     └─────┬─────┘
          │          └──────┬─────┘           │
          │                 │                 │
          │        ┌────────┴────────┐        │
          │        ▼   5 × service   ▼        │
          │      ┌─────────────────────┐      │
          └─────►│  service detail L2  │◄─────┘
                 └──────────┬──────────┘
                            │  lateral: related services
                            ▼
                       ┌─────────┐
                       │ SECTORS │
                       └────┬────┘
                            ▼
                       ┌─────────┐
                       │ CONTACT │  ← terminal node
                       └─────────┘
```

### 8.3 Additional rules

- **Lateral service ↔ service:** each service page closes with two contextually adjacent services. Strongest pair: Land Aggregation ↔ Transmission RoW (both are land-tenure problems). Second: Government Liaison ↔ Statutory Approvals.
- **Contact is terminal.** It links only to Home via the logo. Outbound links from a conversion page leak intent.
- **Maximum depth:** 2 clicks from home to any page.
- **No footer link-stuffing** beyond the three columns specified.
- Anchor text is descriptive, never "click here" or "read more".

---

## 9. Page Wireframes

### 9.1 Home — Desktop

```
┌──────────────────────────────────────────────────────────────────┐
│ BOLAMUDI ENTERPRISE      About  Services▾  Sectors  Karnataka    │ 64px sticky
│                                          [Discuss a Project →]   │
└──────────────────────────────────────────────────────────────────┘

┌─ 01 · HERO ──────────────────────── full-bleed, 82vh ────────────┐
│                                                                  │
│  KARNATAKA                                          ┌──────────┐ │
│                                                     │  STATE   │ │
│  Land aggregation and statutory                     │  OUTLINE │ │
│  approvals for utility-scale                        │  w/ RE   │ │
│  renewable energy projects.                         │ districts│ │
│                                                     │  marked  │ │
│  ─────────────────────────────────                  └──────────┘ │
│  Principal-led. 20 years in utility-scale                        │
│  solar, wind, hybrid and pumped storage.                         │
│                                                                  │
│  [ Discuss a Project → ]    [ How we work ↓ ]                    │
└──────────────────────────────────────────────────────────────────┘
```
**Decisions.** No image, no video, no stock. The Karnataka outline is the hero visual — the one asset owned outright, and it declares geographic focus before a word is read. The headline names service + scale, not a slogan; enterprise buyers scan for capability, not inspiration. The credential line sits below a hairline rule at small scale — asserted once, quietly. Loud credentials read insecure.

```
┌─ 02 · POSITIONING ──────────── 2-col, 60/40 ────────────────────┐
│  Dense 3-sentence paragraph:      │  ── Focus                   │
│  what the firm does, for whom,    │  Utility-scale only         │
│  in which state. No adjectives.   │  ── Geography               │
│                                   │  Karnataka                  │
│                                   │  ── Model                   │
│                                   │  Principal-led mandates     │
└─────────────────────────────────────────────────────────────────┘
```
**Decision.** The right rail is a spec block, not marketing copy — it reads as a datasheet. This slot is conventionally occupied by a client logo bar. With no logos available, a factual spec strip occupies the position rather than leaving a structural gap that reads as absence.

```
┌─ 03 · SERVICES ───────────────── 5 cards, 3+2 grid ─────────────┐
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                │
│  │ 01          │ │ 02          │ │ 03          │                │
│  │ Land        │ │ Government  │ │ Statutory   │                │
│  │ Aggregation │ │ Liaison     │ │ Approvals   │                │
│  │ 2 lines     │ │ 2 lines     │ │ 2 lines     │                │
│  │        →    │ │        →    │ │        →    │                │
│  └─────────────┘ └─────────────┘ └─────────────┘                │
│  ┌─────────────┐ ┌─────────────┐                                │
│  │ 04 Trans-   │ │ 05 Project  │                                │
│  │ mission RoW │ │ Dev Support │                                │
│  └─────────────┘ └─────────────┘                                │
└─────────────────────────────────────────────────────────────────┘
```
**Decisions.** Numbered 01–05 — sequence implies method rather than menu. Cards are bordered, never shadowed; shadows plus rounded corners are the SaaS tell. Land Aggregation carries a heavier top rule to mark flagship status without a "featured" badge.

```
┌─ 04 · PRINCIPAL ────────────── 40/60, muted bg ─────────────────┐
│  ┌────────────┐   Two decades in utility-scale renewable        │
│  │            │   energy development across Karnataka.          │
│  │  MONOGRAM  │                                                 │
│  │    "BE"    │   Most recently in a senior management role     │
│  │            │   responsible for land and approvals.           │
│  └────────────┘                                                 │
│                   Land · Approvals · RoW · Liaison              │
│                   → About the Principal                         │
└─────────────────────────────────────────────────────────────────┘
```
**Decisions.** Positioned immediately after services because the product is the person and the traffic is referral validation. A typographic monogram, not a portrait — with no owned photography, a phone portrait would undo the entire visual system. A restrained monogram reads deliberate; a poor photograph reads amateur. Muted background separates it as an interstitial and breaks the card-grid rhythm.

```
┌─ 05 · KARNATAKA ───────────────── full-bleed ───────────────────┐
│  Where we work                                                  │
│  ┌──────────────────────┐  Ballari      Solar + Wind            │
│  │                      │  Koppal       Solar                   │
│  │   DISTRICT MAP       │  Gadag        Wind                    │
│  │   RE corridors       │  Vijayapura   Solar + PSP             │
│  │   evacuation nodes   │  Chitradurga  Wind                    │
│  │                      │  Tumakuru     Solar                   │
│  └──────────────────────┘  → Karnataka in detail                │
└─────────────────────────────────────────────────────────────────┘
```
**Decision.** The only demonstrable asset on the site. Districts paired with technology in a table — specificity substitutes for case studies. Nobody without operating history writes this list correctly, and the reader in the market knows it.

```
┌─ 06 · PROCESS ────────────── horizontal stage-gate ─────────────┐
│  01 ──── 02 ──── 03 ──── 04 ──── 05 ──── 06                     │
│  Site   Tenure  Aggre-  Conver- Appro-  RoW &                   │
│  ID     Dilig.  gation  sion    vals    Handover                │
│  ↓      ↓       ↓       ↓       ↓       ↓                       │
│  1 line each: the deliverable produced at that gate             │
└─────────────────────────────────────────────────────────────────┘
```
**Decision.** This is the deleted `/approach` page compressed into a strip. Each gate states its **deliverable**, not its activity — deliverables are what distinguish a consultant from a broker, and this block does more anti-broker work than any copy on the site. Drawn in engineering-diagram register: hairlines, numerals, no illustration.

```
┌─ 07 · SECTORS ───────────────── 4-col text ─────────────────────┐
│  Solar │ Wind │ Hybrid │ Pumped Storage       → Sectors         │
└─────────────────────────────────────────────────────────────────┘
```
**Decision.** Deliberately thin. Sectors are qualification, not differentiation — every competitor covers solar and wind. Additional weight here would be padding, and padding is visible.

```
┌─ 08 · CONFIDENTIALITY ────────── centred, narrow ───────────────┐
│  "We do not disclose client identities or transaction details,  │
│   during or after engagement. In land aggregation, discretion   │
│   is a commercial control, not a courtesy."                     │
└─────────────────────────────────────────────────────────────────┘
```
**Decision.** Converts the site's largest gap into a stated professional standard and pre-empts *"why are there no clients here?"* before the visitor consciously forms the question. Placed late in the scroll because it answers a doubt that only surfaces after browsing.

```
┌─ 09 · CTA BAND ─────────────── dark, full-bleed ────────────────┐
│  Discuss a project.        [ Contact → ]   +91 XXXXX  ·  email  │
└─────────────────────────────────────────────────────────────────┘
┌─ FOOTER · 3 columns ────────────────────────────────────────────┐
```

---

### 9.2 /about — Desktop

No breadcrumb (L1). This page carries the site.

```
┌─ HEADER ────────────────────────────────────────────────────────┐
│  Principal                                                      │
│  [Name]                                                         │
│  ──────────────────────────────────────────                     │
│  Bolamudi Enterprise is a proprietorship providing land         │
│  aggregation and statutory approval support to renewable        │
│  energy developers in Karnataka.                                │
└─────────────────────────────────────────────────────────────────┘

┌─ 01 · CAREER RECORD ──────────── 2-col 65/35 ───────────────────┐
│  3–4 paragraphs, anonymised:      │  ── Experience              │
│  20 years, utility-scale,         │  20 years                   │
│  Karnataka, land + approvals +    │  ── Technologies            │
│  RoW, senior management role.     │  Solar · Wind · Hybrid ·    │
│  Employer named if permitted.     │  Pumped Storage             │
│                                   │  ── Scale                   │
│                                   │  Utility-scale              │
└─────────────────────────────────────────────────────────────────┘

┌─ 02 · DEPARTMENTAL FLUENCY ──────── 2-col list ─────────────────┐
│  Revenue Department      Section 109 conversion, RTC, mutation  │
│  KREDL                   Project registration, land clearance   │
│  KERC                    Tariff and approval filings            │
│  CEIG                    Electrical safety clearance            │
│  KPTCL / PGCIL           Evacuation, RoW, connectivity          │
│  Forest & Environment    Diversion, NOCs                        │
└─────────────────────────────────────────────────────────────────┘
```
**The most important block on the site.** It replaces the articles that will not be written and the "government contacts" claim that must not be published. It proves system knowledge by naming process and authority correctly — something a broker cannot produce. Two columns: authority left, actual process right, so it reads as a reference document rather than a claim.

```
┌─ 03 · DISTRICTS ────────────────────────────────────────────────┐
│  Districts of operation — chip list                             │
│  Ballari  Koppal  Gadag  Vijayapura  Chitradurga  Tumakuru ...  │
│  → Karnataka in detail                                          │
└─────────────────────────────────────────────────────────────────┘

┌─ 04 · CONFIDENTIALITY & ENGAGEMENT ───── narrow, bordered ──────┐
│  Confidentiality  — client identities and terms not disclosed   │
│  Engagement       — principal-led; no work subcontracted        │
│  [ CONFLICT POSITION — RESERVED SLOT, one line ]                │
└─────────────────────────────────────────────────────────────────┘

┌─ 05 · ENTITY DETAILS ─────────── 3-col, small type ─────────────┐
│  Registered name  │  Udyam / GSTIN  │  Registered address       │
└─────────────────────────────────────────────────────────────────┘

┌─ 06 · CTA BAND ─────────────────────────────────────────────────┐
```
**Decision on §05.** Registration details appear on-page, not only in the footer. On a proprietorship with no clients or projects, verifiable registration is the strongest hard evidence available, and buyers in this market check.

---

### 9.3 /services — Hub

```
┌─ HEADER ────────────────────────────────────────────────────────┐
│  Services                                                       │
│  End-to-end development-stage support, from site identification │
│  through to construction handover.                              │
└─────────────────────────────────────────────────────────────────┘

┌─ 01 · STAGE-GATE PROCESS ──────── full-width diagram ───────────┐
│  01 Site ID → 02 Tenure Diligence → 03 Aggregation →            │
│  04 Conversion → 05 Approvals → 06 RoW & Handover               │
│  Under each gate: deliverable + the service that owns it        │
└─────────────────────────────────────────────────────────────────┘

┌─ 02 · SERVICE LIST ────── 5 full-width rows, not cards ─────────┐
│  01 │ Land Aggregation          │ 3-line summary │  →           │
│  02 │ Government Liaison        │ 3-line summary │  →           │
│  03 │ Statutory Approvals       │ 3-line summary │  →           │
│  04 │ Transmission Right of Way │ 3-line summary │  →           │
│  05 │ Project Development Supt. │ 3-line summary │  →           │
└─────────────────────────────────────────────────────────────────┘

┌─ 03 · ENGAGEMENT NOTE ──────────────────────────────────────────┐
│  Mandates are principal-led. Services are taken individually    │
│  or as a full development-stage scope.                          │
└─────────────────────────────────────────────────────────────────┘
┌─ 04 · CTA BAND ─────────────────────────────────────────────────┐
```
**Decisions.** The hub leads with the process diagram, not the service list — sequence before menu. This is the only surviving location where methodology is demonstrated, so it earns first position. Full-width rows rather than a card grid: rows accommodate three lines of substance where cards force two, and the hub's job is qualification, not visual variety. §03 carries the "RE Project Facilitation" positioning that was denied its own page.

---

### 9.4 Service detail template (all 5)

Breadcrumb present. Structure identical across all five for scannability and build efficiency.

```
Home / Services / [Service]

┌─ HEADER ────────────────────────────────────────────────────────┐
│  [Service Name]                                                 │
│  One-sentence definition of scope.                              │
│  ──────────────                                                 │
│  Principal-led · Karnataka · Utility-scale     ← context strip  │
└─────────────────────────────────────────────────────────────────┘
```
**Decision — the context strip.** Deep entry from search or a forwarded link is the norm. This strip establishes who the firm is on every service page without assuming the homepage was seen. Three data points, one line, no repetition of the positioning paragraph.

```
┌─ 01 · WHAT THIS COVERS ──────── 2-col 65/35 ────────────────────┐
│  2–3 paragraphs of substance      │  ── Typical duration        │
│                                   │  ── Applies at stage        │
│                                   │  ── Related authorities     │
└─────────────────────────────────────────────────────────────────┘

┌─ 02 · PROCESS ─────────────── numbered vertical steps ──────────┐
│  01 ─ Step        Description + the authority involved          │
│  02 ─ Step        ...                                           │
│  03 ─ Step        ...                                           │
└─────────────────────────────────────────────────────────────────┘

┌─ 03 · DELIVERABLES ──────────────── checklist ──────────────────┐
│  What physically lands with the client at completion.           │
│  Land schedules · encumbrance summaries · approval trackers ·   │
│  RoW alignment maps · document sets                             │
└─────────────────────────────────────────────────────────────────┘
```
**Decision — §03 is mandatory on every service page.** Deliverables are the single clearest separator between a consultant and a broker. A broker describes an outcome; a consultant names an artefact. With no fee structure published, this is the only remaining professionalisation signal.

```
┌─ 04 · WHERE ────────────────────────────────────────────────────┐
│  Districts relevant to this service   → Karnataka in detail     │  [enforced link]
└─────────────────────────────────────────────────────────────────┘

┌─ 05 · WHO DELIVERS ─────────────────────────────────────────────┐
│  2 lines on the principal's experience in this specific area    │
│  → About the Principal                                          │  [enforced link]
└─────────────────────────────────────────────────────────────────┘

┌─ 06 · RELATED SERVICES ────────── 2 cards ──────────────────────┐
└─────────────────────────────────────────────────────────────────┘
┌─ 07 · CTA BAND ─────────────────────────────────────────────────┐
```

**Per-page content notes:**

| Page | Specific requirement |
|---|---|
| Land Aggregation | Flagship. Deepest §01 and §02. Must address fragmentation, RTC verification, mutation, encumbrance, holdout handling. |
| **Government Liaison** | **Departments and process only. Never relationships, access, contacts, influence, or "smooth clearance". Reframe as statutory coordination.** See §10.1. |
| Statutory Approvals | Structure §02 authority-by-authority: KREDL → KERC → CEIG → Forest → Pollution Control. |
| Transmission RoW | Highest search intent. Strongest metadata investment. Distinct buyer (transmission contractor / EPC) — CTA copy adjusted accordingly. |
| Project Development Support | Shortest. Positioned as extension of the client's internal team. Avoid overlap with the other four. |

---

### 9.5 /sectors — Single page

```
┌─ HEADER ────────────────────────────────────────────────────────┐
│  Sectors                                                        │
│  Utility-scale renewable energy across four technologies.       │
└─────────────────────────────────────────────────────────────────┘

┌─ 01 SOLAR ──────────── 2-col: land characteristics | approvals  │
┌─ 02 WIND ───────────── 2-col: land characteristics | approvals  │
┌─ 03 HYBRID ─────────── 2-col: land characteristics | approvals  │
┌─ 04 PUMPED STORAGE ─── 2-col: land characteristics | approvals  │
│                                                                 │
│  Each section: land footprint, tenure pattern, typical          │
│  district, approval variance. Cross-links to relevant services. │
└─────────────────────────────────────────────────────────────────┘
┌─ 05 · CTA BAND ─────────────────────────────────────────────────┐
```
**Decision.** Each section is framed by **land and approval implications**, not by technology explanation. Explaining what solar PV is would be insulting to the reader and would duplicate content available everywhere. The differentiating content is *how the land problem differs by technology* — which only an operator knows. Pumped Storage is the highest-value section: fewest competitors have handled it, and its land and clearance profile is materially different.

---

### 9.6 /karnataka

```
┌─ HEADER ────────────────────────────────────────────────────────┐
│  Karnataka                                                      │
│  Renewable energy development conditions, district by district. │
└─────────────────────────────────────────────────────────────────┘

┌─ 01 · STATE MAP ──────────────── full-bleed ────────────────────┐
│  Districts of operation, RE corridors, evacuation nodes         │
└─────────────────────────────────────────────────────────────────┘

┌─ 02 · DISTRICT TABLE ───────────────────────────────────────────┐
│  District │ Technology │ Tenure pattern │ Typical parcel size   │
│  Ballari  │ Solar+Wind │ ...            │ ...                   │
│  Koppal   │ Solar      │ ...            │ ...                   │
│  ...                                                            │
└─────────────────────────────────────────────────────────────────┘

┌─ 03 · LAND & TENURE CONDITIONS ────── prose + tables ───────────┐
│  Fragmentation patterns, RTC and revenue record realities,      │
│  common title conditions, conversion timelines by district      │
└─────────────────────────────────────────────────────────────────┘

┌─ 04 · APPROVAL LANDSCAPE ───────────────────────────────────────┐
│  Authorities, sequence, indicative durations                    │
└─────────────────────────────────────────────────────────────────┘

┌─ 05 · EVACUATION ───────────────────────────────────────────────┐
│  Substation and corridor constraints by region                  │
└─────────────────────────────────────────────────────────────────┘

┌─ 06 · SERVICES IN THIS GEOGRAPHY ──── 5 links ──────────────────┐  [enforced]
┌─ 07 · CTA BAND ─────────────────────────────────────────────────┐
```
**Decision.** This page does the work the deleted `/insights` section was meant to do — permanently, in one place, with no ongoing writing commitment. None of it is confidential; all of it is operational knowledge accumulated over 20 years. **If only one page is built properly, build this one.** It is the sole page on the site that demonstrates rather than asserts.

---

### 9.7 /contact

```
┌─ HEADER ────────────────────────────────────────────────────────┐
│  Contact                                                        │
└─────────────────────────────────────────────────────────────────┘

┌─ 2-col 45/55 ───────────────────────────────────────────────────┐
│  DIRECT                        │  ENQUIRY                       │
│  +91 XXXXX XXXXX  (tel:)       │  Name                          │
│  email@domain     (mailto:)    │  Organisation                  │
│                                │  Email                         │
│  Registered address            │  Phone                         │
│  [Full address]                │  District / location           │
│                                │  Capacity (MW)                 │
│  Udyam · GSTIN                 │  Requirement                   │
│                                │  [ Send → ]                    │
└─────────────────────────────────────────────────────────────────┘
```
**Decisions.** Phone first and to the left — the primary conversion channel for this buyer. The form asks **District** and **Capacity** as qualifying fields; they filter unqualified enquiries and simultaneously signal that the firm operates at utility scale. No map embed: third-party scripts, cookie implications, and layout shift, for zero value on a page nobody navigates to physically. Contact is a terminal node — no outbound links except the logo.

---

### 9.8 Mobile deltas

| Section | Change |
|---|---|
| Hero | Map moves below the headline, ~40% height. Headline never competes with a graphic at 380px. |
| Services grid | Single-column full-width rows with right chevron. Not cards — cards surrender ~40% of mobile width to padding. |
| Process stage-gate | Rotates to a vertical timeline. Horizontal scroll strips are missed by roughly half of users. |
| Karnataka table | District + technology only; technology as a tag. Drop remaining columns. Full table available on desktop. |
| Principal block | Monogram above text, centred. |
| Departmental fluency table | Stacks to authority-above-process pairs, hairline separated. |
| Sticky bottom bar | `Call` 50% / `Enquire` 50%, 56px, present on every page. |
| Header CTA | Collapses to icon. Bottom bar carries conversion. |
| Footer | Columns stack; registration details remain visible, not collapsed into an accordion. |

---

## 10. Content Rules

### 10.1 Prohibited language — sitewide

**Banned outright:**
- "Contacts in the government", "government connections", "strong relationships with officials"
- "Fast-track", "smooth clearance", "hassle-free approvals", "we get things done"
- Any phrasing implying influence over an outcome rather than competence in a process

**Rationale.** On a public Indian website these phrases read as access peddling. Three consequences: (a) large IPPs and any foreign-capital investor screen for FCPA / UK Bribery Act exposure and the phrasing can disqualify outright; (b) it positions the firm as a fixer rather than a consultant — fixers are paid once, consultants receive mandates; (c) it is unverifiable and unremarkable, since every land broker in Karnataka makes the same claim.

**Replacement register — procedural fluency:**

> Two decades working directly with Karnataka's revenue, energy and forest departments — including Section 109 land conversions, KREDL registration, KERC filings, CEIG clearances, and KPTCL/PGCIL right-of-way approvals.

Same underlying message. Zero compliance exposure. Specific enough that only an operator could have written it. **Naming the machinery correctly is the demonstration. "Contacts" is not.**

### 10.2 Title and role

- Role at Bolamudi: **Principal.**
- Career seniority described in prose: *"most recently in a senior management role responsible for land and approvals across Karnataka."*
- Rationale: "Senior Manager" describes the last rung of someone else's ladder and reads oddly on a proprietor's own site. "Principal" is standard consultancy usage, signals that the senior person does the work, and is not inflated.

### 10.3 Also banned

- Testimonials, anonymous or otherwise
- "Trusted by leading developers" or any unattributable claim
- Statistics counters (projects, MW, acres) — none are substantiable
- Client logo bars
- Stock photography of any kind, including AI-generated imagery
- Exclamation marks
- Superlatives without a source

---

## 11. Visual System

Locked, because with no photography the system carries the entire credibility load.

| Element | Specification | Rationale |
|---|---|---|
| **Typeface — headings** | One serif (engineering-report register) | Authority. Serif signals established/advisory. |
| **Typeface — body** | One neutral grotesk | Legibility, technical register. Two families maximum. |
| **Type scale** | 64 / 40 / 24 / 16 | Large scale with real whitespace is how a photo-less page is filled without reading as empty. |
| **Colour** | Deep navy or graphite + off-white + one restrained accent | No gradients, no glassmorphism, no glow. |
| **Rules** | 1px hairlines as the primary structural device | Technical-drawing language. This carries the "engineering firm" read in place of imagery. The single most important visual decision on the project. |
| **Corners** | 0–2px radius | Rounded corners are the strongest startup signal available. |
| **Shadows** | None | Borders only. |
| **Motion** | Framer Motion: fade + 8px rise, 300ms, `once: true` | Nothing parallaxes, nothing bounces, nothing loops. Motion is punctuation, not decoration. |
| **Grid** | 12-column, 1280px max, generous gutters | |
| **Imagery** | Maps, diagrams, tables, monogram only | See C3. |

---

## 12. Technical Requirements

| Item | Specification |
|---|---|
| Rendering | SSG for all 12 pages. Content is stable; performance is a credibility signal. |
| Fonts | `next/font`, self-hosted, zero layout shift |
| Metadata | Next.js Metadata API, per-page title / description / OG |
| Structured data | `Organization`, `LocalBusiness`, `Service` (×5), `BreadcrumbList` |
| Sitemap | XML, all 12 pages, submitted |
| Analytics | Plausible or Fathom — avoids the cookie consent banner entirely. At this traffic volume GA4 adds no usable capability and costs a consent modal in the first decisive seconds. |
| Targets | LCP < 2.0s · INP < 200ms · CLS < 0.1 · Lighthouse ≥ 95 |
| Accessibility | WCAG 2.2 AA |
| OG images | Per-page, correctly rendering in WhatsApp and email previews. In a referral business this is the first impression roughly half the time. |

---

## 13. Future Scalability

The structure absorbs all foreseeable additions without re-architecture. **Nav ceiling stays at six items permanently; nothing new goes top-level.**

| Phase | Addition | Slots into | Requires |
|---|---|---|---|
| 2 | Articles / insights | `/insights` + `/insights/[slug]` | Content commitment. Route reserved, not built. |
| 2 | Engagement models and fee structure | `/approach` reinstated as L1 | Commercial model decision |
| 2 | Individual sector pages | `/sectors/[sector]` — split when each carries real content | Content depth |
| 3 | District pages | `/karnataka/[district]` — breadcrumb pattern already defined | Content depth |
| 3 | Case studies (once company-owned) | `/experience/[slug]` | Non-NDA project history |
| 3 | Service × sector intersections | `/services/[service]/[sector]` | Only when a service page ranks and needs to spawn |
| 4 | Team, careers | `/about/team`, `/about/careers` | 5+ staff |
| 4 | BESS, green hydrogen | Sections on `/sectors` | |
| 4 | Other states | `/karnataka` → `/regions/karnataka`, 301 redirect | **The only true structural change.** Plan the redirect now; do not build for it now. |

---

## 14. Build Sequence

Ordered by load-bearing importance, not by page order.

1. `/about` — carries the site
2. `/karnataka` — only demonstrable asset
3. `/services/land-aggregation` — flagship commercial page
4. Home
5. `/services` hub + stage-gate diagram
6. Remaining 4 service pages
7. `/sectors`
8. `/contact`
9. `/privacy-policy`, `/terms`

---

## 15. Unresolved Items

| # | Item | Blocks | Status |
|---|---|---|---|
| 1 | **Conflict-of-interest position** — one line, no numbers required | `/about` §04, `/services/land-aggregation` credibility | **OPEN.** Slot reserved. Largest remaining gap. |
| 2 | Can the previous employer be named? Check the **employment agreement**, not the project NDAs — different documents. | `/about` §01. Largest single credibility variable remaining. | OPEN |
| 3 | Engagement model *structure* (retainer / success-linked / hybrid) — no figures required | Reinstatement of `/approach`; removes the largest disqualifier | DECLINED — revisit |
| 4 | Content commitment | `/insights` | DECLINED |
| 5 | Registered address, Udyam number, GSTIN | Footer, `/about` §05, LocalBusiness schema | Required before build |
| 6 | Confirmed district list with technology mapping | Home §05, `/about` §03, `/karnataka` §02 | Required before content |

---

## 16. Standing Limitation

Every reference firm named in the brief — Black & Veatch, AECOM, Arup, WSP, Jacobs, Siemens Energy — earns credibility through **published evidence**: named projects, technical papers, identified clients. This project has opted out of all three categories.

The IA and design can make the firm look established. Neither can make it look **proven**, and a buyer reading closely will register the difference.

That is an acceptable trade for a referral-validation site, and the structure above extracts the maximum available value from the assets that exist. It should not be mistaken for a business development asset. Inbound demand will come from the principal's network and LinkedIn presence; this website is the landing surface for both.

---

*End of document.*
