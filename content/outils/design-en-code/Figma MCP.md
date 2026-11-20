---
title: "Figma MCP"
type: outil
description: "Relie un agent aux maquettes, composants et variables Figma via un serveur distant."
format: serveur-mcp
tags:
  - metier/produit-design
  - metier/ingenierie
  - theme/mcp
  - theme/design-system
  - theme/frontend
editeur: "Figma"
logo: "[[figma.png]]"
site: "https://developers.figma.com/docs/figma-mcp-server/"
statut: disponible
note_documentation: 5
note_precision: 4
note_maturite: 4
memo: "[[Figma MCP mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# Figma MCP

> Figma MCP donne à un agent accès aux fichiers Figma autorisés. Le serveur distant expose le contexte des maquettes et peut aussi modifier des éléments sur le canvas avec les clients et droits compatibles.

**Composition** : Un serveur [[Model Context Protocol|MCP]] distant hébergé par Figma et une option desktop. Le nombre d’outils accessibles dépend du mode de connexion et du client. Le guide public rassemble documentation et skills.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[Figma MCP mémo|mémo pratique]].

## Résumé

Le point d’accès distant `https://mcp.figma.com/mcp` fonctionne sans l’application de bureau. Dans le projet examiné, Claude Code et Codex déclarent le même serveur distant dans `.mcp.json` et `.codex/config.toml`. Une déclaration configure la connexion. L’accès effectif passe par l’autorisation du compte Figma.

## Fonctionnalités

- Extraire le contexte d’une maquette avec `get_design_context`, obtenir une capture avec `get_screenshot` et retrouver les variables attachées à un nœud avec `get_variable_defs`.
- Rechercher les composants et variables de bibliothèques accessibles, puis relier certains composants à leur code avec Code Connect.
- Créer ou modifier des éléments natifs dans Figma avec `use_figma` via le serveur distant et un client compatible. Figma présente l’écriture sur le canvas comme une bêta.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★★|
|Précision des descriptions|★★★★☆|
|Maturité|★★★★☆|
|Popularité|—|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Le guide GitHub est partagé par plusieurs outils et skills Figma._

### Points forts

La lecture fournit à l’agent le contexte d’un élément précis, en complément d’une capture. Une maquette structurée par composants et variables lui donne des références réutilisables.

### Limites

Les outils et quotas dépendent de l’offre, du siège et du client. Figma demande un siège Full pour écrire hors des brouillons et applique les droits du fichier. Les résultats destinés à la production demandent une revue visuelle et une vérification du code.

### Qualité

Documentation officielle détaillée, lecture et écriture observées par des tiers et plus d’un an de recul sur la connexion distante. L’écriture directe reste en bêta.

## Relations

- **Utilisé par** [[Figma Use]] pour l’accès programmatique au canvas et [[Figma Generate Library]] pour les travaux de bibliothèque.
- **Complémentaire de** [[UI UX Pro Max]] lorsque les recommandations d’interface doivent s’appuyer sur une maquette ou des composants Figma existants.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

Rango.design a créé des variables, un composant réutilisable et des instances dans un brouillon. Creative Bloq rapporte un essai de passage de maquettes à du code React avec Claude Code.

### Ce qui est critiqué

L’essai Creative Bloq décrit le travail de préparation des maquettes et de rédaction des consignes. Dans un autre essai, des instructions et une bibliothèque mieux cadrées ont réduit les écarts de réutilisation.

### Ce qui n'est pas établi

Les essais consultés ne couvrent pas toutes les combinaisons de client, de siège et de taille de fichier. Ils ne permettent pas de chiffrer un gain moyen sur des projets de production.

### Comparaison

L’option desktop s’appuie sur l’application et permet de cibler une sélection. Le serveur distant traite des liens de fichiers ou de nœuds et expose l’écriture sur le canvas aux clients compatibles.

### Verdict

Adapté aux allers-retours entre une maquette et son implémentation. Commencer avec un nœud précis et valider le résultat sur le fichier et dans l’application.

## Sources

- [Documentation du serveur](https://developers.figma.com/docs/figma-mcp-server/)
- [Outils et exemples](https://developers.figma.com/docs/figma-mcp-server/tools-and-prompts/)
- [Accès et quotas](https://developers.figma.com/docs/figma-mcp-server/rate-limits-access/)
- [Guide public et skills Figma](https://github.com/figma/mcp-server-guide)

### Sources des avis

- [Essai Rango.design](https://rango.design/articles/figma-mcp) — essai sur un fichier brouillon avec le plugin officiel. Les mesures concernent un seul exemple.
- [Essai de Creative Bloq](https://www.creativebloq.com/ai/designing-using-claude-code-and-figma-mcp-how-good-are-they) — retour d’une équipe sur la transformation de maquettes en composants React.
- [Essai de réutilisation de composants](https://devm.io/ux/design-systems-llms) — comparaison de deux consignes sur une bibliothèque donnée. Plusieurs paramètres variant à la fois, elle n’isole pas l’effet d’un skill.

_Dernière analyse : 20 novembre 2026_
