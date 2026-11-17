---
title: "Google Stitch"
type: outil
description: "Exploration prompt-to-UI et export vers code ou Figma."
format: application
tags:
  - metier/produit-design
  - theme/design-system
  - theme/frontend
  - theme/mcp
editeur: "Google Labs"
logo: "[[stitch.png]]"
site: "https://stitch.withgoogle.com/"
depot: "https://github.com/google-labs-code/stitch-sdk"
licence: "Apache-2.0"
statut: preversion
derniere_maj: 2026-11-05
note_documentation: 4
note_precision: 3
note_maturite: 2
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Google Stitch

> Plateforme de conception d'interfaces UI/UX propulsée par les modèles Gemini de Google Labs, permettant de générer, annoter et convertir des prototypes interactifs en code ou en assets Figma.

**Composition** : 8 skills, 2 agents, 6 outils MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves.

## Résumé

Développé par Google Labs, **Google Stitch** est un outil de conception d'interfaces utilisateur (vibe design / generative UI) basé sur l'IA. Il transforme des descriptions textuelles, des captures d'écran ou des croquis en prototypes web et mobiles. Le dépôt référencé ci-dessus est celui du SDK (`stitch-sdk`), pas celui du produit lui-même, qui reste propriétaire.

Positionné à la frontière entre le design UI et le développement front-end, Stitch s'intègre au workflow des développeurs via un SDK dédié (`@google/stitch-sdk`), un serveur MCP (Model Context Protocol) et un ensemble d'Agent Skills (`google-labs-code/stitch-skills`). Il permet ainsi d'orchestrer la génération de designs directement depuis des assistants de code IA (Claude Code, Cursor, Gemini CLI).

## Fonctionnalités

- **Génération UI multi-modale :** création d'écrans web et mobiles à partir de prompts textuels, de maquettes manuscrites ou de captures d'écran.

- **Annotation interactive & édition multimodale :** sélection visuelle d'éléments de l'interface pour appliquer des modifications ciblées en langage naturel.

- **Export vers code et Figma :** exportation vers Figma (calques éditables avec Auto-Layout) ou vers du code (HTML/CSS, React, React Native).

- **Écosystème MCP & SDK :** intégration via serveur MCP et SDK Node.js/TypeScript pour permettre aux agents IA de générer, modifier et synchroniser des interfaces.

## Analyse
|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|—|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité non notée : le dépôt public `google-labs-code/stitch-sdk` est un SDK annexe, pas le produit._

### Points forts

- **Idéation rapide prompt-to-UI** : entrée texte, image ou voix, écrans multiples et export vers le code ou Figma permettent d'obtenir en quelques minutes une direction suffisamment concrète pour discuter et tester, notamment pour un développeur solo ou un atelier 0→1.

- **Intégration aux workflows d'agents** : le serveur MCP et le SDK (`@google/stitch-sdk`) simplifient le pont entre design et code pour les assistants de code.

- **Export Figma** : annoncé comme respectant les calques éditables et les contraintes Auto-Layout ; la fidélité sur des écrans complexes reste à vérifier au cas par cas.

### Limites

- **Génération d'écrans, pas système de design** : le résultat nécessite souvent une reprise pour la marque, l'accessibilité, les états complexes et la cohérence entre composants ; le code généré doit être vérifié avant production.

- **Collaboration et handoff** : l'export amélioré ne remplace pas Figma pour les composants, variantes, commentaires et la collaboration d'équipe ; v0 et Lovable vont plus loin vers une application fonctionnelle.

- **Statut expérimental :** produit issu de Google Labs, encore sujet à de fréquentes évolutions de fonctionnalités et d'API.

- **Quotas de génération :** limitation sur les modes standard et expérimentaux dans sa version bêta gratuite.

- **Dépendance à l'écosystème Gemini :** moins personnalisable au niveau du choix des modèles LLM sous-jacents.

### Qualité

**Commentaire :** Google Stitch propose une documentation claire et des SDK bien structurés pour l'intégration agentique. La maturité reste intermédiaire en raison du statut de projet Google Labs en bêta. Les affirmations de rendus « haute fidélité » ou d'export « avancé » relèvent de la communication de l'éditeur ; les comparatifs indépendants décrivent un excellent outil d'exploration de directions et de prototypes, à transférer dans un vrai design system pour la production.

## Relations

- **Alternative à :** [[Figma]] (resté l'environnement de collaboration et de handoff), Figma Make, [[v0.dev]], Lovable, [[Claude Design]], [[Penpot]]

- **S'intègre avec :** [[Figma]], [[Cursor]], [[Claude Code]], [[Google Agent Development Kit]]

- **Utilise :** [[Gemini API]], [[Model Context Protocol|MCP Protocol]]

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Stitch est apprécié pour la rapidité de l’idéation prompt-to-UI, l’entrée texte/image/voix, les écrans multiples et l’export vers code ou Figma. Pour un développeur solo ou un atelier 0→1, il permet d’obtenir en quelques minutes une direction suffisamment concrète pour discuter et tester.

Les retours insistent sur la différence entre génération d’écrans et système de design. Le résultat nécessite souvent une reprise pour la marque, l’accessibilité, les états complexes et la cohérence entre composants. En tant que produit Labs, limites et comportement changent vite. L’export amélioré ne remplace pas encore l’ensemble de la collaboration Figma.

### Comparaison

Figma reste le « design OS » pour composants, variantes, commentaires et handoff. Figma Make ajoute la génération dans ce cadre, avec des crédits. v0 et Lovable vont plus loin vers une application fonctionnelle. Stitch se positionne entre idéation visuelle et génération de code, avec une barrière d’entrée basse.

### Verdict

Excellent pour explorer des directions et créer un prototype ; pour la production, transférer dans un vrai design system et vérifier le code généré.

## Sources

- [GitHub](https://github.com/google-labs-code/stitch-sdk)

- [Website](https://stitch.withgoogle.com/)

### Sources des avis

- [Test Stitch vs Figma Make](https://0xminds.com/blog/guides/google-stitch-vs-figma-make-2026-vibe-coding)
- [Comparatif Stitch, v0, Lovable et Figma Make](https://brainy.ink/paper/google-stitch-for-designers)
- [Analyse Stitch vs Figma](https://versustool.com/google-stitch-vs-figma)

_Dernière analyse : 12 novembre 2026_
