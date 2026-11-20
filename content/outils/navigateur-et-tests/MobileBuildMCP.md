---
title: "MobileBuildMCP"
type: outil
description: "Compile et teste les projets Xcode et pilote le simulateur iOS depuis un agent."
format: serveur-mcp
tags:
  - metier/ingenierie
  - theme/mcp
  - theme/tests
  - theme/automatisation
editeur: "Sentry"
logo: "[[mobilebuildmcp.png]]"
site: "https://www.mobilebuildmcp.com/docs"
depot: "https://github.com/getsentry/MobileBuildMCP"
licence: "MIT"
statut: disponible
derniere_maj: 2026-10-22
etoiles: 6595
forks: 329
etoiles_releve: 2026-11-20
note_documentation: 5
note_precision: 4
note_maturite: 4
note_popularite: 3
memo: "[[MobileBuildMCP mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# MobileBuildMCP

> MobileBuildMCP, anciennement XcodeBuildMCP, est un serveur MCP et une CLI pour compiler, tester, lancer et déboguer les applications pour les plateformes Apple depuis un Mac.

**Composition** : Jusqu’à 82 outils répartis en 15 workflows dans la version 2.7.1, selon la documentation officielle. Le workflow du simulateur est activé par défaut.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[MobileBuildMCP mémo|mémo pratique]].

## Résumé

Le serveur expose les opérations de développement Apple via le [[Model Context Protocol|MCP]]. Une même configuration peut mémoriser le projet ou workspace, le schéma et le simulateur. Le dépôt de MyAlbumEasy-iOS épingle encore le paquet npm `xcodebuildmcp@2.7.0`. La documentation de la version 2.7.1 utilise le nouveau nom de paquet `mobilebuildmcp`.

## Fonctionnalités

- Découverte des projets et des schémas, compilation, tests et lecture des résultats.
- Démarrage du simulateur, installation et lancement de l’application, collecte des logs.
- Interaction avec l’interface et captures via `ui-automation`, débogage LLDB via `debugging`.
- Accès à certaines fonctions de l’IDE via `xcode-ide` et le pont d’Apple.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★★|
|Précision des descriptions|★★★★☆|
|Maturité|★★★★☆|
|Popularité|★★★☆☆|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Popularité calculée à partir de 6 595 étoiles relevées via l’API GitHub le 20 novembre 2026._

### Points forts

La référence sépare les noms des outils MCP de ceux des sous-commandes CLI. La compilation et le pilotage du simulateur fonctionnent sans ouvrir l’IDE.

### Limites

Les outils exigent un Mac avec Xcode et les runtimes nécessaires. Le workflow `xcode-ide` dépend du pont natif d’Apple. Vérifier les workflows actifs avant de demander une capture ou un geste.

### Qualité

Référence détaillée des commandes et prérequis, opérations principales observées par des tiers et dépôt public ouvert depuis mars 2025.

## Relations

- **Alternative partielle à** [[Xcode MCP]] pour compiler et tester. Le workflow `xcode-ide` peut aussi lui déléguer les fonctions propres à l’IDE.
- **Complémentaire de** [[SwiftUI Pro]] pour examiner les vues en situation et de [[Swift Testing Pro]] pour exécuter la suite.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

Un essai publié par macbox décrit un build et un lancement sur simulateur via un Mac distant. Un développeur sur Reddit rapporte utiliser le serveur pour démarrer le simulateur et examiner une capture.

### Ce qui est critiqué

Un utilisateur signale qu’un tap référencé peut être indiqué comme réussi alors que le bouton de l’alerte reste affiché. Le ticket documente un cas ouvert.

### Ce qui n'est pas établi

Les retours consultés n’établissent pas le taux de succès des parcours simulés ni le gain de temps sur plusieurs projets.

### Comparaison

[[Xcode MCP]] accède au projet ouvert et aux fonctions de l’IDE. `xcodebuild` et `simctl` restent des options directes si un script connaît déjà son projet et sa destination.

### Verdict

Pertinent pour donner à un agent une boucle de compilation, de tests et d’observation sur simulateur. Pour une vérification répétable, consigner aussi la destination et le résultat attendu.

## Sources

- [Dépôt officiel](https://github.com/getsentry/MobileBuildMCP)
- [Documentation officielle](https://www.mobilebuildmcp.com/docs)
- [Référence des outils](https://www.mobilebuildmcp.com/docs/tools)
- [Version 2.7.1](https://github.com/getsentry/MobileBuildMCP/releases/tag/v2.7.1)

### Sources des avis

- [Comparatif et essai de macbox](https://macbox.build/guides/xcode-mcp-servers/) — essai direct. L’auteur commercialise un hébergement Mac compatible.
- [Discussion iOSProgramming](https://www.reddit.com/r/iOSProgramming/comments/1wius7u/xcode_mcp_va_xcodebuildmcp/) — retour d’usage individuel sur les captures et le simulateur.
- [Ticket sur le tap d’alerte](https://github.com/getsentry/MobileBuildMCP/issues/573) — signalement d’un utilisateur dans le dépôt du projet.

_Dernière analyse : 20 novembre 2026_
