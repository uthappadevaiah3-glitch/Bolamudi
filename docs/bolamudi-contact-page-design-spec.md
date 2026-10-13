# Bolamudi Enterprise — Contact Page Design Specification

**Route:** `/contact`
**Version:** 1.0 · 10 Aug 2026
**Roles applied:** Product Strategy · UX · UI · Creative Direction · Content · SEO · Frontend Architecture

---

## 0. Inherited assumptions (flag before you build)

I do not have the design tokens from the pages already specified in this project. This page assumes the following and **must be reconciled** against the global system:

| Assumption | Value used here | Action |
|---|---|---|
| Primary brand colour | Deep navy `#0B2540` | Confirm against global palette |
| Accent | Restrained teal `#0E7C86` (or ochre `#B4762B`) | Confirm |
| Type | Single grotesk (Inter / IBM Plex Sans), no serif pairing | Confirm |
| Grid | 12-col, 1280px max content, 80px gutters desktop | Confirm |
| Header/footer | Already built, sticky header 72px | Reuse, do not redesign |

**Colour decision, explained:** avoid "eco green." Every second renewable company in India uses leaf-green, which reads NGO or startup, and makes Bolamudi visually interchangeable with its own competitors. Navy + a single desaturated accent is the palette of Black & Veatch, Arup, WSP and Jacobs because it reads *engineering*, not *environmentalism*. The client is not buying sustainability — they are buying execution certainty on a ₹500–2,000 crore asset.

---

## 1. Strategic premise — what this page actually is

A contact page for a B2B project-development consultancy is **not** a "get in touch" page. It is a **qualification and reassurance page**. Two visitor states arrive here:

**State A — Cold, direct arrival (approx. 35–45% of traffic).** Landed from a Google search like *"land aggregation consultant Karnataka solar"*. Has never seen the Services page. Will not fill a form until the page proves, in under 8 seconds, that this is a serious firm and not a broker.

**State B — Warm, internal navigator (approx. 55–65%).** Already read Services and Experience. Wants the form immediately, or wants a phone number to call today.

**Design consequence:** the page must front-load a compressed credibility line *and* the form simultaneously — no long hero, no scroll-to-find-the-form. Direct channels (phone/email/WhatsApp) sit adjacent to the form so State B is never forced through a form to reach a human. That single decision drives the two-column layout in §3.

### Page objectives, ranked
1. Produce **qualified** project enquiries with enough context to scope a call (primary conversion).
2. Give a decision-maker a **direct human channel** in one tap (secondary conversion).
3. Capture the brochure lead (tertiary — see §6 and the pushback there).
4. Deflect unqualified traffic (job-seekers, panel vendors, EPC cold-callers) via FAQ and form structure.

### Success metrics
- Form completion rate of form-starters: target **>55%** (long B2B forms plateau here; below 40% means the field set is wrong).
- Enquiries with a stated project location + capacity: target **>70%** (this is the real quality metric, not raw volume).
- Phone/WhatsApp tap rate: target **>6%** of page sessions.
- Bounce on `/contact`: expect 45–60% and do not optimise it — cold arrivals who read the FAQ and self-disqualify are a *success*.

### Brutal note on volume
This page will receive very low traffic — realistically 100–600 sessions/month in year one. **Do not optimise it for conversion-rate mechanics.** Optimise every element for the single reader who is a project head at an IPP. One correct enquiry is worth more than a 3% CTR improvement. This principle overrides several "best practices" below, and I flag where.

---

## 2. Information architecture and section order

```
1. Page header band (compact, dark)         — H1, positioning line, response SLA
2. Main grid: Enquiry form  |  Contact rail — the conversion zone (rail is sticky)
3. "What happens next" 3-step               — inside the form column, below submit
4. Operational footprint / map              — orientation + coverage proof
5. Credentials & trust strip                — statutory bodies, confidentiality note
6. FAQ accordion                            — deflection + long-tail semantic content
7. Closing contact band                     — call / WhatsApp for non-form users
```

**Why the map is *after* the form, not before it.** Map placement above the form is a legacy pattern from retail and clinic websites, where the user's job is *to physically visit*. Nobody visits a project-development consultancy before signing an NDA. The map's job here is **coverage proof**, not navigation — so it belongs adjacent to the trust section, not above the conversion action.

**Why no hero image.** Stock photography of solar farms and hard hats is the single fastest way to look like a startup or a reseller. AECOM and Arup use their own project photography or none at all. Bolamudi has no photo library it can legally publish (client sites, confidentiality). The header band therefore uses a **dark navy field with a faint technical texture** — a 1px contour/grid pattern at 4–6% opacity — which reads survey drawing, costs nothing in LCP, and can never look fake.

---

## 3. Section-by-section specification

### 3.1 Page header band

**Layout:** full-bleed dark band, 12-col grid, content in cols 1–8. Padding `pt-20 pb-16` desktop (`pt-12 pb-10` mobile). No image, no CTA button.

**Content:**

- Breadcrumb (small, 13px, `Home / Contact`) — aids SEO and orientation on cold arrival.
- **H1:** `Contact Bolamudi Enterprise`
- **Sub-line (20px, max 60ch):** "Speak directly with our founder about land aggregation, statutory approvals and transmission right of way for your project in Karnataka."
- **SLA strip (three inline items, 14px, separated by a 1px vertical rule):**
  `Response within 1 business day` · `20+ years of on-ground execution` · `NDA available before you share site data`

