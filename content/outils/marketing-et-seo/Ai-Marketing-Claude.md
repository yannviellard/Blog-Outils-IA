---
title: "ai-marketing-claude"
type: outil
description: "Suite marketing structurée : audit, contenu, SEO, funnels et rapports."
format: collection
tags:
  - metier/marketing-ventes
  - theme/seo
  - theme/redaction
  - theme/recherche
editeur: "zubair-trabzada"
site: "https://www.skool.com/aiworkshop"
depot: "https://github.com/zubair-trabzada/ai-marketing-claude"
licence: "MIT"
statut: disponible
derniere_maj: 2026-03-02
etoiles: 2894
forks: 734
etoiles_releve: 2026-11-11
note_documentation: 3
note_precision: 4
note_maturite: 2
note_popularite: 3
memo: "[[Ai-Marketing-Claude mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# ai-marketing-claude

> Suite marketing pour Claude Code regroupant 15 skills, 5 subagents spécialisés et plusieurs scripts Python pour auditer des sites, analyser la concurrence, optimiser le copywriting et les funnels, générer des campagnes, des contenus et des rapports marketing.

**Composition** : 15 skills, 5 agents.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Ai-Marketing-Claude mémo]] pour le mémo pratique.

## Résumé

`ai-marketing-claude` est une suite de **skills et agents marketing pour Claude Code**, conçue principalement pour les entrepreneurs, solopreneurs et agences.

Le projet fournit une commande `/market` qui orchestre différents workflows marketing. Son architecture combine un orchestrateur principal, 14 sub-skills dédiés, 5 agents parallèles, des scripts Python et des templates réutilisables.

Les principales commandes couvrent l'audit marketing, le copywriting, les emails, les réseaux sociaux, les publicités, les funnels, l'analyse concurrentielle, les landing pages, les lancements, les rapports, le SEO et le branding.

Le projet est particulièrement orienté **audit et production de livrables marketing**, avec génération de rapports Markdown ou PDF et une méthodologie de scoring sur six dimensions.

## Fonctionnalités

- **Audit marketing complet** avec 5 agents parallèles couvrant contenu, conversion, SEO/technique, positionnement concurrentiel et stratégie.
    
- **15 workflows marketing** : audit, copywriting, emails, social, ads, funnel, competitors, landing, launch, proposal, reports, SEO et brand.
    
- **Analyse concurrentielle** via le skill `market-competitors` et le script `competitor_scanner.py`.
    
- **Génération de copy** avec analyse du type de page, de la voix de marque, des propositions de valeur, CTA et recommandations before/after.
    
- **Rapports Markdown et PDF** avec scores, graphiques, comparaisons, findings et plan d'action priorisé.
    
- **Templates marketing** pour séquences email, calendrier de contenu, propositions commerciales et lancement.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★☆☆|
|Précision des descriptions|★★★★☆|
|Couverture marketing|★★★★★|
|Qualité des workflows|★★★★☆|
|Analyse concurrentielle|★★★★☆|
|Automatisation réelle|★★★☆☆|
|Intégrations / données externes|★★☆☆☆|
|Maturité|★★☆☆☆|
|Popularité|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 2 894 au 11 novembre 2026._

**Commentaire :** suite Claude Code orientée marketing, avec une architecture claire et une couverture fonctionnelle importante. Sa principale faiblesse est l'écart entre la richesse des workflows et la profondeur de l'automatisation : l'essentiel repose sur les instructions données à Claude et quelques scripts Python plutôt que sur des intégrations marketing natives. La popularité, notée à part à partir des étoiles, ne mesure pas la qualité. Le site renvoie vers la communauté Skool de l'auteur (AI Workshop) : le dépôt sert aussi de vitrine à cette offre, ce qui invite à distinguer ce qui est gratuit de ce qui ne l'est pas. Voir [[#Avis indépendants|les avis indépendants]].

La méthodologie d'audit attribue notamment 25 % au contenu/messaging, 20 % au CRO, 20 % au SEO, 15 % au positionnement concurrentiel, 10 % à la marque/confiance et 10 % à la stratégie de croissance. Les scores sont ensuite agrégés en une note globale sur 100.

Ces scores doivent toutefois être considérés comme des **heuristiques**, et non comme des mesures objectives de performance marketing.

### Points forts

- **Très bonne couverture fonctionnelle** pour une suite relativement compacte.
    
- Architecture claire : orchestrateur → skills → agents → scripts → templates.
    
