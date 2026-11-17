---
title: "Ruflo"
type: outil
description: "Meta-harnais expérimental pour essaims, mémoire et coordination autour de Claude Code ou Codex."
format: cli
tags:
  - metier/ingenierie
  - theme/multi-agent
  - theme/memoire
  - theme/mcp
editeur: "ruvnet"
site: "https://cognitum.one/"
depot: "https://github.com/ruvnet/ruflo"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 81843
forks: 9648
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 2
note_maturite: 2
note_popularite: 4
memo: "[[Ruflo mémo]]"
avis_maj: 2026-09-25
modified: 2026-11-12
---

# Ruflo

> Ruflo est un **agent meta-harness** pour Claude Code et Codex qui ajoute orchestration multi-agent, swarms, mémoire persistante, apprentissage, workflows, fédération entre machines et intégration MCP. Il se positionne comme une couche d'exécution et de coordination autour des agents plutôt que comme un simple ensemble de skills.

**Composition** : 30+ skills, 98 agents et 314 outils MCP (annoncés par le projet).

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour la chronologie détaillée des audits et des réponses de l'équipe, et [[Ruflo mémo]] pour le mémo pratique. Les compteurs ci-dessus sont ceux du projet : un audit indépendant d'avril 2026 avait relevé qu'une grande partie des outils MCP ne faisaient qu'enregistrer un état.

## Résumé

Ruflo (anciennement Claude Flow) est un framework d'orchestration agentique conçu pour transformer Claude Code et Codex en systèmes multi-agents coordonnés. Il fournit une couche d'exécution comprenant agents spécialisés, swarms, mémoire vectorielle, workflows, hooks, MCP, daemon workers et fédération entre plusieurs machines.

Le projet propose deux modes d'installation très différents : des plugins Claude Code relativement légers, ou une installation CLI complète qui ajoute MCP, hooks, daemon, agents et une infrastructure de coordination plus intrusive.

Le projet a connu une évolution rapide en 2026. Les versions récentes ont corrigé plusieurs problèmes de fiabilité, de mémoire, de sécurité et de fédération, mais le dépôt reste très actif avec un volume important d'issues ouvertes. **Il doit être considéré comme expérimental** : les critiques publiques de printemps 2026 (audit indépendant d'avril, second audit de mai) étaient sévères, et les améliorations qui ont suivi reposent surtout sur les déclarations et audits de l'équipe elle-même ; à notre connaissance, aucun audit indépendant n'a été publié sur une version postérieure à mai 2026.

## Fonctionnalités

- **Multi-agent orchestration** : coordination d'agents spécialisés et exécution de tâches sous forme de swarms.
    
- **Hive-mind / swarm** : mécanismes de coordination, consensus et partage de tâches entre agents.
    
- **Adaptive memory** : mémoire persistante basée notamment sur AgentDB, vector search et mécanismes de récupération de patterns.
    
- **Self-learning** : apprentissage à partir des trajectoires et résultats des tâches afin d'améliorer les exécutions futures.
    
- **Workflow automation** : workflows multi-étapes, autopilot et workers exécutés en arrière-plan.
    
- **Federation** : coordination d'agents répartis sur plusieurs machines via une couche de communication sécurisée.
    
- **MCP integration** : exposition d'un grand nombre d'outils et intégration avec l'écosystème MCP.
    
- **Claude Code / Codex / Hermes** : Ruflo se positionne comme une couche d'orchestration indépendante du runtime d'agent sous-jacent.
    
- **Hooks** : intégration profonde avec Claude Code permettant notamment le routage automatique des tâches.
    
- **Plugins** : architecture modulaire avec des plugins séparés pour core, swarm, mémoire, federation, workflows, etc.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★☆☆☆|
|Richesse fonctionnelle|★★★★★|
|Architecture / extensibilité|★★★★☆|
|Réalité des fonctionnalités|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|★★★★☆|
|Stabilité|★★★☆☆|
|Simplicité|★★☆☆☆|
|Sécurité|★★★☆☆|
|Prévisibilité des coûts|★★☆☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 81 843 au 16 novembre 2026._

**Commentaire :** Ruflo est devenu un framework substantiel, et les critiques de « stubs » formulées en avril 2026 portaient sur des versions antérieures. Les releases récentes montrent un travail réel sur swarm, mémoire, fédération, sécurité et fiabilité, mais ce travail est attesté surtout par l'équipe elle-même : l'audit interne du 29 mai 2026 a lui-même constaté que les multiplicateurs de performance annoncés ne tenaient pas (HNSW mesuré à 1,48× au lieu de « 150× à 12 500× »), et des audits automatisés internes corrigeaient encore des benchmarks trompeurs en septembre. La note « Réalité des fonctionnalités » est donc de ★★★☆☆ tant qu'aucune vérification indépendante récente n'existe. Son périmètre extrêmement large introduit par ailleurs une surface technique importante : MCP, hooks, daemon, workers, mémoire, agents et fédération. Un test comparatif de mai 2026 rapportait environ 220 000 tokens et 35 minutes pour une fonctionnalité moyenne.