**Decisions explained:**
- **H1 includes the company name.** Cold arrivals from search need to confirm they are in the right place; also matches the branded query "bolamudi contact".
- **Sub-line names the four services in plain language.** It doubles as a self-qualification filter and carries the page's target keywords naturally, not stuffed.
- **The SLA strip is the highest-ROI element on the page.** The number-one reason a project head does not submit a B2B form is uncertainty about whether anyone will reply. Stating the response window converts. The NDA line is specific to this business: land parcel data and site coordinates are commercially sensitive, and offering the NDA *before* they ask signals you have done this before. No startup thinks to write that line.
- **No CTA button in the header.** The form is already visible. A button that scrolls 200px is noise.

### 3.2 Main grid — the conversion zone

**Desktop:** 12-col grid. Form in cols 1–7 (58%). Contact rail in cols 9–12 (approx. 33%) with a one-column gap. Rail is `position: sticky; top: 96px` and stops before the section ends.

**Why the form is on the left, not the right.** Left-to-right reading and F-pattern scanning place the first fixation in the top-left. The primary action belongs there. The rail on the right functions as a persistent **escape hatch** — a visitor who dislikes forms can see the phone number the entire time they scroll the form. Putting contact details left and the form right (the other common pattern) subordinates the conversion action and pushes a 12-field form into the narrower column, which is a layout mistake.

**Why sticky.** The form is tall. Without stickiness, the phone number scrolls away exactly when the visitor gets fatigued at field 8 — the moment they are most likely to abandon and call instead. Sticky rail captures that abandonment as a phone conversion rather than a bounce.

#### Contact rail contents, in order

**1. Direct channels card** (white card on `slate-50` page background, 1px `slate-200` border, no shadow — shadows read consumer-SaaS; borders read document/engineering)

| Channel | Display | Behaviour |
|---|---|---|
| Phone | `+91 XXXXX XXXXX`<br><span>Direct line — Founder</span> | `tel:+91XXXXXXXXXX` |
| Email | `enquiries@bolamudi.in` | `mailto:` with prefilled subject `Project Enquiry — [Your Company]` |
| Email (secondary) | `careers@bolamudi.in` | Deflects job applicants out of the project funnel |
| WhatsApp | `Message on WhatsApp` | `https://wa.me/91XXXXXXXXXX?text=<prefilled>` |

Prefilled WhatsApp text: `Hello, I would like to discuss a renewable energy project in Karnataka.` — removes the blank-message hesitation and pre-frames the conversation as business.

**Decisions explained:**
- **"Direct line — Founder" is a competitive weapon.** Against AECOM or a large IPP's internal team, Bolamudi's structural advantage is principal-level access. Say it. Large firms cannot.
- **Two email addresses make a one-person firm read as an organisation.** This is cheap (aliases) and effective. `careers@` also protects the founder's inbox from CV spam, which matters given the email-only backend (§5.5).
- **WhatsApp is styled as a neutral outline button, not the brand-green WhatsApp pill, and there is no floating bubble widget on desktop.** In Indian infrastructure and land dealings, WhatsApp *is* the working channel — omitting it would be tone-deaf. But a green floating WA bubble is the visual signature of a small trader, and instantly contradicts the "established consultancy" positioning. On mobile, WhatsApp is promoted to the sticky action bar (§9) because that is where it is actually used. This is a deliberate desktop/mobile divergence, not an inconsistency.

**2. Business hours card**

```
Business hours (IST)
Monday – Friday      09:30 – 18:30
Saturday             09:30 – 13:30
Sunday               Closed

● Open now                       [computed]
Site visits and field meetings by prior appointment.
```

**Decisions explained:**
- **"IST" is stated explicitly.** Investment firms and international developers (Japanese, Singaporean, European capital is active in Karnataka RE) will read this page from other time zones.
- **Saturday half-day is included.** It is the honest Indian business norm and reads as locally credible; a Mon–Fri-only block looks copy-pasted from a US template.
- **The "Open now / Closed" pill is computed from IST, not the browser's clock.** Render it only after hydration (`useEffect`) to avoid a server/client mismatch and a CLS shift. If JS is off, the pill is absent — no broken state.
- **"By prior appointment"** manages the expectation that someone can walk in. Given the unresolved office question (§7), this line is doing real work.

**3. Brochure download card** — see §6.

### 3.3 "What happens next" — 3-step, inside the form column

Placed **directly below the submit button**, three numbered steps, horizontal on desktop, stacked on mobile:

1. **Acknowledgement** — You receive a confirmation email with a reference number, immediately.
2. **Scoping call** — A 30-minute call within one business day to understand the site, capacity and timeline.
3. **Written scope** — A confidentiality undertaking and a defined scope of work before any data changes hands.

**Why this exists.** Submit anxiety — "what am I signing up for, will I be spammed, will a salesperson chase me" — is the largest silent killer of B2B form conversion. Naming the next three steps removes it. It is also a soft demonstration of process maturity: a broker has no process to describe. This block costs one component and is worth more than any visual polish on the page.

---

## 4. Enquiry form — full specification

### 4.1 Field set

Grouped into three visible `<fieldset>`s with `<legend>`s. Single column throughout (two-column form rows increase completion errors and break on zoom).

**Fieldset 1 — Your details**