- **5 agents parallèles spécialisés**, permettant de séparer contenu, conversion, technique, concurrence et stratégie.
    
- Bon niveau de structuration des workflows : les skills définissent les étapes d'analyse et les formats de sortie.
    
- Le skill copywriting va au-delà de la génération de texte et analyse notamment la proposition de valeur, le ton, les CTA et le type de page.
    
- Génération de rapports Markdown ou PDF directement exploitables.
    
- Licence **MIT**, permettant modification et réutilisation.
    

### Limites

- **Pas de MCP tools natifs** : les scripts et skills ne constituent pas une couche d'intégration comparable à un véritable système connecté à GA4, Google Ads, Meta Ads ou Search Console.
    
- Les audits reposent largement sur l'analyse du contenu accessible au modèle et sur des scripts Python relativement simples.
    
- Les scores marketing donnent une impression de précision supérieure à ce que permet réellement leur méthodologie.
    
- Le scanner concurrentiel analyse principalement les sites et informations accessibles, plutôt que des données propriétaires ou des performances réelles.
    
- Plusieurs problèmes ouverts concernent l'audit de sites Wix, les erreurs liées à Cloudflare et l'installation sous Windows.
    
- Le dépôt public affiche une histoire Git très courte : une seule révision principale est visible sur le dépôt, malgré plusieurs pull requests externes.
    
- Risque de **chevauchement important** avec d'autres collections de marketing skills, notamment les projets spécialisés en SEO, CRO, paid ads ou content marketing.
    
- Le projet est davantage un **framework de workflows marketing assistés par LLM** qu'une plateforme autonome de marketing automation.
    

## Relations
   
- **Alternative à :** [[Marketing Skills from Corey Haines]] (bibliothèque plus large et modulaire), [[ai-sales-team-claude]] pour les workflows marketing
    
- **Alternative à :** autres suites généralistes de marketing skills pour Claude Code
    
- **S'intègre avec :** Claude Code
    
- **Utilise :** Claude Code · Python · ReportLab
    
- **Architecture :** Skills → Subagents → Python scripts → Markdown/PDF reports
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

La suite répond bien aux équipes qui veulent transformer Claude Code en atelier marketing : audit parallèle, copywriting, SEO, funnels et rapports sont rassemblés dans un flux cohérent. Les retours généraux sur les skills marketing confirment qu’elles font surtout gagner du temps sur les tâches répétitives, la réutilisation multicanal et la cohérence du brief.

Le consensus est plus prudent sur l’autonomie réelle. Sans accès fiable aux analytics, CRM, comptes publicitaires et données clients, un agent produit surtout des recommandations et des brouillons. Les utilisateurs mentionnent aussi les problèmes de contexte, le volume de plugins et la nécessité d’une voix de marque bien documentée. Les affirmations stratégiques ou SEO doivent être confrontées aux données réelles.

### Comparaison

Corey Haines propose une bibliothèque plus large et modulaire ; Hyper Marketing Skills insiste davantage sur l’exécution connectée aux plateformes. `ai-marketing-claude` est attractif pour son audit orchestré et ses livrables, mais plus lourd qu’un petit ensemble de skills ciblées.

### Verdict

Bonne boîte à outils pour une petite agence ou un solopreneur discipliné ; elle amplifie un processus marketing existant, elle ne remplace ni les données ni le jugement métier.

## Sources

- [GitHub](https://github.com/zubair-trabzada/ai-marketing-claude)
    
- [README](https://github.com/zubair-trabzada/ai-marketing-claude/blob/main/README.md)
    
- [License](https://github.com/zubair-trabzada/ai-marketing-claude/blob/main/LICENSE)
    
- [Issues](https://github.com/zubair-trabzada/ai-marketing-claude/issues)
    
- [Pull Requests](https://github.com/zubair-trabzada/ai-marketing-claude/pulls)
    

### Sources des avis

- [Comparatif de skills marketing](https://growthhackers.se/en/blog/claude-code-marketing-skills-comparison)
- [Retours d’utilisateurs sur les limites des agents marketing](https://www.reddit.com/r/AskMarketing/comments/1u758dd/what_claude_skills_have_you_built_that_are/)
- [Dépôt officiel](https://github.com/zubair-trabzada/ai-marketing-claude)

_Dernière analyse : 12 novembre 2026_

* La page GitHub publique indique actuellement une activité/présentation correspondant à une version initialement publiée en mars 2026 ; plusieurs pull requests externes ont toutefois été ouvertes ultérieurement.