### Points forts

- **Vision très complète** de l'orchestration agentique : agents, mémoire, workflows, swarms, federation et learning sont réunis dans un même environnement.
    
- **Intégration profonde avec Claude Code** grâce aux hooks, plugins, MCP et agents spécialisés.
    
- **Architecture modulaire** : les plugins permettent désormais d'utiliser certaines fonctionnalités sans installer nécessairement l'ensemble du runtime Ruflo.
    
- **Mémoire agentique** avec AgentDB, recherche vectorielle et mécanismes de récupération de patterns ; des audits ont relevé avant correctifs une mémoire gonflée par des doublons et des embeddings factices, et des défauts d'embeddings restaient ouverts en septembre.
    
- **Fédération multi-machine** permettant de dépasser le modèle d'un agent exécuté uniquement sur une machine locale.
    
- **Cadence de publication très élevée** : plus de 7 500 commits et des releases quasi quotidiennes en septembre 2026 (sa popularité ne constitue pas une preuve de fiabilité).
    
- Les versions récentes ont notamment corrigé des problèmes concernant l'identité des événements de fédération, l'échappement des hooks Windows, l'intégrité de la mémoire et le consensus des swarms.
    

### Limites

- **Complexité élevée** : Ruflo cherche à couvrir orchestration, mémoire, agents, MCP, hooks, workers, learning et federation dans une seule plateforme.
    
- **Grande surface d'outils** : l'installation complète expose plus de 300 outils MCP, ce qui peut augmenter la complexité du contexte et de la sélection d'outils par le modèle.
    
- **Risque de sur-ingénierie** pour les projets qui ont seulement besoin de quelques agents spécialisés et de bonnes pratiques de développement.
    
- **Consommation de tokens et exécution autonome à surveiller** : des problèmes liés aux workers headless, aux daemons et à la consommation de ressources ont été documentés.
    
- **Historique de problèmes de sécurité et de consentement** : une vulnérabilité critique concernait une ancienne version du MCP bridge, et une issue de juin 2026 rapportait des sessions Claude Code autonomes déclenchées sans consentement avec une ancienne version. Ces problèmes sont à considérer comme des éléments historiques, pas comme une preuve d'une vulnérabilité identique dans la version actuelle.
    
- **Projet très mouvant** : plusieurs corrections importantes ont encore été publiées en septembre 2026, notamment autour de la mémoire, de la fédération et de la sécurité.
    
- **Les performances annoncées doivent être contextualisées** : les benchmarks mesurent principalement les performances de l'orchestration et ne démontrent pas nécessairement une amélioration équivalente de la qualité ou de la productivité du développement. Plusieurs chiffres du README ont dû être remplacés par des valeurs mesurées après l'audit interne de mai 2026.

- **Gain face à un agent unique non démontré** : un bon agent, un plan clair et quelques revues produisent souvent l'essentiel du résultat ; [[Claude Code]] fournit déjà sous-agents et équipes avec moins de couche intermédiaire.
    

## Relations

- **Alternative à :** [[CrewAI]], [[LangGraph]], [[AutoGen]], autres frameworks d'orchestration multi-agent
    
- **S'intègre avec :** Claude Code · Codex · Hermes · MCP
    
- **Utilise :** AgentDB · MCP · hooks Claude Code · vector/RAG memory
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 25 septembre 2026._

### Synthèse

Ruflo promet une orchestration ambitieuse : essaims, mémoire, routage et méthodes structurées donnent l’impression de pouvoir industrialiser une équipe d’agents. Les utilisateurs attirés par les systèmes multi-agents apprécient la richesse des primitives et le nombre d’exemples.

Les critiques publiques ont été inhabituellement sévères au printemps 2026. Un audit communautaire contestait de nombreuses affirmations et des utilisateurs décrivaient un écart entre démonstration et code réellement utilisé. Ces critiques portaient sur des versions d’avril–mai 2026 ; l’équipe y a répondu par des correctifs et par un audit interne publié (voir la chronologie ci-dessous). D’autres trouvent que la complexité de l’orchestration dépasse son bénéfice : un bon agent, un plan clair et quelques revues produisent souvent 80 % du résultat. La popularité GitHub ne constitue pas une preuve de fiabilité.

### Chronologie des critiques et des réponses

