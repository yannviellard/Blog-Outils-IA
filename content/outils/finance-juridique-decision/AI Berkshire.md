---
title: "AI Berkshire"
type: outil
description: "Recherche financière value multi-agent avec vérification et synthèse contradictoire."
format: collection
tags:
  - metier/direction
  - metier/operations
  - theme/recherche
  - theme/multi-agent
editeur: "xbtlin"
site: "https://github.com/xbtlin/ai-berkshire"
depot: "https://github.com/xbtlin/ai-berkshire"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-04
etoiles: 17095
forks: 2513
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 3
note_maturite: 2
note_popularite: 4
memo: "[[AI Berkshire mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# AI Berkshire

> Framework de recherche en investissement basé sur Claude Code et Codex, qui transforme des méthodologies d'investissement value en workflows structurés combinant **20 skills, multi-agent research, vérification des données et synthèse contradictoire**.

**Composition** : 20 skills, 4 agents et un Team Lead.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[AI Berkshire mémo]] pour le mémo pratique.

## Résumé

AI Berkshire est un framework de recherche financière conçu pour Claude Code et Codex. Il formalise les approches de Warren Buffett, Charlie Munger, Duan Yongping et Li Lu dans une collection de skills spécialisés.

Son architecture repose sur trois couches : **Skill Layer** pour les workflows, **Agent Layer** pour les analyses parallèles et contradictoires, et **Tool Layer** pour les recherches web, les calculs financiers et l'audit des rapports.

Le projet se distingue surtout par son approche **multi-agent** : certains workflows lancent quatre analystes indépendants représentant différentes perspectives, puis un Team Lead confronte et synthétise leurs résultats. Le dépôt fournit également des scripts et outils de vérification afin de limiter les erreurs de données et de calcul.

## Fonctionnalités

- **20 skills spécialisés** couvrant recherche d'entreprises, earnings, analyse sectorielle, screening, portefeuille, suivi de thèse et outils de réflexion.
    
- **Recherche multi-agent parallèle** avec quatre analystes indépendants et un Team Lead chargé de la synthèse et de la confrontation des résultats.
    
- **Cross-validation financière** avec récupération de données depuis plusieurs sources et outils de vérification des calculs.
    
- **Workflows de recherche longue** pouvant produire des rapports structurés et réutilisables.
    
- **Compatibilité Claude Code + Codex** avec une source canonique de skills et des adaptations Codex générées automatiquement.
    
- **Suivi de thèse et détection de dérive** permettant de comparer différentes versions d'une analyse dans le temps.
    
- **Screening hiérarchique** permettant de filtrer rapidement avant de lancer les analyses approfondies.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Architecture des workflows|★★★★★|
|Multi-agent|★★★★☆|
|Vérification / rigueur des données|★★★☆☆|
|Portabilité|★★★★☆|
|Maturité|★★☆☆☆|
|Popularité|★★★★☆|
|Réutilisabilité des patterns|★★★★★|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 17 095 au 11 novembre 2026._

**Commentaire :** projet particulièrement intéressant pour son architecture de recherche plutôt que pour son domaine financier. La séparation **skills → agents → tools**, la recherche parallèle et la vérification indépendante constituent des patterns facilement transposables à d'autres systèmes d'agents. La documentation est abondante et le projet est activement maintenu, avec plus de 1 300 commits et une activité importante sur les issues et pull requests. Les notes de vérification des données et de maturité sont prudentes : les mécanismes de vérification sont ceux du projet, sans validation indépendante, le backtesting historique n'est pas encore livré et le recul indépendant reste faible (la plupart des contenus reprennent le dépôt ou son positionnement ; voir [[#Avis indépendants|les avis indépendants]]).

### Points forts

- Architecture claire en **trois couches** : skills, agents et tools.
    
- Bon exemple de **multi-agent research** : les agents produisent des analyses indépendantes avant synthèse (indépendance relative : ce sont des instances du même modèle, qui peuvent partager les mêmes données et les mêmes erreurs).
    
