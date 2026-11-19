---
title: "Paperclip"
type: outil
description: "Application auto-hébergeable pour coordonner des équipes d'agents IA, leurs tâches, leurs budgets et leurs validations."
format: application
tags:
  - metier/ingenierie
  - metier/operations
  - theme/multi-agent
  - theme/automatisation
editeur: "Paperclip Labs, Inc."
logo: "[[paperclip.svg]]"
site: "https://paperclip.ing/"
depot: "https://github.com/paperclipai/paperclip"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-19
etoiles: 114903
forks: 19079
etoiles_releve: 2026-11-19
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 5
memo: "[[Paperclip mémo]]"
avis_maj: 2026-11-19
modified: 2026-11-19
---

# Paperclip

> Paperclip donne aux équipes d'agents IA un espace commun pour relier leurs tâches à des objectifs, suivre leurs exécutions et contrôler les dépenses et les validations. Des adaptateurs raccordent les agents qui réalisent le travail.

Voir aussi le [[Paperclip mémo|mémo pratique]] et les [[#Avis indépendants|avis indépendants]].

## Résumé

Paperclip modélise chaque organisation comme une « entreprise » avec des objectifs, des projets, un organigramme et des tâches. On configure le rôle et l'environnement de chaque agent, puis on lui attribue une tâche. Le serveur transmet le contexte à l'adaptateur et conserve les traces d'exécution et d'activité.

L'édition auto-hébergeable est sous licence MIT. Elle comprend un serveur Node.js, une interface web et une API, avec PostgreSQL embarqué pour démarrer localement. La version stable relevée le 19 novembre 2026 est `v2026.1117.0`. Le site propose aussi une liste d'attente pour l'offre hébergée. Le coût des modèles, des abonnements et de l'infrastructure dépend du déploiement.

## Fonctionnalités

- **Organisation du travail**. Assigner des tâches rattachées à des projets et à des objectifs, définir des rôles et suivre les dépendances entre tâches.
- **Adaptateurs**. Raccorder notamment Claude Code, Codex, OpenCode ou Hermes. L'adaptateur passe le contexte au moteur et remonte les résultats disponibles.
- **Déclenchement des agents**. Un *heartbeat* correspond à une exécution déclenchée, par exemple, par une affectation, un commentaire, une routine ou un horaire. L'historique donne accès aux états et aux journaux.
- **Budgets et gouvernance**. Suivre les dépenses par agent ou par organisation, appliquer des limites et prévoir des validations pour certaines décisions. L'API distingue les usages dont le coût est inconnu.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★★|

> Notes alignées sur le [[Comparatif global des outils|barème global]]. Popularité calculée à partir des 114 903 étoiles du dépôt GitHub, qui comptait 19 079 forks le 19 novembre 2026.

### Points forts

- Une tâche relie l'objectif, le responsable, les blocages et les traces d'exécution. Cela facilite la reprise après un échec ou un transfert entre agents.
- L'équipe peut conserver ses moteurs d'agents existants et centraliser le suivi des tâches.
- L'installation locale permet de tester la gestion des tâches avec une base embarquée avant de décider d'un déploiement partagé.

### Limites

- Le suivi des coûts dépend des données remontées par les adaptateurs et du mode de facturation. Comparer les montants aux relevés du fournisseur avant de s'appuyer sur un plafond.
- Les routines dépendent de la disponibilité du serveur et des moteurs raccordés. Les essais tiers ont observé des différences de configuration, de contexte et de fiabilité selon l'adaptateur et la version.
- Un agent local utilise les droits et outils accessibles dans son environnement d'exécution. Limiter ces accès et consulter les avis de sécurité avant d'exposer une instance ou de la partager entre équipes.

### Qualité

La documentation couvre l'installation, les adaptateurs, la CLI et l'API. Certains guides de démarrage divergent sur les valeurs par défaut du mode réseau, ce qui justifie de vérifier le mode affiché. Les essais indépendants confirment l'installation, les fonctions de suivi et des exécutions réelles. Le projet public, créé en mars 2026, a moins d'un an de recul.

## Relations

- **Alternative à** [[Ruflo]] pour coordonner plusieurs agents. Paperclip convient au suivi d'un portefeuille de tâches, de responsables et de budgets. Ruflo s'adresse aux équipes qui veulent configurer des essaims et leur mémoire autour du moteur d'exécution.
- **Utilise** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]] ou [[Hermes Agent]] comme moteurs via des adaptateurs.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 19 novembre 2026._

