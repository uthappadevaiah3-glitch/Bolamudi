"""Reusable building blocks. Every page is assembled from these, so a change here shows up site-wide.

Each function returns an HTML string. Facts (phone, email, menu, services, photos) come from config.py;
looks come from assets/styles.css and assets/tokens.css. No function adds styling of its own.
"""
import hashlib
from pathlib import Path

import config as cfg

ASSETS = Path(__file__).parent / 'assets'
# Cache-busting tag on the CSS/JS links: changes whenever they change, so browsers fetch the new files.
VER = hashlib.md5(b''.join((ASSETS / f).read_bytes() for f in ('tokens.css', 'styles.css', 'main.js'))).hexdigest()[:8]
CURRENT = ' aria-current="page"'


def classes(*names):
    return ' '.join(n for n in names if n)


def titled(name):
    return f'{name} — {cfg.COMPANY}'


def tel():
    return 'tel:' + cfg.PHONE.replace(' ', '')


def service_href(slug):
    return f'services-{slug}.html'


def bg(img):
    """Background photo for a .photo band: the one inline style pages may use."""
    return f' style="--img:url(img/{img})"'


def img(file):
    return f'<img src="img/{file}" alt="{cfg.PHOTOS[file]["alt"]}" loading="lazy">'


def fig(file, cls=''):
    return f'<figure class="{classes("photo-fig", cls)}">{img(file)}</figure>'


# ---------- page frame ----------

