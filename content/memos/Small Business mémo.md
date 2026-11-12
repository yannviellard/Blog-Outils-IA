---
title: "Small Business — Mémo"
type: memo
fiche: "[[Small Business]]"
date: 2026-09-25
---

# Small Business — Mémo

> L'essentiel pour utiliser [[Small Business]], le plugin d'Anthropic qui aide à gérer une petite entreprise avec Claude : finance, ventes, marketing, clients, opérations, recrutement (44 skills). Pas besoin de retenir de commandes : on décrit son besoin en français courant, un routeur choisit la bonne skill. Rien n'est envoyé, publié ou payé sans ton accord.

## Installation

```bash
# Claude Code
claude plugin marketplace add anthropics/knowledge-work-plugins
claude plugin install small-business@knowledge-work-plugins
```

Dans Claude Cowork : l'installer depuis [claude.com/plugins](https://claude.com/plugins/).

Puis dire **« get me started »** (« aide-moi à démarrer ») : une mise en route de 15 minutes connecte tes deux premiers outils (QuickBooks, PayPal, HubSpot, Canva, Google Workspace, Microsoft 365…), fait un premier essai réel, apprend ton activité et enregistre ta charte graphique pour les rapports.

## Ce qu'on peut demander

|Domaine|Exemples de demandes|
|---|---|
|Trésorerie et finance|« Est-ce que je peux payer les salaires ? », « Prévision de trésorerie », « Clôture le mois », « Paie les factures », « Qui me doit de l'argent ? », « Prépare les impôts »|
|Ventes|« Trouve-moi des clients », « Qui dois-je appeler ? », « Écris ce message de prospection », « Relance les clients inactifs », « Fais un devis pour ce chantier », « Mets à jour le CRM »|
|Marketing|« Mon marketing fonctionne-t-il ? », « Point de croissance de la semaine », « Crée le contenu », « Mes pubs », « SEO »|
|Clients et réputation|« Que disent les clients ? », « Un client est mécontent », « Vérifie mes commandes »|
|Opérations et recrutement|« Trie mes e-mails », « Brief du lundi », « Réassort », « Rédige une offre d'emploi », « Trie ces candidatures », « Relis ce contrat », « Aides et appels d'offres »|
|Personnalisation|« Mets à jour ma charte » (logo et couleurs depuis un lien), « Automatise ça » (transforme une tâche répétée en skill), « Connecte mon ERP »|

## Quelques skills utiles par leur nom

|Skill|Ce qu'elle fait|
|---|---|
|`business-pulse` / `monday-brief`|Synthèse de l'activité, brief du lundi.|
|`cash-flow-snapshot`|Photo de la trésorerie.|
|`invoice-chase`|Relance des factures impayées.|
|`close-month`|Clôture mensuelle, avec validation à chaque étape.|
|`plan-payroll` / `payroll-prep`|Préparation de la paie (c'est toi qui valides le paiement).|
|`lead-triage` / `call-list`|Priorise les prospects, liste d'appels.|
|`contract-review`|Relecture d'un contrat.|
|`proposal-builder` / `grant-rfp-writer`|Propositions commerciales, réponses aux appels d'offres.|
|`review-reputation`|Suivi des avis clients.|
|`build-agent` / `build-connector`|Crée ta propre skill ou un connecteur vers un outil non pris en charge.|

## Conseils d'utilisation

- **Commencer par « get me started »** : la mise en route rend tous les résultats plus pertinents.
- **Pas besoin de connecteur pour essayer** : chaque skill fonctionne aussi avec un export CSV, un PDF ou un e-mail collé.
- **Valider chaque étape** : payer une facture et la saisir en comptabilité sont deux validations distinctes ; la paie reste préparée, c'est toi qui déclenches.
- **Pas de chiffre inventé** : un montant illisible est signalé comme tel. Vérifier quand même les montants avant validation.
- **Pensé pour les États-Unis** (1099, outils comme QuickBooks) : adapter la fiscalité et les obligations à ton pays, et faire relire par un professionnel.
- **Les permissions existantes s'appliquent** : Claude ne voit que ce que l'utilisateur connecté a déjà le droit de voir dans chaque outil.

## Sources

- [README du plugin Small Business](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business)
- [Introducing Claude for Small Business — Anthropic](https://www.anthropic.com/news/claude-for-small-business)
- [Claude for Small Business: complete setup guide — The VC Corner](https://www.thevccorner.com/p/claude-for-small-business-complete-setup-guide-2026)
- [Claude for Small Business: Plugin Guide — We Call Shotgun](https://wecallshotgun.com/blog/claude-for-small-business-31-skills-guide)
