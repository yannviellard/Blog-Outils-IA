---
title: "Small Business"
type: outil
description: "44 skills Anthropic pour ventes, marketing, finance, clients, opérations et recrutement."
format: collection
tags:
  - metier/direction
  - metier/marketing-ventes
  - metier/operations
  - theme/mcp
editeur: "Anthropic"
logo: "[[claude.svg]]"
site: "https://claude.com/solutions/small-business"
depot: "https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business"
statut: disponible
derniere_maj: 2026-11-09
note_documentation: 4
note_precision: 4
note_maturite: 3
memo: "[[Small Business mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Small Business

> Plugin Anthropic transformant Claude en assistant opérationnel pour petites entreprises : **44 skills** couvrant finance, ventes, marketing, opérations, clients et recrutement, avec un routeur en langage naturel et des workflows multi-étapes soumis à validation humaine.

**Composition** : 44 skills, connecteurs MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Small Business mémo]] pour le mémo pratique.

## Résumé

**Small Business** fait partie de `anthropics/knowledge-work-plugins` ; Anthropic le présente comme un **Business Operating System basé sur Claude** plutôt qu'une simple collection de prompts. Concrètement, il s'agit d'un ensemble de skills et de workflows en Markdown/JSON qui s'appuie sur les connecteurs et les licences de l'entreprise.

Le plugin fournit un routeur (`smb-router`) capable d'interpréter une demande en langage naturel et de sélectionner automatiquement la skill appropriée. Il couvre notamment la trésorerie, les factures, la paie, le reporting, les ventes, le CRM, le marketing, les propositions commerciales, les contrats, le support client, les opérations et le recrutement.

Les workflows composent plusieurs skills en séquences et imposent des **approval gates** avant les actions externes : envoyer, publier, payer ou modifier des données.

Le projet est entièrement **file-based**, principalement constitué de Markdown et JSON, sans code, infrastructure ou build nécessaire. Anthropic le présente explicitement comme une base destinée à être personnalisée avec le contexte, les processus et les outils propres à chaque entreprise.

## Fonctionnalités

- **Business router** : sélection automatique de la skill appropriée à partir d'une demande en langage naturel.
    
- **Finance & opérations** : cash-flow, paie, rapprochement, clôture mensuelle, factures, fiscalité et reporting.
    
- **Sales & CRM** : recherche de leads, qualification, CRM, pipeline, outreach et réactivation de clients.
    
- **Marketing** : stratégie de contenu, SEO/AI visibility, réseaux sociaux, publicité, réputation et campagnes.
    
- **Workflows agentiques** : enchaînement de plusieurs skills avec validation explicite entre les étapes.
    
- **Connecteurs MCP** : intégration avec les outils métier externes ; les workflows peuvent néanmoins fonctionner à partir de CSV, PDF, emails ou données fournies dans la conversation.
    
- **Build-your-own** : skills, workflows, contexte métier et connecteurs peuvent être adaptés directement dans le plugin.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|—|
|Couverture fonctionnelle|★★★★★|
|Extensibilité|★★★★★|
|Sécurité opérationnelle|★★★☆☆|
|Adaptation internationale|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité non notée : l'outil est un sous-dossier du dépôt `anthropics/knowledge-work-plugins`, dont les étoiles mesurent l'ensemble._

**Commentaire :** collection de skills bien structurée : architecture cohérente, nombreux workflows réutilisables, routeur central et intégrations MCP. La conception est orientée **human-in-the-loop**, avec validation prévue avant les actions ayant un impact externe ; ces garde-fous sont décrits par Anthropic et n'ont pas fait l'objet d'une vérification indépendante, d'où une note de sécurité opérationnelle à ★★★☆☆ : donner à un agent l'accès aux finances, aux ventes et aux documents augmente les risques d'erreur et de permission.

La principale limite est le positionnement initial très orienté **small business américain**. Les workflows financiers, fiscaux, RH et juridiques constituent des assistants opérationnels mais ne remplacent pas un professionnel qualifié ; Anthropic précise explicitement que le plugin ne fournit pas de conseil financier, fiscal, juridique ou RH.

### Points forts

- **Architecture très cohérente** : router → skills → workflows → connecteurs.
    
- **44 skills** couvrant l'essentiel des fonctions d'une petite entreprise.
    
