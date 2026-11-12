---
title: "OpenCode"
type: outil
description: "Harnais open source et multi-modèles pour les équipes qui privilégient le contrôle et l'absence de verrouillage."
format: agent
tags:
  - metier/ingenierie
  - theme/contexte
  - theme/mcp
editeur: "Anomaly"
site: "https://opencode.ai/"
depot: "https://github.com/anomalyco/opencode"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 226085
forks: 30555
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 3
note_maturite: 4
note_popularite: 5
memo: "[[OpenCode mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# OpenCode

> Agent de développement logiciel open source et agnostique vis-à-vis des modèles, conçu pour travailler directement dans un codebase depuis le terminal, le desktop ou le web.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et opinions publiés, et [[OpenCode mémo]] pour le mémo pratique.

Mémo : [[OpenCode mémo]] pour les commandes à retenir.

## Résumé

OpenCode est un **agent de coding open source** conçu comme une alternative agnostique à Claude Code. Sa caractéristique centrale est de ne pas être lié à un fournisseur de modèles : il peut utiliser Claude, OpenAI, Google, de nombreux autres fournisseurs ou des modèles locaux. OpenCode s'appuie notamment sur AI SDK et Models.dev pour prendre en charge plus de 75 fournisseurs LLM.

Le projet met également l'accent sur une interface terminal (TUI), le support natif du LSP et une architecture client/serveur permettant notamment de piloter un processus OpenCode à distance.

Le projet connaît une croissance rapide : le dépôt officiel comptait plus de **1 500 contributeurs** au 22 septembre 2026. Ces chiffres mesurent l'attention portée au projet ; les retours d'usage indépendants sont nettement moins nombreux (voir l'avis).

## Fonctionnalités

- **Multi-provider / multi-modèles** : Claude, OpenAI, Gemini, modèles open source et modèles locaux.

- **Agentic coding** : exploration du codebase, modification de fichiers, commandes shell et workflows autonomes.

- **TUI avancée** : interface terminal pensée autour des workflows de développeurs et utilisateurs de Neovim.

- **LSP natif** pour améliorer la compréhension et la navigation dans le code.

- **Agent Skills** : comportements réutilisables définis via `SKILL.md`, avec compatibilité notamment avec les emplacements de Skills Claude et Agents.

- **Agents spécialisés et sous-agents** pour les recherches complexes et tâches multi-étapes.

- **MCP** pour connecter des outils et services externes.

- **Plugins et configuration extensible**.

- **Architecture client/serveur** permettant de séparer l'agent de son interface.

- **Desktop, Web, CLI/TUI et Docker**, avec notamment `opencode pair` pour accéder à une session via une interface web.

- **OpenCode Go** : abonnement à 10 $/mois donnant accès à un ensemble de modèles open source.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★★★☆|
|Popularité|★★★★★|
|Multi-modèles|★★★★★|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 226 085 au 11 novembre 2026._

### Points forts

- **Agnostique vis-à-vis des modèles** : permet de choisir le meilleur modèle selon la tâche, le coût ou les contraintes de confidentialité. Plus de 75 fournisseurs sont supportés.

- **Open source et MIT**, contrairement à Claude Code.

- **Très forte extensibilité** : Skills, Agents, Plugins, MCP et configuration personnalisable.

- **Interopérabilité intéressante avec l'écosystème Claude** : OpenCode peut découvrir des Skills placées dans `.claude/skills` et certains autres emplacements compatibles.

- **Support des modèles locaux**, permettant de réduire la dépendance aux fournisseurs cloud.

- **Architecture client/serveur** intéressante pour des usages distants et des interfaces alternatives au terminal.

- **Communauté de contributeurs très large** (plus de 1 500), signe d'une dynamique ouverte, sans valeur de preuve sur la qualité des résultats.

### Limites

- **Qualité dépendante du modèle choisi** : contrairement à un environnement intégré à un fournisseur unique, la performance globale varie selon le provider et le modèle sélectionné. Certains utilisateurs jugent [[Claude Code]] plus cohérent, mieux intégré et plus simple à faire fonctionner sur des travaux sérieux.

- **Davantage de choix implique davantage de configuration** : provider, modèle, contexte, permissions et stratégies d'utilisation doivent parfois être définis par l'utilisateur. C'est un outil « excellent pour les power users », moins « prêt à réussir » qu'un outil propriétaire pour qui veut un comportement optimisé sans réglages.

- **L'économie espérée n'est pas garantie** : le coût API d'un modèle premium peut annuler l'avantage tarifaire face à un abonnement propriétaire.

- **Ouvert ne signifie pas accès garanti aux abonnements grand public** : les changements de politique d'authentification de certains fournisseurs ont montré qu'un harnais ouvert ne permet pas toujours d'utiliser leurs forfaits.

- **Projet très actif et en évolution rapide**, ce qui peut entraîner des changements fréquents de comportement, de configuration ou d'API.

- **Écosystème moins intégré que celui d'un fournisseur propriétaire** pour certaines fonctionnalités avancées liées directement au modèle.

- **Les modèles et APIs restent généralement payants séparément**, sauf lorsqu'un service comme OpenCode Go ou un provider particulier fournit une formule dédiée.

- **L'abstraction multi-provider peut devenir une complexité supplémentaire** lorsqu'on cherche à reproduire exactement le même comportement d'un agent d'un environnement à l'autre.

- **Peu de sources indépendantes** : les sources ci-dessous sont toutes officielles ; les retours d'usage proviennent surtout de discussions communautaires (voir l'avis).

