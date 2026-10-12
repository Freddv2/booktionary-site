#!/usr/bin/env python3
"""Render content.py to committed static HTML. No runtime dependencies."""
import html as h, json, os, re
from content import SITE, PAGES
from home_ui import HOME_UI
from home_refresh import REFRESH
from language_support import BOOK_LANGUAGES, INTERFACE_LOCALES

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
    """Render the approved reading-first homepage in each supported locale."""
    lang = page['lang']
    ui = dict(HOME_UI[lang], **REFRESH[lang])
    pre = depth_prefix(page)
    esc = lambda value: h.escape(fr_typography(value, lang))
    homes = [p for p in pages if not p['slug']]
    alts = ''.join(f'  <link rel="alternate" hreflang="{p["lang"]}" href="{url_for(p)}">\n' for p in homes)
    alts += '  <link rel="alternate" hreflang="x-default" href="https://booktionary.io/">\n'
    store_url = h.escape(SITE['appstore_url'], quote=True)

    def download_button():
        return (f'<a class="bt-download" href="{store_url}"><span><small>{esc(ui["download"])}</small>'
                '<strong>App Store</strong></span><span aria-hidden="true">↗</span></a>')

    def heading(lines):
        return f'{esc(lines[0])}<br><em>{esc(lines[1])}</em>'

    steps = ''.join(f'<article class="bt-step"><span>0{i+1}</span><h3>{esc(title)}</h3><p>{esc(body)}</p></article>'
                    for i, (title, body) in enumerate(ui['steps']))
    proof_bodies = (ui['proof_language'], ui['context_short'], ui['benefits'][0][1], ui['benefits'][2][1])
    proof = ''.join(f'<article><h3>{esc(title)}</h3><p>{esc(body)}</p>'
                    + (f'<a href="#meaning">{esc(ui["context_link"])} ↓</a>' if i == 1 else '') + '</article>'
                    for i, (title, body) in enumerate(zip(ui['proof_titles'], proof_bodies)))
    features = ''
    for i, (title, body) in enumerate(ui['features']):
        detail = (f'<p class="bt-small">{esc(ui["context_note"])}</p>' if i == 0 else
                  '<div class="bt-word-shapes"><span lang="en">running → run</span><span lang="fr">mangeaient → manger</span></div>' if i == 1 else
                  f'<p class="bt-small">{esc(ui["word_note"])}</p>')
        features += f'<article class="bt-feature"><h3>{esc(title)}</h3><p>{esc(body)}</p>{detail}</article>'
    language_rows = [f'<li data-book-language="{code}"><span lang="{code}">{esc(name)}'
                     + (f'<small lang="en">{esc(english_name)}</small>' if code != 'en' else '')
                     + f'</span><span class="bt-availability">{esc(ui["built_in"] if code == "en" else ui["download_pack"])}</span></li>'
                     for code, name, english_name in BOOK_LANGUAGES]
    benefits = ''.join(f'<article><h3>{esc(title)}</h3><p>{esc(body)}</p></article>' for title, body in ui['benefits'])
    faq_items = list(ui['faqs'])
    faq_items[2] = ui['translation_faq']
    faq_items.insert(3, (ui['context_question'], ui['features'][0][1] + ' ' + ui['context_note']))
    faqs = ''.join(f'<details><summary>{esc(question)}</summary><p>{esc(answer)}</p></details>' for question, answer in faq_items)
    locale_links = ''.join(f'<a href="{url_for(p)}" lang="{p["lang"]}" hreflang="{p["lang"]}"'
                          + (' aria-current="page"' if p['lang'] == lang else '')
                          + f'>{LABELS[p["lang"]][0]}</a>' for p in homes)
    related_links = ''.join(f'<a href="{pre}{language_path(lang)}{slug}/">{esc(find(pages, lang, slug)["question"])} ↗</a>' for slug in page['siblings'])
    related = (f'<nav class="bt-reading bt-wrap" aria-label="{esc(ui["related"])}"><p class="bt-kicker">{esc(ui["related"])}</p>'
               f'<div class="bt-reading-links">{related_links}</div></nav>') if related_links else ''
    support = fr_typography(page.get('extra_html', ''), lang)
    return f'''<!-- Generated by build.py from content.py, home_ui.py and home_refresh.py. Do not edit this file by hand. -->
<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(page['question'])}</title>
  <meta name="description" content="{esc(page['description'])}">
  <link rel="canonical" href="{url_for(page)}">
{alts}  <link rel="stylesheet" href="{pre}assets/home.css">
  <link rel="icon" href="{pre}assets/favicon-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="{pre}assets/icon-180.png">
  <script type="application/ld+json">
{jsonld(page)}
  </script>
</head>
<body><div id="bt-refresh">
  <header class="bt-header bt-wrap">
    <a class="bt-brand" href="#top" aria-label="Booktionary"><img src="{pre}assets/app-icon-main.png" alt="" width="37" height="37"><span>Booktionary</span></a>
    <nav aria-label="{NAV_LABELS[lang][0]}"><a href="#how-it-works">{esc(ui['nav'][0])}</a><a href="#meaning">{esc(ui['meaning_nav'])}</a><a href="#languages">{esc(ui['nav'][1])}</a></nav>
    <a class="bt-header-get" href="{store_url}">{esc(ui['get'])} ↗</a>
  </header>
  <main id="top">
    <section class="bt-hero bt-wrap" aria-labelledby="hero-title">
      <div><p class="bt-kicker">{esc(ui['eyebrow'])}</p>
        <h1 id="hero-title">{esc(ui['title'][0])}<br>{esc(ui['title'][1])} <em>{esc(ui['title'][2])}</em></h1>
        <p class="bt-lead">{esc(ui['lead'])}</p>
        <div class="bt-actions">{download_button()}<a class="bt-text-link" href="#how-it-works">{esc(ui['see'])} ↓</a></div>
        <p class="bt-purchase">{esc(ui['requirements'])} · $1.99 USD</p>
      </div>
      <figure class="bt-hero-photo"><img src="{pre}assets/scanning.webp" alt="{esc(ui['photo_caption'])}" width="851" height="1848" fetchpriority="high"><figcaption>{esc(ui['photo'])}</figcaption></figure>
    </section>
    <section class="bt-how bt-wrap" id="how-it-works" aria-labelledby="how-title">
      <div class="bt-how-head"><div><p class="bt-kicker">{esc(ui['how_kicker'])}</p><h2 id="how-title">{heading(ui['how_heading'])}</h2></div><p>{esc(ui['how_lead'])}</p></div>
      <div class="bt-steps">{steps}</div>
    </section>
    <section class="bt-proof bt-wrap" id="proof" aria-labelledby="proof-title"><p class="bt-kicker" id="proof-title">{esc(ui['proof_kicker'])}</p><div class="bt-proof-grid">{proof}</div></section>
    <section class="bt-meaning" id="meaning" aria-labelledby="meaning-title"><div class="bt-wrap bt-meaning-grid">
      <div><p class="bt-kicker">{esc(ui['meaning_kicker'])}</p><h2 id="meaning-title">{heading(ui['meaning_heading'])}</h2>{features}</div>
      <figure class="bt-native bt-photo-example"><div class="bt-reading-photo"><img src="{pre}assets/booktionary-real-book-photo.jpg" alt="{esc(ui['example_alt'])}" width="667" height="1100" loading="lazy"></div><figcaption>{esc(ui['example_caption'][0])}<br>{esc(ui['example_caption'][1])}</figcaption></figure>
    </div></section>
    <section class="bt-languages bt-wrap" id="languages" aria-labelledby="language-title">
      <div class="bt-language-intro"><div><p class="bt-kicker">{esc(ui['language_kicker'])}</p><h2 id="language-title">{heading(ui['language_heading'])}</h2></div><p>{esc(ui['language_lead'])}</p></div>
      <ul class="bt-language-list">{''.join(language_rows[:6])}</ul>
      <details class="bt-all-languages"><summary>{esc(ui['all_languages'])}</summary><ul class="bt-language-list">{''.join(language_rows[6:])}</ul></details>
      <div class="bt-language-notes"><article><h3>{esc(ui['translation_title'])}</h3><p>{esc(ui['translation'])}</p></article><article><h3>{esc(ui['interface_title'])}</h3><p>{esc(ui['interface_note'])}</p></article></div>
      <p class="bt-small bt-scope">{esc(ui['language_scope'])}</p>
      <aside class="bt-upcoming"><div><p class="bt-kicker">{esc(ui['upcoming_kicker'])}</p><h3>{esc(ui['upcoming_title'])}</h3></div><div><p>{esc(ui['upcoming_body'])}</p><p class="bt-small">{esc(ui['upcoming_note'])}</p></div></aside>
    </section>
    <section class="bt-quiet"><div class="bt-wrap bt-quiet-grid"><div><p class="bt-kicker">{esc(ui['quiet_kicker'])}</p><h2>{esc(ui['quiet_title'][0])}<br>{esc(ui['quiet_title'][1])}<br><em>{esc(ui['quiet_title'][2])}</em></h2></div><div>{benefits}</div></div></section>
    <section class="bt-faq bt-wrap" id="questions" aria-labelledby="questions-title"><div><p class="bt-kicker">{esc(ui['questions_kicker'])}</p><h2 id="questions-title">{heading(ui['questions_title'])}</h2><a class="bt-support" href="mailto:fredddv@hotmail.com">{esc(ui['support'])} ↗</a></div><div>{faqs}</div></section>
    <section class="bt-support-panel bt-wrap" id="support" aria-label="{NAV_LABELS[lang][2]}">{support}</section>
{related}
    <section class="bt-last"><p class="bt-kicker">{esc(ui['final_kicker'])}</p><h2>{heading(ui['final_title'])}</h2>{download_button()}<p class="bt-purchase">{esc(ui['price'])} · {esc(ui['requirements'])}</p></section>
  </main>
  <footer class="bt-wrap"><div class="bt-footer"><a class="bt-brand" href="#top"><img src="{pre}assets/app-icon-main.png" alt="" width="29" height="29" loading="lazy">Booktionary</a><nav aria-label="{NAV_LABELS[lang][1]}"><a href="{pre}privacy.html">{esc(ui['privacy'])}</a><a href="{pre}licenses.html">{esc(ui['licences'])}</a><a href="#support">{NAV_LABELS[lang][2]}</a></nav></div><div class="bt-footer-bottom"><p>{esc(ui['footer_line'])}</p><nav aria-label="{esc(ui['site_languages'])}">{locale_links}</nav></div><p class="bt-small bt-credit">{esc(ui['credit'])}</p></footer>
</div></body>
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
{extra}{sibs}    <p class="cta"><a href="{h.escape(SITE['appstore_url'], quote=True)}">{cta}</a></p>
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
