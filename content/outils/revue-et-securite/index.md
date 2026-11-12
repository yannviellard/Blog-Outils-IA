---
title: "Revue, sécurité et création de skills"
type: famille
description: "Contrôle de la qualité du code et des extensions produits avec un agent."
modified: 2026-11-12
---

# Revue, sécurité et création de skills

> Contrôle de la qualité du code et des extensions produits avec un agent.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Premier filet, jamais contrôle unique : les trois outils sont des assistants dans le flux, à compléter par tests, analyse statique et humain.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Claude Code Review]]|Première passe de revue de code intégrée au dépôt et au flux de développement.|Plugin|[[Claude Code Review mémo\|Mémo]]|
|[[Security Guidance]]|Garde-fou de sécurité pendant la génération et avant commit ou push.|Plugin|[[Security Guidance mémo\|Mémo]]|
|[[Skill Creator]]|Création, test comparatif et optimisation de skills avec un vrai cycle d'évaluation.|Skill|[[Skill Creator mémo\|Mémo]]|

## Points d'attention

- Compléter avec tests, SAST/SCA et revue humaine.
- Auditer les instructions et scripts des skills comme toute dépendance logicielle.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Claude Code Review]]|★★★★★|★★★☆☆|★★★☆☆|**11**|—|Doc officielle complète ; chiffres internes ; fonctions en research preview.|
|[[Security Guidance]]|★★★★☆|★★★★☆|★★★☆☆|**11**|—|README précis, limites explicites ; plugin récent lié à la version de Claude Code.|
|[[Skill Creator]]|★★★★☆|★★★★☆|★★★☆☆|**11**|—|SKILL.md dense mais documenté, limites assumées ; circularité possible des évaluations.|

## Critères propres à la famille

|Outil|Déclenchement|Coût|Limite principale|À compléter par|
|---|---|---|---|---|
|[[Claude Code Review]]|Local, cloud (ultra), service managé|0 / 5–25 $ / 15–25 $ par revue|Angles morts d'un même modèle ; chiffres internes|Second modèle, tests, humain|
|[[Security Guidance]]|Hooks à l'écriture et au commit|Appels API (×2 en mode dual)|Faux positifs et manqués ; pas un SAST|CodeQL, Semgrep, Snyk|
|[[Skill Creator]]|Cycle construire–évaluer–réviser|Tokens significatifs|Circularité des cas de test générés|Vrais cas + jeu de validation séparé|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[CodeRabbit]], [[GitHub Copilot Code Review]], [[Cursor Bugbot]].

_Dernière analyse : 12 novembre 2026_
