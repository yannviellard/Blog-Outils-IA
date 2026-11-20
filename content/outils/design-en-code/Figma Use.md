---
title: "Figma Use"
type: outil
description: "Guide la lecture et la modification du canvas avec la Plugin API de Figma."
format: skill
tags:
  - metier/produit-design
  - metier/ingenierie
  - theme/mcp
  - theme/design-system
  - theme/automatisation
editeur: "Figma"
logo: "[[figma.png]]"
site: "https://help.figma.com/hc/en-us/articles/39166810751895-Figma-skills-for-MCP"
depot: "https://github.com/figma/mcp-server-guide/tree/main/skills/figma-use"
statut: disponible
derniere_maj: 2026-11-12
note_documentation: 4
note_precision: 4
note_maturite: 3
memo: "[[Figma Use mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# Figma Use

> Figma Use (`figma-use`) est le skill officiel à charger avant d’appeler `use_figma`. Il guide l’exécution de JavaScript dans le contexte du fichier Figma.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[Figma Use mémo|mémo pratique]].

## Résumé

Le [[Skill|skill]] fait le lien entre les demandes de l’utilisateur et la Plugin API exposée par [[Figma MCP]]. Il couvre les opérations d’écriture et les lectures qui exigent un script, comme l’inspection détaillée de la structure d’une page.

## Fonctionnalités

- Lire les nœuds et inspecter les composants, la mise en page ou les liaisons de variables.
- Créer ou modifier les nœuds, les variantes, les variables et l’Auto Layout.
- Renvoyer les identifiants des objets touchés et relire l’état du canvas avant une reprise si l’écriture a pu s’appliquer en partie.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|—|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Le guide GitHub est partagé par plusieurs outils et skills Figma._

### Points forts

Les références précisent les contraintes de la Plugin API, comme le chargement d’une police avant de modifier un texte ou la sélection de la page au début d’un appel.

### Limites

Le skill dépend du serveur distant et d’un client qui propose `use_figma`. Pour une composition visuelle, Figma l’associe à `figma-generate-design`. Pour une bibliothèque réutilisable, Figma l’associe à [[Figma Generate Library]].

### Qualité

Références techniques détaillées et opérations sur les composants observées dans des essais du flux Figma. L’effet propre du skill n’est pas mesuré.

## Relations

- **Utilise** [[Figma MCP]] pour exécuter la Plugin API et observer le résultat.
- **Complémentaire de** [[Figma Generate Library]] pour les tokens et les composants réutilisables.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

L’essai Rango.design montre des composants et des variables natifs. Un utilisateur de Claude Code décrit avoir retrouvé et réutilisé les bonnes variantes d’une bibliothèque après en avoir indexé les composants.

### Ce qui est critiqué

Ce même témoignage décrit des approximations lorsque les composants n’étaient pas explicitement retrouvés. Le comparatif devmio montre que le contenu du prompt et la structure de la bibliothèque influent sur le résultat.

### Ce qui n'est pas établi

Les sources évaluent le flux complet. Elles ne mesurent pas la différence entre deux exécutions identiques avec et sans `figma-use`.

### Comparaison

Les outils dédiés `get_metadata` et `get_screenshot` peuvent suffire pour lire la structure ou l’apparence. `use_figma` convient à une lecture qui exige une logique JavaScript ou à une modification native.

### Verdict

À charger avant toute opération `use_figma`. Délimiter le fichier, la page et les objets concernés, puis contrôler les identifiants et le résultat visible.

## Sources

- [Définition officielle](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-use/SKILL.md)
- [Plugin API Figma](https://developers.figma.com/docs/plugins/api/)
- [Écriture sur le canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)

### Sources des avis

- [Essai Rango.design](https://rango.design/articles/figma-mcp) — essai sur un fichier brouillon avec le plugin officiel. Les mesures concernent un seul exemple.
- [Retour sur la réutilisation de variantes](https://www.reddit.com/r/UXDesign/comments/1umeqvh/how_i_got_claude_to_actually_use_my_figma_design/) — témoignage individuel avec un exemple d’import dans un autre fichier.
- [Essai de réutilisation de composants](https://devm.io/ux/design-systems-llms) — comparaison de deux consignes sur une bibliothèque donnée. Plusieurs paramètres variant à la fois, elle n’isole pas l’effet d’un skill.

_Dernière analyse : 20 novembre 2026_
