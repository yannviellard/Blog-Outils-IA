---
title: "UI/UX Pro Max"
type: outil
description: "Base locale de styles, palettes, typographies, règles UX et recommandations par stack."
format: skill
tags:
  - metier/produit-design
  - theme/design-system
  - theme/accessibilite
  - theme/frontend
editeur: "nextlevelbuilder"
site: "https://uupm.cc/"
depot: "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-10
etoiles: 148098
forks: 15670
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 5
memo: "[[UI UX Pro Max mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# UI/UX Pro Max

> Skill de **design intelligence** pour les assistants de programmation IA. Il fournit une base de connaissances recherchable couvrant les styles UI, palettes de couleurs, typographies, guidelines UX, icônes, graphiques et bonnes pratiques spécifiques aux stacks, afin d'aider un agent à concevoir, implémenter, auditer et améliorer des interfaces.

**Composition** : 1 skill, compatible avec 20+ plateformes.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[UI UX Pro Max mémo]] pour le mémo pratique.

## Résumé

UI/UX Pro Max transforme une base de connaissances de design en **skill exploitable directement par les coding agents**. Le workflow repose sur une analyse du contexte du produit, une recherche dans des données structurées, la génération de recommandations cohérentes puis l'application de guidelines spécifiques à la technologie utilisée.

Le projet fournit notamment **79 styles UI, 192 palettes, 74 associations typographiques, 119 guidelines UX, 105 icônes, 17 presets GSAP, 25 types de graphiques et 22 stacks technologiques** dans sa configuration actuelle.

Il ne s'agit donc pas d'un simple prompt de génération d'interfaces : le cœur du projet est constitué de **données structurées + scripts de recherche + instructions de skill**, permettant à l'agent de sélectionner des recommandations en fonction du contexte plutôt que de tout charger dans son contexte à chaque requête.

## Fonctionnalités

- **Base de connaissances UI/UX recherchable** couvrant styles, couleurs, typographie, UX, icônes, charts et patterns.
    
- **Génération de design systems** à partir du type de produit, de l'industrie, du style recherché et de la stack technique.
    
- **Guidelines UX et accessibilité** destinées à guider la conception et la revue des interfaces.
    
- **Recommandations spécifiques aux stacks**, notamment React, Next.js, Vue, Svelte, Tailwind, shadcn/ui, SwiftUI, React Native, Flutter, Jetpack Compose et Three.js.
    
- **Workflow de recherche local** basé sur des fichiers de données et un script `search.py`.
    
- **Compatibilité multi-agents** : Claude Code, Codex, Cursor, Windsurf, GitHub Copilot, Roo Code, Gemini, OpenCode et de nombreuses autres plateformes.
    
- **CLI d'installation** permettant de déployer le skill sur différentes plateformes via `ui-ux-pro-max-cli`.
    
- **Démos et exemples visuels** accessibles depuis le site officiel, avec des exemples par secteur, style et mode clair/sombre.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Richesse du référentiel|★★★★☆|
|Qualité des recommandations|★★★★☆|
|Architecture du skill|★★★★☆|
|Multi-plateforme|★★★★★|
|Maturité|★★★☆☆|
|Popularité|★★★★★|
|Maintenabilité|★★★★☆|
|Intégration coding agents|★★★★★|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 148 098 au 11 novembre 2026._

**Commentaire :** projet particulièrement intéressant parce qu'il dépasse le simple prompt engineering : il combine **skill, données structurées, moteur de recherche local et templates spécifiques aux agents**. L'architecture permet de maintenir une base de connaissances relativement volumineuse sans injecter l'intégralité du contenu dans le contexte de l'agent. Le projet reste néanmoins en évolution rapide : le dépôt affiche encore plusieurs dizaines d'issues et de pull requests ouvertes, dont certaines concernent l'installation, le packaging et la synchronisation des métadonnées.

### Points forts

- **Base de connaissances structurée**, avec des centaines d'éléments directement exploitables par un agent ; la quantité (styles, palettes, associations) donne une impression d'exhaustivité qui ne remplace ni un designer, ni la recherche utilisateur, ni des tests visuels.
    
- **Recherche contextuelle** plutôt qu'un simple long prompt statique.
    
- **Approche orientée design system**, permettant de maintenir une cohérence entre les différentes décisions UI.
    
- **Large couverture technologique**, incluant aussi bien les frameworks web que les technologies mobiles comme SwiftUI.
    
- **Très bonne compatibilité avec les coding agents**, avec des templates dédiés à de nombreuses plateformes, dont Codex.
    
