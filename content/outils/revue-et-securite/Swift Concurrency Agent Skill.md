---
title: "Swift Concurrency Agent Skill"
type: outil
description: "Aide à diagnostiquer les problèmes de concurrence et à migrer vers Swift 6."
format: skill
tags:
  - metier/ingenierie
  - theme/revue-de-code
  - theme/tests
editeur: "Antoine van der Lee"
logo: "[[swift-concurrency.png]]"
site: "https://www.swiftconcurrencycourse.com/"
depot: "https://github.com/AvdLee/Swift-Concurrency-Agent-Skill"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-06
etoiles: 1721
forks: 102
etoiles_releve: 2026-11-20
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 3
memo: "[[Swift Concurrency Agent Skill mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# Swift Concurrency Agent Skill

> Swift Concurrency Agent Skill, installé sous l’identifiant `swift-concurrency`, guide un agent sur `async/await`, les acteurs, `Sendable` et la concurrence stricte en Swift 6.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[Swift Concurrency Agent Skill mémo|mémo pratique]].

## Résumé

Ce [[Skill|skill]] d’Antoine van der Lee demande de partir du diagnostic et des réglages réels du projet. Il propose des références pour analyser les frontières d’isolation et préparer des migrations par étapes.

## Fonctionnalités

- Refactorisation de callbacks vers `async/await`, tâches structurées et annulation.
- Analyse de `@MainActor`, de la réentrance des acteurs et du passage de valeurs `Sendable`.
- Migration Swift 6, analyse des erreurs de compilation et tests du code concurrent.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|★★★☆☆|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Popularité calculée à partir de 1 721 étoiles relevées via l’API GitHub le 20 novembre 2026._

### Points forts

La démarche commence par le mode du langage, le niveau de vérification de concurrence et l’isolation par défaut. Les références couvrent aussi les tests et Core Data.

### Limites

Les règles dépendent du compilateur et des options du projet. Des tickets documentent des exemples à vérifier dans certaines configurations Swift 6.

### Qualité

Diagnostic et migration bien structurés. Les catalogues confirment le périmètre, tandis que des signalements portent sur la validité de certains exemples. Dépôt lancé en janvier 2026.

## Relations

- **Complémentaire de** [[SwiftUI Pro]] pour les appels asynchrones côté interface et de [[Swift Testing Pro]] pour les tests de comportements concurrents.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

SwiftSkills repère une couverture des migrations et des décisions d’isolation. Le dépôt d’intégration smorinlabs référence une révision inspectée et un parcours d’installation.

### Ce qui est critiqué

Un ticket avec des exemples reproductibles signale des extraits qui échouent en mode Swift 6 ou peuvent se bloquer. Il s’agit d’observations sur des exemples, avec leur contexte de compilation.

### Ce qui n'est pas établi

Aucune comparaison consultée ne mesure la baisse du nombre de courses de données ni le délai de migration avec et sans le skill.

### Comparaison

[Swift Concurrency Pro de Paul Hudson](https://github.com/twostraws/Swift-Concurrency-Agent-Skill) couvre aussi les acteurs et les tâches. Les diagnostics du compilateur apportent le retour concret pour valider une modification.

### Verdict

Point de départ pour trier des diagnostics d’isolation et relire une migration par étapes. Compiler après chaque changement de frontière d’isolation.

## Sources

- [Dépôt officiel](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill)
- [Documentation officielle du cours](https://www.swiftconcurrencycourse.com/)
- [Version 2.3.1](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill/releases/tag/2.3.1)
- [Guide officiel de migration Swift 6](https://www.swift.org/migration/)

### Sources des avis

- [Comparatif SwiftSkills](https://swiftskills.dev/guides/swift-concurrency-ai-agents) — comparatif de périmètre à partir des dépôts, sans évaluation de migration.
- [Parcours d’installation smorinlabs](https://github.com/smorinlabs/ios-mac-skills) — intégration tierce avec révision inspectée, sans mesure de résultat.
- [Ticket sur des exemples Swift 6](https://github.com/AvdLee/Swift-Concurrency-Agent-Skill/issues/56) — signalement détaillé dans le dépôt du projet.

_Dernière analyse : 20 novembre 2026_
