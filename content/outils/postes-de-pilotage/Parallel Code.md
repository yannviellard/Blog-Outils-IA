---
title: "Parallel Code"
type: outil
description: "Application MIT, locale et sans compte pour lancer plusieurs CLI dans des worktrees."
format: application
tags:
  - metier/ingenierie
  - theme/multi-agent
  - theme/revue-de-code
editeur: "johannesjo"
logo: "[[parallel-code.png]]"
site: "https://parallelcode.app"
depot: "https://github.com/johannesjo/parallel-code"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 1091
forks: 151
etoiles_releve: 2026-11-16
note_documentation: 3
note_precision: 3
note_maturite: 2
note_popularite: 3
memo: "[[Parallel Code mémo]]"
avis_maj: 2026-10-10
modified: 2026-11-12
---

# Parallel Code

> Application locale et MIT pour exécuter Codex, Claude Code, Gemini, Copilot CLI ou d'autres agents côte à côte, chacun dans sa branche et son worktree.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Parallel Code mémo]] pour le mémo pratique.

## Résumé

Parallel Code cherche à conserver la transparence du terminal tout en ajoutant la structure qui lui manque. Lors de la création d'une tâche, l'application crée une branche et un worktree, lance l'agent choisi, suit son terminal et présente ensuite le diff. L'utilisateur peut comparer plusieurs solutions, commenter le code, fusionner le résultat retenu ou supprimer les autres.

Le projet est gratuit, sans compte, sans serveur de l'éditeur et sous MIT. Il fonctionne sur macOS et Linux. Un mode Docker optionnel renforce l'isolation du processus, mais sa configuration des variables d'environnement mérite une attention particulière.

## Fonctionnalités

- Branche et worktree automatiques par tâche.
- Vue tuilée ou focus, navigation au clavier et terminaux par tâche.
- Diff intégré, commentaires en ligne, commit, push et fusion.
- Mode Arena : même prompt envoyé à plusieurs agents pour comparer les résultats.
- Import de worktrees existants et mode direct sans isolation.
- Monitoring sur téléphone via réseau local ou Tailscale.
- Sandboxing Docker configurable par `.parallel-code/Dockerfile`.
- État persistant, notifications système, thèmes et raccourcis personnalisables.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★☆☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (11 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 1 091 au 16 novembre 2026._

### Points forts

- Licence MIT, fonctionnement local et absence de télémétrie déclarée.
- Modèle mental simple : une tâche, une branche, un agent, un diff.
- Aucun abonnement de plateforme en plus des agents utilisés.
- Revue et comparaison intégrées sans masquer les vrais terminaux.
- Docker disponible lorsque l'isolation Git ne suffit pas.

### Limites

- Projet plus jeune et communauté plus petite que les leaders.
- Peu d'avis indépendants détaillés ; beaucoup de contenus proviennent du créateur.
- Windows non pris en charge.
- Interface Electron plus lourde qu'un outil natif ou une TUI.
- En Docker, certaines clés API de l'environnement peuvent être transmises par défaut au conteneur.

### Qualité

**Commentaire :** option locale et réversible pour essayer les worktrees multi-agent. La précision des descriptions est notée ★★★☆☆ : une part importante des contenus détaillés vient du créateur et les avis indépendants sont peu nombreux. La maturité (★★☆☆☆) et la sécurité du passage d'environnement doivent être validées selon le contexte.

## Relations

- **Alternative à :** [[Paradev]], [[Conductor]], [[Claude Squad]]
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], Gemini CLI, Copilot CLI, Docker
- **Utilise :** Git worktrees, terminaux locaux, GitHub CLI

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 10 octobre 2026._

### Synthèse

Les retours disponibles mettent en avant la réduction du changement de contexte : voir plusieurs terminaux et leurs diffs dans une seule fenêtre rend les sessions plus faciles à comparer. Le caractère local, gratuit et compatible avec plusieurs CLI est également apprécié.

Il faut cependant interpréter ces signaux avec prudence. Une part importante des publications Reddit et articles détaillés a été écrite par le créateur du projet. Les réponses indépendantes sont encore peu nombreuses et suggèrent parfois que des worktrees manuels suffisent aux développeurs expérimentés.

### Avis favorables

- Passage presque immédiat depuis une collection de terminaux existants.
- Isolation automatique qui évite les changements de branche dans le checkout principal.
- Mode Arena utile pour comparer deux modèles ou deux approches.
- Pas de compte, pas de serveur de l'éditeur et licence permissive.
- Vue mobile pratique pour savoir si un agent réclame une décision.

### Critiques et risques

- Manque de recul communautaire et faible volume d'avis vraiment indépendants.
- Plusieurs demandes UX et hooks de cycle de vie restent ouvertes.
- Les worktrees n'isolent pas les ports, bases ou processus.
- Le mode Docker peut transmettre des clés présentes dans l'environnement ; il faut les retirer explicitement.
- Le gain face à Git worktree + terminal dépend fortement du besoin de vue graphique.

### Verdict

Le meilleur candidat pour une expérimentation locale, libre et peu engageante. À adopter progressivement sur des tâches non sensibles avant de lui confier secrets, accès cloud ou fusion automatisée.

## Sources

- [Dépôt officiel](https://github.com/johannesjo/parallel-code)
- [Politique de confidentialité](https://github.com/johannesjo/parallel-code/blob/main/PRIVACY.md)
- [Site](https://parallelcode.app)

### Sources des avis

- [Présentation et discussion initiale](https://www.reddit.com/r/ClaudeCode/comments/1s3lwj7/i_built_a_gui_that_runs_real_claude_code/)
- [Discussion sur la charge mentale multi-agent](https://www.reddit.com/r/ClaudeAI/comments/1rbtmfd/ive_been_running_5_claude_code_instances_in/)
- [Issues du projet](https://github.com/johannesjo/parallel-code/issues)
- [Politique de confidentialité et Docker](https://github.com/johannesjo/parallel-code/blob/main/PRIVACY.md)

_Dernière analyse : 12 novembre 2026_
