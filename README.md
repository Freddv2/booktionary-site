# booktionary.io

Static site, generated. `content.py` holds article copy and detailed home-page
support content. `home_ui.py` and `home_refresh.py` hold the localized landing-page copy;
`build.py` renders both to committed HTML.

## Editing

For an app release that changes website copy, prepare and validate the generated
site on a branch and open a PR against `main`. Record its PR number, exact head
SHA, target app version, and a unique expected English text fragment in
`release/pending-website.json` on `main`. The scheduled
`publish-released-website.yml` workflow checks the public App Store version in
both the US and Canada. Only when both show the exact target version does it
rebuild and test the prepared PR, merge it, request a Pages build, and verify
the live site. It also supports manual dispatch for a release-day check.
For a release with no website change, record that decision in the app release
assessment and leave the pending file absent. Replace the pending file for the
next release only after the previous site update is verified live.

Privacy and license documents are maintained as standalone HTML; `build.py` does
not generate or replace them.

Edit `content.py`, `home_ui.py`, `home_refresh.py`, or the localized JSON sources, never the generated HTML directly — every page starts
with a comment saying so, and hand edits are silently overwritten on the
next build. Then:

```
python3 build.py && python3 validate.py
```

`validate.py` is the test suite. A change is not done until it ends with
`48 page(s) checked, 0 failing` (47 content pages and one compatibility redirect) and `git status --porcelain` is empty
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

Home/support pages cover all 26 app interface choices and all 31 App Store locales through 27 canonical website editions. `site_locales.py` records every mapping. English, French and Spanish regional store locales share their language edition; Portuguese has Brazilian and European editions, Chinese has both scripts, and Kurmanji uses Latin script. They share reciprocal hreflang links and a visible language selector. The English/French question pages retain their paired links. Edit content.py, regenerate with `python3 build.py`, then run `python3 validate.py` and `python3 -m unittest discover -s tests -v`. The homepage labels its example price as USD; the App Store supplies the regional price.

## Reading-first homepage

The October 11 approved mockup leads with “Stay in the story”, followed by
pointing at an unfamiliar word, seeing the meaning, and continuing to read.
The four supporting proofs follow this flow. `assets/home.css` contains the
responsive visual system. The original seven homepages keep their full layout; the 20 additional editions use the same visual system with all ten released product-description blocks.

Version 1.0.10 released on October 10 with **24 book languages**, **24
English-word translation targets**. Version 1.0.12 provides **26 interface language options**, with one French choice and separate Simplified and Traditional Chinese choices.
`language_support.py` keeps the scopes distinct. English is bundled; 23 other
dictionaries and word-translation packs are separate optional downloads.
Greek is an interface/translation language, not a book language. Kurmanji is
Latin-script Kurdish; Malay covers Rumi; Chinese covers both scripts.

Version 1.0.11 added optional translated definitions for English books in 19
supported destinations on iOS 18+. Contextual sense selection requires supported
Apple Intelligence hardware with the model available on iOS 26+; otherwise
the first dictionary meaning is shown. Keep those qualifications in all locales.

`assets/booktionary-real-book-photo.jpg` is the user-approved generated product
illustration, showing the English/French example. Its provenance is recorded
alongside the asset. Actual historical app screenshots remain untouched in
`assets/language-expansion/` but are no longer displayed in decorative frames.

