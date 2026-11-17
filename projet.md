# Projet — Blog Tools IA

## But

Constituer une base de connaissance au format Markdown recensant les outils, frameworks, skills et agents autour de l'IA (principalement l'écosystème Claude Code), puis la publier sous forme de petit blog/wiki avec [Quartz](https://quartz.jzhao.xyz/), à partir d'un repo GitHub.

## Contenu

- Chaque outil fait l'objet d'une fiche Markdown rangée dans le dossier de sa famille, `content/outils/<famille>/`, rédigée à partir du [gabarit](<content/_modeles/Template Article "Nom du projet".md>) commun ; elle se termine par une synthèse des avis indépendants.
- Structure type d'une fiche : métadonnées dans le frontmatter (format, tags, éditeur, site, dépôt, licence, statut, étoiles, notes), résumé, fonctionnalités, analyse notée (★), points forts/limites, relations avec d'autres outils (liens `[[wikilink]]`), avis indépendants, sources.
- Autour des fiches : mémos (`content/memos/`), pages de famille, pages métier (`content/metiers/`), concepts, guides, méthode (barème, taxonomie) et pages de tags. Organisation détaillée : [architecture.md](architecture.md) ; procédure : [CLAUDE.md](CLAUDE.md).
- Tags en français sur deux listes fermées, `metier/…` et `theme/…`, définies dans la [Taxonomie](content/methode/Taxonomie.md).
- Logos des projets stockés dans [images/logos/](images/logos/).
- Rédaction actuellement faite dans Obsidian (dossier `.obsidian/` à la racine de `content/`).

## Publication

- Génération du site statique via Quartz 5 à partir de ce contenu Markdown : moteur installé à la racine le 12 novembre 2026 (version 5.0.0 du 20 septembre 2026), configuration dans `quartz.config.yaml`, construction locale avec `npx quartz build --serve` (voir [CLAUDE.md](CLAUDE.md)).
- Repo GitHub comme source du site : `yannviellard/Blog-Outils-IA`, publié sur GitHub Pages par le workflow `.github/workflows/deploy.yml` à chaque push sur `main`.
- Les wikilinks `[[...]]` entre fiches sont nativement supportés par Quartz et alimentent le graphe de connaissances.

## Décisions (23 septembre 2026)

- **Générateur** : Quartz, dans un seul repo — `content/` devient le dossier de contenu de Quartz et reste le coffre Obsidian.
- **Titre et langue** : « AI Tools Wiki », interface en français.
- **Audience** : blog public et indexé.
- **Hébergement cible** : GitHub Pages, repo `<compte>/blog-tools-ia`, sous-domaine `aitoolswiki.viellard.fr`.
- **Première étape** : tester en local uniquement ; visibilité du repo et mise en ligne décidées après.
- **Accueil** : courte intro, accès par type de fiche, puis le graphe de connaissances.
- **Wikilinks sans cible** : conservés, affichés grisés ; ils servent de liste des fiches à écrire.
- **URLs** : générées par Quartz depuis les chemins des fichiers ; arborescence fixée le 12 novembre 2026 (voir [architecture.md](architecture.md)), à ne plus changer après la mise en ligne.
- **Exclus du site** : le dossier `_modeles/` (gabarits), `.obsidian/` et toute page avec `draft: true`.
- **Logos** : pas affichés pour l'instant.
- **Publication** : commit + push git manuel.
- **Titre d'onglet** (12 novembre 2026) : le titre de la page seul, sans suffixe « · AI Tools Wiki », qui aurait doublé le titre de l'accueil.
- **Mesure d'audience** : aucune pour l'instant (`analytics: null`).
- **Propriétés des fiches** : affichées par l'encadré « Fiche » du plugin local `plugins/wiki-fiche/`, en français.
- **Mise en ligne** (16 novembre 2026) : dépôt GitHub public, GitHub Pages (gratuit pour un dépôt public) et sous-domaine `aitoolswiki.viellard.fr`, déclaré chez BookMyName, qui gère les DNS de viellard.fr, par un enregistrement CNAME vers `yannviellard.github.io`. Écarté : garder le dépôt privé avec Cloudflare Pages.

## À faire

- Mettre en ligne : rendre le dépôt public, activer GitHub Pages (source « GitHub Actions », domaine `aitoolswiki.viellard.fr`), ajouter l'enregistrement CNAME `aitoolswiki` → `yannviellard.github.io.` chez BookMyName, puis cocher « Enforce HTTPS ». Le workflow est écrit et testé sur une copie propre (16 novembre 2026).
- Compléter les logos manquants dans `images/logos/`.
