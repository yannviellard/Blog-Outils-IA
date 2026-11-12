---
title: "Superset"
type: outil
description: "IDE agentique local et multi-harnais avec worktrees, terminaux persistants, diff et navigateur."
format: application
tags:
  - metier/ingenierie
  - theme/multi-agent
  - theme/revue-de-code
editeur: "Superset (devenu Paradev)"
site: "https://superset.sh"
depot: "https://github.com/superset-sh/superset"
licence: "Elastic License 2.0"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 16215
forks: 1454
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[Superset mémo]]"
avis_maj: 2026-10-10
modified: 2026-11-12
---

# Superset

> IDE agentique local pour exécuter Codex, Claude Code, Gemini, OpenCode, Cursor Agent et d'autres CLI dans des worktrees isolés, avec terminaux persistants, revue de diff et navigateur intégré.

**Composition** : skills intégrées, 100+ agents (annoncés), 1 serveur MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Superset mémo]] pour le mémo pratique.

## Résumé

Superset remplace l'empilement de terminaux par un poste de pilotage centré sur la tâche. Chaque workspace peut recevoir sa propre branche et son propre Git worktree ; l'agent y exécute ses commandes sans modifier directement le checkout principal. L'application regroupe le terminal, le suivi d'état, le diff, les commentaires de revue, les previews web et les opérations GitHub.

Le produit ne fournit pas le modèle : il lance les agents déjà installés et utilise les abonnements ou clés existants. L'application locale individuelle et les workspaces locaux sont gratuits. Pro ajoute notamment fonctions distantes et services d'équipe. Le code est publié sous Elastic License 2.0 : il est consultable et modifiable, mais ne peut pas être revendu tel quel comme service concurrent.

## Fonctionnalités

- Worktree et branche par tâche, ou checkout local partagé lorsque l'isolation est inutile.
- Terminaux persistants avec onglets, splits, presets et indicateurs d'attention.
- Diff intégré, commentaires en ligne, commit, push et parcours de pull request.
- Navigateur intégré avec détection des ports et mode de sélection visuelle.
- CLI, SDK TypeScript et serveur MCP pour créer et superviser des workspaces.
- Accès distant, application mobile et automatisations planifiées selon l'offre.
- Scripts `setup`, `run` et `teardown` dans `.superset/config.json`.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (11 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 16 215 au 11 novembre 2026._

### Points forts

- Supporte de nombreux harnais sans réécrire leur interface CLI.
- Réunit orchestration, terminal, revue et preview dans un même espace.
- Les sessions continuent via le service local même si l'interface redémarre.
- Données et appels aux fournisseurs restent locaux par défaut.
- Configuration des environnements reproductible dans le dépôt.

### Limites

- Interface plus dense et plus lourde qu'un terminal natif.
- Linux reste secondaire et Windows n'est pas officiellement pris en charge.
- Les worktrees n'isolent ni processus, ni ports, ni bases de données, ni secrets.
- Un sous-agent qui crée lui-même des worktrees peut entrer en conflit avec la structure de Superset.
- L'argument « 100+ agents » décrit une capacité technique, pas une charge humainement supervisable.

### Qualité

**Commentaire :** bon compromis pour un développeur qui souhaite rester libre de choisir ses agents tout en automatisant les worktrees et la revue ; les retours indépendants confirment surtout les notifications, la persistance des terminaux et la lisibilité des workspaces, pas un gain de temps mesuré. Voir [[#Avis indépendants|les avis indépendants]] pour les retours utilisateurs et [[Superset mémo]] pour la configuration.

## Relations

- **Alternative à :** [[Conductor]], [[Parallel Code]], [[cmux]], [[Claude Squad]]
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], GitHub, Linear, Slack
- **Utilise :** Git worktrees, terminaux locaux, CLI d'agents

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 10 octobre 2026._

### Synthèse

Les retours favorables insistent sur trois bénéfices concrets : retrouver toutes les sessions dans une seule barre latérale, recevoir une notification lorsqu'un agent attend et laisser les terminaux continuer pendant une mise à jour ou une fermeture « douce » de l'interface. Plusieurs utilisateurs venant d'iTerm2 ou de terminaux divisés considèrent que Superset leur apporte la même souplesse, avec worktrees et revue en plus.

Les réserves concernent surtout l'interface, jugée moins élégante ou moins immédiate que celle de [[Conductor]], et la complexité qui apparaît lorsqu'un agent interne crée ses propres sous-agents ou worktrees. Les issues publiques montrent aussi un produit qui évolue très vite : c'est positif pour la correction des problèmes, mais cela implique des régressions et changements fréquents.

### Ce qui revient dans les avis positifs

- Les agents s'exécutent dans de vrais terminaux et conservent leur comportement natif.
- Les notifications réduisent la surveillance manuelle.
- Les workspaces et branches sont plus lisibles qu'une collection d'onglets anonymes.
- Le service local persistant protège mieux les longues sessions lors des mises à jour.
- La gratuité du mode local permet un essai sérieux avant tout abonnement.

### Critiques récurrentes

- Courbe d'apprentissage de l'interface et densité des panneaux.
- Coût de préparation de chaque worktree : dépendances, `.env`, ports et bases.
- Linux moins poli que macOS ; pas de version Windows officielle.
- Isolation Git parfois confondue avec une sandbox de sécurité.
- Risque d'augmenter le nombre de tâches plus vite que la capacité de revue humaine.

### Fiabilité des témoignages

Les discussions communautaires contiennent des réponses de fondateurs et d'éditeurs concurrents. Elles permettent d'identifier les irritants, mais pas de mesurer objectivement le temps gagné. Les affirmations de performance ou d'échelle doivent être vérifiées sur un dépôt réel.

### Verdict

Excellent choix pour deux à cinq flux parallèles avec revue fréquente. Il apporte moins lorsqu'un développeur travaille surtout dans un seul checkout ou possède déjà une configuration tmux/worktree maîtrisée.

## Sources

- [Dépôt officiel](https://github.com/superset-sh/superset)
- [Documentation](https://docs.superset.sh)
- [Tarifs](https://superset.sh/pricing)

### Sources des avis

- [Discussion : orchestrateurs utilisés au quotidien](https://www.reddit.com/r/ClaudeCode/comments/1viwdnh/what_orchestrator_are_you_using/)
- [Comparaison Conductor, Superset et cmux](https://www.reddit.com/r/ClaudeCode/comments/1rxwkoz/my_thoughts_on_conductor_vs_superset_vs_cmux_vs/)
- [Issues du dépôt](https://github.com/superset-sh/superset/issues)
- [Dépôt officiel](https://github.com/superset-sh/superset)

_Dernière analyse : 12 novembre 2026_
