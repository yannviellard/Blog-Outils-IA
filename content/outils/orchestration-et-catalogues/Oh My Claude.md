---
title: "Oh My Claude Code"
type: outil
description: "Framework « batteries incluses » d'agents et workflows pour Claude Code."
format: collection
tags:
  - metier/ingenierie
  - theme/multi-agent
  - theme/planification
editeur: "Yeachan-Heo"
site: "https://ohmyclaudecode.com/"
depot: "https://github.com/Yeachan-Heo/oh-my-claudecode"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 40764
forks: 3641
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 4
memo: "[[Oh My Claude mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Oh My Claude Code

> Framework d'orchestration multi-agents pour Claude Code. OMC ajoute des agents spécialisés, des skills, des hooks, des workflows persistants et l'exécution parallèle afin d'automatiser des tâches complexes de développement.

**Composition** : 39 skills, 19 agents, 55 outils MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Oh My Claude mémo]] pour le mémo pratique.

## Résumé

Oh My Claude Code (OMC) est une couche d'orchestration installée au-dessus de Claude Code. Son architecture repose sur quatre briques : **Hooks** pour détecter les événements, **Skills** pour injecter des comportements, **Agents** pour exécuter les tâches et **State** pour conserver l'état des workflows entre les changements de contexte.

Le projet est particulièrement orienté **multi-agent** : les tâches complexes peuvent être décomposées puis distribuées à plusieurs agents spécialisés. Le mode `Team` constitue désormais l'interface d'orchestration principale, avec un pipeline `plan → PRD → execution → verification → fix`.

OMC propose également une CLI (`omc`) et un plugin Claude Code distinct. Il peut faire intervenir d'autres CLI/modèles, notamment **Codex et Gemini**, via des workers tmux.

## Fonctionnalités

- **Agent Teams** : orchestration de plusieurs agents avec tâches partagées et exécution parallèle.
    
- **19 agents spécialisés** : exploration, analyse, planification, architecture, exécution, debugging, tests, sécurité, review, UI, documentation, etc.
    
- **39 skills** : workflows `autopilot`, `ralph`, `ralplan`, `research`, `verify`, `team`, `deep-interview`, `release`, etc.
    
- **Workflows persistants** : certains modes continuent jusqu'à validation de la réalisation (`ralph`).
    
- **Smart model routing** : association des agents à différents niveaux de modèles selon la complexité.
    
- **Multi-modèles** : possibilité de déléguer certaines tâches à Claude, Codex, Gemini et autres providers via la CLI.
    
- **HUD** : suivi en temps réel des agents, tokens, tâches et états d'exécution.
    
- **Skillify** : extraction de patterns issus des sessions afin de créer des skills réutilisables.
    
- **Vérification et QA** : agents et workflows dédiés à la validation du résultat avant de déclarer une tâche terminée.
    
- **MCP** : possibilité de configurer des serveurs MCP additionnels, notamment Context7, Exa ou GitHub.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|
|Richesse fonctionnelle|★★★★★|
|Orchestration multi-agents|★★★★☆|
|Simplicité|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 40 764 au 11 novembre 2026._

**Commentaire :** projet très riche et fortement actif, avec une architecture désormais structurée autour des agents, skills, hooks et états persistants. La documentation est abondante, mais la quantité de fonctionnalités et de modes rend l'ensemble sensiblement plus complexe qu'un simple ensemble de skills. Les nombreuses releases et corrections montrent également un projet encore en évolution rapide. La release 5.4.0 publiée le 11 septembre 2026 comportait notamment 5 nouvelles fonctionnalités et 10 corrections.

### Points forts

- **Orchestration multi-agents très poussée**, avec parallélisation et rôles spécialisés.
    
- **Couverture très large du cycle de développement** : analyse → architecture → planification → implémentation → tests → review → vérification.
    
- **Workflows autonomes** particulièrement adaptés aux tâches longues ou complexes.
    
- **Interopérabilité multi-modèles** avec Claude, Codex et Gemini.
    
