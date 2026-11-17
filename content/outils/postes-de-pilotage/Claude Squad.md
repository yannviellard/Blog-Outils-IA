---
title: "Claude Squad"
type: outil
description: "TUI fondée sur tmux et Git worktrees pour piloter plusieurs agents CLI."
format: cli
tags:
  - metier/ingenierie
  - theme/multi-agent
editeur: "smtg-ai"
site: "https://smtg-ai.github.io/claude-squad/"
depot: "https://github.com/smtg-ai/claude-squad"
licence: "AGPL-3.0"
statut: disponible
derniere_maj: 2026-08-20
etoiles: 8817
forks: 636
etoiles_releve: 2026-11-16
note_documentation: 3
note_precision: 4
note_maturite: 3
note_popularite: 3
memo: "[[Claude Squad mémo]]"
avis_maj: 2026-10-10
modified: 2026-11-12
---

# Claude Squad

> TUI open source qui lance plusieurs agents CLI dans des sessions tmux et des Git worktrees distincts, avec navigation, aperçu de diff et opérations de branche depuis un seul terminal.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Claude Squad mémo]] pour le mémo pratique.

## Résumé

Claude Squad fournit la couche minimale absente de tmux : une liste de tâches, un état par agent, un aperçu de sa sortie et un diff. Chaque nouvelle session obtient un worktree et une branche construits à partir de l'état Git de départ. L'agent continue en arrière-plan dans tmux et peut être réattaché à tout moment.

Malgré son nom, le programme accepte Codex, Gemini, OpenCode, Aider et toute commande compatible. Il est particulièrement adapté aux serveurs, à SSH et aux utilisateurs clavier. Il n'offre pas le niveau de revue graphique, navigateur ou configuration d'environnement de [[Paradev]] et [[Conductor]].

## Fonctionnalités

- Une session tmux et un Git worktree par tâche.
- TUI unique pour créer, suivre, mettre en pause, reprendre et supprimer.
- Aperçu terminal et diff commutables.
- Commit/push et checkout depuis le menu.
- Profils nommés pour plusieurs agents et commandes.
- Mode expérimental `--autoyes` pour accepter automatiquement les prompts.
- Configuration locale dans `~/.claude-squad/config.json`.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★☆☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (11 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 8 817 au 16 novembre 2026._

### Points forts

- Léger, gratuit, scriptable et compatible SSH.
- Architecture transparente fondée sur tmux, Git et les CLI réelles.
- Plusieurs profils évitent le verrouillage sur Claude Code.
- Communauté plus importante que beaucoup de petits orchestrateurs TUI.
- Aucun compte ou service cloud supplémentaire.

### Limites

- Requiert tmux, `gh` et une bonne compréhension de Git.
- Visibilité limitée lorsque de nombreux worktrees s'accumulent.
- Hooks de setup, `.env`, dépendances et ports encore rudimentaires.
- Support Windows fragile.
- `--autoyes` peut autoriser des opérations dangereuses sans supervision.
- Pas de navigateur, mémoire partagée ou workflow de revue avancé.

### Qualité

**Commentaire :** point d'entrée TUI pertinent pour qui maîtrise tmux et Git, mais il faut compléter l'isolation Git par une vraie stratégie d'environnement et de revue. Voir [[#Avis indépendants|les avis indépendants]] et [[Claude Squad mémo]].

## Relations

- **Alternative à :** [[Parallel Code]], [[Paradev]], tmux manuel
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], Gemini, Aider, GitHub
- **Utilise :** tmux, Git worktrees, GitHub CLI

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 10 octobre 2026._

### Synthèse

Claude Squad divise les utilisateurs selon leur rapport au terminal. Pour ceux qui maîtrisent tmux et Git, il automatise juste ce qu'il faut : session persistante, worktree, branche, diff et retour rapide dans l'agent. Certains témoignages le décrivent comme une amélioration décisive par rapport aux worktrees manuels.

D'autres le trouvent instable ou encore trop abstrait : la TUI ne suffit pas toujours à comprendre quelles branches existent, quels services tournent et ce qui peut être fusionné. Les issues confirment des difficultés autour de Windows, des variables d'environnement, du timing de lancement des agents et de l'absence de hooks complets pour préparer chaque worktree.

### Avis favorables

- Très faible surcharge pour un utilisateur déjà à l'aise dans tmux.
- Sessions persistantes et accessibles par SSH.
- Worktrees automatiques sans application graphique lourde.
- Possibilité de mélanger Claude, Codex, Gemini et Aider via les profils.
- Projet suffisamment populaire pour disposer d'exemples et de forks.

### Critiques récurrentes

- Bugs et comportement fragile autour de tmux ou des mises à jour de CLI.
- Manque de vue globale explicite pour les non-spécialistes de Git.
- Environnements de développement parallèles à configurer manuellement.
- Windows mal pris en charge.
- Le mode auto-acceptation privilégie le débit au détriment du contrôle.

### Verdict

Très pertinent sur une station Unix ou un serveur distant. Pour un utilisateur qui veut une revue visuelle, des previews et une fusion guidée, [[Parallel Code]] ou [[Paradev]] sont plus appropriés.

## Sources

- [Dépôt officiel](https://github.com/smtg-ai/claude-squad)
- [Issues](https://github.com/smtg-ai/claude-squad/issues)

### Sources des avis

- [Retour enthousiaste sur l'usage avec worktrees](https://www.reddit.com/r/ClaudeAI/comments/1lfimy8/)
- [Retour critique : retour aux worktrees manuels](https://www.reddit.com/r/ClaudeAI/comments/1lsgaab/stopped_using_claude_squad_and_just_use_git/)
- [Difficulté à visualiser les tâches](https://www.reddit.com/r/ClaudeCode/comments/1ua835x/workflow_for_managing_app_features_and_issues/)
- [Issues officielles](https://github.com/smtg-ai/claude-squad/issues)

_Dernière analyse : 12 novembre 2026_
