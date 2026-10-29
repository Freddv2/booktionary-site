"""Approved reading examples, with matching interface language per edition."""
import json
from pathlib import Path

ARTWORK = json.loads((Path(__file__).resolve().parent /
                      'reading_artwork_release.json').read_text())['locales']