- **Extensible** : skills locaux, skills extraits automatiquement et configuration par projet.
    
- Projet actif et suivi (voir la note Popularité, indicateur d'attention et non de qualité).
    

### Limites

- **Complexité élevée** par rapport à Claude Code seul ou à un système de skills plus minimaliste.
    
- Risque de **sur-orchestration** pour les tâches simples : plusieurs agents peuvent ajouter du coût et du contexte sans bénéfice proportionnel.
    
- Les workflows autonomes peuvent être sensibles aux problèmes de contexte ou d'exécution ; des utilisateurs ont notamment rapporté des interruptions de `ralph` nécessitant de relancer l'exécution.
    
- Les gains annoncés en matière de consommation de tokens doivent être considérés avec prudence : le projet annonce notamment **30–50 % d'économie** grâce au routing, mais les résultats indépendants disponibles ne permettent pas de considérer ce chiffre comme établi.
    
- **Chevauchement important avec d'autres frameworks** de workflow Claude Code, notamment [[Superpowers]] et [[GStack]].
    
- L'activation des Agent Teams repose encore sur une fonctionnalité expérimentale de Claude Code.

- **Recouvrement avec les fonctions natives** : sous-agents, agent teams et workflows de [[Claude Code]] évoluent vite ; les règles du framework peuvent entrer en conflit avec celles du dépôt ou avec ces fonctions natives, et compliquer les mises à jour.

- **Peu de retours indépendants** consacrés spécifiquement au projet (voir [[#Avis indépendants|les avis indépendants]]) : la note d'orchestration repose sur la documentation du projet, sans évaluation tierce comparant le gain à un agent unique bien cadré.
    

## Relations

- **Alternative à :** [[Superpowers]] — les deux proposent une méthodologie structurée de développement, mais OMC est davantage orienté orchestration et automatisation multi-agents.
    
- **S'intègre avec :** Claude Code · Codex CLI · Gemini CLI · MCP · tmux · Git worktrees
    
- **Inspiré par :** [[oh-my-opencode]] · [[Superpowers]] · [[Everything Claude Code]] · [[Ouroboros]]
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le projet plaît aux utilisateurs qui veulent une expérience « batteries incluses » : agents, commandes et workflows prêts à l’emploi évitent de construire leur configuration Claude Code pièce par pièce. Le nom et la philosophie évoquent un framework de productivité, utile pour découvrir des patterns avancés rapidement.

Le nombre de retours indépendants spécifiquement consacrés au projet demeure limité. Les débats sur les frameworks voisins mettent en garde contre la surcouche : trop de commandes et de phases peuvent rendre le comportement difficile à suivre, gonfler la consommation et compliquer la mise à jour. Les règles du framework peuvent également entrer en conflit avec celles du dépôt ou les fonctions natives qui évoluent vite.

### Comparaison

Superpowers est plus resserré autour d’un processus de développement ; BMAD est plus méthodologique et documentaire ; Everything Claude Code ressemble davantage à une distribution complète ; OpenCode/Oh My OpenCode visent un harnais multi-fournisseur.

### Verdict

Intéressant pour démarrer avec un setup très opinionated, mais à évaluer sur un projet réel et à alléger si l’orchestration consomme plus de temps qu’elle n’en économise.

## Sources

- [Website](https://ohmyclaudecode.com/)
    
- [GitHub](https://github.com/Yeachan-Heo/oh-my-claudecode)
    
- [Architecture](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/main/docs/ARCHITECTURE.md)
    
- [Reference](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/main/docs/REFERENCE.md)
    
- [Releases](https://github.com/Yeachan-Heo/oh-my-claudecode/releases)
    

### Sources des avis

- [Site officiel](https://ohmyclaudecode.com/)
- [Dépôt officiel](https://github.com/Yeachan-Heo/oh-my-claudecode)
- [Comparaison de systèmes de workflow](https://www.reddit.com/r/ClaudeAI/comments/1sybpya/compared_11_popular_claude_code_workflow_systems/)

_Dernière analyse : 12 novembre 2026_