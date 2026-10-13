"""Legal: privacy.html and terms.html (terms also lists the photo credits from config.PHOTOS)."""
import components as ui
import config as cfg

UPDATED = 'August 2026'


def credit(file):
    p = cfg.PHOTOS[file]
    kind = 'Map' if file.endswith('.svg') else 'Photo'
    return f'{kind}: <a href="https://commons.wikimedia.org/wiki/File:{p["source"]}" rel="noopener">{p["by"]}</a>, {p["licence"]}'


privacy = f'''
<section><div class="wrap prose">
<p>{cfg.COMPANY} (&ldquo;we&rdquo;, &ldquo;us&rdquo;) respects the privacy of every visitor and correspondent. This notice describes what we collect and how we use it, in line with the Digital Personal Data Protection Act, 2023.</p>
<h2>What we collect</h2>
<p>Only what you submit through the enquiry form or send us directly: name, organisation, contact details, and the content of your enquiry. This site sets no analytics or advertising cookies.</p>
<h2>How we use it</h2>
<p>To respond to your enquiry and maintain a record of our correspondence. We do not sell, rent or share your details with third parties, and we do not add you to marketing lists.</p>
<h2>Retention and your rights</h2>
<p>Correspondence records are retained for as long as needed to serve the relationship. You can withdraw consent or request deletion at any time by writing to <a href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a>.</p>
</div></section>'''

terms = f'''
<section><div class="wrap prose">
<p>By using this website you accept the terms below.</p>
<h2>Content</h2>
<p>Material on this site is provided for general information about our practice. It is not legal, regulatory or investment advice, and statutory procedures described here change; verify the current position before acting on it.</p>
<h2>No engagement by browsing</h2>
<p>Nothing on this site creates a client relationship. Engagements are formed only by a written mandate signed by both parties.</p>
<h2>Intellectual property</h2>
<p>All content, marks and design on this site belong to {cfg.COMPANY} and may not be reproduced without permission, except the photographs and map listed under Photo credits, which remain under their own licences.</p>
<h2>Liability</h2>
<p>We accept no liability for loss arising from reliance on the general information on this site.</p>
</div></section><section><div class="wrap prose" id="photo-credits"><h2>Photo credits</h2><p class="muted">Photographs and the district map are used under their Creative Commons licences via Wikimedia Commons.</p><ul>{''.join(f'<li>{credit(f)}</li>' for f in cfg.PHOTOS)}</ul></div></section>'''

PAGES = {
    'privacy.html': ui.page(ui.titled('Privacy Notice'), f'How {cfg.COMPANY} handles personal data.',
                            ui.page_head('Legal', 'Privacy Notice', f'Last updated: {UPDATED}') + privacy),
    'terms.html': ui.page(ui.titled('Terms of Use'), f'Terms of use for the {cfg.COMPANY} website.',
                          ui.page_head('Legal', 'Terms of Use', f'Last updated: {UPDATED}') + terms),
}
