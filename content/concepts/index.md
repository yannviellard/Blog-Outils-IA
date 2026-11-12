---
title: "Concepts"
type: index
description: "Les notions de base pour comprendre les outils du wiki : MCP, skill, plugin, hook, sous-agent, harnais, worktree, mémoire."
modified: 2026-11-12
---

# Concepts

Les notions qui reviennent dans toutes les fiches, définies une fois, avec leur fonctionnement et leurs points de vigilance.

- [[Model Context Protocol|MCP (Model Context Protocol)]] — protocole ouvert qui relie un agent ou une application d'IA à des outils et à des sources de données externes.
- [[Skill]] — dossier d'instructions et de ressources qu'un agent charge seulement quand la tâche le demande.
- [[Plugin]] — paquet qui installe d'un coup des skills, des sous-agents, des hooks et des serveurs MCP dans un agent.
- [[Hook]] — action déclenchée automatiquement à un moment précis du cycle de vie d'un agent, capable de bloquer une action.
- [[Subagents|Sous-agents]] — agent spécialisé, avec son propre contexte, ses instructions et ses outils, auquel l'agent principal délègue une tâche.
- [[Harnais d'agent]] — logiciel qui entoure un modèle pour en faire un agent : boucle d'exécution, outils, permissions et gestion du contexte.
- [[Worktree]] — copie de travail supplémentaire d'un même dépôt Git, qui permet de faire travailler plusieurs agents en parallèle sur des branches différentes.
- [[Mémoire d'agent]] — ce qu'un agent conserve d'une session à l'autre : fichiers d'instructions, notes qu'il écrit lui-même ou outils de mémoire dédiés.

_Dernière analyse : 12 novembre 2026_