| # | Field | Type | Req | Notes |
|---|---|---|---|---|
| 1 | Full name | text | ✅ | `autocomplete="name"` |
| 2 | Company / Organisation | text | ✅ | `autocomplete="organization"` |
| 3 | Designation | text | — | `autocomplete="organization-title"` |
| 4 | Email | email | ✅ | Label helper: "Work email preferred" |
| 5 | Phone / WhatsApp | tel | ✅ | `+91` prefix default, country selector, 10-digit validation for IN |

**Fieldset 2 — Project details**

| # | Field | Type | Req | Options |
|---|---|---|---|---|
| 6 | Nature of enquiry | select | ✅ | Land Aggregation · Government Liaison & Statutory Approvals · Transmission Right of Way · Project Development Support · Pumped Storage / Hybrid Advisory · Partnership or Vendor · Careers · Other |
| 7 | Technology | chip multi-select | — | Solar · Wind · Hybrid · BESS · Pumped Storage · Transmission |
| 8 | Project location | text + district autocomplete | — | Placeholder: "District, State — e.g. Koppal, Karnataka" |
| 9 | Approximate capacity (MW) | number | — | `min=0`, no spinner styling |
| 10 | Project stage | select | — | Exploratory · Site identification · Land aggregation in progress · Approvals stage · Financial closure · Under construction |

**Fieldset 3 — Your requirement**

| # | Field | Type | Req | Notes |
|---|---|---|---|---|
| 11 | Message | textarea | ✅ | 4 rows, 1,000 char limit, live counter from 800 |
| 12 | Consent | checkbox | ✅ | DPDP notice — see §4.6 |
| 13 | Updates opt-in | checkbox | — | "Send me occasional updates on Karnataka RE policy and approvals." Unchecked by default. |

Message placeholder (it teaches, it does not describe): `Site location, approximate extent of land required, target capacity and expected timeline.`

### 4.2 Why 13 fields and not 4 — the central form decision

Conventional CRO wisdom says shorten the form. **That advice is wrong for this business, and here is why.**

- **The funnel is low-volume, high-value.** An unqualified enquiry costs the founder a wasted hour. A lost enquiry costs one lead out of maybe twenty a month. At this ratio, qualification beats volume — the asymmetry runs the opposite way to e-commerce.
- **Form length is a credibility signal in this sector.** A three-field "Name / Email / Message" box is what a startup landing page uses. An RFI-style structured form is what a consultancy uses. The form's *shape* communicates that you intend to scope work, not chase leads.
- **Structured data makes the first call competent.** Knowing "Koppal, 250 MW solar, land aggregation in progress" before dialling turns a discovery call into a consultation. That converts.
- **Only 6 of 13 fields are required.** Perceived length is managed by grouping (three short fieldsets read faster than one 13-row wall), clear `Optional` markers, and a single column with generous 24px vertical rhythm.

**Explicitly rejected: multi-step wizard.** It hides total length (which feels manipulative to a senior audience), breaks browser autofill, complicates keyboard and screen-reader flow, and adds state management for zero measurable gain at this traffic volume. One page, three groups.

**Note the "Careers" and "Partnership or Vendor" options in field 6.** These are deliberate routing valves: they let unqualified traffic self-identify so it can be auto-routed to a different inbox and out of the project pipeline, instead of being disguised as a project enquiry.

### 4.3 Field UI

- **Labels always visible above the input.** Never placeholder-as-label — it fails WCAG 3.3.2, disappears on focus, and breaks for anyone interrupted mid-form.
- Input height 48px, radius 6px (not pill — pills read consumer), 1px `slate-300` border, `slate-900` text at 16px (16px minimum prevents iOS zoom-on-focus).
- Focus: 2px accent ring + 2px offset. Never `outline: none`.
- Required marked with `*` **and** the word "Required" in the accessible name; optional fields labelled `(optional)` in `slate-500`. Marking optionals rather than requireds is better when most fields are optional — here it is roughly even, so mark both.
- Submit: full-width on mobile, auto-width left-aligned on desktop. Label `Submit enquiry` — not "Send" (too casual), not "Submit" (bureaucratic).

### 4.4 Validation, states, errors

- **Validate on blur, never on keystroke.** Keystroke validation shows an error on the first character of an email — a well-documented irritant.
- **Zod schema shared** between client and the route handler. One source of truth; the server re-validates because client validation is a UX affordance, not a security control.
- **Error presentation:** red 14px text below the field, `aria-invalid="true"`, `aria-describedby` pointing at the error id, plus a **non-colour cue** (an alert icon) for colour-blind users.
- **Error summary** at the top of the form on failed submit: `role="alert"`, `tabindex="-1"`, focus moved to it, listing each error as a link to its field. This is the single most useful accessibility feature on any long form.
- **Submitting:** button gets `aria-busy="true"` and a spinner, label changes to `Submitting…`. **The button is not disabled** — a disabled button loses focus and is invisible to some screen readers. Guard against double-submit in the handler, not the DOM.
- **Success:** stay on the page, replace the form region with an inline confirmation panel inside a `role="status"` live region:
  > **Enquiry received — reference BOL-2608-4712.**
  > A confirmation has been sent to `name@company.com`. We will respond within one business day.
  > Meanwhile: `Download Company Profile` · `Read the FAQ`

  **Why inline, not a redirect to `/thank-you`.** A redirect loses the reference number in a page the user will never revisit, and creates an indexable thin page you then have to `noindex`. Inline confirmation keeps the brochure CTA in front of a now-warm lead. If GA4/Ads conversion tracking is ever required, fire the event on success — a URL change is not needed.
