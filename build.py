#!/usr/bin/env python3
"""Render content.py to committed static HTML. No runtime dependencies."""
import html as h, json, os, re
from content import SITE, PAGES
from home_ui import HOME_UI
from language_support import (BOOK_LANGUAGES, INTERFACE_LANGUAGES,
                              INTERFACE_LOCALES, SCREEN_LOCALES)

ROOT = os.path.dirname(os.path.abspath(__file__))
LABELS = {
    "en": ("English", "Booktionary on the App Store", "Privacy", "Licences", "Related questions"),
    "fr": ("Français", "Booktionary sur l’App Store", "Confidentialité", "Licences", "Questions liées"),
    "fr-CA": ("Français (Canada)", "Booktionary sur l’App Store", "Confidentialité", "Licences", "Questions liées"),
    "es": ("Español", "Booktionary en el App Store", "Privacidad", "Licencias", "Preguntas relacionadas"),
    "pt-BR": ("Português (Brasil)", "Booktionary na App Store", "Privacidade", "Licenças", "Perguntas relacionadas"),
    "pt-PT": ("Português (Portugal)", "Booktionary na App Store", "Privacidade", "Licenças", "Perguntas relacionadas"),
    "it": ("Italiano", "Booktionary sull’App Store", "Privacy", "Licenze", "Domande correlate"),
    "de": ("Deutsch", "Booktionary im App Store", "Datenschutz", "Lizenzen", "Verwandte Fragen"),
}
NAV_LABELS = {
    "en": ("Main navigation", "Footer navigation", "Support"),
    "fr": ("Navigation principale", "Navigation de bas de page", "Assistance"),
    "fr-CA": ("Navigation principale", "Navigation de bas de page", "Soutien"),
    "es": ("Navegación principal", "Navegación del pie de página", "Ayuda"),
    "pt-BR": ("Navegação principal", "Navegação do rodapé", "Suporte"),
    "pt-PT": ("Navegação principal", "Navegação do rodapé", "Apoio"),
    "it": ("Navigazione principale", "Navigazione nel piè di pagina", "Assistenza"),
    "de": ("Hauptnavigation", "Fußnavigation", "Hilfe"),
}

def language_path(lang):
    return "" if lang == "en" else lang + "/"

def url_for(page):
    return f"{SITE['domain']}/{language_path(page['lang'])}" + (page['slug'] + "/" if page['slug'] else "")

def out_path(page):
    parts = [ROOT]
    if page["lang"] != "en": parts.append(page["lang"])
    if page["slug"]: parts.append(page["slug"])
    return os.path.join(*parts, "index.html")

def depth_prefix(page):
    n = (1 if page["lang"] != "en" else 0) + (1 if page["slug"] else 0)
    return "../" * n if n else ""

def find(pages, lang, slug):
    for p in pages:
        if p["lang"] == lang and p["slug"] == slug: return p
    return None

def jsonld(page):
    if page["slug"]:
        data = {"@context": "https://schema.org", "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": page["question"],
                    "acceptedAnswer": {"@type": "Answer",
                                       "text": " ".join(page["paragraphs"])}}]}
    else:
        data = {"@context": "https://schema.org", "@type": "SoftwareApplication",
                "name": "Booktionary", "applicationCategory": "ReferenceApplication",
                "operatingSystem": "iOS 17.0 or later", "url": url_for(page),
                "installUrl": SITE["appstore_url"],
                "inLanguage": list(INTERFACE_LOCALES),
                "description": page["description"],
                "offers": {"@type": "Offer", "price": "1.99", "priceCurrency": "USD",
                           "url": SITE["appstore_url"]}}
    return json.dumps(data, ensure_ascii=False, indent=1).replace("<", "\\u003c")

def fr_typography(text, lang):
    """French typographic convention: a narrow no-break space before ? ! ; :
    instead of an ASCII space, so the punctuation cannot wrap onto its own line."""
    if not lang.startswith("fr"):
        return text
    return re.sub(r" ([?!;:])", " \\1", text)

