---
title: "Figma Generate Library"
type: outil
description: "Construit ou met à jour dans Figma les tokens, composants et variantes issus d’une base de code."
format: skill
tags:
  - metier/produit-design
  - metier/ingenierie
  - theme/mcp
  - theme/design-system
  - theme/frontend
editeur: "Figma"
logo: "[[figma.png]]"
site: "https://help.figma.com/hc/en-us/articles/39166810751895-Figma-skills-for-MCP"
depot: "https://github.com/figma/mcp-server-guide/tree/main/skills/figma-generate-library"
statut: disponible
derniere_maj: 2026-10-28
note_documentation: 4
note_precision: 3
note_maturite: 3
memo: "[[Figma Generate Library mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# Figma Generate Library

> Figma Generate Library (`figma-generate-library`) organise la création ou la mise à jour d’éléments de design system Figma à partir du code.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[Figma Generate Library mémo|mémo pratique]].

## Résumé

Le [[Skill|skill]] distingue plusieurs périmètres, des seuls tokens à la bibliothèque complète, en passant par une famille de composants ou une mise à jour ciblée. Dans le dépôt examiné, sa copie locale déclare `disable-model-invocation: true`. Le lancement est donc manuel dans Claude Code. La définition amont consultée le 20 novembre 2026 déclare `false`.

## Fonctionnalités

- Comparer le code et les ressources Figma, puis lister les écarts dans le périmètre demandé.
- Créer ou réutiliser des variables primitives, des alias sémantiques, des modes et des styles.
- Construire les composants ou variantes demandés et relier leurs propriétés aux variables. En mise à jour, conserver les identifiants et liaisons valides lorsque c’est possible.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|—|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Le guide GitHub est partagé par plusieurs outils et skills Figma._

### Points forts

Le workflow commence par les fondations et permet de limiter l’intervention aux composants ou tokens demandés. Il prévoit de vérifier les valeurs, les liaisons et le rendu.

### Limites

Il faut l’accès au code de référence, au fichier Figma cible et au serveur distant pour écrire. Le skill orchestre une intervention. La cohérence dépend de l’inventaire et de la validation des états. La documentation décrit une mise à jour par demande, sans synchronisation continue.

### Qualité

Procédure officielle détaillée. Les retours de tiers concernent surtout le workflow de bibliothèque dans son ensemble et un cas ponctuel concerne directement le skill.

## Relations

- **Utilise** [[Figma MCP]] et s’appuie sur [[Figma Use]] pour les appels à la Plugin API.
- **Complémentaire de** [[UI UX Pro Max]] pour passer de spécifications de design system à des éléments natifs dans Figma.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

Digital Rebel décrit un travail sur des tokens, composants et règles avec Claude Code et Figma MCP. Rango.design montre la création d’un ensemble de variables et d’un composant réutilisable sur un périmètre réduit.

### Ce qui est critiqué

Un utilisateur de `figma-generate-library` a signalé que des états de bouton annoncés comme distincts étaient visuellement identiques. Ce cas illustre la nécessité de comparer les variantes en contexte.

### Ce qui n'est pas établi

Les sources consultées ne montrent pas de comparaison reproductible sur la mise à jour de grandes bibliothèques ou la conservation des liaisons au fil des changements de code.

### Comparaison

La construction manuelle dans Figma offre un contrôle direct des états et des liaisons. [[Figma Use]] conduit les appels à la Plugin API, tandis que Figma Generate Library définit l’ordre des opérations pour une bibliothèque.

### Verdict

Adapté à la reproduction ciblée de tokens ou d’une famille de composants. Vérifier les modes, variantes et liaisons avant de diffuser la bibliothèque.

## Sources

- [Définition officielle](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-library/SKILL.md)
- [Écriture sur le canvas](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)

### Sources des avis

- [Retour Digital Rebel](https://digitalrebel.fi/blog/design-systems-with-claude-code-and-figma) — retour de pratique sur le flux Claude Code et Figma. Le rôle propre de ce skill n’est pas isolé.
- [Essai Rango.design](https://rango.design/articles/figma-mcp) — essai sur un fichier brouillon avec le plugin officiel. Les mesures concernent un seul exemple.
- [Discussion sur la création d’un design kit](https://www.reddit.com/r/FigmaDesign/comments/1s44zq4/creating_design_kit/) — témoignage ponctuel sur des états de bouton générés avec le skill.

_Dernière analyse : 20 novembre 2026_
