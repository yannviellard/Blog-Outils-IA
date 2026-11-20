---
title: "SwiftUI Pro — Mémo"
type: memo
fiche: "[[SwiftUI Pro]]"
date: 2026-11-20
---

# SwiftUI Pro — Mémo

> Installer le skill et demander une revue SwiftUI ciblée. Voir la fiche [[SwiftUI Pro]] et les [[SwiftUI Pro#Avis indépendants|avis indépendants]].

## Installation

```bash
npx skills add \
  https://github.com/twostraws/swiftui-agent-skill \
  --skill swiftui-pro
```

## Commandes principales

|Commande|Rôle|
|---|---|
|`/swiftui-pro`|Lancer le skill dans Claude Code.|
|`$swiftui-pro`|Cibler le skill dans Codex.|

## Configuration et usage

L’installeur propose un choix d’agents et une installation limitée au projet ou globale. Dans la demande de revue, préciser les vues, la version minimale du système et le thème à examiner.

## Conseils d'utilisation

Pour une revue d’accessibilité, relire les constats puis vérifier le comportement réel avec VoiceOver. Pour une revue de performance, conserver une mesure Instruments avant et après.

## Sources

- [Installation et invocation officielles](https://github.com/twostraws/SwiftUI-Agent-Skill)
