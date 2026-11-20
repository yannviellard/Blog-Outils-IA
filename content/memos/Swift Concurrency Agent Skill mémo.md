---
title: "Swift Concurrency Agent Skill — Mémo"
type: memo
fiche: "[[Swift Concurrency Agent Skill]]"
date: 2026-11-20
---

# Swift Concurrency Agent Skill — Mémo

> Installer le skill et cadrer un diagnostic de concurrence Swift. Voir la fiche [[Swift Concurrency Agent Skill]] et les [[Swift Concurrency Agent Skill#Avis indépendants|avis indépendants]].

## Installation

```bash
npx skills@latest add \
  https://github.com/avdlee/swift-concurrency-agent-skill \
  --skill swift-concurrency
```

## Commandes principales

|Commande|Rôle|
|---|---|
|`/plugin marketplace add`|Ajouter le catalogue dans Claude Code.|
|`/plugin install`|Installer le plugin depuis ce catalogue.|

## Configuration et usage

Dans Claude Code, utiliser ces deux commandes dans l’ordre.

```text
/plugin marketplace add AvdLee/Swift-Concurrency-Agent-Skill
/plugin install swift-concurrency@swift-concurrency-agent-skill
```

## Conseils d'utilisation

Demander à l’agent d’utiliser `swift-concurrency`. Fournir le diagnostic complet, le mode Swift et l’isolation par défaut. Pour une migration, compiler et tester après chaque étape.

## Sources

- [Installation et usage officiels](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill)
- [Guide officiel de migration Swift 6](https://www.swift.org/migration/)
