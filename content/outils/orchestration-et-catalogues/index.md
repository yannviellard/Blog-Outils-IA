---
title: "Orchestration et catalogues d'agents"
type: famille
description: "Couches qui coordonnent plusieurs agents, et bibliothèques de rôles, d'agents ou de skills où piocher."
modified: 2026-11-12
---

# Orchestration et catalogues d'agents

> Couches qui coordonnent plusieurs agents, et bibliothèques de rôles, d'agents ou de skills où piocher.

Zone : [[outils/index#Le poste de travail de l'agent|Le poste de travail de l'agent]] · Barème : [[Comparatif global des outils]]

## En bref

Plus de composants ne signifie pas de meilleurs résultats : les avis convergent vers « installer peu, épingler, mesurer ». Ruflo est le seul dont le discours a dû être corrigé après des audits.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Oh My Claude]]|Framework « batteries incluses » d'agents et workflows pour Claude Code.|Collection|[[Oh My Claude mémo\|Mémo]]|
|[[Ruflo]]|Meta-harnais expérimental pour essaims, mémoire et coordination autour de Claude Code ou Codex.|CLI|[[Ruflo mémo\|Mémo]]|
|[[Wshobson Agents]]|Marketplace modulaire et multi-harnais d'agents, skills, commandes et orchestrateurs.|Collection|[[Wshobson Agents mémo\|Mémo]]|
|[[Agency Agents]]|Plus de 230 définitions de rôles réparties en une quinzaine de divisions d'entreprise ; plus de rôles ne garantit pas de meilleurs résultats.|Collection|[[Agency Agents mémo\|Mémo]]|
|[[Alirezarezvani Claude Skills]]|Très vaste bibliothèque transversale de skills, agents, plugins et commandes.|Collection|[[Alirezarezvani Claude Skills mémo\|Mémo]]|

## Points d'attention

- Mesurer le gain réel face à un agent unique bien cadré.
- Installer peu de composants, épingler les versions et mesurer leur apport.
- Sélectionner et tester quelques rôles plutôt qu'un catalogue entier.
- Auditer les instructions et scripts comme toute dépendance logicielle.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Oh My Claude]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★★★☆|Doc abondante ; économie de 30–50 % non établie ; dépend d'une fonction expérimentale.|
|[[Ruflo]]|★★★★☆|★★☆☆☆|★★☆☆☆|**8**|★★★★☆|Doc abondante ; chiffres du README corrigés après audits ; expérimental, défauts ouverts.|
|[[Wshobson Agents]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★★☆|Doc par plugin ; auto-évaluation interne seulement ; catalogue récent à maintenir.|
|[[Agency Agents]]|★★★☆☆|★★★☆☆|★★★☆☆|**9**|★★★★★|Fichiers simples ; provenance des profils discutée ; pas de releases formelles.|
|[[Alirezarezvani Claude Skills]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★★★☆|Doc structurée ; compteurs variables, qualité hétérogène ; évolution rapide.|

## Critères propres à la famille

|Outil|Taille annoncée|Nature|Risque principal|
|---|---|---|---|
|[[Oh My Claude]]|19 agents, 39 skills|Orchestration multi-agent (Agent Teams expérimentaux)|Recouvrement avec les fonctions natives|
|[[Ruflo]]|98 agents, 314 outils MCP (annoncés)|Meta-harnais, essaims, mémoire|Écart historique entre discours et réalité|
|[[Wshobson Agents]]|94 plugins, 202 agents, 183 skills|Marketplace modulaire multi-harnais|Chaque plugin est une dépendance à auditer|
|[[Agency Agents]]|230+ rôles|Catalogue de personas en Markdown|Plus de rôles ne garantit pas de meilleurs résultats|
|[[Alirezarezvani Claude Skills]]|380 skills, 114 agents|Bibliothèque de skills et scripts|Qualité hétérogène, bruit de contexte|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[CrewAI]], [[LangGraph]], [[AutoGen]].

_Dernière analyse : 12 novembre 2026_
