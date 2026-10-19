"""Canonical website editions and the released app/store locales they serve.

Regional English, French and Spanish listings share a language page. Portuguese
keeps two editions; Chinese keeps both scripts. Kurmanji is Latin-script only.
"""
STORE_TO_WEB = {
    'cs': 'cs', 'da': 'da', 'de-DE': 'de', 'el': 'el',
    'en-AU': 'en', 'en-CA': 'en', 'en-GB': 'en', 'en-US': 'en',
    'es-ES': 'es', 'es-MX': 'es', 'fr-CA': 'fr', 'fr-FR': 'fr',
    'id': 'id', 'it': 'it', 'ja': 'ja', 'ko': 'ko', 'ms': 'ms',
    'nl-NL': 'nl', 'no': 'nb', 'pl': 'pl', 'pt-BR': 'pt-BR',
    'pt-PT': 'pt-PT', 'ro': 'ro', 'ru': 'ru', 'sv': 'sv',
    'th': 'th', 'tr': 'tr', 'uk': 'uk', 'vi': 'vi',
    'zh-Hans': 'zh-Hans', 'zh-Hant': 'zh-Hant',
}
INTERFACE_TO_WEB = {code: code for code in (
    'en', 'fr', 'es', 'it', 'de', 'da', 'nl', 'nb', 'ru', 'sv', 'pl',
    'cs', 'ja', 'th', 'ro', 'vi', 'el', 'tr', 'id', 'zh-Hans',
    'zh-Hant', 'ko', 'uk', 'ku', 'ms',
)}
# The app has one Portuguese interface. Both regional website editions exist.
INTERFACE_TO_WEB['pt'] = 'pt-PT'
WEB_LOCALES = tuple(dict.fromkeys((*STORE_TO_WEB.values(), *INTERFACE_TO_WEB.values())))
