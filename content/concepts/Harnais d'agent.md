---
title: "Harnais d'agent"
type: concept
description: "Logiciel qui entoure un modèle pour en faire un agent : boucle d'exécution, outils, permissions et gestion du contexte."
aliases:
  - Harnais
  - Agent harness
  - Harness
modified: 2026-11-12
---

# Harnais d'agent

> Logiciel qui entoure un modèle pour en faire un agent : boucle d'exécution, outils, permissions et gestion du contexte.

Le **harnais** (« agent harness » en anglais) est ce qui transforme un modèle de langage en agent. Il envoie la tâche au modèle, exécute les outils que celui-ci demande (lire un fichier, lancer une commande, interroger un serveur [[Model Context Protocol|MCP]]), lui renvoie les résultats et recommence jusqu'à la fin de la tâche. Il fixe aussi les permissions, l'environnement de travail et la gestion du contexte : résumé des échanges trop longs, [[Mémoire d'agent|mémoire]], fichiers d'instructions. Deux agents qui utilisent le même modèle peuvent donc travailler très différemment.

## Fonctionnement

- **Le terme chez Anthropic** : son article du 26 novembre 2025 sur les agents de longue durée qualifie le Claude Agent SDK de harnais d'agent généraliste, qui fournit les outils, la gestion du contexte (dont la compaction) et l'environnement d'exécution.
- **Améliorer l'agent par le harnais** : le même article améliore les résultats sur des tâches longues sans changer de modèle. Une première session prépare l'environnement (script d'initialisation, fichier de progression, liste des fonctionnalités, premier commit) ; chaque session suivante relit cet état, avance d'une fonctionnalité, la teste de bout en bout et laisse le dépôt propre.
- **Dans le wiki**, on appelle harnais les agents complets ([[outils/agents-de-developpement/index|Agents de développement]]) et, par extension, les configurations qui les spécialisent : instructions, [[Skill|skills]], [[Subagents|sous-agents]], [[Hook|hooks]] (voir le guide [[Architecture multi-repos et harnais Claude Code]]).

## Points de vigilance

- **Le harnais décide de ce que l'agent peut faire.** Ses permissions et son isolation (bac à sable, [[Worktree|worktree]]) comptent autant que le modèle.
- **Empiler des couches a un coût.** Les « méta-harnais » qui ajoutent agents, mémoire et orchestration au-dessus d'un agent existant ([[Ruflo]], [[Oh My Claude]]) se jugent sur leur gain face à un agent unique bien cadré.
- **Questions ouvertes** selon Anthropic : un agent généraliste ou plusieurs agents spécialisés, et la portée de ces méthodes au-delà du développement web.

## Sources

- [Anthropic, Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) : article de l'éditeur, 26 novembre 2025.

_Dernière analyse : 12 novembre 2026_
