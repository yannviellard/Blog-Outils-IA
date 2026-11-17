---
title: "Huashu Design"
type: outil
description: "Workflow design-as-code ouvert avec exploration de plusieurs directions visuelles."
format: skill
tags:
  - metier/produit-design
  - theme/design-system
  - theme/frontend
  - theme/video
editeur: "alchaincyf"
site: "https://www.huasheng.ai/"
depot: "https://github.com/alchaincyf/huashu-design"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-10
etoiles: 29629
forks: 3178
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 3
note_maturite: 2
note_popularite: 4
memo: "[[Huashu Design mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Huashu Design

> **Huashu Design** est un Skill de design agentique qui permet à Claude Code, Codex, Cursor et d'autres agents de produire des prototypes haute fidélité, présentations HTML/PPTX, animations, infographies et variantes de design directement en HTML/CSS/JS. Il impose notamment l'exploration de trois directions visuelles avant la réalisation finale.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Huashu Design mémo]] pour le mémo pratique.

## Résumé

Huashu Design transforme un agent de code en **designer/mini studio de production visuelle**. Le Skill ne se limite pas à générer du HTML : il définit un workflow complet comprenant recherche de références, analyse des assets de marque, exploration de plusieurs directions, production, validation et critique.

Le projet est explicitement destiné aux **productions visuelles en HTML**, et non au développement d'applications Web de production, aux sites SEO ou aux systèmes nécessitant un backend.

Le workflow est **agent-agnostic** : le projet indique une compatibilité avec Claude Code, Cursor, Codex, OpenClaw et Hermes.

Le dépôt a été relicencié sous **MIT le 14 mai 2026**, supprimant les restrictions commerciales de sa précédente licence Personal Use.

## Fonctionnalités

- **Prototypes interactifs** : prototypes App/Web haute fidélité, notamment avec cadre iPhone, navigation multi-écrans et validation Playwright.
    
- **Exploration de design** : génération obligatoire de trois directions visuelles avant réalisation, avec une bibliothèque de 60 styles HTML natifs.
    
- **Design system / brand assets** : prise en compte de logos, palettes, captures UI et autres assets de marque avant conception.
    
- **Motion design** : animations pilotées par timeline avec export MP4, GIF et interpolation 60 fps.
    
- **Présentations** : decks HTML 1920×1080 convertibles en PPTX éditable.
    
- **Infographies** : compositions destinées à l'impression avec export PDF, PNG 300 dpi et SVG.
    
- **Tweaks** : exploration interactive de variantes de couleurs, typographie et densité via paramètres persistants.
    
- **5-Dimension Critique** : évaluation selon cohérence philosophique, hiérarchie visuelle, qualité d'exécution, fonctionnalité et innovation, avec sorties Keep / Fix / Quick Wins.
    
- **Workflow de Junior Designer** : hypothèses et premiers résultats présentés tôt afin de réduire le coût des erreurs de direction.
    
- **Bibliothèque de styles** : 20 styles Web, 20 styles présentation et 20 styles infographie, principalement réalisés en CSS sans génération d'image.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Richesse fonctionnelle|★★★★★|
|Qualité du workflow|★★★★☆|
|Exploration visuelle|★★★★☆|
|Prototypage|★★★★☆|
|Motion design|★★★★☆|
|Maturité|★★☆☆☆|
|Popularité|★★★★☆|
|Intégration avec les agents|★★★★☆|
|Remplacement de Figma|★★☆☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 29 629 au 16 novembre 2026._

