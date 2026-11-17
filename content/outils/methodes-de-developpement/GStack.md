---
title: "gstack"
type: outil
description: "Suite opinionated couvrant produit, architecture, développement, QA, sécurité et livraison."
format: collection
tags:
  - metier/ingenierie
  - metier/produit-design
  - theme/planification
  - theme/revue-de-code
  - theme/tests
editeur: "Garry Tan"
site: "https://github.com/garrytan/gstack"
depot: "https://github.com/garrytan/gstack"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 141752
forks: 20935
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 5
memo: "[[GStack mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# gstack

> Suite de **23 skills opinionated pour Claude Code** qui transforme Claude en une équipe virtuelle couvrant produit, architecture, design, développement, code review, QA, sécurité, documentation et release.

**Composition** : 23 skills, 8 outils MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[GStack mémo]] pour le mémo pratique.

## Résumé

gstack est un framework de skills pour Claude Code conçu autour d'une métaphore d'**équipe d'ingénierie complète** : CEO/product manager, engineering manager, designer, reviewer, QA engineer, security officer, release engineer et technical writer.

Son approche est fortement structurée et opinionated. Chaque rôle correspond à une commande `/...`, permettant de faire intervenir Claude selon la phase du cycle de développement. Le projet inclut notamment des workflows de planification, revue de code, QA navigateur, sécurité, documentation et livraison.

## Fonctionnalités

- **Product & planning** : `/office-hours`, `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/autoplan`
    
- **Development & debugging** : `/investigate`, `/pair-agent`, `/careful`, `/freeze`, `/guard`
    
- **Code review & QA** : `/review`, `/qa`, `/qa-only`, `/browse`, `/design-review`
    
- **Design** : `/design-consultation`, `/design-shotgun`, `/design-html`
    
- **Security & performance** : `/cso`, `/benchmark`
    
- **Release & documentation** : `/ship`, `/land-and-deploy`, `/document-release`, `/document-generate`
    
- **Contexte et continuité** : `/context-save`, `/context-restore`, `/retro`
    
- **Navigation web réelle** avec Chromium/Aside, permettant à Claude de manipuler une application, prendre des screenshots et vérifier son comportement.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Couverture fonctionnelle|★★★★★|
|Qualité des workflows|★★★★☆|
|QA / validation UI|★★★★☆|
|Intégration Claude Code|★★★★★|
|Simplicité|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|★★★★★|
|Légèreté / consommation de tokens|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 141 752 au 16 novembre 2026._

**Commentaire :** gstack est particulièrement complet et couvre des étapes souvent peu structurées dans les workflows Claude Code, notamment la réflexion produit, la revue UX, la QA dans un navigateur réel et la préparation de release. En contrepartie, son caractère très opinionated et son nombre élevé de skills rendent le workflow plus lourd que des frameworks centrés uniquement sur l'ingénierie. Des utilisateurs signalent notamment une consommation de tokens supérieure et une complexité plus importante que Superpowers.

### Points forts

- **Couverture très large du cycle produit/logiciel**, de l'idée jusqu'à la release.
    
- **Séparation claire des rôles**, ce qui permet de faire examiner un même travail sous plusieurs angles.
    
- **QA navigateur particulièrement intéressante** : Claude peut réellement naviguer dans l'application, effectuer des clics et produire des preuves visuelles.
    
- **Très forte orientation produit**, avec des reviews dédiées au produit, à l'architecture et au design.
    
- **Revue de sécurité intégrée**, avec un workflow dédié aux audits OWASP/STRIDE ; il s'agit d'une revue assistée par LLM, qui ne remplace ni SAST/SCA ni revue humaine.
    
- **Documentation automatisée** avec génération selon le framework Diátaxis.
    
