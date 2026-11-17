---
title: "Claude SEO"
type: outil
description: "Pack SEO étendu, utile comme couche d'exécution dans un dépôt connecté aux vraies données."
format: collection
tags:
  - metier/marketing-ventes
  - theme/seo
  - theme/recherche
editeur: "AgriciDaniel"
site: "https://claude-seo.md/"
depot: "https://github.com/AgriciDaniel/claude-seo"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-10
etoiles: 29850
forks: 3756
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 4
memo: "[[Claude SEO mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Claude SEO

> Plugin SEO complet pour Claude Code qui orchestre 25 skills et 18 agents spécialisés pour automatiser les audits SEO techniques, éditoriaux, Schema.org, GEO/AEO, local, e-commerce et international.

**Composition** : 25 skills, 18 agents, extensions MCP optionnelles.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Claude SEO mémo]] pour le mémo pratique.

## Résumé

**Claude SEO** transforme Claude Code en environnement d'analyse SEO multi-agent. Un orchestrateur coordonne des skills et agents spécialisés pour analyser différentes dimensions d'un site, puis produire des recommandations et rapports structurés.

Le projet couvre le **SEO technique**, le contenu, Schema.org, le SEO local, l'e-commerce, l'international et surtout le **GEO / AI Search**, avec des fonctionnalités dédiées à la citabilité des contenus par les moteurs de recherche utilisant l'IA.

## Fonctionnalités

- **Audit SEO multi-agent** : analyse parallèle de plusieurs dimensions techniques et éditoriales d'un site.
    
- **SEO technique et contenu** : crawlabilité, indexation, sitemap, Core Web Vitals, qualité du contenu, E-E-A-T et architecture.
    
- **GEO / AI Search** : analyse et optimisation de la citabilité des contenus pour les moteurs de recherche et interfaces basés sur l'IA.
    
- **Schema.org** : analyse et validation des données structurées JSON-LD.
    
- **SEO local, e-commerce et international** : fonctionnalités spécialisées selon le type de site et le marché ciblé.
    
- **Analyse sémantique** : clustering de mots-clés et analyse des sujets et pages concurrentes.
    
- **Monitoring SEO** : snapshots et détection de dérive SEO dans le temps.
    

## Analyse

|**Critère**|**Note**|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|
|Architecture agents/skills|★★★★★|
|Couverture fonctionnelle|★★★★★|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 29 850 au 16 novembre 2026._

### Points forts

- Architecture **multi-agent très structurée**, avec séparation claire entre skills, agents, extensions, scripts et orchestration.
    
- Couverture particulièrement large du SEO, incluant le **GEO / AI Search** en plus du SEO traditionnel.
    
- Projet suffisamment industrialisé pour intégrer tests, CI, sécurité, extensions et différentes sources de données externes.
    
- Architecture intéressante comme **référence pour concevoir des systèmes spécialisés multi-agent avec Claude Code**.
    

### Limites

- **Complexité importante** : 25 skills et 18 agents rendent le système plus difficile à comprendre et personnaliser qu'un simple skill SEO.
    
- Plusieurs fonctionnalités avancées nécessitent des **services ou APIs externes** et leur configuration.
    
- L'orchestration de nombreux agents peut augmenter le temps d'exécution et certains workflows peuvent atteindre les limites d'exécution de Claude Code.
    
- La richesse fonctionnelle peut être disproportionnée pour un besoin SEO simple.

- **Pas de données propres** : le plugin ne possède pas spontanément les données de Search Console, d'analytics, de backlinks ou de concurrence ; sans connexions réelles et sans validation, il peut fournir des recommandations génériques ou datées.

- **Recul indépendant limité** : les comparatifs de skills SEO montrent de gros écarts de qualité entre projets, et les promesses de classement ne doivent pas être confondues avec des résultats mesurés.
    

### Qualité

**Commentaire :** projet intéressant pour son architecture (maturité notée ★★★☆☆ faute de recul indépendant). La séparation skills/agents/extensions, l'orchestration parallèle, les tests et les intégrations en font davantage un **framework spécialisé d'agents SEO** qu'une simple collection de prompts. Sa principale faiblesse est la complexité induite par cette richesse fonctionnelle, et il fonctionne comme couche d'exécution dans un dépôt connecté aux vraies données plutôt que comme source de données. Voir [[#Avis indépendants|les avis indépendants]].

## Relations

- **Complémentaire de :** [Semrush](https://www.semrush.com/) · [Ahrefs](https://ahrefs.com/) · DataForSEO, qui restent supérieurs pour les bases de mots-clés, les backlinks et le suivi historique ; Claude SEO est plus fort pour transformer un diagnostic en changements de code locaux

- **Alternative à :** outils d'audit SEO traditionnels et autres skills SEO pour agents (les suites de [[Marketing Skills from Corey Haines]] couvrent le SEO dans un ensemble plus large)
    
- **S'intègre avec :** Google Search Console · PageSpeed Insights · CrUX · GA4 · Ahrefs · DataForSEO · Firecrawl · Bing Webmaster · SE Ranking
    
- **Utilise :** Claude Code · Python · Playwright · MCP
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

La couverture très large — technique, schema, contenu, local, GEO/AEO et reporting — est son principal attrait. Le fait de travailler directement dans le dépôt permet à un agent de relier audit et corrections plutôt que de produire un simple rapport.

Le recul indépendant sur ce dépôt précis reste limité et les comparatifs de skills SEO montrent de gros écarts de qualité. Une skill peut appliquer une checklist ou générer du balisage, mais elle ne possède pas spontanément les données de Search Console, d’analytics, de backlinks ou de concurrence. Sans connexions réelles et sans validation, elle risque de fournir des recommandations génériques ou datées. Les promesses de classement ne doivent pas être confondues avec des résultats mesurés.

### Comparaison

Les suites de Corey Haines couvrent SEO dans un ensemble marketing plus large. Les outils SaaS comme Semrush ou Ahrefs restent supérieurs pour les bases de mots-clés, backlinks et suivi historique. Claude SEO est plus fort pour transformer un diagnostic en changements de code locaux.

### Verdict

Bonne couche d’exécution SEO dans un dépôt ; elle complète, mais ne remplace pas, les plateformes de données et l’expertise éditoriale.

## Sources

- [GitHub](https://github.com/AgriciDaniel/claude-seo)
    
- [Website](https://claude-seo.md/)
    
- [Releases](https://github.com/AgriciDaniel/claude-seo/releases)
    

### Sources des avis

- [Comparaison de neuf skills SEO](https://claudefa.st/blog/tools/skills/claude-code-seo-skills)
- [Comparaison de onze skills SEO/GEO](https://rywalker.com/research/seo-geo-agent-skills)
- [Présentation et périmètre de Claude SEO](https://seoagent.com/blog/seo-tools-for-claude-code)

_Dernière analyse : 12 novembre 2026_