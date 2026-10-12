# booktionary.io

Static site, generated. `content.py` holds article copy and detailed home-page
support content. `home_ui.py` and `home_refresh.py` hold the localized landing-page copy;
`build.py` renders both to committed HTML.

## Editing

Privacy and license documents are maintained as standalone HTML; `build.py` does
not generate or replace them.

Edit `content.py`, `home_ui.py` or `home_refresh.py`, never the generated HTML directly — every page starts
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

Home/support pages are available in English, French, Spanish, Brazilian Portuguese, European Portuguese, Italian and German. They share reciprocal hreflang links and a visible language selector. The English/French question pages retain their paired links. Edit content.py, regenerate with `python3 build.py`, then run `python3 validate.py` and `python3 -m unittest discover -s tests -v`. The homepage labels its example price as USD; the App Store supplies the regional price.

## Reading-first homepage

The October 11 approved mockup leads with “Stay in the story”, followed by
pointing at an unfamiliar word, seeing the meaning, and continuing to read.
The four supporting proofs follow this flow. `assets/home.css` contains the
responsive layout shared by all seven editions.

Version 1.0.10 released on October 10 with **24 book languages**, **24
English-word translation targets**, and **27 interface localizations**.
`language_support.py` keeps the scopes distinct. English is bundled; 23 other
dictionaries and word-translation packs are separate optional downloads.
Greek is an interface/translation language, not a book language. Kurmanji is
Latin-script Kurdish; Malay covers Rumi; Chinese covers both scripts.

Optional full-definition translations into 19 destinations remain upcoming
in 1.0.11 and require iOS 18+. Contextual sense selection requires supported
Apple Intelligence hardware with the model available on iOS 26+; otherwise
the first dictionary meaning is shown. Keep those qualifications in all locales.

`assets/booktionary-real-book-photo.jpg` is the user-approved generated product
illustration, showing the English/French example. Its provenance is recorded
alongside the asset. Actual historical app screenshots remain untouched in
`assets/language-expansion/` but are no longer displayed in decorative frames.

App Store anchors and SoftwareApplication schema use the tracked URL from
`SITE["appstore_url"]`. Preserve all campaign parameters when editing it.
Do not modify offline-resource catalogs or downloadable packs when updating
presentation. Support details remain on every homepage for App Store use.

The app repo's `docs/languages.md` contains the complete support matrix and
download sizes; `docs/appstore/screenshots/README.md` identifies the 124
current App Store images. Historical capture directories remain preserved.

The website has one French edition at `/fr/`. `/fr-CA/` is a generated
compatibility redirect for existing support URLs, omitted from hreflang, the
selector and sitemap. Canadian French remains an app/store localization.
