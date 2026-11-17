---
title: "OpenCLI"
type: outil
description: "Transformation de sites et applications déjà connectés en commandes déterministes."
format: cli
tags:
  - metier/ingenierie
  - metier/operations
  - theme/navigateur
  - theme/automatisation
editeur: "jackwener"
logo: "[[opencli.svg]]"
site: "https://opencli.info/"
depot: "https://github.com/jackwener/opencli"
licence: "Apache-2.0"
statut: disponible
derniere_maj: 2026-11-07
etoiles: 31110
forks: 3044
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 3
note_maturite: 2
note_popularite: 4
memo: "[[OpenCLI mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# OpenCLI

> CLI open source qui transforme des sites web, des applications Electron et des outils locaux en commandes déterministes, en réutilisant la session Chrome déjà connectée de l'utilisateur. Il fournit plus de 100 adaptateurs prêts à l'emploi et des skills pour qu'un agent IA (Claude Code, Cursor…) pilote n'importe quelle page via le navigateur de l'utilisateur.

**Composition** : 6 skills.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours de la communauté, et [[OpenCLI mémo]] pour le mémo pratique.

## Résumé

OpenCLI part d'une idée simple : plutôt que de passer par une API officielle (souvent absente, limitée ou payante) ou par un scraper classique (bloqué par les protections anti-bot), il s'appuie sur le navigateur où l'utilisateur est déjà connecté. Une extension Chrome, la « Browser Bridge », et un petit daemon local servent de pont entre la ligne de commande et les onglets Chrome. Une commande comme `opencli twitter trending` ou `opencli bilibili hot` s'exécute alors avec la session réelle de l'utilisateur, et renvoie un résultat structuré (tableau, JSON, YAML, Markdown ou CSV).

Le projet, créé en mars 2026 par jackwener, a changé d'architecture avec la version 1.0 : Playwright a été abandonné au profit du couple daemon + extension Chrome, plus léger. Il couvre trois usages :

1. **Des adaptateurs intégrés** pour plus de 100 sites : beaucoup de plateformes chinoises (Bilibili, Zhihu, Xiaohongshu, Douyin, Weibo…) mais aussi Reddit, Hacker News, Twitter/X, LinkedIn, Amazon, Claude, Gemini ou NotebookLM.
2. **Le pilotage libre d'un navigateur par un agent IA** : avec la skill `opencli-browser`, l'agent navigue, clique, remplit des formulaires et extrait des données à partir de snapshots DOM structurés plutôt que de captures d'écran.
3. **La création de nouveaux adaptateurs** : la skill `opencli-adapter-author` guide l'agent de l'exploration du site jusqu'à la vérification de la commande générée.

L'argument central est le coût : une fois un adaptateur écrit, son exécution ne consomme aucun token de LLM. L'IA sert à écrire l'adaptateur une fois ; ensuite, la commande tourne de façon déterministe autant de fois que nécessaire.

## Fonctionnalités

- **Plus de 100 adaptateurs de sites** : lecture (tendances, recherche, profils, commentaires, notifications) et, pour certains, écriture (publier, liker, suivre, répondre, envoyer des messages).

- **Réutilisation de la session Chrome** : pas de clé API ni d'identifiants à fournir ; les cookies restent dans le navigateur. Gestion de plusieurs profils Chrome avec alias (`opencli profile use work`).

