---
title: "Hook"
type: concept
description: "Action déclenchée automatiquement à un moment précis du cycle de vie d'un agent, capable de bloquer une action."
aliases:
  - Hooks
modified: 2026-11-12
---

# Hook

> Action déclenchée automatiquement à un moment précis du cycle de vie d'un agent, capable de bloquer une action.

Un **hook** est une action définie par l'utilisateur que l'agent exécute automatiquement à un moment précis : avant ou après l'appel d'un outil, à l'envoi d'une demande, à la fin d'une réponse, à l'ouverture d'une session… Une instruction écrite dans un fichier de contexte peut ne pas être suivie ; un hook, lui, s'exécute à chaque fois. C'est le moyen de rendre une règle systématique : formater après chaque modification, bloquer une commande dangereuse, journaliser.

## Fonctionnement (Claude Code)

- **Où les définir** : en JSON dans les fichiers de réglages : `~/.claude/settings.json` (tous les projets), `.claude/settings.json` (projet, partageable), `.claude/settings.local.json` (projet, non versionné), réglages gérés par l'organisation, fichier `hooks/hooks.json` d'un [[Plugin]], ou en-tête d'un skill ou d'un sous-agent.
- **Structure** : un **événement** (par exemple `PreToolUse`, `PostToolUse`, `UserPromptSubmit`, `Stop`, `SessionStart`), un **filtre** (par exemple l'outil `Bash`) et un ou plusieurs **gestionnaires** : commande shell, requête HTTP, appel d'un outil MCP, question posée à un modèle, ou sous-agent (expérimental).
- **Bloquer** : sur les événements qui le permettent, un code de sortie 2 arrête l'action et transmet le message d'erreur à l'agent ; une sortie JSON permet des décisions plus fines (autoriser, refuser, demander).

## Points de vigilance

- **Du code qui s'exécute seul.** Un hook lance des commandes sur la machine à chaque événement : ceux d'un dépôt ou d'un plugin se relisent comme n'importe quel script. Une organisation peut n'autoriser que les hooks qu'elle gère.
- **Pas un contrôle d'accès.** La documentation indique que le filtre conditionnel des hooks fonctionne au mieux et recommande le système de permissions, plutôt qu'un hook, pour imposer une autorisation ou une interdiction stricte.
- **Coût.** Les hooks qui interrogent un modèle l'appellent à chaque déclenchement (voir le coût de [[Security Guidance]]).

## Dans le wiki

- [[Security Guidance]] : contrôles de sécurité déclenchés à l'écriture et avant commit.
- [[Claude-Mem]] et [[MemPalace]] : mémoire alimentée automatiquement par des hooks.
- Les agents [[Claude Code]] et [[OpenAI Codex]] proposent des hooks.

## Sources

- [Claude Code, Hooks reference](https://code.claude.com/docs/en/hooks) : documentation officielle, consultée le 12 novembre 2026.
- [Claude Code, How Claude remembers your project](https://code.claude.com/docs/en/memory) : documentation officielle (les fichiers d'instructions sont du contexte, pas une configuration imposée).

_Dernière analyse : 12 novembre 2026_
