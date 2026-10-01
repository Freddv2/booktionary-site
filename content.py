SITE = {
    "domain": "https://booktionary.io",
    "appstore_url": "https://apps.apple.com/app/id6796368335",
}

HOME_EN = {
    "lang": "en", "slug": "", "pair": "",
    "question": "Booktionary — a camera dictionary for paper books",
    "description": "Point your iPhone at a word in a paper book to see its definition. English is built in; French, Spanish, Portuguese, Italian and German packs are optional downloads. Lookups work offline.",
    "paragraphs": [
        "Booktionary is an iPhone app that turns the camera into a dictionary for paper books. You hold the phone over the page and rest a small ring on a word; a highlight sweeps across it and the definition slides up. The camera stays open, so looking up five words in a row costs no more than looking up one.",
        "English definitions are built in. Download French, Spanish, Portuguese, Italian or German definitions when you want them; translation packs are a separate choice. Once installed, definitions and translations stay on your phone and lookups work in airplane mode. Pack setup needs an internet connection, but camera images and lookup words stay on the device. There is no account, history, sync or analytics.",
        "The part that matters on real prose is that the printed word is rarely the dictionary's headword. Booktionary reduces inflected forms before it searches, so mangeaient finds manger and were finds be. Choose the book language before reading. English books can also show translations into five languages after their separate packs are installed.",
        "iPhone, iOS 17 and later. $1.99 once — no subscription and no in-app purchases.",
    ],
    "hero": ("assets/definition.jpg", "An iPhone held over an open novel; the word luminous is highlighted on the page and its dictionary definition is shown below it."),
    "siblings": ["look-up-word-paper-book", "kindle-dictionary-for-paper-books",
                 "camera-dictionary-offline"],
    "extra_html": """<h2>Tips</h2>
<ul>
  <li>Good light helps more than anything else.</li>
  <li>If nothing is recognised, move the phone nearer the page. About 15 cm works well.</li>
  <li>A slight tilt is fine. The app reads text at a natural reading angle.</li>
  <li>The ring never moves and never changes colour. It marks where the app is looking; the highlight sweeping across the word is what tells you it has been read.</li>
  <li>Tap outside the definition, swipe it away, or use the close button to return to the camera.</li>
</ul>
<h2>Support</h2>
<p>Questions, bugs, or a word it read wrong:
<a href="mailto:fredddv@hotmail.com">fredddv@hotmail.com</a></p>
""",
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
   "English definitions are built in. Download French, Spanish, Portuguese, Italian or German definitions and an English-book translation target before reading offline; installed packs stay on the device. Six book languages, $1.99 once.",
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
   "Booktionary includes the English dictionary and offers French, Spanish, Portuguese, Italian and German dictionaries as optional downloads. You can also download an English-book translation target separately. After installation, recognition and lookups run on the phone and work offline. An internet connection is needed to load the pack catalog and download selected files; lookup words and camera images are not sent.",
   "There is no account, history, sync or analytics. Optional pack requests go to booktionary.io; the hosting provider's security logging is described in the Privacy Policy.",
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
   "The other differences are practical. Lens needs a connection for most of what it does; some camera dictionaries, Booktionary among them, keep installed dictionary packs on the device and work with no signal. And a translation of a whole region will pull your eye away from the line you were reading, which is the cost the tool was supposed to remove.",
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
   "Booktionary is built around all three: English definitions are built in, French, Spanish, Portuguese, Italian and German dictionaries are optional downloads, there is no subscription or in-app purchase, and inflected forms are reduced before searching. It is a camera dictionary rather than a typing one, which suits reading and does not suit writing.",
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

HOME_FR = dict(lang="fr", slug="", pair="",
  hero=("assets/definition.jpg", "Un iPhone tenu au-dessus d'un roman ouvert ; le mot luminous est surligné sur la page et sa définition apparaît en dessous."),
  question="Booktionary — un dictionnaire par appareil photo pour les livres papier",
  description="Visez un mot d'un livre papier avec l'iPhone pour afficher sa définition. L'anglais est intégré ; les packs français, espagnols, portugais, italiens et allemands se téléchargent à la demande. Les recherches fonctionnent hors ligne.",
  paragraphs=[
   "Booktionary est une application iPhone qui transforme l'appareil photo en dictionnaire pour les livres papier. Vous tenez le téléphone au-dessus de la page et posez un petit cercle sur un mot ; un surlignage le parcourt et la définition apparaît. L'appareil photo reste ouvert : chercher cinq mots de suite ne coûte pas plus que d'en chercher un.",
   "Le dictionnaire anglais est intégré. Téléchargez les définitions françaises, espagnoles, portugaises, italiennes ou allemandes quand vous en avez besoin ; les packs de traduction sont un choix séparé. Une fois installés, dictionnaires et traductions restent sur le téléphone et les recherches fonctionnent en mode avion. La préparation des packs nécessite une connexion, mais les images de la caméra et les mots recherchés restent sur l'appareil. Il n'y a ni compte, ni historique, ni synchronisation, ni statistiques.",
   "Ce qui compte sur un vrai texte, c'est que le mot imprimé est rarement l'entrée du dictionnaire. Booktionary ramène les formes fléchies à leur lemme avant de chercher : mangeaient trouve manger, yeux trouve œil. Choisissez la langue du livre avant de lire. Les livres anglais peuvent afficher des traductions en cinq langues après téléchargement des packs séparés.",
   "iPhone, iOS 17 et versions ultérieures. 1,99 $ US une fois — sans abonnement ni achat intégré.",
  ],
  siblings=["chercher-mot-livre-papier", "dictionnaire-kindle-livre-papier", "dictionnaire-photo-hors-ligne"],
  extra_html="""<h2>Conseils</h2>
<ul>
  <li>Un bon éclairage aide plus que tout le reste.</li>
  <li>Si rien n'est reconnu, rapprochez le téléphone de la page. Une quinzaine de centimètres convient bien.</li>
  <li>Une légère inclinaison ne pose pas de problème. L'application lit le texte à l'angle de lecture naturel.</li>
  <li>Le cercle ne bouge jamais et ne change jamais de couleur. Il indique où l'application regarde ; c'est le surlignage qui parcourt le mot qui vous dit qu'il a été lu.</li>
  <li>Touchez à l'extérieur de la définition, faites-la glisser, ou utilisez le bouton de fermeture pour revenir à l'appareil photo.</li>
</ul>
<h2>Assistance</h2>
<p>Questions, problèmes, ou un mot mal lu :
<a href="mailto:fredddv@hotmail.com">fredddv@hotmail.com</a></p>
""")

QUESTIONS_FR = [
 dict(lang="fr", slug="chercher-mot-livre-papier", pair="look-up-word-paper-book",
  question="Comment chercher un mot dans un livre papier ?",
  description="Les options pour chercher un mot inconnu dans un livre imprimé, et ce que chacune coûte en confort de lecture.",
  paragraphs=[
   "Il existe quatre solutions réalistes : taper le mot dans une application de dictionnaire, viser le mot avec un appareil photo, lire le livre sur une liseuse, ou garder un dictionnaire papier à côté de soi. Le meilleur choix dépend surtout du coût de l'interruption, pas de la richesse du dictionnaire.",
   "Taper reste le plus fiable et le plus lent. Il faut poser le livre, déverrouiller le téléphone, écrire un mot dont on ignore parfois l'orthographe, puis retrouver sa ligne. Beaucoup de lecteurs finissent par renoncer et deviner d'après le contexte, ce qui se défend mais laisse le mot inappris.",
   "Un dictionnaire par appareil photo supprime la saisie. On tient le téléphone au-dessus de la page et la définition apparaît sans quitter la caméra. Booktionary fonctionne ainsi : on pose un cercle sur le mot, un surlignage le parcourt, la définition monte, et l'appareil photo reste ouvert pour le mot suivant.",
   "Une liseuse règle le problème encore mieux, avec son dictionnaire intégré — mais seulement pour les livres numériques. Sur papier, le choix se joue entre la saisie et l'appareil photo.",
  ],
  siblings=["dictionnaire-kindle-livre-papier", "pointer-appareil-photo-mot", "sans-perdre-sa-page"]),

 dict(lang="fr", slug="dictionnaire-kindle-livre-papier", pair="kindle-dictionary-for-paper-books",
  question="Existe-t-il une application qui donne le dictionnaire du Kindle sur un livre papier ?",
  description="Le dictionnaire intégré du Kindle ne fonctionne que sur les livres numériques. Les dictionnaires par appareil photo en sont l'équivalent le plus proche sur papier.",
  paragraphs=[
   "Appuyer sur un mot pour obtenir sa définition est la fonction qui manque le plus quand on revient au papier, et rien ne la reproduit exactement. Une page imprimée ne peut pas signaler quel mot on touche : le téléphone doit lire la page et déterminer de quel mot il s'agit.",
   "Les dictionnaires par appareil photo s'en approchent le plus. On tient le téléphone au-dessus de la page et on touche le mot à l'écran, ou on place un repère dessus. Booktionary utilise la seconde approche : un petit cercle reste au centre de l'image, on le pose sur le mot, et la définition apparaît environ une seconde plus tard.",
   "La différence pratique avec un Kindle est qu'on tient un téléphone au-dessus du livre plutôt que de toucher la page, et que l'éclairage compte. La ressemblance, c'est que la recherche n'interrompt plus la lecture : l'appareil photo reste ouvert, donc les recherches successives ne coûtent rien.",
   "Le dictionnaire anglais est intégré. Téléchargez les définitions françaises, espagnoles, portugaises, italiennes ou allemandes et une langue de traduction pour un livre anglais avant de lire hors ligne ; les packs installés restent sur l'appareil. Six langues de livre, 1,99 $ US une fois.",
  ],
  siblings=["chercher-mot-livre-papier", "dictionnaire-photo-hors-ligne", "pointer-appareil-photo-mot"]),

 dict(lang="fr", slug="pointer-appareil-photo-mot", pair="point-camera-at-word",
  question="Peut-on pointer l'appareil photo sur un mot pour avoir sa définition ?",
  description="Oui, c'est exactement ce que font les dictionnaires par appareil photo. Comment ils fonctionnent et ce qui distingue un bon d'un mauvais.",
  paragraphs=[
   "Oui. Plusieurs applications iPhone lisent le texte à travers l'appareil photo et renvoient la définition d'un seul mot plutôt que la traduction d'un bloc entier. La reconnaissance se fait sur l'appareil, donc la réponse arrive en une seconde environ et aucune photo n'est envoyée ailleurs.",
   "Ce qui sépare une application utilisable d'une application agaçante, c'est le traitement des formes fléchies. Le mot imprimé n'est souvent pas celui que liste le dictionnaire : pluriels, temps composés, conjugaisons. Un outil qui lit le mot et le cherche tel quel échoue sur une grande partie d'un vrai texte.",
   "Booktionary ramène le mot à sa forme de dictionnaire avant de chercher : vécut trouve vivre, mangeaient trouve manger. Il garde aussi l'appareil photo ouvert entre deux recherches, ce qui compte plus qu'il n'y paraît — rouvrir une application pour chaque mot est précisément ce qui fait renoncer.",
   "Un bon éclairage aide plus que tout le reste, et une quinzaine de centimètres au-dessus de la page est la bonne distance.",
  ],
  siblings=["chercher-mot-livre-papier", "dictionnaire-photo-vs-google-lens", "chercher-verbe-conjugue"]),

 dict(lang="fr", slug="dictionnaire-photo-hors-ligne", pair="camera-dictionary-offline",
  question="Un dictionnaire par appareil photo fonctionne-t-il sans connexion ?",
  description="Certains oui, d'autres non, et la taille du téléchargement suffit presque toujours à le deviner.",
  paragraphs=[
   "Tout dépend de l'endroit où se trouve le dictionnaire. Les applications qui envoient le mot reconnu à un serveur exigent une connexion à chaque recherche ; celles qui embarquent le dictionnaire fonctionnent partout. La taille trahit le choix : un dictionnaire complet dépasse largement la centaine de mégaoctets, donc une application de 30 Mo appelle forcément quelque chose.",
   "La reconnaissance de texte, elle, se fait généralement sur l'appareil sur les iPhone récents et n'est pas la contrainte. La contrainte, ce sont les données du dictionnaire.",
   "Booktionary intègre le dictionnaire anglais et propose les dictionnaires français, espagnol, portugais, italien et allemand en téléchargement facultatif. Les directions de traduction se téléchargent séparément. Une fois installés, reconnaissance et recherches se font sur le téléphone et fonctionnent hors ligne. Une connexion est nécessaire pour consulter le catalogue et télécharger les fichiers choisis ; les mots recherchés et les images de la caméra ne sont pas envoyés.",
   "Il n'y a ni compte, ni historique, ni synchronisation, ni statistiques. Les requêtes de téléchargement passent par booktionary.io ; la journalisation de sécurité de l'hébergeur est décrite dans la politique de confidentialité.",
  ],
  siblings=["dictionnaire-hors-ligne-iphone", "pointer-appareil-photo-mot", "dictionnaire-kindle-livre-papier"]),

 dict(lang="fr", slug="lire-roman-langue-etrangere", pair="read-novel-foreign-language",
  question="Comment lire un roman en langue étrangère sans s'arrêter à chaque mot ?",
  description="Le conseil habituel est de deviner d'après le contexte. La variable plus utile est le coût d'une seule recherche.",
  paragraphs=[
   "Le conseil classique consiste à choisir des livres légèrement au-dessus de son niveau et à déduire les mots inconnus du contexte. Cela fonctionne, mais suppose en silence que chercher un mot coûte cher. Changez cette hypothèse et le calcul change avec elle.",
   "Ce qui détermine vraiment si un livre difficile reste lisible, c'est le coût d'une recherche. À quinze secondes, on renonce au bout d'une page et on décroche ; à deux secondes, on peut chercher un quart des mots et suivre malgré tout l'histoire. Optimisez la recherche avant d'optimiser la difficulté du texte.",
   "Sur papier, cela veut dire ne pas taper. Un dictionnaire par appareil photo — Booktionary fonctionne ainsi, en tenant le téléphone au-dessus du mot — supprime le changement d'application et l'orthographe. Sur liseuse, le dictionnaire intégré s'en charge déjà.",
   "Les lectures graduées et les éditions bilingues sont l'autre voie. Elles aident beaucoup au début, et leur intérêt s'estompe généralement vers le niveau B2, quand les vrais livres deviennent accessibles.",
  ],
  siblings=["combien-de-mots-chercher", "chercher-verbe-conjugue", "chercher-mot-livre-papier"]),

 dict(lang="fr", slug="chercher-verbe-conjugue", pair="look-up-conjugated-word",
  question="Comment chercher un verbe conjugué dans un dictionnaire ?",
  description="Les dictionnaires listent des infinitifs et les livres donnent des formes conjuguées. Ce décalage fait échouer la plupart des outils de recherche.",
  paragraphs=[
   "Un dictionnaire s'organise par entrée : l'infinitif d'un verbe, le singulier d'un nom. Un texte, non. On lit vécut, mangeaient, yeux ou eut, et aucune de ces formes n'est l'entrée cherchée. Retrouver la forme de base est une étape supplémentaire, et dans une langue qu'on apprend encore, c'est l'étape difficile.",
   "Certains dictionnaires gèrent cela, beaucoup non. Le Wiktionnaire reconnaît généralement les formes fléchies ; de nombreuses applications ne renvoient tout simplement rien. Si vous choisissez un outil pour lire plutôt que pour écrire, c'est la première capacité à tester.",
   "Booktionary effectue cette réduction avant de chercher : vécut donne vivre, mangeaient donne manger, yeux donne œil. C'est la raison pour laquelle il fonctionne sur des romans et pas seulement sur des menus et des panneaux.",
   "En français, le passé simple est la forme qui piège le plus les apprenants, parce qu'il est partout en littérature et quasiment absent à l'oral.",
  ],
  siblings=["lire-roman-langue-etrangere", "pointer-appareil-photo-mot", "chercher-mot-livre-papier"]),

 dict(lang="fr", slug="sans-perdre-sa-page", pair="without-losing-your-place",
  question="Comment chercher un mot sans perdre sa page ?",
  description="Perdre sa ligne coûte souvent plus cher que la recherche elle-même. Quelques manières de l'éviter.",
  paragraphs=[
   "La plupart des lecteurs décrivent le même échec : on pose le livre, on déverrouille un téléphone, on tape, on se laisse distraire, puis on passe plusieurs secondes à retrouver la phrase. La définition a pris deux secondes et l'interruption trente.",
   "Une réponse traditionnelle consiste à différer : souligner le mot ou le noter en marge, et tout chercher plus tard. Cela préserve la lecture, mais dans les faits la liste différée est rarement relue.",
   "L'autre solution est de raccourcir l'interruption au point qu'elle cesse de compter. Un dictionnaire par appareil photo y parvient en supprimant la saisie et en gardant les yeux sur la page : avec Booktionary, on tient le téléphone au-dessus du mot et la définition apparaît juste au-dessus, donc on ne perd pas sa place puisqu'on n'a jamais quitté le livre des yeux.",
   "Garder un doigt sur la ligne pendant la recherche est la version sans technologie de la même idée, et elle fonctionne.",
  ],
  siblings=["chercher-mot-livre-papier", "dictionnaire-kindle-livre-papier", "combien-de-mots-chercher"]),

 dict(lang="fr", slug="dictionnaire-photo-vs-google-lens", pair="camera-dictionary-vs-google-lens",
  question="Quelle est la différence entre un dictionnaire photo et Google Lens ?",
  description="Lens traduit des zones de texte. Un dictionnaire photo définit un mot. Ce ne sont pas les mêmes outils.",
  paragraphs=[
   "Google Lens est un outil visuel généraliste. Pointé sur une page, il reconnaît et traduit un bloc de texte, ce qui est parfait pour un menu, un panneau ou un paragraphe totalement incompréhensible. Il donne la traduction d'un passage, pas la définition d'un mot.",
   "Un dictionnaire photo est volontairement plus étroit. Il identifie un seul mot et renvoie son entrée de dictionnaire — sens, nature, parfois étymologie — dans la même langue ou dans la vôtre. Si vous lisez déjà la phrase et butez sur un mot, c'est ce qu'il vous faut.",
   "Les autres différences sont pratiques. Lens exige une connexion pour l'essentiel de ses fonctions ; certains dictionnaires photo, dont Booktionary, gardent les packs installés sur l'appareil et fonctionnent sans réseau. Et traduire une zone entière détourne le regard de la ligne en cours, c'est-à-dire exactement le coût que l'outil devait supprimer.",
   "Aucun ne remplace l'autre. Pour lire un roman dans une langue qu'on maîtrise en partie, l'outil étroit gagne.",
  ],
  siblings=["pointer-appareil-photo-mot", "dictionnaire-photo-hors-ligne", "chercher-mot-livre-papier"]),

 dict(lang="fr", slug="dictionnaire-hors-ligne-iphone", pair="offline-dictionary-app-iphone",
  question="Quel dictionnaire hors ligne choisir sur iPhone ?",
  description="Ce qu'il faut regarder dans un dictionnaire hors ligne, et comment vérifier depuis la fiche App Store qu'il l'est vraiment.",
  paragraphs=[
   "La première chose à regarder est la taille du téléchargement. Un dictionnaire hors ligne est volumineux — un dictionnaire sérieux dépasse largement la centaine de mégaoctets — donc une application qui promet une couverture complète en vingt ou trente mégaoctets télécharge des données plus tard ou interroge un serveur.",
   "La deuxième est de savoir si le mode hors ligne fait partie de l'application ou constitue une option payante. Plusieurs applications sont gratuites à l'installation et réservent l'usage hors ligne, ou les langues supplémentaires, à un abonnement. Le modèle se défend, mais mieux vaut le savoir avant de compter dessus en avion.",
   "La troisième est le traitement des formes fléchies, si vous l'utilisez en lisant. Un dictionnaire incapable de passer de vécut à vivre vous décevra dès la première page d'un roman.",
   "Booktionary répond à ces trois critères : le dictionnaire anglais est intégré, les dictionnaires français, espagnol, portugais, italien et allemand se téléchargent à la demande, sans abonnement ni achat intégré, pour 1,99 $ US une fois ; les formes fléchies sont ramenées à leur lemme avant la recherche. Les packs installés fonctionnent hors ligne.",
  ],
  siblings=["dictionnaire-photo-hors-ligne", "chercher-verbe-conjugue", "dictionnaire-kindle-livre-papier"]),

 dict(lang="fr", slug="combien-de-mots-chercher", pair="how-many-words-to-look-up",
  question="Combien de mots faut-il chercher quand on lit dans une langue étrangère ?",
  description="Il n'y a pas de bon pourcentage. La vraie question est le coût d'une recherche, car il décide du nombre qu'on peut se permettre.",
  paragraphs=[
   "Le conseil arrive d'ordinaire sous forme de pourcentage : connaître 95 % ou 98 % des mots et lire au fil du texte. C'est une règle raisonnable qui masque la vraie variable — non pas combien de mots vous ignorez, mais combien coûte chaque recherche.",
   "Si une recherche prend quinze secondes, même 5 % de mots inconnus devient insupportable et vous finirez par les sauter. Si elle prend deux secondes, un quart de la page reste praticable et vous apprendrez les mots au lieu de les deviner. Les lecteurs qui racontent avoir lu très au-dessus de leur niveau mentionnent presque toujours une recherche rapide quelque part.",
   "L'ordre pratique est donc : rendre les recherches peu coûteuses, puis choisir le livre le plus difficile qui vous plaise. Sur papier, cela veut dire ne pas taper — Booktionary est fait pour cela, en tenant le téléphone au-dessus du mot. Sur liseuse, le dictionnaire intégré suffit.",
   "Le seul cas où chercher moins vaut mieux est la lecture de plaisir, quand l'intrigue compte plus que le vocabulaire. Devinez alors librement et continuez.",
  ],
  siblings=["lire-roman-langue-etrangere", "sans-perdre-sa-page", "chercher-verbe-conjugue"]),
]

PAGES = [HOME_EN] + QUESTIONS_EN + [HOME_FR] + QUESTIONS_FR