- **Six skills pour agents IA** (installables avec `npx skills add jackwener/opencli`) : `opencli-browser` (pilotage libre), `opencli-adapter-author` (écriture d'adaptateurs), `opencli-autofix` (réparation d'un adaptateur cassé), `opencli-browser-sitemap` et `opencli-sitemap-author` (mémoire des parcours d'un site), `opencli-usage` (référence des commandes).

- **Primitives de navigation** : `open`, `click`, `type`, `fill`, `select`, `wait`, `extract`, `network`, `eval`, gestion des onglets, avec des sessions nommées et des identifiants d'onglet.

- **Hub CLI** : une interface unique pour des outils locaux existants (`gh`, `docker`, `vercel`, `wrangler`, `obsidian`, Notion, Discord, Telegram…) et enregistrement de ses propres binaires avec `opencli external register`.

- **Adaptateurs d'applications de bureau** via le Chrome DevTools Protocol : Cursor, Codex, ChatGPT, Antigravity, Trae, Discord, Doubao…

- **Téléchargement de médias** : images, vidéos et articles depuis Xiaohongshu, Bilibili (avec yt-dlp), Twitter, Pixiv, Zhihu, WeChat…

- **Pensé pour les scripts** : formats de sortie multiples et codes de sortie Unix normalisés (66 résultat vide, 69 extension déconnectée, 77 authentification requise…).

- **Système de plugins** : adaptateurs communautaires installables depuis GitHub (`opencli plugin install github:user/repo`).

- **Installation** : application de bureau OpenCLIApp (macOS/Windows) ou `npm install -g @jackwener/opencli` (Node.js ≥ 20.18.1), plus l'extension depuis le Chrome Web Store ; diagnostic avec `opencli doctor`.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 31 110 au 16 novembre 2026._

### Points forts

- **Aucun coût LLM à l'exécution** : la logique est figée dans l'adaptateur, ce qui rend les tâches répétitives rapides, reproductibles et gratuites en tokens, contrairement à un agent qui explore la page à chaque fois.

- **Accès aux sites sans API** : la réutilisation de la session connectée donne accès à des données que ni une API officielle ni un scraper anonyme n'atteignent facilement.

- **Conçu pour les agents** : les skills couvrent tout le cycle, de l'usage au pilotage libre, à l'écriture et à la réparation d'adaptateurs.

- **Couverture unique des plateformes chinoises** (Xiaohongshu, Bilibili, Zhihu, Douyin, WeChat…), rarement prises en charge par les outils occidentaux.

- **Rythme de développement soutenu** : releases hebdomadaires et environ 248 contributeurs (sa popularité, acquise en six mois, mesure l'attention, pas la qualité ; les articles de présentation sont souvent promotionnels et l'essai critique le plus fiable reste la lecture des issues GitHub).

### Limites

- **Risque de bannissement de compte** : les actions passent par le vrai compte de l'utilisateur. Sur Xiaohongshu, des comptes ont été bloqués ; le mainteneur recommande de s'en tenir à la lecture et d'éviter l'écriture sur cette plateforme.

- **Surface de sécurité importante** : l'extension peut exécuter du JavaScript arbitraire dans les pages et accéder aux cookies de toutes les sessions ouvertes. Un durcissement a été fait (authentification du daemon, isolation des onglets), mais la politique de sécurité complète — liste de sites autorisés, confirmation avant toute action d'écriture — est encore en discussion (issue #1595, ouverte depuis mai 2026).

- **Fragilité des adaptateurs** : ils dépendent de la structure des sites ; un changement d'interface ou un contrôle anti-automatisation peut les casser ou renvoyer silencieusement un résultat vide. La skill `opencli-autofix` existe pour cette raison.

- **Dépendance à Chrome/Chromium** et à une extension installée ; l'usage sur un serveur sans interface graphique est plus complexe.

- **Conditions d'utilisation des sites** : automatiser un compte personnel peut enfreindre les CGU de certaines plateformes ; la responsabilité reste celle de l'utilisateur.

### Qualité

**Commentaire :** documentation riche et projet extrêmement actif, avec une vraie réflexion sur l'usage par des agents (skills, codes de sortie, formats structurés). La maturité reste moyenne : le projet a six mois, les adaptateurs cassent au gré des changements des sites, et le modèle de sécurité — un agent qui agit avec toutes les sessions connectées de l'utilisateur — n'a pas encore de garde-fous complets.

## Relations

- **Alternative à :** [[Agent Browser]], [[Playwright]], [[Chrome DevTools MCP]], AutoCLI (réécriture en Rust d'une approche similaire). Différence de modèle de sécurité : ces outils pilotent un navigateur neuf ou isolé (plus sûr, mais sans les sessions déjà connectées), alors qu'OpenCLI agit avec les sessions réelles de l'utilisateur.

- **S'intègre avec :** [[Claude Code]], Cursor, Codex, [[NotebookLM]] et Gemini (adaptateurs dédiés)

- **Utilise :** Chrome/Chromium, extension Browser Bridge, Chrome DevTools Protocol, Node.js

- **À ne pas confondre avec :** [[OpenCode]], un agent de code sans rapport

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

OpenCLI plaît pour son idée de départ : transformer une page web en commande fiable, sans clé API ni scraper, en réutilisant la session du navigateur. L’argument le plus repris est le coût nul à l’exécution : l’IA écrit l’adaptateur une fois, puis la commande tourne sans consommer de tokens. La facilité d’installation et la couverture des plateformes chinoises (Xiaohongshu, Bilibili, Zhihu, WeChat) expliquent une grande partie de l’adoption. Le recul critique reste faible : la plupart des articles sont promotionnels, et le lancement sur Hacker News n’a suscité que trois commentaires brefs.

Les critiques sérieuses viennent des issues GitHub. Sur Xiaohongshu, des comptes ont été bannis après des actions d’écriture automatisées ; le mainteneur recommande de s’en tenir à la lecture, et un chantier de septembre 2026 ajoute un rythme de requêtes plus humain. Un audit communautaire de l’extension a relevé en mars 2026 l’exécution de JavaScript arbitraire, un accès trop large aux cookies et un contournement de l’isolation des onglets, en partie corrigés. La politique de sécurité promise (confirmation avant les actions d’écriture, liste de sites autorisés) est encore en discussion. Enfin, les adaptateurs cassent quand un site change son interface, parfois en renvoyant un résultat vide sans erreur.

### Comparaison

Agent Browser et Playwright pilotent un navigateur neuf ou isolé, plus sûr mais sans les sessions déjà connectées de l’utilisateur. Chrome DevTools MCP sert surtout au diagnostic (performance, réseau, console). AutoCLI reprend une approche proche, réécrite en Rust. Sur V2EX, des lecteurs relativisent la nouveauté (un pilotage de pages via le Chrome DevTools Protocol) et le comparent à CLI-Anything, un projet de l’université de Hong Kong. OpenCLI se distingue par ses adaptateurs prêts à l’emploi et par la réutilisation directe du navigateur connecté.

### Verdict

Très pratique pour récupérer des données de sites sans API, en lecture seule. À utiliser avec un profil Chrome dédié, sans connexion aux comptes sensibles, et sans laisser un agent agir seul tant que les garde-fous de sécurité ne sont pas livrés. Les issues GitHub restent la source la plus fiable pour juger l’outil.

## Sources

- [GitHub](https://github.com/jackwener/opencli)

- [Site officiel](https://opencli.info/)

- [Issue #399 — durcissement de sécurité de l'extension](https://github.com/jackwener/opencli/issues/399)

- [Issue #1595 — politique de sécurité (écriture, domaines, daemon)](https://github.com/jackwener/opencli/issues/1595)

- [Issue #677 — compte Xiaohongshu banni](https://github.com/jackwener/opencli/issues/677)

### Sources des avis

- [Hacker News — lancement](https://news.ycombinator.com/item?id=47396702)
- [V2EX — annonce](https://www.v2ex.com/t/1199331)
- [V2EX — version 1.0](https://www.v2ex.com/t/1199918)
- [DEV Community — WonderLab](https://dev.to/wonderlab/one-open-source-project-a-day-no39-opencli-turning-any-website-into-a-zero-cost-cli-tool-for-cg8)
- [DEV Community — Tenglong AI](https://dev.to/tenglongai2026/i-turned-my-browser-into-a-terminal-and-now-i-can-control-any-website-from-the-command-line-124l)
- [Issue #677 — compte Xiaohongshu banni](https://github.com/jackwener/opencli/issues/677)
- [Issue #399 — audit de sécurité de l’extension](https://github.com/jackwener/opencli/issues/399)
- [Issue #1595 — politique de sécurité en discussion](https://github.com/jackwener/opencli/issues/1595)
- [Issue #2470 — rythme des requêtes et anti-détection](https://github.com/jackwener/opencli/issues/2470)

_Dernière analyse : 12 novembre 2026_
