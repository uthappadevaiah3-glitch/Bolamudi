"""The five service detail pages: services-<key>.html. One template, five sets of content.

Names, taglines, header photos and the previous/next order come from SERVICES in config.py.
"""
import components as ui
import config as cfg


PAGER_LABELS = {'prev': '<span aria-hidden="true">&larr;</span> Previous service',
                'next': 'Next service <span aria-hidden="true">&rarr;</span>'}


def pager_link(slug, direction):
    if slug is None:  # first service has no previous, last has no next
        return ''
    s = cfg.SERVICES[slug]
    return (f'<a class="pager-link {direction}" href="{ui.service_href(slug)}" rel="{direction}">'
            f'<span class="pager-dir">{PAGER_LABELS[direction]}</span><span class="pager-title">{s["title"]}</span>'
            f'<span class="pager-sub">{s["tagline"]}</span></a>')


def pager(slug):
    """Previous / next service in config order (no wrap-around), with a link back to all services."""
    keys = list(cfg.SERVICES)
    i = keys.index(slug)
    prev = keys[i - 1] if i > 0 else None
    nxt = keys[i + 1] if i + 1 < len(keys) else None
    return f'''<nav class="pager" aria-label="More services">
  <div class="wrap">
    {pager_link(prev, 'prev')}
    {pager_link(nxt, 'next')}
    <a class="pager-all" href="services.html">All services &middot; {i + 1:02d} of {len(keys):02d}</a>
  </div>
</nav>'''


def service_page(slug, card_line, problem, solution, process, deliverables, cta_title, cta_body):
    s = cfg.SERVICES[slug]
    rows = [(ui.chip(f'{i:02d}'), f'<strong>{stage}</strong>', what) for i, (stage, what) in enumerate(process, 1)]
    crumb = f'<a href="services.html">Services</a> / {s["title"]}'
    body = ui.page_head(crumb, s['title'], s['tagline'], s['photo']) + f'''
<section>
  <div class="wrap g57">
    <div>
      <p class="eyebrow">The Problem</p>
      <h2 class="fs-30">{card_line}</h2>
    </div>
    <div class="prose">{problem}</div>
  </div>
</section>
<section class="surf">
  <div class="wrap g57">
    <div><p class="eyebrow">Our Response</p><h2 class="fs-30">How we run it</h2></div>
    <div class="prose">{solution}</div>
  </div>
</section>
<section>
  <div class="wrap">
    {ui.sec_head('Process', 'Stage by stage')}
    {ui.table(['#', 'Stage', 'What happens'], rows)}
  </div>
</section>
<section class="surf">
  <div class="wrap">
    {ui.sec_head('Deliverables', 'What you hold at the end')}
    <div class="grid2">{''.join(deliverables)}</div>
  </div>
</section>
{pager(slug)}
''' + ui.cta_band(cta_title, cta_body, [ui.btn('Start the conversation', 'contact.html', 'onwhite')], width='w-720', gap='mt-16')
    return {ui.service_href(slug): ui.page(ui.titled(s['title']), s['tagline'], body, nav='services.html')}


PAGES = {}

