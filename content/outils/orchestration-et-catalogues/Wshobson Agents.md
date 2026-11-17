---
title: "wshobson/agents"
type: outil
description: "Marketplace modulaire et multi-harnais d'agents, skills, commandes et orchestrateurs."
format: collection
tags:
  - metier/ingenierie
  - metier/operations
  - theme/multi-agent
editeur: "wshobson"
site: "https://github.com/wshobson/agents"
depot: "https://github.com/wshobson/agents"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-08
etoiles: 42566
forks: 4500
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[Wshobson Agents mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# wshobson/agents

> Marketplace open source de composants agentiques prêts à l'emploi : 94 plugins, 202 agents spécialisés, 183 skills, 105 commands et 16 orchestrateurs multi-agents, utilisables depuis Claude Code et plusieurs autres environnements agentiques.

**Composition** : 94 plugins, 202 agents, 183 skills, 105 commandes et 16 orchestrateurs.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Wshobson Agents mémo]] pour le mémo pratique.

## Résumé

**wshobson/agents** est un vaste marketplace de composants pour le développement assisté par agents. Le projet organise des agents spécialisés, skills, commandes et workflows multi-agents sous forme de plugins indépendants et composables.

Son architecture repose sur un principe de **source unique** dans `plugins/`, à partir de laquelle sont générés des artefacts adaptés à différents _agentic harnesses_. Le projet cible notamment Claude Code, OpenAI Codex CLI, Cursor, OpenCode, GitHub Copilot, Antigravity CLI et Pi.

L'installation est granulaire : installer un plugin ne charge que ses propres agents, skills et commandes dans le contexte, plutôt que l'ensemble du marketplace.

## Fonctionnalités

- **94 plugins spécialisés** couvrant notamment le développement, les langages, l'infrastructure, la sécurité, l'IA/ML, la data, la documentation, le business et le SEO.
    
- **202 agents spécialisés** pour l'architecture, les langages, le backend, la sécurité, les données, le ML, la documentation et d'autres domaines.
    
- **183 skills à divulgation progressive**, permettant de ne charger les connaissances détaillées qu'au moment où elles sont nécessaires.
    
- **105 commands** pour automatiser des opérations comme le scaffolding, les tests, les audits de sécurité et l'infrastructure.
    
- **16 orchestrateurs multi-agents** couvrant notamment le développement full-stack, la sécurité, le ML et l'incident response.
    
- **Support multi-harness** avec génération d'artefacts natifs pour plusieurs environnements à partir d'une même source.
    
- **PluginEval**, framework d'évaluation en trois niveaux : analyse statique, jugement LLM et simulations Monte Carlo.
    
- **Outils de validation et de génération** permettant de détecter les dérives entre la source et les artefacts générés.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Architecture|★★★★★|
|Modularité|★★★★★|
|Qualité des composants|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|
|Portabilité|★★★★☆|
|Évaluation / QA|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 42 566 au 16 novembre 2026._

**Commentaire :** projet très structuré pour sa taille, avec une documentation organisée par plugins, agents, skills, architecture et harnesses. La séparation entre source `plugins/` et artefacts spécifiques aux environnements est particulièrement robuste. La présence de `plugin-eval`, de tests de génération et de contrôles de dérive apporte une vraie démarche de qualité.

La principale limite vient de la **taille du catalogue** : avec 94 plugins et plusieurs centaines de composants, il existe un risque de recouvrement ou de duplication entre agents. Le dépôt possède d'ailleurs une issue ouverte concernant des agents portant le même nom mais présentant un contenu divergent.

### Points forts

- **Très forte modularité** : les plugins sont isolés, composables et installables individuellement.
    
- **Architecture multi-harness ambitieuse** : une même base Markdown peut alimenter plusieurs environnements agentiques avec des adaptations natives plutôt qu'une simple conversion générique.
    
- **Large couverture fonctionnelle** : développement, backend, frontend/mobile, sécurité, data, ML, infrastructure, documentation, business et SEO.
    