- **Failure:** inline error panel offering the phone number and email as fallbacks, with the message text preserved in the textarea. Losing a typed enquiry is unforgivable — persist the draft to `sessionStorage` under a namespaced key and clear it on success.

### 4.5 Anti-spam

Layered, cheapest-first:

1. **Honeypot** field, visually hidden with `position:absolute; left:-9999px`, `aria-hidden="true"`, `tabindex="-1"` (never `display:none` — some bots detect it; never focusable — screen readers must not find it).
2. **Time-to-submit floor** — reject submissions completed in under 3 seconds.
3. **Cloudflare Turnstile** (invisible mode). Chosen over reCAPTCHA v3: no Google advertising cookie, materially better for a DPDP-era privacy notice, and no "select the traffic lights" accessibility failure.
4. **Rate limit** in the route handler: 5 submissions per IP per hour.

### 4.6 Consent and DPDP compliance

India's **DPDP Rules, 2025 were notified on 13 November 2025**, with most operational obligations — notice, consent, rights workflows, breach reporting — to be fully in place by **mid-May 2027**, and the Consent Manager framework becoming operational **13 November 2026**. A contact form collecting name, email and phone is processing digital personal data of Indian residents, so this page is in scope. Build it right now rather than retrofitting.

**Required, not optional:**
- An **itemised notice** at the point of collection — what is collected, the specific purpose, and how to withdraw. Not a link alone.
- Consent checkbox, **unchecked by default**, with its own visible label. No pre-ticked boxes, no bundling the marketing opt-in with the enquiry consent — that is exactly what the Rules prohibit. Hence two separate checkboxes (fields 12 and 13).
- Named **grievance contact** and a working withdrawal route reachable from the site.

**Consent checkbox copy:**
> ☐ I consent to Bolamudi Enterprise using the details above to respond to this enquiry and to maintain a record of our correspondence. You can withdraw consent or request deletion at any time by writing to privacy@bolamudi.in. See our [Privacy Notice](/privacy).

**Requires legal input, not design input:** identity and registered address of the data fiduciary, named grievance officer, and retention period. Flagged as a blocker for launch, not a nice-to-have.

### 4.7 Backend — email-only (as chosen), and its risk

Chosen: transactional email, no CRM. Workable, with mandatory mitigations.

| Element | Spec |
|---|---|
| Transport | Resend or AWS SES from a verified sending domain |
| To | `enquiries@bolamudi.in` (a **distribution alias**, not a personal Gmail) |
| BCC | A second address the founder does not use daily — recovery copy |
| Auto-ack | Immediate to the enquirer, with reference `BOL-DDMM-NNNN`, plain-text-first HTML, from the same verified domain |
| Deliverability | SPF, DKIM and DMARC on the sending domain before launch — non-negotiable |
| Subject line | `[Enquiry] {Nature} — {Company} — {Location}, {MW} MW` so the inbox is sortable |
| Body | Plain-text table of all fields, in submission order |

**Brutal risk, stated plainly.** With email-only, **you cannot prove an enquiry arrived.** One spam-folder classification, one full mailbox, one DKIM misconfiguration and a ₹1,000+ crore project enquiry vanishes with no trace and no alert. For a business whose entire proposition is reliability, that is a poorly-placed risk.

Cheapest fix, roughly two hours of work: append every submission to a Postgres table (Neon/Supabase free tier) or, at minimum, a Google Sheet via a service account, **before** attempting the email send. The reference number then means something. Recommend doing this at launch, not later.

---

## 5. Operational footprint / map section

Your answer on the office address was "not decided," so this is specified as a **two-mode component** with a clear recommendation.

```tsx
<OfficeMap mode="region" | "pin" />
```

### Mode A — `region` (recommended until a commercial office exists)

Full-width section, dark navy background. Left column (cols 1–5): heading `Where we operate`, a short paragraph, and the text address block. Right column (cols 6–12): an inline **SVG outline of Karnataka** with markers on the districts where projects have been executed — Koppal, Gadag, Ballari, Vijayapura, Bagalkot, Raichur, Chitradurga, Tumakuru, Belagavi (confirm the actual list).

Address block:
```
Registered office
Bengaluru, Karnataka, India
Correspondence and meetings by appointment.
```

**Why this is the stronger design, not a compromise.** Dropping a Google pin on a residential address is the fastest way to destroy the "established consultancy" positioning you asked for — a visitor who street-views a house has re-priced you in three seconds. A district-marked coverage map answers the question the visitor actually has ("have you worked near *my* site?") instead of the question they didn't ask ("which building do you sit in?"). It converts an absence into execution proof.

Secondary benefits: inline SVG means zero third-party requests, no consent banner implications, no CLS, and full control of styling to match the palette. A Google Maps iframe cannot do any of that.

### Mode B — `pin` (only once a commercial office is signed)

Google Maps **Embed API** iframe, with a **click-to-load** wrapper: a static styled map image with a `Load interactive map` button; the iframe mounts only on click.

Reasons: a Maps iframe pulls roughly 0.6–1 MB and sets third-party cookies before any user action — bad for LCP, bad for the privacy notice. Click-to-load fixes both. `loading="lazy"`, `title="Map showing the location of the Bolamudi Enterprise office"`, `referrerPolicy="no-referrer-when-downgrade"`. Always place a `Get directions` text link beside it, because a text link works when an iframe is blocked.

**Both modes render at exactly the same height** so the section never shifts when you switch modes.

---

