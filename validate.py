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
    for path, fails in sorted(problems.items()):
        print(f"FAIL {path}")
        for f in fails: print(f"       {f}")
    print(f"\n{checked} page(s) checked, {len(problems)} failing")
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