PAGES |= service_page(
    'land-aggregation',
    'Projects don&rsquo;t fail on the last parcel. They fail on the parcel nobody checked properly.',
    '''<p>A 300&nbsp;MW solar project needs roughly 1,200 to 1,500 acres. In Karnataka that is almost never one seller. It is 80 to 200 khatedars across four or five villages, with fragmented holdings, undivided family shares, minors&rsquo; interests, tenancy exposure, grant and inam restrictions, and RTC entries that do not match who is actually farming the land.</p>
<p>Most developers discover this in the wrong order. Parcels are tied up on the strength of a broker&rsquo;s assurance, advances are paid, and the title problem surfaces during lender due diligence &mdash; eight weeks before financial close, when the cost of a gap in the chain is the entire drawdown schedule.</p>
<p>The second failure is geometric. Parcels get bought where they are available, not where the array needs them, and the project ends up with a polygon it cannot build on efficiently or evacuate from economically.</p>
<h3>Failure modes we are hired to prevent</h3>
<ul><li>A 30-year title flow with an unresolved partition or an unrecorded mutation</li>
<li>Hold-out parcels sitting inside the array boundary, discovered after 80% acquisition</li>
<li>Land tied up at a price set before anyone benchmarked guidance value</li>
<li>Land-use conversion started after registration instead of before</li>
<li>A land file that a lender&rsquo;s counsel cannot audit</li></ul>''',
    '''<p>We assemble contiguous, encumbrance-free, connectivity-viable land and hand it over in a condition that survives lender diligence. Title is verified before money moves, not after.</p>
<p>Every parcel enters a register at first contact and stays in it through registration, khata and mutation &mdash; so at any point in the mandate you can see exactly which survey numbers are clean, which are consented, which are executed and which are at risk.</p>''',
    [('Site screening &amp; terrain assessment', 'Polygon shortlisting against resource, slope, evacuation distance, forest and wildlife buffers, water bodies, habitations and existing infrastructure.'),
     ('Survey number mapping', 'Village cadastral overlay; Bhoomi RTC pull for every survey number in the polygon; tippan/Mojini sketch reconciled to ground.'),
     ('Title due diligence', '30-year title chain, encumbrance certificate, mutation register chain, partition status, minors&rsquo; interest, PTCL / inam / grant restrictions, tenancy exposure. Conducted with empanelled counsel.'),
     ('Owner engagement &amp; rate discovery', 'Village-level engagement, guidance value versus prevailing market benchmarking, consent mapping, early identification of hold-out risk inside the array boundary.'),
     ('Agreement execution', 'Registered Agreement to Sale or lease deed, power of attorney where appropriate, advance schedule tied to documentary milestones.'),
     ('Statutory pathway', 'Conversion via the Deputy Commissioner, or the automatic conversion route available to renewable energy projects under the 2025 Land Revenue Rules &mdash; sequenced before registration, not after.'),
     ('Compensatory afforestation land', 'Where the project diverts forest land, the developer must provide an equal extent of non-forest land for compensatory afforestation, handed to the Forest Department free of encumbrances and notified as protected forest before final forest approval. We identify suitable blocks &mdash; ten hectares or more, ideally twenty-five or more to avoid the small-block surcharge &mdash; verify title, aggregate them and complete transfer and mutation to the Forest Department, on the same register as the project land.'),
     ('Registration &amp; mutation', 'Sub-registrar execution, khata transfer, mutation into the SPV&rsquo;s name, updated RTC reflecting the project entity.'),
     ('Handover', 'Consolidated land dossier issued to developer and lender in audit format.')],
    [ui.panel(f'Spatial {ui.chip("SHP / KML / PDF")}', [
        'Village-wise project polygon with survey-number-level GIS layer',
        'Array-boundary overlay showing acquired, consented, in-progress and at-risk parcels']),
     ui.panel(f'Register &amp; diligence {ui.chip("XLSX / PDF")}', [
        'Parcel register &mdash; survey number, extent, khatedar, RTC status, encumbrance, consent, execution status',
        '30-year title opinion pack per parcel',
        'Risk log for restricted, disputed and hold-out parcels']),
     ui.panel(f'Executed documents {ui.chip("PDF, lender format")}', [
        'Registered Agreements to Sale / lease deeds',
        'Conversion order from the Deputy Commissioner, or deemed-conversion acknowledgement',
        'Registered sale deeds, khata certificates and mutated RTCs in the SPV&rsquo;s name',
        'Compensatory afforestation land schedule, title pack and transfer to the Forest Department, where forest land is diverted',
        'Land Due Diligence Handover File'], cls='span-all')],
    'Send us your polygon or your capacity target.',
    'We&rsquo;ll return a land feasibility read &mdash; village coverage, likely title complexity, indicative rate band and aggregation risk &mdash; within 10 working days.')

PAGES |= service_page(
    'government-liaison',
    'Files don&rsquo;t get rejected. They wait &mdash; and your COD date moves with them.',
    '''<p>Approvals in Karnataka are rarely refused. They stall. A file reaches a desk with one annexure missing or one affidavit in the wrong format, a query is raised, and nobody is physically present to answer it. Two weeks become two months.</p>
<p>A developer&rsquo;s Bengaluru or Delhi team cannot sit in a Taluk office in Koppal for three weeks. So the file waits. Nobody is at fault, and the schedule slips anyway.</p>''',
    '''<p>We hold the file. Continuous, documented follow-through with Revenue (Deputy Commissioner, Assistant Commissioner, Tahsildar), the Energy Department, KREDL, KPTCL and the ESCOMs, KSPCB, Forest, Gram Panchayat and District Administration &mdash; with escalation through Karnataka Udyog Mitra and the single-window committees where the investment threshold allows.</p>
<p><strong>We do this through documentation, not influence.</strong> Every submission is a complete, compliant application file. Every step is recorded in a status register you can audit. If a file is stuck, you will know which desk, since when, and on what query.</p>''',
    [('Approval mapping', 'Department matrix built for your specific project type, capacity, land classification and district.'),
     ('File preparation', 'Annexure-complete applications assembled and pre-checked against the receiving officer&rsquo;s checklist, not a generic one.'),
     ('Submission &amp; acknowledgement', 'Physical and portal submission with dated acknowledgements captured for every filing.'),
     ('Departmental follow-through', 'Scheduled desk-level follow-up. Queries answered in writing within 72 hours of being raised.'),
     ('Committee representation', 'Representation through Karnataka Udyog Mitra &mdash; State Level Single Window Clearance Committee for &#8377;15&nbsp;Cr&ndash;&#8377;500&nbsp;Cr, State High Level Clearance Committee above &#8377;500&nbsp;Cr.'),
     ('Escalation', 'Defined escalation ladder with recorded dates, used when a file exceeds its statutory or normal timeline.'),
     ('Weekly status reporting', 'One register, one owner, one weekly report. Every open file, its desk, its age and its next action.')],
    [ui.panel('Registers', [
        'Project-specific approval matrix with department, officer level, statutory timeline and dependency',
        'Dated acknowledgement register', 'Query&ndash;response log with turnaround times',
        'Weekly status register &mdash; open files, desk, age, next action, risk flag']),
     ui.panel('Dossiers', [
        'Application dossiers for every filing, with annexure index',
        'Committee submissions, minutes and approval orders', 'Closure pack on completion'])],
    'Share your approval schedule. We&rsquo;ll mark where it will slip.',
    'Send your current department list and target dates. We&rsquo;ll return a marked-up matrix showing which items are mis-sequenced, which are missing, and which will not meet your COD.')

