"""Protect both stores and the platform-specific promises on every homepage."""
import json
import re
import unittest
from html.parser import HTMLParser
from urllib.parse import urlparse, parse_qs
import build
from content import PAGES

class Anchors(HTMLParser):
    def __init__(self):
        super().__init__(); self.links=[]
    def handle_starttag(self, tag, attrs):
        if tag=='a': self.links.append(dict(attrs).get('href',''))

class PlatformsTest(unittest.TestCase):
    def test_each_home_offers_both_platforms_and_explains_android(self):
        for page in (p for p in PAGES if not p['slug']):
            with self.subTest(locale=page['lang']):
                rendered=build.render_page(page,PAGES)
                links=Anchors();links.feed(rendered)
                play=[u for u in links.links if urlparse(u).netloc=='play.google.com']
                self.assertGreaterEqual(len(play),2)
                self.assertTrue(all(parse_qs(urlparse(u).query)['id']==['com.freddv2.booktionary'] for u in play))
                self.assertIn('id="android"',rendered)
                self.assertRegex(rendered, r'Android\w* 12')
                self.assertRegex(rendered,r'8\s*(GB|Go|ГБ|ГБ|جيجابايت)')
                self.assertIn('ML Kit',rendered)
                self.assertIn('privacy-android.html',rendered)
                lead=re.search(r'<p class="bt-lead">(.*?)</p>',rendered)[1]
                self.assertNotIn('iPhone',lead)
                self.assertNotIn('Android',lead)
                schema=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',rendered,re.S)[1])
                self.assertEqual(len(schema['installUrl']),2)
                self.assertEqual(len(schema['offers']),2)
                self.assertIn('Android 8.0 or later',schema['operatingSystem'])
