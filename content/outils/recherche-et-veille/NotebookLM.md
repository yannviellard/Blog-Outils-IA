---
title: "NotebookLM (Gemini Notebook)"
type: outil
description: "Lecture et synthèse ancrées dans un corpus choisi, avec citations et formats pédagogiques."
format: application
tags:
  - metier/direction
  - metier/support-client
  - metier/operations
  - theme/recherche
  - theme/voix
  - theme/video
editeur: "Google"
logo: "[[notebooklm.svg]]"
site: "https://notebooklm.google.com/"
licence: "Propriétaire"
statut: disponible
derniere_maj: 2026-09-23
note_documentation: 3
note_precision: 3
note_maturite: 4
avis_maj: 2026-09-24
modified: 2026-11-19
---

# NotebookLM (Gemini Notebook)

> Assistant de recherche et de réflexion de Google, récemment renommé **Gemini Notebook**, qui ancre systématiquement ses réponses dans les sources fournies par l'utilisateur (documents, PDF, sites web, vidéos YouTube, audio) plutôt que dans ses connaissances générales, et peut transformer ces sources en résumés audio façon podcast, résumés vidéo, rapports, cartes mentales ou fiches de révision.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves.

## Résumé

NotebookLM — rebaptisé Gemini Notebook sur son site officiel — est un outil de Google qui inverse le fonctionnement habituel d'un chatbot IA : au lieu de puiser dans des connaissances générales, il construit ses réponses exclusivement à partir des sources que l'utilisateur importe dans un « notebook » (documents Google Docs/Slides, PDF, pages web, vidéos YouTube, fichiers audio, texte collé). Cet ancrage systématique aux sources (grounding) vise à réduire le risque d'hallucination et à fournir des réponses citées, traçables jusqu'au passage exact du document d'origine.

