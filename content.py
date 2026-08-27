SITE = {
    "domain": "https://booktionary.io",
    "appstore_url": "https://apps.apple.com/app/id6796368335",
}

HOME_EN = {
    "lang": "en", "slug": "", "pair": "",
    "question": "Booktionary — a camera dictionary for paper books",
    "description": "Hold your phone over a word in a paper book and its definition appears. English and French, entirely offline, nothing collected.",
    "paragraphs": [
        "Booktionary is an iPhone app that turns the camera into a dictionary for paper books. You hold the phone over the page and rest a small ring on a word; a highlight sweeps across it and the definition slides up. The camera stays open, so looking up five words in a row costs no more than looking up one.",
        "Both dictionaries live on the device — 156 MB of English and 189 MB of French, together 94% of the download. It works in airplane mode, underground, and anywhere with no signal. There is no account, no history, no sync and no analytics; the App Store privacy label reads Data Not Collected.",
        "The part that matters on real prose is that the printed word is rarely the dictionary's headword. Booktionary reduces inflected forms before it searches, so mangeaient finds manger and were finds be. Language is detected automatically and English and French work in the same session.",
        "iPhone, iOS 17 and later. $1.99 once — no subscription and no in-app purchases.",
    ],
    "siblings": ["look-up-word-paper-book", "kindle-dictionary-for-paper-books",
                 "camera-dictionary-offline"],
}

