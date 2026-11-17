---
title: "Superpowers"
type: outil
description: "Processus de développement centré sur clarification, planification, TDD, revue et vérification."
format: collection
tags:
  - metier/ingenierie
  - metier/produit-design
  - theme/planification
  - theme/tests
  - theme/revue-de-code
editeur: "obra"
site: "https://claude.com/plugins/superpowers"
depot: "https://github.com/obra/superpowers"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-03
etoiles: 318267
forks: 28369
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 5
memo: "[[Superpowers mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Superpowers

> Framework de skills et méthodologie de développement pour les coding agents. Superpowers structure le travail de l'agent autour du brainstorming, de la conception, de la planification, du TDD, du développement par sous-agents, de la revue de code et de la vérification finale.

**Composition** : 14+ skills.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Superpowers mémo]] pour le mémo pratique.

## Résumé

Superpowers est une **méthodologie de développement agentique** construite autour d'un ensemble de skills composables. Le projet ne fournit pas principalement de nouveaux outils techniques : il cherche à modifier le comportement du coding agent en lui imposant un processus de développement structuré.

Le workflow principal couvre notamment :

**brainstorming → design → plan d'implémentation → TDD → développement par sous-agents → revue → vérification.**

Le projet est initialement conçu pour Claude Code mais supporte désormais plusieurs coding agents, dont Codex, Cursor, Gemini CLI, OpenCode, GitHub Copilot CLI, Qwen Code et d'autres.

## Fonctionnalités

- **Brainstorming et spécification** : clarification du besoin, exploration des alternatives et validation progressive du design.
    
- **Implementation planning** : transformation du design validé en plan détaillé et découpé en tâches.
    
- **Test-Driven Development** : workflow RED → GREEN → REFACTOR avec priorité donnée aux tests avant l'implémentation.
    
- **Subagent-driven development** : exécution des tâches par des sous-agents avec inspection et revue intermédiaire.
    
- **Systematic debugging** : recherche structurée de la cause racine plutôt que corrections successives des symptômes.
    
- **Code review** : revue de conformité aux spécifications puis revue de qualité du code.
    
- **Git worktrees** : isolation du travail dans des branches/worktrees dédiés.
    
- **Verification before completion** : vérification des résultats avant de déclarer une tâche terminée.
    
- **Skill development** : mécanismes permettant de créer et tester de nouvelles skills.
    
- **Multi-harness** : support de nombreux coding agents au-delà de Claude Code.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★★|
|Qualité méthodologique|★★★★☆|
|Intégration coding agents|★★★★★|
|Simplicité d'utilisation|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 318 267 au 16 novembre 2026._

**Commentaire :** projet très largement adopté (voir la note Popularité ; disponible dans la marketplace officielle de Claude Code), avec une méthodologie clairement documentée et un workflow cohérent. Cette popularité mesure l'attention, pas l'effet sur la qualité du code : aucune mesure indépendante citée ici ne chiffre le gain, d'où des notes de maturité et de qualité méthodologique à ★★★★☆. Sa principale contrepartie est le caractère relativement prescriptif du processus : certaines tâches simples ne nécessitent pas l'ensemble du cycle brainstorming → planification → TDD → sous-agents → revue. Voir [[#Avis indépendants|les avis indépendants]].

### Points forts

- **Structure fortement le développement agentique** au lieu de simplement fournir des prompts ou commandes supplémentaires.
    
- **Favorise la vérification et les preuves** : tests, revue du code et validation avant de considérer une tâche comme terminée.
    
- **Workflow particulièrement adapté aux tâches complexes** nécessitant conception, découpage et modifications successives.
    
- **Subagent-driven development** permettant de séparer implémentation et revue.
    
- **Méthodologie explicite et composable** grâce aux skills indépendantes.
    
- **Forte adoption** et activité importante du dépôt (signal d'attention, non preuve d'efficacité).
    
- **Compatible avec de nombreux coding agents**, ce qui réduit la dépendance à Claude Code.
    
- **MIT**, permettant son utilisation et son adaptation librement.
    

### Limites

- **Processus potentiellement lourd** pour les petites modifications ou tâches triviales.
    
- **Coût en tokens et en temps potentiellement supérieur** lorsqu'un workflow implique plusieurs étapes ou sous-agents.
    
- **TDD prescriptif** qui n'est pas nécessairement pertinent pour tous les types de développement, notamment certaines phases exploratoires ou purement visuelles.
    
- **Dépendance au comportement du coding agent** : les skills constituent des instructions et workflows, et ne garantissent pas mécaniquement leur exécution parfaite.
    
- **Risque de sur-processus** si toutes les tâches sont systématiquement soumises au workflow complet.
    
- **Écosystème en évolution rapide**, avec des différences possibles entre les harnesses et les versions.

- **Suivre un rituel ne garantit pas la justesse** : le processus repose sur un modèle, et des tests écrits en TDD peuvent ne pas couvrir le bon comportement ni valider une architecture correcte. Des développeurs expérimentés préfèrent d'ailleurs appliquer eux-mêmes ces pratiques plutôt que de laisser un plugin les orchestrer.
    

## Relations

- **Alternative à :** workflows de développement agentique personnalisés basés uniquement sur `CLAUDE.md`, plan mode natif, GSD (séparation plus stricte des phases et des contextes), [[BMAD Method]] (cycle produit plus documentaire), [[GStack]]
    
- **S'intègre avec :** Claude Code · Codex · Cursor · Gemini CLI · OpenCode · GitHub Copilot CLI · Qwen Code
    
- **Utilise :** Skills · Subagents · Git · Worktrees · tests automatisés
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Superpowers est fréquemment recommandé pour imposer un processus fiable : clarification, plan, TDD, petits incréments, revue et vérification. Les utilisateurs apprécient qu’il transforme un agent pressé d’écrire du code en collaborateur plus méthodique, sans la lourdeur documentaire d’un framework produit complet.

Les critiques visent la rigidité et la cérémonie sur les tâches simples. Des développeurs expérimentés préfèrent parfois appliquer eux-mêmes ces pratiques plutôt que laisser un plugin les orchestrer. Comme le système repose encore sur un modèle, suivre un rituel ne garantit pas que les tests couvrent le bon comportement ni que l’architecture soit correcte.

### Comparaison

GSD sépare davantage les phases et contextes pour les longs travaux. BMAD couvre découverte produit et architecture avec beaucoup plus d’artefacts. Le plan mode natif est plus léger. Superpowers occupe un bon milieu pour le développement quotidien orienté qualité.

### Verdict

Très bon choix pour les fonctionnalités moyennes à grandes et les équipes qui veulent systématiser TDD et revue ; à désactiver ou alléger pour les corrections triviales.

## Sources

- [GitHub — obra/superpowers](https://github.com/obra/superpowers)
    
- [Claude Plugin Marketplace — Superpowers](https://claude.com/plugins/superpowers)
    
- [ClaudePluginHub — Superpowers](https://www.claudepluginhub.com/plugins/obra-superpowers-2)
    

### Sources des avis

- [Comparaison Superpowers vs GSD](https://defract.dev/vs/gsd-vs-superpowers)
- [Discussion Superpowers, GSD et autres](https://www.reddit.com/r/ClaudeCode/comments/1qlsdjb/superpowers_vs_gsd_vs_others/)
- [Test comparatif de workflows](https://www.chaseai.io/blog/gsd-vs-superpowers-vs-claude-code)

_Dernière analyse : 12 novembre 2026_