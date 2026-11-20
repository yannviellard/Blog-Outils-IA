---
title: "SwiftUI Pro"
type: outil
description: "Guide la revue SwiftUI sur les API, l’état des vues, les performances et l’accessibilité."
format: skill
tags:
  - metier/ingenierie
  - theme/frontend
  - theme/accessibilite
  - theme/revue-de-code
editeur: "Paul Hudson"
logo: "[[swiftui-pro.png]]"
depot: "https://github.com/twostraws/SwiftUI-Agent-Skill"
licence: "MIT"
statut: disponible
derniere_maj: 2026-10-26
etoiles: 6598
forks: 256
etoiles_releve: 2026-11-20
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 3
memo: "[[SwiftUI Pro mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# SwiftUI Pro

> SwiftUI Pro est le skill `swiftui-pro` de Paul Hudson pour écrire et relire le code SwiftUI avec un agent.

Voir aussi la section [[#Avis indépendants|Avis indépendants]] et le [[SwiftUI Pro mémo|mémo pratique]].

## Résumé

Le [[Skill|skill]] fournit des instructions et des références thématiques en complément des règles du projet. Il peut cadrer une revue générale ou cibler une question, comme une API dépréciée ou un problème de VoiceOver.

## Fonctionnalités

- Revue de l’état, de la navigation, de la mise en page et des animations.
- Recherche d’API dépréciées et vérification de la disponibilité des remplacements.
- Revue des mises à jour de vues et de l’accessibilité, notamment VoiceOver.

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★☆☆|

> _Notes alignées sur le [[Comparatif global des outils|barème global]]. Popularité calculée à partir de 6 598 étoiles relevées via l’API GitHub le 20 novembre 2026._

### Points forts

Le dépôt documente plusieurs modes d’installation et d’invocation. Une revue peut être limitée à un fichier ou à une dimension précise.

### Limites

La version 2 cible un outillage Swift récent. Vérifier les disponibilités pour la version minimale de l’application et mesurer les performances avec Instruments.

### Qualité

README et références détaillés, invocation démontrée publiquement et retour d’usage sur des revues ponctuelles. Dépôt lancé en mars 2026.

## Relations

- **Complémentaire de** [[MobileBuildMCP]] pour vérifier les vues sur simulateur, de [[Swift Concurrency Agent Skill]] pour l’isolation et de [[Swift Testing Pro]] pour la couverture des comportements.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

Peter Friese montre une installation et une revue effective dans Gemini CLI. Des utilisateurs sur Reddit décrivent des passes ciblées et citent des observations sur des API ou des usages de concurrence.

### Ce qui est critiqué

Un commentaire demande un comparatif avec et sans skill. Un ticket du dépôt signale un cas particulier des variables d’état dans les macros Preview.

### Ce qui n'est pas établi

Les exemples consultés ne permettent pas de quantifier les gains de performance, d’accessibilité ou de temps de revue.

### Comparaison

[SwiftUI Expert](https://github.com/AvdLee/SwiftUI-Agent-Skill) couvre un périmètre comparable. Une revue à partir de la documentation Apple reste possible avec les règles du projet et un périmètre explicite.

### Verdict

Adapté aux revues ciblées de vues SwiftUI. Contrôler les recommandations d’API avec le SDK du projet et les constats d’accessibilité sur l’app exécutée.

## Sources

- [Dépôt officiel](https://github.com/twostraws/SwiftUI-Agent-Skill)
- [Documentation Apple de SwiftUI](https://developer.apple.com/documentation/swiftui)
- [Version 2.0.0](https://github.com/twostraws/SwiftUI-Agent-Skill/releases/tag/2.0.0)

### Sources des avis

- [Démonstration de Peter Friese](https://www.youtube.com/watch?v=bjqrPpmxkKc) — revue montrée dans Gemini CLI par un tiers qui présente aussi Gemini.
- [Discussion SwiftUI](https://www.reddit.com/r/SwiftUI/comments/1rmigoi/swiftui_agent_skill_for_people_using_codex_claude/) — annonce de l’auteur et réponses indépendantes, de portée anecdotique.
- [Discussion sur les skills pour iOS](https://www.reddit.com/r/iOSProgramming/comments/1sngkcg/any_agent_skills_for_ios_development/) — préférence d’un utilisateur, sans protocole de comparaison.
- [Ticket sur les aperçus](https://github.com/twostraws/SwiftUI-Agent-Skill/issues/12) — cas signalé dans le dépôt public.

_Dernière analyse : 20 novembre 2026_