PAGES |= service_page(
    'statutory-approvals',
    'The approval list you&rsquo;re working from is probably wrong for your project.',
    '''<p>Approval checklists circulate as PDFs between developers. They are usually wrong for the specific case, because the requirement changes with capacity, land classification, district, distance to a forest boundary, whether you are ISTS or intra-state connected, and whether storage is involved.</p>
<p>The consequence is always the same and always late: a missing consent discovered at commissioning, when a CEIG charging approval or a KSPCB consent is the only thing standing between a built asset and first revenue.</p>''',
    '''<p>We build the statutory register for your project specifically &mdash; not from a template &mdash; and own every item in it from application through to the compliance calendar we hand you at the end.</p>
<p>Nothing is &ldquo;assumed applicable.&rdquo; Every item is either filed, closed as not applicable with a recorded reason, or flagged as at risk.</p>''',
    [('Statutory register build', 'Case-specific register derived from capacity, technology, land classification, district and connectivity route. Each item carries applicability reasoning.'),
     ('Pre-condition clearing', 'Khata, RTC correction and NOCs that are prerequisites to the main applications &mdash; cleared first, because filing out of sequence is the most common cause of rejection.'),
     ('Land use &amp; conversion', 'Conversion via the Deputy Commissioner or the automatic conversion route under the 2025 Land Revenue Rules. Notarised affidavits in Forms 21B/21C, RTC extracts, mutation register extracts, pre-conversion sketch, khata and master plan extract. 30-day deemed-approval clock tracked.'),
     ('Energy-side approvals', 'KREDL registration and commissioning formalities under the Karnataka Renewable Energy Policy 2022&ndash;27; KERC filings where applicable; KPTCL/ESCOM evacuation approval; CEIG charging approval.'),
     ('Environmental &amp; local', 'Consent to Establish and Consent to Operate; Forest and Wildlife clearances where the alignment or footprint requires; Gram Panchayat NOC; fire NOC where applicable.'),
     ('Grid-side', 'CTU Stage-I and Stage-II connectivity, GNA application within six months of Stage-II grant, and management of the connectivity bank guarantee &mdash; &#8377;10 lakh per MW for renewable generating stations &mdash; including validity tracking so it is never allowed to lapse.'),
     ('Compliance calendar handover', 'Every approval with its validity, renewal date, renewal lead time and responsible party.')],
    [ui.panel('Register &amp; filings', [
        'Project statutory register with applicability reasoning per item',
        'Filed application dossiers and dated acknowledgements',
        'Conversion order or deemed-conversion acknowledgement']),
     ui.panel('Approvals held', [
        'KREDL registration and commissioning documents', 'KSPCB Consent to Establish and Consent to Operate',
        'CEIG charging approval', 'Evacuation approval from KPTCL / ESCOM',
        'Connectivity and GNA grant letters, with bank guarantee validity tracker',
        'Compliance calendar with renewal dates and lead times'])],
    'Tell us the project. We&rsquo;ll tell you the actual list.',
    'Send capacity, district, land classification and connectivity route. We&rsquo;ll return the statutory register for that specific project &mdash; including the items that are commonly missed.')

