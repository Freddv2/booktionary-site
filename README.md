# booktionary.io

Static site, generated. `content.py` holds article copy and detailed home-page
support content. `home_ui.py` holds the short, localized landing-page copy;
`build.py` renders both to committed HTML.

## Editing

Privacy and license documents are maintained as standalone HTML; `build.py` does
not generate or replace them.

Edit `content.py` or `home_ui.py`, never the generated HTML directly — every page starts
with a comment saying so, and hand edits are silently overwritten on the
next build. Then:

```
python3 build.py && python3 validate.py
```

`validate.py` is the test suite. A change is not done until it ends with
`28 page(s) checked, 0 failing` and `git status --porcelain` is empty
(build.py's output is deterministic, so a clean tree after a rebuild means
the committed HTML matches content.py).

## Publishing

GitHub Pages serves this site from `main`. Merging to `main` is publishing
— there is no separate deploy step and no staging environment.

## The home page is an App Store requirement

The site root (`/` and `/fr/`) is the Support URL registered with Apple for
the shipping iOS app. Apple's Guideline 1.5 expects real support
information there. The Support section (and its `mailto:` link) on both
home pages must not be removed or replaced with pure marketing copy.

## Localization

Home/support pages are available in English, French, Canadian French, Spanish, Brazilian Portuguese, European Portuguese, Italian and German. They share reciprocal hreflang links and a visible language selector. The English/French question pages retain their paired links. Edit content.py, regenerate with `python3 build.py`, then run `python3 validate.py` and `python3 -m unittest discover -s tests -v`. Purchase messaging avoids a fixed international price; the App Store supplies the regional price.
