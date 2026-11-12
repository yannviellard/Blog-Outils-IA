---
title: "Conductor"
type: outil
description: "Application macOS guidée pour exécuter, relire et fusionner des agents dans des workspaces isolés."
format: application
tags:
  - metier/ingenierie
  - theme/multi-agent
  - theme/revue-de-code
editeur: "Melty Labs"
site: "https://www.conductor.build"
licence: "Propriétaire"
statut: disponible
note_documentation: 4
note_precision: 4
note_maturite: 3
memo: "[[Conductor mémo]]"
avis_maj: 2026-10-10
modified: 2026-11-12
---

# Conductor

> Application macOS pour exécuter Codex, Claude Code, Cursor et OpenCode dans des workspaces Git isolés, puis relire, tester et fusionner leur travail depuis une interface guidée.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Conductor mémo]] pour le mémo pratique.

## Résumé

Conductor traite chaque unité livrable comme un workspace comprenant branche, worktree, terminal, conversation, environnement d'exécution et parcours de revue. Plusieurs workspaces servent aux tâches indépendantes ; plusieurs agents peuvent aussi partager un workspace lorsqu'ils doivent travailler sur le même état de code.

L'application locale est gratuite sur Mac. Les offres payantes ajoutent workspaces cloud, collaboration et administration. Conductor est plus prescriptif que [[cmux]] : il ne cherche pas seulement à afficher plusieurs terminaux, mais à encadrer le cycle création → exécution → diff → checks → pull request → archivage.

## Fonctionnalités

- Worktree et branche par workspace.
- Plusieurs agents dans un même workspace ou plusieurs workspaces parallèles.
- Diff viewer avec commentaires renvoyables à l'agent.
- Checks GitHub, état de la CI, déploiements, commentaires et todos.
- Scripts de setup, run et archive dans `.conductor/settings.toml`.
- Copie explicite des fichiers ignorés et variables propres au workspace.
- Allocation de plages de ports via `CONDUCTOR_PORT`.
- Workspaces cloud isolés dans des sandboxes Linux sur les offres correspondantes.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|—|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (11 octobre 2026). Popularité non notée : pas de dépôt public._

### Points forts

- Interface cohérente pour les utilisateurs qui ne veulent pas gérer tmux et Git à la main.
- Bonne séparation entre tâches indépendantes et agents collaborant sur une branche.
- Parcours de revue et de fusion particulièrement lisible.
- Configuration projet suffisamment riche pour `.env`, dépendances, ports et services.
- Possibilité de commencer localement sans abonnement.

### Limites

- Application locale réservée à macOS.
- Produit fermé et offre cloud payante.
- La préparation d'un worktree peut être lente sur un monorepo lourd.
- Les agents locaux possèdent les permissions de l'utilisateur : le worktree n'est pas une frontière de sécurité.
- Une configuration incomplète entraîne rapidement dépendances réinstallées, secrets absents ou services en collision.

### Qualité

**Commentaire :** choix pertinent pour une équipe qui veut un workflow PR explicite et une interface plus guidée que [[Superset]] ; les critiques les plus sévères visent d'anciennes versions, mais le coût de configuration demeure. La valeur dépend fortement de la qualité de `.conductor/settings.toml`.

## Relations

- **Alternative à :** [[Superset]], [[Parallel Code]], [[Claude Squad]]
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], Cursor, GitHub, Linear
- **Utilise :** Git worktrees, branches, scripts de cycle de vie

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 10 octobre 2026._

### Synthèse

Les utilisateurs favorables citent surtout l'interface, la création automatique des worktrees et le parcours de revue. Certains continuent d'utiliser Conductor au quotidien après avoir essayé [[Superset]] et [[cmux]], ce qui suggère que son approche guidée répond bien au besoin « une tâche, un workspace, une PR ».

Les critiques historiques sont concrètes : lenteur, réinstallation de dépendances, `.env` non recopié, collisions de worktrees et comportement légèrement différent des CLI natives. La documentation actuelle répond à une partie de ces points avec les fichiers à copier, scripts de setup, plages de ports et réglages locaux ; elle ne supprime cependant pas le coût de configuration.

### Avis favorables

- Interface jugée plus claire et agréable que plusieurs alternatives.
- Création, revue et archivage des branches regroupés au même endroit.
- Bon support de la collaboration sur une branche ou de l'isolation entre branches.
- Les checks et commentaires de PR rapprochent l'outil d'un véritable poste de livraison.

### Critiques récurrentes

- Lenteur ressentie sur certains dépôts ou lors de la préparation répétée des workspaces.
- Dépendances et fichiers ignorés absents tant que le projet n'est pas configuré.
- Support incomplet de certaines commandes natives ou slash commands selon le harnais.
- macOS seulement et tarification Pro élevée pour le cloud.
- Risque de donner une impression de sécurité alors que les agents locaux gardent les droits du compte utilisateur.

### Évolution à prendre en compte

Les critiques Reddit les plus sévères décrivent souvent d'anciennes versions. Depuis, Conductor documente explicitement `Files to copy`, les scripts de setup/run/archive et `CONDUCTOR_PORT`. Il faut donc distinguer défaut du produit et projet non préparé pour les worktrees.

### Verdict

Le plus accessible de la sélection pour qui accepte macOS et un workflow structuré. Sur un projet lourd, un test doit mesurer le délai de création d'un workspace, la consommation disque et le temps de remise en route de l'environnement.

## Sources

- [Documentation](https://www.conductor.build/docs)
- [Worktrees](https://www.conductor.build/docs/concepts/git-worktrees)
- [Tarifs](https://www.conductor.build/pricing)

### Sources des avis

- [Comparaison Conductor, Superset et cmux](https://www.reddit.com/r/ClaudeCode/comments/1rxwkoz/my_thoughts_on_conductor_vs_superset_vs_cmux_vs/)
- [Retour critique sur setup et worktrees](https://www.reddit.com/r/ClaudeCode/comments/1ulblh5/i_tried_conductor_cmux_and_the_rest_for_running/)
- [Discussion sur le runtime Claude Code](https://www.reddit.com/r/conductorbuild/comments/1s9a40n/is_conductor_actually_using_claude_code/)
- [Configuration officielle d'un projet](https://www.conductor.build/docs/configure-your-project)

_Dernière analyse : 12 novembre 2026_
