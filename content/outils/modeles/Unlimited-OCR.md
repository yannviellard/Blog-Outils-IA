---
title: "Unlimited-OCR"
type: outil
description: "Modèle OCR de Baidu à poids ouverts pour extraire et structurer le contenu de documents multipages."
format: bibliotheque
tags:
  - metier/ingenierie
  - metier/operations
  - theme/extraction-donnees
editeur: "Baidu"
logo: "[[baidu.png]]"
site: "https://huggingface.co/baidu/Unlimited-OCR-2"
depot: "https://github.com/baidu/Unlimited-OCR"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-16
etoiles: 31324
forks: 3358
etoiles_releve: 2026-11-19
note_documentation: 4
note_precision: 3
note_maturite: 2
note_popularite: 4
memo: "[[Unlimited-OCR mémo]]"
avis_maj: 2026-11-19
modified: 2026-11-19
---

# Unlimited-OCR

> Baidu propose deux générations de modèles pour transcrire et structurer des documents à partir d'images de pages. Unlimited OCR 2 vise les PDF longs dont le texte ou les tableaux se poursuivent d'une page à l'autre.

Voir aussi le [[Unlimited-OCR mémo|mémo pratique]] et les [[#Avis indépendants|avis indépendants]].

## Résumé

Unlimited-OCR est le dépôt commun aux deux générations. La première est sortie le 22 juin 2026 et **Unlimited OCR 2** le 27 octobre 2026. Cette fiche porte principalement sur la seconde, celle que documente la branche principale. Le code du dépôt et les poids de la v2 sont publiés sous licence MIT. Baidu propose également un accès hébergé via TextMind.

En local, le PDF est d'abord converti en images ordonnées. Le modèle produit des blocs balisés indiquant notamment le type et la position du contenu. Un script de Baidu convertit ces blocs en Markdown et conserve les tableaux en HTML.

## Fonctionnalités

- **OCR multipage** : exploite le contexte des pages voisines pour reconstituer l'ordre de lecture et rapprocher des fragments de texte ou de tableaux.
- **Analyse de mise en page** : repère les titres, tableaux, figures et autres blocs, avec leurs coordonnées. Le post-traitement peut réunir les fragments d'un tableau réparti sur plusieurs pages.
- **Deux modes d'inférence** : Transformers pour un essai Python, ou une version adaptée de SGLang pour servir le modèle via une API compatible OpenAI. Le mode par fenêtres de SGLang traite les longs documents par groupes de pages.
- **Attention clairsemée (SR-SWA)** : la v2 sélectionne un ensemble borné de références visuelles à consulter pendant le décodage. Le rapport de Baidu décrit une réduction du coût de cette étape sur les documents longs.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|★★★★☆|

> Notes alignées sur le [[Comparatif global des outils|barème global]]. Popularité calculée sur l'ensemble du dépôt, qui comptait 31 324 étoiles et 3 358 forks le 19 novembre 2026.

### Points forts

- Poids téléchargeables et traitement local possible. C'est pertinent lorsque les documents doivent rester dans l'environnement de l'entreprise.
- La structure de sortie permet de contrôler l'ordre de lecture et de revenir aux zones de la page source.
- Le dépôt documente l'inférence et fournit le convertisseur Markdown, ainsi que les scripts des benchmarks multipages de Baidu.

### Limites

- La configuration de référence de Baidu utilise une NVIDIA A800 avec 80 Go de VRAM. Le chemin SGLang dépend d'un paquet adapté par Baidu. Les besoins réels varient avec le moteur, le document et les paramètres.
- L'exemple Transformers utilise `trust_remote_code=True`, qui exécute du code Python distribué avec le modèle. En entreprise, épingler et examiner la révision avant exécution.
- Un essai tiers de la v2 a observé des sorties incomplètes sans erreur explicite. Vérifier la couverture des pages, les cellules et les chiffres avant d'indexer le résultat ou de l'utiliser dans un processus métier.

### Qualité

Les exemples et le rapport suffisent pour monter un essai. Le dimensionnement matériel reste peu documenté. Les comparaisons indépendantes confirment l'intérêt du modèle, avec des résultats sensibles au corpus et à la configuration. La première génération a moins de six mois de recul au moment de cette analyse.

## Relations

- **Alternatives** : DeepSeek-OCR-2, PaddleOCR-VL et Chandra 2 pour l'analyse documentaire. Le choix dépend des documents, des champs à conserver et du moteur d'inférence disponible.
- **Complément** : [[NotebookLM]] pour interroger des documents après extraction, quand la politique de traitement des données autorise leur import.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 19 novembre 2026._

### Ce qui est apprécié

- **V2** : Efraín Garay relève un taux d'erreur médian de 0,12 % par caractère sur 20 pages riches en texte d'un rapport de la Banque centrale du Chili, sur une RTX 4070 Ti SUPER de 16 Go. La référence était la couche texte du PDF et les pages ne comportaient pas d'images.
- **V1** : Newtuple place Unlimited-OCR en tête selon son juge LLM sur quatre lots, avec son écart le plus marqué sur les pages mixtes de rapports financiers. La comparaison utilise des baselines plus anciennes et mesure des pages isolées.

### Ce qui est critiqué

- **V2** : dans l'essai de Garay, Transformers a épuisé les 16 Go de VRAM sur un document de 80 pages. Le mode par fenêtres de la version SGLang testée s'est bloqué et une exécution en fenêtre unique a renvoyé 24 pages sur 40. Le test portait sur une version du paquet antérieure à celle indiquée aujourd'hui dans le dépôt.
- **V1** : sur PureDocBench, le score du modèle passe de 72,05 sur le niveau facile à 53,71 sur le niveau difficile. Newtuple relève également des problèmes d'alignement dans des tableaux financiers.

### Ce qui n'est pas établi

- Le rapport de Baidu annonce 84,59 sur MPDocBench et 77,06 sur MarathonDocBench pour la v2. Les essais tiers cités utilisent d'autres corpus et ne reproduisent pas ces scores. La capacité à traiter de façon fiable plusieurs centaines de pages sur une configuration donnée reste à mesurer.
- Les sources consultées ne permettent pas d'estimer uniformément la qualité sur des formulaires manuscrits, des scans dégradés et des documents multilingues.

### Comparaison

Sur les 20 pages du rapport chilien, Garay relève une erreur médiane de 0,31 % pour Chandra 2 et de 3,12 % pour DeepSeek-OCR (première version). PureDocBench compare pour sa part Unlimited-OCR v1 à PaddleOCR-VL et DeepSeek-OCR-2 sur des pages de difficulté croissante. Ces protocoles éclairent des usages différents. Pour une décision de déploiement, comparer les moteurs sur les mêmes PDF, à résolution égale, et mesurer séparément la couverture des pages, l'exactitude des tableaux et le coût.

### Verdict

Un candidat à tester pour structurer localement des PDF multipages, notamment quand un tableau se poursuit sur la page suivante. La couverture des pages et la fidélité des tableaux méritent un contrôle explicite sur les documents les plus longs.

## Sources

- [Dépôt et documentation Baidu](https://github.com/baidu/Unlimited-OCR) et [métadonnées de l'API GitHub](https://api.github.com/repos/baidu/Unlimited-OCR).
- [Poids et fiche du modèle v2](https://huggingface.co/baidu/Unlimited-OCR-2) et [fiche v1](https://huggingface.co/baidu/Unlimited-OCR).
- [Rapport technique de Baidu pour la v2](https://arxiv.org/abs/2610.39308) et [documentation du post-traitement](https://github.com/baidu/Unlimited-OCR/tree/main/utils).
- [Avatar de l'organisation Baidu sur GitHub](https://avatars.githubusercontent.com/u/13245940?v=4&s=256).

### Sources des avis

- [Efraín Garay, comparaison locale sur 16 Go](https://efraingaray.com/en/blog/unlimited-ocr-2-16gb/). Essai indépendant de la v2 avec protocole et révisions indiqués. Corpus et matériel limités.
- [Newtuple, benchmark OCR mis à jour le 16 octobre 2026](https://www.newtuple.com/post/ocr-benchmark-paddleocr-docling-llamaparse-surya). Essai tiers de la v1 sur la plateforme d'évaluation de l'auteur. Jugement par LLM et baselines de juin.
- [PureDocBench, résultats par difficulté](https://huggingface.co/datasets/zhihengli-casia/puredocbench). Résultats publiés par l'équipe du benchmark sur la v1. Comparaison standardisée de la restitution des pages.

_Dernière analyse : 19 novembre 2026_