### Qualité

**Commentaire :** OpenCode se distingue moins par un modèle propriétaire que par son **harnais multi-modèles**. Son architecture ouverte permet de changer de fournisseur, d'utiliser des modèles locaux et de construire ses propres Skills, Agents, Plugins et intégrations MCP. La grille de notation reprend celle des autres agents (documentation, précision, maturité) et n'ajoute que le multi-modèles, seul point appuyé par des faits vérifiables (plus de 75 fournisseurs) ; l'expérience terminal, la richesse fonctionnelle ou l'interopérabilité ne sont pas notées faute de retours indépendants. La croissance rapide du dépôt indique une forte attention, mais aussi un projet qui évolue vite.

## Relations

- **Alternative à :** [[Claude Code]], [[OpenAI Codex]], [[Cursor]]

- **S'intègre avec :** [[Model Context Protocol|MCP]], [[GitHub]], [[LSP]], [[Neovim]], [[VS Code]]

- **Utilise :** [[Claude]], [[GPT]], [[Gemini]], [[Models.dev]], [[AI SDK]], [[Skill|Agent Skills]]

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Les utilisateurs apprécient surtout la liberté de choisir le fournisseur et le modèle, l’interface terminal, l’ouverture du projet et la possibilité d’utiliser des modèles locaux ou moins chers. Pour les experts qui veulent composer leur propre stack, OpenCode peut reproduire l’essentiel d’un agent propriétaire sans verrouillage fort.

Les avis ne sont pas unanimes. Certains trouvent Claude Code plus cohérent, mieux intégré et plus simple à faire fonctionner sur des travaux sérieux. OpenCode demande davantage de configuration, et le coût API d’un modèle premium peut annuler l’économie espérée. Les changements de politique d’authentification des fournisseurs montrent aussi qu’un harnais ouvert ne garantit pas l’accès aux abonnements grand public.

### Comparaison

Claude Code offre le flux le plus intégré autour de Claude ; Codex combine modèles OpenAI et délégation locale/cloud ; Cursor privilégie l’IDE. OpenCode gagne sur le multi-modèle, l’auto-hébergement partiel et la personnalisation, mais transfère à l’utilisateur le choix des modèles et la maintenance.

### Verdict

Excellent pour les power users et les équipes qui refusent le lock-in ; moins « prêt à réussir » qu’un outil propriétaire pour les utilisateurs qui veulent un comportement optimisé sans réglages.

## Sources

- [GitHub — anomalyco/opencode](https://github.com/anomalyco/opencode)

- [OpenCode](https://opencode.ai/)

- [OpenCode Documentation](https://opencode.ai/docs/)

- [OpenCode — Providers](https://opencode.ai/docs/providers)

- [OpenCode — Agent Skills](https://opencode.ai/docs/skills)

### Sources des avis

- [Discussion sur les raisons de choisir OpenCode](https://www.reddit.com/r/opencode/comments/1wj13ox/what_is_the_reason_you_use_opencode_instead_of/)
- [Retours OpenCode vs Claude Code](https://www.reddit.com/r/opencodeCLI/comments/1rpomf5/opencode_vs_claude_code/)
- [Comparaison Claude Code et OpenCode](https://docs.bswen.com/blog/2026-03-23-claude-code-vs-opencode-comparison/)

_Dernière analyse : 12 novembre 2026_
