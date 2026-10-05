#!/usr/bin/env python3
"""Render content.py to committed static HTML. No runtime dependencies."""
import html as h, json, os, re
from content import SITE, PAGES

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
                "inLanguage": ["en", "fr", "fr-CA", "es", "pt", "it", "de"],
                "description": page["description"]}
    return json.dumps(data, ensure_ascii=False, indent=1).replace("<", "\\u003c")

def fr_typography(text, lang):
    """French typographic convention: a narrow no-break space before ? ! ; :
    instead of an ASCII space, so the punctuation cannot wrap onto its own line."""
    if not lang.startswith("fr"):
        return text
    return re.sub(r" ([?!;:])", " \\1", text)

def render_page(page, pages):
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
    write_sitemap()

if __name__ == "__main__":
    main()
