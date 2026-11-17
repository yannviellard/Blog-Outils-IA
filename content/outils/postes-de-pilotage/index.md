---
title: "Postes de pilotage multi-agent"
type: famille
description: "Applications et terminaux qui font travailler plusieurs agents en parallèle, chacun sur sa branche, avec un point de revue commun."
modified: 2026-11-15
---

# Postes de pilotage multi-agent

> Applications et terminaux qui font travailler plusieurs agents en parallèle, chacun sur sa branche, avec un point de revue commun.

Zone : [[outils/index#Le poste de travail de l'agent|Le poste de travail de l'agent]] · Barème : [[Comparatif global des outils]]

## En bref

Deux approches : des orchestrateurs centrés sur la tâche, le worktree et la revue (Paradev, Conductor, Parallel Code, Claude Squad) et des terminaux de supervision qui laissent l'organisation Git à l'utilisateur (cmux, Warp). Dans tous les cas, un worktree évite les écrasements directs mais n'isole ni les ports, ni les bases de données, ni les secrets, et n'est pas une frontière de sécurité.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Paradev]]|IDE agentique local et multi-harnais (anciennement Superset) avec worktrees, terminaux persistants, diff et navigateur.|Application|[[Paradev mémo\|Mémo]]|
|[[Conductor]]|Application macOS guidée pour exécuter, relire et fusionner des agents dans des workspaces isolés.|Application|[[Conductor mémo\|Mémo]]|
|[[Parallel Code]]|Application MIT, locale et sans compte pour lancer plusieurs CLI dans des worktrees.|Application|[[Parallel Code mémo\|Mémo]]|
|[[Claude Squad]]|TUI fondée sur tmux et Git worktrees pour piloter plusieurs agents CLI.|CLI|[[Claude Squad mémo\|Mémo]]|
|[[cmux]]|Terminal macOS natif centré sur les splits, notifications et agents demandant de l'attention.|Application|[[cmux mémo\|Mémo]]|
|[[Warp]]|Terminal multiplateforme avec agent intégré et orchestration cloud Oz.|Application|[[Warp mémo\|Mémo]]|

## Points d'attention

- Isoler les tâches par worktree et limiter le nombre de travaux simultanés à ce qui peut réellement être relu.
- Les worktrees évitent les écrasements directs entre tâches, mais pas les conflits de fusion ni les collisions de ports, bases de données ou services locaux (voir [[Worktree]]).

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Paradev]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★★☆|Doc officielle (CLI, SDK, MCP) ; fonctions confirmées par les retours ; produit de 13 mois, renommé et passé sous licence MIT en novembre 2026, évolution rapide.|
|[[Conductor]]|★★★★☆|★★★★☆|★★★☆☆|**11**|—|Doc claire et à jour ; critiques anciennes en partie corrigées ; macOS seulement, produit fermé.|
|[[Parallel Code]]|★★★☆☆|★★★☆☆|★★☆☆☆|**8**|★★★☆☆|README et politique de confidentialité ; peu d'avis indépendants, beaucoup de contenus du créateur ; projet jeune.|
|[[Claude Squad]]|★★★☆☆|★★★★☆|★★★☆☆|**10**|★★★☆☆|README et issues ; limites honnêtes ; comportement fragile autour de tmux et de Windows.|
|[[cmux]]|★★★★☆|★★★★☆|★★★☆☆|**11**|★★★★☆|Doc et API documentées ; performances et notifications confirmées ; fonctions mobiles/cloud récentes.|
|[[Warp]]|★★★★★|★★★★☆|★★★★☆|**13**|★★★★☆|Doc de référence ; changements d'interface et de tarifs contestés ; terminal établi, couche agentique récente.|

## Critères propres à la famille

|Outil|Plateformes|Licence|Isolation Git|Revue intégrée|Coût|
|---|---|---|---|---|---|
|[[Paradev]]|macOS ; Linux expérimental ; pas de Windows|MIT (depuis le 4 novembre 2026)|Worktree et branche par tâche|Diff, commentaires, pull requests|Local gratuit ; Pro 20 $/mois, Team 60 $/mois|
|[[Conductor]]|macOS|Propriétaire|Worktree par workspace ; sandboxes Linux cloud (payant)|Diff, checks GitHub, commentaires|Local gratuit, cloud payant|
|[[Parallel Code]]|macOS, Linux|MIT|Worktree par tâche ; Docker optionnel|Diff, commentaires, mode Arena|Gratuit, sans compte|
|[[Claude Squad]]|Unix (tmux requis) ; Windows fragile|AGPL-3.0|Session tmux + worktree|Aperçu de diff, commit/push|Gratuit|
|[[cmux]]|macOS (TUI pour Linux et Windows)|GPL-3.0-or-later|Aucune imposée|Non (navigateur et API scriptables)|Gratuit|
|[[Warp]]|macOS, Linux, Windows|AGPL-3.0 (client) ; services commerciaux|Non centrale ; agents cloud (Oz)|Diff et agent intégrés|Crédits, offres payantes|

_Dernière analyse : 15 novembre 2026_