## 6. Brochure download — gated, as chosen, plus a pushback

### Flow as specified

Rail card, third position:

> **Company Profile & Credentials**
> Project experience, statutory approval track record, and scope of services. PDF, 12 pages, 2.4 MB.
> `[ Download Company Profile ]`

Click opens a **modal** (not a page navigation — never lose the enquiry form state) with three fields: Full name*, Company*, Work email*, plus the DPDP consent line. On submit:

1. Show the download link **immediately, on screen** — `<a href="/downloads/bolamudi-company-profile-2026.pdf" download>`.
2. **And** email the same link.

**Deliver both, always.** Email-only delivery loses every user who mistypes an address or whose corporate filter quarantines the mail — that is 20–40% of gated downloads, and they leave believing you are broken.

Technical: PDF served from `/public/downloads/`, versioned filename, `<5 MB`, generated as PDF/A with real text (not scanned images) so it is searchable and accessible. Fire an analytics event `brochure_download`. Set `Content-Disposition: attachment`.

### The pushback

Gating is a defensible B2B default, but at **100–600 sessions/month it is optimising the wrong variable.** You are trading credibility (open, confident disclosure) for perhaps 5–15 email addresses a month that you already capture better through the enquiry form. Senior project heads at IPPs are precisely the audience most likely to abandon a gate for a company profile — they have five other consultants to evaluate.

**Recommended compromise, if you will take it:** two documents.
- **Capability Statement** — 2 pages, ungated, one click. Services, districts, years, approval bodies.
- **Company Profile & Credentials** — 12 pages, gated. Project detail, references, approval track record.

This gives cold visitors something immediately (credibility) and reserves the gate for genuinely high-intent readers (lead quality). It is the pattern most mid-size engineering consultancies converge on. Built as specified either way — the component takes a `gated: boolean` prop, so this stays a one-line decision you can reverse.

---

## 7. Credentials & trust strip

Full-width, light background, above the FAQ. Four elements:

**7.1 Four metrics** (large numerals, no icons, no count-up animation):

| Metric | Value |
|---|---|
| Years of on-ground execution | 20+ |
| Capacity facilitated | ___ MW *(needs a real, defensible number)* |
| Districts covered in Karnataka | ___ |
| Statutory approvals secured | ___ |

**No count-up animation on the numbers.** Animated counters are a startup/marketing tic. Static numerals read as facts on a document. This is a deliberate rejection of a very common pattern.

**Every number must be defensible if a due-diligence team asks.** If capacity facilitated cannot be substantiated, delete the metric — a challenged number destroys more trust than a missing one creates.

**7.2 Statutory bodies engaged** — a plain text list, no logos:
`KERC · KPTCL · PCKL · KREDL · Department of Revenue · KIADB · Forest Department · ESCOMs (BESCOM / HESCOM / GESCOM / MESCOM / CESC) · CEIG · SLDC · Gram Panchayat & Tahsildar offices`

**This is the highest-value trust element on the page and no competitor can fake it.** A firm that has not actually filed and followed up with PCKL and the Tahsildar's office does not write that list. To an IPP project head it is instantly legible as insider knowledge. Confirm each entry — one wrong body-name signals the opposite.

**7.3 Confidentiality note** (replaces a client logo wall):
> Client names and project details are withheld under confidentiality undertakings. References are shared on request during evaluation.

**Do not display client logos you do not have written permission to use.** It is a legal exposure and, worse, a sophisticated buyer will verify one. The confidentiality line is *stronger* — it says you handle sensitive land and approvals data professionally.

**7.4 Founder credibility line** — one sentence, name and 20+ years at a named or unnamed reputed developer, with a link to `/about`. Personal accountability is this firm's asset; don't hide it behind a corporate "we".

---

## 8. FAQ

**Placement:** below trust, above the closing band. **Layout:** two columns on desktop — heading and a "still have a question?" nudge in cols 1–4 (sticky), accordion in cols 6–12. Single column on mobile.

**Behaviour:** `<details>/<summary>` based (shadcn Accordion is fine, but ensure a `button` with `aria-expanded` if not using native). **First item closed by default** — an open item biases which question is read. Allow multiple open simultaneously; forcing single-open makes comparing two answers annoying.

### FAQ copy (8 items)

**1. What exactly does Bolamudi Enterprise do?**
We provide project development support for utility-scale renewable energy projects in Karnataka — land identification and aggregation, government liaison, statutory and regulatory approvals, and transmission right of way. We work on behalf of developers, IPPs and EPC contractors; we do not develop or own projects ourselves.

**2. Do you work outside Karnataka?**
Our depth is in Karnataka, where we have two decades of relationships across Revenue, Forest, KPTCL and the ESCOMs. We evaluate adjacent-state enquiries case by case and will tell you plainly if we are not the right firm for a geography.

**3. How early should we involve you in a project?**
Ideally at site identification, before land negotiations begin. Involving us after advances have been paid on parcels means we inherit constraints — title defects, missing access, unsuitable classification — that are expensive or impossible to correct later.

**4. Can you help with land that is already partly aggregated?**
Yes. This is common. We assess title, extent, contiguity, access and land classification on what you hold, identify the gaps and constraints, and complete the aggregation.

**5. How do you handle confidentiality on site data?**
We execute a mutual confidentiality undertaking before you share coordinates, survey numbers or commercial terms. Client names and project details are never disclosed in our marketing material.

