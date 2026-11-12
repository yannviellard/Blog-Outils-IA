---
title: "Frontend Design — Mémo"
type: memo
fiche: "[[FrontEnd Design]]"
date: 2026-09-25
---

# Frontend Design — Mémo

> L'essentiel pour utiliser [[FrontEnd Design]], la skill officielle d'Anthropic qui pousse Claude à concevoir des interfaces distinctives plutôt que des pages « template ». Elle n'a pas de commande : elle se déclenche seule, et **la qualité du résultat dépend surtout du brief que tu donnes**.

## Installation

```bash
# Claude Code (marketplace du dépôt anthropics/claude-code)
/plugin marketplace add anthropics/claude-code
/plugin install frontend-design@claude-code-plugins
/plugin list                      # vérifier

# Autres agents, via le standard Agent Skills
npx skills add anthropics/skills --skill frontend-design
```

## Comment elle travaille

1. **Identifier le sujet** : quel produit, pour qui, pour faire quoi. Si le brief ne le dit pas, Claude propose une hypothèse et la fait confirmer.
2. **Plan en tokens** : 4 à 6 couleurs nommées (hex), les polices et leur rôle, un concept de mise en page (avec wireframes ASCII), quelques principes.
3. **Relecture du plan** : tout ce qui ressemble à un choix par défaut est révisé, avec explication.
4. **Construction**, puis **autocritique** avec captures d'écran si l'environnement le permet.

## Écrire un bon brief

|Élément|Exemple|
|---|---|
|Sujet et public|« Site d'une brasserie artisanale pour des amateurs de bière de 25–45 ans »|
|Direction visuelle|« Brutaliste, typographie mono, fond presque noir, accent vert »|
|Contraintes|« Next.js + Tailwind, une seule page, mobile d'abord »|
|À éviter|« Pas de dégradé violet, pas d'Inter, pas de grille de cartes identiques »|
|Contenu réel|Textes, chiffres, noms de produits : un contenu fictif rend la page générique.|

Un prompt générique donne un résultat générique, même avec la skill.

## Les « signes IA » que la skill cherche à éviter

- Fond crème + serif contrasté + accent terracotta (très proche de la charte de Claude elle-même)
- Fond presque noir + un seul accent vert acide ou vermillon
- Mise en page « journal » avec filets fins et colonnes denses
- Le kit SaaS : cartes arrondies identiques, même ombre grise partout, dégradés décoratifs
- Petits libellés EN CAPITALES au-dessus de chaque titre, séparateurs « A · B · C », flèches « → » sur les boutons
- Un seul mot en italique ou en couleur dans le titre, numérotation « 01 / 02 / 03 » sur un contenu qui n'est pas une suite
- Animations d'apparition sur chaque section au lieu d'un seul moment orchestré

Si ton brief demande explicitement l'un de ces styles, la skill le suit : le brief l'emporte toujours.

## Conseils d'utilisation

- **Concentrer l'audace sur un seul élément** et garder le reste sobre.
- **Demander le plan avant le code** (« montre-moi d'abord ta palette, tes polices et ta mise en page ») pour corriger la direction à moindre coût.
- **Ne pas l'utiliser avec un design system existant** (Material UI, charte d'entreprise) : elle cherche la singularité et casse la cohérence. Préférer alors [[UI UX Pro Max]] ou le design system de [[Claude Design]].
- **Inutile pour une petite retouche** d'un seul élément.
- **Exigences de base à vérifier** : responsive jusqu'au mobile, focus clavier visible, `prefers-reduced-motion` respecté, contrastes suffisants.

## Sources

- [SKILL.md frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
- [Improving frontend design through Skills — blog Anthropic](https://claude.com/blog/improving-frontend-design-through-skills)
- [Frontend Design Skill — wmedia.es](https://wmedia.es/en/tips/claude-code-frontend-design-skill)
- [Prompting for frontend aesthetics — Claude Cookbooks](https://github.com/anthropics/claude-cookbooks/blob/main/coding/prompting_for_frontend_aesthetics.ipynb)
