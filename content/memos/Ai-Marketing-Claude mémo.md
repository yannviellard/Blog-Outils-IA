---
title: "AI Marketing Claude — Mémo"
type: memo
fiche: "[[Ai-Marketing-Claude]]"
date: 2026-09-25
---

# AI Marketing Claude — Mémo

> Les commandes à connaître pour [[Ai-Marketing-Claude]], la suite marketing pour Claude Code : audit marketing d'un site avec 5 agents en parallèle, rédaction, séquences d'e-mails, calendrier social, publicités, analyse concurrentielle, et rapports PDF prêts pour un client.

## Installation

```bash
git clone https://github.com/zubair-trabzada/ai-marketing-claude.git
cd ai-marketing-claude
./install.sh

pip install reportlab     # optionnel : nécessaire pour les rapports PDF
```

Le dépôt propose aussi une installation en une ligne (`curl … | bash`) ; lire `install.sh` avant de l'exécuter.

## Commandes

Toutes passent par `/market` dans Claude Code.

### Analyser

|Commande|Ce qu'elle fait|
|---|---|
|`/market audit <url>`|Audit complet par 5 agents en parallèle, note globale sur 100, rapport dans `MARKETING-AUDIT.md`.|
|`/market quick <url>`|Aperçu marketing en une minute.|
|`/market landing <url>`|Analyse de conversion (CRO) d'une landing page.|
|`/market funnel <url>`|Analyse et optimisation du tunnel de vente.|
|`/market competitors <url>`|Rapport de veille concurrentielle.|
|`/market seo <url>`|Audit SEO du contenu.|
|`/market brand <url>`|Analyse de la voix de marque et recommandations.|

### Produire

|Commande|Ce qu'elle fait|
|---|---|
|`/market copy <url>`|Réécrit les textes du site, avec exemples avant/après.|
|`/market emails <sujet>`|Séquence d'e-mails complète (bienvenue, nurturing, lancement).|
|`/market social <sujet>`|Calendrier de contenus sociaux sur 30 jours.|
|`/market ads <url>`|Visuels et textes publicitaires pour toutes les plateformes.|
|`/market launch <produit>`|Plan de lancement produit.|

### Livrer à un client

|Commande|Ce qu'elle fait|
|---|---|
|`/market proposal <client>`|Proposition commerciale.|
|`/market report <url>`|Rapport marketing complet en Markdown.|
|`/market report-pdf <url>`|Rapport marketing professionnel en PDF.|

## Barème de l'audit

|Catégorie|Poids|
|---|--:|
|Contenu et message|25 %|
|Optimisation de la conversion|20 %|
|SEO et visibilité|20 %|
|Positionnement concurrentiel|15 %|
|Marque et confiance|10 %|
|Croissance et stratégie|10 %|

## Workflow type (agence ou freelance)

1. `/market audit <site du prospect>` avant le rendez-vous commercial
2. `/market proposal <client>` en s'appuyant sur les constats
3. `/market report-pdf <url>` comme livrable

## Conseils d'utilisation

- **Présenter les constats comme des opportunités**, pas comme des échecs : le client doit se sentir compris, pas jugé (conseil de la skill `market-proposal` elle-même).
- **Relire les notes** : ce sont des estimations du modèle, utiles pour prioriser, pas des mesures objectives.
- **Coût** : `audit` lance 5 sous-agents ; garder `quick` pour un premier tri.
- **Compléter avec des vraies données** (analytics, taux de conversion) : l'outil ne voit que la page publique.

## Sources

- [README ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude)
- [Skill market-proposal](https://github.com/zubair-trabzada/ai-marketing-claude/blob/main/skills/market-proposal/SKILL.md)
- [Rapport d'évaluation — OpenAgentSkill](https://www.openagentskill.com/skills/zubair-trabzada-ai-marketing-claude/evals)
