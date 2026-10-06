"""Public support scope for the upcoming expanded-language release.

Keep book languages separate from interface locales and English translation
targets. The catalog is checked against this scope by the site test suite.
"""
BOOK_LANGUAGES = (
    ("en", "English", "English"),
    ("fr", "Français", "French"),
    ("es", "Español", "Spanish"),
    ("pt", "Português", "Portuguese"),
    ("it", "Italiano", "Italian"),
    ("de", "Deutsch", "German"),
    ("da", "Dansk", "Danish"),
    ("nl", "Nederlands", "Dutch"),
    ("nb", "Norsk (bokmål)", "Norwegian Bokmål"),
    ("ru", "Русский", "Russian"),
    ("sv", "Svenska", "Swedish"),
    ("pl", "Polski", "Polish"),
    ("cs", "Čeština", "Czech"),
    ("ja", "日本語", "Japanese"),
    ("th", "ไทย", "Thai"),
    ("ro", "Română", "Romanian"),
    ("vi", "Tiếng Việt", "Vietnamese"),
    ("tr", "Türkçe", "Turkish"),
    ("id", "Bahasa Indonesia", "Indonesian"),
    ("zh", "中文 · 简体 / 繁體", "Chinese — Simplified / Traditional"),
    ("ko", "한국어", "Korean"),
    ("uk", "Українська", "Ukrainian"),
    ("ku", "Kurdî (Kurmancî)", "Kurdish — Kurmanji, Latin script"),
    ("ms", "Bahasa Melayu", "Malay — Rumi, Latin script"),
)
TRANSLATION_TARGETS = tuple(code for code, _, _ in BOOK_LANGUAGES if code != "en") + ("el",)
INTERFACE_LOCALES = (
    "en", "fr", "fr-CA", "es", "pt", "it", "de", "da", "nl", "nb",
    "ru", "sv", "pl", "cs", "ja", "th", "ro", "vi", "el", "tr", "id",
    "zh-Hans", "zh-Hant", "ko", "uk", "ku", "ms",
)
SCREEN_LOCALES = {"en": "en", "fr": "fr", "es": "es",
                  "pt-BR": "pt", "pt-PT": "pt", "it": "it", "de": "de"}
_NATIVE_NAMES = {code: name for code, name, _ in BOOK_LANGUAGES}
_NATIVE_NAMES.update({"fr-CA": "Français (Canada)", "zh-Hans": "中文（简体）",
                      "zh-Hant": "中文（繁體）", "el": "Ελληνικά"})
INTERFACE_LANGUAGES = tuple((locale, _NATIVE_NAMES[locale]) for locale in INTERFACE_LOCALES if locale != "fr-CA")
