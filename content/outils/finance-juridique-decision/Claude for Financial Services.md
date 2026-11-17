---
title: "Claude for Financial Services"
type: outil
description: "Workflows et connecteurs pour banque d'affaires, recherche actions, fonds et patrimoine."
format: collection
tags:
  - metier/direction
  - metier/operations
  - theme/mcp
  - theme/recherche
editeur: "Anthropic"
logo: "[[claude.svg]]"
site: "https://claude.com/solutions/financial-services"
depot: "https://github.com/anthropics/financial-services"
licence: "Apache-2.0"
statut: disponible
derniere_maj: 2026-10-28
etoiles: 41335
forks: 5758
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[Claude for Financial Services mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Claude for Financial Services

> Collection d'exemples de référence publiée par Anthropic (agents, skills, commandes et connecteurs MCP) pour automatiser des workflows de services financiers : investment banking, equity research, private equity, fund administration et wealth management.

## Résumé

**Claude for Financial Services** est un dépôt officiel d'Anthropic regroupant des workflows spécialisés pour les métiers financiers. Il fournit à la fois des **agents end-to-end**, des **skills réutilisables**, des **slash commands** et des **connecteurs MCP** vers des plateformes de données financières.

Le projet peut être utilisé comme plugin **Claude Cowork**, comme plugin **Claude Code**, ou comme base pour déployer des agents via l'API **Claude Managed Agents**. L'architecture est entièrement basée sur des fichiers Markdown et YAML/JSON, sans étape de build.

Le dépôt est présenté par Anthropic comme un ensemble de **templates de référence adaptables**, plutôt que comme une application autonome. Les agents et leurs skills peuvent être modifiés pour correspondre aux processus, données et standards d'une organisation.

**Composition** : nombreuses skills, 9 agents, 11+ outils MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Claude for Financial Services mémo]] pour le mémo pratique.

## Fonctionnalités

- **Agents spécialisés** : Pitch Agent, Market Researcher, Meeting Prep Agent, Earnings Reviewer, Model Builder, Valuation Reviewer, GL Reconciler, Month-End Closer, Statement Auditor et KYC Screener.
    
- **Financial analysis** : comparable companies, DCF, LBO, modèles 3 états, audit Excel et contrôle qualité de présentations.
    
- **Market & competitive research** : analyse sectorielle, paysage concurrentiel, peer comps, recherche thématique et génération d'idées.
    
- **Investment banking** : pitch decks, CIM, teasers, buyer lists, merger models et deal tracking.
    
- **Equity research** : earnings analysis, initiation reports, model updates, sector overviews, thesis tracking et catalyst calendars.
    
- **Private equity** : deal sourcing, screening, due diligence, unit economics, IC memos et portfolio monitoring.
    
- **MCP connectors** : intégrations avec Daloopa, Morningstar, S&P Global, FactSet, Moody's, LSEG, PitchBook, Aiera, Chronograph, Egnyte et Box.
    
- **Managed Agents** : modèles de déploiement avec orchestrateur, sous-agents et mécanismes de handoff.
    
- **Microsoft 365** : outillage permettant de provisionner l'intégration Claude dans Excel, PowerPoint, Word et Outlook.
    
- **Architecture modulaire** : les agents embarquent les skills nécessaires ; les skills peuvent également être installés indépendamment via les vertical plugins.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Architecture|★★★★★|
|Modularité|★★★★★|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|
|Réutilisabilité hors finance|★★★★☆|
|Intérêt pour les workflows financiers|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 41 335 au 16 novembre 2026._

**Commentaire :** projet particulièrement intéressant comme **référence d'architecture agentique et de conception de skills**, au-delà de son domaine financier. La séparation entre agents, skills, commandes et connecteurs est claire et permet de réutiliser ou d'adapter des composants sans installer toute la stack. Le dépôt est officiellement maintenu par Anthropic et présente déjà une architecture relativement complète, mais certaines fonctionnalités reposent sur des fournisseurs de données externes nécessitant des abonnements ou des clés API.

### Points forts

- **Projet officiel Anthropic** avec une architecture cohérente et directement exploitable dans Claude Code et Cowork.
    
- **Architecture très modulaire** : agents, skills, commandes et MCP connectors sont séparés et réutilisables.
    
- **Agents end-to-end** permettant de transformer des workflows complexes en processus reproductibles.
    
- **Skills particulièrement riches** pour l'analyse financière, la recherche concurrentielle, la modélisation et le contrôle qualité de decks.
    
