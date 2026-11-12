---
title: "MCP (Model Context Protocol)"
type: concept
description: "Protocole ouvert qui relie un agent ou une application d'IA à des outils et à des sources de données externes."
aliases:
  - MCP
  - MCP Protocol
  - serveur MCP
  - serveurs MCP
modified: 2026-11-12
---

# MCP (Model Context Protocol)

> Protocole ouvert qui relie un agent ou une application d'IA à des outils et à des sources de données externes.

Le **Model Context Protocol** standardise la façon dont une application d'IA (un agent, un assistant, un éditeur) se connecte à des outils et à des données. Un serveur MCP écrit une fois fonctionne avec tous les clients compatibles. Anthropic a publié le protocole le 25 novembre 2024, puis l'a confié le 9 décembre 2025 à l'Agentic AI Foundation, un fonds de la Linux Foundation cofondé avec Block et OpenAI.

## Fonctionnement

- **Trois rôles**, selon la spécification : l'**hôte** (l'application d'IA qui ouvre les connexions), le **client** (le connecteur, dans l'hôte, qui dialogue avec un serveur) et le **serveur** (le service qui fournit du contexte et des capacités). Les messages suivent le format JSON-RPC 2.0.
- **Ce qu'un serveur expose** : des **outils** (fonctions que le modèle peut appeler), des **ressources** (données à lire) et des **prompts** (modèles de messages). Le client peut de son côté permettre au serveur de demander une information à l'utilisateur.
- **Extensions** : des modules optionnels, négociés entre client et serveur, complètent le cœur du protocole, par exemple les tâches asynchrones de longue durée ou des éléments d'interface affichés dans la conversation (MCP Apps).
- La spécification en vigueur au 12 novembre 2026 est celle du 28 juillet 2026. Elle s'inspire du Language Server Protocol, qui joue le même rôle pour les langages de programmation dans les éditeurs.

## Points de vigilance

- **Un outil MCP exécute du code.** La spécification demande que l'hôte obtienne le consentement explicite de l'utilisateur avant d'appeler un outil, et que les descriptions d'outils soient tenues pour non fiables si le serveur ne l'est pas. Le protocole ne peut pas imposer ces règles lui-même : elles reposent sur l'application.
- **Empoisonnement d'outils.** Invariant Labs a décrit le 1er avril 2025 des attaques où des instructions cachées dans la description d'un outil, invisibles pour l'utilisateur mais lues par le modèle, détournent l'agent. CyberArk a montré ensuite que tout le schéma d'un outil, et pas seulement sa description, peut servir de vecteur. Un serveur peut aussi modifier la description d'un outil après son approbation.
- **Coût en contexte.** Chaque serveur connecté ajoute la description de ses outils au contexte du modèle. Installer peu de serveurs, de sources connues, et vérifier leurs permissions.

## Dans le wiki

- **Serveurs MCP** : [[Chrome DevTools MCP]], [[Glif MCP]], [[Perplexity MCP]].
- **Clients** : les agents de développement ([[Claude Code]], [[OpenAI Codex]], [[OpenCode]], [[Hermes Agent]]).
- Les fiches qui exposent ou consomment des serveurs MCP portent le thème [[tags/theme/mcp|MCP]].

## Sources

- [Spécification du Model Context Protocol](https://modelcontextprotocol.io/specification/latest) : version du 28 juillet 2026, consultée le 12 novembre 2026.
- [Anthropic, Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) : annonce de l'éditeur, 25 novembre 2024.
- [Anthropic, Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) : annonce de l'éditeur, 9 décembre 2025.
- [Linux Foundation, création de l'Agentic AI Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation) : communiqué.
- [Invariant Labs, MCP Security Notification: Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification) : recherche en sécurité, 1er avril 2025, par une entreprise qui développe des outils de sécurité pour agents.
- [CyberArk, Poison everywhere: No output from your MCP server is safe](https://www.cyberark.com/resources/threat-research-blog/poison-everywhere-no-output-from-your-mcp-server-is-safe) : recherche en sécurité d'un éditeur du secteur.

_Dernière analyse : 12 novembre 2026_
