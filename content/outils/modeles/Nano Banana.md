---
title: "Nano Banana"
type: outil
description: "API et modèles Google pour générer ou retoucher rapidement des images."
format: api
tags:
  - metier/marketing-ventes
  - theme/image
editeur: "Google DeepMind"
site: "https://gemini.google/fr/overview/image-generation/?hl=fr-FR"
statut: disponible
derniere_maj: 2026-06-30
note_documentation: 5
note_precision: 3
note_maturite: 4
memo: "[[Nano Banana mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Nano Banana

> Famille de modèles propriétaires de Google DeepMind, intégrée à Gemini, pour générer et retoucher des images à partir de texte et d’images de référence. Elle couvre désormais trois profils : vitesse et coût avec Nano Banana 2 Lite, polyvalence avec Nano Banana 2, précision avec Nano Banana Pro.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours, et [[Nano Banana mémo]] pour les commandes à retenir.

## Résumé

**Nano Banana** est le nom public de la famille **Gemini Image**. Elle est accessible dans l’application Gemini et, pour les développeurs, dans Google AI Studio, la Gemini API et les offres Google Cloud compatibles.

Le produit se distingue par son fonctionnement conversationnel : on peut fournir une consigne, ajouter une ou plusieurs images, puis demander des corrections successives sans reconstruire tout le prompt. Google met particulièrement en avant la conservation des sujets, le rendu du texte dans l’image, le changement de cadrage, l’éclairage, la mise au point, le transfert de style et l’adaptation aux différents formats.

## Modèles de la famille

|Modèle public|Identifiant API|Positionnement|
|---|---|---|
|Nano Banana 2.1|`gemini-nano-banana-2.1`|Modèle utilisé dans les exemples de la documentation officielle de génération d’images (API « interactions ») ; positionnement détaillé à vérifier dans la documentation.|
|Nano Banana 2 Lite|`gemini-3.1-flash-lite-image`|Le plus rapide et le moins coûteux ; pensé pour le volume, les brouillons et l’idéation. Moins adapté aux nombreuses références et aux longues retouches successives.|
|Nano Banana 2|`gemini-3.1-flash-image`|Modèle généraliste : génération jusqu’en 4K, bon rendu du texte, connaissances du monde et gestion de plusieurs références.|
|Nano Banana Pro|`gemini-3-pro-image`|Modèle premium pour les tâches complexes, la localisation, la cohérence de marque et le contrôle créatif précis.|
|Nano Banana (historique)|`gemini-2.5-flash-image`|Première version, désormais considérée comme historique ; Google recommande de migrer vers 2 Lite.|

## Fonctionnalités

- **Génération et retouche conversationnelles :** création, ajout, suppression ou remplacement d’éléments par instructions en langage naturel.

- **Références visuelles :** utilisation d’images fournies pour préserver un sujet, une identité, un produit ou une direction artistique.

- **Contrôle créatif :** modification de l’angle de vue, du cadrage, de la profondeur de champ, de la lumière, des couleurs et des textures.

- **Texte dans l’image :** génération de titres, affiches, invitations, logos, bandes dessinées et contenus multilingues plus lisibles que sur les générations précédentes.

- **Formats de production :** changement de ratio et redimensionnement sans recadrage destructeur ; Nano Banana 2 vise notamment la génération jusqu’en 4K.

- **Connaissances et données :** Nano Banana 2 et Pro peuvent s’appuyer sur les connaissances de Gemini ; certains parcours Google exploitent aussi des informations issues du Web pour produire des diagrammes ou infographies.

- **Intégration développeur :** appels multimodaux via la Gemini API avec SDK Python, JavaScript, Java et Go, ainsi qu’une interface REST.

- **Traçabilité :** toutes les images générées incorporent le filigrane invisible SynthID ; l’application Gemini ajoute aussi un marquage visible selon le produit ou le forfait.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★★|
|Précision des descriptions|★★★☆☆|
|Qualité visuelle|★★★★☆|
|Retouche d’images|★★★★☆|
|Rendu du texte|★★★★☆|
|Cohérence des sujets|★★★★☆|
|Rapidité|★★★★★|
|Fiabilité factuelle|★★☆☆☆|
|Contrôle pixel à pixel|★★★☆☆|
|Maturité|★★★★☆|
|Popularité|—|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité non notée : pas de dépôt public._

