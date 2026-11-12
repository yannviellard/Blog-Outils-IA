---
title: "Claude for Financial Services — Mémo"
type: memo
fiche: "[[Claude for Financial Services]]"
date: 2026-09-25
---

# Claude for Financial Services — Mémo

> Les commandes à connaître pour [[Claude for Financial Services]], les agents, skills et connecteurs de données d'Anthropic pour la finance : banque d'affaires, recherche actions, private equity, administration de fonds, gestion de patrimoine. Utilisables dans Claude Code ou Claude Cowork. Tout est produit en brouillon, pour validation par un professionnel.

## Installation dans Claude Code

```bash
claude plugin marketplace add anthropics/financial-services

# Socle à installer en premier : modélisation + tous les connecteurs de données
claude plugin install financial-analysis@claude-for-financial-services

# Puis les verticales utiles
claude plugin install investment-banking@claude-for-financial-services
claude plugin install equity-research@claude-for-financial-services

# Et/ou des agents complets
claude plugin install pitch-agent@claude-for-financial-services
claude plugin install gl-reconciler@claude-for-financial-services
```

Dans Cowork : **Paramètres → Plugins → Ajouter**, puis coller l'URL du dépôt.

## Commandes par métier

### Modélisation (socle `financial-analysis`)

|Commande|Ce qu'elle fait|
|---|---|
|`/comps`|Analyse de sociétés comparables (multiples).|
|`/dcf`|Valorisation DCF avec WACC et analyse de sensibilité.|
|`/lbo`|Modèle de LBO.|
|`/3-statement-model`|Remplit un modèle à trois états financiers.|
|`/debug-model`|Audite un modèle Excel : formules, valeurs en dur, équilibres.|
|`/competitive-analysis`|Paysage concurrentiel.|
|`/ppt-template`|Apprend à Claude tes modèles PowerPoint de marque.|

### Banque d'affaires

`/one-pager` (profil d'entreprise), `/cim` (mémorandum d'information), `/teaser`, `/buyer-list`, `/merger-model` (relution/dilution), `/process-letter`, `/deal-tracker`

### Recherche actions

`/earnings` (note post-résultats), `/earnings-preview`, `/initiate` (initiation de couverture), `/model-update`, `/morning-note`, `/sector`, `/thesis`, `/catalysts`, `/screen`

### Private equity

`/source` (recherche de cibles), `/screen-deal` (tri rapide des dossiers entrants), `/dd-checklist`, `/dd-prep`, `/unit-economics`, `/returns` (TRI/MOIC), `/ic-memo` (mémo de comité), `/portfolio`, `/value-creation` (plan à 100 jours), `/ai-readiness`

## Agents complets

|Agent|Ce qu'il fait|
|---|---|
|Pitch Agent|Comparables, transactions, LBO → pitch deck de marque, de bout en bout.|
|Meeting Prep Agent|Dossier de préparation avant un rendez-vous client.|
|Market Researcher|Secteur ou thème → panorama, concurrents, comparables, idées.|
|Earnings Reviewer|Conférence de résultats + publications → mise à jour du modèle → note.|
|Model Builder|DCF, LBO, trois états, comparables, directement dans Excel.|
|GL Reconciler / Month-End Closer|Rapprochements, recherche d'écarts, clôture mensuelle.|
|Valuation Reviewer / Statement Auditor|Valorisations et relevés destinés aux investisseurs (LP).|
|KYC Screener|Analyse des pièces d'ouverture de compte, signale les manques.|

## Conseils d'utilisation

- **Installer `financial-analysis` en premier** : il contient les compétences de modélisation partagées et les connecteurs.
- **Connecteurs payants** : FactSet, S&P Global, PitchBook, Moody's, Morningstar… exigent un abonnement chez le fournisseur. Ils visent surtout la banque et la recherche ; un cabinet comptable n'en a pas l'usage.
- **Tester sur des périodes déjà clôturées** avant de confier un vrai mois ou un vrai dossier aux agents.
- **Ne jamais automatiser la validation** : les agents préparent, un professionnel signe. Ne pas brancher de script qui publie leurs brouillons tels quels.
- **Personnaliser** : ajouter terminologie, processus et normes de présentation de la maison dans les fichiers de skills, et ses modèles PowerPoint via `/ppt-template`.
- **Figer une version** (commit précis) si ta politique interne exige des résultats reproductibles.

## Sources

- [README anthropics/financial-services](https://github.com/anthropics/financial-services)
- [Installer les plugins finance — Claude Help Center](https://support.claude.com/en/articles/13851150-install-financial-services-plugins)
- [Use Claude Code as a Wall Street Analyst — The Rundown](https://app.therundown.ai/guides/turn-claude-code-into-your-personal-wall-street-analyst)
- [10 Free Anthropic Finance Plugins: A Solo CPA's Test — FindSkill.ai](https://findskill.ai/blog/anthropic-finance-plugins-solo-cpas-month-end-close/)
