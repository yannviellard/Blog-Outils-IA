---
title: "Modèles"
type: famille
description: "Modèles d'IA propriétaires consommés par API."
modified: 2026-11-12
---

# Modèles

> Modèles d'IA propriétaires consommés par API.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Deux modèles propriétaires consommés par API, qui ne se comparent pas entre eux : décisions typées pour Jev, images pour Nano Banana. Chacun se compare à son alternative établie (indiquée).

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Jev]]|API de décisions typées, rapides et peu coûteuses pour classer, router ou filtrer.|API|[[Jev mémo\|Mémo]]|
|[[Nano Banana]]|API et modèles Google pour générer ou retoucher rapidement des images.|API|[[Nano Banana mémo\|Mémo]]|

## Points d'attention

- [[Jev]] : escalader les cas ambigus ou à faible confiance vers un humain ou un LLM.
- [[Nano Banana]] : contrôler les droits, le texte généré et la cohérence de marque.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Jev]]|★★★★★|★★★☆☆|★☆☆☆☆|**9**|—|Doc remarquable (18 cookbooks) ; chiffres de lancement non reproduits ; lancé en septembre 2026.|
|[[Nano Banana]]|★★★★★|★★★☆☆|★★★★☆|**12**|—|Doc API complète ; comparaisons indépendantes divergentes ; famille de modèles établie.|

## Critères propres à la famille

|Outil|Usage|Ouverture|Modèle économique|Limite principale|Alternative établie|
|---|---|---|---|---|---|
|[[Jev]]|Décisions typées sur du texte (classer, router, filtrer)|Propriétaire (SDK et skill MIT)|À l'usage : 0,042 $ par million de tokens en entrée, sortie gratuite (annoncé)|Chiffres de lancement non reproduits, accès instable|Petits LLM, classifieurs BERT|
|[[Nano Banana]]|Génération et retouche d'images|Propriétaire|API et forfaits Google|Fiabilité factuelle faible, quotas|ChatGPT Images, Midjourney, Adobe Firefly, FLUX, Ideogram|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[ChatGPT Images]], [[Midjourney]], [[Adobe Firefly]], [[FLUX]], [[Ideogram]], [[Laya]].

_Dernière analyse : 12 novembre 2026_