- **Progressive disclosure** des skills, limitant le chargement inutile du contexte.
    
- **Framework d'évaluation intégré** (PluginEval) avec analyse statique, LLM Judge et Monte Carlo ; il s'agit d'une auto-évaluation du projet, sans validation indépendante de la qualité des composants.
    
- **Bonne discipline d'ingénierie** : génération des artefacts, validation, tests de compatibilité et contrôles de dérive sont intégrés au repository.
    
- **Licence MIT**, permettant une utilisation et une adaptation permissives.
    

### Limites

- **Catalogue très volumineux** : le nombre élevé de plugins et d'agents peut rendre la sélection et le routing plus complexes.
    
- **Risque de redondance** : certaines fonctionnalités peuvent se chevaucher entre agents ou plugins ; une issue ouverte documente notamment des collisions de noms entre agents.
    
- **Portabilité non parfaite** : les différents harnesses n'offrent pas exactement les mêmes capacités, ce qui nécessite des adaptations spécifiques par environnement.
    
- **Dépendance à l'écosystème des agentic harnesses** : la valeur du marketplace dépend en partie de la capacité de l'environnement utilisé à exploiter agents, skills, commands et orchestration.
    
- **Qualité hétérogène possible** dans un catalogue aussi large, malgré les mécanismes de validation et d'évaluation.

- **Chaque plugin est une dépendance** : agents, skills, commandes et scripts peuvent contenir des instructions et des outils puissants ; les études sur les marketplaces de plugins pointent un défi de maintenance et de co-évolution. Installer peu, épingler les versions et auditer le code ; le nombre de composants ou d'étoiles ne prouve ni la qualité ni l'utilité dans un dépôt donné.
    

## Relations

- **Alternative à :** [[Agency Agents]]
    
- **S'intègre avec :** [[Claude Code]]
    
- **S'intègre avec :** [[OpenAI Codex]]
    
- **S'intègre avec :** [[Cursor]]
    
- **S'intègre avec :** [[OpenCode]]
    
- **S'intègre avec :** [[GitHub Copilot]]
    
- **Utilise :** Agent Skills / `SKILL.md`
    
- **Utilise :** architecture de plugins
    
- **Utilise :** multi-agent orchestration
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le marketplace est apprécié pour sa largeur, son installation granulaire et son ambition multi-environnements. Il donne aux utilisateurs des briques réutilisables — agents, skills, commandes et orchestrateurs — sans les obliger à installer toute la collection.

Le volume rend la sélection et la gouvernance difficiles. Une étude récente des marketplaces Claude Code montre une croissance rapide, mais aussi un défi de co-évolution et de maintenance. Chaque plugin est une dépendance qui peut contenir instructions, scripts et outils puissants. Le nombre de composants ou d’étoiles ne prouve ni la qualité ni l’utilité dans un dépôt donné.

### Comparaison

Agency Agents est plus proche d’un catalogue de rôles Markdown. Alirezarezvani fournit beaucoup de skills et références unitaires. Everything Claude Code offre une configuration plus intégrée. `wshobson/agents` se distingue par son packaging en plugins granulaires et ses orchestrateurs.

### Verdict

Un des catalogues les plus riches pour utilisateurs avancés ; installer peu, épingler les versions, auditer le code et mesurer chaque ajout.

## Sources

- [GitHub — wshobson/agents](https://github.com/wshobson/agents)
    
- [README](https://github.com/wshobson/agents/blob/main/README.md)
    
- [Architecture / AGENTS.md](https://github.com/wshobson/agents/blob/main/AGENTS.md)
    
- [Contributing](https://github.com/wshobson/agents/blob/main/CONTRIBUTING.md)
    

### Sources des avis

- [Dépôt officiel](https://github.com/wshobson/agents)
- [Étude empirique des marketplaces de plugins](https://arxiv.org/abs/2608.28497)
- [Analyse de qualité de 673 skills](https://www.agentskillreport.com/quality-in-the-agent-skills-ecosystem.pdf)

_Dernière analyse : 12 novembre 2026_