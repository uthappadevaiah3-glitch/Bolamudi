"""Karnataka coverage: karnataka.html"""
import components as ui

legend = [
    ('Core Operating Districts', 'Where we work continuously and hold current ground knowledge.'),
    ('Active Coverage', 'Where we operate on project mandate.'),
    ('Statewide Capability', 'Where we can mobilise, with lead time.'),
    ('Not claimed', 'Districts without meaningful utility-scale renewable potential. We would rather say so.'),
]

tiers = [
    (ui.chip('CORE'), '<strong>Tumakuru &middot; Chitradurga &middot; Koppal &middot; Gadag &middot; Ballari &middot; Vijayanagara &middot; Vijayapura &middot; Bagalkot</strong>', 'Solar &middot; Wind &middot; Transmission', 'Continuous operation, current ground knowledge, district briefings available.'),
    (ui.chip('ACTIVE'), 'Bidar &middot; Kalaburagi &middot; Yadgir &middot; Raichur &middot; Davanagere &middot; Haveri &middot; Belagavi &middot; Shivamogga', 'Solar &middot; Wind &middot; PSP', 'Operating on project mandate; recent field presence.'),
    (ui.chip('STATEWIDE'), 'Remaining RE-relevant districts', 'Case by case', 'Mobilisation with lead time; assessed against the specific site.'),
    (ui.chip('NOT CLAIMED'), 'Coastal belt &middot; much of Malnad &middot; Bengaluru Urban', '&mdash;', 'No meaningful utility-scale solar or wind resource. We would rather say so.'),
]

body = ui.page_head(
    'Karnataka', 'We know this ground.',
    'Bolamudi Enterprise develops the land, approvals and right of way that utility-scale renewable projects in Karnataka stand on. This is a district-by-district account of how that actually works here &mdash; what the land looks like, where the approvals slow down, and what stops projects.',
    'wind-farmland.jpg',
    actions=ui.btns(ui.btn('Explore the coverage', '#coverage', 'onwhite'), ui.btn('Request a district briefing', 'contact.html', 'ghost'))) + f'''
<section class="tight surf">
  <div class="wrap">
    <p class="eyebrow">How to read this coverage</p>
    <div class="grid4 mt-8">
      {''.join(f'<div><h4>{t}</h4><p class="muted fs-14">{d}</p></div>' for t, d in legend)}
    </div>
  </div>
</section>
<section id="coverage">
  <div class="wrap">
    <div class="g57 v-center mb-48">
      {ui.fig('karnataka-map.svg')}
      <div><p class="eyebrow">Statewide</p><h2>All 31 districts. One state, worked end to end.</h2>
      <p class="muted mt-14">From Bidar to Chamarajanagar, we take land, approvals and right of way work anywhere in Karnataka. The tiers below show where we hold continuous ground knowledge and where we mobilise on mandate.</p></div>
    </div>
    {ui.sec_head('Coverage Matrix', 'The state, tiered honestly', 'Karnataka&rsquo;s utility-scale renewable resource is geographically lopsided, and everyone in this audience knows it. A map that lights up Udupi with the same intensity as Koppal tells an informed visitor you don&rsquo;t know the state.')}
    {ui.table(['Tier', 'Districts', 'Technologies', 'What it means'], tiers)}
  </div>
</section>
<section class="surf">
  <div class="wrap">
    {ui.sec_head('Ground Intelligence', 'Featured district: Koppal', 'Kalaburagi Division &middot; Core Operating District &middot; Solar &middot; Wind &middot; Transmission', lead_cls='muted mt-10')}
    <div class="prose">
      <p><strong>Resource profile.</strong> Strong direct normal irradiance across the northern taluks with a workable wind regime on the higher ground; among the districts the state has identified for ultra-mega solar development.</p>
      <p><strong>Land character.</strong> Fragmented dryland holdings with active joint-family shares; workable contiguous blocks are achievable but demand disciplined parcel sequencing and early hold-out identification.</p>
      <p><strong>Approvals character.</strong> Conversion and Section 109 dominate the early file; the queue forms at the district revenue offices, and sequencing against KREDL registration decides the quarter.</p>
      <p><strong>Evacuation character.</strong> Grid context is favourable near the ultra-mega park corridors, but bay availability must be confirmed before land commitment, not after.</p>
      {ui.btns(ui.btn('Request a briefing on Koppal', 'contact.html'))}
    </div>
  </div>
</section>
<section class="dark">
  <div class="wrap w-820">
    <p class="eyebrow">Honest Limits</p>
    <h2>Where we don&rsquo;t operate</h2>
    <p class="mt-18">Karnataka&rsquo;s renewable resource is not evenly distributed, and neither is useful expertise.</p>
    <p class="mt-14">The coastal districts and much of the Malnad belt do not support utility-scale solar or wind at competitive tariffs &mdash; rainfall, forest cover, terrain and land fragmentation all work against it. Pumped storage is a different question in that geography, and one we follow closely, but hydrological and forest clearance work there is a specialist discipline with its own institutional relationships. We will say honestly where our knowledge ends.</p>
    <p class="mt-14">We also do not take on land aggregation where the parcel structure or the local situation means the timeline we would have to quote is one no developer should accept. It is faster and cheaper for everyone to learn that in the first conversation.</p>
    <p class="mt-14">If a district is outside what we claim, we will usually still know who to point you to.</p>
  </div>
</section>
''' + ui.CTA

PAGES = {'karnataka.html': ui.page(
    ui.titled('Karnataka Coverage'),
    'A district-by-district account of how renewable development actually works in Karnataka — what the land looks like, where approvals slow down, and what stops projects.',
    body, nav='karnataka.html')}
