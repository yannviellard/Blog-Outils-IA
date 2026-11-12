---
title: "Mémoire et contexte"
type: famille
description: "Outils qui conservent ou structurent ce que l'agent sait d'un projet, d'une session à l'autre."
modified: 2026-11-12
---

# Mémoire et contexte

> Outils qui conservent ou structurent ce que l'agent sait d'un projet, d'une session à l'autre.

Zone : [[outils/index#Le poste de travail de l'agent|Le poste de travail de l'agent]] · Barème : [[Comparatif global des outils]]

## En bref

La mémoire native et des fichiers Markdown relus à la main restent l'alternative la plus transparente ; ces outils se justifient quand le coût de l'oubli dépasse celui de l'infrastructure.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Claude-Mem]]|Mémoire automatique intersession ; utile quand le coût de l'oubli justifie l'infrastructure.|Plugin|[[Claude-Mem mémo\|Mémo]]|
|[[MemPalace]]|Mémoire locale partagée entre agents, à tester sur ses propres cas avant adoption sensible.|CLI|[[MemPalace mémo\|Mémo]]|
|[[Graphify]]|Knowledge graph déterministe pour cartographier et interroger un codebase.|CLI|[[Graphify mémo\|Mémo]]|

## Points d'attention

- Éviter que la mémoire ou le graphe devienne obsolète.
- L'ancrage dans une source ne garantit pas que cette source est juste ou à jour.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Claude-Mem]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★★★★|Doc correcte ; coût en tokens rapporté ; nombreux correctifs worker/hooks.|
|[[MemPalace]]|★★★★☆|★★☆☆☆|★★☆☆☆|**8**|★★★★☆|Doc améliorée ; benchmarks surtout internes, analyses critiques ; fiabilité du stockage à surveiller.|
|[[Graphify]]|★★★★☆|★★★☆☆|★★☆☆☆|**9**|★★★★★|Doc détaillée ; benchmarks du projet ; très récent (branche v8), dette technique visible.|

## Critères propres à la famille

|Outil|Stockage|Alimentation|Risque principal|Alternative simple|
|---|---|---|---|---|
|[[Claude-Mem]]|SQLite + Chroma, local|Automatique par hooks|Tokens, faux souvenirs|Mémoire native + fichiers|
|[[MemPalace]]|Local-first, verbatim, MCP|Automatique par hooks|Benchmarks internes, fiabilité du stockage|Mémoire native + fichiers|
|[[Graphify]]|Graphe `graph.json`, MCP|Analyse batch, mise à jour incrémentale|Langages dynamiques, projet très récent|Sourcegraph, Serena, index sémantique|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[Mem0]], [[Supermemory]], [[Engram]].

_Dernière analyse : 12 novembre 2026_
