"""Contact: contact.html"""
import components as ui
import config as cfg

next_steps = [
    ('We read your enquiry against the district', 'Stage, technology and location are matched to what we know of the ground.'),
    (f'First reply within {cfg.RESPONSE_TIME}', 'A substantive response &mdash; not an acknowledgement &mdash; including whether we are the right party.'),
    ('A scoped conversation', 'If it fits, a call against your specific site. Commercial terms are discussed against a specific site and timeline, never a brief.'),
]

questions = [
    ('What exactly does Bolamudi Energy do?','Pre-construction development support for utility-scale renewable projects in Karnataka: land aggregation, statutory approvals, government liaison, evacuation coordination and transmission right of way &mdash; from site screening to construction-ready handover.'),
    ('Do you work outside Karnataka?', 'No. Land procedure, revenue practice and local body process are state-specific, and our value is district-level depth in one state.'),
    ('How early should we involve you in a project?', 'At site screening, before commercial commitment. The most expensive land and approval errors are made before a specialist is in the room.'),
    ('Can you help with land that is already partly aggregated?', 'Yes. We audit what is held &mdash; title, contiguity, statutory position &mdash; and take over the remainder with a sequencing plan that protects what you have already invested.'),
    ('How do you handle confidentiality on site data?', 'NDAs on request before any site data is shared. Every engagement file is held with the client, and we do not disclose client identities or project locations.'),
    ('How are your services priced?', 'Against a specific site and a specific timeline &mdash; retainer, milestone or success-fee structures sized to scope. We do not quote development support against a brief, because a number given without the ground reality behind it would be a guess.'),
    ('What is a realistic timeline for statutory approvals in Karnataka?', 'It depends on capacity, land classification, district and connectivity route. Anyone quoting a fixed timeline without those inputs is guessing. We provide indicative ranges per approval category against your specific project, with dependencies stated.'),
    ('Do you take on transmission right of way work independently?', 'Yes. RoW is a self-contained mandate &mdash; corridor walk-down, route optimisation, compensation under the MoP 2024 guidelines, and clearance through the District Administration.'),
]

consent = (f'I consent to {cfg.COMPANY} using the details above to respond to this enquiry and to maintain a record of '
           f'our correspondence. You can withdraw consent or request deletion at any time by writing to {cfg.EMAIL}. '
           f'See our <a href="privacy.html">Privacy Notice</a>.')

body = ui.page_head(
    'Contact', 'Start with a conversation about your site.',
    'Tell us the district, the technology and the stage you are at. We will tell you what the land and approval path looks like, and whether we are the right party for it.') + f'''
<section>
  <div class="wrap g57">
    <div>
      <p class="eyebrow">Direct</p>
      {ui.contact_lines()}
      <hr class="gold-rule">
      <p class="eyebrow">What happens next</p>
      {ui.numbered(next_steps)}
      <hr class="gold-rule">
      <p class="muted fs-14">Client names and project details are withheld under confidentiality undertakings. References are shared on request during evaluation.</p>
    </div>
    <div>
      {ui.enquiry_form(consent, bordered=True)}
    </div>
  </div>
</section>
<section class="surf">
  <div class="wrap g57">
    <div><p class="eyebrow">FAQ</p><h2>Before you write</h2></div>
    <div>
      {ui.faq(questions)}
    </div>
  </div>
</section>
'''

PAGES = {'contact.html': ui.page(
    ui.titled('Contact'),
    f'Start a conversation about your site in Karnataka. Tell us the district, the technology and the stage — we respond within {cfg.RESPONSE_TIME}.',
    body, nav='contact.html')}