**6. How are your services priced?**
Engagements are scoped individually — per-acre for land aggregation, milestone-based for approvals, or a retainer for end-to-end development support. Pricing follows the scoping call; we do not publish rate cards, because no two sites carry the same risk.

**7. What is a realistic timeline for statutory approvals in Karnataka?**
It depends on capacity, land classification, evacuation arrangement and whether forest or CRZ clearances are involved. We give an indicative schedule after reviewing the site, and we flag the specific dependencies that will drive the critical path rather than quoting a generic number.

**8. Do you take on transmission right of way work independently?**
Yes. Right of way and corridor negotiation are frequently the binding constraint on a project, and we take these on as standalone engagements as well as part of full development support.

**Content rationale.** Each answer does one of three jobs: qualifies (2, 6), demonstrates domain judgment (3, 7), or removes a specific objection (5, 8). Answers 6 and 7 deliberately **refuse to give a number** — quoting a price or a fixed timeline for Karnataka approvals would be inaccurate, and a project head who knows the domain would immediately mark you as inexperienced for doing so. Refusing, *and explaining why*, is the credible answer.

### SEO honesty on FAQ schema
Include `FAQPage` JSON-LD for semantic clarity and for LLM/AI-answer surfaces — **but do not expect a search-result benefit.** Google stopped showing FAQ rich results on **7 May 2026**, removed the rich-result report and Rich Results Test support in June 2026, and drops Search Console API support in August 2026. The markup is still valid Schema.org and harmless to keep; anyone selling FAQ schema as an SEO win in 2026 is selling you a 2019 tactic.

---

## 9. Closing contact band

Dark navy, full-width, short. Left: `Ready to discuss your project?` plus one sentence. Right: two buttons — `Call +91 XXXXX XXXXX` (primary, solid) and `Message on WhatsApp` (secondary, outline).

**Purpose:** catches the visitor who read the entire page, including the FAQ, and never touched the form. That reader is high-intent and phone-oriented. Without this band their only option is to scroll back up.

---

## 10. Desktop layout

- Max content width **1280px**, 12 columns, 32px gutters, 80px page margins.
- Vertical section rhythm: 96–120px between sections; 24px between form fields; 8px label-to-input.
- Form column max **640px** — a 45–75 character measure. Wider inputs measurably increase error rates and look like a database admin panel.
- Rail sticky at `top: 96px` (72px header + 24px). Rail unsticks before the section boundary so it never overlaps the map section.
- **Breakpoints:** `<640` single column · `640–1023` single column, wider fields · `1024–1279` 8/4 split, tighter gutters · `≥1280` full 7/4 split.
- No shadows anywhere. Hierarchy is expressed through **1px borders, background tone, and whitespace** — the visual language of engineering documents rather than consumer apps.

---

## 11. Mobile layout

Order changes deliberately — the rail cannot simply stack below a 13-field form, or nobody will ever see the phone number.

```
1. Header band (compact)
2. Direct-channels card              ← promoted above the form
3. Enquiry form (single column)
4. What happens next
5. Business hours (collapsed accordion)
6. Brochure CTA
7. Coverage map (SVG scales; region mode only on mobile)
8. Trust metrics (2×2 grid)
9. FAQ
10. Closing band
+ Sticky bottom action bar: [ Call ] [ WhatsApp ]
```

**Decisions explained:**
- **Contact card above the form on mobile.** Mobile visitors are far likelier to call than to complete 13 fields on a phone keyboard. Making them scroll a long form to find a number is hostile.
- **Sticky bottom action bar, two buttons only, 56px tall, safe-area inset padding.** It appears after 25% scroll (not immediately — an instant overlay on a fresh page reads as an ad). WhatsApp appears here, and only here, because this is where it is genuinely used.
- **Business hours collapsed** to reclaim vertical space; the "Open now" pill stays visible in the collapsed header so the useful signal is not hidden.
- **Map is region-mode on mobile even if pin mode is enabled on desktop.** An interactive Google iframe inside a scrolling page is a scroll-trap on touch devices.
- Tap targets ≥48×48px; inputs 52px tall on mobile; `inputMode="tel"` / `"numeric"` / `"email"` on the relevant fields so the correct keyboard appears.

---

## 12. Motion (Framer Motion)

Deliberately minimal. Motion here should feel like a well-made document settling, not a product launch.

| Element | Motion |
|---|---|
| Section entrance | `y: 16 → 0`, `opacity: 0 → 1`, 400ms, ease `[0.16, 1, 0.3, 1]`, `whileInView` with `once: true`, `amount: 0.3` |
| Stagger within a group | `staggerChildren: 0.08`, capped at 5 children |
| Accordion | Height auto, 220ms |
| Form success panel | Cross-fade 250ms, no slide |
| Buttons | 120ms background transition, no scale |

**Explicitly rejected:** parallax, scroll-jacking, number count-ups, letter-by-letter text reveals, page transitions, hover-tilt cards. Every one of these signals a startup or a portfolio site. Restraint is the brief.

**`prefers-reduced-motion: reduce` removes all of it** — set Framer's `MotionConfig reducedMotion="user"` at the layout level and provide a CSS fallback that zeroes transition durations. This is a WCAG 2.3.3 obligation, and it also matters for the ~35% of users who dislike motion.

**Never animate anything that delays the form becoming interactive.** Form fields render immediately, unanimated; motion applies only to sections below the fold.

---

## 13. Accessibility — WCAG 2.2 AA

