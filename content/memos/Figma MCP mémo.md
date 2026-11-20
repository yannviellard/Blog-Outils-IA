---
title: "Figma MCP — Mémo"
type: memo
fiche: "[[Figma MCP]]"
date: 2026-11-20
---

# Figma MCP — Mémo

> Configurer le serveur distant, autoriser le compte Figma et cibler une maquette. Voir la fiche [[Figma MCP]] et les [[Figma MCP#Avis indépendants|avis indépendants]].

## Installation

Pour une connexion seule, utiliser la commande du client choisi, puis autoriser l’accès dans le navigateur.

**Claude Code**

```bash
claude mcp add --transport http figma \
  https://mcp.figma.com/mcp
```

**Codex CLI**

```bash
codex mcp add figma \
  --url https://mcp.figma.com/mcp
```

## Commandes principales

|Commande ou outil|Rôle|
|---|---|
|`get_design_context`|Lire le contexte du nœud.|
|`get_screenshot`|Voir la maquette ou le composant.|
|`get_variable_defs`|Lire les variables utilisées par le nœud.|
|`use_figma`|Exécuter la Plugin API sur un client compatible.|

## Utilisation

Copier le lien d’un composant ou d’un frame. Pour une modification sur le canvas, charger les skills Figma et vérifier les droits du compte sur le fichier.

## Conseils d'utilisation

Vérifier le fichier ciblé avant d’écrire et utiliser un brouillon pour la première passe. Pour le code, comparer le rendu avec la capture de la maquette.

## Sources

- [Installer le serveur distant](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)
- [Outils et exemples](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