### Ce qui est apprécié

- Ryan T. Walton a installé `v2026.722.0` et créé une tâche liée à un projet et à un objectif. Son essai confirme la présence des dépendances, de l'espace de travail et du journal d'activité dans le flux de gestion. Il s'est arrêté avant d'exécuter un agent réel.
- JACAR a fait tourner `v2026.1005.0` avec Docker et a observé des exécutions, des réponses et des événements d'usage avec un petit modèle local raccordé par l'adaptateur `process`.

### Ce qui est critiqué

- Dans l'essai de JACAR, l'assistant de démarrage n'a pas permis de raccorder directement le modèle local choisi. Sur huit exécutions via la configuration de contournement, quatre ont réussi et deux ont produit une réponse. Le modèle était de 0,8 milliard de paramètres, ce qui limite la portée des observations sur la qualité des réponses.
- Felipe Fontoura décrit des problèmes de transmission des instructions avec l'adaptateur Hermes dans sa propre équipe de 13 agents. Il a maintenu un adaptateur dérivé et une validation humaine avant publication. Son retour porte sur son environnement et il est l'auteur de l'alternative qu'il présente.

### Ce qui n'est pas établi

- Les retours consultés ne mesurent pas la fiabilité de la version actuelle sous charge ni la précision des budgets pour toutes les combinaisons d'adaptateurs et de fournisseurs.
- Le nombre de tâches terminées ne suffit pas à établir un gain de temps. Les essais cités ne quantifient pas le temps de supervision et de correction sur un processus comparable.

### Comparaison

[[Ruflo]] et Paperclip répondent tous deux à un besoin de coordination, à des niveaux différents. L'un structure l'exécution en essaim, l'autre rend le travail visible à l'échelle de l'organisation. Pour évaluer l'intérêt de Paperclip, comparer le même workflow avec un seul agent et avec une équipe supervisée, en incluant le temps de validation.

### Verdict

Paperclip mérite un essai quand plusieurs agents travaillent déjà sur des tâches qui se transmettent et qu'il devient difficile de retrouver les résultats, les coûts et les décisions. Un premier essai avec un agent, une tâche interne et une validation humaine permet d'évaluer l'outil avec peu de configuration.

## Sources

- [Site officiel de Paperclip](https://paperclip.ing/) et [kit de marque](https://paperclip.ing/brand/).
- [Dépôt GitHub](https://github.com/paperclipai/paperclip), [API GitHub](https://api.github.com/repos/paperclipai/paperclip) et [version stable v2026.1117.0](https://github.com/paperclipai/paperclip/releases/tag/v2026.1117.0).
- [Installation et CLI](https://docs.paperclip.ing/reference/cli/installation/), [premier agent](https://docs.paperclip.ing/guides/getting-started/your-first-agent/) et [comptabilisation des coûts](https://docs.paperclip.ing/reference/api/costs/).
- [Avis de sécurité publiés sur GitHub](https://github.com/paperclipai/paperclip/security/advisories).

### Sources des avis

- [Ryan T. Walton, essai de Paperclip](https://www.ryantwalton.dev/spotlights/paperclip/). Essai indépendant de la version de juillet 2026, limité à l'installation, l'API et la gestion de tâches.
- [JACAR, essai Docker avec un petit modèle local](https://jacar.es/en/paperclip-ai-agent-orchestration-docker/). Essai tiers réalisé le 7 octobre 2026 et publié le 4 novembre. Les résultats sont observés sur un adaptateur et un modèle.
- [Felipe Fontoura, retour sur 13 agents](https://felipefontoura.com/articles/paperclip-ai-agent-company/). Retour d'exploitation mis à jour le 6 octobre 2026. L'auteur maintient l'adaptateur tiers qu'il présente.

_Dernière analyse : 19 novembre 2026_
