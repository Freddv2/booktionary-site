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
`28 page(s) checked, 0 failing (27 content pages and one compatibility redirect)` and `git status --porcelain` is empty
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

Home/support pages are available in English, French, Spanish, Brazilian Portuguese, European Portuguese, Italian and German. They share reciprocal hreflang links and a visible language selector. The English/French question pages retain their paired links. Edit content.py, regenerate with `python3 build.py`, then run `python3 validate.py` and `python3 -m unittest discover -s tests -v`. Purchase messaging avoids a fixed international price; the App Store supplies the regional price.

## Upcoming language expansion

All seven home editions list the candidate's **24 book languages**, **24
English-word translation targets** and **27 interface localizations**.
`language_support.py` keeps those scopes distinct. English definitions alone
are bundled; the 23 other dictionaries and every translation pack are
independent optional downloads. The native-language list must match
`offline-resources/catalog-v2.json`; Greek belongs only to the interface and
English translation scopes. Kurdish is Latin-script Kurmanji, Malay is Rumi,
and Chinese supports Simplified and Traditional text.

The site explicitly labels these additions as a **upcoming language expansion** because the
expanded-language candidate is retained for a later release. The separate
six-language 1.0.9 (18) is waiting for App Review. Keep that availability notice
until the expansion itself is released. The current App Store version has
six book languages. Do not redirect older builds to the expanded catalog or
change the legacy `catalog.json` when updating presentation.

`assets/language-expansion/` contains 12 byte-for-byte screenshots from the
app's October 5 actual-resource capture set. `provenance.json` records the
source commit, source paths, dimensions and SHA-256. Each home uses its own
localized home/picker screen (Portuguese variants share the app's `pt`
interface). The separate screenshot gallery is omitted at the user’s request.
Do not alter app UI in the screenshots or imply a Greek book dictionary.

The language strip scrolls continuously through the implemented languages,
including both Chinese scripts. French regional duplicates are omitted. Greek carries an
interface/English-translation label. Its duplicate visual group is hidden from
assistive technology. Hover or keyboard focus pauses movement;
reduced-motion preferences disable animation and permit manual scrolling.

The app repo's `docs/languages.md` contains the complete support matrix and
download sizes; `docs/appstore/screenshots/README.md` identifies the 124
current App Store images. Historical capture directories remain preserved.

The website has one French edition at `/fr/`. `/fr-CA/` is a generated
compatibility redirect for existing support URLs, omitted from hreflang, the
selector and sitemap. Canadian French remains an app/store localization.
