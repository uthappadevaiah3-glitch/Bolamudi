# Bolamudi Enterprise — Home Page Design Specification

**Version 1.0 · Creative direction, UX, UI, content, SEO, accessibility, frontend architecture**
Stack: Next.js (App Router) · TypeScript · Tailwind · shadcn/ui · Framer Motion

---

## 0. Before the design: two strategic problems you must resolve

I was asked not to assume anything and to be honest. So this comes first.

### 0.1 You chose "institutional / faceless" with zero proof assets. That combination does not work.

Look at what the reference firms actually put on their homepages. Black & Veatch, AECOM, Arup, WSP, Jacobs — 80–90% of their homepage real estate is **evidence**: project cards with client names, MW and km figures, office counts, named leadership, awards, ESG reports. The institutional tone is *earned by* the evidence. It is not a visual style you can apply on top of nothing.

Strip the evidence out and what remains is adjectives — "trusted partner", "excellence in execution", "end-to-end solutions". A BD head at ReNew, Ayana or Tata Power has read that sentence four hundred times. On a faceless site with no numbers, no logos and no photos, it reads as a shell company. You will have engineered the exact opposite of trust.

**Second problem, specific to your business.** Land aggregation and government liaison are relationship businesses. The buyer is not buying a corporate entity. They are buying access to a person who knows which Tahsildar's office moves fast, which villages have clean revenue records, which KPTCL substation has evacuation headroom. Anonymity destroys the only thing you are selling.

### 0.2 Recommendation — "institutional" is a visual register, not anonymity

Hold the line on everything that makes a site look establishment:

| Keep from institutional | Reject from startup |
| --- | --- |
| Restrained palette, two accent colours max | Purple/blue gradients, glassmorphism |
| Serif headlines, generous measure | Oversized rounded sans, emoji |
| 12-column grid, hard alignment, hairline rules | Floating blobs, tilted cards |
| Formal, specific copy | "Let's build the future together ✨" |
| Slow, small motion (150–400ms, ≤24px travel) | Parallax scenes, scroll-jacking, spinning 3D |
| Real documents and process artefacts | Illustrated cartoon characters |

But keep a **Leadership** block with the promoter named, photographed, and 20 years of specifics. Arup names its board. Jacobs names its CEO. Naming a leader *is* institutional behaviour. Facelessness is what shell companies do.

**If you overrule me and stay fully anonymous**, the spec still works — Section 11 (Leadership) becomes "Our Practice" and carries process credentials instead of a person. I have marked that fallback inline. I think it is the weaker site by a large margin, and I want that on record.

### 0.3 Your proof substitute: convert expertise into artefacts

You have no MW numbers yet. You do have 20 years of knowledge nobody else has bothered to publish. Publish it. Concretely:

1. **Karnataka statutory approvals matrix** — every clearance a utility-scale RE project needs in Karnataka, with issuing authority and indicative timeline. Nobody has this on a clean web page. It is the single highest-leverage asset on your site.
2. **District coverage map** — the districts you have actually worked in, with terrain/land-tenure notes.
3. **Land aggregation methodology** — your due-diligence checklist, expressed as a named process.
4. **Transmission & evacuation primer** — RoW, corridor constraints, CTU/STU interface.

Specific knowledge is the only credible substitute for a track record. Vague claims are not. Sections 8 and 9 of this design are built entirely around this idea.

### 0.4 Blind spots I want you to look at

- **Your primary CTA assumes inbound demand.** New entity, no SEO authority, no logos. Realistically your first ten deals come from the founder's phone. The website's actual job in year one is to *survive due diligence after the meeting*, not to generate leads. Design for the person who was given your card yesterday and is checking whether you are real. That changes priorities: credentials, specificity and contact clarity beat conversion-rate optimisation.
- **NDAs.** You will be tempted to write "worked with leading IPPs". Unverifiable claims are worse than silence with this audience. Use anonymised but *specific* framing instead: "1,200 acres aggregated across 3 districts for a 500 MW solar park" is credible; "trusted by India's top developers" is not.
- **The logo.** The script "Bolamudi" wordmark is decorative and will be hard to read at 32px in a sticky header. Budget for a horizontal lockup and a simplified monogram. Flagged again in Section 3.
- **English-only.** Land owners and district officials are a real secondary audience. Kannada is worth considering for at least the contact page. Out of scope for this document; do not forget it.

---

## 1. Positioning and messaging platform

Everything below derives from this. If you disagree with this, stop and fix it before looking at layout.

**Category:** Renewable energy project development support — Karnataka.

**Positioning statement (internal, not for the site):**
> For renewable energy developers, IPPs and infrastructure investors building in Karnataka, Bolamudi Enterprise de-risks the two stages that kill projects — land and approvals — through two decades of on-the-ground execution across the state's districts, revenue offices and utilities.

**The single idea the homepage must land:** *Land and statutory approvals are where Karnataka RE projects die. We are the people who have already solved that, district by district.*

**Message hierarchy (top to bottom of page):**

1. What we do and where — instantly, without a scroll.
2. Why it is hard — the bottleneck, named precisely.
3. How we solve it — services and process.
4. Proof that we know the terrain — geography and statutory artefacts.
5. Who we do it for — audience validation.
6. Who we are — leadership credibility.
7. How to start — conversion.

**Tone of voice:** Declarative. Specific. No superlatives. Present tense. Never "we strive to" or "we aim to". Use nouns that only an insider uses — *revenue survey number, mutation, RTC/Pahani, 79A/79B, Section 109, KERC, KPTCL, CTU, LOA, RoW compensation, conversion certificate*. This vocabulary is itself a credential; a marketing agency writing this site would not produce those words. Use them sparingly enough that an investment analyst still follows.

---

## 2. Design system foundations

### 2.1 Colour

Derived from the logo. The logo has one problem: gold-on-white at small sizes fails contrast. The system below fixes that by demoting gold to a non-text accent.

| Token | Hex | Role | Notes |
| --- | --- | --- | --- |
| `forest-900` | `#0B1F19` | Darkest surfaces, footer | |
| `forest-800` | `#14342B` | **Primary brand.** Dark sections, primary button fill | Logo green |
| `forest-700` | `#1B4D3E` | Hover state on primary | |
| `forest-100` | `#E8EFEA` | Tinted section backgrounds | |
| `gold-600` | `#856318` | Gold **text** and icons on light backgrounds | 5.53:1 white · 5.16:1 surface-1 · 4.73:1 forest-100 — passes AA everywhere |
| `gold-500` | `#C39A3E` | Rules, dividers, decorative accents only. **Never text, never a focus ring** | 2.62:1 on white — decorative only |
| `gold-focus` | `#A8791F` | Focus indicator, all backgrounds | 3.87:1 white · 3.61:1 surface-1 · 3.48:1 forest-800 — clears the 3:1 non-text threshold on every surface |
| `gold-200` | `#E8D9A8` | Gold text/accents on `forest-800` / `forest-900` | 9.59:1 on forest-800 — passes AAA |
| `ink-900` | `#16181A` | Body text on light | |
| `ink-600` | `#5A5E5C` | Secondary text | 6.58:1 white · 6.13:1 surface-1 — passes AA |
| `ink-400` | `#6E736F` | Captions, metadata | 4.83:1 white · 4.50:1 surface-1 — passes AA at any size |

**Every ratio above is measured, not estimated.** Three values changed during verification and are worth knowing about, because they are the exact mistakes a gold-and-green brand invites:

- The obvious gold (`#9A7420`) computes to 4.29:1 on white — it *looks* dark enough and it is not. Darkened to `#856318`.
- The logo gold `#C39A3E` is 2.62:1 on white. It cannot be text, and it cannot be a focus ring either, since focus indicators need 3:1.
- No single gold clears 3:1 against both white and `forest-800`, so the focus ring gets its own token (`#A8791F`) that clears it on both.
- The conventional "muted grey" `#8C918E` is 3.2:1 — a very common AA failure. Darkened to `#6E736F`.

