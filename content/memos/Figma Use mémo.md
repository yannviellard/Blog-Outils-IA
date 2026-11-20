---
title: "Figma Use — Mémo"
type: memo
fiche: "[[Figma Use]]"
date: 2026-11-20
---

# Figma Use — Mémo

> Charger le skill puis inspecter ou modifier les objets du bon fichier. Voir la fiche [[Figma Use]] et les [[Figma Use#Avis indépendants|avis indépendants]].

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
|`/figma-use`|Demander explicitement le workflow dans Claude Code.|
|`use_figma`|Exécuter une lecture avancée ou une modification.|
|`get_screenshot`|Contrôler le rendu des changements.|

## Utilisation

Fournir le lien du fichier et cibler une page ou un nœud. Inclure `figma-use` dans `skillNames`, avec le préfixe `resource:` si le skill provient d’une ressource MCP. Pour une opération de bibliothèque, charger aussi [[Figma Generate Library]].

## Conseils d'utilisation

Conserver les identifiants renvoyés. Si l’outil indique qu’une écriture a pu s’appliquer partiellement, relire l’état avant de relancer.

## Sources

- [Définition et règles d’usage](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use/SKILL.md)
- [Démarrage avec Figma MCP](https://help.figma.com/hc/en-us/articles/39216419318551-Get-started-with-the-Figma-MCP-server)