### Points forts

- **Bon équilibre vitesse/qualité :** Nano Banana 2 concentre, selon Google, une grande partie des capacités avancées de Pro dans un modèle Flash plus rapide ; la rapidité est confirmée par les tests indépendants.

- **Retouche naturelle :** l’échange conversationnel est bien adapté aux itérations, même sans maîtriser un logiciel d’édition complexe.

- **Écosystème très large :** disponibilité dans Gemini, AI Studio, l’API, Google Cloud et plusieurs produits Google.

- **Gamme lisible :** Lite pour le volume, 2 pour le quotidien et Pro pour les compositions exigeantes.

### Limites

- **Pas une source factuelle :** une infographie visuellement convaincante peut contenir des dates, chiffres, légendes ou relations erronés ; les données doivent être vérifiées séparément.

- **Résultats variables :** visages, proportions, détails de marque et continuité entre itérations peuvent encore dériver selon le prompt et les références.

- **Contrôle moins déterministe qu’un éditeur classique :** le modèle peut réinterpréter une demande locale et modifier d’autres parties de l’image.

- **Service propriétaire :** poids du modèle, code d’entraînement et licence ne sont pas ouverts ; quotas, prix et disponibilité dépendent des offres Google.

- **Pas de vainqueur universel face aux concurrents :** les comparaisons indépendantes divergent sur le photoréalisme (Tom's Guide donne l'avantage à Nano Banana 2 pour la richesse des décors et les mockups ; TechRadar préfère ChatGPT Images 2.0 sur une série de retouches réalistes) ; les résultats dépendent des prompts, des références et du style recherché.

- **Détails plausibles inventés :** une évaluation académique de Nano Banana Pro relève une forte qualité perceptuelle mais l'invention de détails et des performances inférieures à des modèles spécialisés sur certaines mesures strictes.

- **Quotas et filigranes :** l'accès aux modèles avancés, les quotas et le filigrane visible varient selon le forfait et le produit Google utilisé.

- **Risque de manipulation :** le photoréalisme et l’édition de personnes facilitent la création d’images trompeuses malgré SynthID et les garde-fous.

### Qualité

**Commentaire :** Nano Banana est une offre très complète pour passer rapidement d’une idée à une image exploitable, puis la corriger par conversation. Ses points forts sont la vitesse, la retouche conversationnelle et le texte intégré ; la fidélité aux références est bonne mais n'est pas toujours stricte, et la fiabilité factuelle est faible (voir [[#Avis indépendants|les avis indépendants]]). Il reste nécessaire de contrôler les faits, l’identité des personnes, les marques et les détails fins avant toute publication.

## Relations
 
- **Alternative à :** [[ChatGPT Images]], [[Midjourney]], [[Adobe Firefly]], [[FLUX]], [[Ideogram]]

- **S’intègre avec :** [[Gemini]], [[Google AI Studio]], [[Gemini API]], [[Vertex AI]], [[Google Ads]], [[Google Flow]], [[Stitch by Google]]

- **Utilise :** [[Gemini 3.1 Flash]], [[Gemini 3 Pro]], [[SynthID]], [[Google Search]]


## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Les tests convergent sur trois qualités : **la vitesse**, **la retouche guidée par conversation** et **la richesse visuelle**. Nano Banana 2 conserve souvent des détails fins d’une photo source et produit rapidement des compositions denses. Les progrès du texte intégré sont également nets, ce qui le rend pertinent pour les affiches, maquettes de campagnes, concepts produits et infographies.

Les avis divergent davantage sur le photoréalisme. Dans son comparatif, Tom’s Guide donne l’avantage global à Nano Banana 2 pour la richesse des décors, les mockups et les scènes d’action. TechRadar préfère au contraire ChatGPT Images 2.0 sur une série de retouches réalistes, notamment pour la lumière, les textures et les visages, tout en jugeant Nano Banana plus rapide et souvent plus spectaculaire. Ces résultats dépendent fortement des prompts, des références et du style recherché : il n’existe pas de vainqueur universel.

