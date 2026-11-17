---
title: "HyperFrames"
type: outil
description: "Vidéo programmable en HTML/CSS/JavaScript, particulièrement accessible aux agents."
format: bibliotheque
tags:
  - metier/marketing-ventes
  - theme/video
  - theme/frontend
editeur: "HeyGen"
logo: "[[hyperframes.png]]"
site: "https://hyperframes.heygen.com/"
depot: "https://github.com/heygen-com/hyperframes"
licence: "Apache-2.0"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 84945
forks: 7866
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 3
note_maturite: 2
note_popularite: 4
memo: "[[HyperFrames mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# HyperFrames

> Framework open source de HeyGen permettant de créer des vidéos MP4 déterministes à partir de HTML, CSS, médias et animations, avec une architecture particulièrement conçue pour être pilotée par des coding agents.

**Composition** : 21 skills.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[HyperFrames mémo]] pour le mémo pratique.

## Résumé

HyperFrames transforme le web en format d'authoring vidéo : une composition est décrite en HTML/CSS/JS, enrichie avec des médias et des animations seekable, puis rendue de manière déterministe en MP4.

Le projet combine un **CLI**, un moteur de rendering basé notamment sur Chromium/Puppeteer et FFmpeg, un **Studio graphique**, un SDK, un player embarquable, des capacités de rendering distribué et un ensemble de **21 Skills destinées aux coding agents**.

Son positionnement distinctif est donc moins celui d'un simple moteur vidéo que celui d'une **infrastructure de création vidéo agentique** : l'agent peut planifier une vidéo, produire la composition HTML, configurer les animations, intégrer les médias, effectuer les contrôles puis lancer le rendering.

## Fonctionnalités

- **Composition vidéo en HTML/CSS/JS** avec animations seekable et rendu déterministe en MP4.
    
- **CLI** pour initialiser, prévisualiser, éditer et rendre les compositions.
    
- **HyperFrames Studio**, éditeur graphique avec timeline et interface dockable.
    
- **21 Skills pour agents**, chargées à la demande via un router `/hyperframes`.
    
- Workflows spécialisés : `product-launch-video`, `faceless-explainer`, `pr-to-video`, `embedded-captions`, `talking-head-recut`, `music-to-video`, `motion-graphics`, etc.
    
- Support de technologies web et d'animation telles que **GSAP, Anime.js, Lottie, Three.js et WAAPI**.
    
- **Registry** de composants et blocs réutilisables.
    
- **Player embarquable** et SDK pour intégration dans d'autres applications.
    
- Rendering distribué via **AWS Lambda** et **Google Cloud Run**.
    
- Intégrations explicites avec **Claude Code, Codex, Cursor et Gemini CLI**.
    
- Captures de sites web et workflows de transformation d'un site ou d'un contenu existant en vidéo.
    
- Exemples open source de vidéos de lancement produits réalisés avec HyperFrames.
    

## Analyse

|**Critère**|**Note**|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 84 945 au 16 novembre 2026._

**Commentaire :** projet très actif, publié par HeyGen (éditeur de vidéo IA) et présenté comme déjà utilisé en production chez HeyGen, avec une architecture relativement complète : core, engine, producer, CLI, Studio, SDK, player, rendering distribué et Skills. Le dépôt comptait plus de 4 600 commits au 22 septembre 2026 et continue de recevoir des releases très fréquentes.

