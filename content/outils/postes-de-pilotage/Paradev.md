---
title: "Paradev"
type: outil
description: "IDE agentique local et multi-harnais (anciennement Superset) avec worktrees, terminaux persistants, diff et navigateur."
format: application
tags:
  - metier/ingenierie
  - theme/multi-agent
  - theme/revue-de-code
editeur: "Paradev (anciennement Superset)"
site: "https://paradev.com"
depot: "https://github.com/ParadevAI/Paradev"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-15
etoiles: 16323
forks: 1463
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[Paradev mémo]]"
avis_maj: 2026-11-15
modified: 2026-11-15
---

# Paradev

> IDE agentique local pour exécuter Claude Code, Codex, OpenCode, Gemini CLI, Cursor Agent et d'autres CLI dans des worktrees isolés, avec terminaux persistants, revue de diff et navigateur intégré. Anciennement Superset ; sans lien avec Apache Superset, l'outil de business intelligence.

**Composition** : skills intégrées (`superset:*`), CLI, SDK TypeScript, 1 serveur MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Paradev mémo]] pour le mémo pratique.

## Résumé

Paradev remplace l'empilement de terminaux par un poste de pilotage centré sur la tâche. Chaque workspace peut recevoir sa propre branche et son propre Git [[Worktree|worktree]] ; l'agent y exécute ses commandes sans modifier directement le checkout principal. L'application regroupe le terminal, le suivi d'état des agents, le diff, les commentaires de revue, les previews web et les opérations GitHub.

Le produit s'appelait Superset jusqu'au 26 octobre 2026 : le renommage a été annoncé avec une levée de fonds d'amorçage (11,5 millions de dollars selon la presse spécialisée). La CLI garde le nom `superset` (avec l'alias `paradev`) et les dépôts configurés avant le renommage conservent leur dossier `.superset/`.

Le produit ne fournit pas le modèle : il lance les agents déjà installés et utilise les abonnements ou clés existants, sans relayer les appels aux modèles selon l'éditeur. L'offre gratuite couvre un utilisateur, les workspaces locaux, l'application et la CLI ; Pro (20 $ par utilisateur et par mois) ajoute l'accès distant, les automatisations, les intégrations Linear et Slack et l'application iPhone et iPad ; Team (60 $) ajoute des workspaces dans le cloud. Le code est publié sous licence MIT depuis le 4 novembre 2026, après neuf mois sous Elastic License 2.0.

## Fonctionnalités

