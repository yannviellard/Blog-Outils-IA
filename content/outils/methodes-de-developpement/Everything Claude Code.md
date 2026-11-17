---
title: "Everything Claude Code (ECC)"
type: outil
description: "Configuration de référence très riche à élaguer et adapter au contexte de l'équipe."
format: collection
tags:
  - metier/ingenierie
  - theme/contexte
  - theme/planification
  - theme/tests
  - theme/revue-de-code
editeur: "Affaan Mustafa"
logo: "[[everything-claude-code.svg]]"
site: "https://ecc.tools"
depot: "https://github.com/affaan-m/ECC"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-06
etoiles: 304071
forks: 44807
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 5
memo: "[[Everything Claude Code mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Everything Claude Code (ECC)

> Système open source d'Affaan Mustafa qui donne à Claude Code (et, avec des adaptateurs, à Codex, Cursor, OpenCode, Gemini…) une méthode de travail complète : planifier, tester, implémenter, relire dans un contexte neuf, vérifier, mémoriser et améliorer. Il regroupe 68 agents, 292 skills, des hooks, des règles, une mémoire partagée entre agents et un scanner de sécurité (AgentShield).

**Composition** : 292 skills, 68 agents, configurations MCP fournies et serveur `ecc-memory-mcp` optionnel.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Everything Claude Code mémo]] pour le mémo pratique.

## Résumé

**Everything Claude Code**, désormais appelé **ECC**, est né de plus de dix mois d'usage quotidien de Claude Code par son auteur, qui se présente comme lauréat d'un hackathon Anthropic. Ce qui était au départ une collection de configurations est devenu, avec la version 2.0 de juin 2026, ce que le projet appelle un « système d'exploitation du harness d'agent » : un cycle de travail outillé **plan → test → implémentation → revue → vérification → mémoire → amélioration**, installé une fois plutôt que réexpliqué à chaque prompt.

Le principe affiché est « optimiser la fenêtre de contexte, persister tout le reste ». Les **skills** se chargent seulement quand la tâche en a besoin, les **agents** isolent planification, implémentation et revue dans des contextes séparés, les **règles** (toujours chargées) s'installent au cas par cas, les **hooks** appliquent des contrôles déterministes hors du contexte du modèle, et les **instincts** sont des patterns appris des sessions réelles, rappelés quand ils sont pertinents.

Le projet fonctionne surtout avec Claude Code, dispose d'une synchronisation Codex supportée et d'adaptateurs aux capacités limitées pour d'autres agents. La branche 2.2 (août–septembre 2026) apporte une installation guidée (`npx ecc-universal setup`), un « Memory Vault » commun à plusieurs agents et une revue des plans dans le navigateur. Le code reste sous licence MIT ; une offre payante, ECC Pro, propose une GitHub App pour les dépôts privés.