- Importance accordée à la **traçabilité et à la vérification des données**, plutôt qu'à une simple génération de texte.
    
- 20 workflows couvrant différents niveaux de profondeur, du screening rapide à la recherche approfondie.
    
- Compatible avec **Claude Code et Codex**, avec une base de workflow commune.
    
- Projet actif et suivi (voir la note Popularité, qui mesure l'attention portée au dépôt, non la validité de la méthodologie).
    
- Le projet est suffisamment structuré pour servir de **référence d'architecture pour des systèmes multi-agents spécialisés**.
    

### Limites

- Très fortement spécialisé dans l'investissement et la recherche financière.
    
- Une partie importante des workflows dépend de conventions propres au dépôt (`reports/`, `tools/`, scripts et structures de fichiers), ce qui limite l'installation “plug-and-play” des skills dans un autre environnement.
    
- Les performances financières publiées par le projet sont celles du mainteneur et ne constituent pas une validation indépendante de la méthodologie.
    
- Les workflows multi-agent peuvent être **coûteux en tokens et en temps**, particulièrement pour les analyses approfondies.
    
- La forte spécialisation des prompts autour des quatre investisseurs réduit la généricité de certaines skills.
    
- Le projet annonce encore comme travaux futurs le **backtesting historique**, l'analyse macroéconomique et l'intégration de données temps réel via MCP ; ces éléments ne font donc pas encore partie du framework complet.

- **Impression de certitude excessive** : une synthèse très structurée peut paraître plus sûre qu'elle n'est ; la qualité dépend des données récupérées (ce n'est ni une base financière propriétaire ni un terminal de marché) et le coût en appels de modèle est élevé.

- **Ne constitue pas un conseil en investissement** : le framework formalise un processus d'analyse à auditer par son utilisateur, pas des signaux ou recommandations prêts à l'emploi.
    

## Relations
    
- **Alternative à :** [[AI Research Agents]], [[Investment Research Agents]]
    
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]]
    
- **Utilise :** Web Search · Python · scripts de vérification financière · subagents
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

L’accueil est surtout positif chez les personnes qui cherchent à formaliser une analyse « value » avec Claude Code ou Codex. Les points appréciés sont les checklists reproductibles, la confrontation de plusieurs analystes et le recours prioritaire aux documents financiers primaires. Le projet semble particulièrement utile comme **cadre de travail** et comme antidote à une analyse improvisée.

Le recul indépendant reste toutefois faible : beaucoup de contenus reprennent le dépôt ou son positionnement. Les réserves portent sur la dépendance à la qualité des données récupérées, le coût en appels de modèles et le risque qu’une synthèse très structurée donne une impression de certitude excessive. Ce n’est ni une base financière propriétaire ni un substitut à la vérification humaine.

### Comparaison

Face à Perplexity, Gemini Deep Research ou un terminal Bloomberg, AI Berkshire apporte une méthodologie d’investissement plus explicite, mais moins de données propriétaires. Il convient mieux à un investisseur qui veut auditer son raisonnement qu’à celui qui attend des signaux ou recommandations prêts à l’emploi.

### Verdict

Prometteur et différenciant pour structurer une recherche fondamentale ; à utiliser comme processus d’analyse, jamais comme conseiller financier autonome.

## Sources

- [GitHub — AI Berkshire](https://github.com/xbtlin/ai-berkshire)
    
- [README English](https://github.com/xbtlin/ai-berkshire/blob/main/README_EN.md)
    
- [Investment Team Skill](https://github.com/xbtlin/ai-berkshire/blob/main/codex-skills/investment-team/SKILL.md)
    
- [Contributing Guide](https://github.com/xbtlin/ai-berkshire/blob/main/CONTRIBUTING.md)
    

### Sources des avis

- [Présentation et workflows officiels](https://github.com/xbtlin/ai-berkshire/blob/main/README.md)
- [Revue TopGit](https://topgit.dev/repo/xbtlin/ai-berkshire)
- [Analyse du niveau de validation publique](https://tuleo.net/entities/ai-berkshire?locale=en)

_Dernière analyse : 12 novembre 2026_