def render_home(page, pages):
    """The approved editorial landing page, shared by every supported site locale."""
    lang = page["lang"]
    ui = HOME_UI[lang]
    pre = depth_prefix(page)
    esc = h.escape
    screen_locale = SCREEN_LOCALES[lang]
    home_asset = f"assets/language-expansion/{screen_locale}-home.png"
    picker_asset = f"assets/language-expansion/{screen_locale}-languages.png"
    twin = find(pages, "en", "")
    homes = [p for p in pages if not p["slug"]]
    alts = "".join(f'  <link rel="alternate" hreflang="{p["lang"]}" href="{url_for(p)}">\n' for p in homes)
    alts += f'  <link rel="alternate" hreflang="x-default" href="{url_for(twin)}">\n'

    def store_link(css_class, label):
        return (f'<a class="{css_class}" href="{SITE["appstore_url"]}">'
                f'{label}<span aria-hidden="true">↗</span></a>')

    def download_button():
        return store_link("download", (f'<span class="apple-symbol" aria-hidden="true"></span>'
                                        f'<span><small>{esc(ui["download"])}</small>'
                                        f'<strong>App Store</strong></span>'))

    def price_note():
        return f'<p class="purchase-note priced-note"><strong>$1.99 USD</strong><span>{esc(ui["price"])}</span></p>'

    frame_home = (f'<div class="device-frame"><div class="device-screen">'
                  f'<img src="{pre}{home_asset}" alt="{esc(ui["home_alt"])}" width="1206" height="2622" loading="lazy">'
                  '<span class="device-island" aria-hidden="true"></span><span class="device-home-indicator" aria-hidden="true"></span>'
                  '</div></div>')
    frame_languages = (f'<div class="device-frame"><div class="device-screen">'
                       f'<img src="{pre}{picker_asset}" alt="{esc(ui["picker_alt"])}" width="1206" height="2622" loading="lazy">'
                       '<span class="device-island" aria-hidden="true"></span><span class="device-home-indicator" aria-hidden="true"></span>'
                       '</div></div>')
    step_illustrations = [
        f'<div class="step-image native-home">{frame_home}</div>',
        f'<div class="step-image scan-image"><img src="{pre}assets/scanning.webp" alt="" width="851" height="1848" loading="lazy"></div>',
        f'<div class="step-image definition-image"><img src="{pre}assets/definition.webp" alt="" width="851" height="1848" loading="lazy"></div>',
    ]
    steps = "\n".join(
        f'<article class="step">{step_illustrations[i]}<div class="step-title"><span>0{i+1}</span>'
        f'<h3>{esc(title)}</h3></div><p>{esc(description)}</p></article>'
        for i, (title, description) in enumerate(ui["steps"])
    )
    language_strip = "".join(
        f'<span lang="{locale}">{esc(name)}'
        + (f'<small lang="{lang}">{esc(ui["greek_scope_label"])}</small>' if locale == "el" else '')
        + '</span>' for locale, name in INTERFACE_LANGUAGES
    )
    language_rows = "".join(
        f'<li data-book-language="{code}"><span lang="{code}">{esc(name)}'
        + (f'<span class="language-name" lang="en">{esc(english_name)}</span>' if code != "en" else '') + '</span>'
        f'<small>{esc(ui["built_in"] if code == "en" else ui["download_pack"])}</small></li>'
        for code, name, english_name in BOOK_LANGUAGES
    )
    benefits = "".join(
        f'<article><span aria-hidden="true">0{i+1}</span><div><h3>{esc(title)}</h3><p>{esc(description)}</p></div></article>'
        for i, (title, description) in enumerate(ui["benefits"])
    )
    faqs = "".join(
        f'<details><summary>{esc(question)}<span aria-hidden="true">+</span></summary><p>{esc(answer)}</p></details>'
        for question, answer in ui["faqs"]
    )
    locale_links = " ".join(
        f'<a href="{url_for(p)}" lang="{p["lang"]}" hreflang="{p["lang"]}"'
        + (' aria-current="page"' if p["lang"] == lang else '')
        + f'>{LABELS[p["lang"]][0]}</a>' for p in homes
    )
    related_links = "".join(
        f'<li><a href="{pre}{language_path(lang)}{slug}/">{esc(find(pages, lang, slug)["question"])}</a></li>'
        for slug in page["siblings"]
    )
    related = (f'<nav class="related-reading" aria-labelledby="related-title"><h2 id="related-title">{esc(ui["related"])}</h2>'
               f'<ul>{related_links}</ul></nav>') if related_links else ""
    support = fr_typography(page.get("extra_html", ""), lang)
    return f'''<!-- Generated by build.py from content.py and home_ui.py. Do not edit this file by hand. -->
<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(page["question"])}</title>
  <meta name="description" content="{esc(fr_typography(page["description"], lang))}">
  <link rel="canonical" href="{url_for(page)}">
{alts}  <link rel="stylesheet" href="{pre}assets/home.css">
  <link rel="icon" href="{pre}assets/favicon-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="{pre}assets/icon-180.png">
  <script type="application/ld+json">
{jsonld(page)}
  </script>
</head>
<body>
  <header class="site-header wrap">
    <a class="brand" href="#top" aria-label="Booktionary"><img src="{pre}assets/app-icon-main.png" alt="" width="44" height="44"><span>Booktionary</span></a>
    <nav aria-label="{NAV_LABELS[lang][0]}"><a href="#how-it-works">{esc(ui["nav"][0])}</a><a href="#languages">{esc(ui["nav"][1])}</a><a href="#questions">{esc(ui["nav"][2])}</a></nav>
    {store_link("header-download", esc(ui["get"]))}
  </header>
  <main id="top">
    <aside class="release-note wrap">{esc(ui["release_note"])}</aside>
    <section class="hero wrap" aria-labelledby="hero-title">
      <div class="hero-copy">
        <p class="eyebrow"><span class="status-dot" aria-hidden="true"></span>{esc(ui["eyebrow"])}</p>
        <h1 id="hero-title">{esc(ui["title"][0])}<br>{esc(ui["title"][1])} <em>{esc(ui["title"][2])}</em></h1>
        <p class="hero-description">{esc(ui["lead"])}</p>
        <div class="hero-actions">{download_button()}<a class="text-link" href="#how-it-works">{esc(ui["see"])} <span aria-hidden="true">↓</span></a></div>
        {price_note()}
      </div>
      <figure class="hero-figure"><div class="hero-photo"><img src="{pre}assets/scanning.webp" alt="An iPhone scans the word luminous in a paper book" width="851" height="1848" fetchpriority="high"><span class="photo-label">{esc(ui["photo"])}</span></div><figcaption>{esc(ui["photo_caption"])}</figcaption></figure>
    </section>
    <section class="language-strip wrap" id="language-preview"><div class="language-strip-heading"><span class="eyebrow">{esc(ui["strip"])}</span></div><div class="language-carousel" tabindex="0" role="region" aria-label="{esc(ui["interface_note"])}"><div class="language-carousel-track"><div class="language-carousel-group">{language_strip}</div><div class="language-carousel-group" aria-hidden="true">{language_strip}</div></div></div></section>
    <section class="how-section wrap" id="how-it-works" aria-labelledby="how-title">
      <div class="section-heading"><div><p class="eyebrow">{esc(ui["how_kicker"])}</p><h2 id="how-title">{esc(ui["how_title"][0])}<br>{esc(ui["how_title"][1])} <em>{esc(ui["how_title"][2])}</em></h2></div><p>{esc(ui["how_lead"])}</p></div>
      <div class="steps">{steps}</div>
    </section>
    <section class="languages-editorial" id="languages" aria-labelledby="language-title"><div class="wrap language-with-capture">
      <div class="language-information"><p class="eyebrow">{esc(ui["language_kicker"])}</p><h2 id="language-title">{esc(ui["language_title"])}</h2><p class="language-description">{esc(ui["language_lead"])}</p>
        <ul class="dictionary-rows">{language_rows}</ul><div class="language-reading-notes"><p>{esc(ui["translation"])}</p><p>{esc(ui["language_scope"])}</p><p>{esc(ui["interface_note"])}</p><p>{esc(ui["pack_note"])}</p></div></div>
      <figure class="native-language-capture"><a class="language-device-link" href="{pre}{picker_asset}" aria-label="{esc(ui["full_screen"])}">{frame_languages}</a><figcaption><span>{esc(ui["screen_caption"])}</span><a href="{pre}{picker_asset}">{esc(ui["full_screen"])}</a></figcaption></figure>
    </div></section>
    <section class="quiet-section"><div class="wrap quiet-layout"><div><p class="eyebrow">{esc(ui["quiet_kicker"])}</p><h2>{esc(ui["quiet_title"][0])}<br>{esc(ui["quiet_title"][1])}<br><em>{esc(ui["quiet_title"][2])}</em></h2></div><div class="quiet-benefits">{benefits}</div></div></section>
    <section class="questions-section wrap" id="questions" aria-labelledby="questions-title"><div><p class="eyebrow">{esc(ui["questions_kicker"])}</p><h2 id="questions-title">{esc(ui["questions_title"][0])}<br><em>{esc(ui["questions_title"][1])}</em></h2><a class="support-link" href="mailto:fredddv@hotmail.com">{esc(ui["support"])} <span aria-hidden="true">↗</span></a></div><div class="questions">{faqs}</div></section>
    <section class="support-panel wrap" aria-label="{NAV_LABELS[lang][2]}">{support}{related}</section>
    <section class="last-section wrap" aria-labelledby="last-title"><img src="{pre}assets/app-icon-main.png" alt="" width="76" height="76" loading="lazy"><p class="eyebrow">{esc(ui["final_kicker"])}</p><h2 id="last-title">{esc(ui["final_title"][0])}<br><em>{esc(ui["final_title"][1])}</em></h2>{download_button()}{price_note()}<p class="device-requirements">{esc(ui["requirements"])}</p></section>
  </main>
  <footer class="site-footer wrap"><div><a class="brand" href="#top"><img src="{pre}assets/app-icon-main.png" alt="" width="34" height="34" loading="lazy"><span>Booktionary</span></a><p>{esc(ui["footer_line"])}</p></div><nav aria-label="{NAV_LABELS[lang][1]}"><a href="{pre}privacy.html">{esc(ui["privacy"])}</a><a href="{pre}licenses.html">{esc(ui["licences"])}</a><a href="mailto:fredddv@hotmail.com">{NAV_LABELS[lang][2]}</a></nav><div class="locale-links" aria-label="{esc(ui["site_languages"])}">{locale_links}</div><p class="credit">{esc(ui["credit"])}</p></footer>
</body>
</html>
'''

