"""All supported reader languages need a usable, linked search destination."""
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build
from content import PAGES

EXPECTED_HOMES = {
    'en', 'fr', 'es', 'pt-BR', 'pt-PT', 'it', 'de', 'cs', 'da', 'el',
    'id', 'ja', 'ko', 'ku', 'ms', 'nb', 'nl', 'pl', 'ro', 'ru', 'sv',
    'th', 'tr', 'uk', 'vi', 'zh-Hans', 'zh-Hant',
}


class PageMetadata(HTMLParser):
    def __init__(self):
        super().__init__()
        self.alternates = {}
        self.links = []
        self.description = None
        self.canonical = None

    def handle_starttag(self, tag, attributes):
        a = dict(attributes)
        if tag == 'link' and a.get('rel') == 'alternate':
            self.alternates[a['hreflang']] = a['href']
        if tag == 'link' and a.get('rel') == 'canonical':
            self.canonical = a['href']
        if tag == 'meta' and a.get('name') == 'description':
            self.description = a['content']
        if tag == 'a':
            self.links.append(a.get('href', ''))


class SearchCoverageTests(unittest.TestCase):
    def test_every_supported_language_has_a_home(self):
        self.assertEqual({p['lang'] for p in PAGES if not p['slug']}, EXPECTED_HOMES)

    def test_every_home_is_reciprocal_and_uses_its_own_description(self):
        homes = [p for p in PAGES if not p['slug']]
        expected = {p['lang']: build.url_for(p) for p in homes}
        expected['x-default'] = 'https://booktionary.io/'
        for page in homes:
            with self.subTest(locale=page['lang']):
                rendered = build.render_page(page, PAGES)
                parsed = PageMetadata()
                parsed.feed(rendered)
                self.assertEqual(parsed.alternates, expected)
                self.assertEqual(parsed.canonical, build.url_for(page))
                schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', rendered, re.S)[1])
                self.assertEqual(parsed.description, schema['description'])
                self.assertTrue(parsed.description)
                self.assertIn('mailto:fredddv@hotmail.com', parsed.links)
                for target in expected.values():
                    self.assertIn(target, parsed.links)

    def test_all_store_locales_and_interface_choices_resolve(self):
        from site_locales import STORE_TO_WEB, INTERFACE_TO_WEB
        self.assertEqual(len(STORE_TO_WEB), 31)
        self.assertEqual(len(INTERFACE_TO_WEB), 26)
        self.assertEqual(set(STORE_TO_WEB.values()) | set(INTERFACE_TO_WEB.values()), EXPECTED_HOMES)
        self.assertEqual(STORE_TO_WEB['fr-CA'], 'fr')
        self.assertEqual(STORE_TO_WEB['en-AU'], 'en')
        self.assertEqual(STORE_TO_WEB['es-MX'], 'es')
        self.assertEqual(STORE_TO_WEB['no'], 'nb')
        self.assertEqual(INTERFACE_TO_WEB['ku'], 'ku')
        self.assertNotEqual(STORE_TO_WEB['zh-Hans'], STORE_TO_WEB['zh-Hant'])
        self.assertNotEqual(STORE_TO_WEB['pt-BR'], STORE_TO_WEB['pt-PT'])


if __name__ == '__main__':
    unittest.main()