L'API et certains composants restent néanmoins en version `0.x`, et le projet évolue rapidement ; la maturité est notée ★★☆☆☆ car il dispose de beaucoup moins d'historique, de templates et de retours de production indépendants que [[Remotion]] (voir [[#Avis indépendants|les avis indépendants]]). La documentation est abondante mais certaines parties sont encore très liées aux conventions propres à HyperFrames et à son écosystème de Skills.

### Points forts

- **Approche agent-first native** : les Skills décrivent explicitement le workflow de production et permettent à un agent de piloter la création vidéo de bout en bout.
    
- **HTML/CSS comme langage de composition**, ce qui rend le système particulièrement accessible aux coding agents et aux développeurs web.
    
- **Déterminisme du rendering**, permettant de traiter la composition comme du code plutôt que comme une simple capture d'écran.
    
- Architecture modulaire couvrant aussi bien le rendering que l'édition, le SDK, le player et le déploiement distribué.
    
- **Studio + code + agent** : possibilité de combiner génération par agent et édition humaine.
    
- Écosystème de Skills particulièrement développé, avec des workflows allant de la vidéo produit aux explications de PR GitHub.
    
- Projet actif, avec des releases rapprochées (sa popularité est un indicateur d'attention, non de maturité).
    
- Licence **Apache-2.0**, adaptée à de nombreux usages commerciaux sous réserve des licences propres aux assets et dépendances.
    

### Limites

- Architecture fortement dépendante de **Chromium/Puppeteer et FFmpeg**, avec un coût potentiel en ressources et en temps de rendering par rapport à des moteurs graphiques natifs.
    
- Le modèle HTML/CSS est particulièrement adapté au motion design, aux vidéos explicatives et aux compositions graphiques, mais ne remplace pas nécessairement un logiciel de montage traditionnel pour des workflows vidéo très complexes.
    
- Projet encore en **version 0.x**, avec une API et des workflows susceptibles d'évoluer rapidement.
    
- L'écosystème de Skills constitue une force mais crée également une dépendance aux conventions et au workflow propres à HyperFrames.
    
- Les projets contenant de nombreux médias binaires peuvent devenir volumineux : le dépôt utilise notamment Git LFS pour ses fichiers vidéo de tests de régression.
    
- La qualité finale dépend fortement de la qualité du HTML/CSS/JS généré et donc du workflow de l'agent : l'agent écrit du code rendu image par image, les résultats peuvent paraître basiques sans direction artistique, et le débogage d'animations web reste du développement.

- **Peu de retours de production indépendants** : l'essentiel des comparaisons avec Remotion provient de contenus d'éditeurs ou de développeurs enthousiastes ; Remotion reste plus rassurant pour une infrastructure vidéo React déjà industrialisée.
    

## Relations

- **Complémentaire de :** [[Claude Code]], [[OpenAI Codex]], [[Cursor]]
    
- **Alternative à :** [[Remotion]]
    
- **S'intègre avec :** Claude Code · Codex · Cursor · Gemini CLI · Puppeteer · FFmpeg · GSAP · Three.js
    
- **Utilise :** HTML · CSS · JavaScript/TypeScript · Chromium/Puppeteer · FFmpeg
    
- **Inspiration / écosystème proche :** [[Remotion]]
    
- **Écosystème associé :** [[HyperFrames Community Skills]]
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Les premiers utilisateurs apprécient de pouvoir créer une vidéo avec les technologies web que les agents maîtrisent déjà : HTML, CSS, JavaScript et GSAP. La prévisualisation rapide et les workflows prêts à l’emploi rendent la vidéo programmatique plus accessible, notamment pour les vidéos produit et les motion graphics.

Les retours rappellent que HyperFrames ne génère pas magiquement une vidéo : l’agent écrit du code qui est rendu image par image. Les résultats peuvent paraître basiques sans direction artistique, et le débogage d’animations web reste du développement. Le projet a beaucoup moins d’historique, de templates et de retours de production que Remotion.

### Comparaison

Remotion offre un modèle React déterministe par frame, un écosystème mûr et davantage de contrôle pour les pipelines data-driven. HyperFrames favorise le HTML standard et les bibliothèques d’animation familières aux modèles. CapCut ou After Effects restent meilleurs pour le montage manuel et la finition visuelle.

### Verdict

Excellent choix pour laisser un agent produire rapidement une vidéo web éditable ; Remotion reste plus rassurant pour une infrastructure vidéo React déjà industrialisée.

## Sources

- [GitHub](https://github.com/heygen-com/hyperframes)
    
- [Website](https://hyperframes.heygen.com/)
    
- [Documentation](https://hyperframes.heygen.com/)
    
- [HyperFrames Launches](https://github.com/heygen-com/hyperframes-launches)
    

### Sources des avis

- [Retour comparatif Remotion/HyperFrames](https://www.reddit.com/r/heygen/comments/1snl38i/hyperframes_opensource_framework_that_turns_html/)
- [Verdict développeur](https://autoae.online/blog/hyperframes-vs-remotion-developer-verdict)
- [Revue indépendante](https://andrew.ooo/posts/hyperframes-heygen-html-video-agents-review/)

_Dernière analyse : 12 novembre 2026_