def render_page(page, pages):
    if not page["slug"]:
        return render_home(page, pages)
    pre = depth_prefix(page)
    lang = page["lang"]
    q = h.escape(fr_typography(page["question"], lang))
    body = "\n".join(f"    <p>{h.escape(fr_typography(t, lang))}</p>" for t in page["paragraphs"])
    hero = ""
    if page.get("hero"):
        src, alt = page["hero"]
        hero = f'    <img class="hero" src="{pre}{src}" alt="{h.escape(alt)}" width="880" height="1108">\n'

    benefits = {
        'en': 'One purchase. All language packs included. No subscription or in-app purchases.',
        'fr': 'Un seul achat. Tous les packs de langues inclus. Sans abonnement ni achat intégré.',
        'fr-CA': 'Un seul achat. Tous les ensembles de langues inclus. Sans abonnement ni achats intégrés.',
        'es': 'Una compra. Todos los paquetes de idiomas incluidos. Sin suscripción ni compras integradas.',
        'pt-BR': 'Uma compra. Todos os pacotes de idiomas incluídos. Sem assinatura nem compras no app.',
        'pt-PT': 'Uma compra. Todos os pacotes de línguas incluídos. Sem subscrição nem compras integradas.',
        'it': 'Un acquisto. Tutti i pacchetti di lingue inclusi. Nessun abbonamento né acquisto in-app.',
        'de': 'Ein Kauf. Alle Sprachpakete enthalten. Kein Abo, keine In-App-Käufe.',
    }
    purchase = '' if page['slug'] else f'    <p class="purchase">{h.escape(benefits[lang])}</p>\n'
    extra = fr_typography(page.get("extra_html", ""), lang)
    if extra and not extra.endswith("\n"):
        extra += "\n"
    sibs = ""
    links = []
    for slug in page["siblings"]:
        s = find(pages, lang, slug)
        if s is None:
            raise ValueError(f"page {lang}/{page['slug'] or '(home)'!r}: sibling slug {slug!r} does not resolve to any page")
        links.append(f'      <li><a href="{pre}{language_path(lang)}{slug}/">{h.escape(fr_typography(s["question"], lang))}</a></li>')
    heading_id = "related-questions"
    if links:
        heading = LABELS[lang][4]
        sibs = f'    <nav aria-labelledby="{heading_id}">\n      <h2 id="{heading_id}">{heading}</h2>\n      <ul>\n' + "\n".join(links) + "\n      </ul>\n    </nav>\n"
    twin = find(pages, "fr" if lang == "en" else "en", page["pair"] or "")
    cluster = [p for p in pages if not p["slug"]] if not page["slug"] else [page] + ([twin] if twin else [])
    alts = "".join(f'  <link rel="alternate" hreflang="{p["lang"]}" href="{url_for(p)}">\n' for p in cluster)
    # x-default must point at the English member of this page's own cluster,
    # so the cluster names the root back reciprocally (Google "no return tags").
    x_default = url_for(page) if lang == "en" else (url_for(twin) if twin else f"{SITE['domain']}/")
    alts += f'  <link rel="alternate" hreflang="x-default" href="{x_default}">\n'
    cta = LABELS[lang][1]
    home_href = pre + language_path(lang) or "./"
    language_label = {'en':'Languages','fr':'Langues','fr-CA':'Langues','es':'Idiomas','pt-BR':'Idiomas','pt-PT':'Línguas','it':'Lingue','de':'Sprachen'}[lang]
    language_links = " · ".join(f'<a href="{url_for(p)}" lang="{p["lang"]}" hreflang="{p["lang"]}"' + (' aria-current="page"' if p["lang"] == lang else '') + f'>{LABELS[p["lang"]][0]}</a>' for p in cluster)
    # A question page gets a wordmark linking home; the home page is already there.
    wordmark = "" if not page["slug"] else (
        f'  <div class="wordmark"><a href="{home_href}">Booktionary</a></div>\n')
    privacy_label, licences_label = LABELS[lang][2:4]
    return f"""<!-- Generated by build.py from content.py. Do not edit this file by hand. -->
<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{q}</title>
  <meta name="description" content="{h.escape(fr_typography(page['description'], lang))}">
  <link rel="canonical" href="{url_for(page)}">
{alts}  <link rel="stylesheet" href="{pre}assets/style.css">
  <link rel="icon" href="{pre}assets/favicon-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="{pre}assets/icon-180.png">
  <script type="application/ld+json">
{jsonld(page)}
  </script>
</head>
<body>
  <nav class="languages" aria-label="{language_label}">{language_links}</nav>
{wordmark}  <main>
    <h1>{q}</h1>
{purchase}{hero}{body}
{extra}{sibs}    <p class="cta"><a href="{SITE['appstore_url']}">{cta}</a></p>
  </main>
  <footer>
    <a href="{home_href}">Booktionary</a> ·
    <a href="{pre}privacy.html">{privacy_label}</a> ·
    <a href="{pre}licenses.html">{licences_label}</a>
  </footer>
</body>
</html>
"""

