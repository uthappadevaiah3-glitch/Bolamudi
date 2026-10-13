"""Builds the Bolamudi website.   Run:  python site/build.py

  config.py       site facts: phone, email, menu, services, photo credits
  components.py   shared building blocks: header, footer, cards, panels, forms, ...
  pages/          the words on each page, assembled from components
  assets/         tokens.css (colours, fonts), styles.css, main.js, images
  dist/           OUTPUT: the finished website, rebuilt from scratch on every run, and
                  zipped to ../bolamudi-site.zip. Upload that; never edit dist/ by hand.
"""
import sys
sys.dont_write_bytecode = True  # keep the source folders free of __pycache__

import re
import shutil
from pathlib import Path

from pages import about, contact, home, karnataka, legal, sectors, service_pages, services

ROOT = Path(__file__).parent
ASSETS, DIST = ROOT / 'assets', ROOT / 'dist'
PAGE_MODULES = (home, about, services, service_pages, sectors, karnataka, contact, legal)


def read(name):
    return (ASSETS / name).read_text(encoding='utf-8')


def write(path, text):
    path.write_text(text, encoding='utf-8', newline='\n')


def resolve(value, tokens):
    """A token's final value, following var() references; 'rgb(27, 77, 62)' comes back as '#1B4D3E'."""
    value = re.sub(r'var\(--([\w-]+)\)', lambda m: resolve(tokens[m[1]], tokens), value).strip()
    rgb = re.fullmatch(r'rgb\((\d+),\s*(\d+),\s*(\d+)\)', value)
    return '#%02X%02X%02X' % tuple(map(int, rgb.groups())) if rgb else value


def build():
    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ASSETS, DIST, ignore=shutil.ignore_patterns('*.css', '*.svg'))
    write(DIST / 'styles.css', read('tokens.css') + read('styles.css'))  # one stylesheet, tokens first
    # SVGs shown via <img> can't read CSS variables, so the token values are written into them here.
    tokens = dict(re.findall(r'--([\w-]+)\s*:\s*([^;]+);', re.sub(r'/\*.*?\*/', '', read('tokens.css'), flags=re.S)))
    for svg in ASSETS.rglob('*.svg'):
        text = re.sub(r'var\(--([\w-]+)\)', lambda m: resolve(tokens[m[1]], tokens), svg.read_text(encoding='utf-8'))
        write(DIST / svg.relative_to(ASSETS), text)
    pages = {name: html for m in PAGE_MODULES for name, html in m.PAGES.items()}
    for name, html in pages.items():
        write(DIST / name, html)
    check(pages)
    shutil.make_archive(str(ROOT.parent / 'bolamudi-site'), 'zip', DIST)
    print(f'Built {len(pages)} pages into {DIST}  (zipped: {ROOT.parent / "bolamudi-site.zip"})')


def check(pages):
    """Architecture guard: stop the build if a page or the stylesheet breaks the rules."""
    css = re.sub(r'/\*.*?\*/', '', read('styles.css'), flags=re.S)
    raw = re.findall(r'#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?)\((?!var\()', css)
    assert not raw, f'styles.css has raw colours {raw}: add a token to tokens.css and use var(--name)'
    ids = {name: set(re.findall(r'\sid="([^"]+)"', html)) for name, html in pages.items()}
    for name, html in pages.items():
        for style in re.findall(r'\sstyle="([^"]*)"', html):
            assert re.fullmatch(r'--img:url\(img/[\w.-]+\)', style), \
                f'{name}: inline style "{style}"; give it a class in styles.css instead'
        for ref in re.findall(r'\s(?:href|src)="([^"]+)"', html) + re.findall(r'url\(([^)]+)\)', html):
            if re.match(r'https?:|mailto:|tel:', ref):
                continue
            path, _, anchor = ref.partition('#')
            target = path.split('?')[0] or name
            assert (DIST / target).is_file(), f'{name}: broken link "{ref}"'
            assert not anchor or anchor in ids.get(target, ()), f'{name}: "{ref}" points at a missing #{anchor}'
    for svg in DIST.rglob('*.svg'):
        assert 'var(' not in svg.read_text(encoding='utf-8'), f'{svg.name}: uses an unknown token'


if __name__ == '__main__':
    build()
