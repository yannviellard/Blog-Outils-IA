---
title: "Web Design Guidelines"
type: outil
description: "Audit sémantique de plus de cent règles UI, accessibilité et performance."
format: skill
tags:
  - metier/produit-design
  - theme/frontend
  - theme/accessibilite
editeur: "Vercel"
site: "https://skills.sh/vercel-labs/agent-skills"
depot: "https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md"
licence: "MIT"
statut: disponible
derniere_maj: 2026-01-16
note_documentation: 4
note_precision: 4
note_maturite: 3
memo: "[[Web Design Guidelines mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Web Design Guidelines

> Skill officielle de Vercel qui audite du code d'interface web par rapport à plus de 100 règles de bonnes pratiques (accessibilité, focus, formulaires, animation, typographie, performance, i18n…) issues des « Web Interface Guidelines » de Vercel, et restitue les manquements au format concis `fichier:ligne` directement exploitable.

**Composition** : 1 skill, de la collection `vercel-labs/agent-skills`.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Web Design Guidelines mémo]] pour le mémo pratique.

## Résumé

`web-design-guidelines` est l'une des skills de la collection officielle `vercel-labs/agent-skills`, déclenchée par des demandes comme « review my UI », « check accessibility » ou « audit design ». Son fonctionnement est volontairement minimal côté skill : le fichier `SKILL.md` ne contient pas lui-même la liste des règles, mais instruit l'agent d'aller récupérer à chaque revue la version la plus à jour du référentiel via `WebFetch`, depuis le dépôt [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines). Ce choix garantit que l'audit utilise toujours les règles les plus récentes plutôt qu'une copie figée au moment de l'installation de la skill.

Le référentiel ainsi récupéré (`command.md`) couvre seize catégories : accessibilité, états de focus, formulaires, animation, typographie, gestion du contenu, images, performance, navigation & état, tactile & interaction, zones sûres & mise en page, mode sombre & thématisation, locale & i18n, sécurité d'hydratation, états au survol, et contenu/copywriting. Chaque catégorie liste des règles très concrètes et vérifiables (ex. « bouton icône seul → `aria-label` obligatoire », « jamais `transition: all` », « `Intl.DateTimeFormat` plutôt qu'un format de date codé en dur »), accompagnées d'une liste explicite d'anti-patterns à signaler.

Le format de sortie est délibérément terse et actionnable : les résultats sont groupés par fichier, au format `fichier:ligne — problème`, cliquable dans VS Code, sans préambule ni justification sauf si le correctif n'est pas évident — une conception pensée pour maximiser le rapport signal/bruit dans le contexte d'un agent de code plutôt que produire un rapport verbeux.

## Fonctionnalités

- **Récupération dynamique des règles** : `WebFetch` du fichier `command.md` du dépôt `vercel-labs/web-interface-guidelines` à chaque revue, plutôt qu'une copie statique embarquée dans la skill.