- **Open source, MIT et gratuit**, avec une adoption GitHub très importante (indicateur d'attention, non de qualité).
    

### Limites

- **Workflow lourd et très opinionated** : toutes les étapes ne sont pas nécessaires pour chaque tâche.
    
- **Consommation de tokens potentiellement importante**, notamment lorsqu'on utilise plusieurs phases de review.
    
- **Chevauchement avec d'autres frameworks de skills**, notamment Superpowers pour la planification, l'implémentation et la vérification.
    
- **Risque de sur-processus** sur les petites tâches : lancer plusieurs rôles spécialisés peut coûter davantage que la tâche elle-même.
    
- **Certaines fonctionnalités nécessitent une infrastructure supplémentaire**, notamment le navigateur Chromium/Aside pour la QA.
    
- **Philosophie fortement liée aux pratiques de Garry Tan** : les workflows sont volontairement prescriptifs plutôt que neutres, et un cadre conçu pour les habitudes de son auteur doit être adapté au dépôt et à l'équipe plutôt que pris pour une norme.

- **Projet porté par un auteur principal** : 14 contributeurs seulement malgré une très forte audience (voir la note Popularité), et peu d'avis indépendants consacrés spécifiquement à gstack (voir [[#Avis indépendants|les avis indépendants]]) ; la valeur dépend du temps de revue et du taux de retouche économisés, pas de la popularité.

- **Sentiment de progrès** : comme d'autres frameworks de workflow, il peut ajouter de la cérémonie et du contexte sans garantir une meilleure qualité de code.
    
- **Projet très actif et en évolution rapide**, avec de nombreuses issues et pull requests ; les utilisateurs doivent donc suivre les évolutions du framework.
    

## Relations

- **Alternative à :** [[BMAD Method]], [[Compound Engineering]]
    
- **S'intègre avec :** [[Claude Code]], GitHub, Chromium / Playwright
    
- **Utilise :** Claude Code Skills, Git, GitHub CLI, Chromium, Playwright
    

**Positionnement par rapport à Superpowers :** les deux frameworks se chevauchent fortement sur la planification et le développement. Superpowers est davantage centré sur la **méthodologie d'ingénierie et le processus d'implémentation**, notamment TDD et développement par sous-agents, tandis que gstack couvre plus largement les dimensions **produit, design, QA, sécurité et release**. Des retours d'utilisateurs décrivent également gstack comme plus complexe et plus consommateur de tokens.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

gstack plaît aux utilisateurs qui veulent un processus de développement plus cadré sans adopter une méthode aussi lourde que BMAD. Son attrait vient d’un workflow opinionated, de commandes prêtes à l’emploi et de la crédibilité pratique de son auteur.

Les avis indépendants directement consacrés à gstack restent moins nombreux que pour Superpowers, GSD ou BMAD. Les critiques générales de ces frameworks s’appliquent : ils peuvent ajouter de la cérémonie, du contexte et un sentiment de progrès sans garantir la qualité du code. Un cadre conçu pour les habitudes de son auteur doit être adapté au dépôt et à l’équipe, pas considéré comme une norme universelle.

### Comparaison

Superpowers met l’accent sur brainstorming, TDD et revue ; GSD sur la séparation des contextes et l’exécution par phases ; BMAD couvre l’ensemble du cycle produit. gstack occupe un milieu pragmatique, plus direct que BMAD et plus opinionated qu’un simple plan natif.

### Verdict

Un bon workflow à tester sur une fonctionnalité réelle. Sa valeur dépendra moins de sa popularité que du temps de revue et du taux de retouche qu’il économise à votre équipe.

## Sources

- [GitHub](https://github.com/garrytan/gstack)
    
- [Skills documentation](https://github.com/garrytan/gstack/blob/main/docs/skills.md)
    
- [README](https://github.com/garrytan/gstack/blob/main/README.md)
    
- [Comparaison utilisateurs avec Superpowers](https://www.reddit.com/r/ClaudeCode/comments/1s16ckh/whats_the_difference_between_superpower_and_gstack/)
    

### Sources des avis

- [Dépôt officiel](https://github.com/garrytan/gstack)
- [Comparatif panoramique des workflows Claude Code](https://fanweibin.cn/posts/2026-04-03-j1zxIBC6)
- [Comparaison de onze systèmes de workflow](https://www.reddit.com/r/ClaudeAI/comments/1sybpya/compared_11_popular_claude_code_workflow_systems/)

_Dernière analyse : 12 novembre 2026_