App Store anchors and SoftwareApplication schema use `build.appstore_url_for(lang)`.
It preserves the app, provider and media parameters from `SITE["appstore_url"]`
and assigns a campaign per page language: `booktionary_web_en`,
`booktionary_web_fr`, `booktionary_web_de`, `booktionary_web_es`,
`booktionary_web_it`, `booktionary_web_pt_br` and `booktionary_web_pt_pt`,
with the same `booktionary_web_<locale>` convention for all 27 editions
(locale tags are lowercased and hyphens become underscores).
Question pages use their language's campaign too. These tokens describe the
referring page, not the purchaser's territory. Historic traffic retains the old
`booktionary_website_ios` campaign; compare periods with that migration in mind.
Apple's privacy thresholds can hide low-volume campaigns, so absent data is not
proof of zero downloads. This adds no website scripts, cookies or paid service.
See [Apple's campaign-link documentation](https://developer.apple.com/help/app-store-connect-analytics/acquisition/campaign-links).
Do not modify offline-resource catalogs or downloadable packs when updating
presentation. Support details remain on every homepage for App Store use.

The app repo's `docs/languages.md` contains the complete support matrix and
download sizes; `docs/appstore/screenshots/README.md` identifies the 124
current App Store images. Historical capture directories remain preserved.

The website has one French edition at `/fr/`. `/fr-CA/` is a generated
compatibility redirect for existing support URLs, omitted from hreflang, the
selector and sitemap. Canadian French remains an App Store locale. Canadian phone preferences use the single French app-language choice.

### Localized release images (1.0.12)

The pending 1.0.12 website PR uses matching app interface controls in each
localized homepage's definition example. The source images and checksums are
recorded in `assets/localized-interface/manifest.json`; Portuguese regional pages
share the app's Portuguese interface. The English book passage and definition
remain English, and the caption names the demonstrated word-translation language.
The scanning hero has no interface text and can remain shared. Publish these
images only through the exact-version gate after 1.0.12 is public in the US and
Canadian App Store listings.

## All-language search discovery — 19 October 2026

`search_descriptions.json` supplies 27 localized homepage summaries.
`article_search_descriptions.json` supplies the 20 English/French article
summaries. These describe the actual page; Google may choose a different
snippet. Every generated page has a self-canonical URL, a reciprocal hreflang
cluster and sitemap coverage.

`locale_labels.json` supplies short native interface labels for the 20 new
editions. `localized_homes.json` freezes the ten released App Store description
blocks for 19 of them; Kurmanji has separately prepared copy following the same
released feature boundaries. `localized_home.py` renders every block, including
download, coverage and device limitations. Greek is for English-book readers
and word translations; it does not advertise Greek book scanning. No independent
native-speaker certification is claimed for the new website labels/copy.

All 27 editions have a visible language selector and their own campaign token.
The 20 new homepages add no new app capabilities, assets, scripts or paid service.
Indexability checks do not establish that Google has indexed a URL. Read the
Search Console evidence and actual deployment state in the app repository's
`docs/qa/2026-10-19-all-locale-search-visibility.md`.

`BingSiteAuth.xml` is Bing's public ownership-verification file. Keep it at the
site root so Bing Webmaster Tools can verify `https://booktionary.io/`. The
existing `sitemap.xml` contains all 47 content URLs; verification and sitemap
submission do not establish that Bing has indexed those pages.


## Prepared English expansion — iOS 1.0.14

`english_translation_release.json` holds the same 27 localized product-fact
paragraphs used for the 1.0.14 App Store preparation. The seven established
homepages add these facts to their language section and translation FAQ; the
20 extended editions add them to the existing translation-support block.
All 23 supported non-English book sources offer separately downloaded English
word equivalents. English definitions depend on a compatible Apple model.
Greek remains excluded as a book source; no Sorani or Jawi coverage is added.
Existing approved images, layout, campaign links and support contact remain.

Publish this branch only after public iOS 1.0.14 is available. Its release PR
and actual main/head IDs belong in the app release impact record. Do not
re-enable or dispatch GitHub Actions as part of this preparation. The existing
1.0.12 pending-website file is historical; this branch does not silently replace
it on main or publish new app claims before release.

## Prepared 1.0.15 update

The release adds definition word actions and optional Google search disclosures
in all 27 website editions. Both privacy policies describe the explicit browser
search action. `reading_artwork_release.json` pins approved photographic examples
with the matching interface language in every edition; the Kurmanji portrait has
separate owner approval. Original PNGs are reused without resampling. Older
illustrations remain historical assets. Publish this update only after iOS
1.0.15 is public in both the US and Canada, using the pinned website release gate.
