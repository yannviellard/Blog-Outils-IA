---
title: "BMAD Method"
type: outil
description: "Méthode complète, de l'idée à l'implémentation, adaptée surtout aux produits complexes."
format: collection
tags:
  - metier/ingenierie
  - metier/produit-design
  - theme/planification
  - theme/tests
editeur: "BMad Code"
site: "https://docs.bmad-method.org/"
depot: "https://github.com/bmad-code-org/BMAD-METHOD"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-08
etoiles: 55261
forks: 6161
etoiles_releve: 2026-11-11
note_documentation: 5
note_precision: 4
note_maturite: 4
note_popularite: 4
memo: "[[BMAD Method mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# BMAD Method

> Framework open source de développement logiciel assisté par IA qui structure l'ensemble du cycle produit, de l'idéation et de l'analyse jusqu'à la planification, l'architecture, l'implémentation et la revue du code, à travers des agents spécialisés et des workflows adaptatifs.

**Composition** : 30+ skills, 5 agents principaux, aucun outil MCP natif.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[BMAD Method mémo]] pour le mémo pratique.

## Résumé

**BMAD (Build More, Architect Dreams)** est une méthodologie AI-native qui transforme des assistants de programmation comme Claude Code, Cursor ou GitHub Copilot en une équipe structurée d'agents spécialisés.

Le framework couvre quatre grandes phases : **Analyse → Planification → Solutioning → Implémentation**, avec des workflows adaptatifs permettant d'utiliser davantage ou moins de processus selon la complexité du changement.

Son approche repose sur trois primitives : des **skills** représentant des capacités, des **agents nommés** apportant une continuité de persona et des **workflows** orchestrant des processus structurés.

La version 6.12.0, publiée en septembre 2026, poursuit une évolution vers une planification adaptative : le framework détermine davantage la quantité de « ceremony » nécessaire après avoir analysé le changement, plutôt que d'imposer systématiquement un processus lourd.

## Fonctionnalités

- **Agents spécialisés** : Analyst, Product Manager, Architect, Developer et UX Designer, chacun disposant de ses propres skills et workflows.
    
- **Product discovery** : brainstorming, recherche marché/domaine/technique, product brief, PRFAQ et recherche approfondie.
    
- **Product & architecture** : PRD, epics/stories, architecture système et préparation à l'implémentation.
    
- **Développement & qualité** : build, sprint planning, code review, génération de tests E2E et rétrospectives.
    
- **Scale-adaptive workflows** : le niveau de processus peut être adapté à la complexité du changement, d'un petit correctif à un projet important.
    
- **Architecture modulaire** : modules complémentaires comme BMad Builder, Test Architect (TEA), Game Dev Studio ou Creative Intelligence Suite.
    
- **Personnalisation** : personas, contexte métier et comportement des workflows peuvent être personnalisés via des overrides sans modifier les fichiers installés.
    
- **Installation simple** : `npx bmad-method install`, avec génération des skills correspondant aux modules installés.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★★|
|Précision des descriptions|★★★★☆|
|Maturité|★★★★☆|
|Popularité|★★★★☆|
|Couverture produit|★★★★★|
|Couverture développement|★★★★☆|
|Flexibilité|★★★★☆|
|Simplicité|★★★☆☆|
|Écosystème|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 55 261 au 11 novembre 2026._

**Commentaire :** BMAD est aujourd'hui un framework très complet et particulièrement structuré pour relier **product discovery → spécifications → architecture → développement**. Sa documentation est abondante et organisée par tutoriels, guides pratiques, explications et références.

Le principal compromis reste la complexité : malgré les évolutions récentes vers des workflows adaptatifs, BMAD possède beaucoup de concepts, d'agents, de skills et de documents. La v6.12 améliore justement ce point en permettant aux changements simples de suivre un chemin beaucoup plus court.

Le projet reste par ailleurs en évolution rapide : plusieurs issues ouvertes en septembre 2026 concernent encore l'installation, les workflows, la persistance du contexte et certaines intégrations.

### Points forts

- **Couverture très large du cycle produit**, depuis l'idée jusqu'au code.
    
- **Très forte structuration du contexte** : les documents produits par une phase alimentent les phases suivantes.
    
- **Agents spécialisés et workflows explicites**, permettant de reproduire une organisation de type équipe produit/tech.
    
- **Approche modulaire et extensible**, avec possibilité de créer ses propres modules et agents.
    
