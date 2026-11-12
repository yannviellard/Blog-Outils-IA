---
title: "Worktree"
type: concept
description: "Copie de travail supplémentaire d'un même dépôt Git, qui permet de faire travailler plusieurs agents en parallèle sur des branches différentes."
aliases:
  - Worktrees
  - Git worktree
modified: 2026-11-12
---

# Worktree

> Copie de travail supplémentaire d'un même dépôt Git, qui permet de faire travailler plusieurs agents en parallèle sur des branches différentes.

Un **worktree** (arbre de travail) est une copie de travail rattachée à un dépôt Git existant, créée par `git worktree add`. Chaque worktree a sa propre branche extraite, son propre `HEAD` et son propre index, mais partage le reste du dépôt : historique, branches, configuration. Les outils multi-agents s'en servent pour que plusieurs agents travaillent en même temps sans modifier les mêmes fichiers.

## Fonctionnement

- **Commandes** : `git worktree add <chemin> [<branche>]` crée un worktree ; `git worktree list` les affiche ; `git worktree remove` supprime un worktree sans modification en cours ; `git worktree prune` nettoie ceux dont le dossier a disparu.
- **Une branche, un worktree** : Git refuse par défaut d'extraire dans un nouveau worktree une branche déjà extraite ailleurs (sauf avec `--force`). Chaque tâche travaille donc sur sa propre branche.
- **Avec les agents** : les postes de pilotage créent en général un worktree et une branche par tâche, puis proposent de relire le diff avant fusion (voir [[outils/postes-de-pilotage/index|Postes de pilotage multi-agent]]). Claude Code peut aussi isoler un sous-agent dans un worktree (`isolation: worktree`).

## Points de vigilance

- **Isolation partielle.** Un worktree évite les écrasements directs entre tâches, mais pas les conflits de fusion. Il n'isole ni les ports, ni les bases de données, ni les services locaux, ni les secrets, et n'est pas une frontière de sécurité.
- **Fichiers non suivis.** Les fichiers ignorés par Git (variables d'environnement, dépendances installées, `CLAUDE.local.md`) n'existent que dans le worktree où ils ont été créés.
- **Sous-modules.** Selon la documentation de Git, leur prise en charge est incomplète, et il est déconseillé de créer plusieurs extractions d'un dépôt parent de sous-modules.
- **Relecture.** Le nombre de tâches parallèles utile est limité par ce qui peut réellement être relu.

## Dans le wiki

- Un worktree par tâche : [[Superset]], [[Conductor]], [[Parallel Code]], [[Claude Squad]].
- Terminaux qui laissent l'organisation Git à l'utilisateur : [[cmux]], [[Warp]].

## Sources

- [Git, git-worktree](https://git-scm.com/docs/git-worktree) : documentation officielle, consultée le 12 novembre 2026.
- [Claude Code, Subagents](https://code.claude.com/docs/en/sub-agents) : documentation officielle (option `isolation: worktree`).
- [Claude Code, How Claude remembers your project](https://code.claude.com/docs/en/memory) : documentation officielle (`CLAUDE.local.md` propre à chaque worktree).

_Dernière analyse : 12 novembre 2026_
