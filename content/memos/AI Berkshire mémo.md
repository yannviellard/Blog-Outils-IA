---
title: "AI Berkshire — Mémo"
type: memo
fiche: "[[AI Berkshire]]"
date: 2026-09-25
---

# AI Berkshire — Mémo

> Les commandes à connaître pour [[AI Berkshire]], le cadre de recherche en investissement « value » pour Claude Code et Codex. Il applique les méthodes de quatre investisseurs (Buffett, Munger, Duan Yongping, Li Lu) avec des agents qui travaillent en parallèle et se contredisent avant de conclure. Ce sont des outils d'analyse, pas des conseils en investissement.

## Installation

```bash
git clone https://github.com/xbtlin/ai-berkshire.git
cd ai-berkshire

# Claude Code : installe les commandes dans ~/.claude/commands
./scripts/install-claude-commands.sh

# Codex : installe les skills (et, en option, les prompts slash)
./scripts/install-codex-skills.sh
./scripts/install-codex-prompts.sh
```

Dans Codex, appeler une skill par son nom (« utilise investment-research pour étudier Tencent ») ou via `/prompts:investment-research`.

## Commandes

### Recherche approfondie

|Commande|Ce qu'elle fait|
|---|---|
|`/investment-research <société>`|Analyse complète selon les quatre méthodes.|
|`/investment-team <société>`|Même analyse par 4 agents en parallèle : plus rapide et plus complète, plus coûteuse.|
|`/management-deep-dive <dirigeant> <société>`|Étude approfondie de la direction.|
|`/private-company-research <société>`|Société non cotée, avec peu d'information publique (ex. SpaceX).|
|`/deep-company-series <société>`|Série de 8 longs articles sur une entreprise.|

### Résultats financiers

|Commande|Ce qu'elle fait|
|---|---|
|`/earnings-review <société> <période>`|Lecture des résultats à partir des documents originaux uniquement.|
|`/earnings-team <société> <rapport>`|Lecture en équipe, puis article prêt à publier.|

### Filtrer un secteur

|Commande|Ce qu'elle fait|
|---|---|
|`/investment-checklist <sociétés>`|Check-list de Buffett en six étapes : 10 minutes pour décider s'il faut creuser.|
|`/quality-screen <liste, secteur ou indice>`|Élimine les entreprises qui échouent à 7 critères stricts.|
|`/industry-research <secteur>`|Panorama de toute la chaîne de valeur.|
|`/industry-funnel <secteur>`|Du marché entier à 10 candidats, puis 3 analysés en profondeur.|
|`/bottleneck-hunter <tendance>`|Cherche les goulets d'étranglement physiques d'une chaîne d'approvisionnement.|
|`/era-alpha <thème>`|Repère les gagnants d'une grande tendance de croissance, avec règles d'entrée et de sortie.|

### Suivre un portefeuille

|Commande|Ce qu'elle fait|
|---|---|
|`/portfolio-review <positions en %>`|Revue du portefeuille : poids, concentration, rééquilibrage.|
|`/thesis-tracker <société>`|Vérifie si la thèse d'investissement tient toujours après l'achat.|
|`/thesis-drift <société> <thèse1.md> <thèse2.md>`|Compare deux versions d'une thèse : faits, valorisation ou simple formulation.|
|`/news-pulse <société>`|Explique en 10 minutes une forte variation du cours.|
|`/income-investment <valeur> …`|Distingue un dividende durable d'un piège à rendement.|

### Outils de réflexion

|Commande|Ce qu'elle fait|
|---|---|
|`/dyp-ask <question>`|Raisonne à la manière de Duan Yongping.|
|`/financial-data`|Impose deux sources indépendantes pour chaque chiffre clé, alerte au-delà de 1 % d'écart.|
|`/wechat-article <société>`|Article rédigé par trois agents (auteur, éditeur, lecteur).|

## Conseils d'utilisation

- **Filtrer avant d'approfondir** : `/quality-screen` ou `/investment-checklist` d'abord, `/investment-research` ou `/investment-team` seulement si ça vaut le coût. Les analyses complètes consomment beaucoup de tokens.
- **Prendre le meilleur modèle pour les décisions importantes** : l'auteur déconseille d'économiser sur le modèle pour juger une valorisation, un avantage concurrentiel ou une direction.
- **Vérifier un fait clé à part** avec la commande `/deep-research` de Claude Code (selon le README), avant de lancer une analyse de société.
- **Éviter `--dangerously-skip-permissions`** hors d'un environnement de confiance, même si le README le suggère pour limiter les demandes d'autorisation.
- **Contenu surtout en chinois** et centré sur les marchés chinois et hongkongais : les exemples et une partie des rapports sont en chinois.
- **Garder un regard critique** : les performances passées mises en avant par l'auteur ne garantissent rien, et chaque conclusion doit être revérifiée.

## Sources

- [README AI Berkshire (anglais)](https://github.com/xbtlin/ai-berkshire/blob/main/README_EN.md)
- [Dépôt xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)
- [AI Berkshire — DeepWiki](https://deepwiki.com/xbtlin/ai-berkshire)