|Date|Version|Événement|
|---|---|---|
|4 avril 2026|v3.5.51|Audit indépendant (roman-rr) : environ 290 des 300+ outils MCP ne font qu’enregistrer un état, prédictions « neuronales » et précision générées au hasard (`Math.random()`), mémoire gonflée par des doublons. Relayé par une issue sur la liste awesome-claude-code.|
|3 mai 2026|v3.6.14 à 3.6.22|Le mainteneur reconnaît les constats et publie des correctifs pour 24 problèmes documentés, dont la prédiction factice et la déduplication de la mémoire. Une partie des lacunes d’architecture n’est corrigée que partiellement.|
|4 mai 2026|v3.6.12|Un second audit (issue #1700) signale 5 fonctions « réelles » cassées ou cosmétiques (workers, embeddings, SONA, hive-mind, routage) ; l’issue est close le lendemain.|
|11 mai 2026|non précisée|Test comparatif de Gerald Chen : ~220 000 tokens et ~35 minutes pour une fonctionnalité moyenne, non recommandé pour un développeur indépendant.|
|29 mai 2026|v3.10.6 → v3.10.7|Audit interne mesuré (6 auditeurs, vraies mesures) : la boucle d’auto-apprentissage fonctionne réellement, mais les multiplicateurs de performance annoncés ne tiennent pas (HNSW « 150× à 12 500× » mesuré à 1,48×, métrique Flash Attention générée au hasard). Correctifs dans la v3.10.7 : inversion des récompenses négatives, métrique aléatoire retirée, embeddings factices désormais signalés comme tels, HNSW réellement activé (1,9× à 4,7×), chiffres du README remplacés par des valeurs mesurées.|
|septembre 2026|v3.39 à v3.45|Releases quasi quotidiennes. Des audits automatisés internes corrigent encore des benchmarks trompeurs (ex. mesure de démarrage factice supprimée le 5 septembre), et plusieurs défauts restent ouverts (initialisation des embeddings signalée comme réussie malgré un téléchargement ignoré, stockage et recherche utilisant des modèles d’embedding différents).|

À notre connaissance, **aucun audit indépendant n’a été publié sur une version postérieure à mai 2026**. Les critiques d’avril ne décrivent donc plus fidèlement la version actuelle, mais les améliorations reposent surtout sur les déclarations et audits de l’équipe elle-même.

### Comparaison

Claude Code fournit déjà sous-agents et équipes avec moins de couche intermédiaire. LangGraph est plus bas niveau mais plus explicite pour des applications contrôlées. BMAD structure un processus sans prétendre être une infrastructure d’essaim complète. Ruflo vise plus large, donc exige plus d’audit.

### Verdict

À considérer comme expérimental, mais à juger sur sa version actuelle plutôt que sur les critiques d’avril 2026 : l’équipe a corrigé une bonne partie des défauts relevés et publie désormais des chiffres mesurés. Ne pas l’introduire dans un dépôt sensible sans audit du code, test comparatif contre un workflow simple et mesures de coût/qualité.

## Sources

- [GitHub — Ruflo](https://github.com/ruvnet/ruflo)
    
- [GitHub — Releases](https://github.com/ruvnet/ruflo/releases)
    
- [GitHub — Issues](https://github.com/ruvnet/ruflo/issues)
    
- [Ruflo Wiki](https://github.com/ruvnet/ruflo/wiki)
    
- [Reddit — retour critique sur Ruflo](https://www.reddit.com/r/ClaudeAI/comments/1sckiy8/do_not_install_ruflo_into_your_claude_code/)
    

- [Audit indépendant de la v3.5.51 — gist roman-rr (4 avril 2026)](https://gist.github.com/roman-rr/ed603b676af019b8740423d2bb8e4bf6)
    
- [Issue #1700 — second audit sur la v3.6.12](https://github.com/ruvnet/ruflo/issues/1700)
    
- [Audit interne mesuré de Ruflo (29 mai 2026)](https://github.com/ruvnet/ruflo/blob/main/docs/reviews/intelligence-system-audit-2026-05-29.md)
    
- [Comparatif des plugins d'orchestration — Gerald Chen (11 mai 2026)](https://chenguangliang.com/en/posts/claude-code-multi-agent-orchestration-plugins/)
    

### Sources des avis

- [Audit critique communautaire](https://www.reddit.com/r/ClaudeAI/comments/1sckiy8/do_not_install_ruflo_into_your_claude_code/)
- [Audit indépendant de la v3.5.51 et réponse du mainteneur — gist roman-rr](https://gist.github.com/roman-rr/ed603b676af019b8740423d2bb8e4bf6)
- [Issue #1700 — second audit sur la v3.6.12](https://github.com/ruvnet/ruflo/issues/1700)
- [Comparatif des plugins d’orchestration — Gerald Chen (11 mai 2026)](https://chenguangliang.com/en/posts/claude-code-multi-agent-orchestration-plugins/)
- [Audit interne mesuré de Ruflo (29 mai 2026)](https://github.com/ruvnet/ruflo/blob/main/docs/reviews/intelligence-system-audit-2026-05-29.md)
- [PR #2228 — correctifs et chiffres mesurés (v3.10.7)](https://github.com/ruvnet/ruflo/pull/2228)
- [Discussion Claude Flow/Ruflo et SPARC](https://www.reddit.com/r/ClaudeAI/comments/1s469qg/claude_flow_and_sparc_methodoloy/)
- [Retours sur l’orchestration multi-agent](https://www.reddit.com/r/ClaudeAI/comments/1ryrhiv/multi_agent_orchestration_what_is_your_workflow/)

_Dernière analyse : 12 novembre 2026_