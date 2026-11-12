---
title: "UI UX Pro Max — Mémo"
type: memo
fiche: "[[UI UX Pro Max]]"
date: 2026-09-25
---

# UI UX Pro Max — Mémo

> Les commandes à connaître pour [[UI UX Pro Max]], la skill qui donne à Claude Code, Codex ou Cursor une base de connaissances de design interrogeable : styles d'interface, palettes, associations de polices, règles UX, types de graphiques, conseils par stack technique. Elle peut aussi générer et enregistrer un design system complet.

## Installation

```bash
# Claude Code
/plugin marketplace add nextlevelbuilder/ui-ux-pro-max-skill
/plugin install ui-ux-pro-max@ui-ux-pro-max-skill

# Ou via le CLI (recommandé), depuis le projet
npm install -g ui-ux-pro-max-cli
uipro init --ai claude          # aussi : codex, cursor, gemini, all…
uipro init --ai claude --global # pour tous tes projets (~/.claude/skills/)
```

Prérequis : Python 3 (bibliothèque standard seulement, aucun accès réseau). Le paquet npm s'appelle `ui-ux-pro-max-cli` ; l'ancien `uipro-cli` est obsolète.

## Utilisation

Dans Claude Code, Codex ou Cursor, la skill se déclenche seule dès qu'on demande du travail d'interface :

- « Construis une landing page pour mon SaaS »
- « Crée un tableau de bord d'analytique santé »
- « Fais une app bancaire fintech en thème sombre »

Préciser la stack dans la demande (React, Next.js, shadcn/ui, Vue, SwiftUI, Flutter…), sinon HTML + Tailwind par défaut.

## Commandes du CLI

|Commande|Ce qu'elle fait|
|---|---|
|`uipro init --ai <agent>`|Installe la skill pour un agent.|
|`uipro init --dry-run`|Montre ce qui serait installé.|
|`uipro update`|Rafraîchit les fichiers de la skill (`--global` pour l'installation globale).|
|`uipro versions`|Liste les versions disponibles.|
|`uipro uninstall`|Désinstalle (détecte l'agent automatiquement).|

## Recherche directe (script `search.py`)

Chemin pour Claude Code : `python3 .claude/skills/ui-ux-pro-max/scripts/search.py`

|Commande (arguments de `search.py`)|Ce qu'elle fait|
|---|---|
|`"fintech banking" --design-system -f markdown`|Génère un design system complet (couleurs, typo, espacements, composants).|
|`"SaaS dashboard" --design-system --persist -p "MonApp"`|Génère **et enregistre** le design system dans `design-system/monapp/MASTER.md`.|
|`… --persist -p "MonApp" --page "dashboard"`|Ajoute des règles propres à une page, dans `design-system/monapp/pages/dashboard.md`.|
|`"glassmorphism" --domain style`|Cherche un style d'interface.|
|`"elegant serif" --domain typography`|Cherche des associations de polices.|
|`"dashboard" --domain chart`|Cherche le bon type de graphique.|
|`"error summary validation" --domain ux`|Cherche une règle UX.|
|`"form validation" --stack react`|Conseils propres à une stack.|

## Design system persistant : maître + surcharges

- `MASTER.md` : la référence globale (couleurs, typographie, espacements, composants).
- `pages/<page>.md` : uniquement les écarts d'une page par rapport au maître.

Prompt conseillé quand tu construis une page : « Lis `design-system/monapp/MASTER.md`. Vérifie si `design-system/monapp/pages/checkout.md` existe ; si oui, ses règles priment. Puis génère le code. »

## Conseils d'utilisation

- **Enregistrer le design system tôt** (`--persist`) : les pages suivantes restent cohérentes entre les sessions.
- **Attention à `--force`** : `--persist` ne réécrit pas un `MASTER.md` existant, sauf avec `--force`, qui efface les décisions précédentes. Relire le fichier avant de régénérer.
- **Requêtes courtes et ciblées** : une intention dominante, 2 à 5 mots utiles et une contrainte (produit, plateforme, interaction).
- **Mentionner les anciennes versions explicitement** (ex. « Next.js 15 ») si ton projet n'est pas à jour : sinon la skill donne les conseils de la version actuelle.
- **Se servir des vérifications finales** (contraste, focus, labels ARIA, taille des zones tactiles) avant de livrer.

## Sources

- [README UI UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)
- [SKILL.md](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md)
- [How to Use the ui-ux-pro-max Skill in Claude Code — Skillselion](https://skillselion.com/guides/how-to-use-ui-ux-pro-max-skill)
- [Top 8 Claude Skills for UI/UX Engineers — Snyk](https://snyk.io/articles/top-claude-skills-ui-ux-engineers/)