**On dark sections:** white text is 13.5:1 on `forest-800` and 17.15:1 on `forest-900`; `rgba(255,255,255,0.78)` body text is 8.79:1 on forest-800; `rgba(255,255,255,0.6)` footer text is 6.82:1 on forest-900. All pass comfortably — do not drop below 0.6 opacity.
| `line` | `#E2E4E0` | Hairline rules, card borders | |
| `surface-1` | `#F7F7F4` | Alternate section background | Warm off-white, not grey |
| `canvas` | `#FFFFFF` | Default page | |

**Rules.**
- Gold is a *rule and accent* colour. It draws the eye to structure, never to blocks of text. Gold used as fill on a button will look like a payday-loan site.
- Section backgrounds alternate `canvas → surface-1 → canvas → forest-800`. Never two dark sections in a row; the page loses rhythm and feels heavy.
- Maximum three colours visible in any single viewport, excluding photography.

**Why:** the reference firms all run one dominant brand colour, one accent, and a large neutral range. Startups run five. Restricting the palette is the cheapest, most reliable way to read as established.

### 2.2 Typography

| Role | Family | Why |
| --- | --- | --- |
| Headings | **Source Serif 4** (variable) | A serif headline is the strongest single "not a startup" signal available. Startups run geometric sans almost universally. Source Serif 4 is a Charter descendant — legal/academic lineage, reads as authoritative, and its variable axis gives 400–700 in one file. It also harmonises with the serif "ENTERPRISE" in the logo. |
| Body / UI | **Inter** (variable) | Neutral, exceptional screen legibility at 15–18px, excellent tabular figures for data blocks, huge language coverage. It disappears, which is the job. |
| Data / eyebrows | **IBM Plex Mono**, uppercase, letterspaced | Monospace on section labels and figures signals engineering without a single illustration. Used at 12px only, in `ink-600` or `gold-600`. |

Load as `next/font/google` with `display: swap` and subset `latin`. Three families is the ceiling; total variable-font payload ≈ 130 KB, acceptable. Self-host via `next/font` so no third-party request and no CLS.

**Type scale** — 1.25 modular ratio, `clamp()` for fluidity:

| Token | Desktop | Mobile | Line height | Tracking | Use |
| --- | --- | --- | --- | --- | --- |
| `display` | 64px | 36px | 1.08 | −0.02em | H1 only |
| `h2` | 44px | 30px | 1.15 | −0.015em | Section headings |
| `h3` | 28px | 22px | 1.25 | −0.01em | Card titles, sub-sections |
| `h4` | 20px | 18px | 1.35 | 0 | Small card titles |
| `lead` | 20px | 17px | 1.55 | 0 | Hero sub-copy, section intros |
| `body` | 17px | 16px | 1.65 | 0 | Default paragraph |
| `small` | 15px | 14px | 1.6 | 0 | Card body, captions |
| `eyebrow` | 12px | 12px | 1.4 | 0.1em | Mono, uppercase section labels |

**Rules.**
- Negative tracking on large serif is mandatory; default spacing looks amateurish above 32px.
- Body measure capped at **68 characters** (`max-w-[68ch]`). Full-bleed 1400px paragraphs are the most common tell of a template site.
- Headline weight 600, never 700 — 700 Source Serif is heavy and shouty at display sizes.
- Sentence case for all headings and buttons. Title Case reads dated; ALL CAPS reserved for the 12px mono eyebrow only.

### 2.3 Grid and spacing

- Base unit **8px**. Every margin, padding and gap is a multiple. No 15px, no 22px.
- Outer shell max `1440px`. Content container max `1200px`, centred.
- **12 columns**, gutter 32px desktop / 24px tablet / 16px mobile. Page margin 64px desktop, 40px tablet, 20px mobile.
- Breakpoints: `sm 640` · `md 768` · `lg 1024` · `xl 1280` · `2xl 1536`.

**Vertical rhythm — section padding (top/bottom):**

| Section weight | ≥1280px | 768–1279px | <768px |
| --- | --- | --- | --- |
| Hero | 120 / 120 | 96 / 96 | 72 / 64 |
| Standard | 128 | 96 | 72 |
| Dense (map, matrix) | 112 | 88 | 64 |
| Compact (strip, CTA band) | 72 | 64 | 56 |

Inside a section: eyebrow → 16px → H2 → 24px → intro paragraph → 64px → content. Card internal padding 32px desktop, 24px mobile.

**Why so much whitespace:** perceived seniority correlates almost linearly with vertical breathing room. Cramped sections read as cheap. 128px between sections is not wasteful; it is the price of looking like Arup.

### 2.4 Elevation, borders, corners

- **Borders over shadows.** `1px solid line` on cards. Institutional sites are flat and ruled; shadow-heavy cards read consumer-SaaS.
- Corner radius **4px** on cards and inputs, **2px** on buttons, **0** on section dividers and image containers. Large radii (12–24px) are a startup signal — avoid.
- Exactly one elevation level exists: a `0 1px 2px rgba(11,31,25,0.06)` on hover for interactive cards. Nothing else lifts.

### 2.5 Iconography

**Lucide React** (ships with shadcn/ui), 1.5px stroke, 24px default, `currentColor`.

Do **not** use the coloured illustrated icons from the logo sheet inside the site body. They are branding artwork, not UI icons; at 24px they turn to mud and their gold fails contrast. Keep them for the brand sheet and possibly the footer.

Icon-per-service mapping (Lucide names): `MapPinned` land aggregation · `Landmark` government liaison · `FileCheck2` statutory approvals · `SunMedium` RE facilitation · `Cable` transmission RoW · `ClipboardCheck` project development support.

Rules: icons are `gold-600` on light, `gold-200` on dark, `1.5px` stroke, never filled, never in a coloured circle chip (chips are a startup convention). Always `aria-hidden="true"` — the adjacent text label carries the meaning.

### 2.6 Photography and imagery direction

This is where the site will be won or lost, and where you currently have nothing.

**Direction:** documentary, wide, low-saturation, human-scale. Karnataka landscape must be recognisable — red laterite soil, dry deciduous scrub, black cotton soil, Deccan plateau horizons. **Not** the generic blue-sky-panel-array stock photo that every RE company in the world uses.

**Shot list to commission (one day, one photographer, ~₹25–40k — do this before launch):**

| # | Shot | Where used | Aspect |
| --- | --- | --- | --- |
| 1 | Wide land parcel at low sun, survey marker in foreground, hills behind | Hero background | 16:9, 2400px |
| 2 | Hands over a cadastral/village map on a vehicle bonnet | Bottleneck section | 4:3 |
| 3 | Transmission line receding across scrubland | Transmission service card / RoW | 3:2 |
| 4 | Government office corridor or record room, shot respectfully, no faces | Approvals section | 3:2 |
| 5 | Operating solar or wind site at distance, land in foreground | Services band | 21:9 |
| 6 | Founder portrait — outdoors on site, mid-grey background, natural light, no studio white | Leadership | 4:5 |

**Founder portrait is non-negotiable if you keep any human credibility on the page.** A stock businessman photo is instantly detectable and does more damage than no photo.

**Interim (pre-shoot) fallback:** run hero as `forest-800` with a subtle contour/topographic line pattern at 6% `gold-500` opacity, plus the map artefact from Section 8. A restrained typographic hero with no photo beats a bad stock photo. It does **not** beat a good real photo — book the shoot.

**Technical:** `next/image`, AVIF+WebP, hero `priority` + `fetchPriority="high"`, everything else lazy. Explicit `width`/`height` on every image (CLS = 0). Hero served at 1920/1280/750 widths. Every image gets descriptive `alt` — decorative textures get `alt=""`.