- **Écosystème de modules et adoption élevée** : forte audience du dépôt principal (voir la note Popularité, indicateur d'attention et non de résultat).
    
- **Compatible avec plusieurs assistants de développement**, plutôt que dépendant d'un seul agent.
    

### Limites

- **Complexité et courbe d'apprentissage** supérieures à des frameworks plus légers.
    
- Risque de **sur-processus** lorsque le changement est simple, même si la v6.12 cherche précisément à réduire ce problème.
    
- Nombre important d'artefacts, de skills et de workflows à comprendre.
    
- Projet en évolution rapide avec quelques **régressions et problèmes de compatibilité** encore visibles dans les issues récentes.
    
- Peut être redondant avec d'autres frameworks agentiques couvrant déjà la planification, le développement et la revue.

- **Les livrables générés exigent une revue humaine** : une architecture très détaillée peut partir d'une mauvaise hypothèse, et le coût de coordination (phases, agents, appels de modèle) peut dépasser le bénéfice sur un correctif ou une petite fonctionnalité ; certains utilisateurs reviennent à un plan simple et quelques itérations.
    

## Relations

- **Alternative à :** OpenSpec (le plus léger, centré sur le format des changements), Spec Kit (chemin de spécification plus direct), GSD et [[Superpowers]] (plus compacts pour l'exécution quotidienne), [[GStack]]

- **S'intègre avec :** Claude Code · Cursor · GitHub Copilot · Codex · autres AI coding assistants
    
- **Utilise :** AI coding assistants · Markdown · Git · skills/workflows
    

## Positionnement

BMAD se distingue principalement par son orientation **« product-to-code »** : il cherche à structurer non seulement l'implémentation mais aussi la réflexion produit, la recherche, les exigences, l'UX et l'architecture.

À l'inverse, des frameworks comme **gstack** mettent davantage l'accent sur la transformation d'un agent en équipe de développement capable d'aller jusqu'au **review → QA → ship**, tandis que **Superpowers** se concentre davantage sur la qualité et la discipline du développement agentique.

BMAD est donc particulièrement pertinent lorsque la **définition du produit et de l'architecture** constitue une partie importante du problème, plutôt que comme simple couche de productivité pour coder plus vite.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

BMAD est souvent salué pour remettre de la discipline entre l’idée et le code : analyse, PRD, architecture, stories et revue rendent les décisions plus explicites. Les retours sont particulièrement favorables pour les projets greenfield importants, où la documentation générée aide à limiter les dérives du « vibe coding ».

Le reproche dominant est la **cérémonie**. BMAD multiplie les phases, les agents et les appels de modèle ; pour une correction ou une petite fonctionnalité, ce coût de coordination peut dépasser le bénéfice. Des utilisateurs finissent par revenir à un plan simple et quelques itérations. Les livrables ont aussi besoin d’une revue humaine : une architecture très détaillée peut toujours partir d’une mauvaise hypothèse.

### Comparaison

OpenSpec est le plus léger et centré sur le format des changements ; Spec Kit offre un chemin de spécification plus direct ; BMAD couvre le cycle produit le plus large. Superpowers et GSD sont généralement plus compacts pour l’exécution quotidienne.

### Verdict

Très bon cadre pour un nouveau produit complexe ou une équipe qui manque de méthode ; disproportionné pour les petits changements. À activer selon la taille du travail.

## Sources

- [GitHub — BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
    
- [Documentation officielle](https://docs.bmad-method.org/)
    
- [Documentation — Agents](https://docs.bmad-method.org/fr/reference/agents/)
    
- [Documentation — Workflows](https://docs.bmad-method.org/fr/reference/workflow-map/)
    
- [Changelog](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/CHANGELOG.md)
    
- [Issues](https://github.com/bmad-code-org/BMAD-METHOD/issues)
    

### Sources des avis

- [Comparatif OpenSpec, Spec Kit et BMAD](https://aicodingpatterns.com/en/patterns/openspec-vs-spec-kit-vs-bmad/)
- [Analyse des problèmes résolus par chaque méthode](https://reasoncore.dev/post/bmad-openspec-spec-kit-and-kiro-solve-different-workflow-problems)
- [Discussion GSD, Superpowers et BMAD](https://www.reddit.com/r/ClaudeCode/comments/1rhmnnl/best_framework_for_code_evolutions_gsd/)

_Dernière analyse : 12 novembre 2026_