QUESTIONS_EN = [
 dict(lang="en", slug="look-up-word-paper-book", pair="chercher-mot-livre-papier",
  question="How do you look up a word while reading a paper book?",
  description="The practical options for looking up an unfamiliar word in a printed book, and what each one costs you in reading flow.",
  paragraphs=[
   "There are four realistic options. Type the word into a dictionary app, point a camera app at it, read the book on an e-reader instead, or keep a paper dictionary beside you. Which is best depends almost entirely on how much each interruption costs you, not on which dictionary is most thorough.",
   "Typing is the most reliable and the slowest. You put the book down, unlock the phone, type a word you may not be able to spell, and then find your line again. Readers often stop bothering and guess from context instead, which is a reasonable trade but means the word is never learned.",
   "A camera dictionary removes the typing. You hold the phone over the page and the definition appears without you leaving the camera. Booktionary works this way: rest a ring on the word, a highlight sweeps across it, the definition slides up, and the camera stays open so the next word costs nothing.",
   "An e-reader solves this best of all, with tap-to-define built in — but only for ebooks. For a printed book the choice is between typing and a camera.",
  ],
  siblings=["kindle-dictionary-for-paper-books", "point-camera-at-word", "without-losing-your-place"]),

 dict(lang="en", slug="kindle-dictionary-for-paper-books", pair="dictionnaire-kindle-livre-papier",
  question="Is there an app that gives you Kindle's tap-to-define on paper books?",
  description="Kindle's tap-to-define only works on ebooks. Camera dictionaries are the nearest equivalent for printed books, and here is how close they get.",
  paragraphs=[
   "Tap-to-define is the feature people miss most when they go back to paper, and nothing reproduces it exactly. A printed page cannot report which word you touched, so the phone has to read the page and work out which word you mean.",
   "Camera dictionaries are the closest equivalent. You hold the phone over the page and either tap the word on screen or hold a marker over it. Booktionary uses the second approach: a small ring stays in the centre of the frame, you put it on the word, and about a second later the definition appears.",
   "The practical difference from a Kindle is that you hold a phone above the book rather than touching the page, and that lighting matters. The practical similarity is that the lookup no longer interrupts you — the camera stays open, so consecutive lookups cost nothing.",
   "Booktionary keeps both dictionaries on the device, so unlike a Kindle it needs no connection at all. English and French, $1.99 once.",
  ],
  siblings=["look-up-word-paper-book", "camera-dictionary-offline", "point-camera-at-word"]),

 dict(lang="en", slug="point-camera-at-word", pair="pointer-appareil-photo-mot",
  question="Can you point your phone camera at a word to get its definition?",
  description="Yes — camera dictionaries do exactly this. How they work, where they fail, and what separates a usable one from a frustrating one.",
  paragraphs=[
   "Yes. Several iPhone apps read text through the camera and return a definition for a single word rather than translating a whole block. They rely on on-device text recognition, so they respond in about a second and do not need to send a photo anywhere.",
   "The thing that separates a usable one from a frustrating one is what happens to inflected words. The word printed on the page is often not the form the dictionary lists — plurals, past tenses, conjugations. A tool that reads the word and searches for it verbatim will simply fail on much of real prose.",
   "Booktionary reduces the word to its dictionary form before searching, so wended finds wend and mangeaient finds manger. It also keeps the camera open between lookups, which matters more than it sounds: reopening an app for every word is what makes people stop looking words up at all.",
   "Good light helps more than anything else, and holding the phone roughly 15 cm above the page is the sweet spot.",
  ],
  siblings=["look-up-word-paper-book", "camera-dictionary-vs-google-lens", "look-up-conjugated-word"]),

 dict(lang="en", slug="camera-dictionary-offline", pair="dictionnaire-photo-hors-ligne",
  question="Does a camera dictionary work without an internet connection?",
  description="Some do and some do not, and the difference is usually visible in the app's download size.",
  paragraphs=[
   "It depends entirely on where the dictionary lives. Apps that send the recognised word to a server need a connection for every lookup; apps that bundle the dictionary work anywhere. The download size gives it away — a full English dictionary is well over a hundred megabytes, so a 30 MB app is almost certainly calling out to something.",
   "Text recognition itself is usually on-device on modern iPhones and is not the constraint. The constraint is the dictionary data.",
   "Booktionary bundles both: 156 MB of English and 189 MB of French, which is 94% of its download size. That makes it a large app, deliberately, in exchange for working in airplane mode, on the underground, on a plane and in places with no signal. Nothing is sent anywhere, because there is nowhere to send it.",
   "The side effect is privacy: with no network calls there is no account, no history and no analytics. The App Store privacy label reads Data Not Collected.",
  ],
  siblings=["offline-dictionary-app-iphone", "point-camera-at-word", "kindle-dictionary-for-paper-books"]),

 dict(lang="en", slug="read-novel-foreign-language", pair="lire-roman-langue-etrangere",
  question="How do you read a novel in a foreign language without stopping at every word?",
  description="The usual advice is to read above your level and guess from context. The more useful variable is what a single lookup costs you.",
  paragraphs=[
   "The standard advice is to pick books slightly above your level and infer unknown words from context. That works, but it quietly assumes looking a word up is expensive. Change that assumption and the calculation changes with it.",
   "What actually determines whether you can read a harder book is the cost of one lookup. At fifteen seconds you will stop bothering after a page and drift; at two seconds you can afford to look up a quarter of the words and still follow the story. Optimise the lookup before you optimise the difficulty of the text.",
   "For paper, that means not typing. A camera dictionary — Booktionary works this way, holding the phone over the word — removes the switching and the spelling. For ebooks, an e-reader's built-in dictionary already does it.",
   "Graded readers and bilingual editions are the other route. They work well early on, and most learners find the benefit tails off around B2, when real books become reachable.",
  ],
  siblings=["how-many-words-to-look-up", "look-up-conjugated-word", "look-up-word-paper-book"]),

 dict(lang="en", slug="look-up-conjugated-word", pair="chercher-verbe-conjugue",
  question="How do you look up a conjugated word in a dictionary?",
  description="Dictionaries list root forms, and the page gives you inflected ones. This mismatch is the main reason lookup tools fail on real prose.",
  paragraphs=[
   "Dictionaries are organised by headword — the infinitive of a verb, the singular of a noun. Text is not. You read vécut, mangeaient, wended or oxen, and none of those is the entry you need. Working out the root before you can search is an extra step, and in a language you are still learning it is the hard step.",
   "Some dictionaries handle this and many do not. Wiktionary generally recognises inflected forms; plenty of dictionary apps do not, and simply return nothing. If you are choosing a tool for reading rather than for writing, this is the single capability worth testing first.",
   "Booktionary performs this reduction before it searches, so vécut resolves to vivre, mangeaient to manger, were to be and mice to mouse. It is the reason it works on novels rather than only on menus and signs.",
   "For French specifically, the passé simple is the form that catches most learners out, because it appears constantly in literature and almost never in speech.",
  ],
  siblings=["read-novel-foreign-language", "point-camera-at-word", "look-up-word-paper-book"]),

 dict(lang="en", slug="without-losing-your-place", pair="sans-perdre-sa-page",
  question="How do you look up words in a book without losing your place?",
  description="Losing the line is usually a bigger cost than the lookup itself. A few approaches that avoid it.",
  paragraphs=[
   "Most people describe the same failure: they put the book down, unlock a phone, type, get distracted, and then spend several seconds finding the sentence again. The definition took two seconds and the interruption took thirty.",
   "One traditional answer is to defer — underline the word or note it in the margin, and look everything up later. It preserves the reading, but in practice the deferred list rarely gets read.",
   "The alternative is to shorten the interruption enough that it stops mattering. A camera dictionary does this by removing the typing and keeping your eyes on the page: with Booktionary you hold the phone over the word and the definition appears above it, so your place is never lost because you never looked away from the book.",
   "Keeping a finger on the line while you look up is a low-technology version of the same idea, and it works.",
  ],
  siblings=["look-up-word-paper-book", "kindle-dictionary-for-paper-books", "how-many-words-to-look-up"]),

 dict(lang="en", slug="camera-dictionary-vs-google-lens", pair="dictionnaire-photo-vs-google-lens",
  question="What is the difference between a camera dictionary and Google Lens?",
  description="Lens translates regions of text. A camera dictionary defines one word. They are built for different jobs.",
  paragraphs=[
   "Google Lens is a general visual tool. Pointed at a page it will recognise and translate a block of text, which is excellent for a menu, a sign or a paragraph you cannot read at all. It gives you a translation of the passage rather than a definition of a word.",
   "A camera dictionary is narrower on purpose. It identifies a single word and returns its dictionary entry — sense, part of speech, sometimes etymology — in the same language or in yours. If you can already read the sentence and are stuck on one word, that is what you want.",
   "The other differences are practical. Lens needs a connection for most of what it does; some camera dictionaries, Booktionary among them, keep the dictionary on the device and work with no signal. And a translation of a whole region will pull your eye away from the line you were reading, which is the cost the tool was supposed to remove.",
   "Neither replaces the other. For reading a novel in a language you mostly know, the narrow tool wins.",
  ],
  siblings=["point-camera-at-word", "camera-dictionary-offline", "look-up-word-paper-book"]),

 dict(lang="en", slug="offline-dictionary-app-iphone", pair="dictionnaire-hors-ligne-iphone",
  question="What is the best offline dictionary app for iPhone?",
  description="What to look for in an offline dictionary, and how to tell from the App Store listing whether an app is genuinely offline.",
  paragraphs=[
   "The first thing to check is the download size. Offline dictionaries are large — a serious English dictionary runs to well over a hundred megabytes — so any app claiming full offline coverage in twenty or thirty megabytes is downloading data later or calling a server.",
   "The second is whether the offline dictionary is the whole app or a paid extra. Several apps are free to install and gate offline use, or additional languages, behind a subscription. That is a reasonable model, but it is worth knowing before you rely on it on a plane.",
   "The third is inflection handling, if you are using it while reading. A dictionary that cannot get from wended to wend will disappoint you on the first page of a novel.",
   "Booktionary is built around all three: 345 MB of English and French dictionaries on the device, no subscription and no in-app purchases, $1.99 once, and inflected forms reduced before searching. It is a camera dictionary rather than a typing one, which suits reading and does not suit writing.",
  ],
  siblings=["camera-dictionary-offline", "look-up-conjugated-word", "kindle-dictionary-for-paper-books"]),

 dict(lang="en", slug="how-many-words-to-look-up", pair="combien-de-mots-chercher",
  question="How many words should you look up when reading in a second language?",
  description="There is no correct percentage. The useful question is what one lookup costs you, because that decides how many you can afford.",
  paragraphs=[
   "Advice usually arrives as a percentage: know 95% or 98% of the words and read for flow. It is a reasonable heuristic and it hides the real variable, which is not how many words you do not know but how much each lookup costs.",
   "If a lookup takes fifteen seconds, even 5% unknown words is unbearable and you will start skipping them. If it takes two seconds, a quarter of the page is workable and you will actually learn the words rather than guessing past them. Readers who describe successfully reading well above their level almost always mention a fast lookup somewhere in the story.",
   "So the practical order is: make lookups cheap, then choose the hardest book you enjoy. On paper that means not typing — Booktionary is built for this, holding the phone over the word rather than switching apps. On an e-reader the built-in dictionary already does it.",
   "The one case for looking up less is when you are reading for pleasure and the plot matters more than the vocabulary. Then guess freely and go on.",
  ],
  siblings=["read-novel-foreign-language", "without-losing-your-place", "look-up-conjugated-word"]),
]

PAGES = [HOME_EN] + QUESTIONS_EN