### 2.7 Motion principles

Motion is the fastest way to look like a startup. Constraints:

- **Duration** 200–400ms. Nothing longer except the hero's one-time entrance (600ms).
- **Easing** `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out-quint). No bounce, no spring overshoot, no elastic.
- **Travel** ≤24px. Elements fade and rise slightly; they never fly, rotate, scale past 1.02, or blur in.
- **Trigger once.** `whileInView` with `viewport={{ once: true, amount: 0.25 }}`. Re-animating on every scroll pass is a consumer pattern and becomes irritating on a long page.
- **Stagger** 60–80ms between siblings, capped at 6 children. Beyond that the last card arrives late enough to feel broken.
- **Forbidden:** scroll-jacking, parallax layers, horizontal scroll sections, counting-number animations (you have no numbers — and even with numbers they undermine gravitas), typewriter text, marquee logo belts, cursor followers, page-transition curtains.
- **`prefers-reduced-motion: reduce` → all transforms become opacity-only at 150ms, or are removed entirely.** Not optional. Implement as a single `useReducedMotion()` guard in a shared `<Reveal>` wrapper so it cannot be forgotten per-component.

**Framer Motion architecture:** one shared `<Reveal>` component (fade + `y: 16 → 0`) and one `<RevealGroup>` (stagger container). Every animation on the site goes through those two. This prevents drift and keeps the JS payload small. Import from `framer-motion` inside client components only; keep section shells as Server Components.

---

## 3. Global chrome

### 3.1 Header — sticky, two-state

**Height:** 88px at rest, **64px after 80px of scroll**, transition 250ms. Background at rest: transparent over hero (hero is dark, so nav text is white). After scroll: `canvas` with `1px solid line` bottom border and the 1px shadow. This transition is the only "clever" chrome behaviour on the site, and it is a convention institutional firms use, so it does not read as startup.

**Left:** horizontal logo lockup, 40px tall at rest → 32px scrolled.

> **Logo blocker.** The supplied mark is a vertical stack (emblem over script wordmark over "ENTERPRISE" over five icons). It cannot go in a 64px header. You need a **horizontal lockup** — emblem left, "Bolamudi" + "ENTERPRISE" stacked right — and a **monogram** (the B emblem alone) for the mobile header and favicon. Also test the script wordmark at 32px height; if the "B" flourish loses definition, it needs redrawing with thicker hairlines. Commission this before build.

**Centre/right nav (desktop ≥1024px):**

`Services ▾` · `Approach` · `Karnataka` · `Insights` · `About` · `Contact` — then the CTA button.

`Services` opens a **mega-menu panel**, not a dropdown list: full-width, `canvas` background, 32px padding, two columns of six services each with a one-line description, plus a right-hand rail containing a single promoted card ("Karnataka statutory approvals guide →"). Opens on hover (150ms delay in, 300ms out) *and* on click/Enter; closes on `Esc`, on outside click, on focus leaving. Full keyboard traversal with arrow keys. This is a shadcn/ui `NavigationMenu` — use it rather than rolling your own, because it already implements the WAI-ARIA menu pattern correctly.

**Why a mega-menu:** six services in a flat dropdown looks thin. A panel with descriptions instantly communicates depth of practice, which is exactly what a firm with no track record needs. It also front-loads keywords for crawlers.

**Header CTA:** `Request consultation` — primary button, `forest-800` fill, white text, 2px radius, 44px tall, 20px horizontal padding. Present in **every** state, including scrolled and mobile.

**Mobile (<1024px):** monogram left, hamburger right (44×44 tap target). Opens a **full-screen sheet** (shadcn `Sheet`), not a slide-in half panel: `forest-800` background, nav items at 22px serif with 24px vertical spacing, services expandable as an accordion, phone number and email as tappable links at the bottom above a full-width `Request consultation` button. Body scroll locked; focus trapped; `Esc` and swipe-right both close; first focusable element receives focus on open, and focus returns to the hamburger on close.

**Skip link:** `Skip to main content`, visually hidden until focused, first element in DOM, jumps to `#main`.

### 3.2 Footer

`forest-900` background, four zones, 96px top padding, 40px bottom.

- **Zone A (col 1–4):** logo (white/gold-200 version), one-sentence descriptor, registered address, GSTIN/CIN if available. Registration numbers are a disproportionately strong legitimacy signal for a new entity — include them.
- **Zone B (col 5–7):** Services — all six as links.
- **Zone C (col 8–10):** Company — About, Approach, Karnataka coverage, Insights, Careers, Contact.
- **Zone D (col 11–12):** Get in touch — phone (`tel:` link), email (`mailto:`), LinkedIn icon link, and a secondary-style `Request consultation` button.
- **Bottom bar:** hairline `rgba(255,255,255,0.12)` rule, then `© 2026 Bolamudi Enterprise. All rights reserved.` left, `Privacy policy · Terms · Disclaimer` right. 13px, `rgba(255,255,255,0.6)` — verify this hits 4.5:1 against `forest-900`; if not, lift to 0.7.

Mobile: zones stack; B and C become accordions to avoid a 900px-tall footer.

---

## 4. Home page section hierarchy

| # | Section | Job to be done | Background | Desktop height (approx) |
| --- | --- | --- | --- | --- |
| 1 | Hero | Say what we do, where, and for whom in under 3 seconds | `forest-800` + photo | 100vh capped at 820px |
| 2 | Positioning strip | Convert the hero claim into a scannable capability set | `canvas` | 200px |
| 3 | The bottleneck | Name the pain precisely enough that the reader thinks "they get it" | `surface-1` | 620px |
| 4 | Services | Show breadth of practice; route to service pages | `canvas` | 900px |
| 5 | Development lifecycle | Show method — the strongest available substitute for a track record | `forest-800` | 640px |
| 6 | Karnataka coverage | Prove geographic specificity | `canvas` | 720px |
| 7 | Statutory approvals | The credential artefact. Depth no competitor publishes | `surface-1` | 680px |
| 8 | Who we work with | Audience validation — "this is for me" | `canvas` | 520px |
| 9 | Why Bolamudi | Differentiators, honestly framed | `surface-1` | 560px |
| 10 | Leadership | The actual credibility anchor | `canvas` | 620px |
| 11 | Governance & conduct | De-risk the liaison question before they ask it | `forest-800` | 420px |
| 12 | Insights | SEO surface + demonstrates currency | `canvas` | 560px |
| 13 | FAQ | Long-tail SEO + objection handling | `surface-1` | 640px |
| 14 | CTA + inquiry form | Convert | `forest-900` | 720px |
| 15 | Footer | Navigate, legitimise, contact | `forest-900` | 480px |

**Total scroll ≈ 9,600px desktop.** That is long. It is *deliberately* long — with no logos and no numbers, depth of substance is the only lever you have, and a short page would be a short page of adjectives. But mitigate:

- Sections 12 (Insights) and 13 (FAQ) can be **deferred to phase 2** if you cannot produce three genuine articles at launch. Two thin placeholder posts are worse than no Insights section.
- Add a **section-progress rail** (Section 4.16) so length feels navigable rather than endless.
- Every section must survive the test: *does this contain information a competent competitor could not have written?* If not, cut it.

---

## 5. Section-by-section specification

Notation: **P** = purpose, **C** = content/microcopy, **L** = layout, **I** = interaction, **M** = motion, **A** = accessibility, **R** = responsive.

---

### 5.1 Hero

**P.** Answer three questions before any scroll: *what is this company, where does it operate, is it serious?* Nothing else. No secondary messaging, no feature list.

**L.** Full-bleed. Background photo #1 at 100% width, overlaid with a left-to-right gradient `forest-900 92% → forest-900 45%` plus a global 20% `forest-900` wash so text contrast holds regardless of crop. Content sits in columns 1–7 (58% width), vertically centred, bottom-weighted. Columns 8–12 stay empty so the photograph reads — resist the urge to fill it.