- Worktree et branche par tâche, ou checkout local partagé lorsque l'isolation est inutile.
- Terminaux persistants avec onglets, splits, presets et indicateurs d'attention.
- Diff intégré, commentaires en ligne, commit, push et parcours de pull request (checks, fils de revue, fusion).
- Navigateur intégré avec détection des ports par workspace et mode de sélection visuelle (« Design »).
- CLI, SDK TypeScript et serveur [[Model Context Protocol|MCP]] pour créer et superviser des workspaces depuis un script ou un agent.
- Accès distant, application iPhone et iPad, automatisations planifiées ou déclenchées par un événement (offre Pro) ; workspaces cloud (offre Team).
- Scripts `setup`, `run` et `teardown` dans `.paradev/config.json` (ou `.superset/config.json` pour les dépôts plus anciens).

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (11 octobre 2026, revues le 15 novembre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 16 323 au 16 novembre 2026._

### Points forts

- Prend en charge de nombreux harnais sans réécrire leur interface CLI.
- Réunit orchestration, terminal, revue et preview dans un même espace.
- Les sessions continuent via le service local même si l'interface redémarre.
- Données et appels aux fournisseurs restent locaux par défaut, selon l'éditeur.
- Configuration des environnements reproductible dans le dépôt.
- Licence MIT depuis le 4 novembre 2026 : le code peut être réutilisé sans les restrictions de l'Elastic License 2.0.

### Limites

- Interface plus dense et plus lourde qu'un terminal natif.
- macOS d'abord : Linux en AppImage x64 expérimentale, pas de version Windows au 15 novembre 2026.
- Les worktrees n'isolent ni processus, ni ports, ni bases de données, ni secrets.
- Un sous-agent qui crée lui-même des worktrees peut entrer en conflit avec la structure de Paradev.
- Renommage récent : la CLI (`superset`), les variables (`SUPERSET_ROOT_PATH`) et une partie des documents tiers portent encore l'ancien nom.
- Deux changements de licence en neuf mois (Elastic License 2.0 le 4 février 2026, MIT le 4 novembre 2026) : le modèle économique est encore en mouvement.

### Qualité

**Commentaire :** bon compromis pour un développeur qui souhaite rester libre de choisir ses agents tout en automatisant les worktrees et la revue ; les retours indépendants confirment surtout les notifications, la persistance des terminaux et la lisibilité des workspaces, pas un gain de temps mesuré. Voir [[#Avis indépendants|les avis indépendants]] pour les retours utilisateurs et [[Paradev mémo]] pour la configuration.

## Relations

- **Alternative à :** [[Conductor]], [[Parallel Code]], [[cmux]], [[Claude Squad]]
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], GitHub, Linear, Slack
- **Utilise :** Git worktrees, terminaux locaux, CLI d'agents

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 15 novembre 2026._

### Ce qui est apprécié

- Les agents s'exécutent dans de vrais terminaux et conservent leur comportement natif.
- Les notifications réduisent la surveillance manuelle : la barre latérale indique quel agent travaille, a fini ou attend une réponse.
- Les workspaces et branches sont plus lisibles qu'une collection d'onglets anonymes ; plusieurs utilisateurs venant d'iTerm2 ou de terminaux divisés y retrouvent la même souplesse, avec worktrees et revue en plus.
- Le service local persistant protège mieux les longues sessions lors des mises à jour.
- La gratuité du mode local permet un essai sérieux avant tout abonnement.

### Ce qui est critiqué

- Courbe d'apprentissage de l'interface et densité des panneaux ; l'interface est jugée moins immédiate que celle de [[Conductor]].
- Coût de préparation de chaque worktree : dépendances, `.env`, ports et bases.
- Linux expérimental et pas de version Windows : le comparatif d'Autonomous (29 octobre 2026) le range parmi les principales limites.
- Complexité lorsqu'un agent interne crée ses propres sous-agents ou worktrees.
- Évolution très rapide : le dépôt compte 1 299 issues et pull requests ouvertes au 15 novembre 2026 ; elles montrent des corrections fréquentes, mais aussi des régressions.

### Ce qui n'est pas établi

- Aucun test indépendant ne mesure un gain de temps ou de qualité par rapport à un seul agent bien utilisé.
- Les articles parus lors du renommage (TechBytes, 26 octobre 2026) reprennent le communiqué de l'éditeur, y compris des affirmations non vérifiées (certification SOC 2 Type II, traitement local des données).
- Le montant et la date de clôture de la levée de fonds diffèrent selon les sources.

### Comparaison

[[Conductor]] propose un parcours plus guidé « une tâche, un workspace, une PR », mais reste fermé et limité à macOS. [[Parallel Code]] est plus léger et gratuit, avec moins d'intégrations. [[cmux]] et [[Warp]] laissent l'organisation Git à l'utilisateur. [[Claude Squad]] convient mieux à un serveur ou à SSH, sans revue graphique. Paradev se distingue par l'étendue de ses surfaces (CLI, SDK, MCP, mobile, automatisations) et, depuis novembre 2026, par sa licence MIT.

### Verdict

Adapté à deux à cinq flux parallèles avec revue fréquente. Il apporte moins lorsqu'un développeur travaille surtout dans un seul checkout ou possède déjà une configuration tmux et worktrees maîtrisée.

## Sources

- [Dépôt officiel](https://github.com/ParadevAI/Paradev)
- [Documentation](https://docs.paradev.com)
- [Tarifs](https://paradev.com/pricing)
- [Changement de licence vers MIT (pull request n° 9356, 4 novembre 2026)](https://github.com/ParadevAI/Paradev/pull/9356)
- [Renommage du produit (pull request n° 8874, 26 octobre 2026)](https://github.com/ParadevAI/Paradev/pull/8874)

### Sources des avis

- [Discussion : orchestrateurs utilisés au quotidien](https://www.reddit.com/r/ClaudeCode/comments/1viwdnh/what_orchestrator_are_you_using/) : témoignages d'utilisateurs ; la discussion contient aussi des réponses de fondateurs et d'éditeurs concurrents.
- [Comparaison Conductor, Superset et cmux](https://www.reddit.com/r/ClaudeCode/comments/1rxwkoz/my_thoughts_on_conductor_vs_superset_vs_cmux_vs/) : retour d'un utilisateur ayant essayé les trois ; avis personnel, non mesuré.
- [11 Conductor Alternatives Compared by Platform and Price — Autonomous](https://www.autonomous.ai/ourblog/conductor-alternatives) : comparatif du 29 octobre 2026 fondé sur les sites des éditeurs ; l'éditeur du blog vend un produit voisin (Harness Pro).
- [Paradev: one workspace for Claude Code, Codex and any coding agent — TechBytes](https://techbytes.app/posts/paradev-one-workspace-for-claude-code-codex-and-any-coding/) : article du 26 octobre 2026 largement fondé sur le communiqué de l'éditeur.
- [Issues du dépôt](https://github.com/ParadevAI/Paradev/issues) : régressions et demandes publiques ; reflètent les problèmes signalés, pas leur fréquence réelle.

_Dernière analyse : 15 novembre 2026_
