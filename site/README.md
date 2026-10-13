# Bolamudi website: source

Edit the files in this folder, then build. The build writes the finished website to `dist/` and zips it to
`../bolamudi-site.zip`. Upload that zip, or the `dist` folder, to the host. Never edit `dist/`; every build recreates it.

```
python site/build.py                                  # build
python -m http.server 8000 --directory site/dist      # preview at http://localhost:8000
```

## Where to change what

| To change | Edit |
|---|---|
| Colours, fonts, page width | `assets/tokens.css` |
| Phone, email, reply time, company name, enquiry-form key, menu, footer links | `config.py` |
| A service's name, tagline, header photo, or its place in the previous/next order | `SERVICES` in `config.py` |
| A photo (alt text and credit) | put the file in `assets/img/` and list it in `PHOTOS` in `config.py` |
| The words on a page | `pages/<page>.py` |
| A piece used on many pages: header, footer, buttons, cards, panels, rows, form, icons | `components.py` |
| How a piece looks | `assets/styles.css` |

The company name comes from `config.py` in titles, header, footer, forms and the legal pages. In body text it is
written out in full in the page files.

## How it fits together

- `config.py`: facts that appear on more than one page (contact details, menu, services, photo credits, the
  seven-step development sequence).
- `components.py`: functions that return the HTML for shared pieces. Pages are assembled from them.
- `pages/`: one file per page, content only. `service_pages.py` builds all five service pages from one template.
- `assets/tokens.css`: every colour, font and width. Faded variants are derived from the same values, and the
  build writes the colours into the Karnataka map too.
- `assets/styles.css`: component styles, using tokens only. One-off spacing tweaks are the small utility classes at
  the end (`mt-16`, `fs-15`, …), each defined once.
- `assets/main.js`: menu toggle, scroll reveal and the enquiry form. The form's endpoint and error text come
  from the form markup, so they follow `config.py`.

## Rules the build enforces

`python site/build.py` stops with a message if:

- `styles.css` contains a raw colour instead of a token,
- a page has an inline `style=""` (only background photos, `--img`, are allowed),
- a link points at a page, file or `#anchor` that doesn't exist,
- an SVG uses a token that `tokens.css` doesn't define.
