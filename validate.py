#!/usr/bin/env python3
"""Page-contract checks. Run after every build; exit code 0 means the site is shippable."""
import json, os, re, sys

BANNED_PHRASES = ["as mentioned above", "see below", "as we said",
                  "as discussed", "see above", "comme indiqué plus haut",
                  "voir ci-dessus", "comme dit plus haut"]
APPSTORE = "https://apps.apple.com/app/id6796368335"

def text_of(html):
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))

def check_file(path):
    fails = []
    html = open(path, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", html, re.S)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    desc = re.search(r'<meta name="description" content="(.*?)"', html, re.S)
    if not title: fails.append("no <title>")
    if not h1: fails.append("no <h1>")
    if not desc: fails.append("no meta description")
    if title and h1 and title.group(1).strip() != h1.group(1).strip():
        fails.append("title and h1 differ")
    if re.search(r"<script(?![^>]*application/ld\+json)", html, re.I):
        fails.append("javascript present")
    if re.search(r'(src|href)="https?://(?!apps\.apple\.com|booktionary\.io)', html):
        fails.append("external asset or non-App-Store absolute link")
    appstore_links = re.findall(r'<a\s[^>]*href="' + re.escape(APPSTORE) + r'"[^>]*>', html)
    if len(appstore_links) != 1:
        fails.append(f"expected exactly 1 App Store link, found {len(appstore_links)}")
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
    root = os.path.dirname(os.path.abspath(__file__))
    parent = os.path.dirname(os.path.abspath(path))
    is_home = parent in (root, os.path.join(root, "fr"))
    if not is_home:
        fails += check_question_page(html)
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

def check_pairs(root):
    """Every non-x-default, non-self hreflang alternate must point at a file
    that exists, and that file's own alternates must point back at this page."""
    fails = []
    pages = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if "index.html" in filenames:
            rel = os.path.relpath(os.path.join(dirpath, "index.html"), root)
            pages[rel] = open(os.path.join(dirpath, "index.html"), encoding="utf-8").read()

    def url_path(rel):
        d = os.path.dirname(rel)
        return d + "/" if d else ""

    def alt_paths(html):
        return {m.group(2) for m in re.finditer(
            r'<link rel="alternate" hreflang="(\w+)" href="https://booktionary\.io/([^"]*)"', html)
            if m.group(1) != "x-default"}

    for rel, html in pages.items():
        own_path = url_path(rel)
        for m in re.finditer(r'<link rel="alternate" hreflang="(\w+)" href="https://booktionary\.io/([^"]*)"', html):
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

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    problems, checked = {}, 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for fn in filenames:
            if not fn.endswith(".html"): continue
            if fn in ("privacy.html", "licenses.html"): continue
            p = os.path.join(dirpath, fn)
            checked += 1
            f = check_file(p)
            if f: problems[os.path.relpath(p, root)] = f
    pair_fails = check_pairs(root)
    for path, fails in sorted(problems.items()):
        print(f"FAIL {path}")
        for f in fails: print(f"       {f}")
    if pair_fails:
        print("FAIL hreflang reciprocity")
        for f in pair_fails: print(f"       {f}")
    print(f"\n{checked} page(s) checked, {len(problems)} failing")
    return 1 if (problems or pair_fails) else 0

if __name__ == "__main__":
    sys.exit(main())
