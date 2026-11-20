---
title: "Xcode MCP — Mémo"
type: memo
fiche: "[[Xcode MCP]]"
date: 2026-11-20
---

# Xcode MCP — Mémo

> Autoriser un agent externe à utiliser le projet ouvert dans Xcode. Voir la fiche [[Xcode MCP]] et les [[Xcode MCP#Avis indépendants|avis indépendants]].

## Installation

Dans Xcode 26.3 ou ultérieur, ouvrir **Settings → Intelligence → Model Context Protocol**, puis choisir **While Xcode is Open** ou **Always** pour l’accès des agents externes. Ouvrir ensuite le projet dans Xcode.

## Commandes principales

|Commande|Rôle|
|---|---|
|`claude mcp list`|Vérifier l’enregistrement dans Claude Code.|
|`codex mcp list`|Vérifier l’enregistrement dans Codex.|

## Configuration et usage

Apple documente les commandes suivantes. Choisir celle du client utilisé.

```bash
# Claude Code
claude mcp add --transport stdio xcode -- \
  xcrun mcpbridge

# Codex
codex mcp add xcode -- xcrun mcpbridge
```

## Conseils d'utilisation

Si plusieurs projets sont ouverts, préciser celui sur lequel l’agent doit agir. Le réglage **Never** retire l’accès des agents externes.

## Sources

- [Configuration officielle du pont](https://developer.apple.com/documentation/xcode/giving-external-agents-access-to-xcode)
