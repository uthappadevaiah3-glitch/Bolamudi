"""About: about.html"""
import components as ui

stats = [
    ('20+', 'Years in utility-scale renewable project execution'),
    ('4', 'Asset classes &mdash; Solar, Wind, Hybrid, Pumped Storage'),
    ('Karnataka', 'Statewide revenue district and DISCOM coverage'),
    ('Pre-construction', 'Full scope &mdash; land, approvals, evacuation, right of way'),
]

not_list = [
    ('Not an EPC contractor', 'We do not construct or procure.'),
    ('Not a technical or DPR consultant', 'We do not size plants, model yield or prepare engineering reports.'),
    ('Not a land broker', 'We are retained by the developer, we are not paid by the landowner, and we do not hold positions in land we aggregate.'),
]

domain = [
    ('Land aggregation &amp; title', 'Aggregation is a title problem before it is a negotiation problem.', [
        'Village-level identification and survey-number-wise feasibility screening',
        'RTC, mutation register and encumbrance chain verification',
        'Joint measurement and boundary reconciliation with survey authorities',
        'Structuring for purchase, long-lease and hybrid tenure',
        'Section 109 exemption route under the Karnataka Land Reforms Act, 1961',
        'Ceiling-limit and non-agriculturist acquisition constraints',
        'Seven-year transfer restriction and its effect on downstream project sale',
        'Gomala, government and inam land classification and grant pathways']),
    ('Land use &amp; statutory approvals', 'Approvals are sequence-dependent. Filing in the wrong order costs quarters.', [
        'Conversion and land-use position, including the deemed and automatic conversion route under the Karnataka Land Revenue (Amendment) Rules, 2025',
        'KREDL registration, scrutiny and the SLAC allotment route',
        'Incentive and reimbursement claims under the Karnataka Renewable Energy Policy 2022&ndash;27',
        'District administration and Deputy Commissioner office liaison',
        'Single-window and Udyog Mitra coordination where applicable',
        'Forest, environmental and wildlife clearance interfaces, including compensatory afforestation land, where the site demands it',
        'Panchayat, local body and NOC coordination']),
    ('Evacuation &amp; grid connectivity', 'A project without a confirmed bay is a project without a date.', [
        'Evacuation scheme application and approval through KPTCL',
        'Substation and bay availability assessment prior to land commitment',
        'ESCOM interface &mdash; BESCOM, HESCOM, GESCOM, MESCOM, CESC',
        'Intra-state and ISTS connectivity coordination and long-term access',
        'Interconnection and metering point coordination with the developer&rsquo;s technical team']),
    ('Transmission right of way', 'The corridor is negotiated parcel by parcel, not corridor by corridor.', [
        'Route optimisation against land cost, crop pattern and habitation',
        'Tower footing and corridor consent from individual landowners',
        'Crop and structure compensation assessment and settlement',
        'Objection handling and district administration escalation',
        'Sequencing RoW against the construction and stringing programme']),
]

LED, SUPPORTED = '&#9679; Led', '&#9675; Supported'
lifecycle = [
    ('Site identification', 'Terrain, resource, access and evacuation proximity screening', SUPPORTED),
    ('Land aggregation', 'Title verification, owner negotiation, consolidation', LED),
    ('Land use &amp; exemption', 'Conversion position, Section 109 exemption, tenure structuring', LED),
    ('Statutory approvals', 'KREDL, SLAC, district administration, sectoral clearances', LED),
    ('Evacuation &amp; connectivity', 'KPTCL scheme approval, bay allocation, ESCOM interface', LED),
    ('Transmission right of way', 'Corridor consent, compensation, objection resolution', LED),
    ('Construction &amp; COD', 'Continuity support, residual approvals, local interface', SUPPORTED),
]

statements = [
    ('On why this practice exists', 'Twenty years of executing utility-scale solar, wind, hybrid and pumped storage projects in Karnataka have taught us one thing repeatedly: the difference between a project that commissions on schedule and one that slips two years is almost never engineering. It is land, statute and relationships, handled early and handled properly.'),
    ('On how the work is done', 'Development support is not a document exercise. It is field work &mdash; village visits, survey records, taluk offices, individual landowners, and the same officials over years rather than weeks. It cannot be delegated to someone learning it on your project. Every engagement is led personally by our senior team.'),
    ('On what we will not do', 'We will not commit to an aggregation timeline before title and owner consent have been tested on the ground. We will not report a statutory position we have not confirmed at source. A developer who is told the truth late has lost a year; a developer who is told the truth early has lost a week.'),
]

principles = [
    ('Verified before reported.', 'No status reaches a client that has not been confirmed at source. We do not relay assurances we have not tested.'),
    ('Land first, promises second.', 'No aggregation timeline is committed until title and owner consent have been tested in the field. Optimistic land schedules are the most expensive error in Indian renewable development.'),
    ('The landowner is a stakeholder, not an obstacle.', 'Fair, transparent, documented dealing at village level. Every acre acquired badly becomes a litigation, an agitation or a stalled tower three years later.'),
    ('Compliance over speed.', 'We will not take a route that clears a file faster and leaves a title or statutory defect behind. Defects surface at diligence, refinancing or sale, when they cost the most.'),
    ('One principal, one accountable owner.', 'The person who assessed your site is the person in the taluk office and the person on your call. No handoffs, no account-management layer.'),
]