Height `min(100vh, 820px)` with `min-height: 640px`. Capping at 820px matters: on a 27" monitor an uncapped 100vh hero is a 1300px wall of nothing.

**C.**

- Eyebrow (mono, 12px, `gold-200`): `KARNATAKA · RENEWABLE ENERGY PROJECT DEVELOPMENT`
- H1 (Source Serif 600, `display`, white):
  **`Land and approvals, resolved before they become the critical path.`**
- Lead (20px, `rgba(255,255,255,0.82)`, max 58ch):
  `Bolamudi Enterprise secures land, statutory clearances and transmission right of way for utility-scale solar, wind, hybrid and pumped storage projects across Karnataka — led by two decades of on-ground execution.`
- Primary CTA: `Request a consultation` → scrolls to `#contact`
- Secondary CTA: `How we work` (ghost, white 1px border) → scrolls to `#approach`
- Bottom-left micro-strip, mono 12px, `rgba(255,255,255,0.7)`, gold hairline above: `LAND AGGREGATION · GOVERNMENT LIAISON · STATUTORY APPROVALS · TRANSMISSION ROW`

**Why this H1.** It states the *outcome the buyer cares about* (schedule risk) rather than the service you sell. "Critical path" is project-management vocabulary — it signals you think like a developer, not a vendor. It avoids every dead phrase: no "empowering", no "partner of choice", no "end-to-end". It is 11 words and readable at 36px on a phone.

**Why the second sentence carries the founder claim without naming him.** "Led by two decades of on-ground execution" is defensible, specific, and preserves your institutional voice while still putting experience in the first viewport. This is the compromise between your stated preference and my recommendation.

**I.** Both CTAs use smooth scroll (`scroll-behavior: smooth` respecting reduced-motion) with `scroll-margin-top: 96px` on targets so the sticky header does not cover the heading. Primary button hover: `forest-700`, 150ms. No scroll-down chevron animation — it is a consumer pattern and the fold is obviously scrollable.

**M.** One-time entrance, no scroll trigger: eyebrow → H1 → lead → CTAs → micro-strip, each `opacity 0→1, y 20→0`, 600ms, 90ms stagger. Background image fades in over 800ms from `opacity 0.85 → 1` with `scale 1.03 → 1`. **Total under 1.4s.** Reduced-motion: everything renders immediately at final position.

**A.** H1 is the page's only `<h1>`. Contrast: white on the gradient must be ≥7:1 at every point over the photo — test the *lightest* pixel of the chosen image, not the average. Buttons are real `<button>`/`<a>` elements, 44px minimum height. Focus ring: 2px `gold-focus` (#A8791F) at 2px offset — visible against both the dark hero and light sections.

**R.**
- ≥1280: as above.
- 1024–1279: content columns 1–8, H1 52px.
- 768–1023: content full width, H1 40px, photo overlay strengthens to 65% because there is less clear space.
- <768: **height becomes `auto` with 72px vertical padding — never `100vh`** (mobile browser chrome makes 100vh unreliable and it pushes the CTA below the fold). H1 36px. CTAs stack full-width with 12px gap. Micro-strip becomes two lines, or drops entirely below 380px.

---

### 5.2 Positioning strip

**P.** Immediately after the single-idea hero, give the scanner the capability set. Many B2B visitors never read a paragraph; this strip must work on its own.

**L.** `canvas`, 72px padding. Four equal columns divided by 1px vertical `line` rules (the rules matter — they are what makes it read as a technical spec sheet rather than a feature grid). Each column: 24px Lucide icon in `gold-600`, 16px gap, `h4` label, 8px gap, one line of `small` in `ink-600`.

**C.**

| Icon | Label | Sub-line |
| --- | --- | --- |
| `MapPinned` | Land aggregation | Parcel identification to registered conveyance |
| `Landmark` | Government liaison | District, state and utility interface |
| `FileCheck2` | Statutory approvals | Consent to establish through commissioning |
| `Cable` | Transmission RoW | Corridor alignment and landowner settlement |

**Why only four when you have six services.** Four fits one desktop row at a readable size and covers the value proposition. Six creates a cramped row or an awkward 3×2. The remaining two appear in full in Section 5.4.

**M.** Fade + `y:12` on view, 70ms stagger, once.
**A.** Renders as a `<ul>`; icons `aria-hidden`; the divider rules are CSS borders, not DOM elements.
**R.** ≥1024: 4 columns. 768–1023: 2×2 with horizontal rules between rows. <768: 2×2 at 15px label size — do **not** stack to a single column, that produces a 4-screen-tall strip for four words each.

---

### 5.3 The bottleneck

**P.** Demonstrate that you understand the client's problem more precisely than they expect. In consultancy sales this section does more work than the services list — it is where the reader decides you are an insider.

**L.** `surface-1`. Two columns, 7/5 split. Left: eyebrow, H2, two paragraphs, then three numbered "failure mode" rows. Right: photograph #2 (hands over a cadastral map) in a `4:3` container, radius 0, with a 12px `gold-500` left rule running its full height.

**C.**

- Eyebrow: `THE DEVELOPMENT BOTTLENECK`
- H2: **`Projects are rarely lost on engineering.`**
- Body:
  `Module supply, EPC capability and financing are competitive markets with known solutions. Land and statutory clearance are not. In Karnataka they are local, sequential, and unforgiving of assumptions made from a head office in Bengaluru, Mumbai or Delhi.`
  `A single unresolved tenancy claim, an unconverted survey number, or a right of way alignment that crosses one uncooperative holding can move commissioning by two quarters. The cost is not the land. The cost is the schedule.`
- Three failure modes, mono-numbered `01 / 02 / 03`, each `h4` + one line of `small`:
  - `01 · Title that does not survive diligence` — `Fragmented holdings, unrecorded inheritance, tenancy entries and land-ceiling restrictions surface late, after commercial terms are agreed.`
  - `02 · Approvals treated as parallel when they are sequential` — `Clearances have dependency chains. Applying in the wrong order can cost an entire season.`
  - `03 · Right of way negotiated after the route is fixed` — `Corridor decisions taken on a map without landowner sequencing create hold-outs with maximum leverage.`

**Why this works.** It is falsifiable, specific, and slightly unflattering to the reader's own process — which is exactly what makes an expert credible. It also contains zero claims about Bolamudi, so nothing here can be challenged.

**M.** Left column fades/rises as a group; failure-mode rows stagger 80ms; image fades with `scale 1.02 → 1` over 500ms.
**A.** Failure modes are an `<ol>`. The `01/02/03` markers are `aria-hidden` decorative spans, since the ordered list already conveys sequence.
**R.** <1024: image moves above the text, `16:9` crop, full-bleed to page margins. Failure modes become full-width stacked rows with a 1px top rule each.

---

### 5.4 Services

**P.** Show the full practice, route traffic to six service pages (each of which is an SEO landing page), and make the firm feel larger than it is through breadth and specificity of scope.

**L.** `canvas`, 128px padding. Section header centred, max 640px. Then a **3×2 grid** of cards, 32px gap.

