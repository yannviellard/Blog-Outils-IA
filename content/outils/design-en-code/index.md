---
title: "Design en code"
type: famille
description: "Outils pour concevoir des interfaces dans le code et relier leur implémentation aux maquettes et bibliothèques de design."
modified: 2026-11-20
---

# Design en code

> Outils pour concevoir des interfaces dans le code et relier leur implémentation aux maquettes et bibliothèques de design.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Deux étages : orienter la direction artistique (FrontEnd Design, Huashu, Taste), puis auditer et finir (Impeccable, UI UX Pro Max, Web Design Guidelines) ; shadcn-ui est la brique de composants. Aucun ne remplace une revue visuelle humaine.

[[Figma MCP]], [[Figma Use]] et [[Figma Generate Library]] couvrent trois besoins : lire une maquette, modifier ses éléments et construire une bibliothèque à partir du code.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[FrontEnd Design]]|Direction artistique initiale pour éviter les interfaces frontend génériques.|Skill|[[FrontEnd Design mémo\|Mémo]]|
|[[Huashu Design]]|Workflow design-as-code ouvert avec exploration de plusieurs directions visuelles.|Skill|[[Huashu Design mémo\|Mémo]]|
|[[Taste Skill]]|Exploration visuelle plus expressive pour sortir des layouts IA répétitifs.|Collection|[[Taste Skill mémo\|Mémo]]|
|[[Impeccable]]|Audit et finition ciblée de la typographie, du rythme, de la hiérarchie et du polish.|Skill|[[Impeccable mémo\|Mémo]]|
|[[UI UX Pro Max]]|Base locale de styles, palettes, typographies, règles UX et recommandations par stack.|Skill|[[UI UX Pro Max mémo\|Mémo]]|
|[[Web Design Guidelines]]|Audit sémantique de plus de cent règles UI, accessibilité et performance.|Skill|[[Web Design Guidelines mémo\|Mémo]]|
|[[shadcn-ui]]|Fondation de design system React dont l'équipe possède directement le code.|Bibliothèque|[[shadcn-ui mémo\|Mémo]]|
|[[Figma MCP]]|Relie un agent aux maquettes, composants et variables Figma via un serveur distant.|Serveur MCP|[[Figma MCP mémo\|Mémo]]|
|[[Figma Use]]|Guide la lecture et la modification du canvas avec la Plugin API de Figma.|Skill|[[Figma Use mémo\|Mémo]]|
|[[Figma Generate Library]]|Construit ou met à jour dans Figma les tokens, composants et variantes issus d’une base de code.|Skill|[[Figma Generate Library mémo\|Mémo]]|

## Points d'attention

- Direction artistique ([[FrontEnd Design]], [[Huashu Design]], [[Taste Skill]]) : fournir des références de marque et des critères d'acceptation visuels.
- Audit et finition ([[Impeccable]], [[UI UX Pro Max]], [[Web Design Guidelines]]) : compléter par accessibilité, captures comparées et tests utilisateurs.
- Design system ([[shadcn-ui]]) : le code est possédé par l'équipe, donc également maintenu par elle.
- Pour Figma, préciser le fichier et la bibliothèque de référence, puis contrôler les variables et variantes avant de partager les changements.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[FrontEnd Design]]|★★★☆☆|★★★★☆|★★★☆☆|**10**|—|SKILL.md unique, description fidèle ; skill officiel.|
|[[Huashu Design]]|★★★★☆|★★★☆☆|★★☆☆☆|**9**|★★★★☆|README bilingue ; démonstrations promotionnelles ; licence changée en mai 2026.|
|[[Taste Skill]]|★★★☆☆|★★★☆☆|★★☆☆☆|**8**|★★★★★|Site + README ; v2 expérimentale ; aucune évaluation indépendante.|
|[[Impeccable]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★★★|Doc du site et du dépôt ; fonctions fidèles ; structure en évolution.|
|[[UI UX Pro Max]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★★★★|Doc correcte ; exhaustivité apparente ; packaging fragile.|
|[[Web Design Guidelines]]|★★★★☆|★★★★☆|★★★☆☆|**11**|—|Référentiel détaillé ; revue statique assumée ; collection récente.|
|[[shadcn-ui]]|★★★★★|★★★★★|★★★★☆|**14**|★★★★★|Doc de référence ; modèle éprouvé ; Base UI et presets récents.|
|[[Figma MCP]]|★★★★★|★★★★☆|★★★★☆|**13**|—|Documentation officielle détaillée, lecture et écriture observées par des tiers et plus d’un an de recul sur la connexion distante. L’écriture directe reste en bêta.|
|[[Figma Use]]|★★★★☆|★★★★☆|★★★☆☆|**11**|—|Références techniques détaillées et opérations sur les composants observées dans des essais du flux Figma. L’effet propre du skill n’est pas mesuré.|
|[[Figma Generate Library]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|—|Procédure officielle détaillée. Les retours de tiers concernent surtout le workflow de bibliothèque dans son ensemble et un cas ponctuel concerne directement le skill.|

## Critères propres à la famille

|Outil|Étape|Forme|Sortie|Limite principale|
|---|---|---|---|---|
|[[FrontEnd Design]]|Génération initiale|Skill|Direction artistique du premier jet|Déclaratif, aucune validation visuelle|
|[[Huashu Design]]|Prototype HTML|Skill|HTML, PPTX, animations|Jeune, licence récemment changée|
|[[Taste Skill]]|Exploration|Skills|Variance, motion, densité réglables|Variance pouvant devenir incohérence|
|[[Impeccable]]|Audit et finition|Skill|24 commandes, 61 règles déterministes|Retouches cosmétiques sans fin|
|[[UI UX Pro Max]]|Décision de design|Skill + base de données|Recommandations par stack|Ne garantit pas le résultat final|
|[[Web Design Guidelines]]|Audit du code|Skill|`fichier:ligne` sur 100+ règles|Revue statique, référentiel distant|
|[[shadcn-ui]]|Implémentation|Bibliothèque|Composants dont l'équipe possède le code|Maintenance à la charge de l'équipe|
|[[Figma MCP]]|Aller-retour maquette ↔ code|Serveur MCP distant|Contexte et modifications Figma natives|Droits, quotas et compatibilité client|
|[[Figma Use]]|Inspection et édition|Skill + Plugin API|Nœuds, composants et variables dans Figma|Dépend de l’accès à use_figma|
|[[Figma Generate Library]]|Création ou rapprochement code–maquette|Skill + Figma MCP|Bibliothèque de tokens, composants et variantes|Contrôle de l’inventaire, des états et des liaisons|

_Dernière analyse : 20 novembre 2026_