**À noter :** le dépôt de référence est [affaan-m/ECC](https://github.com/affaan-m/ECC) ; `WorldFlowAI/everything-claude-code` est une copie figée en janvier 2026.

## Fonctionnalités

- **Workflows de développement** : `/ecc:plan` (plan éditable avant tout code), skill `tdd-workflow` (cycle RED → GREEN → REFACTOR avec preuves), `/code-review` en contexte neuf, `/build-fix`, `/refactor-clean`, `/security-scan`, `/update-docs`, `/test-coverage`.
    
- **68 agents spécialisés** : planner, architect, tdd-guide, code-reviewer, security-reviewer, build-error-resolver, e2e-runner, doc-updater, relecteurs par langage (Go, Python, TypeScript, F#…), database-reviewer, mle-reviewer.
    
- **292 skills** chargées à la demande : TDD, recherche, sécurité, documentation, frontend, data, ML, opérations, `context-budget` (audit de la consommation de contexte).
    
- **Mémoire et continuité** : `/save-session`, `/resume-session`, `/learn-eval`, instincts appris avec score de confiance, et **Memory Vault** (`ecc memory`) au format Markdown commun à Claude, Codex, Hermes, OpenClaw, Kimi.
    
- **Hooks** : résumés de session, injection de contexte au démarrage (plafonnable), contrôles déterministes, suggestions de compaction.
    
- **Règles** optionnelles, par langage ou par projet.
    
- **AgentShield** : analyse de la configuration de l'agent lui-même (prompts, hooks, configuration MCP, permissions, secrets) comme surface d'attaque.
    
- **Installation guidée** multi-agents (Claude Code, Codex, Kimi Code) avec diagnostic, réparation et désinstallation propres.
    
- **Configurations MCP** prêtes (GitHub, Supabase, Vercel, Railway…), à activer au cas par cas.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Richesse fonctionnelle|★★★★★|
|Modularité|★★★★☆|
|Qualité des workflows|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★★|
|Maintenance|★★★★☆|
|Intégration Claude Code|★★★★★|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 304 071 au 16 novembre 2026._

**Commentaire :** ECC est l'un des projets les plus suivis de l'écosystème Claude Code, avec un rythme de publication hebdomadaire et plusieurs centaines de contributeurs. Sa force vient de la combinaison agents + skills + règles + hooks + vérification, et d'une vraie réflexion sur le coût en contexte (skills à la demande, plafonds d'injection, `/context-budget`). Il reste très opinionated (TDD, couverture de 80 %, délégation aux agents) et son volume impose de sélectionner les composants plutôt que de tout activer.

### Points forts

- **Cycle de travail complet et vérifiable** : chaque résultat laisse une trace (plan, test en échec, test qui passe, revue, vérification finale).
    
- **Revue en contexte neuf** : l'agent qui relit n'est pas celui qui a écrit le code.
    
- **Attention portée au contexte** : skills chargées à la demande, règles sélectives, plafonds configurables, audit avec `/context-budget`.
    
- **Mémoire portable entre agents** (Memory Vault) plutôt que des transcriptions propriétaires.
    
- **Sécurité de l'environnement d'agent** prise en compte avec AgentShield.
    
- **Projet très actif** : ~356 contributeurs, releases fréquentes et notes de version détaillées (la popularité mesure l'attention portée au dépôt ; une cadence de publication élevée n'est pas en soi un gage de qualité).
    

### Limites

- **Risque de surcharge** : 68 agents et 292 skills, c'est beaucoup. Un usage occasionnel est souvent mieux servi par un `CLAUDE.md` bien écrit.
    
- **Doublons à l'installation** : installer ECC deux fois dans le même agent (plugin + copie manuelle) duplique skills, commandes et hooks ; le README insiste sur « une seule méthode par agent ».
    
- **Forte opinion sur certaines pratiques** : TDD systématique, seuil de couverture de 80 %.
    
- **Parité inégale entre agents** : l'expérience est complète sur Claude Code, plus limitée ailleurs.
    
- **Surface en évolution rapide** : des commandes courtes historiques (`/tdd`, `/eval`) ont été retirées au profit des skills ; guides et tutoriels tiers peuvent être dépassés.
    
- **Modèle économique mixte** : le cœur est gratuit et MIT, mais certaines fonctions (GitHub App pour dépôts privés) sont payantes.

- **Les « méga-setups » vieillissent vite** : règles potentiellement contradictoires entre elles ou avec celles du dépôt, plus grand coût cognitif et de contexte ; très opinionated, l'ensemble convient moins à un dépôt existant ou à une équipe qui a ses propres conventions.

- **Composants tiers à auditer** : agents, skills et hooks disposent potentiellement du shell et des fichiers ; les lire et épingler les versions avant installation (AgentShield analyse la configuration mais ne remplace pas cette relecture).
    

## Relations

- **Alternative à :** [[Superpowers]], [[GStack]], [[Oh My Claude]], [[BMAD Method]]
    
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], Cursor, Kimi Code, Hermes, OpenClaw
    
- **Utilise :** agents, skills, slash commands, hooks et MCP de Claude Code ; [[Playwright]] pour les tests de bout en bout
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le projet est séduisant comme configuration de référence : il rassemble commandes, agents, skills et réglages qu’un utilisateur devrait autrement découvrir séparément. Les collections de ce type font gagner du temps et donnent des exemples concrets d’organisation d’un environnement Claude Code.

Les retours sur les « méga-setups » sont mitigés. Ils vieillissent vite, peuvent contenir des règles contradictoires et augmentent le coût cognitif comme le contexte chargé. Un environnement très opinionated peut être spectaculaire en démo mais moins adapté à un dépôt existant ou à une équipe avec ses propres conventions. Les composants tiers doivent être lus et épinglés, car ils disposent potentiellement du shell et des fichiers.

### Comparaison

Superpowers fournit un processus de développement plus resserré ; BMAD structure le cycle produit ; `wshobson/agents` et Alirezarezvani servent davantage de catalogues. Everything Claude Code convient à qui cherche un « dotfiles pour agent » complet, mais il est moins minimal qu’une configuration maison.

### Verdict

Très bonne source d’inspiration et point de départ accéléré ; à élaguer et adapter plutôt qu’à adopter aveuglément.

## Sources

- [GitHub — affaan-m/ECC](https://github.com/affaan-m/ECC)
    
- [Site ecc.tools](https://ecc.tools)
    
- [Longform Guide](https://github.com/affaan-m/ECC/blob/main/the-longform-guide.md)
    
- [CHANGELOG](https://github.com/affaan-m/ECC/blob/main/CHANGELOG.md)
    
- [Everything Claude Code (ECC) — tutoriel DataCamp](https://www.datacamp.com/tutorial/everything-claude-code)
    

### Sources des avis

- [Dépôt officiel](https://github.com/affaan-m/ECC)
- [Manuel complet sur l’architecture et les risques de dépendances](https://arxiv.org/abs/2608.26742)
- [Analyse de la qualité de l’écosystème de skills](https://www.agentskillreport.com/quality-in-the-agent-skills-ecosystem.pdf)

_Dernière analyse : 12 novembre 2026_