def page(title, description, body, nav=None):
    """A complete HTML document; `nav` is the menu entry to mark as the current page."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="{cfg.FONTS_URL}" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={VER}">
<link rel="icon" type="image/png" href="favicon.png">
</head>
<body>
{header(nav)}
<main>
{body}
</main>
{footer()}
<script src="main.js?v={VER}"></script>
</body>
</html>
'''


def brand(home_label=True):
    first, rest = cfg.COMPANY.upper().split(' ', 1)
    label = f' aria-label="{cfg.COMPANY} — home"' if home_label else ''
    return (f'<a class="brand" href="index.html"{label}><img src="logo-mark.png" alt="">'
            f'<span class="wm">{first}<small>{rest}</small></span></a>')


def header(current=None):
    items = ''.join(f'\n        <li><a href="{href}"{CURRENT if href == current else ""}>{label}</a></li>'
                    for href, label in cfg.NAV)
    cta_href, cta_label = cfg.NAV_CTA
    return f'''<header class="site-header">
  <div class="wrap">
    {brand()}
    <button class="nav-toggle" aria-expanded="false" aria-controls="mainnav" aria-label="Menu">&#9776;</button>
    <nav class="main" id="mainnav">
      <ul>{items}
        <li><a href="{cta_href}" class="nav-cta">{cta_label}</a></li>
      </ul>
    </nav>
  </div>
</header>'''


def footer():
    services = ''.join(f'\n          <li><a href="{service_href(slug)}">{s["name"]}</a></li>'
                       for slug, s in cfg.SERVICES.items())
    company = ''.join(f'\n          <li><a href="{href}">{label}</a></li>' for href, label in cfg.FOOTER_COMPANY)
    return f'''<footer>
  <div class="wrap">
    <div class="cols">
      <div>
        {brand(home_label=False)}
        <p>Land, statutory clearances and transmission right of way for utility-scale renewable projects across Karnataka.</p>
      </div>
      <div>
        <h5>Services</h5>
        <ul>{services}
        </ul>
      </div>
      <div>
        <h5>Company</h5>
        <ul>{company}
        </ul>
      </div>
      <div>
        <h5>Get in touch</h5>
        <ul>
          <li><a href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a></li>
          <li><a href="{tel()}">{cfg.PHONE}</a></li>
        </ul>
        <a class="btn ghost" href="contact.html">Request consultation</a>
      </div>
    </div>
    <div class="legal">
      <span>&copy; {cfg.YEAR} {cfg.COMPANY}. All rights reserved.</span>
      <span><a href="privacy.html">Privacy</a> &middot; <a href="terms.html">Terms</a> &middot; <a href="terms.html#photo-credits">Photo credits</a></span>
    </div>
  </div>
</footer>'''


def page_head(eyebrow, title, lead, photo=None, actions=''):
    """Dark band at the top of inner pages, optionally over a photo."""
    open_ = f'<div class="page-head photo"{bg(photo)}>' if photo else '<div class="page-head">'
    return (f'{open_}<div class="wrap"><p class="eyebrow">{eyebrow}</p><h1>{title}</h1>'
            f'<p class="lead">{lead}</p>{actions}</div></div>')


# ---------- section parts ----------

def sec_head(eyebrow, title, lead=None, lead_cls='muted mt-14', cls=''):
    lead_html = f'\n    <p class="{lead_cls}">{lead}</p>' if lead else ''
    return f'<div class="{classes("sec-head", cls)}"><p class="eyebrow">{eyebrow}</p><h2>{title}</h2>{lead_html}</div>'


def btn(label, href, kind=''):
    """kind: '' (solid), 'ghost' (outline) or 'onwhite' (white, for dark bands)."""
    return f'<a class="{classes("btn", kind)}" href="{href}">{label}</a>'


def btns(*buttons, cls=''):
    return f'<div class="{classes("btns", cls)}">{"".join(buttons)}</div>'


def cta_band(title, body, buttons, width='w-760', gap='mt-18'):
    return f'''<section class="darker">
  <div class="wrap tc {width}">
    <h2>{title}</h2>
    <p class="{gap}">{body}</p>
    {btns(*buttons, cls="center")}
  </div>
</section>'''


# Closing call-to-action shared by About, Services, Sectors and Karnataka
CTA = cta_band(
    'If you are assessing a site in Karnataka, start with the questions that decide the project.',
    'Is the land clean, is the bay available, and is the corridor realistic. We will tell you before you commit capital, not after.',
    [btn('Start a site discussion', 'contact.html', 'onwhite'), btn('View services', 'services.html', 'ghost')])


def card(title, text, href=None, tag='div', cls='', title_cls=''):
    """A bordered card; with `href` it becomes a link card with an 'Explore service' foot."""
    h3 = f'<h3 class="{title_cls}">' if title_cls else '<h3>'
    if href:
        return (f'<a class="{classes("card", cls)}" href="{href}">{h3}{title}</h3><p>{text}</p>'
                f'<div class="foot">Explore service <span aria-hidden="true">&rarr;</span></div></a>')
    return f'<{tag} class="{classes("card", cls)}">{h3}{title}</h3><p>{text}</p></{tag}>'


def row(text, title=None, idx=None, tag='div', cls='', hide_idx=False):
    """Gold-ruled row: optional index label, optional title, then text."""
    aria = ' aria-hidden="true"' if hide_idx else ''
    idx_html = f'<span class="idx"{aria}>{idx}</span>' if idx else ''
    title_html = f'<h4>{title}</h4>' if title else ''
    return f'<{tag} class="{classes("row", cls)}">{idx_html}{title_html}<p>{text}</p></{tag}>'


def numbered(items, tag='div', hide_idx=False):
    """Rows numbered 01, 02, … from (title, text) pairs."""
    return '\n'.join(row(text, title, f'{i:02d}', tag, hide_idx=hide_idx) for i, (title, text) in enumerate(items, 1))


def panel(title, items=(), intro=None, cls='', top='', body=''):
    """Gold-topped panel: optional picture on top, title, optional intro, dash list, extra body."""
    intro_html = f'<p class="muted intro">{intro}</p>' if intro else ''
    ul = '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>' if items else ''
    return f'<div class="{classes("panel", cls)}">{top}<h3>{title}</h3>{intro_html}{ul}{body}</div>'


def timeline(steps):
    lis = ''.join(f'\n      <li><span class="idx">{i:02d}</span><h4>{t}</h4><p>{d}</p></li>'
                  for i, (t, d) in enumerate(steps, 1))
    return f'<ol class="timeline">{lis}\n    </ol>'


def chip(text):
    return f'<span class="mono-chip">{text}</span>'


def table(head, rows):
    th = ''.join(f'<th scope="col">{h}</th>' for h in head)
    body = '\n'.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return (f'<div class="table-scroll"><table>\n      <thead><tr>{th}</tr></thead>\n'
            f'      <tbody>{body}</tbody>\n    </table></div>')


def faq(items):
    """Accordion of (question, answer) pairs; the first starts open."""
    return '\n'.join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>'
                     for i, (q, a) in enumerate(items))


# ---------- line icons (colours come from the tokens via .ico in styles.css; .ac = gold accent) ----------

ICONS = {
    'land': '<path d="M4 30 L14 25 L26 29 L36 24 L36 34 L26 38 L14 34 L4 38 Z"/><path d="M14 25 V34 M26 29 V38"/>'
            '<path class="ac" d="M20 22 C20 22 13 15 13 10 a7 7 0 0 1 14 0 C27 15 20 22 20 22 Z"/>'
            '<circle class="ac" cx="20" cy="10" r="2.5"/>',
    'liaison': '<path d="M6 16 L20 7 L34 16 Z"/><path d="M10 19 V31 M16 19 V31 M24 19 V31 M30 19 V31"/>'
               '<path d="M5 35 H35 M7 31 H33"/><path class="ac" d="M20 7 V2 L25 3.5 L20 5"/>',
    'approvals': '<path d="M9 4 H25 L31 10 V36 H9 Z"/><path d="M25 4 V10 H31"/><path d="M14 16 H26 M14 21 H26"/>'
                 '<path class="ac" d="M14 29 L18 32.5 L26 25"/>',
    'transmission': '<path d="M20 3 L13 37 M20 3 L27 37 M15.5 25 L24.5 25 M14 31 L26 31 M17 15 L23 15"/>'
                    '<path d="M8 11 H32 M10 18 H30"/><path class="ac" d="M2 14 Q5 20 8 11 M38 14 Q35 20 32 11"/>',
}


def icon(name):
    return f'<svg class="ico" viewBox="0 0 40 40" width="40" height="40" aria-hidden="true">{ICONS[name]}</svg>'


# ---------- contact ----------

def contact_lines():
    """Phone, email and reply promise. Light or dark (.darker) styling is handled by CSS."""
    return f'''<p class="contact-phone"><a href="{tel()}">{cfg.PHONE}</a></p>
      <p class="contact-email"><a href="mailto:{cfg.EMAIL}">{cfg.EMAIL}</a></p>
      <p class="contact-note">Response within {cfg.RESPONSE_TIME}</p>
      <p class="contact-fine">Confidential &middot; No obligation &middot; NDA on request</p>'''


STAGES = ['Exploring', 'Site identified', 'Under development', 'Under acquisition']
TECHNOLOGIES = ['Solar', 'Wind', 'Hybrid', 'Pumped storage', 'Transmission', 'Other']


def _select(id_, name, label, options):
    opts = ''.join(f'<option>{o}</option>' for o in options)
    return (f'<div><label for="{id_}">{label}</label><select id="{id_}" name="{name}" required>'
            f'<option value="">Select&hellip;</option>{opts}</select></div>')


def enquiry_form(consent, bordered=False):
    """The enquiry form and its thank-you panel. main.js posts it to the form's action."""
    b = 'bordered' if bordered else ''
    error = f'Sorry, your enquiry could not be sent. Please call {cfg.PHONE} or email {cfg.EMAIL}.'
    return f'''<form class="{classes("form-card enquiry", b)}" action="{cfg.FORM_ENDPOINT}" method="post" data-error="{error}" novalidate>
        <input type="hidden" name="access_key" value="{cfg.FORM_KEY}">
        <input type="hidden" name="subject" value="New enquiry from {cfg.DOMAIN}">
        <input type="checkbox" name="botcheck" hidden tabindex="-1" autocomplete="off">
        <div class="grid2">
          <div><label for="f-name">Full name *</label><input id="f-name" name="name" required></div>
          <div><label for="f-org">Organisation *</label><input id="f-org" name="org" required></div>
        </div>
        <div class="grid2">
          <div><label for="f-email">Work email *</label><input id="f-email" name="email" type="email" required></div>
          <div><label for="f-phone">Phone</label><input id="f-phone" name="phone" type="tel"></div>
        </div>
        <div class="grid2">
          {_select("f-stage", "stage", "Project stage *", STAGES)}
          {_select("f-tech", "technology", "Technology *", TECHNOLOGIES)}
        </div>
        <label for="f-district">District / location</label><input id="f-district" name="district">
        <label for="f-msg">How can we help *</label><textarea id="f-msg" name="message" rows="4" required></textarea>
        <div class="consent"><input type="checkbox" id="f-consent" name="consent" required><label for="f-consent">{consent}</label></div>
        <button class="btn" type="submit">Send enquiry</button>
      </form>
      <div class="{classes("form-success form-card", b)}" role="alert" aria-live="polite">
        <h3 tabindex="-1">Enquiry received</h3>
        <p class="muted">We will respond within {cfg.RESPONSE_TIME}. For anything urgent, call {cfg.PHONE}.</p>
      </div>'''
