---
title: "Swift Testing Pro — Mémo"
type: memo
fiche: "[[Swift Testing Pro]]"
date: 2026-11-20
---

# Swift Testing Pro — Mémo

> Installer Swift Testing Pro et cibler la revue d’une suite Swift Testing. Voir la fiche [[Swift Testing Pro]] et les [[Swift Testing Pro#Avis indépendants|avis indépendants]].

## Installation

```bash
npx skills add \
  https://github.com/twostraws/swift-testing-agent-skill \
  --skill swift-testing-pro
```

## Commandes principales

|Commande|Rôle|
|---|---|
|`/swift-testing-pro`|Lancer le skill dans Claude Code.|
|`$swift-testing-pro`|Cibler le skill dans Codex.|

## Configuration et usage

Préciser le fichier ou la suite et la révision attendue. Par exemple, demander de repérer des tests qui partagent la même assertion et pourraient devenir des tests paramétrés.

## Conseils d'utilisation

Vérifier les prérequis de l’API Swift utilisée, puis exécuter la suite. En cas de migration partielle, conserver les tests d’interface existants dans XCTest.

## Sources

- [Installation et invocation officielles](https://github.com/twostraws/Swift-Testing-Agent-Skill)
- [Documentation du framework](https://developer.apple.com/documentation/testing)
