---
title: "Modèles"
type: famille
description: "Modèles d'IA spécialisés, accessibles par API ou à déployer à partir de poids téléchargeables."
modified: 2026-11-19
---

# Modèles

> Modèles d'IA spécialisés, accessibles par API ou à déployer à partir de poids téléchargeables.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Jev produit des décisions typées, Nano Banana génère et retouche des images, et Unlimited-OCR transcrit et structure des documents. Pour chaque usage, le tableau des critères indique les alternatives à comparer.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Jev]]|API de décisions typées, rapides et peu coûteuses pour classer, router ou filtrer.|API|[[Jev mémo\|Mémo]]|
|[[Nano Banana]]|API et modèles Google pour générer ou retoucher rapidement des images.|API|[[Nano Banana mémo\|Mémo]]|
|[[Unlimited-OCR]]|Modèle OCR de Baidu à poids ouverts pour extraire et structurer le contenu de documents multipages.|Bibliothèque|[[Unlimited-OCR mémo\|Mémo]]|

## Points d'attention

- [[Jev]] : escalader les cas ambigus ou à faible confiance vers un humain ou un LLM.
- [[Nano Banana]] : contrôler les droits, le texte généré et la cohérence de marque.
- [[Unlimited-OCR]] : mesurer la couverture des pages et la fidélité des tableaux sur les PDF les plus longs.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Jev]]|★★★★★|★★★☆☆|★☆☆☆☆|**9**|—|Doc remarquable (18 cookbooks) ; chiffres de lancement non reproduits ; lancé en septembre 2026.|
|[[Nano Banana]]|★★★★★|★★★☆☆|★★★★☆|**12**|—|Doc API complète ; comparaisons indépendantes divergentes ; famille de modèles établie.|
|[[Unlimited-OCR]]|★★★★☆|★★★☆☆|★★☆☆☆|**9**|★★★★☆|Exemples d'inférence et rapport détaillés, dimensionnement peu documenté. Essais tiers encourageants sur certains corpus, limites multipages observées. Dépôt lancé en juin 2026.|

## Critères propres à la famille

|Outil|Usage|Ouverture|Modèle économique|Limite principale|Alternative établie|
|---|---|---|---|---|---|
|[[Jev]]|Décisions typées sur du texte (classer, router, filtrer)|Propriétaire (SDK et skill MIT)|À l'usage : 0,042 $ par million de tokens en entrée, sortie gratuite (annoncé)|Chiffres de lancement non reproduits, accès instable|Petits LLM, classifieurs BERT|
|[[Nano Banana]]|Génération et retouche d'images|Propriétaire|API et forfaits Google|Fiabilité factuelle faible, quotas|ChatGPT Images, Midjourney, Adobe Firefly, FLUX, Ideogram|
|[[Unlimited-OCR]]|OCR et structuration de documents multipages|Code et poids de la v2 sous MIT|GPU en local ou offre hébergée Baidu|Mémoire GPU et sorties parfois incomplètes sur les documents longs|DeepSeek-OCR-2, PaddleOCR-VL, Chandra 2|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[ChatGPT Images]], [[Midjourney]], [[Adobe Firefly]], [[FLUX]], [[Ideogram]], [[Laya]].

_Dernière analyse : 19 novembre 2026_
