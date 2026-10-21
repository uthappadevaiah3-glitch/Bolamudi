"""Homepage: index.html"""
import components as ui
import config as cfg


def service_card(slug, text):
    return ui.card(cfg.SERVICES[slug]['name'], text, href=ui.service_href(slug), cls='reveal')


strip = [
    ('land', 'Land aggregation', 'Parcel identification to registered conveyance'),
    ('liaison', 'Government liaison', 'District, state and utility interface'),
    ('approvals', 'Statutory approvals', 'Consent to establish through commissioning'),
    ('transmission', 'Transmission RoW', 'Corridor alignment and landowner settlement'),
]

cards = [
    service_card('land-aggregation', 'Parcel identification, ownership verification, revenue-record diligence, landowner negotiation, aggregation across fragmented holdings, and registered conveyance or lease.'),
    service_card('government-liaison', 'Sustained interface with district administration, revenue and survey departments, state nodal agencies, KREDL, KPTCL and pollution control boards.'),
    service_card('statutory-approvals', 'Land conversion, NA permissions, consent to establish and operate, forest and environmental referrals, local body NOCs, and approval sequencing.'),
    service_card('transmission-row', 'Corridor assessment, route optimisation against land holdings, RoW negotiation, crop and structure compensation, and access arrangements.'),
    ui.card('Renewable project facilitation', 'Site suitability, resource-adjacent land banking, and coordination across solar, wind, hybrid and pumped storage development.', href='services.html', cls='reveal'),
    service_card('project-development-support', 'Documentation, due-diligence packs for lenders and acquirers, land schedules, and ongoing support through construction.'),
]

approvals = [
    ('District &amp; revenue', ['Land conversion (<abbr title="Non-Agricultural">NA</abbr>)', 'Tenancy and land-ceiling checks', 'Mutation and khata transfer', 'Village panchayat NOC', 'Revenue survey and sketch']),
    ('State &amp; regulatory', ['<abbr title="Karnataka Renewable Energy Development Ltd">KREDL</abbr> registration', '<abbr title="Karnataka Electricity Regulatory Commission">KERC</abbr> approvals', 'Pollution control board <abbr title="Consent for Establishment">CFE</abbr>/<abbr title="Consent for Operation">CFO</abbr>', 'Fire and factories NOC', 'Forest and wildlife referrals', 'Groundwater clearance']),
    ('Utility &amp; transmission', ['<abbr title="Karnataka Power Transmission Corporation Ltd">KPTCL</abbr>/<abbr title="Central Transmission Utility">CTU</abbr> connectivity', 'Evacuation approval', 'Bay allotment', 'Right of way approvals', 'Crossing permissions', 'Charging and commissioning clearance']),
]

audiences = [
    ('Renewable energy developers', 'Land and clearance execution for projects under active development, from feasibility through construction.'),
    ('Independent power producers', 'Sustained land and regulatory support across a portfolio, in one state, with one accountable team.'),
    ('Infrastructure &amp; EPC contractors', 'Right of way, access, and local clearance support during execution, where delay is measured in daily cost.'),
    ('Investors &amp; diligence teams', 'Independent land and approval diligence on assets under acquisition, including title-risk assessment.'),
]

reasons = [
    ('Single-state specialisation', 'We work only in Karnataka. Land procedure, revenue practice and local body process are state and district specific, and we have chosen depth over geographic spread.'),
    ('Development-side experience', 'Our practice is built from two decades inside the execution of utility-scale solar, wind, hybrid and pumped storage projects — not from advisory observation of them.'),
    ('Continuity from screening to commissioning', 'The team that assesses feasibility stays through conveyance, clearance and right of way. Nothing is handed to a new party at the point where context matters most.'),
    ('Documented, auditable process', 'Every mandate produces a documented land and approvals record suitable for lender, auditor and acquirer review.'),
]

facts = [
    ('Experience', '20+ years, utility-scale renewable development'),
    ('Asset Classes', 'Solar, wind, hybrid, pumped storage'),
    ('Functions', 'Land, liaison, statutory approvals, transmission RoW'),
    ('Geography', 'Karnataka, district-level'),
]

questions = [
    ('Do you work outside Karnataka?', 'No. Land procedure, revenue practice and local body process are state-specific, and our value is district-level depth in one state. We would rather decline work than dilute that.'),
    ('Do you acquire land on your own account?', 'No. We act for the developer, not as a principal. We are not paid by landowners and we hold no positions in land we aggregate.'),
    ('At what stage should we engage you?', 'At site screening, before commercial commitment. Most expensive land and approval errors are made before a specialist is in the room. A short pre-acquisition assessment costs days and can save quarters.'),
    ('How long do statutory approvals take in Karnataka?', 'It depends on capacity, land classification, district and connectivity route — which is exactly why fixed quotes from anyone should concern you. We provide indicative ranges per approval category against your specific project, with the dependencies stated.'),
    ('How do you charge?', 'Retainer, milestone and success-fee structures, sized against scope rather than time. Commercial terms are discussed against a specific site and a specific timeline — we do not quote development support against a brief.'),
    ('Can you support due diligence on an asset we are acquiring?', "Yes, as an independent scope: land and approval diligence including title-risk assessment, delivered in a format your lender's counsel can audit."),
    ('How do you handle landowner negotiation?', "Fair, transparent, documented dealing at village level. Every acre acquired badly becomes a litigation, an agitation or a stalled tower three years later — and it becomes the developer's problem. We treat the landowner as a stakeholder, not an obstacle."),
    ('What do you need from us to begin?', 'The district, the technology, the stage you are at, and — if you have one — the polygon or survey numbers under consideration. That is enough for a first read.'),
]

