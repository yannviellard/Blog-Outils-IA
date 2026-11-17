---
title: "Recherche et veille"
type: famille
description: "Accès au web et synthèse de sources, pour l'agent ou pour l'utilisateur."
modified: 2026-11-15
---

# Recherche et veille

> Accès au web et synthèse de sources, pour l'agent ou pour l'utilisateur.

Zone : [[outils/index#Produire et décider|Produire et décider]] · Barème : [[Comparatif global des outils]]

## En bref

Choisir selon la source : le web ouvert (Gemini Deep Research, Perplexity), un corpus maîtrisé (NotebookLM), les pages à extraire (Firecrawl) ou les réseaux sociaux (Agent Reach). Aucun ne dispense de lire les sources primaires.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Gemini Deep Research]]|Recherche web multi-étapes et rapports longs, notamment dans l'écosystème Google.|Application|—|
|[[NotebookLM]]|Lecture et synthèse ancrées dans un corpus choisi, avec citations et formats pédagogiques.|Application|—|
|[[Perplexity MCP]]|Serveur MCP officiel de Perplexity, hébergé ou local : recherche web, réponses sourcées, raisonnement et recherche approfondie, facturés à l'usage.|Serveur MCP|[[Perplexity MCP mémo\|Mémo]]|
|[[Agent Reach]]|Installation et routage d'outils d'accès à de nombreuses plateformes web et sociales.|CLI|[[Agent Reach mémo\|Mémo]]|
|[[Firecrawl]]|Recherche, scraping et crawl rendus en Markdown ou JSON prêts pour les LLM.|API|[[Firecrawl mémo\|Mémo]]|

## Points d'attention

- Vérifier les sources primaires et les citations.
- Lire les passages sources importants, pas seulement la synthèse.
- L'ancrage dans une source ([[NotebookLM]]) ne garantit pas que cette source est juste ou à jour.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Gemini Deep Research]]|★★★☆☆|★★★☆☆|★★★★☆|**10**|—|Une page produit et des billets Google ; comparaisons contradictoires ; lancé fin 2024.|
|[[NotebookLM]]|★★★☆☆|★★★☆☆|★★★★☆|**10**|—|Documentation éditeur ; tests indépendants favorables ; établi depuis 2023, rebranding récent.|
|[[Perplexity MCP]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★☆☆|Doc officielle complète (serveur distant, local, auto-hébergé) ; avis concordants mais documentaires, sans test pratique ; 20 mois, moteurs passés de Sonar à l'Agent API en 2026.|
|[[Agent Reach]]|★★★★☆|★★★☆☆|★★☆☆☆|**9**|★★★★★|Doc d'installation ; fiabilité dépendante de backends fragiles ; migrations fréquentes.|
|[[Firecrawl]]|★★★★☆|★★★★☆|★★★★☆|**12**|★★★★★|Doc complète ; réserves sur coûts et auto-hébergement ; service établi.|

## Critères propres à la famille

|Outil|Type|Source interrogée|Contrôle du corpus|Limite principale|
|---|---|---|---|---|
|[[Gemini Deep Research]]|Application|Web, Workspace|Faible|Citations imparfaites, verdicts contradictoires|
|[[NotebookLM]]|Application|Corpus fourni|Élevé|Une source erronée reste erronée|
|[[Perplexity MCP]]|Serveur MCP officiel (hébergé ou local)|Web, via l'API Perplexity|Moyen|Payant à l'usage ; synthèse dont les sources restent à vérifier|
|[[Agent Reach]]|Installeur / routeur d'outils|Réseaux sociaux et plateformes|Local|Fragilité des backends, CGU|
|[[Firecrawl]]|API / open source|Pages web en Markdown/JSON|Élevé|Coût à volume, anti-bot|

_Dernière analyse : 15 novembre 2026_
