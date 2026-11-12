---
title: "Agents de développement"
type: famille
description: "Agents complets qui lisent un dépôt, modifient le code et exécutent des commandes ; ils servent de socle aux autres outils."
modified: 2026-11-12
---

# Agents de développement

> Agents complets qui lisent un dépôt, modifient le code et exécutent des commandes ; ils servent de socle aux autres outils.

Zone : [[outils/index#Le poste de travail de l'agent|Le poste de travail de l'agent]] · Barème : [[Comparatif global des outils]]

## En bref

Pas de vainqueur universel. Claude Code domine l'exploration d'un dépôt et l'extensibilité ; Codex la délégation, la revue et la CI avec une consommation de tokens plus sobre ; OpenCode le contrôle et l'absence de verrouillage ; Hermes n'est pas d'abord un agent de code mais un assistant persistant.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Claude Code]]|Agent de développement très extensible, particulièrement fort pour explorer un dépôt et conduire des tâches longues.|Agent|[[Claude Code mémo\|Mémo]]|
|[[OpenAI Codex]]|Agent efficace pour déléguer des tâches bien spécifiées, automatiser et relire le code.|Agent|[[OpenAI Codex mémo\|Mémo]]|
|[[OpenCode]]|Harnais open source et multi-modèles pour les équipes qui privilégient le contrôle et l'absence de verrouillage.|Agent|[[OpenCode mémo\|Mémo]]|
|[[Hermes Agent]]|Assistant persistant, auto-hébergeable et polyvalent, avec mémoire, outils, messagerie et tâches planifiées.|Agent|[[Hermes Agent mémo\|Mémo]]|

## Points d'attention

- Choisir selon le besoin d'exploration, de délégation, d'ouverture ou de persistance.
- Pour une automatisation avec [[Hermes Agent]], limiter les permissions et garder une procédure de reprise manuelle.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Claude Code]]|★★★★★|★★★★☆|★★★★☆|**13**|★★★★★|Doc versionnée de référence ; chiffres internes non reproduits ; ~16 mois, régression et incidents corrigés.|
|[[OpenAI Codex]]|★★★★★|★★★★☆|★★★★☆|**13**|★★★★★|Doc exhaustive ; fonctions variables selon forfait ; ~17 mois, failles de sandbox corrigées vite.|
|[[OpenCode]]|★★★★☆|★★★☆☆|★★★★☆|**11**|★★★★★|Doc correcte ; sources uniquement officielles ; forte adoption mais évolution rapide, peu de retours indépendants.|
|[[Hermes Agent]]|★★★★★|★★★☆☆|★★★☆☆|**11**|★★★★★|Doc très approfondie ; promesse d'auto-amélioration contestée ; jeune (v0.x), CVE historiques.|

## Critères propres à la famille

|Outil|Ouverture|Modèles|Isolation par défaut|Prévisibilité des coûts|Plus fort pour|
|---|---|---|---|---|---|
|[[Claude Code]]|Propriétaire (le dépôt public ne contient pas le code de la CLI)|Claude (API, Bedrock, Google Cloud, Foundry)|6 modes de permission, classifieur auto, sandbox Bash|Faible : quotas modifiés plusieurs fois en 2026|Explorer un dépôt, tâches longues, écosystème d'extensions|
|[[OpenAI Codex]]|CLI Apache-2.0 (contributions externes refusées) ; cloud et application propriétaires|Modèles OpenAI (locaux via `--oss`)|Sandbox au niveau du système ; deux évasions corrigées en août 2026|Faible à moyenne : fenêtres de 5 h ; tokens plus sobres|Déléguer, relire, automatiser en CI|
|[[OpenCode]]|MIT|75+ fournisseurs, modèles locaux|Dépend de la configuration choisie|Variable : l'économie n'est pas garantie avec un modèle premium|Contrôle, absence de verrouillage|
|[[Hermes Agent]]|MIT|Multi-fournisseurs, modèles locaux|8 couches documentées ; 3 CVE historiques ; sandbox recommandé|Moyenne : la revue en arrière-plan consomme des jetons|Assistant persistant (mémoire, messagerie, cron)|

## Absents notables

Agents de développement cités dans le wiki sans fiche pour l'instant : [[Cursor]] (donné comme alternative dans ces fiches), [[GitHub Copilot]] et [[Gemini CLI]] (cités dans d'autres fiches).

_Dernière analyse : 12 novembre 2026_
