---
title: "MobileBuildMCP — Mémo"
type: memo
fiche: "[[MobileBuildMCP]]"
date: 2026-11-20
---

# MobileBuildMCP — Mémo

> Relier un agent à MobileBuildMCP et retrouver les outils essentiels du simulateur. Voir la fiche [[MobileBuildMCP]] et les [[MobileBuildMCP#Avis indépendants|avis indépendants]].

## Installation

Avec npm, lancer le serveur à la demande via `npx -y mobilebuildmcp@latest mcp`. Pour Claude Code, la configuration officielle est la suivante.

```bash
claude mcp add MobileBuildMCP -- \
  npx -y mobilebuildmcp@latest mcp
```

## Commandes principales

|Commande|Rôle|
|---|---|
|`mobilebuildmcp doctor`|Diagnostiquer l’installation et les dépendances.|
|`mobilebuildmcp setup`|Choisir les workflows et les réglages du projet.|
|`discover_projs` puis `list_schemes`|Repérer le projet et ses schémas via MCP.|
|`session_set_defaults`|Mémoriser le projet, le schéma et le simulateur.|
|`build_run_sim`|Compiler, installer et lancer sur simulateur.|
|`test_sim`|Exécuter les tests sur simulateur.|

## Configuration et usage

Le workflow `simulator` est activé par défaut. Ajouter `ui-automation` pour interagir avec les vues et faire des captures. Le projet MyAlbumEasy-iOS utilise `xcodebuildmcp@2.7.0`, avec l’ancien nom du paquet.

## Conseils d'utilisation

Préciser le schéma et la destination avant le premier essai. Vérifier le rapport de test et les logs à la fin du parcours.

## Sources

- [Configuration des clients](https://www.mobilebuildmcp.com/docs/clients)
- [Référence des outils](https://www.mobilebuildmcp.com/docs/tools)
- [Configuration du projet](https://www.mobilebuildmcp.com/docs/setup)
