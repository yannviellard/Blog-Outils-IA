---
title: "Sous-agents"
type: concept
description: "Agent spécialisé, avec son propre contexte, ses instructions et ses outils, auquel l'agent principal délègue une tâche."
aliases:
  - Sous-agent
  - Subagent
modified: 2026-11-12
---

# Sous-agents

> Agent spécialisé, avec son propre contexte, ses instructions et ses outils, auquel l'agent principal délègue une tâche.

Un **sous-agent** travaille dans sa propre fenêtre de contexte, avec ses instructions, ses outils et ses permissions, puis ne renvoie qu'un résumé de son travail à l'agent principal. Une exploration longue ou une sortie volumineuse ne surchargent donc pas la conversation principale. On s'en sert aussi pour spécialiser un rôle (revue de code, recherche) ou pour confier une tâche simple à un modèle plus rapide et moins cher.

## Fonctionnement (Claude Code)

- **Définition** : un fichier Markdown avec un en-tête YAML ; le corps du fichier devient les instructions du sous-agent. Seuls `name` et `description` sont obligatoires ; des champs comme `tools`, `model`, `permissionMode`, `skills`, `mcpServers` ou `hooks` le restreignent ou l'équipent.
- **Emplacements** : `.claude/agents/` (projet), `~/.claude/agents/` (tous les projets), dossier `agents/` d'un [[Plugin]], ou réglages gérés par l'organisation, qui priment sur les autres.
- **Sous-agents intégrés** : notamment Explore (recherche en lecture seule dans le code), Plan (recherche en mode plan) et general-purpose.
- **Délégation** : le sous-agent ne voit pas l'historique de la conversation, seulement le message de délégation. Par défaut, il peut lui-même lancer des sous-agents, jusqu'à trois niveaux sous la conversation principale.

## Points de vigilance

- **Coût.** Chaque sous-agent envoie ses propres requêtes, décomptées des mêmes limites d'usage que la conversation principale. Les résultats détaillés de nombreux sous-agents finissent aussi par occuper le contexte.
- **Latence.** Un sous-agent part de zéro et doit reconstituer le contexte dont il a besoin.
- **Contexte permanent.** Les descriptions de tous les sous-agents disponibles restent dans le contexte ; Claude Code avertit au démarrage au-delà de 15 000 tokens de descriptions cumulées.
- **Plus d'agents ne veut pas dire de meilleurs résultats.** Les avis réunis dans le wiki sur les catalogues et l'orchestration convergent vers « installer peu, épingler, mesurer » (voir [[outils/orchestration-et-catalogues/index|Orchestration et catalogues d'agents]]).

## Dans le wiki

- [[Claude Code]] et [[OpenAI Codex]] fournissent des sous-agents intégrés et acceptent des agents personnalisés.
- [[LLM Council]] fait délibérer cinq conseillers, qui sont des sous-agents d'un même modèle.
- [[Skill Creator]] confie l'évaluation à des sous-agents (grader, comparator, analyzer).
- Catalogues de rôles : [[Agency Agents]], [[Wshobson Agents]], [[Alirezarezvani Claude Skills]].

## Sources

- [Claude Code, Subagents](https://code.claude.com/docs/en/sub-agents) : documentation officielle, consultée le 12 novembre 2026.

_Dernière analyse : 12 novembre 2026_
