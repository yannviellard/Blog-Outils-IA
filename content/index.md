---
title: AI Tools Wiki
type: index
description: "Cartographie raisonnée des agents, skills, applications et services d'IA pour l'entreprise, avec des notes justifiées et des avis indépendants."
modified: 2026-11-12
---

# AI Tools Wiki

Une cartographie raisonnée des agents IA, applications, skills, frameworks et services qui peuvent équiper une entreprise, principalement autour de Claude Code. Chaque outil a une **fiche détaillée**, qui se termine par une synthèse des **avis indépendants**, et, quand il a des commandes à retenir, un **mémo pratique**.

> [!info] Ce que mesurent les notes
> Trois notes sur 5 évaluent la fiabilité de l'information et le recul disponibles sur un outil (documentation, précision des descriptions, maturité), pas sa performance sur votre cas. Une quatrième, la popularité, est calculée à partir des étoiles GitHub. Barème et règles : [[Comparatif global des outils]].

## Par métier

Partir du besoin de son équipe, puis consulter les outils recommandés et leur point d'attention.

|Métier|Pour|
|---|---|
|[[Direction et gouvernance]]|Stratégie, décision, finances, organisation des processus.|
|[[Ingénierie et développement]]|Concevoir, coder, tester, sécuriser, déployer et maintenir les applications.|
|[[Produit et design]]|Besoins utilisateurs, prototypes, cohérence de l'interface.|
|[[Commercial et marketing]]|Marché, campagnes, contenu, référencement, déclinaison de la marque.|
|[[Succès client et support]]|Réponses aux clients, base de connaissances, suivi de l'adoption.|
|[[Opérations et fonctions support]]|Juridique, administration, finance, RH, automatisations internes.|

## Par famille

Comprendre ce qu'on installe et à quoi le comparer : chaque outil appartient à une seule famille, dont la page donne les notes et les critères de choix. Vue d'ensemble : [[outils/index|Tous les outils]].

- **Le poste de travail de l'agent** : [[outils/agents-de-developpement/index|Agents de développement]] · [[outils/postes-de-pilotage/index|Postes de pilotage multi-agent]] · [[outils/methodes-de-developpement/index|Méthodes de développement]] · [[outils/orchestration-et-catalogues/index|Orchestration et catalogues d'agents]] · [[outils/memoire-et-contexte/index|Mémoire et contexte]]
- **Construire et livrer** : [[outils/revue-et-securite/index|Revue, sécurité et création de skills]] · [[outils/navigateur-et-tests/index|Navigateur et tests]] · [[outils/backend-et-deploiement/index|Backend, authentification et déploiement]] · [[outils/prototypage-en-ligne/index|Prototypage en ligne]] · [[outils/design-en-code/index|Design en code]] · [[outils/modeles/index|Modèles]]
- **Produire et décider** : [[outils/recherche-et-veille/index|Recherche et veille]] · [[outils/marketing-et-seo/index|Marketing et SEO]] · [[outils/image-video-medias/index|Image, vidéo et médias]] · [[outils/ecriture-voix-messagerie/index|Écriture, voix et messagerie]] · [[outils/finance-juridique-decision/index|Finance, juridique et décision]]

## Comprendre

Les notions qui reviennent dans toutes les fiches : [[Model Context Protocol|MCP]] · [[Skill]] · [[Plugin]] · [[Hook]] · [[Subagents|Sous-agents]] · [[Harnais d'agent]] · [[Worktree]] · [[Mémoire d'agent]]. Glossaire : [[concepts/index|Concepts]].

## Assembler

[[Architecture multi-repos et harnais Claude Code]] : organiser plusieurs dépôts web, mobile, backend, produit et marketing, avec un harnais spécialisé dans chaque dépôt et des contrats communs. Tous les guides : [[guides/index|Guides]].

## Mémos

[[memos/index|Tous les mémos]] : installation, commandes principales et conseils d'utilisation, vérifiés dans la documentation officielle de chaque outil.

## Méthode

[[methode/index|À propos du wiki]] (ce qu'il mesure, comment il est écrit) · [[Comparatif global des outils]] (barème et toutes les notes) · [[Taxonomie]] (familles, formats, métiers, thèmes).

## Principes de sélection

1. **Partir d'un besoin métier**, pas du nombre d'agents ou de fonctionnalités.
2. **Tester un workflow réel** avec un critère mesurable : temps gagné, taux de retouche, précision ou coût.
3. **Installer le minimum utile** : chaque skill, plugin, MCP ou mémoire ajoute du contexte, des dépendances et une surface d'attaque.
4. **Conserver une validation humaine** pour les décisions financières, juridiques, commerciales, éditoriales et de sécurité.
5. **Prévoir la réversibilité** : formats ouverts, exports, versions épinglées et procédure manuelle de secours.