**Structure**
- One `<h1>`. Section headings `h2`, subheads `h3`. No level skipping.
- Landmarks: `<main>`, `<form>` with `aria-labelledby`, `<nav aria-label="Breadcrumb">`.
- Skip-to-content link as the first focusable element (inherited from layout — verify it lands on `<main>` here).

**Forms** (the highest-risk area on this page)
- Persistent visible `<label for>` on every input. No placeholder-only labels (3.3.2).
- `<fieldset>`/`<legend>` for the three groups; `<fieldset>` with `role="group"` for the technology chips.
- `autocomplete` tokens on name, organization, organization-title, email, tel (1.3.5).
- `aria-invalid`, `aria-describedby` linking error and helper text.
- Error summary receives focus on failed submit; each entry links to its field (3.3.1, 3.3.3).
- **2.5.8 Target Size (Minimum)** — all controls ≥24×24px CSS; we use 48px.
- **3.3.7 Redundant Entry** — do not re-ask for anything already provided; the brochure modal pre-fills from the enquiry form if it was already submitted in-session.
- **3.3.8 Accessible Authentication** — no cognitive-test CAPTCHA. Turnstile invisible mode satisfies this; reCAPTCHA image challenges would not.
- Submit button never `disabled`; use `aria-busy`.

**Feedback and live regions**
- Success panel: `role="status"` (polite). Failure panel: `role="alert"` (assertive). One live region per outcome — do not stack them, or screen readers announce twice.
- Character counter: `aria-live="polite"`, announcing only from 800 characters, otherwise it chatters.

**Visual**
- Body text ≥4.5:1, large text ≥3:1, **UI component borders and focus indicators ≥3:1** (1.4.11) — the common failure is a `slate-200` input border on white at 1.5:1. Use `slate-300` minimum, and 400 on the dark band.
- Focus visible on every interactive element, 2px + 2px offset, never removed (2.4.7, 2.4.11 Focus Not Obscured — verify the sticky mobile action bar does not cover a focused field; add scroll-padding-bottom).
- Never colour alone: errors carry an icon and text; the "Open now" pill carries a word, not just a green dot.
- Usable at 200% zoom and 320px reflow (1.4.10) — the two-column grid must collapse, not scroll horizontally.

**Links and channels**
- `tel:` and `mailto:` links have accessible names that include the action: "Call +91 XXXXX XXXXX", not just the number.
- WhatsApp link: `rel="noopener noreferrer"`, and the accessible name states it opens WhatsApp.
- Map iframe (pin mode): `title` attribute, and a text `Get directions` link as the non-iframe path.
- Brochure link: accessible name includes format and size — "Download Company Profile, PDF, 2.4 MB" (3.2.5 context change warning).

**Modal (brochure gate)**
- Focus trapped, focus returns to the trigger on close, `Esc` closes, `aria-modal="true"`, `aria-labelledby`, background scroll locked, background content `aria-hidden`.

**Testing gate before launch:** axe DevTools clean; full keyboard-only pass through submit; NVDA/Chrome and VoiceOver/Safari pass; 200% zoom; 320px width; forced-colors mode.

---

## 14. SEO

**Metadata**
```
Title:       Contact Bolamudi Enterprise | Renewable Energy Project Development, Karnataka   (68 chars)
Description: Speak with Bolamudi Enterprise about land aggregation, statutory approvals and
             transmission right of way for solar, wind, hybrid and pumped storage projects
             in Karnataka. Response within one business day.                                 (198 chars)
Canonical:   https://bolamudi.in/contact
Robots:      index, follow
OG:          og:title, og:description, og:url, og:type=website, og:locale=en_IN,
             og:image (1200×630, dark navy with wordmark + "Contact" — not a stock photo)
Twitter:     summary_large_image
```

**Keyword intent this page should own** (transactional/local, not informational — the Services pages carry informational intent):
- `land aggregation consultant Karnataka`
- `renewable energy project development Karnataka contact`
- `solar land aggregation Karnataka`
- `KPTCL transmission right of way consultant`
- `statutory approvals solar project Karnataka`
- `pumped storage project development consultant Karnataka`

These appear naturally in the H1, sub-line, FAQ answers and field labels. No keyword stuffing — this audience is small, specific and reads carefully; awkward phrasing costs more in credibility than it gains in ranking.

**Structured data** (single `<script type="application/ld+json">` graph, server-rendered)
- `Organization` — name, url, logo, `foundingDate`, `areaServed: State "Karnataka"`, `knowsAbout: [...]`, `founder`
- `ContactPoint` — `contactType: "sales"`, `telephone`, `email`, `availableLanguage: [en, kn, hi]`, `hoursAvailable`
- `LocalBusiness` — **only once a real commercial address exists.** Emitting `LocalBusiness` with a residential or vague address is worse than omitting it: it invites a Google Business Profile mismatch and NAP inconsistency. Until then, `Organization` + `ContactPoint` + `areaServed` is the correct and honest markup.
- `BreadcrumbList`
- `FAQPage` — include for semantics; expect no rich result (see §8).
- `WebPage` with `speakable` omitted (not relevant here).

