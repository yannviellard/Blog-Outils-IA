---
title: "Claude SEO — Mémo"
type: memo
fiche: "[[Claude SEO]]"
date: 2026-09-25
---

# Claude SEO — Mémo

> Les commandes à connaître pour [[Claude SEO]], le plugin SEO complet pour Claude Code : audit de site avec des sous-agents en parallèle, SEO technique, contenu (E-E-A-T), Schema.org, visibilité dans les moteurs IA (GEO), SEO local, e-commerce, international, rapports. Toutes les commandes commencent par `/seo`.

## Installation

```bash
# Plugin Claude Code (≥ 1.0.33)
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
/seo setup        # crée un environnement Python isolé et installe Chromium
/seo doctor       # vérifie que tout est prêt, sans rien modifier
```

Prérequis : Python 3.10+. Des identifiants Google (Search Console, GA4, PageSpeed) sont optionnels mais donnent de vraies données : `/seo google setup`.

## Démarrage rapide

|Commande|Ce qu'elle fait|
|---|---|
|`/seo audit <url>`|Audit complet : jusqu'à 500 pages, sous-agents en parallèle, score de santé sur 100 et plan d'action priorisé (critique / haute / moyenne / basse).|
|`/seo page <url>`|Analyse approfondie d'une page.|
|`/seo schema <url>`|Détecte, valide et génère le balisage Schema.org.|
|`/seo geo <url>`|Optimisation pour les réponses des IA (AI Overviews, ChatGPT…).|
|`/seo sitemap generate`|Génère un sitemap XML.|

## Toutes les commandes principales

### Audit et technique

|Commande|Ce qu'elle fait|
|---|---|
|`/seo technical <url>`|Audit technique en 9 catégories : exploration, indexation, sécurité, URL, mobile, Core Web Vitals, données structurées, rendu JavaScript, IndexNow.|
|`/seo images <url>`|Optimisation des images.|
|`/seo hreflang <url>`|Audit et génération hreflang (sites multilingues).|
|`/seo agentic <url>`|Accessibilité du site aux agents IA : `llms.txt`, Markdown, WebMCP.|
|`/seo drift baseline` / `compare` / `history <url>`|Suit l'évolution SEO d'un site dans le temps.|

### Contenu et stratégie

|Commande|Ce qu'elle fait|
|---|---|
|`/seo content <url>`|Qualité du contenu et E-E-A-T.|
|`/seo content-brief <sujet>`|Brief de contenu : mots-clés, plan, liens internes.|
|`/seo cluster <mot-clé>`|Regroupement sémantique à partir des résultats Google.|
|`/seo plan <type>`|Stratégie SEO (`saas`, `local`, `ecommerce`, `publisher`, `agency`).|
|`/seo programmatic <url>`|SEO programmatique (pages générées à grande échelle).|
|`/seo competitor-pages <url>`|Pages de comparaison avec les concurrents.|
|`/seo sxo <url>`|Search Experience Optimization : type de page, personas.|

### Local, e-commerce, liens

|Commande|Ce qu'elle fait|
|---|---|
|`/seo local <url>`|SEO local : fiche Google, citations, avis.|
|`/seo maps [commande]`|Analyse cartographique et concurrence locale.|
|`/seo ecommerce <url>`|SEO e-commerce et marketplaces.|
|`/seo backlinks <url>`|Profil de liens entrants.|

### Données et extensions

|Commande|Ce qu'elle fait|
|---|---|
|`/seo google [commande]`|API Google : Search Console, PageSpeed, CrUX, GA4, rapports PDF.|
|`/seo bing [commande] <url>`|Bing Webmaster Tools et soumission IndexNow.|
|`/seo ahrefs`, `/seo dataforseo`, `/seo seranking`, `/seo profound`|Extensions vers des outils payants (comptes nécessaires).|
|`/seo unlighthouse <url>`|Lighthouse sur plusieurs pages, en local.|

## Conseils d'utilisation

- **Lancer `/seo doctor` en premier** en cas de problème.
- **Brancher Google Search Console** : sans lui, les Core Web Vitals sont des estimations de laboratoire et l'indexation est déduite, pas mesurée.
- **Coût d'un audit complet** : cinq agents tournent sur Opus depuis la v2.3.1. Commencer par `/seo page` ou `/seo technical` sur un gros site, puis l'audit complet.
- **Sites en JavaScript lourd** : certains constats peuvent être faux (contenu chargé au scroll ou après un clic). Vérifier sur une capture avant d'agir.
- **Suivre dans le temps** : poser une référence avec `/seo drift baseline`, puis comparer après chaque grosse modification.
- **Lire le script d'installation** avant de l'exécuter si tu n'utilises pas le plugin.

## Sources

- [README Claude SEO](https://github.com/AgriciDaniel/claude-seo)
- [Référence des commandes](https://github.com/AgriciDaniel/claude-seo/blob/main/docs/COMMANDS.md)
- [How to Run a Free SEO Audit With Claude SEO](https://claude-seo.md/blog/how-to-run-free-seo-audit-claude-seo)
- [I Ran Claude SEO on My Sites — Engr Mejba Ahmed](https://www.mejba.me/public/index.php/blog/claude-seo-toolkit-guide)
