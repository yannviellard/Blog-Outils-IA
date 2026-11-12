---
title: "Marketing Skills"
type: outil
description: "Frameworks marketing précis pour CRO, copywriting, SEO, lancement et rétention."
format: collection
tags:
  - metier/marketing-ventes
  - theme/seo
  - theme/redaction
editeur: "Corey Haines"
site: "https://marketing-skills.com/"
depot: "https://github.com/coreyhaines31/marketingskills"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 59710
forks: 8720
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[Marketing Skills from Corey Haines mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Marketing Skills

> Bibliothèque de skills marketing pour les agents IA couvrant notamment le CRO, le copywriting, le SEO, l'analytics, la publicité, la rétention, le product marketing et le growth engineering. Compatible avec Claude Code, OpenAI Codex, Cursor, Windsurf et les agents supportant l'Agent Skills specification.

**Composition** : 70 skills, 8+ outils MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Marketing Skills from Corey Haines mémo]] pour le mémo pratique.

## Résumé

`coreyhaines31/marketingskills` est une bibliothèque open source de **skills marketing réutilisables pour les agents de développement IA**.

Le projet repose sur une architecture modulaire : chaque compétence est définie sous forme de fichier Markdown `SKILL.md`, contenant les connaissances, frameworks et workflows nécessaires à l'agent. Les skills peuvent être utilisés individuellement ou combinés.

Le skill `product-marketing` constitue le **contexte central** du système : les autres skills s'appuient sur les informations concernant le produit, l'audience et le positionnement avant d'effectuer leur propre tâche. Cette architecture permet de conserver une cohérence entre stratégie, SEO, contenu, CRO, acquisition et rétention.

Le projet a connu une croissance extrêmement rapide depuis sa création en janvier 2026 et comptait **23 contributeurs et 473 commits** lors de l'analyse du 10 octobre 2026.

## Fonctionnalités

- **Conversion Optimization** : CRO, signup, onboarding, popups et paywalls.
    
- **Content & Copy** : copywriting, copy-editing, emails, cold email, social, image et vidéo.
    
- **SEO & Discovery** : SEO audit, AI SEO/GEO, programmatic SEO, architecture du site, schema et pages concurrentielles.
    
- **Paid Acquisition & Distribution** : Google Ads, Meta, LinkedIn, ad creative, social et événements.
    
- **Analytics & Experimentation** : analytics, attribution et A/B testing.
    
- **Growth & Retention** : referrals, co-marketing, free tools, churn prevention et community marketing.
    
- **Product Marketing & Strategy** : product marketing, customer research, positioning, pricing, offers, launch et marketing plans.
    
- **Sales & RevOps** : prospecting, sales enablement et revenue operations.
    
- **Intégrations marketing** : guides et outils pour connecter les skills à des services externes, avec notamment GA4, Stripe, Mailchimp, Google Ads, Resend, Zapier, ZoomInfo, Clay, Supermetrics, Coupler, Outreach et Crossbeam.
    
- **Installation multi-agent** via `npx skills`, plugin Claude Code, copie directe, submodule ou SkillKit.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Architecture|★★★★★|
|Couverture marketing|★★★★★|
|Qualité des workflows|★★★★★|
|Cohérence entre skills|★★★★★|
|Intégrations|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|
|Portabilité multi-agents|★★★★★|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 59 710 au 11 novembre 2026._

**Commentaire :** le projet est l'une des bibliothèques les plus souvent recommandées par les praticiens pour les skills marketing destinés aux agents de code (l'adoption figure dans le tableau d'en-tête mais n'est pas notée : elle ne mesure pas la qualité). Les notes de qualité des workflows et de cohérence reposent sur la structure du dépôt, sans évaluation indépendante des résultats produits. Sa principale qualité n'est pas seulement le nombre de skills, mais leur **composition autour d'un contexte marketing partagé** et leurs références croisées. Le dépôt suit l'Agent Skills specification et fonctionne avec plusieurs agents, dont Claude Code et Codex.

Le dépôt contient actuellement environ **70 skills indexés**, avec des skills individuels dépassant parfois 200k installations sur la plateforme skills.sh.

### Points forts

- **Très forte couverture fonctionnelle**, allant du SEO et CRO jusqu'au pricing, à la rétention, au product marketing et aux RevOps.
    
- **Architecture cohérente** : `product-marketing` sert de contexte commun aux autres compétences.
    
- Skills **modulaires et composables** plutôt qu'un agent monolithique.
    
- Compatible avec **Claude Code, Codex, Cursor, Windsurf** et les agents conformes à l'Agent Skills specification.
    
- Présence de **skills très spécialisés** : AI SEO, programmatic SEO, attribution, competitor profiling, marketing loops, marketing council, etc.
    
