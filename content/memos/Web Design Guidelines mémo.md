---
title: "Web Design Guidelines — Mémo"
type: memo
fiche: "[[Web Design Guidelines]]"
date: 2026-09-25
---

# Web Design Guidelines — Mémo

> L'essentiel pour utiliser [[Web Design Guidelines]], la skill de Vercel qui audite du code d'interface selon plus de 100 règles (accessibilité, focus, formulaires, animation, typographie, performance, i18n…). Elle rend une liste de problèmes au format `fichier:ligne`, cliquable dans VS Code.

## Installation

```bash
npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines
```

Fonctionne avec Claude Code, Codex, Cursor et tout agent compatible Agent Skills. L'agent doit avoir accès au web : à chaque audit, la skill télécharge la dernière version des règles.

## Comment la déclencher

Aucune commande à retenir : ces phrases la déclenchent.

- « Review my UI » / « Revois mon interface »
- « Check accessibility » / « Vérifie l'accessibilité »
- « Audit design » / « Review UX »
- « Check my site against best practices »

On peut cibler des fichiers : « Audite `src/components/**/*.tsx` avec les web design guidelines ». Sans cible, la skill demande quels fichiers revoir.

## Ce qu'elle vérifie

|Catégorie|Exemples de règles|
|---|---|
|Accessibilité|Bouton icône sans `aria-label`, `<div onClick>` au lieu de `<button>`, images sans `alt`|
|Focus|`outline-none` sans remplacement, `:focus-visible` plutôt que `:focus`|
|Formulaires|`autocomplete` manquant, collage bloqué, erreurs affichées loin du champ|
|Animation|`prefers-reduced-motion` ignoré, `transition: all`|
|Typographie|`...` au lieu de `…`, guillemets droits, chiffres non tabulaires dans les colonnes|
|Images|`width`/`height` manquants (décalage de mise en page), lazy loading|
|Performance|Longues listes non virtualisées, lectures de layout pendant le rendu|
|Navigation et état|Filtres ou onglets absents de l'URL, action destructrice sans confirmation|
|Thème sombre|`color-scheme` absent, `<select>` natif illisible sous Windows|
|i18n|Dates et nombres formatés en dur au lieu de `Intl.*`|
|Contenu|Voix passive, libellés vagues (« Continuer » au lieu de « Enregistrer la clé API »)|

## Format de sortie

```text
## src/Button.tsx
src/Button.tsx:42 - icon button missing aria-label
src/Button.tsx:55 - animation missing prefers-reduced-motion

## src/Card.tsx
✓ pass
```

## Conseils d'utilisation

- **Auditer par petits lots de fichiers** (un dossier de composants à la fois) : les résultats restent précis et le contexte reste léger.
- **Demander ensuite la correction** : « Corrige tous les problèmes trouvés dans `Button.tsx` ».
- **Adapter les règles à ta stack** : plusieurs règles visent React/Next.js (hydratation, `next/link`) et comptent moins ailleurs.
- **Ce n'est pas un linter** : c'est le modèle qui lit le code. Pour une garantie en CI, compléter avec `eslint-plugin-jsx-a11y` ou le détecteur d'[[Impeccable]].
- **Règles consultables** sur [vercel.com/design/guidelines](https://vercel.com/design/guidelines), utile pour comprendre un signalement.

## Sources

- [SKILL.md web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md)
- [Web Interface Guidelines (règles)](https://github.com/vercel-labs/web-interface-guidelines)
- [Web Interface Guidelines — Vercel](https://vercel.com/design/guidelines)