- **Market Researcher** couvrant l'analyse sectorielle, la concurrence et les comparables.
    
- **Pitch Agent** combinant recherche, analyse et production de pitch deck.
    
- **Deck QC** et outils de vérification permettant de contrôler cohérence, données et présentations.
    
- **Connecteurs MCP nombreux**, avec accès possible à des sources professionnelles comme FactSet, PitchBook, LSEG, S&P Global ou Morningstar.
    
- **Tout est basé sur Markdown/YAML/JSON**, ce qui facilite l'inspection, la modification et la création de nouveaux agents ou skills.
    

### Limites

- **Très orienté finance institutionnelle** : une grande partie des fonctionnalités concerne DCF, LBO, equity research, fund administration, KYC ou M&A.
    
- Plusieurs connecteurs MCP nécessitent **un abonnement ou une API key auprès du fournisseur de données**.
    
- Les workflows et conventions sont conçus pour des professionnels de la finance et peuvent nécessiter une adaptation importante pour d'autres domaines.
    
- Les agents produisent des **livrables destinés à être revus par des professionnels** et ne sont pas conçus pour prendre des décisions financières ou exécuter des transactions de manière autonome.
    
- Le dépôt constitue davantage une **bibliothèque de références et de templates** qu'un framework généraliste d'agents.
    
- La délégation entre sous-agents via `callable_agents` est encore présentée comme une fonctionnalité en **Research Preview**.

- **Risque d'erreur factuelle ou de calcul** : même les meilleurs modèles se trompent encore sur une proportion significative de questions financières, et une réponse fluide peut masquer une donnée périmée ou un calcul erroné. Traçabilité, séparation des tâches, validation experte et accès aux sources primaires restent indispensables.

- **Ne remplace pas les données sous licence** : la valeur dépend des connecteurs vers des fournisseurs payants (FactSet, PitchBook, LSEG…) que l'organisation doit déjà posséder ; ni terminal de marché ni conseil financier autonome.

- **Sources de la fiche toutes émises par Anthropic** : les avis indépendants spécifiques à ce dépôt restent rares (voir [[#Avis indépendants|les avis indépendants]]).
    

## Relations

- **Alternative à :** solutions propriétaires d'automatisation des workflows financiers ; complément (et non remplaçant) des terminaux et bases de données comme Bloomberg ou FactSet ; assistants généralistes concurrents (Gemini, ChatGPT)
    
- **S'intègre avec :** [[Claude Cowork]], [[Claude Managed Agents]], Microsoft 365
    
- **Utilise :** [[Model Context Protocol|MCP]], FactSet, PitchBook, LSEG, S&P Global, Morningstar, Daloopa
    
- **Inspire :** architectures d'agents spécialisés et workflows composés de skills
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le positionnement est jugé crédible pour la synthèse de documents, l’analyse de données et la connexion aux fournisseurs déjà utilisés par les institutions. L’intérêt n’est pas seulement le modèle : ce sont surtout les connecteurs, les contrôles d’entreprise et l’intégration au flux des analystes.

Les avis et tests sur l’IA financière imposent toutefois une forte prudence. Même les meilleurs modèles se trompent encore sur une proportion significative de questions financières, et une réponse fluide peut masquer une donnée périmée ou un calcul erroné. Les institutions doivent conserver traçabilité, validation, séparation des tâches et accès aux sources primaires. Claude ne remplace pas les données propriétaires d’un Bloomberg ou FactSet.

### Comparaison

Bloomberg et FactSet dominent par leurs données sous licence, terminaux et fonctions de marché. Gemini et ChatGPT offrent des capacités généralistes comparables. Claude se différencie par sa lecture de longs contextes et le modèle MCP/connecteurs, à condition que l’entreprise possède déjà les sources nécessaires.

### Verdict

Un assistant puissant au-dessus d’un stack financier existant ; pas un terminal de marché ni une source de conseil autonome.

## Sources

- [GitHub — anthropics/financial-services](https://github.com/anthropics/financial-services)
    
- [Claude — Financial Services](https://claude.com/fr/solutions/financial-services)
    

### Sources des avis

- [Présentation officielle](https://claude.com/solutions/financial-services)
- [Évaluation récente de chatbots sur des questions financières](https://www.tomsguide.com/ai/ai-could-be-costing-you-money-new-study-finds-chatbots-get-most-financial-questions-wrong)
- [Audition parlementaire mentionnant Claude for Financial Services](https://committees.parliament.uk/publications/49658/documents/265668/default/)

_Dernière analyse : 12 novembre 2026_