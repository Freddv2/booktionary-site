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

CAMPAIGNS = {
    'en': 'booktionary_web_en', 'fr': 'booktionary_web_fr',
    'de': 'booktionary_web_de', 'es': 'booktionary_web_es',
    'it': 'booktionary_web_it', 'pt-BR': 'booktionary_web_pt_br',
    'pt-PT': 'booktionary_web_pt_pt',
    'cs': 'booktionary_web_cs', 'da': 'booktionary_web_da',
    'el': 'booktionary_web_el', 'id': 'booktionary_web_id',
    'ja': 'booktionary_web_ja', 'ko': 'booktionary_web_ko',
    'ku': 'booktionary_web_ku', 'ms': 'booktionary_web_ms',
    'nb': 'booktionary_web_nb', 'nl': 'booktionary_web_nl',
    'pl': 'booktionary_web_pl', 'ro': 'booktionary_web_ro',
    'ru': 'booktionary_web_ru', 'sv': 'booktionary_web_sv',
    'th': 'booktionary_web_th', 'tr': 'booktionary_web_tr',
    'uk': 'booktionary_web_uk', 'vi': 'booktionary_web_vi',
    'zh-Hans': 'booktionary_web_zh_hans', 'zh-Hant': 'booktionary_web_zh_hant',
}
class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.store = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'a' and 'apps.apple.com' in attrs.get('href', ''):
            self.store.append(attrs['href'])

class HomeRefreshTests(unittest.TestCase):
    def test_settings_path_and_phone_fallback_are_localized(self):
        from home_ui import HOME_UI
        paths = {
            'en': 'Settings → App language', 'fr': 'Réglages → Langue de l’app',
            'es': 'Ajustes → Idioma de la app', 'pt-BR': 'Ajustes → Idioma do app',
            'pt-PT': 'Definições → Língua da app',
            'it': 'Impostazioni → Lingua dell’app', 'de': 'Einstellungen → App-Sprache',
        }
        for locale, path in paths.items():
            with self.subTest(locale=locale):
                note = HOME_UI[locale]['interface_note']
                self.assertIn(path, note)
                self.assertIn('26', note)
                self.assertTrue(any(word in note.lower() for word in ('english', 'anglais', 'inglés', 'inglês', 'inglese', 'englisch')))

    def test_every_purchase_link_and_app_schema_uses_page_language_campaign(self):
        for page in PAGES:
            with self.subTest(lang=page['lang'], slug=page['slug']):
                expected_url = ('https://apps.apple.com/app/apple-store/id6796368335'
                                f'?pt=129235559&ct={CAMPAIGNS[page["lang"]]}&mt=8')
                rendered = build.render_page(page, PAGES)
                parser = Links()
                parser.feed(rendered)
                self.assertEqual(parser.store, [expected_url] * (1 if page['slug'] else 2))
                if not page['slug']:
                    schema = json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>', rendered, re.S)[1])
                    self.assertIn(expected_url, schema['installUrl'])
                    self.assertIn(expected_url, [offer['url'] for offer in schema['offers']])

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
