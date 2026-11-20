---
title: "Revue, sécurité et création de skills"
type: famille
description: "Contrôle de la qualité du code et des extensions produits avec un agent."
modified: 2026-11-20
---

# Revue, sécurité et création de skills

> Contrôle de la qualité du code et des extensions produits avec un agent.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Ces outils assistent la revue et la validation du code. Les trois skills Swift couvrent les vues, l’isolation et les tests.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Claude Code Review]]|Première passe de revue de code intégrée au dépôt et au flux de développement.|Plugin|[[Claude Code Review mémo\|Mémo]]|
|[[Security Guidance]]|Garde-fou de sécurité pendant la génération et avant commit ou push.|Plugin|[[Security Guidance mémo\|Mémo]]|
|[[Skill Creator]]|Création, test comparatif et optimisation de skills avec un vrai cycle d'évaluation.|Skill|[[Skill Creator mémo\|Mémo]]|
|[[SwiftUI Pro]]|Guide la revue SwiftUI sur les API, l’état des vues, les performances et l’accessibilité.|Skill|[[SwiftUI Pro mémo\|Mémo]]|
|[[Swift Concurrency Agent Skill]]|Aide à diagnostiquer les problèmes de concurrence et à migrer vers Swift 6.|Skill|[[Swift Concurrency Agent Skill mémo\|Mémo]]|
|[[Swift Testing Pro]]|Guide la rédaction et la revue de tests avec le framework Swift Testing.|Skill|[[Swift Testing Pro mémo\|Mémo]]|

## Points d'attention

- Compléter avec tests, SAST/SCA et revue humaine.
- Auditer les instructions et scripts des skills comme toute dépendance logicielle.
- Vérifier les recommandations Swift avec le compilateur et le SDK du projet, puis exécuter les tests concernés.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Claude Code Review]]|★★★★★|★★★☆☆|★★★☆☆|**11**|—|Doc officielle complète ; chiffres internes ; fonctions en research preview.|
|[[Security Guidance]]|★★★★☆|★★★★☆|★★★☆☆|**11**|—|README précis, limites explicites ; plugin récent lié à la version de Claude Code.|
|[[Skill Creator]]|★★★★☆|★★★★☆|★★★☆☆|**11**|—|SKILL.md dense mais documenté, limites assumées ; circularité possible des évaluations.|
|[[SwiftUI Pro]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★☆☆|README et références détaillés, invocation démontrée publiquement et retour d’usage sur des revues ponctuelles. Dépôt lancé en mars 2026.|
|[[Swift Concurrency Agent Skill]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★★☆☆|Diagnostic et migration bien structurés. Les catalogues confirment le périmètre, tandis que des signalements portent sur la validité de certains exemples. Dépôt lancé en janvier 2026.|
|[[Swift Testing Pro]]|★★★★☆|★★★☆☆|★★★☆☆|**10**|★★☆☆☆|Le dépôt documente les usages courants. Les sources tierces disponibles confirment principalement le périmètre et l’installation. Dépôt lancé en mars 2026, dernière modification en mai 2026.|

## Critères propres à la famille

|Outil|Déclenchement|Coût|Limite principale|À compléter par|
|---|---|---|---|---|
|[[Claude Code Review]]|Local, cloud (ultra), service managé|0 / 5–25 $ / 15–25 $ par revue|Angles morts d'un même modèle ; chiffres internes|Second modèle, tests, humain|
|[[Security Guidance]]|Hooks à l'écriture et au commit|Appels API (×2 en mode dual)|Faux positifs et manqués ; pas un SAST|CodeQL, Semgrep, Snyk|
|[[Skill Creator]]|Cycle construire–évaluer–réviser|Tokens significatifs|Circularité des cas de test générés|Vrais cas + jeu de validation séparé|
|[[SwiftUI Pro]]|À la demande ou par l’agent|MIT, coût du client agent|Résultats dépendants du SDK et du contexte|Instruments, contrôles VoiceOver et revue humaine|
|[[Swift Concurrency Agent Skill]]|À la demande ou par l’agent|MIT, coût du client agent|Sensibilité aux réglages Swift et aux versions du compilateur|Build Swift 6 et tests d’annulation et d’isolation|
|[[Swift Testing Pro]]|À la demande ou par l’agent|MIT, coût du client agent|Portée centrée sur Swift Testing|Exécution de la suite et tests UI existants|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[CodeRabbit]], [[GitHub Copilot Code Review]], [[Cursor Bugbot]].

_Dernière analyse : 20 novembre 2026_