Les réserves sont importantes. WIRED a obtenu une infographie météo très crédible visuellement mais alimentée par de mauvaises dates, ainsi qu’un montage de visage peu naturel. Une évaluation académique de Nano Banana Pro sur des tâches de vision bas niveau conclut à une forte qualité perceptuelle, mais aussi à l’invention de détails plausibles et à des performances quantitatives inférieures à des modèles spécialisés sur certaines mesures strictes.

### Ce que les utilisateurs apprécient

- Production et itérations rapides, particulièrement avec Nano Banana 2 et 2 Lite.
- Bonne conservation de nombreux détails du sujet et des images de référence.
- Retouche accessible par langage naturel, sans apprentissage d’un éditeur complexe.
- Texte, affiches et visuels marketing plus convaincants que sur de nombreux générateurs précédents.
- Accès simple dans Gemini et intégration directe dans l’écosystème Google.

### Critiques récurrentes

- Données, dates, flèches et légendes d’infographies susceptibles d’être fausses malgré un rendu crédible.
- Visages ou intégrations de sujets parfois artificiels, comme un collage ou une retouche trop lisse.
- Tendance possible à privilégier un rendu séduisant plutôt qu’une reproduction strictement fidèle au pixel.
- Variabilité entre générations et nécessité de prompts précis pour conserver identité, proportions et composition.
- Quotas, filigranes visibles et accès aux modèles avancés variables selon le forfait et le produit Google utilisé.

### Comparaison

**ChatGPT Images** peut être préférable pour certaines retouches photoréalistes et le comportement de la lumière ; **Midjourney** reste très fort pour une direction artistique immédiatement marquée ; **Adobe Firefly** offre un workflow plus intégré aux outils de création ; **Ideogram** demeure une référence utile pour les compositions typographiques. Nano Banana se distingue par la combinaison de la vitesse, de la conversation multimodale, des références visuelles et de son intégration à Gemini.

### Verdict

**Excellent choix pour l’idéation, la retouche rapide, les campagnes visuelles et les variantes à grande échelle.** Pour un contenu publié, il faut relire tout texte, vérifier chaque donnée et contrôler les détails sensibles. Pour une retouche déterministe, une identité de marque stricte ou un travail scientifique, un outil spécialisé reste nécessaire en complément.

## Sources

- [Présentation française de Nano Banana 2](https://gemini.google/fr/overview/image-generation/?hl=fr-FR)

- [Famille Gemini Image — Google DeepMind](https://deepmind.google/models/gemini-image/)

- [Documentation de génération d’images — Gemini API](https://ai.google.dev/gemini-api/docs/image-generation)

- [Lancement de Nano Banana 2 Lite](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)

- [Présentation de Nano Banana Pro](https://blog.google/innovation-and-ai/products/nano-banana-pro/)

### Sources des avis

- [WIRED — prise en main de Nano Banana 2](https://www.wired.com/story/google-nano-banana-2-ai-image-generator-hands-on/)
- [Tom’s Guide — Nano Banana 2 face à ChatGPT 5.2](https://www.tomsguide.com/ai/chatgpt-5.2-vs-nano-banana-2-i-tested-both-to-find-the-better-ai-image-generator)
- [TechRadar — comparaison de retouches réelles avec ChatGPT Images 2.0](https://www.techradar.com/ai-platforms-assistants/i-compared-chatgpt-images-2-0-and-googles-nano-banana-2-using-real-world-prompts-from-portraits-to-product-shots-and-the-ai-image-generator-that-came-out-on-top-genuinely-surprised-me)
- [Évaluation académique de Nano Banana Pro sur 14 tâches et 40 jeux de données](https://arxiv.org/abs/2512.15110)
- [Documentation officielle de la famille Gemini Image](https://ai.google.dev/gemini-api/docs/image-generation)

_Dernière analyse : 12 novembre 2026_
