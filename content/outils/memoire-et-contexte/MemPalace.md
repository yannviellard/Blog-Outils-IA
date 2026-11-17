---
title: "MemPalace"
type: outil
description: "Mémoire locale partagée entre agents, à tester sur ses propres cas avant adoption sensible."
format: cli
tags:
  - metier/ingenierie
  - metier/support-client
  - theme/memoire
  - theme/mcp
editeur: "MemPalace"
logo: "[[mempalace.png]]"
site: "https://mempalaceofficial.com/"
depot: "https://github.com/MemPalace/mempalace"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 60572
forks: 7674
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 2
note_maturite: 2
note_popularite: 4
memo: "[[MemPalace mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# MemPalace

> Système de mémoire persistante **local-first** pour agents IA. MemPalace stocke les conversations et documents sous forme verbatim, les indexe et les rend accessibles par recherche sémantique, MCP et intégrations avec Claude Code et d'autres agents.

**Composition** : 19+ outils MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[MemPalace mémo]] pour le mémo pratique.

## Résumé

MemPalace transforme l'historique des conversations, les fichiers de projets et les connaissances structurées en une mémoire persistante exploitable par les agents.

Son architecture repose sur une métaphore de **memory palace** : Palace → Wing → Hall → Room → Closet → Drawer. Les contenus originaux sont conservés verbatim plutôt que résumés, puis retrouvés par recherche sémantique et, selon les versions/configurations, par recherche hybride et graphe de connaissances.

Pour Claude Code, MemPalace peut utiliser **MCP + hooks** afin de sauvegarder automatiquement les sessions, récupérer du contexte lors d'une nouvelle session et conserver les dernières interactions avant une compression du contexte.

Le projet est **local-first** : les données et embeddings peuvent rester sur la machine. Il propose également désormais un mode serveur partagé pour plusieurs agents ou utilisateurs.

## Fonctionnalités

- **Mémoire persistante** entre les sessions Claude Code.
    
- **Stockage verbatim** des conversations et documents, sans résumé obligatoire.
    
- **Recherche sémantique** et recherche hybride pour retrouver des informations anciennes.
    
- **MCP Server** permettant aux agents compatibles d'interroger et d'écrire dans la mémoire.
    
- **Hooks Claude Code** pour automatiser la sauvegarde et la récupération du contexte.
    
- Organisation hiérarchique des connaissances : Palace → Wing → Hall → Room → Closet → Drawer.
    
- **Knowledge Graph** pour représenter certaines relations et faits.
    
- Import de conversations provenant de plusieurs agents et outils.
    
- Backends de stockage et d'embedding configurables.
    
- Possibilité de déployer un **serveur mémoire partagé** pour plusieurs agents.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★☆☆☆|
|Intégration Claude Code|★★★★☆|
|Fonctionnalités|★★★★★|
|Confidentialité / local-first|★★★★★|
|Maturité|★★☆☆☆|
|Popularité|★★★★☆|
|Simplicité d'installation|★★★☆☆|
|Fiabilité opérationnelle|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 60 572 au 16 novembre 2026._

**Commentaire :** MemPalace est devenu un projet techniquement ambitieux et très actif, avec une intégration de plus en plus poussée des agents et de Claude Code. La documentation et les mécanismes d'installation se sont nettement améliorés, mais l'historique du projet montre encore de nombreux problèmes liés aux hooks, aux versions, aux environnements Python et à la concurrence d'accès à la base. Les releases récentes corrigent une partie importante de ces problèmes, mais plusieurs issues de fiabilité restent ouvertes.

### Points forts

- **Mémoire réellement persistante** : permet à un agent de retrouver des décisions et informations issues de sessions précédentes.
    
- **Local-first** : les données peuvent rester entièrement sur la machine, sans dépendance à une API de mémoire externe.
    
- **Conservation verbatim** : réduit le risque de perdre une information lors d'une chaîne de résumés successifs.
    
- **Très bonne intégration avec MCP** et désormais avec plusieurs environnements d'agents.
    
- Architecture suffisamment riche pour gérer simultanément plusieurs projets, agents et sources.
    
- Développement très actif : les versions récentes ont ajouté daemon local, serveur HTTP, nouveaux backends, parsers et mécanismes de récupération après incident.
    
- Projet open source sous **MIT**, donc facilement inspectable et adaptable.
    

### Limites