- **Approval gates systématiques**, évitant qu'un agent exécute silencieusement une action sensible.
    
- Fonctionne **avec ou sans connecteurs** : CSV, PDF, emails et données conversationnelles restent utilisables.
    
- Architecture **simple à forker et personnaliser**, basée sur Markdown/JSON.
    
- Les workflows illustrent une approche intéressante du passage de la simple skill à l'**agent métier orchestré**.
    
- Compatible avec **Claude Code** en plus de l'expérience Cowork.
    

### Limites

- Forte orientation vers les outils et pratiques du marché américain : QuickBooks, PayPal, HubSpot, Gusto, etc.
    
- Les processus fiscaux, sociaux et comptables nécessitent une adaptation importante selon le pays.
    
- Le nombre élevé de skills peut créer du **skill sprawl** si toutes sont activées sans sélection.
    
- Les skills métier ne constituent pas une expertise professionnelle certifiée.
    
- L'intérêt maximal dépend de la qualité des données et des connecteurs disponibles.
    
- Les métriques GitHub évoluent rapidement et doivent être considérées comme des snapshots plutôt que comme des caractéristiques stables.

- **Le frein principal est l'adoption** : les petites entreprises ont peu de temps pour configurer, contrôler et former leurs équipes ; les workflows prometteurs exigent encore validation, procédures et responsabilité humaine.

- **Licence non renseignée dans cette fiche** : à vérifier avant tout fork ou redistribution, malgré l'argument d'une architecture « simple à forker ».
    

## Relations

- **Alternative à :** collections généralistes de business/marketing skills pour Claude ; assistants déjà intégrés à la suite bureautique (Microsoft Copilot pour Microsoft 365, Gemini pour Google Workspace, ChatGPT Business) — une entreprise purement Microsoft ou Google gagne souvent à tester d'abord celui-ci
    
- **S'intègre avec :** Claude Code · Claude Cowork · MCP · QuickBooks · HubSpot · Canva · DocuSign · Google Workspace · Microsoft 365
    
- **Utilise :** Skills Claude · Commands · MCP Connectors · Workflows agentiques
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le produit est perçu comme une tentative pertinente de rendre les agents accessibles aux petites structures : connecteurs vers QuickBooks, PayPal, HubSpot, Canva, DocuSign, Google Workspace et Microsoft 365, plus des workflows préconstruits. Le fait qu’il n’ajoute pas de supplément au-delà des licences existantes est attractif.

La difficulté n’est pas seulement le produit, mais l’adoption. Les petites entreprises ont peu de temps pour configurer, contrôler et former leurs équipes. Donner à un agent accès aux finances, ventes et documents augmente les risques d’erreur et de permission. Les workflows prometteurs nécessitent encore validation, procédures et responsabilité humaine.

### Comparaison

Microsoft Copilot est naturel pour une entreprise centrée sur Microsoft 365 ; Gemini pour Google Workspace ; ChatGPT Business pour un assistant généraliste. Claude se distingue par les workflows agentiques transversaux et les connecteurs, mais peut demander davantage de conception de processus.

### Verdict

Offre convaincante pour une PME multi-outils prête à formaliser ses opérations ; une entreprise purement Microsoft ou Google gagnera souvent à tester d’abord l’assistant déjà intégré à sa suite.

## Sources

- [GitHub — Small Business](https://github.com/anthropics/knowledge-work-plugins/tree/main/small-business)
    
- [GitHub — Knowledge Work Plugins](https://github.com/anthropics/knowledge-work-plugins)
    
- [Claude for Small Business](https://claude.com/solutions/small-business)
    
- [Anthropic — Introducing Claude for Small Business](https://www.anthropic.com/news/claude-for-small-business)
    

### Sources des avis

- [Annonce et analyse Axios](https://www.axios.com/2026/05/13/anthropic-claude-small-business-smb)
- [Revue et comparaison des offres](https://techsy.io/en/blog/claude-for-small-business-review)
- [Présentation des connecteurs et workflows](https://www.techradar.com/pro/we-are-committed-to-helping-business-owners-harness-ai-more-fully-and-effectively-anthropic-reveals-claude-for-small-business-to-help-close-the-gap-using-ai)

_Dernière analyse : 12 novembre 2026_