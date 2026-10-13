"""Services hub: services.html (the five detail pages are in service_pages.py)"""
import components as ui
import config as cfg

blurbs = {
    'land-aggregation': 'Contiguous, title-clean, registered land &mdash; assembled parcel by parcel. Projects don&rsquo;t fail on the last parcel; they fail on the parcel nobody checked properly.',
    'government-liaison': 'Continuous, documented follow-through with the departments that decide. Files don&rsquo;t get rejected &mdash; they wait, and your COD date moves with them.',
    'statutory-approvals': 'A project-specific statutory register, owned from application to closure. The approval list you&rsquo;re working from is probably wrong for your project.',
    'transmission-row': 'Corridor walked, optimised, compensated and cleared &mdash; span by span. One orchard in a 40&nbsp;km corridor can hold an entire commissioned project.',
    'project-development-support': 'The Karnataka-side development desk &mdash; one interface, one register, one weekly report. Slippage reported before the review meeting, not in it.',
}

cards = [ui.card(cfg.SERVICES[slug]['name'], text, href=ui.service_href(slug)) for slug, text in blurbs.items()]
cards.append(ui.card('Renewable project facilitation', 'The umbrella under which all five services run as one continuous mandate &mdash; site suitability, resource-adjacent land banking, and coordination across solar, wind, hybrid and pumped storage development.', cls='quiet'))

engagements = [
    ('Pre-acquisition assessment', ['Bounded, short-duration review', 'Bay availability and title screening', 'Go / no-go position']),
    ('Stage mandate', ['One stage: land, approvals, evacuation or RoW', 'Defined deliverable and completion criteria', 'Priced against scope, not time']),
    ('Full development support', ['Site identification to construction-ready handover', 'Single accountable point of contact', 'Continuous status file held with the client']),
]

body = ui.page_head(
    'Services', 'The development sequence, run as one scope.',
    'Five areas of practice covering everything between site allocation and construction readiness &mdash; engaged individually or as one continuous mandate.',
    'wind-farmland.jpg') + f'''
<section>
  <div class="wrap">
    <ul class="grid3 bare">
      {''.join(f'<li>{c}</li>' for c in cards)}
    </ul>
  </div>
</section>
<section class="dark">
  <div class="wrap">
    {ui.sec_head('The Development Sequence', 'Why one scope beats five vendors', 'Land, approvals, evacuation and right of way are dependency-ordered. Splitting them across parties creates the gaps where schedules die. We run them as one programme with one accountable owner.', lead_cls='mt-16')}
    {ui.timeline(cfg.DEV_SEQUENCE)}
  </div>
</section>
<section class="surf">
  <div class="wrap">
    {ui.sec_head('Engagement Models', 'Three ways to engage us')}
    <div class="grid3">
      {''.join(ui.panel(t, items) for t, items in engagements)}
    </div>
  </div>
</section>
''' + ui.CTA

PAGES = {'services.html': ui.page(
    ui.titled('Services'),
    'Land aggregation, government liaison, statutory approvals, transmission right of way and project development support for renewable projects in Karnataka.',
    body, nav='services.html')}
