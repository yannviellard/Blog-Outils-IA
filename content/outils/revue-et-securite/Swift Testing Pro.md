---
title: "Swift Testing Pro"
type: outil
description: "Guide la rédaction et la revue de tests avec le framework Swift Testing."
format: skill
tags:
  - metier/ingenierie
  - theme/tests
  - theme/revue-de-code
editeur: "Paul Hudson"
logo: "[[swift-testing-pro.png]]"
depot: "https://github.com/twostraws/Swift-Testing-Agent-Skill"
licence: "MIT"
statut: disponible
derniere_maj: 2026-05-17
etoiles: 483
forks: 20
etoiles_releve: 2026-11-20
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 2
memo: "[[Swift Testing Pro mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# Swift Testing Pro

> Swift Testing Pro est le skill `swift-testing-pro` de Paul Hudson pour aider les agents à écrire et relire des tests avec Swift Testing.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[Swift Testing Pro mémo|mémo pratique]].

## Résumé

Le [[Skill|skill]] donne à l’agent des références sur le framework Swift Testing et ses API. Le dépôt vise Swift 6.2 et ultérieur. Il documente une invocation directe et des demandes de revue ciblées.

## Fonctionnalités

- Déclaration des tests avec `@Test` et assertions avec `#expect` et `#require`.
- Paramétrage des cas, traits et organisation des suites.
- Confirmations asynchrones et tests de terminaison de processus.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|★★☆☆☆|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Popularité calculée à partir de 483 étoiles relevées via l’API GitHub le 20 novembre 2026._

### Points forts

La revue peut cibler une dimension précise, par exemple la paramétrisation d’une suite qui répète les mêmes assertions.

### Limites

La présence du skill ne lance pas la suite. Vérifier la disponibilité des API avec le toolchain et conserver les tests d’interface qui reposent sur XCTest et XCUIAutomation.

### Qualité

Le dépôt documente les usages courants. Les sources tierces disponibles confirment principalement le périmètre et l’installation. Dépôt lancé en mars 2026, dernière modification en mai 2026.

## Relations

- **Complémentaire de** [[SwiftUI Pro]] pour les changements d’interface, de [[Swift Concurrency Agent Skill]] pour les tests asynchrones et de [[MobileBuildMCP]] pour lancer la suite.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

SwiftSkills distingue la couverture des cas paramétrés et des confirmations. Le projet smorinlabs fournit un parcours d’intégration avec une révision amont identifiée.

### Ce qui est critiqué

Le catalogue SwiftAgents signale une cadence de mise à jour ralentie et indique ne pas évaluer le résultat. Les comparatifs consultés donnent peu de retours d’exécution sur des suites réelles.

### Ce qui n'est pas établi

Les sources consultées ne démontrent pas une réduction des tests intermittents ni une hausse de la couverture. Il manque des essais comparables sur plusieurs suites.

### Comparaison

[Swift Testing Expert d’Antoine van der Lee](https://github.com/AvdLee/Swift-Testing-Agent-Skill) couvre aussi la migration depuis XCTest et les traits. Les deux skills s’appuient sur le framework Swift Testing.

### Verdict

Pertinent pour une passe ciblée sur les assertions, les traits ou la paramétrisation. Mesurer la qualité de la modification en relançant la suite et en examinant ce que chaque assertion vérifie.

## Sources

- [Dépôt officiel](https://github.com/twostraws/Swift-Testing-Agent-Skill)
- [Documentation officielle de Swift Testing](https://developer.apple.com/documentation/testing)
- [Framework Swift Testing](https://github.com/swiftlang/swift-testing)

### Sources des avis

- [Comparatif SwiftSkills](https://swiftskills.dev/guides/swift-testing-ai-agents) — lecture comparative des README, sans mesure de qualité des tests.
- [Parcours d’installation smorinlabs](https://github.com/smorinlabs/ios-mac-skills) — intégration tierce avec révision inspectée.
- [Notice SwiftAgents](https://swiftagents.app/tools/swift-testing-pro/) — catalogue tiers qui indique ne pas tester ni recommander les outils listés.

_Dernière analyse : 20 novembre 2026_
