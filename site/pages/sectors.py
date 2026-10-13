"""Sectors: sectors.html"""
import components as ui

# (sector, photo, tagline, paragraphs, linked service, link label)
sectors = [
    ('Solar', 'solar-plant-2.jpg', '4&ndash;5 acres per MW &mdash; contiguity matters more than price', [
        'A utility-scale solar project is a land-assembly problem before it is an engineering problem. The active belts &mdash; Pavagada, Koppal, Gadag, Bagalkot, Vijayapura, Ballari &mdash; have fragmented holdings and steadily rising expectations. Contiguity, not rate, is the binding constraint: a cheap non-contiguous polygon costs more in cabling, land loss and evacuation distance than the saving. Rising guidance values and the seven-year transfer restriction on land acquired under Section 109 make acquisition sequencing a commercial decision, not an administrative one.'],
     'land-aggregation', 'Land aggregation for solar'),
    ('Wind', 'wind-farmland.jpg', 'Small footprints, hard access &mdash; the crane path is the real land problem', [
        'The turbine footprint is small; everything around it is not. Ridge-line micro-siting drives WTG positions, and the land you actually need is the access road, the crane pad and the internal line corridor &mdash; often across owners who see no turbine on their land and no reason to agree. Chitradurga, Gadag, Davanagere, Haveri, Koppal and Belagavi each behave differently. Repowering adds a second problem: legacy land arrangements from the 2000s that were never documented to today&rsquo;s standard.'],
     'transmission-row', 'Right of way for wind corridors'),
    ('Hybrid', 'wind-ridge.jpg', 'Two resource regimes, one land polygon, one evacuation point', [
        'Hybrid projects are attractive because they raise CUF against a single evacuation asset. They are hard because the land has to satisfy two resource regimes at once. Turbine footprints, crane paths and array blocks must coexist on the same polygon, which raises the contiguity requirement sharply &mdash; you cannot substitute a distant parcel. Land aggregation for hybrid should be planned against the combined layout from the start, not solved twice.'],
     'statutory-approvals', 'Approvals for hybrid projects'),
    ('Pumped storage', 'sharavathi.jpg', 'Head differential, geotechnics and forest overlap, screened before the DPR', [
        'Pumped storage is the longest and least forgiving development cycle we work on. A viable site needs 200&ndash;600&nbsp;m of head differential between two reservoir locations at a workable horizontal distance, with geotechnics that support the waterway and powerhouse. In Karnataka, the sites that satisfy the topography frequently sit in or near ecologically sensitive Western Ghats terrain &mdash; and environmental and forest overlap must be screened as a first-order filter, not discovered after DPR spend. Land is typically a mix of revenue, forest and private holdings, each on a different legal track. Central Electricity Authority DPR concurrence sits on the critical path throughout.',
        '<strong>Water allocation.</strong> No pumped storage project in Karnataka moves without a water allocation from the Government of Karnataka, processed through the Water Resources (irrigation) Department and the nigam that controls the source &mdash; Krishna Bhagya Jala Nigam, Karnataka Neeravari Nigam, Cauvery Neeravari Nigam or Visvesvaraya Jala Nigam. A PSP recirculates water rather than consuming it, so the allocation covers the one-time initial fill and annual make-up for evaporation and transit losses &mdash; of the order of 1&nbsp;TMC for a gigawatt-scale scheme. Where an existing irrigation reservoir is proposed as the lower reservoir, the department will protect irrigation and drinking-water commitments first, and its conditions can change the reservoir design itself. We build the water-availability case, run the interface with the irrigation department and the nigam, and track the allocation order alongside land and forest clearance.'],
     'project-development-support', 'Development support for PSP'),
]


def sector_panel(name, photo, tagline, paragraphs, service, link):
    text = ''.join(f'<p class="{ui.classes("muted fs-15", "mt-12" if i else "")}">{p}</p>' for i, p in enumerate(paragraphs))
    more = f'<p class="mt-16"><a href="{ui.service_href(service)}">{link} &rarr;</a></p>'
    return ui.panel(name, top=ui.fig(photo), body=f'<p class="eyebrow">{tagline}</p>{text}{more}')


body = ui.page_head(
    'Sectors', 'Four technologies. Four different land problems.',
    'What we deliver is the same in every sector. What makes it hard is not. A sector section never explains a service &mdash; it explains the terrain.') + f'''
<section>
  <div class="wrap">
    <div class="grid2">
      {''.join(sector_panel(*s) for s in sectors)}
    </div>
  </div>
</section>
''' + ui.CTA

PAGES = {'sectors.html': ui.page(
    ui.titled('Sectors'),
    'Solar, wind, hybrid and pumped storage — what makes each hard in Karnataka, and how the land problem differs.',
    body, nav='sectors.html')}