- **Open source sous licence MIT**.
    
- **Projet actif**, avec des releases et une adoption large ; ces indicateurs d'attention ne mesurent pas la qualité des recommandations.
    
- **Politique de sécurité explicite**, couvrant notamment l'installation CLI, les écritures de fichiers et la supply chain npm.
    

### Limites

- **Risque de standardisation esthétique** : une base de styles et de patterns peut conduire un agent à produire des interfaces cohérentes mais relativement prévisibles si elle est utilisée sans direction artistique propre.
    
- **Volume important de données** : la richesse du référentiel augmente la dépendance à la qualité du moteur de recherche et de la sélection des recommandations.
    
- **Projet en évolution rapide** : certaines fonctionnalités et métadonnées changent encore fréquemment.
    
- **Quelques problèmes de packaging/intégration** subsistent dans l'écosystème multi-plateforme ; une issue récente signale notamment des chemins `~/.claude` codés en dur et des références à des composants non embarqués.
    
- **Ce n'est pas un outil de conception graphique collaboratif** : il complète des outils comme Figma ou Claude Design plutôt que de les remplacer.
    
- **Pas de MCP proprement dit** : son fonctionnement repose principalement sur un skill, des données locales et des scripts de recherche plutôt que sur un serveur MCP.

- **Guide des décisions sans garantir le résultat** : une palette cohérente et des règles correctes peuvent toujours produire une interface banale ou mal hiérarchisée ; la base doit aussi être maintenue au rythme des évolutions des frameworks. À associer à une direction de marque et à une vraie boucle de revue visuelle.
    

## Relations

- **Alternative à :** autres skills de design UI/UX destinés aux coding agents
    
- **S'intègre avec :** Claude Code · Codex · Cursor · Windsurf · GitHub Copilot · OpenCode · Gemini CLI · Roo Code
    
- **Utilise :** base de données locale UI/UX · `search.py` · templates spécifiques aux plateformes
    

## Positionnement

UI/UX Pro Max se situe davantage dans la catégorie **« design knowledge / design intelligence »** que dans celle des outils de prototypage.

```text
Design knowledge
       │
       ▼
┌──────────────────┐
│ UI/UX Pro Max    │
│ styles           │
│ colors           │
│ typography       │
│ UX guidelines    │
│ design systems   │
└────────┬─────────┘
         │
         ▼
   Coding Agent
         │
    ┌────┴────┐
    ▼         ▼
  Web       Mobile
    │         │
    ▼         ▼
React      SwiftUI
```

Il est donc particulièrement adapté lorsqu'un agent doit **prendre des décisions UI/UX cohérentes directement pendant le développement**, plutôt que lorsqu'un designer souhaite produire et éditer manuellement des maquettes.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Les avis sont globalement positifs sur sa base de connaissances recherchable : styles, palettes, associations typographiques, règles UX, graphiques et recommandations par stack donnent à l’agent des choix justifiables sans charger tout le corpus. Sa portabilité et son fonctionnement local sont également appréciés.

La principale limite est qu’il guide des décisions sans garantir un bon résultat final. Une palette cohérente et des règles correctes peuvent toujours produire une interface banale ou mal hiérarchisée. Certains chiffres et listes donnent une impression d’exhaustivité qui ne remplace pas un designer, une recherche utilisateur ou des tests visuels. L’outil doit aussi être maintenu avec les évolutions des frameworks.

### Comparaison

Frontend Design est plus léger et créatif pour le premier écran ; Taste pousse l’expérimentation ; Impeccable améliore l’existant ; Web Design Guidelines audite des règles de qualité. UI/UX Pro Max est le plus proche d’un assistant de design system fondé sur une base structurée.

### Verdict

Très bon socle pour rendre les choix UI plus cohérents et explicites ; à associer à une direction de marque et une vraie boucle de revue visuelle.

## Sources

- [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
    
- [UI/UX Pro Max](https://uupm.cc/)
    
- [Skill definition](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md)
    
- [GitHub Releases](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/releases)
    
- [Security Policy](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/security)
    

### Sources des avis

- [Revue dédiée de UI/UX Pro Max](https://skiln.co/blog/ui-ux-pro-max-skill-review)
- [Comparaison de skills UI/UX](https://www.softwarethug.com/posts/claude-code-ui-design-skills-compared/)
- [Analyse sans le discours promotionnel](https://mrkeyoor.com/repos/ui-ux-pro-max-skill/)

_Dernière analyse : 12 novembre 2026_