**Commentaire :** les notes tiennent compte du fait que le projet est jeune et que plusieurs articles à son sujet reposent sur des démonstrations ou des comparaisons promotionnelles : aucune évaluation indépendante ne confirme encore la qualité des sorties. Une skill reproduit un processus, pas le modèle visuel ni l'interface collaborative d'un outil de design (voir [[#Avis indépendants|les avis indépendants]]). Huashu Design est intéressant par son approche **process-first** : le Skill ne demande pas simplement à l'agent de « faire une belle interface », mais impose une phase d'exploration, plusieurs directions visuelles, une sélection puis une production et une critique. Son périmètre est cependant volontairement centré sur les productions visuelles HTML plutôt que sur la conception graphique collaborative traditionnelle ou le développement d'applications de production.

### Points forts

- **Approche orientée processus** : le design devient une tâche orchestrée par l'agent (références, directions, production, critique) plutôt qu'une simple génération de code.
    
- **Trois directions obligatoires** avant une nouvelle conception, ce qui limite les sorties génériques et favorise l'exploration.
    
- **60 styles HTML natifs** permettant de varier réellement les directions visuelles sans dépendre de génération d'images.
    
- **Pipeline de production complet** : prototype, présentation, animation, infographie, export et critique.
    
- **Très bon support du motion design**, avec un moteur basé sur Stage/Sprite, interpolation et easing.
    
- **Validation automatisée** des prototypes via Playwright.
    
- **Interopérabilité** avec plusieurs coding agents plutôt qu'un seul environnement.
    
- **MIT**, donc utilisable et modifiable librement, y compris dans des contextes commerciaux.
    
- Architecture relativement légère : le dépôt repose principalement sur un `SKILL.md`, des références, assets et scripts, avec notamment `playwright`, `pptxgenjs`, `pdf-lib` et `sharp` côté dépendances.
    

### Limites

- **Pas un véritable outil de design graphique collaboratif** : il n'offre pas le canvas et les interactions d'un outil comme Figma.
    
- **HTML comme média de conception** : le résultat est excellent pour les prototypes et productions visuelles, mais doit être traduit vers d'autres technologies pour une application native ou un produit de production.
    
- **Périmètre explicitement limité** : le Skill déconseille les Web Apps de production, sites SEO et systèmes dynamiques nécessitant un backend.
    
- La qualité finale reste fortement dépendante des capacités de l'agent sous-jacent et de la qualité des instructions/contexte fournis.
    
- La richesse du Skill entraîne une certaine complexité : le dépôt comporte de nombreuses références, assets et scripts qui font partie intégrante du fonctionnement.
    
- Les notes de « 5 dimensions » constituent un mécanisme de critique guidée, pas une mesure objective de la qualité d'un design.

- **Licence récemment modifiée** : passée de « Personal Use » à MIT le 14 mai 2026 ; un changement de licence en moins d'un an invite à vérifier les conditions applicables avant un usage commercial.

- **Peu de recul indépendant** : jeune projet, démonstrations nombreuses, comparaisons parfois promotionnelles.
    

## Relations

- **Complémentaire de :** [[UI UX Pro Max]], [[Impeccable]], [[FrontEnd Design]]
    
- **Alternative à :** [[Claude Design]] pour une approche open source et agentique du prototypage HTML
    
- **S'intègre avec :** Claude Code, Codex, Cursor, OpenClaw, Hermes, Playwright
    
- **Utilise :** HTML · CSS · JavaScript · Playwright · PptxGenJS · PDF-Lib · Sharp
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Huashu Design est apprécié comme alternative ouverte à Claude Design : il apporte un workflow de conception directement dans Claude Code, produit des artefacts web modifiables et évite les quotas d’une preview fermée. Sa portabilité vers plusieurs agents plaît aux utilisateurs qui veulent conserver leurs fichiers et leur méthode.

Le projet reste jeune et plusieurs articles sont basés sur des démonstrations ou des comparaisons promotionnelles. Une skill reproduit un processus, pas le modèle visuel, l’interface collaborative ni tout le contrôle d’un outil de design. La qualité dépend fortement du modèle, du brief et de la capacité de l’utilisateur à critiquer le résultat.

### Comparaison

Claude Design offre une expérience intégrée et des exports plus directs ; Figma demeure supérieur pour le design system, la collaboration et le handoff ; Google Stitch excelle en idéation prompt-to-UI. Huashu Design gagne sur l’ouverture, la portabilité et l’intégration au dépôt.

### Verdict

Très intéressant pour développeurs et petites équipes qui veulent un flux design-as-code ouvert ; pas encore une validation suffisante pour remplacer l’outil de production d’une équipe design.

## Sources

- [GitHub](https://github.com/alchaincyf/huashu-design)
    
- [README](https://github.com/alchaincyf/huashu-design/blob/master/README.md)
    
- [README English](https://github.com/alchaincyf/huashu-design/blob/master/README.en.md)
    
- [SKILL.md](https://github.com/alchaincyf/huashu-design/blob/master/SKILL.md)
    
- [Huasheng](https://www.huasheng.ai/)
    

### Sources des avis

- [Test Huashu Design vs Claude Design](https://popularaitools.ai/blog/huashu-design-vs-claude-design)
- [Comparatif de prototypes UI](https://law007.me/posts/ai-ui-prototype-comparison/)
- [Analyse de l’alternative open source](https://www.synthexprompts.ai/blog/huashu-design-claude-design-alternative)

_Dernière analyse : 12 novembre 2026_