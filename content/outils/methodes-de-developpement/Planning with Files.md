---
title: "Planning with Files"
type: outil
description: "Mémoire de travail explicite dans trois fichiers Markdown pour les tâches longues."
format: skill
tags:
  - metier/ingenierie
  - theme/planification
  - theme/contexte
  - theme/memoire
editeur: "OthmanAdi"
site: "https://skills.sh/othmanadi/planning-with-files/planning-with-files"
depot: "https://github.com/OthmanAdi/planning-with-files"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-10
etoiles: 28008
forks: 2309
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[Planning with Files mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Planning with Files

> Skill de planification persistante pour les agents de développement IA. Il utilise trois fichiers Markdown — `task_plan.md`, `findings.md` et `progress.md` — comme mémoire de travail sur disque afin de maintenir le contexte, suivre l'avancement et reprendre une tâche après `/clear`, une compaction ou une interruption.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Planning with Files mémo]] pour le mémo pratique.

## Résumé

**Planning with Files** est un skill inspiré des techniques de _context engineering_ popularisées par Manus. Son principe central est de sortir les informations importantes de la fenêtre de contexte volatile de l'agent pour les conserver dans des fichiers Markdown persistants.

Le workflow repose principalement sur trois fichiers :

- `task_plan.md` — phases, objectifs, décisions et état d'avancement ;
    
- `findings.md` — recherches, découvertes et décisions techniques ;
    
- `progress.md` — journal des actions, tests et erreurs.
    

Des hooks relisent automatiquement le plan et réinjectent son contenu dans le contexte de l'agent. Le système dispose également d'un mécanisme de récupération après `/clear`, crash ou compaction, ainsi que d'un _completion gate_ permettant de contrôler qu'une tâche est réellement terminée avant que l'agent s'arrête.

Le projet prend aujourd'hui en charge de nombreux environnements, notamment **Claude Code, Codex, Cursor, OpenCode, Pi, Hermes Agent et DeepSeek Harness**, avec des variantes pour plus de 60 agents compatibles avec le standard Agent Skills.

## Fonctionnalités

- **Plan persistant** avec `task_plan.md`, `findings.md` et `progress.md`
    
- **Réinjection automatique du contexte** via des hooks à chaque tour
    
- **Récupération de session** après `/clear`, compaction ou interruption
    
- **Suivi des phases et des erreurs** pour éviter de répéter les mêmes échecs
    
- **Completion gate** empêchant l'agent de s'arrêter prématurément en mode _gated_
    
- **Plans isolés** pour plusieurs tâches parallèles dans `.planning/`
    
- **Commandes dédiées** : `/plan`, `/status`, `/plan-doctor`, `/plan-attest`, `/plan-goal`, `/plan-loop`
    
- **Compatibilité multi-agents / multi-IDE**
    
- **Mécanisme d'attestation SHA-256** permettant de verrouiller le contenu du plan
    
- **Modes autonomes** pour les tâches longues ou non supervisées
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Simplicité du concept|★★★★★|
|Intégration agents|★★★★★|
|Gestion du contexte long|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|
|Robustesse|★★★★☆|
|Légèreté|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 28 008 au 11 novembre 2026._

**Commentaire :** projet actif et largement adopté. Le concept reste extrêmement simple — utiliser des fichiers Markdown comme mémoire de travail — mais l'implémentation est devenue relativement sophistiquée avec hooks, récupération de session, plans parallèles, completion gates, contrôles d'intégrité et intégrations multi-agents. Le dépôt compte 56 contributeurs au 22 septembre 2026.

### Points forts

- **Concept simple et transparent** : l'état de l'agent est lisible directement dans des fichiers Markdown.
    
- **Résout un problème concret des agents longs** : perte du contexte, dérive par rapport à l'objectif et répétition d'erreurs.
    
- **Résistant aux changements de contexte** : le plan survit à `/clear`, à la compaction et aux interruptions de session.
    
- **Hooks mécaniques** : les règles de planification ne dépendent pas uniquement de la volonté du LLM de les respecter.
    
- **Très large compatibilité** avec les principaux agents de développement.
    
- **Adapté aux tâches longues et complexes**, plutôt qu'aux petites modifications.
    
- **Open source MIT** et facilement inspectable.
    
- **Écosystème actif** : nombreuses extensions et projets dérivés utilisant le même pattern (signe de popularité du pattern, non de son efficacité mesurée).
    

### Limites

- **Surcharge opérationnelle** : la mise à jour permanente des trois fichiers peut ajouter du travail et de la consommation de contexte.
    
- **Risque de bureaucratie** pour les tâches simples ou de courte durée.
    
- **Risque de double source de vérité** lorsqu'il est combiné avec d'autres frameworks possédant leur propre système de planification.
    
- Les fichiers sont conçus comme **mémoire de travail temporaire**, pas comme documentation durable : ils sont gitignored par défaut et ne sont pas archivés automatiquement.
    
- La présence d'un plan correctement rempli **ne garantit pas la qualité du résultat** : le système contrôle surtout le suivi du workflow, pas la pertinence des décisions techniques.
    
- Les hooks augmentent la surface de complexité du système et doivent être compris avant une utilisation dans des workflows fortement automatisés.
    
- **Une vulnérabilité de sécurité a dû être corrigée** : la release v2.36.1 décrit un durcissement (suppression de la recherche dans le cache du hook Stop, politique d'exécution PowerShell ramenée de `Bypass` à `RemoteSigned`, ajout de délimiteurs contre l'injection de prompt), sans CVE ni avis de sécurité associé. Des hooks qui relisent et réinjectent des fichiers dans le contexte constituent une surface d'injection : à relire avant usage.

- **Des fichiers non mis à jour deviennent une seconde réalité obsolète** et peuvent tromper l'agent : sans règle d'actualisation et nettoyage en fin de tâche, le plan écrit peut contredire l'état réel du code.

- **Plus de contexte n'est pas plus de compétence** : une étude contrôlée citée dans l'avis montre que des fichiers de contexte ne corrigent pas les échecs de conception ou d'implémentation.

- **Le plan mode natif est plus léger** (mais moins persistant) et un issue tracker reste préférable pour la coordination d'équipe à long terme.

### Qualité

**Commentaire :** idée simple et robuste, bien documentée, utile pour les tâches longues, les recherches et les migrations ; inutile pour les petites corrections. Le projet est largement adopté (voir la note Popularité), ce qui mesure l'attention plus que l'efficacité : la note de gestion du contexte long est limitée à ★★★★☆ car aucune mesure indépendante ne chiffre le gain, et que l'étude contrôlée disponible nuance l'intérêt des fichiers de contexte. Voir [[#Avis indépendants|les avis indépendants]].

## Relations

- **Alternative à :** plan mode natif de [[Claude Code]], méthodes de planification comme [[Superpowers]] ou GSD

- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], Cursor, [[OpenCode]], [[Hermes Agent]]

- **Utilise :** hooks d'agent, fichiers Markdown (`task_plan.md`, `findings.md`, `progress.md`)

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

La skill est appréciée pour une idée simple et robuste : sortir le plan, les découvertes et le progrès de la fenêtre de contexte. Les fichiers persistent après une compaction, un crash ou un changement d’agent, restent lisibles par l’humain et facilitent la reprise d’un travail long.

La principale limite est la discipline. Des fichiers non mis à jour deviennent une seconde réalité obsolète et peuvent tromper l’agent. Pour une petite tâche, trois journaux ajoutent inutilement de la cérémonie. La recherche sur les fichiers de contexte montre par ailleurs qu’ils ne corrigent pas les échecs de conception ou d’implémentation : plus de contexte n’est pas forcément plus de compétence.

### Comparaison

Le plan mode natif est plus léger mais moins persistant. GSD et Superpowers organisent une méthode complète ; Planning with Files fournit seulement une mémoire de travail portable et composable. Un issue tracker est préférable pour la coordination d’équipe à long terme.

### Verdict

Très efficace pour les tâches longues, recherches et migrations ; inutile pour les petites corrections. Ajouter des règles d’actualisation et supprimer les fichiers temporaires une fois le travail terminé.

## Sources

- [GitHub — OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)

- [skills.sh — planning-with-files](https://skills.sh/othmanadi/planning-with-files/planning-with-files)

- [Releases (v2.36.1 : durcissement de sécurité)](https://github.com/OthmanAdi/planning-with-files/releases)

### Sources des avis

- [Présentation de la skill](https://claudesuperpower.com/skills/planning-with-files)
- [Évaluation et comparaison au plan mode](https://skillsupermarket.com/skill/othmanadiplanning-with-files)
- [Étude contrôlée sur les fichiers de contexte](https://arxiv.org/abs/2607.27250)

_Dernière analyse : 12 novembre 2026_
