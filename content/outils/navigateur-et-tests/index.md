---
title: "Navigateur et tests"
type: famille
description: "Pilotage d'un navigateur ou d'une application par l'agent, pour tester, diagnostiquer ou automatiser."
modified: 2026-11-12
---

# Navigateur et tests

> Pilotage d'un navigateur ou d'une application par l'agent, pour tester, diagnostiquer ou automatiser.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Playwright pour le déterminisme, DevTools pour le diagnostic, Agent Browser pour la navigation d'agent ; OpenCLI est le seul à réutiliser vos sessions connectées, donc le plus risqué.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Playwright]]|Tests et automatisation reproductibles sur Chromium, Firefox et WebKit.|Bibliothèque|[[Playwright mémo\|Mémo]]|
|[[Agent Browser]]|Navigation Chrome conçue pour les agents, compacte et orientée accessibilité.|CLI|[[Agent Browser mémo\|Mémo]]|
|[[Chrome DevTools MCP]]|Inspection profonde de Chrome : console, réseau, DOM, performance et runtime.|Serveur MCP|[[Chrome DevTools MCP mémo\|Mémo]]|
|[[OpenCLI]]|Transformation de sites et applications déjà connectés en commandes déterministes.|CLI|[[OpenCLI mémo\|Mémo]]|

## Points d'attention

- Playwright pour le déterminisme, DevTools pour le diagnostic, profils isolés pour les agents.
- Avec [[OpenCLI]], qui réutilise des sessions connectées, privilégier la lecture seule au départ et des permissions minimales.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Playwright]]|★★★★★|★★★★★|★★★★★|**15**|★★★★★|Doc de référence ; affirmations largement confirmées ; projet établi (2020+).|
|[[Agent Browser]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★★☆|README détaillé ; propriétés de sécurité décrites par le projet ; jeune.|
|[[Chrome DevTools MCP]]|★★★★☆|★★★★☆|★★★★☆|**12**|★★★★☆|Doc officielle, périmètre net ; éditeur établi, évolution rapide.|
|[[OpenCLI]]|★★★★☆|★★★☆☆|★★☆☆☆|**9**|★★★★☆|Doc riche ; politique de sécurité promise non livrée ; ~6 mois, comptes bannis.|

## Critères propres à la famille

|Outil|Modèle|Session de l'utilisateur|Idéal pour|À éviter pour|
|---|---|---|---|---|
|[[Playwright]]|Framework de test cross-browser|Non (contextes isolés)|E2E reproductibles en CI|Exploration libre par un agent|
|[[Agent Browser]]|CLI Rust, snapshots d'accessibilité|Profils persistants|Navigation d'un agent de code|QA déterministe|
|[[Chrome DevTools MCP]]|MCP officiel Chrome|Chrome réel|Diagnostic réseau, console, performance|Suites de tests en CI|
|[[OpenCLI]]|Adaptateurs sur Chrome connecté|Oui, sessions réelles|Lire des données de sites sans API|Actions d'écriture, comptes sensibles|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[Cypress]], [[Selenium]], [[WebdriverIO]].

_Dernière analyse : 12 novembre 2026_
