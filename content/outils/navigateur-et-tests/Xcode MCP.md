---
title: "Xcode MCP"
type: outil
description: "Relie un agent externe au projet ouvert et aux outils intégrés de Xcode."
format: serveur-mcp
tags:
  - metier/ingenierie
  - theme/mcp
  - theme/tests
editeur: "Apple"
logo: "[[xcode-mcp.png]]"
site: "https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode"
statut: disponible
note_documentation: 4
note_precision: 4
note_maturite: 3
memo: "[[Xcode MCP mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# Xcode MCP

> Apple fournit un serveur MCP avec Xcode. Le pont `xcrun mcpbridge` relie un agent externe aux outils de l’IDE et au projet ouvert.

**Composition** : Un pont local et des outils fournis par Xcode, dont la liste évolue avec la version de l’IDE.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[Xcode MCP mémo|mémo pratique]].

## Résumé

L’intégration a été introduite avec Xcode 26.3. Apple demande d’autoriser l’accès dans les réglages Intelligence, de configurer le client [[Model Context Protocol|MCP]], puis d’ouvrir le projet dans Xcode. L’IDE signale l’activité de l’agent.

## Fonctionnalités

- Compiler et tester le projet depuis un agent externe.
- Rendre des aperçus SwiftUI et consulter la documentation Apple.
- Avec Xcode 27, consulter ou modifier des réglages de compilation et interagir avec le débogueur selon les outils disponibles.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|—|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Aucun dépôt public consacré au pont Apple._

### Points forts

Le pont donne accès au contexte de l’IDE, notamment aux aperçus et aux diagnostics du projet ouvert.

### Limites

Le parcours `mcpbridge` décrit par Apple demande un projet ouvert et des permissions dans Xcode. Les notes de Xcode 27 mentionnent séparément une préversion de serveur sans workspace ouvert.

### Qualité

Instructions officielles claires et intégration confirmée dans des essais. La liste des outils dépend de la version de Xcode et le recul depuis la version 26.3 reste inférieur à un an.

## Relations

- **Alternative partielle à** [[MobileBuildMCP]] pour la compilation et les tests. Ce dernier peut aussi relayer des fonctions du pont Apple via `xcode-ide`.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

Dans le comparatif macbox, le pont est présenté comme un complément pour les opérations liées au projet et aux aperçus. Des développeurs sur iOSProgramming distinguent également ce contexte du pilotage du simulateur.

### Ce qui est critiqué

Des développeurs signalent des demandes d’autorisation répétées dans certaines configurations de Xcode 26.3 et des réponses plus verbeuses que celles de XcodeBuildMCP. Ces retours datent de cette génération du pont.

### Ce qui n'est pas établi

Les retours consultés ne mesurent ni la fiabilité selon la version de Xcode et le client MCP ni le coût en jetons de parcours équivalents.

### Comparaison

[[MobileBuildMCP]] couvre le cycle de vie du simulateur et les scripts avec sa CLI. Le pont Apple donne accès aux outils du projet ouvert pour travailler dans le contexte de l’IDE.

### Verdict

Adapté lorsque l’agent doit s’appuyer sur les aperçus ou sur l’état du projet dans Xcode. Vérifier la version de Xcode et les outils annoncés par le client.

## Sources

- [Documentation officielle](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode)
- [Notes de Xcode 27](https://developer.apple.com/documentation/xcode-release-notes/xcode-27-release-notes)
- [Annonce de Xcode 26.3](https://www.apple.com/newsroom/2026/02/xcode-26-point-3-unlocks-the-power-of-agentic-coding/)

### Sources des avis

- [Comparatif macbox](https://macbox.build/guides/xcode-mcp-servers/) — comparatif technique. L’auteur commercialise une solution compatible avec MobileBuildMCP.
- [Discussion sur Xcode 26.3](https://www.reddit.com/r/iOSProgramming/comments/1quzw7n/xcode_263_unlocks_the_power_of_agentic_coding/) — témoignage sur les demandes d’autorisation, lié à une ancienne version.
- [Comparaison avec XcodeBuildMCP](https://www.reddit.com/r/iOSProgramming/comments/1rhl7cf/how_does_xcode_263_s_built_in_mcp_server_compare/) — retours de développeurs, sans mesure reproductible.

_Dernière analyse : 20 novembre 2026_