Au-delà du question/réponse classique, l'outil se distingue par sa capacité à transformer un corpus de sources en formats variés : résumés audio interactifs façon podcast (Audio Overviews), résumés vidéo, rapports écrits adaptés à un besoin précis (stratégie de vente, analyse littéraire…), cartes mentales, guides d'étude, questionnaires et flashcards de révision. Il s'appuie sur les derniers modèles Gemini de Google et propose plusieurs paliers d'accès (Gemini Notebook standard, puis intégration dans les offres Google AI Plus, Pro et Ultra) qui augmentent les quotas de génération, le nombre de sources par notebook (50 en standard, jusqu'à 600 en Ultra) et le niveau d'accès aux modèles.

NotebookLM cible aussi bien les particuliers (révision, recherche personnelle, projets créatifs) que les organisations (Business via Google Workspace, Education via Google Workspace for Education, Enterprise via Google Cloud), avec des cas d'usage documentés en apprentissage, recherche, service client (notebooks publics partageables), ventes, formation/onboarding et marketing.

## Fonctionnalités

- **Réponses ancrées aux sources** : chaque réponse est basée sur les documents importés par l'utilisateur, avec citations renvoyant au passage source, plutôt que sur les connaissances générales du modèle.

- **Sources multi-formats** : Google Docs, Google Slides, PDF, pages web, vidéos YouTube, fichiers audio, texte collé directement.

- **Résumés audio interactifs (Audio Overviews)** : génération d'un résumé des sources sous forme de conversation audio façon podcast, lisible/écoutable directement.

- **Résumés vidéo** : transformation du contenu en résumés vidéo, utile notamment pour la formation et l'intégration de nouveaux employés.

- **Rapports sur mesure** : génération de rapports écrits adaptés à un besoin précis (stratégie de vente, analyse artistique, revue de littérature…) en un clic à partir de centaines de sources.

- **Cartes mentales, guides d'étude et flashcards** : outils orientés apprentissage pour réviser un cours ou explorer visuellement un corpus de documents.

- **Découverte de sources et Deep Research** : recherche et ajout de nouvelles sources pertinentes directement depuis l'interface, pour accélérer une revue de littérature.

- **Notebooks publics partageables** : possibilité de publier un notebook (comptes personnels uniquement) pour que d'autres personnes interrogent directement les sources — cas d'usage type : documentation produit ou centre d'aide en libre-service.

- **Paliers d'usage progressifs** : Gemini Notebook standard (jusqu'à 50 sources par notebook), puis intégration dans Google AI Plus (100 sources, 2x les générations), Pro (300 sources, 5x) et Ultra (600 sources, jusqu'à 50x), avec accès à des modèles Gemini plus performants selon le palier.

- **Déploiement organisationnel** : offres Business (Google Workspace), Education (Google Workspace for Education) et Enterprise (Google Cloud), avec garantie que les données de l'organisation ne servent pas à l'entraînement des modèles.

## Analyse
|Critère|Note|
|---|--:|
|Documentation|★★★☆☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★★☆|
|Popularité|—|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité non notée : pas de dépôt public._

### Points forts

- **Ancrage aux sources** : la citation des passages sources limite les digressions par rapport à un chatbot généraliste et permet de vérifier une réponse, un atout pour la recherche et l'étude. L'ancrage ne garantit pas la vérité : une source erronée reste une source erronée, et la qualité des citations dépend du corpus fourni.

- **Formats de restitution très variés et différenciants** : les résumés audio façon podcast en particulier ont largement contribué à la notoriété de l'outil, que le site officiel appuie par des citations de presse.

- **Large éventail de sources acceptées** (documents, PDF, web, YouTube, audio), pratique pour agréger un corpus hétérogène dans un seul espace de travail.

- **Offre organisationnelle claire** avec garanties de confidentialité explicites (données non utilisées pour l'entraînement), facilitant l'adoption en contexte professionnel ou scolaire.

### Limites

- **Formats parfois plus engageants que concis** : certains formats générés (audio, vidéo) privilégient l'engagement plutôt que la densité d'information ; ils ne remplacent pas la lecture des passages sources importants.

- **Fonctions de rédaction, d'annotation et de gestion bibliographique moins complètes** que dans des outils spécialisés ; NotebookLM est un assistant de lecture et d'étude, pas un environnement d'écriture.

- **Quotas et paliers payants** : le nombre de sources et de générations dépend du forfait Google AI choisi.


- **Outil propriétaire et fermé** : aucune transparence sur le code, l'architecture technique ou les mécanismes exacts de citation/grounding au-delà de la communication marketing.

- **Dépendance à l'écosystème Google** : nécessite un compte Google, et la montée en gamme est liée aux offres Google AI (Plus/Pro/Ultra), disponibles seulement dans certaines régions selon le site officiel.

- **Limites de sources par notebook** même dans les paliers supérieurs (600 maximum en Ultra), qui peuvent contraindre des corpus de recherche très volumineux.

- **Repositionnement de marque récent** (« Gemini Notebook ») qui peut créer une confusion avec le nom historique NotebookLM, encore largement utilisé dans la presse et par les utilisateurs.

### Qualité

**Commentaire :** produit abouti et largement adopté, avec un positionnement clair (recherche ancrée aux sources) et des fonctionnalités de restitution différenciantes. La fiche s'appuie principalement sur la communication du site officiel, faute de documentation technique publique ou de code source consultable ; les tests indépendants (voir [[#Avis indépendants|les avis indépendants]]) confirment l'intérêt pour étudier son propre corpus, avec les réserves ci-dessus.

## Relations

- **Alternative à :** ChatGPT Projects (conversation, fichiers et mémoire de projet), Claude (synthèse et rédaction à partir de documents), Perplexity (exploration du web plutôt que d'un corpus propre)

- **Complémentaire de :** [[Gemini Deep Research]] pour l'exploration du web avant d'ancrer un corpus choisi

- **Complémentaire de :** [[Unlimited-OCR]] pour extraire et structurer des documents numérisés avant leur import dans un corpus.

- **S'intègre avec :** Google Docs, Google Slides, Google Drive, YouTube, Google Workspace, Google Workspace for Education, Google Cloud

- **Utilise :** modèles Gemini de Google

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

NotebookLM est largement apprécié pour ses réponses ancrées dans un corpus choisi, ses citations qui ramènent au passage source et ses formats pédagogiques — audio, vidéo, cartes et guides. Il réduit le risque de digression par rapport à un chatbot généraliste et excelle pour étudier un ensemble de documents.

Les limites remontées sont la dépendance à Google, les quotas et la tendance de certains formats à privilégier l’engagement plutôt que la concision. Une source erronée reste une source erronée : l’ancrage n’équivaut pas à la vérité. Les fonctions de rédaction, d’annotation et de gestion bibliographique restent moins complètes que dans des outils spécialisés.

### Comparaison

Perplexity est meilleur pour explorer rapidement le web ; ChatGPT Projects offre une conversation, des fichiers et une mémoire de projet plus généralistes ; Claude excelle sur la synthèse et la rédaction. NotebookLM gagne lorsqu’on veut interroger, apprendre et retracer précisément **son propre corpus**.

### Verdict

Un des meilleurs assistants de lecture et de recherche documentaire disponibles ; moins adapté comme environnement d’écriture complet ou moteur de recherche ouvert unique.

## Sources

- [Gemini Notebook / NotebookLM](https://notebooklm.google.com/)

- [Site marketing](https://notebooklm.google/)

- [Forfaits](https://notebooklm.google/plans)

### Sources des avis

- [Test TechRadar](https://www.techradar.com/pro/notebooklm-review)
- [NotebookLM vs ChatGPT Projects](https://officialairanking.com/comparisons/2026-06-20-notebooklm-vs-chatgpt-projects-our-verdict/)
- [Test NotebookLM vs Perplexity](https://www.tomsguide.com/ai/i-tested-notebooklm-vs-perplexity-for-deep-research-with-5-difficult-prompts-heres-the-clear-winner)

_Dernière analyse : 12 novembre 2026_