- Forte orientation vers les **technical marketers et founders**, avec des workflows directement exploitables par des coding agents.
    
- **Installation sélective** possible : il n'est pas nécessaire d'installer l'ensemble de la bibliothèque.
    
- Projet **MIT**, ce qui facilite l'adaptation et la réutilisation.
    
- Développement actif : 473 commits et des changements de structure réguliers entre v1.x et v2.x.
    
- Les skills sont accompagnés de règles de contribution et de validation, avec une structure standardisée pour chaque `SKILL.md`.
    
- La version 2.x a récemment rationalisé plusieurs skills en fusionnant ou renommant certains modules, ce qui montre une volonté de maintenir une architecture cohérente.
    

### Limites

- **Très grand nombre de skills** : installer toute la bibliothèque peut générer du bruit et augmenter le risque qu'un agent sélectionne une compétence inutile.
    
- Les skills restent principalement des **instructions et workflows pour LLM** ; ils ne remplacent pas les plateformes spécialisées de marketing analytics ou d'advertising.
    
- Les intégrations externes nécessitent souvent des outils, API ou credentials supplémentaires.
    
- La qualité des résultats dépend toujours fortement du contexte fourni à l'agent et des données accessibles.
    
- Certaines compétences sont davantage des **frameworks méthodologiques** que des automatisations exécutables.
    
- La popularité extrêmement élevée peut créer un effet de mode : la **popularité du dépôt indique une adoption et une visibilité exceptionnelles, mais ne constitue pas à elle seule une validation de chaque skill**.
    
- Le projet évolue très rapidement : les changements de noms et de structure entre v1.x et v2.x peuvent nécessiter une attention particulière lors des mises à jour.
    
- Les intégrations partenaires sont explicitement signalées dans le dépôt ; elles sont séparées des recommandations centrales des skills, mais constituent tout de même une dépendance à surveiller dans une stack marketing.
    

## Relations

- **Alternative à :** [[Ai-Marketing-Claude]] (suite plus orchestrée avec audit multi-agent), [[OpenClaudia]], Hyper Marketing Skills (davantage orienté exécution contre des plateformes réelles, selon un comparatif publié par son propre éditeur), autres collections de Marketing Skills pour Claude Code
    
- **S'intègre avec :** Claude Code · OpenAI Codex · Cursor · Windsurf · SkillKit
    
- **Utilise :** Agent Skills specification · Markdown · Node.js CLI · outils MCP / API externes
    
- **Architecture :** Product Marketing Context → Skills spécialisés → outils / intégrations
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Cette collection est l’une des plus souvent recommandées par les praticiens du marketing avec Claude Code. Sa force tient à des frameworks métier précis — CRO, copywriting, contenu, SEO, lancement — qui donnent au modèle un processus et des critères plutôt qu’un vague rôle de « marketeur expert ».

Les limites sont bien comprises : les skills écrivent et analysent, mais n’accèdent pas par défaut aux comptes publicitaires, analytics ou CRM. Leur qualité dépend du contexte de marque, de la donnée client et de la vérification des faits. Une grande bibliothèque peut aussi être surdimensionnée si l’équipe n’utilise que deux ou trois workflows.

### Comparaison

Hyper Marketing Skills met davantage l’accent sur l’exécution contre des plateformes réelles et des workflows payants (selon un comparatif publié par l'éditeur d'Hyper lui-même, donc source partiale). `ai-marketing-claude` propose un audit multi-agent plus orchestré. Corey Haines est souvent préféré comme **base méthodologique ouverte et modulaire**.

### Verdict

Probablement l’un des meilleurs points de départ gratuits pour formaliser un marketing répétable avec un agent ; installer seulement les modules réellement utilisés et les alimenter avec des données propriétaires.

## Sources

- [GitHub](https://github.com/coreyhaines31/marketingskills)
    
- [Website](https://marketing-skills.com/)
    
- [README](https://github.com/coreyhaines31/marketingskills/blob/main/README.md)
    
- [AGENTS.md](https://github.com/coreyhaines31/marketingskills/blob/main/AGENTS.md)
    
- [Contributing](https://github.com/coreyhaines31/marketingskills/blob/main/CONTRIBUTING.md)
    
- [Skills index](https://www.skills.sh/coreyhaines31/marketingskills)
    

### Sources des avis

- [Comparatif Corey Haines vs Hyper](https://www.hyperfx.ai/blog/hyper-marketing-skills-vs-corey-haines-marketing-skills)
- [Retour d’un testeur de skills marketing](https://www.reddit.com/r/ClaudeAI/comments/1vkn063/i_build_and_test_claude_skills_for_digital/)
- [Sélection de skills pour marketeurs](https://claudecodeformarketers.com/blog/claude-code-skills-for-marketers/)

_Dernière analyse : 12 novembre 2026_