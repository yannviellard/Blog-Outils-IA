---
title: "Plugin"
type: concept
description: "Paquet qui installe d'un coup des skills, des sous-agents, des hooks et des serveurs MCP dans un agent."
aliases:
  - Plugins
  - Marketplace
modified: 2026-11-12
---

# Plugin

> Paquet qui installe d'un coup des skills, des sous-agents, des hooks et des serveurs MCP dans un agent.

Dans Claude Code, un **plugin** est un dossier qui regroupe des [[Skill|skills]], des [[Subagents|sous-agents]], des [[Hook|hooks]], des serveurs [[Model Context Protocol|MCP]] ou d'autres composants, installés et chargés comme un tout. Un manifeste, `.claude-plugin/plugin.json`, lui donne son nom et peut ajouter une version et une description. La plupart des plugins viennent d'une **marketplace** : un catalogue, décrit par un fichier `.claude-plugin/marketplace.json` dans un dépôt ou un dossier, qui indique où récupérer chaque plugin.

## Fonctionnement

- **Installation** : commande `/plugin` dans une session (onglet Discover), à partir des marketplaces ajoutées avec `/plugin marketplace add`. Claude Code ajoute la marketplace officielle d'Anthropic (`claude-plugins-official`) au premier lancement interactif.
- **Portée** : utilisateur (tous les projets de la machine), projet (via `.claude/settings.json`, pour toute l'équipe) ou locale (soi-même, dans ce dépôt).
- **Appel** : les skills d'un plugin portent son nom en préfixe : `/nom-du-plugin:nom-du-skill`.
- **Quand s'en servir** : un skill, un sous-agent, un hook ou un serveur MCP fonctionnent aussi seuls. Le plugin sert à les regrouper, à les partager et à les mettre à jour ensemble.

## Points de vigilance

- **Il s'exécute avec vos droits.** Selon la documentation, un plugin installé peut exécuter du code avec les privilèges de l'utilisateur, quelle que soit sa marketplace.
- **Il pèse sur chaque session.** Un plugin activé ajoute à chaque tour le nom et la description de ses skills et de ses agents au contexte ; ses serveurs MCP tournent et ses hooks se déclenchent, même quand on ne s'en sert pas. Désactiver ce qui ne sert pas (`/plugin` ou `claude plugin disable`).
- **Provenance.** Claude Code réserve les noms de marketplaces officielles aux dépôts `github.com/anthropics/` ; toute autre marketplace, y compris celle d'un collègue ou de son organisation, est tierce.

## Dans le wiki

- **Plugins** : [[Claude Code Review]], [[Claude-Mem]], [[Security Guidance]].
- Beaucoup de collections du wiki se distribuent aussi sous forme de plugins ou de marketplaces, par exemple [[Wshobson Agents]], [[Small Business]] ou [[Everything Claude Code]].

## Sources

- [Claude Code, Plugins overview](https://code.claude.com/docs/en/plugins) : documentation officielle, consultée le 12 novembre 2026.
- [Claude Code, Plugin security and trust](https://code.claude.com/docs/en/plugins/security) : documentation officielle.

_Dernière analyse : 12 novembre 2026_
