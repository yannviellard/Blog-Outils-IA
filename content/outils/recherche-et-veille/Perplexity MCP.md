---
title: "Perplexity Control MCP"
type: outil
description: "Serveur communautaire exposant l'ensemble des API Perplexity (clé d'API requise) ; le serveur officiel suffit à la plupart des usages."
format: serveur-mcp
tags:
  - metier/direction
  - metier/marketing-ventes
  - theme/mcp
  - theme/recherche
editeur: "itsablabla"
site: "https://www.perplexity.ai/"
licence: "MIT"
statut: retire
note_documentation: 3
note_precision: 4
note_maturite: 2
memo: "[[Perplexity MCP mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Perplexity Control MCP

> Serveur MCP communautaire qui expose de manière très complète les API Perplexity aux agents IA. Il va au-delà du MCP officiel en donnant accès au Search API, Sonar, Deep Research, Agent API, embeddings, gestion des clés API, estimation des coûts et catalogue des modèles.

> [!warning] Dépôt introuvable
> Au 11 novembre 2026, le dépôt GitHub `itsablabla/perplexity-control-mcp` renvoie une erreur 404 : il a été supprimé ou rendu privé, et aucun paquet npm ne porte ce nom. L'installation décrite ici, qui part d'un clone du dépôt, n'est plus possible en l'état.

**Composition** : 10+ skills, 1 agent, 15+ outils MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves de sécurité, et [[Perplexity MCP mémo]] pour le mémo pratique.

## Résumé

`perplexity-control-mcp` est un serveur **Model Context Protocol** permettant à un agent compatible MCP de piloter directement les différentes API de Perplexity.

Son positionnement est explicitement différent du serveur MCP officiel de Perplexity : alors que celui-ci fournit une interface volontairement simple autour de la recherche, des questions, du raisonnement et du deep research, `perplexity-control-mcp` cherche à exposer **l'ensemble de la surface API** comme un véritable control plane.

Le projet est particulièrement intéressant pour construire des architectures d'agents où Perplexity constitue une couche spécialisée de **web research / intelligence / recherche multi-étapes**.

## Fonctionnalités

- **Agent API** avec `agent_create`, presets de recherche et raisonnement multi-étapes.
    
- **Sonar API** avec contrôle des modèles, paramètres de recherche, filtres de domaines et récence.
    
- **Deep Research asynchrone** avec soumission, suivi et liste des jobs.
    
- **Web Search API** permettant des recherches web brutes avec contrôle fin des résultats.
    
- **Embeddings** classiques et contextualisés.
    
- **Gestion des clés API** : génération, révocation et rotation.
    
- **Estimation des coûts**, catalogue des modèles et health check.
    
- Support **STDIO** et **Streamable HTTP**.
    
- Contrôle beaucoup plus fin des paramètres Perplexity que le MCP officiel.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★☆☆|
|Précision des descriptions|★★★★☆|
|Couverture fonctionnelle|★★★★★|
|Flexibilité API|★★★★★|
|Simplicité d'utilisation|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|—|
|Sécurité|★★★☆☆|
|Pertinence pour agents|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité non notée : le dépôt GitHub est introuvable au 11 novembre 2026._

**Commentaire :** le projet est techniquement ambitieux et couvre une grande partie de l'API Perplexity, avec une architecture relativement claire séparant Agent, Sonar, Search, Embeddings, administration et utilitaires. En revanche, son activité communautaire est très limitée et il s'agit d'un projet tiers, contrairement au serveur MCP officiel de Perplexity.

La principale force est donc la **couverture fonctionnelle**, tandis que le principal risque est de transformer un MCP en exposition directe d'une API complexe, avec de nombreux outils et des fonctions administratives sensibles.

### Points forts

- **Couverture très large** de l'écosystème Perplexity : Search, Sonar, Deep Research, Agent API et embeddings.
    
- Permet de construire des agents spécialisés capables d'effectuer des recherches multi-étapes.
    
- Contrôle fin des paramètres : domaines, récence, langue, modèles, tokens, etc.
    
- Support des traitements asynchrones pour les recherches longues.
    
- Inclut des outils d'exploitation intéressants comme `estimate_cost`, `list_models` et `health_check`.
    
- Architecture TypeScript relativement claire et séparation des responsabilités dans le code.
    
- Licence MIT.
    

### Limites

- **Projet communautaire peu mature** : très faible adoption GitHub au moment de l'analyse.
    
- Ne bénéficie pas du même niveau de confiance que le MCP officiel maintenu par Perplexity.
    