**Technical SEO**
- Server-rendered page (React Server Component); only the form, map and modal are client components. Content must be in the initial HTML.
- Core Web Vitals targets: **LCP < 2.0s** (text LCP element — no hero image, so this is easy to hit), **INP < 200ms**, **CLS < 0.05** (reserve the map's height, gate the "Open now" pill behind hydration, `font-display: swap` with a matched fallback metric).
- `hreflang` not required — `en-IN` only.
- Sitemap: include `/contact` at priority 0.8, `changefreq: monthly`.
- Internal links from this page to `/services`, `/experience` (or `/projects`), `/about`, `/privacy`. Link *to* `/contact` from every page footer and from each service page's closing CTA — contact-page authority in a small site comes almost entirely from internal linking.
- **No `/thank-you` page** to keep out of the index (see §4.4).
- Serve the brochure PDF with a descriptive filename and `X-Robots-Tag: noindex` if you do not want the gated PDF ranking and bypassing the gate. **This is a real leak** — a gated PDF in `/public` is directly reachable by URL. If gating matters, serve it through a signed, expiring route handler instead. Flagging honestly: full gating requires that route; otherwise the gate is decorative.

---

## 15. Frontend architecture

```
app/
  contact/
    page.tsx                    RSC — metadata export, JSON-LD, static content
    _components/
      ContactHeader.tsx         server
      EnquiryForm.tsx           client — react-hook-form + zod
      ContactRail.tsx           server shell
      DirectChannels.tsx        server
      BusinessHours.tsx         client (IST open/closed, post-hydration)
      BrochureCard.tsx          client (modal trigger)
      BrochureGateModal.tsx     client — shadcn Dialog
      WhatHappensNext.tsx       server
      OfficeMap.tsx             client, dynamic import, mode="region"|"pin"
      TrustStrip.tsx            server
      ContactFaq.tsx            server (shadcn Accordion — client leaf only)
      ClosingBand.tsx           server
      MobileActionBar.tsx       client
  api/
    enquiry/route.ts            zod re-validate → Turnstile verify → rate limit → persist → email
    brochure/route.ts           gate verification → signed URL
lib/
  schemas/enquiry.ts            single zod schema, shared client + server
  email/templates/              internal notification + enquirer auto-ack
  constants/karnataka-districts.ts
content/
  contact-faq.ts                FAQ as data → renders the accordion AND the JSON-LD from one source
```

**Decisions explained:**
- **Server-first.** Only five leaves are client components. This keeps the JS bundle small, which is what actually delivers the LCP/INP targets — not any amount of image optimisation.
- **One zod schema** shared by the form and the route handler. Divergent client/server validation is the most common source of silent B2B form failures.
- **FAQ as a data file**, rendering both the visible accordion and the JSON-LD. Two hand-maintained copies of FAQ content always drift, and drifted schema is a quality signal against you.
- **`framer-motion` isolated** in a small `<MotionSection>` wrapper, dynamically imported. Do not import it into the form — motion must never sit on the critical interaction path.
- **shadcn/ui components used:** Form, Input, Select, Textarea, Checkbox, ToggleGroup (technology chips), Dialog, Accordion, Button, Sonner (fallback toasts only — the inline panel is primary; toasts are unreliable for screen readers as a sole channel).

---

## 16. What I would push back on

1. **Email-only backend** — the single biggest risk on this page. Add a database write before launch. Two hours of work protects every enquiry you will ever receive. (§4.7)
2. **Fully gated brochure** — at your traffic volume the gate costs more credibility than it earns in leads. Ship the two-document split. (§6)
3. **Gated PDF in `/public` is not actually gated** — anyone can find the URL. Either accept that the gate is soft, or build the signed route. (§14)
4. **Unresolved office address** — this shapes the map section, the `LocalBusiness` schema and any future Google Business Profile. Decide it before launch; region mode is a genuinely good answer if the answer is "no commercial office yet." (§5)
5. **Unverified trust metrics** — MW facilitated, districts, approvals count. Every number needs to survive a due-diligence question. Delete any that cannot. (§7.1)
6. **DPDP consent text needs legal review** — data fiduciary identity, grievance officer, retention period. Blocker, not backlog. (§4.6)

## 17. Open questions

1. Actual phone number, and is the founder's personal mobile the "direct line"? (Recommended: a dedicated number, so the site can be updated without changing a personal one.)
2. Confirm email domain and aliases: `enquiries@`, `careers@`, `privacy@`.
3. Does the Company Profile PDF exist? Page count, size, and is it design-consistent with the site?
4. Confirmed list of Karnataka districts with executed projects, for the coverage map.
5. Confirmed list of statutory bodies engaged — accuracy is the whole value of §7.2.
6. Named grievance officer for the DPDP notice.
7. Languages the founder handles for the `availableLanguage` schema field (assumed English, Kannada, Hindi).
8. Is a `/privacy` page in scope for this build? The consent checkbox links to it, so it is a hard dependency.

---

## Sources

- [Google Drops FAQ Rich Results From Search — Search Engine Journal](https://www.searchenginejournal.com/google-drops-faq-rich-results-from-search/574429/)
- [FAQPage structured data — Google Search Central](https://developers.google.com/search/docs/appearance/structured-data/faqpage)
- [Digital Personal Data Protection Rules, 2025 (notified 13 Nov 2025) — PIB](https://static.pib.gov.in/WriteReadData/specificdocs/documents/2025/nov/doc20251117695301.pdf)
- [DPDP Act 2023 and DPDP Rules 2025: Compliance Guide — EY India](https://www.ey.com/en_in/insights/cybersecurity/decoding-the-digital-personal-data-protection-act-2023)
- [DPDP Implementation Status Tracker 2026 — CADP](https://cadp.in/resources/guides/dpdp-implementation-tracker/)
