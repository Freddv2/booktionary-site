"""Platform facts sourced from the approved 2026-10-26 Google Play copy.

Kurmanji has a translated website but no corresponding Play listing; its button
opens English. Keep platform promises separate from the iPhone-specific copy.
"""
from html import escape
import json
from pathlib import Path
from urllib.parse import urlencode
COPY=json.loads(Path(__file__).with_name('platform_copy.json').read_text())

def play_url_for(locale):
    return 'https://play.google.com/store/apps/details?'+urlencode({'id':'com.freddv2.booktionary','hl':COPY[locale]['playLocale'].replace('-','_')})

def android_details(locale, privacy_label, prefix):
    sections=[]
    for block in COPY[locale]['androidBlocks']:
        if '\n' in block:
            title,body=block.split('\n',1)
            sections.append(f'<h3>{escape(title)}</h3><p>{escape(body)}</p>')
        else: sections.append(f'<p>{escape(block)}</p>')
    return ('<section class="bt-wrap bt-platform" id="android"><details><summary>Android</summary>'
            +''.join(sections)
            +f'<p><a href="{prefix}privacy-android.html">Android · {escape(privacy_label)}</a></p></details></section>')