- **Plus de 100 règles réparties en catégories** : accessibilité (labels ARIA, HTML sémantique, gestion clavier), focus (états visibles, `:focus-visible`), formulaires (`autocomplete`, types d'input, gestion d'erreurs), animation (`prefers-reduced-motion`, propriétés compositor-friendly), typographie (guillemets courbes, points de suspension, `tabular-nums`), images (dimensions explicites, lazy loading), performance (virtualisation, lecture de layout hors du render, `preconnect`), navigation & état (URL reflétant l'état, deep-linking), tactile (`touch-action`, `overscroll-behavior`), zones sûres (`env(safe-area-inset-*)`), thématisation (`color-scheme`, `theme-color`), i18n (`Intl.DateTimeFormat`/`Intl.NumberFormat`), hydratation (cohérence serveur/client) et contenu/copywriting (voix active, libellés de bouton spécifiques).

- **Liste d'anti-patterns explicite** : détecte des motifs récurrents comme `user-scalable=no`, `onPaste` avec `preventDefault`, `<div onClick>` à la place d'un `<button>`, `outline-none` sans remplacement de focus, ou GIF animé là où une vidéo compressée conviendrait.

- **Sortie normalisée et actionnable** : résultats groupés par fichier au format `fichier:ligne — problème`, avec un simple `✓ pass` pour les fichiers conformes, sans justification superflue.

- **Argument de fichier/pattern** : la skill accepte un fichier ou un pattern à auditer (`argument-hint: <file-or-pattern>`), ou demande à l'utilisateur quels fichiers revoir si aucun n'est fourni.

## Analyse
|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|—|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité non notée : l'outil est un sous-dossier du dépôt `vercel-labs/agent-skills`, dont les étoiles mesurent l'ensemble._

### Points forts

- **Règles concrètes et vérifiables plutôt que des principes vagues** : chaque item est formulé comme un test binaire (présence d'un attribut, propriété CSS spécifique, appel d'API), ce qui le rend directement actionnable par un agent de code.

- **Référentiel à jour** grâce à la récupération dynamique des règles depuis le dépôt source, évitant qu'une skill installée devienne obsolète ; le revers est que le résultat dépend de la version du jour et que le référentiel distant est une entrée à considérer comme non figée.

- **Couverture inhabituellement large** pour une skill de revue UI : au-delà de l'accessibilité classique, elle couvre l'i18n, l'hydratation React/Next.js, les zones sûres mobiles, le mode sombre et même le copywriting.

- **Format de sortie optimisé pour l'usage en agent de code** : `fichier:ligne` cliquable, terse, sans bruit — conçu pour être lu et corrigé rapidement plutôt que pour produire un rapport à présenter tel quel.

- **Maintenue par Vercel** au sein d'une collection de skills officielle activement développée (26+ contributeurs).

### Limites

- **Dépendance à une ressource externe à chaque exécution** : la skill ne fonctionne pas hors ligne et son comportement dépend entièrement de la disponibilité et du contenu du dépôt `vercel-labs/web-interface-guidelines`, qui n'est pas versionné de façon figée dans la skill elle-même.

- **Orientation forte vers l'écosystème React/Next.js/Tailwind** : plusieurs règles (hydratation, `next/link`, JSX) sont moins pertinentes pour des projets hors de cette stack.

- **Pas de vérification automatisée (lint/AST)** : l'audit repose sur la lecture du code par le modèle plutôt que sur des règles ESLint ou un outil statique, avec le risque de faux négatifs sur du code complexe.

- **SKILL.md très minimal en lui-même** : toute la valeur réside dans le référentiel externe, ce qui rend la fiche de la skill peu informative sans consulter `command.md` séparément.

- **Revue statique, pas un test navigateur** : ni comparateur de captures, ni scanner WCAG complet ; un problème visible seulement à l'exécution peut échapper à l'audit, et certaines conventions peuvent ne pas convenir au contexte. À intégrer avant les tests navigateur, pas à leur place.

- **Récupération et exécution d'instructions distantes à chaque revue** : le contenu du référentiel n'est pas épinglé ; à traiter comme une entrée externe (reproductibilité, injection) et à figer si la revue doit être auditée.

### Qualité

**Commentaire :** skill remarquablement bien conçue dans son principe (déléguer les règles à un référentiel externe toujours à jour, sortie ultra-actionnable) et dans le contenu du référentiel lui-même (règles précises, anti-patterns explicites). La maturité reste légèrement en retrait uniquement parce que la collection `agent-skills` est plus jeune que d'autres écosystèmes de skills.

## Relations

- **Alternative à :** audits d'accessibilité manuels, plugins ESLint a11y, axe-core, Lighthouse et WAVE (qui testent le DOM rendu avec des règles automatisées)

- **Complémentaire de :** [[Playwright]] (vérification des interactions), [[Impeccable]] (qualité visuelle) ; à ne pas confondre avec [[Taste Skill]], qui oriente la génération plutôt que l'audit

- **S'intègre avec :** [[Claude Code]], Cursor, tout agent supportant le format Agent Skills

- **Utilise :** [vercel-labs/web-interface-guidelines](https://github.com/vercel-labs/web-interface-guidelines) (référentiel de règles), `WebFetch`

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

La skill est appréciée pour son audit concis et directement actionnable, avec références fichier/ligne. Le chargement dynamique du référentiel garantit des règles récentes et couvre beaucoup de défauts fréquents : accessibilité, focus, formulaires, motion, performance, i18n et hydratation.

Sa portée doit être comprise : c’est une revue statique guidée par un corpus, pas un navigateur de test, un comparateur de screenshots ni un scanner WCAG complet. Elle peut manquer un problème visible seulement à l’exécution et signaler des conventions qui ne conviennent pas au contexte. La récupération distante des règles rend aussi le résultat dépendant de leur version du jour.

### Comparaison

axe-core, Lighthouse et WAVE testent le DOM rendu avec des règles automatisées ; Playwright vérifie les interactions ; Impeccable traite davantage la qualité visuelle. Web Design Guidelines excelle comme première revue de code large et peu coûteuse.

### Verdict

Un excellent linter sémantique assisté par agent ; à intégrer avant les tests navigateur, pas à leur place.

## Sources

- [SKILL.md](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)

- [Dépôt vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills)

- [Référentiel des règles (command.md)](https://github.com/vercel-labs/web-interface-guidelines)

### Sources des avis

- [Référentiel officiel Vercel](https://vercel.com/design/guidelines)
- [Analyse de la skill et de ses limites](https://skill-road.com/en/skills/web-design-guidelines)
- [Panorama des outils d’accessibilité web](https://en.wikipedia.org/wiki/Web_accessibility)

_Dernière analyse : 12 novembre 2026_