- **Complexité élevée** par rapport à une simple mémoire basée sur `CLAUDE.md`, fichiers de contexte ou une base vectorielle minimale.
    
- L'intégration Claude Code a connu plusieurs problèmes de compatibilité : hooks, versions PyPI/plugin désynchronisées, résolution de `python3`, environnements virtuels et installation multiplateforme. Une partie a été corrigée dans les versions suivantes.
    
- Le système peut générer du **bruit mémoire** : conserver beaucoup de contenu verbatim ne garantit pas que le contexte récupéré sera toujours pertinent.
    
- La fiabilité de la couche de stockage reste un point de vigilance pour les installations importantes ou fortement concurrentes ; des problèmes de corruption/concurrence SQLite/Chroma ont notamment été rapportés.
    
- **Projet encore en évolution rapide** : architecture, backends et mécanismes de mémoire changent régulièrement.
    
- Certaines affirmations de performance publiées autour du projet doivent être interprétées avec prudence : les benchmarks mesurent principalement la qualité de retrieval dans des conditions données, et ne constituent pas une preuve générale que MemPalace améliore systématiquement les performances d'un agent. Une grande partie des benchmarks et comparatifs provient de l'écosystème du produit, et des analyses indépendantes (dont une analyse critique de l'architecture sur arXiv) questionnent l'écart entre marketing, code et généralisation réelle.
    
- **La métaphore du « palais » est jugée superflue par certains utilisateurs** par rapport à de simples fichiers ou à une recherche hybride ; elle ajoute des niveaux d'organisation (Wing, Hall, Room, Closet, Drawer) à maintenir.
    
- **Risques classiques d'une mémoire partagée** : mémoire périmée, fuite entre projets ou entre agents (surtout avec le serveur partagé), injection de données et bruit de récupération ; le stockage doit être audité avant tout usage sensible.
    

## Relations

- **Alternative à :** [[Claude-Mem]], autres systèmes de mémoire persistante pour agents
    
- **S'intègre avec :** [[Claude Code]], [[Cursor]], [[OpenAI Codex]], Gemini CLI et autres clients MCP
    
- **Utilise :** MCP · SQLite · ChromaDB · embeddings · Knowledge Graph
    
- **Architecture associée :** recherche sémantique · recherche hybride · mémoire persistante · hooks agents
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

MemPalace attire par son architecture locale, sa métaphore structurée et des scores de récupération revendiqués très élevés. Les utilisateurs apprécient le contrôle des données, l’intégration MCP et la possibilité de partager une mémoire entre plusieurs agents sans service hébergé.

Le projet suscite aussi un scepticisme marqué. Une grande partie des benchmarks et comparatifs vient de l’écosystème du produit, tandis que des analyses indépendantes questionnent l’écart entre marketing, code et généralisation réelle. Certains utilisateurs voient la structure « palais » comme une complexité inutile par rapport à des fichiers ou à une recherche hybride. Les enjeux classiques demeurent : mémoire périmée, fuite entre projets, injection de données et bruit de récupération.

### Comparaison

Mem0 est plus établi comme couche de mémoire générique et hébergée ; Claude-Mem capture automatiquement les sessions Claude Code ; la mémoire native et les fichiers Markdown sont plus simples à inspecter. MemPalace convient surtout à qui veut local-first, multi-agent et contrôle fin.

### Verdict

Projet innovant qui mérite un pilote, mais les chiffres spectaculaires ne suffisent pas. Tester sur ses propres questions, mesurer les faux rappels et auditer le stockage avant usage sensible.

## Sources

- [GitHub](https://github.com/MemPalace/mempalace)
    
- [Documentation](https://mempalaceofficial.com/)
    
- [Releases / Changelog](https://github.com/MemPalace/mempalace/releases)
    
- [Remote / Team Server](https://github.com/MemPalace/mempalace/blob/develop/website/guide/remote-server.md)
    
- [GitHub Issues](https://github.com/MemPalace/mempalace/issues)
    

### Sources des avis

- [Analyse critique de l’architecture](https://arxiv.org/abs/2604.21284)
- [Alternatives et réserves indépendantes](https://vectorize.io/articles/mempalace-alternatives)
- [Discussion d’utilisateurs](https://www.reddit.com/r/ClaudeCode/comments/1sm7n9x/thoughts_on_mempalace/)

_Dernière analyse : 12 novembre 2026_