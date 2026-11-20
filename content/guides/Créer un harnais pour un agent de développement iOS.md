---
title: "Créer un harnais pour un agent de développement iOS"
type: guide
description: "Configurer Claude Code pour un projet Swift, vérifier les builds et les tests sur simulateur, puis valider l’app sur un iPhone avec GStack."
date: 2026-11-20
tags:
  - metier/ingenierie
  - theme/mcp
  - theme/tests
  - theme/revue-de-code
---

# Créer un harnais pour un agent de développement iOS

Un [[Harnais d'agent|harnais]] réunit l’agent, les règles du dépôt et les outils qui lui permettent de vérifier son travail. Ce guide part de la configuration de MyAlbumEasy-iOS pour monter un harnais avec [[Claude Code]]. Le premier objectif est de compiler et de tester l’app sur simulateur. La QA sur iPhone physique vient ensuite.

## 1. Vérifier l’environnement Xcode

Prévoir un Mac avec Xcode, un simulateur iOS installé, Claude Code et Node.js si le serveur MCP de build est lancé avec `npx`. Ouvrir le projet dans Xcode une première fois et vérifier qu’un schéma partagé permet de compiler l’app et d’exécuter ses tests.

Depuis la racine du dépôt, identifier les schémas et les destinations. L’exemple utilise les noms de MyAlbumEasy-iOS. Pour un autre projet, adapter le workspace et le schéma, ou utiliser `-project Nom.xcodeproj` pour un projet sans workspace.

```bash
xcodebuild -version
xcodebuild -list -workspace MyAlbumEasy.xcworkspace
xcodebuild -showdestinations -workspace MyAlbumEasy.xcworkspace -scheme MyAlbumEasy
```

## 2. Donner à l’agent les règles du dépôt

Créer un `CLAUDE.md` à la racine avec les chemins utiles, les contraintes Swift et iOS, les règles d’architecture et les commandes de validation. Indiquer le workspace, le schéma et la destination à utiliser. Si l’équipe maintient ailleurs ses décisions produit et design, pointer vers leur source de référence. MyAlbumEasy-iOS utilise le sous-module `Product-Design-Source` à cette fin.

Pour que l’agent et l’intégration continue exécutent les mêmes contrôles, consigner les commandes de l’équipe dans ce fichier. MyAlbumEasy-iOS, par exemple, compile l’app et ses labos pour le simulateur avec `Tools/build-apps.sh` et lance les tests de ses paquets avec `swift test --package-path Packages/AlbumVisionSDK` et `swift test --package-path Packages/AlbumKit`. Pour les tests d’une app ou d’un parcours UI, indiquer le schéma qui contient les cibles de test et une destination de simulateur concrète.

## 3. Installer les plugins et les skills Swift

Depuis la racine du dépôt, enregistrer les catalogues sur la machine s’ils sont absents, puis installer les plugins avec la portée projet. Cette portée inscrit leur activation dans `.claude/settings.json`. Chaque personne exécute l’installation dans son clone pour télécharger les plugins. [Documentation Claude Code sur les plugins](https://code.claude.com/docs/en/discover-plugins)

```bash
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin marketplace add OthmanAdi/planning-with-files
claude plugin install superpowers@claude-plugins-official --scope project
claude plugin install planning-with-files@planning-with-files --scope project
```

Utiliser [[Superpowers]] pour cadrer la tâche, définir les tests et relire le changement. Sur une tâche qui s’étend sur plusieurs sessions, utiliser [[Planning with Files]] pour conserver le même plan, les décisions et l’avancement dans le dépôt. Tâche et plan restent liés même si la session est interrompue.

Installer les trois [[Skill|skills]] ci-dessous dans `.claude/skills/<nom>/SKILL.md`. Pour chacune, copier le dossier de la skill depuis une révision choisie, avec ses fichiers de référence et sa licence. Consigner le dépôt source et le commit dans `.claude/skills/SOURCES.md`. Un nouveau clone reçoit ainsi la même version. [Documentation Claude Code sur les skills](https://code.claude.com/docs/en/skills)

| Skill                             | Dossier             | Quand l’utiliser                                                                      |
| --------------------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| [[SwiftUI Pro]]                   | `swiftui-pro`       | Relire une vue, sa navigation, son accessibilité ou ses performances.                 |
| [[Swift Concurrency Agent Skill]] | `swift-concurrency` | Modifier du code qui concerne `async/await`, les acteurs, `@MainActor` ou `Sendable`. |
| [[Swift Testing Pro]]             | `swift-testing-pro` | Écrire ou relire des tests avec Swift Testing.                                        |

## 4. Brancher les serveurs MCP

Un serveur [[Model Context Protocol|MCP]] donne à l’agent des outils pour agir. Utiliser [[MobileBuildMCP]] pour compiler, tester et piloter le simulateur. Activer aussi le [[Xcode MCP|MCP natif d’Apple]] si l’agent doit travailler avec le projet ouvert dans Xcode. Les deux offrent des opérations de build. Indiquer dans `CLAUDE.md` lequel utiliser par défaut pour que l’équipe puisse reproduire les validations.

Ajouter les serveurs voulus à la clé `mcpServers` dans le fichier `.mcp.json` à la racine. L’exemple utilise une version fixe du paquet actuel `mobilebuildmcp`. MyAlbumEasy-iOS déclare encore le même projet sous son ancien nom, `XcodeBuildMCP`, avec `xcodebuildmcp@2.7.0`. [Dépôt MobileBuildMCP](https://github.com/getsentry/MobileBuildMCP) · [Documentation Apple](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode)

```json
{
  "mcpServers": {
    "mobilebuildmcp": {
      "command": "npx",
      "args": ["-y", "mobilebuildmcp@2.7.1", "mcp"]
    },
    "xcode": {
      "command": "xcrun",
      "args": ["mcpbridge"]
    }
  }
}
```

Si le terminal sélectionne les seuls outils de ligne de commande ou une autre version de Xcode, définir `DEVELOPER_DIR` vers l’installation voulue. MyAlbumEasy-iOS utilise `/Applications/Xcode.app/Contents/Developer` dans `.claude/settings.json` et dans l’environnement de ses serveurs MCP.

Pour le serveur Apple, autoriser les agents externes dans les réglages **Intelligence** de Xcode et ouvrir le workspace dans l’IDE. Dans Claude Code, approuver les serveurs du projet à la première demande, puis ouvrir `/mcp` pour vérifier l’état de connexion. Pour une première vérification, demander à l’agent de lister les schémas puis de compiler l’app sur le simulateur retenu. Un serveur joignable et un build réussi sont deux vérifications distinctes. [Documentation Claude Code sur les serveurs MCP](https://code.claude.com/docs/en/mcp)

## 5. Ajouter la QA sur iPhone avec GStack

Installer [[GStack]] sur le poste qui pilote l’iPhone et repérer les noms des skills dans Claude Code. Préparer un iPhone appairé et approuvé, connecté en USB, ainsi qu’une cible Debug signée que Xcode sait lancer sur l’appareil. Le flux de GStack utilise le code SwiftUI de l’app et s’appuie sur un état observable. [Installation de GStack](https://github.com/garrytan/gstack/blob/main/docs/install.md) · [Prérequis de la skill iOS QA](https://github.com/garrytan/gstack/tree/main/ios-qa)

| Skill               | Quand l’utiliser                                   | Résultat attendu                                                                     |
| ------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------ |
| `ios-qa`            | Tester un parcours réel sur l’iPhone.              | Étapes du parcours, résultat observé et captures utiles pour reproduire un problème. |
| `ios-design-review` | Vérifier le rendu d’un écran sur l’appareil.       | Observations sur la lisibilité, la hiérarchie et le respect des conventions iOS.     |
| `ios-fix`           | Corriger un bug reproductible relevé par `ios-qa`. | Correctif, nouveau build et reprise du parcours sur le même appareil.                |

Pour démarrer, choisir un parcours court et des données de test. Le premier passage de `ios-qa` peut nécessiter l’intégration de `DebugBridge`, le pont qui permet à GStack d’observer et de piloter l’app. Préparer cette intégration séparément du correctif à tester, lier le pont uniquement en Debug, isoler son démarrage avec `#if DEBUG` et vérifier que la cible Release compile sans le pont. L’installation des skills sur le Mac et l’instrumentation de l’app sont deux étapes distinctes. [Documentation GStack sur le retrait du pont Debug](https://github.com/garrytan/gstack/tree/main/ios-clean)

## 6. Valider le harnais sur une tâche de bout en bout

Choisir un changement réduit, par exemple l’affichage d’un état vide dans une vue SwiftUI. Donner à l’agent le comportement attendu, le schéma et le simulateur. Lui demander de suivre les règles du dépôt, d’utiliser les skills Swift pertinentes, puis de rendre compte des vérifications avec leurs résultats.

1. Compiler la cible et lancer les tests du changement. Relever le schéma, la destination et le résultat.
2. Lancer l’app sur simulateur et vérifier que la vue affiche bien l’état attendu. Garder une capture si le changement est visuel.
3. Si l’usage sur appareil fait partie du besoin, rejouer le parcours avec `ios-qa`. Utiliser `ios-design-review` pour une revue visuelle ou `ios-fix` pour traiter un bug reproduit, puis vérifier le résultat sur l’iPhone.

### Dépannage

| Symptôme                                      | Vérification                                                                                                                                                              |
| --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Le schéma ou le simulateur est introuvable.   | Vérifier le workspace, le partage du schéma et les destinations retournées par `xcodebuild -showdestinations`.                                                            |
| Le serveur Apple reste déconnecté.            | Vérifier le projet ouvert dans Xcode, l’autorisation dans **Intelligence** et le résultat de `xcrun --find mcpbridge`.                                                    |
| MobileBuildMCP se déconnecte au démarrage.    | Vérifier que `npx` est accessible depuis le processus de l’agent et que le nom et la version du paquet correspondent à la configuration. Consulter le détail dans `/mcp`. |
| L’iPhone est absent ou l’app ne se lance pas. | Vérifier le câble, l’appairage et la signature, puis lancer la cible Debug depuis Xcode avant de relancer `ios-qa`.                                                       |

Pour relier ce dépôt iOS aux autres dépôts du produit, voir le guide [[Architecture multi-repos et harnais Claude Code]].
