---
title: "Méthodes de développement"
type: famille
description: "Processus prêts à l'emploi (clarification, plan, tests, revue) qui encadrent le travail d'un agent."
modified: 2026-11-12
---

# Méthodes de développement

> Processus prêts à l'emploi (clarification, plan, tests, revue) qui encadrent le travail d'un agent.

Zone : [[outils/index#Le poste de travail de l'agent|Le poste de travail de l'agent]] · Barème : [[Comparatif global des outils]]

## En bref

Aucune de ces méthodes n'a de mesure indépendante du gain sur la qualité du code : le choix se fait sur la cérémonie acceptable. Le plan natif de l'agent reste la référence à battre pour les petites tâches.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Superpowers]]|Processus de développement centré sur clarification, planification, TDD, revue et vérification.|Collection|[[Superpowers mémo\|Mémo]]|
|[[GStack]]|Suite opinionated couvrant produit, architecture, développement, QA, sécurité et livraison.|Collection|[[GStack mémo\|Mémo]]|
|[[BMAD Method]]|Méthode complète, de l'idée à l'implémentation, adaptée surtout aux produits complexes.|Collection|[[BMAD Method mémo\|Mémo]]|
|[[Planning with Files]]|Mémoire de travail explicite dans trois fichiers Markdown pour les tâches longues.|Skill|[[Planning with Files mémo\|Mémo]]|
|[[Everything Claude Code]]|Configuration de référence très riche à élaguer et adapter au contexte de l'équipe.|Collection|[[Everything Claude Code mémo\|Mémo]]|

## Points d'attention

- Adapter la cérémonie à la taille de la tâche.
- Les livrables générés (exigences, roadmap, architecture) doivent être confrontés aux utilisateurs et aux contraintes réelles.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Superpowers]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★★★|Doc claire ; aucune mesure indépendante du gain ; ~12 mois, évolution rapide.|
|[[GStack]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★★★★|Doc fournie ; peu d'avis indépendants, auteur principal ; quelques mois d'existence.|
|[[BMAD Method]]|★★★★★|★★★★☆|★★★★☆|**13**|★★★★☆|Doc complète et structurée ; livrables à relire ; recul plus long, régressions visibles dans les issues.|
|[[Planning with Files]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★★☆|README clair, limites honnêtes ; correctif de sécurité v2.36.1 ; évolution rapide.|
|[[Everything Claude Code]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★★★★|Doc riche ; positionnement « OS du harness » non vérifié ; vieillit vite, parité inégale entre agents.|

## Critères propres à la famille

|Outil|Périmètre|Cérémonie|Preuve indépendante du gain|Plus pertinent pour|
|---|---|---|---|---|
|[[Superpowers]]|Clarification, plan, TDD, revue, vérification|Moyenne|Aucune mesure citée|Fonctionnalités moyennes à grandes|
|[[GStack]]|Produit, architecture, QA, sécurité, livraison|Élevée|Peu d'avis indépendants|Équipe voulant un cadre opinionated de bout en bout|
|[[BMAD Method]]|Idée, PRD, architecture, stories|Très élevée (adaptative depuis la v6.12)|Comparatifs qualitatifs|Nouveau produit complexe|
|[[Planning with Files]]|Mémoire de travail en 3 fichiers|Faible|Une étude contrôlée nuance l'intérêt des fichiers de contexte|Tâches longues, recherches, migrations|
|[[Everything Claude Code]]|Configuration complète (68 agents, 292 skills)|Élevée|Aucune|Point de départ à élaguer|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[Compound Engineering]].

_Dernière analyse : 12 novembre 2026_
