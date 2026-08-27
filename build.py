#!/usr/bin/env python3
"""Render content.py to committed static HTML. No runtime dependencies."""
import html as h, json, os, sys
from content import SITE, PAGES

ROOT = os.path.dirname(os.path.abspath(__file__))

def url_for(page):
    if page["lang"] == "en":
        return f"{SITE['domain']}/{page['slug']}/" if page["slug"] else f"{SITE['domain']}/"
    return f"{SITE['domain']}/fr/{page['slug']}/" if page["slug"] else f"{SITE['domain']}/fr/"

def out_path(page):
    parts = [ROOT]
    if page["lang"] == "fr": parts.append("fr")
    if page["slug"]: parts.append(page["slug"])
    return os.path.join(*parts, "index.html")

def depth_prefix(page):
    n = (1 if page["lang"] == "fr" else 0) + (1 if page["slug"] else 0)
    return "../" * n if n else ""

def find(pages, lang, slug):
    for p in pages:
        if p["lang"] == lang and p["slug"] == slug: return p
    return None

def jsonld(page, pages):
    if page["slug"]:
        data = {"@context": "https://schema.org", "@type": "FAQPage",
                "mainEntity": [{"@type": "Question", "name": page["question"],
                    "acceptedAnswer": {"@type": "Answer",
                                       "text": " ".join(page["paragraphs"])}}]}
    else:
        data = {"@context": "https://schema.org", "@type": "SoftwareApplication",
                "name": "Booktionary", "applicationCategory": "ReferenceApplication",
                "operatingSystem": "iOS 17", "url": url_for(page),
                "inLanguage": ["en", "fr"],
                "offers": {"@type": "Offer", "price": "1.99", "priceCurrency": "USD"}}
    return json.dumps(data, ensure_ascii=False, indent=1)

def render_page(page, pages):
    pre = depth_prefix(page)
    q = h.escape(page["question"])
    body = "\n".join(f"    <p>{h.escape(t)}</p>" for t in page["paragraphs"])
    sibs = ""
    links = []
    for slug in page["siblings"]:
        s = find(pages, page["lang"], slug)
        if s: links.append(f'      <li><a href="{pre}{"fr/" if page["lang"]=="fr" else ""}{slug}/">{h.escape(s["question"])}</a></li>')
    if links:
        heading = "Related questions" if page["lang"] == "en" else "Questions liées"
        sibs = f'    <nav aria-label="{heading}">\n      <h2>{heading}</h2>\n      <ul>\n' + "\n".join(links) + "\n      </ul>\n    </nav>\n"
    twin = find(pages, "fr" if page["lang"] == "en" else "en", page["pair"] or "")
    alts = f'  <link rel="alternate" hreflang="{page["lang"]}" href="{url_for(page)}">\n'
    if twin:
        alts += f'  <link rel="alternate" hreflang="{twin["lang"]}" href="{url_for(twin)}">\n'
    alts += f'  <link rel="alternate" hreflang="x-default" href="{SITE["domain"]}/">\n'
    cta = "Booktionary on the App Store" if page["lang"] == "en" else "Booktionary sur l'App Store"
    home_href = (pre + "fr/") if page["lang"] == "fr" else (pre or "./")
    privacy_label = "Privacy" if page["lang"] == "en" else "Confidentialité"
    licences_label = "Licences"
    return f"""<!DOCTYPE html>
<html lang="{page['lang']}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{q}</title>
  <meta name="description" content="{h.escape(page['description'])}">
  <link rel="canonical" href="{url_for(page)}">
{alts}  <link rel="stylesheet" href="{pre}assets/style.css">
  <script type="application/ld+json">
{jsonld(page, pages)}
  </script>
</head>
<body>
  <main>
    <h1>{q}</h1>
{body}
{sibs}    <p class="cta"><a href="{SITE['appstore_url']}">{cta}</a></p>
  </main>
  <footer>
    <a href="{home_href}">Booktionary</a> ·
    <a href="{pre}privacy.html">{privacy_label}</a> ·
    <a href="{pre}licenses.html">{licences_label}</a>
  </footer>
</body>
</html>
"""

def main():
    for page in PAGES:
        path = out_path(page)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        open(path, "w", encoding="utf-8").write(render_page(page, PAGES))
        print("wrote", os.path.relpath(path, ROOT))

if __name__ == "__main__":
    main()