reasons = [
    ('Against a large consultancy', 'Large firms sell with partners and deliver with associates. On development support, the value is entirely in the relationships and the field knowledge of the person actually doing it. Here, the person who sells the work is the person who does the work.'),
    ('Against an in-house team', 'An internal development team is built for a pipeline, not a project. For a developer entering Karnataka, or running one or two assets here, twenty years of district-level relationships cannot be hired in a quarter and cannot be justified as permanent overhead.'),
    ('Against a local aggregator', 'A land aggregator solves land and stops. Land solved in isolation from evacuation, statutory sequence and right of way produces a site you own and cannot build on. The stages are interdependent and are handled here as one scope.'),
]

engagements = [
    ('Pre-acquisition assessment', 'A bounded, short-duration review before you commit capital to a site.', [
        'Evacuation and bay availability check', 'Title and classification screening across the target survey numbers',
        'Statutory pathway and realistic timeline', 'Go / no-go position']),
    ('Stage mandate', 'Retained for a defined stage &mdash; land, approvals, evacuation or right of way.', [
        'Defined deliverable and completion criteria', 'Fixed reporting cadence', 'Priced against scope, not time']),
    ('Full development support', 'Retained from site identification to construction-ready handover.', [
        'All stages 02&ndash;06 of the development lifecycle', 'Single accountable point of contact',
        'Continuous status file held with the client']),
]

body = ui.page_head(
    'About Bolamudi Energy', "Two decades inside Karnataka's renewable energy development machinery.",
    'Bolamudi Energy is a project development support firm. We handle the land, statutory and liaison work that decides whether a sanctioned renewable project reaches construction &mdash; and when.',
    'wind-ridge.jpg') + f'''
<section class="tight">
  <div class="wrap">
    <div class="stats">
      {''.join(f'<div><div class="big">{n}</div><p>{t}</p></div>' for n, t in stats)}
    </div>
  </div>
</section>
<section>
  <div class="wrap g57">
    <div>
      <p class="eyebrow">01 &mdash; The Position</p>
      <h2>We occupy the stage most developers underestimate.</h2>
    </div>
    <div class="prose">
      <p>A utility-scale renewable project rarely fails on technology. It fails, or slips by eighteen months, in the pre-construction stage &mdash; where land title is imperfect, where a statutory file sits unmoved on a desk, where an evacuation approval is contingent on a bay that has already been allocated, where a transmission corridor crosses forty parcels and thirty-nine owners agree.</p>
      <p>That stage is our entire practice. We do not build, and we do not advise on what to build. We take a project from allocation to a construction-ready position: land consolidated and clean, approvals held, evacuation secured, corridor cleared.</p>
      <div class="notlist mt-32">
        {''.join(ui.row(text, title) for title, text in not_list)}
      </div>
    </div>
  </div>
</section>
<section class="surf">
  <div class="wrap">
    {ui.sec_head('02 &mdash; Domain Command', 'The work, stated precisely.', 'Development support is a term wide enough to mean nothing. Below is what it means here &mdash; the specific instruments, authorities and procedures we work through in Karnataka.')}
    <div class="grid2">
      {''.join(ui.panel(t, items, intro) for t, intro, items in domain)}
    </div>
  </div>
</section>
<section id="lifecycle">
  <div class="wrap">
    {ui.sec_head('03 &mdash; The Development Lifecycle', 'Where we lead, and where we support.')}
    {ui.table(['#', 'Stage', 'Description', 'Role'],
              [(f'{i:02d}', f'<strong>{s}</strong>', d, r) for i, (s, d, r) in enumerate(lifecycle, 1)])}
  </div>
</section>
<section class="dark">
  <div class="wrap g57">
    <div>
      <p class="eyebrow">04 &mdash; Leadership</p>
      <h2>Founder &amp; Principal</h2>
      <p class="mt-16 fs-15">Every engagement here is led personally by the principal.</p>
    </div>
    <div>
      {''.join(ui.row(text, idx=label, cls='statement') for label, text in statements)}
    </div>
  </div>
</section>
<section id="principles">
  <div class="wrap">
    {ui.sec_head('Operating Principles', 'Five commitments, stated plainly.')}
    <div class="grid2 loose">
      {ui.numbered(principles)}
    </div>
  </div>
</section>
<section class="surf">
  <div class="wrap">
    {ui.sec_head('05 &mdash; Why Bolamudi', 'Three honest reasons, and one honest answer.')}
    <div class="grid3">
      {''.join(ui.card(t, d, title_cls='fs-18') for t, d in reasons)}
    </div>
    <div class="w-760 mt-56">
      <p class="eyebrow">On continuity and single-principal risk</p>
      <p class="muted">The reasonable question about a principal-led practice is what happens if the principal is unavailable or already committed. We answer it directly rather than leave it unasked. Engagements are accepted against declared capacity &mdash; if a project cannot be given proper attention in the window you need, we say so before contracting rather than after. Field execution is supported by an established network of district-level associates who have worked with us for years, under our direction and our accountability. Every engagement maintains a documented file &mdash; title chain, application status, authority correspondence, contact map &mdash; held with the client, so that project knowledge sits with your organisation and not only in our heads.</p>
    </div>
  </div>
</section>
<section>
  <div class="wrap">
    {ui.sec_head('06 &mdash; How We Engage', 'Three ways engagements are structured.')}
    <div class="grid3">
      {''.join(ui.panel(t, items, intro) for t, intro, items in engagements)}
    </div>
    <p class="muted mt-32 italic">Commercial terms are discussed against a specific site and a specific timeline. We do not quote development support against a brief.</p>
  </div>
</section>
''' + ui.CTA

PAGES = {'about.html': ui.page(
    ui.titled('About'),
    'Two decades inside Karnataka renewable energy development. Land, statutory and liaison work that decides whether a sanctioned project reaches construction.',
    body, nav='about.html')}
