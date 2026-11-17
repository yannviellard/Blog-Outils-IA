---
title: "Image, vidéo et médias"
type: famille
description: "Génération d'images et de vidéos, et production vidéo programmable."
modified: 2026-11-17
---

# Image, vidéo et médias

> Génération d'images et de vidéos, et production vidéo programmable.

Zone : [[outils/index#Produire et décider|Produire et décider]] · Barème : [[Comparatif global des outils]]

## En bref

Distinguer ce qui génère des pixels (Higgsfield, Glif, et le modèle [[Nano Banana]], rangé dans la famille [[outils/modeles/index|Modèles]]) de ce qui compose une vidéo de façon reproductible (Remotion, HyperFrames) : ils sont complémentaires, pas concurrents. Les générateurs exigent de tester coûts et nombre d'itérations réels.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Banana Prompts]]|Bibliothèque visuelle de prompts et studio de génération par crédits.|Application|—|
|[[Glif MCP]]|Passerelle MCP vers des workflows créatifs image, vidéo et audio réutilisables.|Serveur MCP|[[Glif MCP mémo\|Mémo]]|
|[[Higgsfield-ai-platform]]|Studio en ligne agrégeant de nombreux modèles d'image, vidéo et audio.|Application|—|
|[[Higgsfield-skills]]|Accès agentique aux fonctions créatives de Higgsfield, à encadrer par budgets et validations.|Collection|[[Higgsfield-skills mémo\|Mémo]]|
|[[Open Generative AI]]|Studio d'image et de vidéo open source et auto-hébergeable, qui génère surtout via l'API payante Muapi.ai.|Application|—|
|[[Remotion]]|Vidéo-as-code mature en React pour productions déterministes et data-driven.|Bibliothèque|[[Remotion mémo\|Mémo]]|
|[[HyperFrames]]|Vidéo programmable en HTML/CSS/JavaScript, particulièrement accessible aux agents.|Bibliothèque|[[HyperFrames mémo\|Mémo]]|

## Points d'attention

- Génération d'images ([[Banana Prompts]], [[Glif MCP]]) : contrôler les droits, le texte généré et la cohérence de marque.
- Plateformes Higgsfield : tester crédits, files d'attente, licence et coût réel des variantes.
- [[Open Generative AI]] : interface ouverte, mais générations facturées par Muapi.ai, la société de son auteur ; son positionnement « sans filtre de contenu » contredit les conditions de Muapi et laisse à l'utilisateur la responsabilité des contenus.
- Vidéo programmable ([[Remotion]], [[HyperFrames]]) : pertinent pour la production répétable ; excessif pour un montage ponctuel.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Banana Prompts]]|★★★☆☆|★★★★☆|★★☆☆☆|**9**|—|Site et FAQ, fiche fidèle ; équipe peu documentée.|
|[[Glif MCP]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★☆☆☆|Doc correcte ; dépôt déprécié, serveur propriétaire ; plateforme établie.|
|[[Higgsfield-ai-platform]]|★★☆☆☆|★★★☆☆|★★★☆☆|**8**|—|Pas de documentation technique publique ; crédits opaques ; offre en évolution rapide.|
|[[Higgsfield-skills]]|★★★★☆|★★★★☆|★★☆☆☆|**10**|★★★☆☆|README, INSTALL, COOKBOOK ; dépend du service ; 89 commits, pas de releases.|
|[[Open Generative AI]]|★★★☆☆|★★☆☆☆|★★★☆☆|**8**|★★★★☆|README complet mais promotionnel ; « sans filtre », données locales et nombre de modèles (200 à 800) contredits ou incohérents ; 9 mois, v2.0.0, actif, installeurs non signés.|
|[[Remotion]]|★★★★★|★★★★☆|★★★★★|**14**|★★★★☆|~1 000 pages de doc ; licence particulière signalée ; production établie.|
|[[HyperFrames]]|★★★★☆|★★★☆☆|★★☆☆☆|**9**|★★★★☆|Doc abondante ; revendications d'éditeur ; v0.x, peu de retours de production.|

## Critères propres à la famille

|Outil|Rôle|Ouverture|Modèle économique|Limite principale|
|---|---|---|---|---|
|[[Banana Prompts]]|Bibliothèque de prompts + studio|Propriétaire|Crédits (9,99–59,99 $/mois)|Qualité variable des prompts|
|[[Glif MCP]]|Agent créatif via MCP|Serveur propriétaire|Crédits|Reproductibilité moindre|
|[[Higgsfield-ai-platform]]|Agrégateur de modèles|Propriétaire|Crédits, abonnements|Opacité des crédits et files|
|[[Higgsfield-skills]]|Skills autour de la plateforme|MIT (service propriétaire)|Crédits Higgsfield|Dépendance totale au service|
|[[Open Generative AI]]|Interface auto-hébergeable, inférence locale en option|MIT|Paiement à l'usage chez Muapi.ai|Dépendance à Muapi, positionnement « sans filtre »|
|[[Remotion]]|Vidéo-as-code React|Licence particulière|Licence commerciale selon taille|N'est pas un générateur IA|
|[[HyperFrames]]|Vidéo-as-code HTML|Apache-2.0|Gratuit, rendu à votre charge|v0.x, peu de recul|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[Runway]], [[Kling]], [[Veo]], [[FLUX]], [[ElevenLabs]], [[Motion Canvas]], [[MoviePy]].

_Dernière analyse : 17 novembre 2026_