PAGES |= service_page(
    'transmission-row',
    'One orchard in the middle of a 40&nbsp;km corridor can hold an entire commissioned project.',
    '''<p>Right of way is where good projects die quietly. The route is drawn in an office on a map. Then the line meets a village, a mango orchard, a borewell, or a landowner in the middle of a forty-kilometre corridor who has no reason to cooperate and every reason to wait.</p>
<p>Every week of RoW delay after mechanical completion is generation that is never sold. Unlike land acquisition, there is no alternative parcel &mdash; the corridor either clears or the asset sits idle.</p>
<p>The compounding error is sequence: routes are finalised before anyone walks them, so the corridor is legally fixed before its actual obstructions are known.</p>''',
    '''<p>We walk the corridor before it is finalised, and we clear it village by village. Route optimisation to design out the hardest crossings, landowner engagement ahead of survey rather than after, compensation determined under the Ministry of Power&rsquo;s June 2024 guidelines, and objections closed through the District Administration on record.</p>''',
    [('Corridor reconnaissance', 'Physical walk-down of the proposed alignment. Habitations, orchards, structures, borewells, water bodies, forest patches, existing line crossings and access constraints recorded span by span.'),
     ('Route optimisation', 'Alternative alignments modelled to minimise habitation and orchard crossings and rationalise angle points. Design changes here cost days; changes after finalisation cost months.'),
     ('Village-level engagement', 'Prior notice, Gram Panchayat briefing, and crop-season sequencing so survey and stringing avoid standing crops.'),
     ('Compensation determination', 'Under the Ministry of Power guidelines dated 14 June 2024, applicable to lines of 66&nbsp;kV and above: 200% of land value for the tower base area (including a one-metre extension on each side), and 30% of land value for the RoW corridor. Valuation on guidance/circle rate, or prevailing market rate where higher. Determined by the Deputy Commissioner; paid one-time and upfront.'),
     ('Objection handling', 'Objections recorded, verified on site, and resolved through the District Administration with a written trail.'),
     ('Disbursement &amp; documentation', 'Payment records, receipts and indemnities compiled per landowner and per span.'),
     ('Stringing support', 'Crop compensation, access track arrangement and on-ground escalation cover through the construction window.')],
    [ui.panel('Assessment', [
        'Corridor walk-down report with span-wise risk map',
        'Optimised route alignment with angle-point schedule and rationale for each deviation',
        'Landowner register per span &mdash; extent affected, tower base area, corridor area, contact and consent status']),
     ui.panel('Settlement', [
        'Compensation working per landowner, computed under the MoP 2024 guidelines',
        'Deputy Commissioner&rsquo;s compensation determination order',
        'Objection log with resolution status and dates', 'Disbursement records, receipts and indemnity documents',
        'Corridor clearance certificate pack'])],
    'Send us your line route. We&rsquo;ll walk it and report in three weeks.',
    'You&rsquo;ll get a span-wise risk map, an optimised alignment proposal, and an indicative compensation exposure under the current MoP guidelines.')

PAGES |= service_page(
    'project-development-support',
    'Slippage gets discovered in the review meeting, not before it.',
    '''<p>Between letter of award and financial close there are roughly two hundred open items across land, approvals, grid, EPC and lender conditions precedent. In most organisations these live in a spreadsheet that nobody owns, updated before review meetings rather than continuously.</p>
<p>The result is not that things go wrong. It is that they go wrong invisibly, and are discovered in the meeting where the schedule is being reported as on track.</p>''',
    '''<p>We run the Karnataka-side development desk: a single accountable interface for land, revenue, energy, grid and district matters, a live milestone register, and a weekly report that tells you what will slip before it slips &mdash; with the reason and the recovery option, not just the red flag.</p>''',
    [('Development baseline', 'Integrated schedule across land, statutory, grid, EPC and finance workstreams, with dependencies made explicit.'),
     ('Critical path &amp; CP mapping', 'Critical path identified, and lender conditions precedent mapped onto it so financing constraints are visible from week one.'),
     ('Weekly milestone register', 'Every milestone with owner, baseline date, forecast date and variance. Variance is reported the week it appears.'),
     ('Risk register', 'Named risks with owner, likelihood, schedule impact and mitigation. Reviewed weekly, not quarterly.'),
     ('Local interface management', 'District administration, Gram Panchayat, community, local vendors and site security handled as a standing responsibility rather than an escalation.'),
     ('Diligence support', 'Lender and investor data room populated and maintained, site visits coordinated, diligence queries answered from source documents.'),
     ('Construction handover', 'Structured handover to the EPC and O&amp;M interface with an open-items register and accountability transferred in writing.')],
    [ui.panel('Reporting', [
        'Integrated development schedule with dependency map',
        'Weekly status report &mdash; milestones, variance, risks, next actions',
        'Conditions precedent tracker mapped to the financing timetable',
        'Live risk register with owners and mitigations', 'Monthly steering pack for management and investors']),
     ui.panel('Diligence &amp; handover', [
        'Data room index and maintained document set', 'Diligence Q&amp;A log',
        'Site visit coordination and briefing packs', 'Construction handover file with open-items register'])],
    'Send us your development schedule. We&rsquo;ll return it marked up.',
    'We&rsquo;ll show you which items are on the critical path, which dependencies are mis-sequenced, and which will not hold.')
