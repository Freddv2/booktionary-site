#!/usr/bin/env python3
"""Page-contract checks. Run after every build; exit code 0 means the site is shippable."""
import json, os, re, sys
from pathlib import Path

BANNED_PHRASES = ["as mentioned above", "see below", "as we said",
                  "as discussed", "see above", "comme indiqué plus haut",
                  "voir ci-dessus", "comme dit plus haut"]
APPSTORE = "https://apps.apple.com/app/id6796368335"
REQUIRED_BOTS = ["GPTBot", "ClaudeBot", "PerplexityBot", "Google-Extended", "CCBot"]

def text_of(html):
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))

def check_file(path):
    fails = []
    html = open(path, encoding="utf-8").read()
    if "<!-- Generated compatibility redirect -->" in html:
        valid = (Path(path).parent.name == "fr-CA"
                 and '<meta http-equiv="refresh" content="0; url=../fr/">' in html
                 and '<link rel="canonical" href="https://booktionary.io/fr/">' in html
                 and '<a href="../fr/">' in html
                 and 'mailto:fredddv@hotmail.com' in html
                 and (Path(path).parent.parent / 'fr/index.html').exists())
        return [] if valid else ["invalid French compatibility redirect"]
    title = re.search(r"<title>(.*?)</title>", html, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    if not title: fails.append("no <title>")
    if not h1: fails.append("no <h1>")
    if not desc: fails.append("no meta description")
    is_home = bool(re.search(r'"@type"\s*:\s*"SoftwareApplication"', html))
    if not is_home and title and h1 and title.group(1).strip() != h1.group(1).strip():
        fails.append("title and h1 differ")
    if re.search(r"<script(?![^>]*application/ld\+json)", html, re.I):
        fails.append("javascript present")
    if re.search(r'(src|href)="https?://(?!apps\.apple\.com|booktionary\.io)', html):
        fails.append("external asset or non-App-Store absolute link")
    appstore_links = re.findall(r'<a\s[^>]*href="' + re.escape(APPSTORE) + r'"[^>]*>', html)
    expected_store_links = 3 if is_home else 1
    if len(appstore_links) != expected_store_links:
        fails.append(f"expected exactly {expected_store_links} App Store link(s), found {len(appstore_links)}")
    if "apps.apple.com/ca/" in html:
        fails.append("storefront-pinned /ca/ App Store URL")
    body_text = text_of(html).lower()
    for phrase in BANNED_PHRASES:
        if phrase in body_text:
            fails.append(f"context-dependent phrase: {phrase!r}")
    if "abandoned" in body_text:
        fails.append("'abandoned' claim about competitors")
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
        try: json.loads(m.group(1))
        except json.JSONDecodeError as e: fails.append(f"invalid JSON-LD: {e}")
    fails += check_alternates(html)
    if is_home:
        fails += check_home_page(html)
    else:
        fails += check_question_page(html)
    return fails

def check_home_page(html):
    """Keep the approved design and App Store support essentials on every locale."""
    fails = []
    for asset in ("app-icon-main.png", "assets/language-expansion/", "-home.png", "-languages.png", "scanning.webp"):
        if asset not in html:
            fails.append(f"missing home asset {asset}")
    if "$1.99 USD" not in html:
        fails.append("missing confirmed US price")
    if "mailto:fredddv@hotmail.com" not in html:
        fails.append("missing support email")
    if html.count('class="device-frame"') < 2:
        fails.append("both app screenshots must be shown in phone frames")
    if "just your next chapter" in text_of(html).lower():
        fails.append("removed tagline has returned")
    from language_support import BOOK_LANGUAGES
    actual = re.findall(r'data-book-language="([^"]+)"', html)
    if len(actual) != len(BOOK_LANGUAGES) or set(actual) != {code for code, _, _ in BOOK_LANGUAGES}:
        fails.append("book-language list differs from the prepared release scope")
    if 'class="release-note wrap"' not in html:
        fails.append("missing upcoming-release availability notice")
    return fails

def check_question_page(html):
    fails = []
    text = text_of(html)
    words = len(text.split())
    if words < 90:
        fails.append(f"answer too thin ({words} words; needs 90+ to stand alone)")
    if not re.search(r"<nav", html):
        fails.append("no related-questions nav")
    return fails

def check_alternates(html):
    """Once both languages exist, every page carries self + twin + x-default."""
    if len(re.findall(r'<link rel="alternate"', html)) < 3:
        return ["missing hreflang alternates (need self, twin, x-default)"]
    return []

def check_xdefault(root):
    """x-default must equal the English member of the page's own cluster
    (itself if English, its twin if French), not the site root unconditionally
    -- otherwise every cluster's x-default points at a page that never names
    it back, and Google may discard the cluster for lack of a return tag."""
    fails = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if "index.html" not in filenames: continue
        path = os.path.join(dirpath, "index.html")
        html = open(path, encoding="utf-8").read()
        if "<!-- Generated compatibility redirect -->" in html: continue
        alts = re.findall(r'<link rel="alternate" hreflang="([\w-]+)" href="([^"]*)">', html)
        alt_map = {}
        for lang, href in alts:
            alt_map.setdefault(lang, href)
        rel = os.path.relpath(path, root)
        if "x-default" not in alt_map:
            fails.append(f"{rel}: missing x-default")
            continue
        if "en" not in alt_map:
            fails.append(f"{rel}: no English member found in this page's own cluster")
            continue
        if alt_map["x-default"] != alt_map["en"]:
            fails.append(f"{rel}: x-default ({alt_map['x-default']}) != English member of its own cluster ({alt_map['en']})")
    return fails

def check_pairs(root):
    """Every non-x-default, non-self hreflang alternate must point at a file
    that exists, and that file's own alternates must point back at this page."""
    fails = []
    pages = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if "index.html" in filenames:
            rel = os.path.relpath(os.path.join(dirpath, "index.html"), root)
            pages[rel] = Path(dirpath, "index.html").read_text(encoding="utf-8")

    def url_path(rel):
        d = os.path.dirname(rel)
        return d + "/" if d else ""

    def alt_paths(html):
        return {m.group(2) for m in re.finditer(
            r'<link rel="alternate" hreflang="([\w-]+)" href="https://booktionary\.io/([^"]*)"', html)
            if m.group(1) != "x-default"}

    for rel, html in pages.items():
        own_path = url_path(rel)
        for m in re.finditer(r'<link rel="alternate" hreflang="([\w-]+)" href="https://booktionary\.io/([^"]*)"', html):
            lang, path = m.group(1), m.group(2)
            if lang == "x-default": continue
            if path == own_path: continue
            target = os.path.join(path, "index.html") if path else "index.html"
            if target not in pages:
                fails.append(f"{rel}: hreflang {lang} points at missing {target}")
                continue
            if own_path not in alt_paths(pages[target]):
                fails.append(f"{rel}: hreflang {lang} -> {target} does not point back")
    return fails

def check_sitemap_and_robots(root):
    fails = []
    sm_path = os.path.join(root, "sitemap.xml")
    if not os.path.exists(sm_path):
        return ["sitemap.xml missing"]
    sm = open(sm_path, encoding="utf-8").read()
    listed = set(re.findall(r"<loc>(.*?)</loc>", sm))
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if "index.html" not in filenames: continue
        rel = os.path.relpath(dirpath, root).replace(os.sep, "/")
        if rel == "fr-CA" and "<!-- Generated compatibility redirect -->" in Path(dirpath, "index.html").read_text():
            continue
        url = "https://booktionary.io/" if rel == "." else f"https://booktionary.io/{rel}/"
        if url not in listed:
            fails.append(f"sitemap missing {url}")
    rb_path = os.path.join(root, "robots.txt")
    if not os.path.exists(rb_path):
        return fails + ["robots.txt missing"]
    rb = open(rb_path, encoding="utf-8").read()
    for bot in REQUIRED_BOTS:
        block = re.search(rf"User-agent:\s*{re.escape(bot)}\s*\nAllow:\s*/", rb, re.I)
        if not block:
            fails.append(f"robots.txt does not explicitly allow {bot}")
    if re.search(r"Disallow:\s*/\s*$", rb, re.M):
        fails.append("robots.txt disallows the whole site")
    return fails

def check_support_files(root):
    """Privacy policies and licenses are excluded from the generated-page contract
    walk below (they aren't build.py-generated pages), but they carry App Store
    consequences (Guideline 1.5, licence disclosure) and must not go missing or empty."""
    fails = []
    for fn in ("privacy.html", "privacy-android.html", "licenses.html"):
        p = os.path.join(root, fn)
        if not os.path.exists(p):
            fails.append(f"{fn} is missing")
        elif os.path.getsize(p) == 0:
            fails.append(f"{fn} is empty")
    return fails

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    problems, checked = {}, 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".html"): continue
            if fn in ("privacy.html", "privacy-android.html", "licenses.html"): continue
            p = os.path.join(dirpath, fn)
            checked += 1
            f = check_file(p)
            if f: problems[os.path.relpath(p, root)] = f
    pair_fails = check_pairs(root)
    xdefault_fails = check_xdefault(root)
    sitemap_fails = check_sitemap_and_robots(root)
    support_fails = check_support_files(root)
    for path, fails in sorted(problems.items()):
        print(f"FAIL {path}")
        for f in fails: print(f"       {f}")
    if pair_fails:
        print("FAIL hreflang reciprocity")
        for f in pair_fails: print(f"       {f}")
    if xdefault_fails:
        print("FAIL x-default")
        for f in xdefault_fails: print(f"       {f}")
    if sitemap_fails:
        print("FAIL sitemap and robots")
        for f in sitemap_fails: print(f"       {f}")
    if support_fails:
        print("FAIL support files")
        for f in support_fails: print(f"       {f}")
    print(f"\n{checked} page(s) checked, {len(problems)} failing")
    return 1 if (problems or pair_fails or xdefault_fails or sitemap_fails or support_fails) else 0

if __name__ == "__main__":
    sys.exit(main())
