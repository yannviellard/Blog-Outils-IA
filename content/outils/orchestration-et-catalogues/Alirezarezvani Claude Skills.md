---
title: "Claude Skills"
type: outil
description: "Très vaste bibliothèque transversale de skills, agents, plugins et commandes."
format: collection
tags:
  - metier/direction
  - metier/support-client
editeur: "alirezarezvani"
site: "https://alirezarezvani.github.io/claude-skills/"
depot: "https://github.com/alirezarezvani/claude-skills"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 29634
forks: 4114
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 4
memo: "[[Alirezarezvani Claude Skills mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Claude Skills

> Bibliothèque open source de skills, agents, plugins et commandes pour les coding agents. Elle couvre notamment le développement, le produit, le marketing, la recherche, la sécurité, les opérations et les fonctions business.

**Composition** : 380 skills et 114 agents, répartis en 20 domaines.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Alirezarezvani Claude Skills mémo]] pour le mémo pratique.

## Résumé

`claude-skills` est une vaste collection de compétences spécialisées destinées aux agents de développement comme Claude Code, Codex CLI, Gemini CLI, Cursor et d'autres outils compatibles avec les Agent Skills.

Le dépôt propose des skills autonomes sous forme de `SKILL.md`, complétés selon les cas par des scripts Python, des références, des templates et des plugins installables. La release 2.12.0 indique 380 skills, 20 domaines, 706 outils Python, 823 documents de référence, 114 agents et 138 commandes slash.

L'approche privilégie des skills relativement indépendants et installables individuellement plutôt qu'une architecture monolithique. Le dépôt fournit également des standards pour créer et maintenir de nouveaux skills.

## Fonctionnalités

- Bibliothèque de **380 skills** couvrant engineering, product, marketing, research, security, business operations, finance et autres domaines.
    
- **Agents et personas spécialisés**, notamment Product Manager, Growth Marketer, Startup CTO et Solo Founder.
    
- **Plugins et commandes slash** permettant d'utiliser les skills individuellement ou par domaine.
    
- Scripts Python déterministes, principalement conçus sans dépendances externes, pour automatiser certaines tâches.
    
- Support de plusieurs coding agents : Claude Code, Codex CLI, Gemini CLI, Cursor et plusieurs autres environnements.
    
- Skills spécialisés de recherche, produit et développement, dont un workflow de deep research multi-sources avec vérification et triangulation des informations.
    
- Standards et mécanismes de contrôle qualité destinés à maintenir la cohérence des skills et plugins.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|
|Richesse fonctionnelle|★★★★★|
|Modularité|★★★★★|
|Cohérence globale|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 29 634 au 11 novembre 2026._

**Commentaire :** le projet est très riche et dispose d'une documentation et de conventions de contribution particulièrement structurées. La quantité de composants est toutefois devenue importante : les 20 domaines et centaines de skills rendent la sélection pertinente plus importante que l'installation globale. La documentation elle-même recommande une installation individuelle des skills, et les conventions imposent des structures et contrôles précis pour les contributions.

### Points forts

- **Très large couverture fonctionnelle** : développement, produit, marketing, recherche, sécurité, finance et opérations sont réunis dans une même bibliothèque.
    
- **Architecture modulaire** : les skills peuvent être sélectionnés et installés individuellement plutôt que d'imposer l'ensemble du dépôt.
    
- **Effort de qualité et de sécurité affiché par le projet** : conventions de structure, validation des scripts, contrôles de références et outils d'audit des skills ; il s'agit de mécanismes déclarés, non d'une validation indépendante du contenu de chaque skill.
    
- **Interopérabilité** avec plusieurs coding agents, ce qui limite le verrouillage sur un seul outil.
    
- Certains composants vont au-delà du simple prompt et fournissent de vrais scripts déterministes et workflows exécutables.
    

### Limites

- **Très grande taille de l'écosystème** : 380 skills et 114 agents peuvent rapidement créer une bibliothèque difficile à maintenir ou à parcourir.
    
- **Qualité potentiellement hétérogène** entre des skills très approfondis et d'autres davantage orientés instructions/workflows.
    
- **Chevauchement fonctionnel** possible avec d'autres collections de skills, agents et frameworks.
    
- La présence de nombreux agents/personas peut encourager une architecture artificiellement multi-agent alors que certains besoins peuvent être traités directement par un agent généraliste.
    
- Les compteurs évoluent rapidement : les chiffres affichés dans le README et ceux des anciennes pages de documentation peuvent différer selon la date de mise à jour.

- **Bruit de contexte et déclenchements ambigus** : installer beaucoup de skills augmente le risque de déclenchements imprécis et de dépendances non auditées ; les analyses de l'écosystème recommandent des skills concises, testées et apportant une information réellement nouvelle au modèle.
    

## Relations

- **Alternative à :** [[Agency Agents]] (centré sur des personas), [[Wshobson Agents]] (marketplace de plugins et orchestrateurs), [[Everything Claude Code]] (configuration plus opinionated)
    
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[Gemini CLI]], [[Cursor]]
    
- **Utilise :** Agent Skills / `SKILL.md`, plugins Claude Code, scripts Python
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

La collection est appréciée pour sa couverture exceptionnelle, sa portabilité entre agents et l’abondance de scripts et références. Elle constitue un bon catalogue pour découvrir des workflows existants et éviter de repartir d’une page blanche.

Comme pour toutes les méga-collections, le volume est aussi sa faiblesse. La qualité, la fraîcheur et le niveau de test ne peuvent pas être uniformes sur des centaines de composants. Installer beaucoup de skills augmente le risque de déclenchements ambigus, de bruit dans le contexte et de dépendances non auditées. Les analyses de l’écosystème recommandent de privilégier des skills concises, testées et apportant une information réellement nouvelle au modèle.

### Comparaison

Face à `wshobson/agents`, cette collection est davantage centrée sur les skills et ressources unitaires ; Agency Agents privilégie les personas ; Everything Claude Code propose une configuration plus opinionated. Son avantage principal reste la largeur du choix, pas une orchestration intégrée.

### Verdict

Excellent catalogue à parcourir et à piocher ; mieux vaut auditer, épingler et tester quelques skills que tout installer.

## Sources

- [GitHub](https://github.com/alirezarezvani/claude-skills)
    
- [Documentation](https://alirezarezvani.github.io/claude-skills/)
    
- [Changelog](https://github.com/alirezarezvani/claude-skills/blob/main/CHANGELOG.md)
    
- [Contributing](https://github.com/alirezarezvani/claude-skills/blob/main/CONTRIBUTING.md)
    

### Sources des avis

- [Documentation officielle](https://alirezarezvani.github.io/claude-skills/)
- [Analyse structurelle de 673 skills](https://www.agentskillreport.com/quality-in-the-agent-skills-ecosystem.pdf)
- [Guide Anthropic de bonnes pratiques](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

_Dernière analyse : 12 novembre 2026_