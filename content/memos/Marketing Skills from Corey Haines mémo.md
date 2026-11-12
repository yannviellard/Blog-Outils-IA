---
title: "Marketing Skills (Corey Haines) — Mémo"
type: memo
fiche: "[[Marketing Skills from Corey Haines]]"
date: 2026-09-25
---

# Marketing Skills (Corey Haines) — Mémo

> Les commandes à connaître pour [[Marketing Skills from Corey Haines]], une cinquantaine de skills marketing pour Claude Code, Codex ou Cursor : conversion, rédaction, SEO, publicité, e-mails, analytics, pricing, lancement, vente. Toutes s'appuient sur un fichier de contexte produit commun.

## Installation

```bash
# Toutes les skills, pour Claude Code
npx skills add coreyhaines31/marketingskills -a claude-code

# Seulement certaines
npx skills add coreyhaines31/marketingskills --skill cro copywriting
npx skills add coreyhaines31/marketingskills --list

# Ou en plugin Claude Code
/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills
```

## Étape 1 : le contexte produit

La skill `product-marketing` crée `.agents/product-marketing.md` : produit, public, personas, concurrence, objections, vocabulaire des clients, voix de marque. **Toutes les autres skills le lisent d'abord.** À faire une fois, au début :

> « Crée mon contexte product marketing »

## Utilisation

En langage naturel (la bonne skill se déclenche) ou directement par son nom :

|Demande|Skill utilisée|
|---|---|
|« Optimise cette landing page pour la conversion »|`/cro`|
|« Écris le texte de la page d'accueil de mon SaaS »|`/copywriting`|
|« Configure le suivi GA4 des inscriptions »|`/analytics`|
|« Crée une séquence de bienvenue en 5 e-mails »|`/emails`|
|« Fais un audit SEO de mon site »|`/seo-audit`|

## Les skills par catégorie

|Catégorie|Skills|
|---|---|
|Conversion|`cro` (pages et formulaires), `signup`, `onboarding`, `popups`, `paywalls`|
|Contenu et rédaction|`copywriting`, `copy-editing`, `cold-email`, `emails`, `social`, `image`, `video`, `sms`|
|SEO|`seo-audit`, `ai-seo` (visibilité dans les réponses des IA), `programmatic-seo`, `site-architecture`, `schema`, `competitors` (pages de comparaison)|
|Publicité et diffusion|`ads`, `ad-creative`, `events`, `influencer-marketing`, `public-relations`, `directory-submissions`|
|Mesure|`analytics`, `ab-testing`, `attribution`|
|Rétention et croissance|`churn-prevention`, `referrals`, `free-tools`, `lead-magnets`, `co-marketing`, `community-marketing`|
|Stratégie|`marketing-plan`, `marketing-ideas`, `marketing-psychology`, `launch`, `pricing`, `offers`, `customer-research`, `marketing-council`|
|Vente|`revops`, `sales-enablement`, `prospecting`, `competitor-profiling`|

## Conseils d'utilisation

- **Remplir le contexte produit avant tout** : sans lui, les résultats restent génériques ; avec lui, chaque skill respecte ton positionnement.
- **Enchaîner les skills liées** : `customer-research` → `copywriting` → `cro` → `ab-testing`, ou `seo-audit` → `schema` → `ai-seo`.
- **N'installer que ce qui sert** (`--skill`) si tu ne fais qu'une partie du marketing.
- **Migration depuis la v1** : 17 skills ont été renommées (ex. `page-cro` → `cro`) ; supprimer les anciens dossiers pour éviter les doublons, et déplacer le fichier de contexte de `.claude/` vers `.agents/product-marketing.md`.
- **Avis multiples** : `marketing-council` simule un conseil d'experts sur une question marketing difficile.

## Sources

- [README marketingskills](https://github.com/coreyhaines31/marketingskills)
- [Skill product-marketing](https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md)
- [Claude Marketing Skills: 32 Picks — AI Builder Club](https://www.aibuilderclub.com/blog/claude-code-for-growth-marketing-skills-guide)
