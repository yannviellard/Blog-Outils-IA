---
title: "Mémoire d'agent"
type: concept
description: "Ce qu'un agent conserve d'une session à l'autre : fichiers d'instructions, notes qu'il écrit lui-même ou outils de mémoire dédiés."
aliases:
  - Mémoire
  - Agent memory
modified: 2026-11-12
---

# Mémoire d'agent

> Ce qu'un agent conserve d'une session à l'autre : fichiers d'instructions, notes qu'il écrit lui-même ou outils de mémoire dédiés.

Un agent démarre chaque session avec une fenêtre de contexte vide : sans dispositif particulier, il ne sait rien de ce qui a été dit ou fait la veille. La **mémoire d'agent** regroupe les moyens de lui transmettre ce savoir : fichiers d'instructions relus à chaque démarrage, notes que l'agent tient lui-même, fichiers de travail dans le dépôt, ou outils dédiés qui stockent et retrouvent l'historique.

## Fonctionnement

- **Fichiers d'instructions** : Claude Code lit au démarrage les fichiers `CLAUDE.md` de l'organisation, de l'utilisateur (`~/.claude/CLAUDE.md`), du projet (`./CLAUDE.md`) et le fichier local non versionné `CLAUDE.local.md`. Il peut lire à la place un `AGENTS.md`, convention partagée avec d'autres agents. La documentation recommande moins de 200 lignes par fichier.
- **Mémoire automatique** : Claude Code note lui-même, dans `~/.claude/projects/<projet>/memory/`, ce qu'il juge utile pour plus tard (préférences, corrections, décisions). L'index `MEMORY.md` est chargé à chaque session, dans la limite de 200 lignes ou 25 Ko. Cette mémoire est activée par défaut dans les sessions locales.
- **Fichiers de travail** : un plan ou un journal de progression tenu dans le dépôt sert de mémoire explicite pour une tâche longue ([[Planning with Files]] ; méthode décrite par Anthropic pour les agents de longue durée, voir [[Harnais d'agent]]).
- **Outils dédiés** : base locale alimentée automatiquement (par exemple par des [[Hook|hooks]]) et interrogée par recherche ou par [[Model Context Protocol|MCP]] ([[Claude-Mem]], [[MemPalace]]), ou graphe du code ([[Graphify]]).

## Points de vigilance

- **Du contexte, pas une règle.** La documentation de Claude Code précise que ces fichiers sont traités comme du contexte et non comme une configuration imposée : pour bloquer une action à coup sûr, il faut un [[Hook|hook]].
- **Obsolescence.** Une mémoire non relue conserve des informations périmées ou fausses ; les avis sur [[Claude-Mem]] signalent des faux souvenirs et un coût en tokens.
- **Coût.** Tout ce qui est chargé au démarrage occupe le contexte à chaque session.
- **L'alternative transparente** reste la mémoire native et des fichiers Markdown relus à la main (voir [[outils/memoire-et-contexte/index|Mémoire et contexte]]).

## Dans le wiki

- Famille [[outils/memoire-et-contexte/index|Mémoire et contexte]] : [[Claude-Mem]], [[MemPalace]], [[Graphify]].
- [[Planning with Files]] (mémoire de travail en trois fichiers), [[Hermes Agent]] (assistant persistant avec mémoire).
- Les fiches concernées portent le thème [[tags/theme/memoire|Mémoire]].

## Sources

- [Claude Code, How Claude remembers your project](https://code.claude.com/docs/en/memory) : documentation officielle, consultée le 12 novembre 2026.
- [Anthropic, Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) : article de l'éditeur, 26 novembre 2025.

_Dernière analyse : 12 novembre 2026_