body = f'''
<!-- 01 HERO -->
<div class="hero photo"{ui.bg('solar-plant.jpg')}>
  <div class="wrap">
    <p class="eyebrow">Karnataka · Renewable Energy Project Development</p>
    <h1>Land and approvals, resolved before they become the critical path.</h1>
    <p class="lead">Bolamudi Energy secures land, statutory clearances and transmission right of way for utility-scale solar, wind, hybrid and pumped storage projects across Karnataka — led by two decades of on-ground execution.</p>
    {ui.btns(ui.btn('Request a consultation', 'contact.html'), ui.btn('How we work', '#approach', 'ghost'))}
    <p class="micro-strip">LAND AGGREGATION · GOVERNMENT LIAISON · STATUTORY APPROVALS · TRANSMISSION ROW</p>
  </div>
</div>

<!-- 02 POSITIONING STRIP -->
<section class="tight">
  <div class="wrap">
    <ul class="strip4 bare">
      {''.join(f'<li>{ui.icon(i)}<h4>{t}</h4><p>{d}</p></li>' for i, t, d in strip)}
    </ul>
  </div>
</section>

<!-- 03 THE BOTTLENECK -->
<section class="surf bleed">
  <div class="wrap g75">
    <div class="reveal">
      <p class="eyebrow">The Development Bottleneck</p>
      <h2>Projects are rarely lost on engineering.</h2>
      <p class="mt-20">Module supply, EPC capability and financing are competitive markets with known solutions. Land and statutory clearance are not. In Karnataka they are local, sequential, and unforgiving of assumptions made from a head office in Bengaluru, Mumbai or Delhi.</p>
      <p class="mt-14">A single unresolved tenancy claim, an unconverted survey number, or a right of way alignment that crosses one uncooperative holding can move commissioning by two quarters. The cost is not the land. The cost is the schedule.</p>
      <ol class="bare mt-32">
        {ui.numbered([
            ('Title that does not survive diligence', 'Fragmented holdings, unrecorded inheritance, tenancy entries and land-ceiling restrictions surface late, after commercial terms are agreed.'),
            ('Approvals treated as parallel when they are sequential', 'Clearances have dependency chains. Applying in the wrong order can cost an entire season.'),
            ('Right of way negotiated after the route is fixed', 'Corridor decisions taken on a map without landowner sequencing create hold-outs with maximum leverage.'),
        ], tag='li', hide_idx=True)}
      </ol>
    </div>
    <figure class="bleed-img">{ui.img('land-parcel.jpg')}<p class="tag">Parcel boundary · before acquisition</p></figure>
  </div>
</section>

<!-- 04 SERVICES -->
<section>
  <div class="wrap">
    {ui.sec_head('Capabilities', 'What we take off your critical path', 'Six areas of practice, delivered as one continuous mandate or engaged individually.', cls='center reveal')}
    <ul class="grid3 bare">
      {''.join(f'<li>{c}</li>' for c in cards)}
    </ul>
  </div>
</section>

<!-- 05 LIFECYCLE -->
<section class="dark" id="approach">
  <div class="wrap">
    {ui.sec_head('Our Approach', 'A sequence, not a service list', 'Land and approvals fail when they are run in parallel by parties who do not talk to each other. We run them as one dependency-ordered programme.', lead_cls='mt-16', cls='reveal')}
    {ui.timeline(cfg.DEV_SEQUENCE)}
    {ui.btns(ui.btn('Read our approach in detail', 'about.html#lifecycle', 'ghost'))}
  </div>
</section>

<!-- 06 KARNATAKA -->
<section>
  <div class="wrap g57">
    <div class="reveal">
      <p class="eyebrow">Where We Operate</p>
      <h2>Karnataka, district by district</h2>
      <p class="muted mt-18">Land practice does not generalise across state lines, and barely generalises across districts. Revenue procedure, land classification, tenancy history and local body process differ enough that experience earned in one district is only partially transferable to the next. Our work is concentrated in the state's high-resource corridors.</p>
      <hr class="gold-rule">
      <p class="eyebrow mb-10">Resource Corridors</p>
      <p class="muted fs-15"><strong>WIND</strong> — Chitradurga, Gadag, Koppal, Davanagere<br><strong>SOLAR</strong> — Tumakuru, Ballari, Vijayapura, Kalaburagi<br><strong>PSP</strong> — Western Ghats fringe</p>
      {ui.btns(ui.btn('Explore our Karnataka coverage', 'karnataka.html', 'ghost'))}
    </div>
    {ui.fig('karnataka-map.svg', 'reveal contain')}
  </div>
</section>

<!-- 07 STATUTORY APPROVALS -->
<section class="surf">
  <div class="wrap">
    {ui.sec_head('Statutory Scope', 'Thirty-plus clearances. One dependency chain.', 'A utility-scale renewable project in Karnataka passes through district administration, multiple state departments, the transmission utility and central agencies. The approvals are not independent, and the order in which they are filed determines the schedule.', lead_cls='muted mt-16', cls='reveal')}
    <div class="grid3">
      {''.join(ui.panel(t, items, cls='reveal') for t, items in approvals)}
    </div>
    <div class="dl-band reveal">
      <div><h4>Karnataka renewable approvals — a practitioner's guide</h4><p>A structured walkthrough of the full clearance chain.</p></div>
      {ui.btn('Download the guide', 'contact.html', 'onwhite')}
    </div>
    <p class="review-stamp">Last reviewed: August 2026</p>
  </div>
</section>

<!-- 08 AUDIENCES -->
<section>
  <div class="wrap">
    {ui.sec_head('Who We Work With', 'Built for the parties who carry schedule risk', cls='reveal')}
    <ul class="grid4 bare">
      {''.join(ui.card(t, d, tag='li', cls='quiet reveal', title_cls='fs-17') for t, d in audiences)}
    </ul>
  </div>
</section>

<!-- 09 WHY BOLAMUDI -->
<section class="surf">
  <div class="wrap g57">
    <div class="reveal">
      <p class="eyebrow">Why Bolamudi</p>
      <h2>Depth in one state, not presence in twenty</h2>
      <p class="muted mt-18">Every point below is a statement of fact or method — never a quality.</p>
      {ui.btns(ui.btn('Request a consultation', 'contact.html'))}
    </div>
    <div class="reveal">
      {ui.numbered(reasons, hide_idx=True)}
    </div>
  </div>
</section>

<!-- 10 LEADERSHIP -->
<section>
  <div class="wrap g57">
    <div class="reveal">
      <div class="lockup-box">
        <img src="logo-lockup.png" alt="{cfg.COMPANY}">
      </div>
    </div>
    <div class="reveal">
      <p class="eyebrow">Leadership</p>
      <h2>Two decades of Karnataka execution</h2>
      <h3 class="mt-20">Founder &amp; Managing Partner</h3>
      <p class="muted mt-14">The practice is built on twenty years spent inside the execution of utility-scale renewable projects with one of India's largest renewable energy developers — across land, liaison, statutory approvals and transmission right of way, at district level, throughout Karnataka.</p>
      <p class="muted mt-12">Bolamudi Energy was founded to offer that execution capability directly to developers, IPPs and investors who carry schedule risk in this state.</p>
      <hr class="gold-rule">
      <div class="grid2 facts">
        {''.join(f'<div><p class="eyebrow">{k}</p><p class="muted fs-15">{v}</p></div>' for k, v in facts)}
      </div>
    </div>
  </div>
</section>

<!-- 11 GOVERNANCE -->
<section class="dark tight">
  <div class="wrap gov-band reveal">
    <p class="eyebrow">Governance &amp; Conduct</p>
    <h3 class="fs-26">Liaison, conducted on the record</h3>
    <p class="mt-16">Our work with government departments is procedural: applications correctly prepared, filed in the right sequence, and followed through official channels. Every mandate is documented to a standard that withstands lender, auditor and acquirer review. We do not undertake work that cannot be recorded.</p>
    <p class="mt-16"><a href="about.html#principles">Read our operating principles →</a></p>
  </div>
</section>

<!-- 13 FAQ -->
<section class="surf">
  <div class="wrap g57">
    <div class="reveal">
      <p class="eyebrow">FAQ</p>
      <h2>Common questions</h2>
      <p class="muted mt-14">Direct answers to the questions we are asked before engagement.</p>
      <p class="mt-16"><a href="contact.html">Ask a different question →</a></p>
    </div>
    <div class="reveal">
      {ui.faq(questions)}
    </div>
  </div>
</section>

<!-- 14 CONVERSION -->
<section class="darker" id="contact">
  <div class="wrap g57">
    <div class="reveal">
      <h2>Start with a conversation about your site</h2>
      <p class="mt-18">Tell us the district, the technology and the stage you are at. We will tell you what the land and approval path looks like, and whether we are the right party for it.</p>
      <hr class="gold-rule">
      {ui.contact_lines()}
    </div>
    <div class="reveal">
      {ui.enquiry_form(f'I consent to {cfg.COMPANY} contacting me about this enquiry.')}
    </div>
  </div>
</section>
'''

PAGES = {'index.html': ui.page(
    f'{cfg.COMPANY} — Land, Approvals &amp; Right of Way for Renewable Projects in Karnataka',
    'Bolamudi Energy secures land, statutory clearances and transmission right of way for utility-scale solar, wind, hybrid and pumped storage projects across Karnataka.',
    body, nav='index.html')}
