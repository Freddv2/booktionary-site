"""Protect the reading flow and downloadable app destination."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build
from content import PAGES

TRACKED_URL = 'https://apps.apple.com/app/apple-store/id6796368335?pt=129235559&ct=booktionary_website_ios&mt=8'
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.store = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'apps.apple.com' in attrs.get('href', ''):
            self.store.append(attrs['href'])

class HomeRefreshTests(unittest.TestCase):
    def test_every_purchase_link_and_app_schema_preserves_campaign(self):
        for page in PAGES:
            with self.subTest(lang=page['lang'], slug=page['slug']):
                rendered = build.render_page(page, PAGES)
                parser = Links()
                parser.feed(rendered)
                self.assertEqual(parser.store, [TRACKED_URL] * (1 if page['slug'] else 3))
                if not page['slug']:
                    schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', rendered, re.S)[1])
                    self.assertEqual(schema['installUrl'], TRACKED_URL)
                    self.assertEqual(schema['offers']['url'], TRACKED_URL)

    def test_localized_home_preserves_support_and_reading_first_order(self):
        for page in (p for p in PAGES if not p['slug']):
            with self.subTest(lang=page['lang']):
                rendered = build.render_page(page, PAGES)
                self.assertIn('id="proof"', rendered)
                self.assertLess(rendered.index('id="how-it-works"'), rendered.index('id="proof"'))
                self.assertLess(rendered.index('id="proof"'), rendered.index('id="meaning"'))
                self.assertIn('booktionary-real-book-photo.jpg', rendered)
                self.assertIn('id="support"', rendered)
                self.assertIn('mailto:fredddv@hotmail.com', rendered)
                self.assertIn('iOS 26', rendered)
                self.assertIn('class="bt-definition"', rendered)
                self.assertNotIn('Coming in version 1.0.11', rendered)
                self.assertNotIn('class="release-note wrap"', rendered)
                self.assertNotIn('class="language-carousel"', rendered)
                self.assertEqual(len(re.findall('data-book-language=', rendered)), 24)