**Card anatomy** (this is the site's most reused component — specify it once, hard):

```
┌────────────────────────────────┐
│  [icon 24px gold-600]          │  32px padding all round
│  ↕ 20px                        │  bg: canvas
│  Land aggregation        (h3)  │  border: 1px line
│  ↕ 12px                        │  radius: 4px
│  Two–three lines describing    │  min-height: 260px (equal via grid)
│  the scope in the client's     │
│  vocabulary.            (small)│
│  ↕ auto (pushes to bottom)     │
│  ─────────────── 1px line ──── │
│  ↕ 16px                        │
│  Explore service        →      │  gold-600, 14px, mono-adjacent
└────────────────────────────────┘
```

**Card interaction.** The whole card is the click target (`<a>` wrapping content — one link per card, not a nested link inside a clickable div, which breaks keyboard nav and screen readers). Hover/focus-visible, 200ms: border → `gold-500`; background → `#FCFBF7`; arrow translates `x: 0 → 4px`; the 1px divider rule animates from `line` to `gold-500` left-to-right via `scaleX` on a pseudo-element. Card does **not** lift, scale, or shadow. Restraint here is the whole point.

**C.** Six cards:

1. **Land aggregation** — `Parcel identification, ownership verification, revenue-record diligence, landowner negotiation, aggregation across fragmented holdings, and registered conveyance or lease.`
2. **Government liaison** — `Sustained interface with district administration, revenue and survey departments, state nodal agencies, KREDL, KPTCL and pollution control boards.`
3. **Statutory approvals** — `Land conversion, NA permissions, consent to establish and operate, forest and environmental referrals, local body NOCs, and approval sequencing.`
4. **Transmission right of way** — `Corridor assessment, route optimisation against land holdings, RoW negotiation, crop and structure compensation, and access arrangements.`
5. **Renewable project facilitation** — `Site suitability, resource-adjacent land banking, and coordination across solar, wind, hybrid and pumped storage development.`
6. **Project development support** — `Documentation, due-diligence packs for lenders and acquirers, land schedules, and ongoing support through construction.`

Section header:
- Eyebrow: `CAPABILITIES`
- H2: `What we take off your critical path`
- Intro: `Six areas of practice, delivered as one continuous mandate or engaged individually.`

**Why "one continuous mandate or engaged individually":** pre-empts the buyer's real question — *do I have to take the whole package?* — in nine words. Good microcopy answers objections before they form.

**M.** Cards fade + `y:16`, staggered by grid position, 60ms, capped at 6, once.
**A.** Grid is a `<ul>` of `<li>`; each card link has an accessible name of the full service title ("Land aggregation — explore service"); the `→` is `aria-hidden`. Focus-visible state must be identical to hover so keyboard users see the same affordance.
**R.** 1024–1279: 2 columns. 768–1023: 2 columns, `min-height` released. <768: 1 column, card padding 24px, `min-height` removed so cards size to content.

---

### 5.5 Development lifecycle

**P.** Method as proof. With no completed projects to show, a rigorously articulated process is the strongest credibility artefact available — it says "we have done this enough times to have named the steps."

**L.** `forest-800` — the page's first dark break, arriving at roughly 35% scroll depth, which is where a long page needs a rhythm change. Seven stages on a **horizontal timeline**: a 1px `rgba(232,217,168,0.25)` rule runs the full width; each stage sits on a 12px `gold-500` node; content alternates above/below the line on desktop to fit seven columns without crowding.

**C.** Eyebrow `OUR APPROACH` · H2 (white) `A sequence, not a service list` · intro (`rgba(255,255,255,0.78)`, 60ch) `Land and approvals fail when they are run in parallel by parties who do not talk to each other. We run them as one dependency-ordered programme.`

| Stage | Title | Line |
| --- | --- | --- |
| 01 | Site screening | Resource, terrain, evacuation proximity and land-tenure pattern assessed together. |
| 02 | Land feasibility | Revenue records, classification, ceiling and tenancy constraints verified before commitment. |
| 03 | Aggregation strategy | Parcel sequencing and negotiation order designed to prevent hold-out leverage. |
| 04 | Acquisition & conveyance | Negotiation, documentation, registration, mutation. |
| 05 | Statutory clearances | Approvals filed in dependency order across district, state and utility authorities. |
| 06 | Transmission & RoW | Corridor alignment, landowner settlement, access arrangements. |
| 07 | Handover & support | Land schedules, diligence packs, continued support through construction. |

Closing CTA in-section: ghost button `Read our approach in detail` → `/approach`.

**I.** Desktop: hovering or focusing a stage raises its node to 16px and brightens its text from 0.78 to 1.0 opacity, 200ms. No click behaviour, no accordion — this is a diagram, and making a diagram interactive without payoff is a common over-design mistake.

**M.** The connecting rule draws left-to-right via `scaleX 0 → 1`, 800ms, `transform-origin: left`, triggered once at 30% in view. Nodes pop in sequentially with 80ms stagger, `scale 0 → 1`, 200ms each. Reduced motion: rule and nodes render at final state instantly. **This is the site's one permitted signature animation — a drawn line reads as engineering, not decoration.**

**A.** Stages are an `<ol>`. Alternating above/below placement is purely visual (CSS `align-self`), so DOM order remains 01→07 for screen readers and keyboard tab order. The timeline rule is decorative CSS. Text on `forest-800`: white ≥13:1, `rgba(255,255,255,0.78)` ≈ 10:1 — both fine.

**R.** 1024–1279: seven stages get tight; drop to a 4+3 two-row timeline. <1024: **vertical timeline** — a 1px rule on the left at 24px inset, nodes on it, content to the right, 40px gap between stages. Vertical is the correct mobile pattern for sequences; horizontal-scroll timelines are consistently ignored by mobile users because the scroll affordance is invisible.

---

### 5.6 Karnataka coverage

**P.** Geographic specificity is proof. "We work in Karnataka" is a claim; a district-level map is evidence of where you have actually been.

**L.** `canvas`. Two columns, 5/7. Left (5): eyebrow, H2, paragraph, and a short list of terrain/regulatory notes. Right (7): **inline SVG map of Karnataka with district boundaries** — active districts filled `forest-800`, adjacent `forest-100`, remainder `#F2F2EE` with `line` strokes, all boundaries at 1px.

**C.**

- Eyebrow: `WHERE WE OPERATE`
- H2: `Karnataka, district by district`
- Body: `Land practice does not generalise across state lines, and barely generalises across districts. Revenue procedure, land classification, tenancy history and local body process differ enough that experience earned in one district is only partially transferable to the next. Our work is concentrated in the state's high-resource corridors.`
- Note list (mono label + line): `RESOURCE CORRIDORS` / `WIND — Chitradurga, Gadag, Koppal, Davanagere · SOLAR — Tumakuru, Ballari, Vijayapura, Kalaburagi · PSP — Western Ghats fringe`
  *(Replace with the districts you have genuinely worked in. Do not list all 31. A short honest list is more credible than a full map, and a full map invites the question "all of them?")*

**I.** Hovering/focusing a district shows a small `forest-900` tooltip with the district name and a one-line note. Tooltip on hover **and** on keyboard focus. Districts are `<path>` elements with `tabindex="0"`, `role="img"` and `<title>`; if that becomes unwieldy, provide a plain text list of districts below the map instead and mark the SVG `aria-hidden`. **The text list is the safer choice** — an interactive SVG map that is not fully keyboard-accessible is an accessibility liability with little conversion upside.

**M.** Districts fade in with a 25ms stagger sweeping north-to-south, 400ms total. Subtle. Once.
**A.** SVG needs `role="img"` and `<title>Districts of Karnataka where Bolamudi Enterprise operates</title>` plus a `<desc>`. Colour alone must never be the only differentiator — active districts also get a 1.5px `gold-500` stroke.
**R.** <1024: map moves below text, scales to full width, max-height 420px, tooltips replaced by the always-visible text list. Hover-dependent information must never be mobile-only content.

---

### 5.7 Statutory approvals

**P.** **This is the most important section on the page.** It is the artefact that proves competence without requiring a track record. It is also, by a distance, your best organic-search asset — "solar project approvals Karnataka" and similar queries have real volume and almost no well-structured content behind them.

**L.** `surface-1`. Full-width section header, then a **three-column matrix** of approval groups, each a bordered panel on `canvas` with a `gold-500` 2px top rule.

**C.**

- Eyebrow: `STATUTORY SCOPE`
- H2: `Thirty-plus clearances. One dependency chain.`
- Intro (max 68ch): `A utility-scale renewable project in Karnataka passes through district administration, multiple state departments, the transmission utility and central agencies. The approvals are not independent, and the order in which they are filed determines the schedule.`

| Panel | Approvals listed |
| --- | --- |
| **District & revenue** | Land conversion (NA) · Section 109 exemption · 79A/79B compliance · Mutation and khata transfer · Village panchayat NOC · Revenue survey and sketch |
| **State & regulatory** | KREDL registration · KERC approvals · Pollution control board CFE/CFO · Fire and factories NOC · Forest and wildlife referrals · Groundwater clearance |
| **Utility & transmission** | KPTCL/CTU connectivity · Evacuation approval · Bay allotment · Right of way approvals · Crossing permissions · Charging and commissioning clearance |

Below the matrix, a full-width `forest-800` band with a `FileText` icon, headline `Karnataka renewable approvals — a practitioner's guide` and CTA `Download the guide` (opens a modal capturing name, organisation, email; PDF delivered immediately).

**Why the gated download.** It is the one place gating is justified: it captures decision-makers who are not yet ready to talk, and the download itself is proof of expertise. Keep the form to three fields. Do not gate anything else on the site.

**Verify every item on this list against current Karnataka procedure before publishing.** Publishing a stale or wrong approval list on the section that is supposed to prove expertise would be self-defeating. Treat it as a living page with a visible `Last reviewed: [Month Year]` stamp — the stamp itself signals rigour.

**I.** Panels are static. No accordions — accordions hide the very depth this section exists to display, and collapsed content is weaker for SEO.
**M.** Panels fade + `y:16`, 80ms stagger. Approval items inside each panel do **not** animate individually; 18 staggered items would take three seconds and feel broken.
**A.** Each panel is `<h3>` + `<ul>`. All abbreviations (NA, CFE, CFO, RoW, KREDL, KERC, KPTCL, CTU) get `<abbr title="...">` on first use.
**R.** 1024–1279: 3 columns retained, padding to 24px. 768–1023: 2 columns, third panel spans full width. <768: single column, each panel full width, 32px gap.

---

### 5.8 Who we work with

**P.** Self-identification. Four visitor types arrive with different questions; each must see their own label within one viewport and know the site is for them.

**L.** `canvas`, 112px padding. Four columns, each a bordered card 240px min-height with a `forest-100` fill and no icon — deliberately quieter than the services cards so the page's visual hierarchy stays intact.

**C.** Eyebrow `WHO WE WORK WITH` · H2 `Built for the parties who carry schedule risk`

| Card | Copy |
| --- | --- |
| **Renewable energy developers** | Land and clearance execution for projects under active development, from feasibility through construction. |
| **Independent power producers** | Sustained land and regulatory support across a portfolio, in one state, with one accountable team. |
| **Infrastructure & EPC contractors** | Right of way, access, and local clearance support during execution, where delay is measured in daily cost. |
| **Investors & diligence teams** | Independent land and approval diligence on assets under acquisition, including title-risk assessment. |

**Why the investor card matters disproportionately.** Diligence work is a short-cycle, credential-light engagement — the easiest first mandate for a new firm to win, and a direct route into the developer relationships behind the asset. Give it equal weight even though it is the smallest revenue line today.

**M.** Fade + `y:12`, 60ms stagger.
**A.** `<ul>`; cards are non-interactive, so no hover state and no cursor change — do not make things look clickable that are not.
**R.** ≥1024: 4 columns. 768–1023: 2×2. <768: 1 column, `min-height` removed.

---

### 5.9 Why Bolamudi

**P.** Differentiation. This is the section most likely to degrade into adjectives, so the constraint is: **every point must be a statement of fact or method, never a quality.** "Focused" is a quality. "We operate in one state" is a fact. Facts persuade; qualities do not.

**L.** `surface-1`. Two columns, 5/7. Left: eyebrow, H2, short paragraph, primary CTA. Right: four rows, each with a `gold-500` 1px top rule, mono index, `h4` title, two lines of body. Rows, not cards — rows read as a considered argument, cards read as marketing.

**C.** Eyebrow `WHY BOLAMUDI` · H2 `Depth in one state, not presence in twenty`

| # | Title | Body |
| --- | --- | --- |
| 01 | Single-state specialisation | We work only in Karnataka. Land procedure, revenue practice and local body process are state and district specific, and we have chosen depth over geographic spread. |
| 02 | Development-side experience | Our practice is built from two decades inside the execution of utility-scale solar, wind, hybrid and pumped storage projects — not from advisory observation of them. |
| 03 | Continuity from screening to commissioning | The team that assesses feasibility stays through conveyance, clearance and right of way. Nothing is handed to a new party at the point where context matters most. |
| 04 | Documented, auditable process | Every mandate produces a documented land and approvals record suitable for lender, auditor and acquirer review. |

**Note on 02:** this is the sentence that carries the founder's 20 years while preserving your institutional voice. It is honest, it is specific, and it is the strongest claim on the page. Do not weaken it into "extensive experience".

**M.** Rows stagger 70ms; the gold rule above each row draws via `scaleX` from left, 300ms, on the same trigger.
**R.** <1024: single column, left block above rows.

---

### 5.10 Leadership

**P.** The credibility anchor. Everything above describes capability; this is where a specific human being with a verifiable history stands behind it.

> **This section is where I most strongly disagree with the "faceless" choice.** In a relationship business, in one state, with a new entity, the promoter's twenty years is the entire asset. Concealing it is not institutional — it is anonymous, and anonymous is what a shell company looks like. Arup, AECOM and Jacobs all name their leadership.
>
> **Fallback if you overrule me:** retitle to `Our practice`, replace the portrait with photograph #5 (operating site), and carry the same four credential points in the third person without a name. You lose most of the section's power. I would not do it.

**L.** `canvas`. Two columns, 5/7. Left (5): portrait, 4:5, radius 0, with a `gold-500` 4px bottom rule. Right (7): eyebrow, H2, name and title, three short paragraphs, then a four-item credential list with mono labels.

**C.**

- Eyebrow: `LEADERSHIP`
- H2: `Two decades of Karnataka execution`
- Name block: `[Full name]` (h3) · `Founder & Managing Partner` (mono, `gold-600`)
- Paragraphs: career narrative — where the 20 years were spent (name the reputed company if you have permission; if not, "one of India's largest renewable energy developers" is acceptable and still verifiable in conversation), the asset classes executed, the scale, and why the firm was founded.
- Credential list: `EXPERIENCE — 20+ years, utility-scale renewable development` · `ASSET CLASSES — Solar, wind, hybrid, pumped storage` · `FUNCTIONS — Land, liaison, statutory approvals, transmission RoW` · `GEOGRAPHY — Karnataka, district-level` — plus a LinkedIn link, which is a strong and cheap verification signal.

**A.** Portrait `alt` must describe the person and context, not "founder photo". LinkedIn link gets `rel="noopener"` and an accessible name including "opens in a new tab" if it targets `_blank`.
**R.** <1024: portrait above, constrained to 320px wide and left-aligned (not full-bleed — a full-width face on mobile is overwhelming).

---

### 5.11 Governance & conduct

**P.** Handle the unspoken objection. "Government liaison" carries an implication in the Indian infrastructure context, and every institutional buyer — particularly foreign-funded IPPs and investment firms with FCPA/UKBA exposure — is thinking about it. Not addressing it is a bigger risk than addressing it.

**L.** `forest-800`, compact 72px padding. Centred, max 780px: `ShieldCheck` icon in `gold-200`, H3 in white, two sentences, and a link to the full policy page.

**C.**

- H3: `Liaison, conducted on the record`
- Body: `Our work with government departments is procedural: applications correctly prepared, filed in the right sequence, and followed through official channels. Every mandate is documented to a standard that withstands lender, auditor and acquirer review. We do not undertake work that cannot be recorded.`
- Link: `Read our code of conduct →`

**Why the last sentence.** "We do not undertake work that cannot be recorded" is unambiguous without being defensive or preachy. It is the sentence a compliance officer needs to see. Do not soften it.

**M.** Simple fade, no transform. This section should feel plain and matter-of-fact; motion would undercut it.
**R.** Unchanged, padding to 56px, body to 16px.

---

### 5.12 Insights *(defer to phase 2 if you cannot launch with three real articles)*

**P.** Demonstrate currency, build topical authority for SEO, and give the "not ready to talk" visitor something to do other than leave.

**L.** `canvas`. Header row: H2 left, `All insights →` text link right. Three cards: 16:9 image, `gold-600` mono category, `h4` title (2-line clamp), 14px `ink-600` date and read time.

**Launch article set** — these map directly to commercial intent and to your genuine expertise:
1. `Sequencing statutory approvals for a solar project in Karnataka`
2. `Land aggregation in fragmented holdings: preventing hold-out leverage`
3. `Right of way: why corridor alignment is a land problem, not a survey problem`

**I.** Whole card is the link. Hover: image `scale 1 → 1.03` inside `overflow: hidden` (image only, card static), title colour → `forest-800`, 250ms.
**A.** `<article>` inside `<ul>`; date in `<time datetime="">`.
**R.** 1024+: 3 columns. 768–1023: 2 columns, third hidden. <768: 1 column, show 2, `View all insights` button below.

---

### 5.13 FAQ

**P.** Objection handling plus long-tail search capture. Every question here is a real query string, and the answers are your only realistic route to featured snippets in year one.

**L.** `surface-1`. Two columns, 4/8. Left (sticky, `top: 120px`): H2 `Common questions`, a line of body, and `Ask a different question →` linking to the contact form. Right (8): shadcn `Accordion`, single-expand, first item open by default, each item 1px `line` bottom border, question in `h4`, chevron rotating 180° over 200ms.

**C.** Eight questions:

1. `Do you work outside Karnataka?` — No. Single-state depth, stated plainly with the reasoning.
2. `Do you acquire land on your own account?` — Clarify the model: you act for the developer, not as a principal. Important commercial clarification.
3. `At what stage should we engage you?` — Answer: at site screening, before commercial commitment. This is a sales argument disguised as an FAQ.
4. `How long do statutory approvals take in Karnataka?` — Give indicative ranges by category with honest caveats. Ranges signal experience; refusing to answer signals the opposite.
5. `How do you charge?` — Retainer, milestone and success-fee structures explained at a level of detail that qualifies leads without pricing yourself in public.
6. `Can you support due diligence on an asset we are acquiring?` — Yes, positioned as an independent scope.
7. `How do you handle landowner negotiation?` — Method, fairness, documentation. Answers the ESG question implicitly.
8. `What do you need from us to begin?` — Concrete list. Reduces friction for the ready buyer.

**A.** shadcn `Accordion` gives correct `aria-expanded`, `aria-controls` and keyboard behaviour — use it, do not rebuild it. Ensure the accordion is still readable with JS disabled (server-render open, progressively collapse).
**SEO.** Emit `FAQPage` JSON-LD from the same data source that renders the accordion, so the two can never drift apart.
**R.** <1024: left block above, sticky removed, accordion full width.

---

### 5.14 Conversion — CTA and inquiry form

**P.** The primary conversion. Everything above earns the right to this section.

**L.** `forest-900`, 120px padding, id `#contact`. Two columns, 5/7.

**Left (5):**
- H2 (white, 44px): `Start with a conversation about your site`
- Body (`rgba(255,255,255,0.78)`): `Tell us the district, the technology and the stage you are at. We will tell you what the land and approval path looks like, and whether we are the right party for it.`
- Direct contact block, gold hairline above: phone as a `tel:` link at 20px, email as `mailto:`, registered address, and `Response within one business day`.
- Trust micro-row, 13px `rgba(255,255,255,0.6)`: `Confidential · No obligation · NDA on request`

**Right (7): the form.** Card on `canvas`, 40px padding, radius 4px.

| Field | Type | Required | Notes |
| --- | --- | --- | --- |
| Full name | text | ✓ | |
| Organisation | text | ✓ | Qualifies B2B intent |
| Work email | email | ✓ | Label "work email" cuts personal-address noise |
| Phone | tel | — | Optional reduces friction; most will fill it anyway |
| Project stage | select | ✓ | Exploring · Site identified · Under development · Under acquisition |
| Technology | select | ✓ | Solar · Wind · Hybrid · Pumped storage · Transmission · Other |
| District / location | text | — | |
| How can we help | textarea (4 rows) | ✓ | |
| Consent | checkbox | ✓ | `I consent to Bolamudi Enterprise contacting me about this enquiry.` |

Submit: full-width primary button, `Send enquiry`.

**Why eight fields, not three.** Conventional CRO says minimise fields. That optimises for volume, which is the wrong target here — a firm with one senior practitioner cannot process volume, and a bare-email lead cannot be triaged. Two qualified enquiries beat twenty unqualified ones. The two selects also let you answer intelligently in the first reply, which is where trust is actually won. **This is a deliberate departure from conversion best practice and I want the reasoning on record.**

**I.**
- Validation on **blur**, not on keystroke. Live per-character validation feels accusatory.
- Errors: 13px `#B3261E` below the field, plus a 1px red field border and a 16px alert icon — never colour alone.
- Submit → button enters loading state with a 16px spinner and text `Sending…`, disabled, `aria-busy="true"`.
- Success: the form is **replaced in place** by a confirmation panel — `CheckCircle` icon in `forest-700`, `Enquiry received`, `We will respond within one business day. For anything urgent, call [number].` Do not redirect to a thank-you page; in-place replacement keeps the direct contact details visible and is measurably better for follow-through.
- Failure: inline error above the form retaining all entered values, plus the phone number as a fallback path. Never lose a user's input.
- Honeypot field plus time-to-submit check for spam. **No visible CAPTCHA** — reCAPTCHA badges look cheap on a professional services site and add friction to a high-value form.

**A.** Every input has a visible `<label>` (never placeholder-as-label). Errors are wired via `aria-describedby` and the container is `role="alert"` `aria-live="polite"`. Focus moves to the first invalid field on failed submit, and to the confirmation heading on success. Tab order is strictly visual order. Selects use native `<select>` on mobile — custom dropdowns are a recurring accessibility failure and native pickers are better on touch.
**M.** The form card fades + `y:20` on view. No motion on individual fields.
**R.** <1024: left block above form, form full width, 24px padding. Selects and inputs 48px tall on touch. Submit button full width and sticky-adjacent — never require a horizontal reach.

---

### 5.15 Additional global interactions

**Section progress rail (desktop ≥1440px only).** A fixed 2px vertical rail at the right page margin, 12 ticks, active tick in `gold-500`, with the section name appearing on hover. Makes a 9,600px page feel structured rather than endless. `aria-hidden` — it duplicates the nav. Hide below 1440px where there is no spare margin.

**Sticky mobile CTA bar (<768px).** Appears after the user scrolls past the hero: a 64px bar fixed to the bottom, `forest-800`, with `Call` (secondary, `tel:`) and `Request consultation` (primary, scrolls to `#contact`). Hides when the contact section is in view. India B2B reality: a large share of mobile visitors want to call, not fill a form. Add `padding-bottom: 64px` to the page so the bar never covers the footer, and respect `env(safe-area-inset-bottom)`.

**Scroll behaviour.** Native smooth scroll only. `scroll-margin-top: 96px` on every anchor target. No custom scroll libraries (Lenis, Locomotive) — they break browser find-in-page, harm accessibility, and add weight for no benefit on a content site.

**Focus management.** A single global focus-visible style: 2px `gold-500` ring at 2px offset, on every interactive element, in both light and dark sections. Never `outline: none` without a replacement.

---

## 6. SEO

### 6.1 Targets

| Intent | Queries | Handled by |
| --- | --- | --- |
| Primary commercial | `land acquisition for solar projects Karnataka`, `renewable energy land aggregation Karnataka`, `government liaison renewable energy Karnataka` | H1, hero lead, services |
| Secondary | `solar project approvals Karnataka`, `transmission right of way consultant India`, `KREDL approval process` | Sections 5.7, 5.13, service pages |
| Informational | `land conversion for solar plant Karnataka`, `79A 79B land purchase renewable`, `KPTCL evacuation approval process` | Insights, FAQ |
| Branded | `Bolamudi Enterprise` | Everything |

Do not chase `renewable energy company India`. You will not rank, and the traffic is wrong. Specific long-tail queries in your actual niche have low competition and high intent — that is the whole opportunity.

### 6.2 On-page

- **Title (58 chars):** `Land & Statutory Approvals for RE Projects | Bolamudi`
- **Meta description (152 chars):** `Bolamudi Enterprise secures land, statutory clearances and transmission right of way for utility-scale solar, wind, hybrid and pumped storage projects in Karnataka.`
- **Heading structure:** exactly one `<h1>`; each section `<h2>`; card titles `<h3>`; sub-items `<h4>`. Never skip levels. Never style a `<div>` to look like a heading.
- **Internal links:** every service card, the approach CTA, insight cards, and footer links. Descriptive anchor text — never "read more" or "click here".
- **Canonical** self-referencing. `hreflang` only if you add Kannada later.
- **Open Graph / Twitter card:** custom 1200×630 image — logo on `forest-800` with the H1 in serif. Not a screenshot.

### 6.3 Structured data (JSON-LD)

`Organization` (name, url, logo, sameAs → LinkedIn, `foundingDate`, `founder` if named), `ProfessionalService` (`areaServed: Karnataka, IN`, `serviceType` × 6), `WebSite` with `SearchAction`, `BreadcrumbList`, `FAQPage` from Section 5.13. Generate all of it from typed constants in `/lib/schema.ts` — never hand-written in JSX where it will rot.

### 6.4 Technical

- Static generation (SSG) for the homepage. There is no dynamic content; there is no reason to pay for SSR.
- Targets: LCP < 2.0s, INP < 200ms, CLS < 0.05, TTFB < 400ms from India.
- LCP element is the H1 (not the hero image) — achievable because the hero is a text overlay. Preload the heading font; do not let the image become LCP.
- `next/image` everywhere; explicit dimensions; AVIF first.
- Ship Framer Motion only in client components; keep every section shell a Server Component. Target < 120 KB first-load JS.
- `sitemap.xml` and `robots.txt` via Next's metadata API.
- **Host in an Indian region or use a CDN with Indian PoPs.** Vercel's Mumbai edge or Cloudflare. Your entire audience is in India; a US-region deployment costs you 200ms on every request for no reason.

---

## 7. Accessibility — WCAG 2.2 AA

- **Contrast:** every token pair in Section 2.1 was computed, not eyeballed — see the notes under the palette table for the four values that failed on first pass. Two risks remain that a token table cannot cover: (a) any future use of `gold-500` as text or as a focus ring — forbid it in the Tailwind config by not exposing it as a text colour; (b) white text over the lightest region of the hero photograph. Test (b) against the actual image's brightest pixel, not its average, and re-test after any photo swap.
- **Keyboard:** every interactive element reachable and operable. Logical tab order. Focus visible everywhere. No keyboard traps. Mega-menu and mobile sheet trap focus while open and restore it on close.
- **Screen readers:** landmark structure `<header> <nav> <main id="main"> <section aria-labelledby="..."> <footer>`. Every section labelled by its own `<h2>` id. Decorative icons and SVGs `aria-hidden`. Meaningful images get real alt text.
- **Motion:** `prefers-reduced-motion` honoured globally through the shared `<Reveal>` component.
- **Forms:** visible labels, programmatic error association, `aria-live` status, no colour-only error signalling, 44×44px minimum touch targets throughout.
- **Zoom:** usable at 200% zoom and at 320px width without horizontal scroll. Test the approvals matrix and the timeline specifically — multi-column grids are where this breaks.
- **Testing:** axe DevTools on every PR, one full keyboard-only pass, one NVDA or VoiceOver pass before launch, Lighthouse accessibility ≥ 95.

---

## 8. Responsive summary

| Breakpoint | Grid | Hero | Services | Timeline | Notable |
| --- | --- | --- | --- | --- | --- |
| ≥1440 | 12 col, 1200 container | Full, 820px cap | 3 col | Horizontal, 7 stages | Progress rail visible |
| 1280–1439 | 12 col | Full | 3 col | Horizontal | Rail hidden |
| 1024–1279 | 12 col, 24px gutter | H1 52px | 2 col | Horizontal 4+3 | Mega-menu retained |
| 768–1023 | 8 col | Stacked, H1 40px | 2 col | Vertical | Nav → hamburger |
| 640–767 | 4 col | Auto height, H1 36px | 1 col | Vertical | Sticky CTA bar appears |
| <640 | 4 col, 20px margin | Auto, CTAs stacked | 1 col | Vertical | Selects native, 48px inputs |

**Mobile-specific rules that are easy to get wrong:**
- Never `100vh` on the hero. Mobile browser chrome makes it unreliable and pushes the CTA below the fold.
- Never rely on hover for content — the district map and any tooltip must have a non-hover equivalent.
- Never horizontal-scroll a timeline or card row without a visible affordance; prefer vertical stacking.
- Always leave bottom padding equal to the sticky CTA bar height.
- Test on a 360×640 device, not just the 390px iPhone viewport. A large share of Indian Android traffic is 360px or narrower.

---

## 9. Build sequence

1. **Design tokens** — Tailwind config: colours, type scale, spacing, radii, easing curves. Nothing else starts until this is locked.
2. **Primitives** — Button (primary/secondary/ghost), Card, SectionHeader, Eyebrow, Container, Reveal, RevealGroup.
3. **Chrome** — Header (both states, mega-menu, mobile sheet), Footer, skip link, focus styles.
4. **Sections in page order.** Each is a self-contained Server Component under `/components/sections/`, content injected as typed props from `/content/home.ts`. Content lives in data files, not JSX — this is what makes copy iteration cheap and lets the FAQ feed both the accordion and the JSON-LD from one source.
5. **Form** — react-hook-form + zod, server action, spam guard, email delivery via Resend or SES, success and failure states.
6. **SEO layer** — metadata, JSON-LD, sitemap, OG image.
7. **QA** — Lighthouse, axe, keyboard pass, screen reader pass, real-device testing on 360px Android and iOS Safari.

**Blockers to clear before build starts:** horizontal logo lockup and monogram · photography shoot (six shots) · founder portrait and biography · verified district list · verified statutory approvals list · registered address and registration numbers · phone number and email routing.

---

## 10. Decisions I would revisit with you

1. **Faceless positioning.** Covered at length. My position is that it is the single biggest risk in this brief.
2. **Page length.** ~9,600px is justified only if every section carries real information. Audit ruthlessly at content stage.
3. **Eight-field form.** Deliberately against CRO orthodoxy. Correct for a capacity-constrained senior practice, wrong for a volume business. If you later want volume, cut to name/email/message and qualify by phone.
4. **Insights at launch.** Three real articles or none. Placeholder content is worse than an absent section.
5. **Approvals matrix accuracy.** The section that proves expertise must be correct. Budget time to verify it, and date-stamp it.
