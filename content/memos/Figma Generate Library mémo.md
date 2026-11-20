---
title: "Figma Generate Library — Mémo"
type: memo
fiche: "[[Figma Generate Library]]"
date: 2026-11-20
---

# Figma Generate Library — Mémo

> Limiter le périmètre, construire les fondations puis contrôler les composants. Voir la fiche [[Figma Generate Library]] et les [[Figma Generate Library#Avis indépendants|avis indépendants]].

## Installation

Installer le plugin officiel dans Claude Code. Il inclut les skills et la configuration du serveur distant.

```bash
claude plugin install \
  figma@claude-plugins-official
```

Pour les autres clients, suivre la procédure Figma d’installation des skills.

## Commandes principales

|Commande ou outil|Rôle|
|---|---|
|`/figma-generate-library`|Lancer le skill manuellement dans le projet examiné.|
|`get_libraries`|Lister les bibliothèques accessibles.|
|`search_design_system`|Identifier les ressources réutilisables.|
|`use_figma`|Construire ou ajuster les éléments Figma avec [[Figma Use]].|

## Utilisation

Préciser le fichier cible, les chemins du code et le périmètre. Pour une mise à jour, inspecter d’abord les écarts. Réutiliser les variables et styles existants, puis ajouter les éléments manquants.

## Conseils d'utilisation

Contrôler les modes, alias, propriétés, variantes et liaisons. Vérifier aussi un jeu représentatif d’instances sur le canvas.

## Sources

- [Définition et étapes officielles](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-library/SKILL.md)
- [Skills Figma](https://help.figma.com/hc/en-us/articles/39166810751895-Figma-skills-for-MCP)
