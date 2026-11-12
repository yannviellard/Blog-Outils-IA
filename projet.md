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

- Génération du site statique via Quartz à partir de ce contenu Markdown.
- Repo GitHub comme source du site (déploiement type GitHub Pages).
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

## À faire

- Initialiser le repo Quartz et le configurer pour pointer sur le dossier `content/`.
- Vérifier/homogénéiser le frontmatter et les noms de fichiers (espaces, guillemets) en vue de la génération des slugs/URLs.
- Exclure `.obsidian/` de la publication.
- Compléter les logos manquants dans `images/logos/`.
