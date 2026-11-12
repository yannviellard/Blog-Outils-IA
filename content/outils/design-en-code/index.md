---
title: "Design en code"
type: famille
description: "Skills et bibliothèques qui guident l'agent vers une interface soignée, directement dans le code."
modified: 2026-11-12
---

# Design en code

> Skills et bibliothèques qui guident l'agent vers une interface soignée, directement dans le code.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Deux étages : orienter la direction artistique (FrontEnd Design, Huashu, Taste), puis auditer et finir (Impeccable, UI UX Pro Max, Web Design Guidelines) ; shadcn-ui est la brique de composants. Aucun ne remplace une revue visuelle humaine.

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

## Points d'attention

- Direction artistique ([[FrontEnd Design]], [[Huashu Design]], [[Taste Skill]]) : fournir des références de marque et des critères d'acceptation visuels.
- Audit et finition ([[Impeccable]], [[UI UX Pro Max]], [[Web Design Guidelines]]) : compléter par accessibilité, captures comparées et tests utilisateurs.
- Design system ([[shadcn-ui]]) : le code est possédé par l'équipe, donc également maintenu par elle.

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

_Dernière analyse : 12 novembre 2026_