- Expose beaucoup d'outils : cette richesse peut augmenter la complexité et le coût de décision pour un agent.
    
- Les outils de gestion des clés (`generate`, `revoke`, `rotate`) sont particulièrement sensibles et ne devraient pas être exposés à un agent généraliste.
    
- Le projet reproduit en partie des fonctionnalités désormais disponibles dans le MCP officiel de Perplexity.
    
- L'intérêt d'une exposition aussi complète doit être évalué par rapport au principe de **moindre privilège** : un agent de recherche n'a généralement besoin que de Search/Research/Reason.
    
- Le projet est davantage un **wrapper/control plane d'API** qu'une véritable couche d'abstraction métier.
    

## Relations

- **Alternative à :** le serveur MCP officiel de Perplexity (`perplexityai/modelcontextprotocol`) pour les besoins nécessitant un contrôle API complet ; fonctionne avec une clé d'API Perplexity (facturation à l'usage), et non en pilotant une session web
    
- **S'intègre avec :** Claude Code · Claude Desktop · Cursor · Comet · tout client MCP compatible
    
- **Utilise :** [[Perplexity API]] · [[Model Context Protocol]]
    

### Positionnement par rapport au MCP officiel

Le serveur officiel `perplexityai/modelcontextprotocol` privilégie une interface plus réduite avec les outils `perplexity_search`, `perplexity_ask`, `perplexity_research` et `perplexity_reason`. Il est directement maintenu par Perplexity et existe également sous forme de serveur MCP distant hébergé par Perplexity.

`perplexity-control-mcp` est donc surtout pertinent lorsque l'objectif est d'accéder à des fonctions qui dépassent cette abstraction : Agent API, recherche brute, jobs asynchrones, embeddings, catalogue des modèles ou gestion des clés.

Pour une architecture d'agents, le projet peut être considéré comme une **couche d'infrastructure avancée**, plutôt que comme le MCP Perplexity par défaut.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le principal attrait est de piloter l'ensemble de la surface API de Perplexity (Search, Sonar, Deep Research asynchrone, Agent API, embeddings, estimation des coûts) depuis Claude Code, Cursor ou Codex, avec des réponses sourcées dans le même workflow que le reste du travail. Le serveur fonctionne avec une **clé d'API Perplexity** (facturation à l'usage) : il n'exploite pas un abonnement Pro et ne pilote pas la session web.

Le recul indépendant sur ce serveur précis est faible (dépôt communautaire quasiment sans étoiles). Le mot « control » renvoie à des outils d'administration sensibles — génération, révocation et rotation de clés d'API — qui ne devraient pas être exposés à un agent généraliste : appliquer le principe de moindre privilège, n'activer que les outils de recherche nécessaires et protéger la clé. La fragilité propre aux projets qui automatisent une interface web (dépendance au DOM, à une session connectée, aux conditions du service) concerne d'autres projets, comme celui évoqué dans la discussion Reddit citée ci-dessous, et non ce serveur.

### Comparaison

Le serveur MCP officiel de Perplexity est plus simple et directement maintenu par l'éditeur ; il suffit à la plupart des usages de recherche. L'API Sonar utilisée en direct est plus robuste et contractuelle. Les MCP de recherche comme Tavily ou Exa sont conçus pour l'intégration. Firecrawl extrait des pages plutôt qu'il ne produit une synthèse. Control MCP n'est pertinent que lorsqu'il faut des fonctions au-delà de l'abstraction du serveur officiel (jobs asynchrones, embeddings, catalogue de modèles, gestion des clés).

### Verdict

Couche d'infrastructure avancée utile pour un usage expérimental ou ciblé ; pour un usage courant, préférer le serveur MCP officiel, et ne pas exposer les outils de gestion de clés sans contrôle de sécurité.

## Sources

- [GitHub — perplexity-control-mcp](https://github.com/itsablabla/perplexity-control-mcp)
    
- [GitHub — Perplexity official MCP Server](https://github.com/perplexityai/modelcontextprotocol)
    
- [Perplexity](https://www.perplexity.ai/)
    

### Sources des avis

- [Dépôt du projet](https://github.com/itsablabla/perplexity-control-mcp)
- [Discussion d’un autre projet, qui exploite une session Perplexity Pro (distinct de ce serveur)](https://www.reddit.com/r/perplexity_ai/comments/1rz9y8q/i_built_a_cli_mcp_server_so_your_perplexity_pro/)
- [Comparaison des outils Deep Research](https://hundredtabs.com/blog/deep-research-comparison-2026)

_Dernière analyse : 12 novembre 2026_