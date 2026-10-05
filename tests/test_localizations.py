import json
from pathlib import Path
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build
import validate

class LocalizedSiteTests(unittest.TestCase):
    def test_regional_home_has_its_own_url_and_asset_depth(self):
        page = dict(lang='fr-CA', slug='')
        self.assertEqual(build.url_for(page), 'https://booktionary.io/fr-CA/')
        self.assertEqual(build.out_path(page), str(Path(build.ROOT)/'fr-CA/index.html'))
        self.assertEqual(build.depth_prefix(page), '../')

    def test_home_hreflang_cluster_names_every_translated_home(self):
        pages = [dict(lang=lang, slug='', pair='', question='Booktionary',
                      description='Camera dictionary', paragraphs=[], siblings=[])
                 for lang in ('en', 'fr', 'fr-CA', 'de')]
        html = build.render_page(pages[2], pages)
        for lang, path in [('en',''), ('fr','fr/'), ('fr-CA','fr-CA/'), ('de','de/')]:
            self.assertIn(f'hreflang="{lang}" href="https://booktionary.io/{path}"', html)
        self.assertIn('hreflang="x-default" href="https://booktionary.io/"', html)
        self.assertIn('lang="fr-CA"', html)

    def test_validator_rejects_missing_regional_alternate(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root,'index.html').write_text('<link rel="alternate" hreflang="pt-BR" href="https://booktionary.io/pt-BR/">')
            self.assertTrue(any('missing pt-BR/index.html' in f for f in validate.check_pairs(root)))

    def test_validator_rejects_regional_alternate_without_return_tag(self):
        with tempfile.TemporaryDirectory() as root:
            Path(root,'index.html').write_text('<link rel="alternate" hreflang="fr-CA" href="https://booktionary.io/fr-CA/">')
            Path(root,'fr-CA').mkdir()
            Path(root,'fr-CA/index.html').write_text('<link rel="alternate" hreflang="fr-CA" href="https://booktionary.io/fr-CA/">')
            self.assertTrue(any('does not point back' in f for f in validate.check_pairs(root)))

if __name__ == '__main__': unittest.main()