def write_sitemap():
    urls = "\n".join(f"  <url><loc>{url_for(p)}</loc></url>" for p in PAGES)
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           f"{urls}\n</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write(xml)
    print("wrote sitemap.xml")

def main():
    for page in PAGES:
        path = out_path(page)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(render_page(page, PAGES))
        print("wrote", os.path.relpath(path, ROOT))
    # Old App Store/support URLs remain reachable, with a single French edition.
    alias = os.path.join(ROOT, "fr-CA", "index.html")
    os.makedirs(os.path.dirname(alias), exist_ok=True)
    with open(alias, "w", encoding="utf-8") as output:
        output.write('''<!-- Generated compatibility redirect -->
<!DOCTYPE html>
<html lang="fr"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Booktionary — Français</title>
<meta name="description" content="La page française de Booktionary est disponible à une seule adresse.">
<link rel="canonical" href="https://booktionary.io/fr/">
<meta http-equiv="refresh" content="0; url=../fr/">
</head><body><h1>Booktionary — Français</h1>
<p><a href="../fr/">Consulter le site et l’assistance en français.</a></p>
<p><a href="mailto:fredddv@hotmail.com">Contacter l’assistance</a></p>
</body></html>
''')
    print("wrote fr-CA/index.html compatibility redirect")
    write_sitemap()

if __name__ == "__main__":
    main()
