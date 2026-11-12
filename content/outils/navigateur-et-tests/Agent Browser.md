---
title: "Agent Browser"
type: outil
description: "Navigation Chrome conçue pour les agents, compacte et orientée accessibilité."
format: cli
tags:
  - metier/ingenierie
  - theme/navigateur
  - theme/tests
editeur: "Vercel Labs"
site: "https://vercel.com/"
depot: "https://github.com/vercel-labs/agent-browser"
licence: "Apache-2.0"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 49700
forks: 3476
etoiles_releve: 2026-11-11
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[Agent Browser mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Agent Browser

> CLI native en Rust pour piloter un navigateur Chrome/Chromium depuis des agents IA : navigation, snapshot d'accessibilité, interactions (clic, saisie, drag), captures d'écran, réseau, authentification persistante et serveur MCP intégré, sans dépendance à Node.js ni à Playwright pour le daemon.

**Composition** : 1 skill (`agent-browser`), 1 serveur MCP (profils configurables).

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Agent Browser mémo]] pour le mémo pratique.

## Résumé

Agent Browser est un CLI d'automatisation de navigateur développé par Vercel Labs, pensé dès l'origine pour être piloté par des agents IA plutôt que par des humains ou des scripts de test classiques. Contrairement à des outils comme Playwright ou Puppeteer, son daemon est un binaire Rust natif qui télécharge et pilote Chrome via Chrome for Testing (le canal d'automatisation officiel de Google), sans nécessiter Node.js ni Playwright pour fonctionner au quotidien.

L'outil expose une commande `snapshot` qui retourne un arbre d'accessibilité avec des références stables (`@e1`, `@e2`…), pensé spécifiquement pour que les agents interagissent avec la page sans dépendre de sélecteurs CSS fragiles — tout en conservant le support des sélecteurs traditionnels et des locators sémantiques (rôle ARIA, texte, label). Il couvre l'ensemble du spectre classique de l'automatisation navigateur (clics, formulaires, drag & drop, upload, réseau, cookies, onglets, cadres, dialogues) et y ajoute des fonctionnalités orientées agents : mode batch pour exécuter plusieurs commandes en un seul appel process, diff de snapshots/screenshots, introspection React et Web Vitals, audits d'accessibilité via axe-core embarqué, support expérimental de WebMCP pour découvrir des outils exposés par une page, et un serveur MCP natif avec plusieurs profils d'outils (`core`, `network`, `state`, `debug`, `tabs`, `react`, `mobile`, `all`).

La gestion de l'authentification est particulièrement développée : réutilisation de profils Chrome existants, profils persistants, sauvegarde/restauration automatique de session, import d'état depuis un Chrome déjà connecté via CDP, et un coffre-fort d'identifiants chiffré (« auth vault ») qui, selon la documentation du projet, permet à l'agent de se connecter par nom sans voir les mots de passe en clair. Des mécanismes de sécurité complémentaires (allowlist de domaines, marqueurs de délimitation de contenu non fiable, politique d'action, confirmation d'actions sensibles, limite de taille de sortie) visent explicitement les risques propres aux agents pilotés par LLM, notamment l'injection de prompt via le contenu d'une page.

## Fonctionnalités

- **CLI native Rust** : daemon rapide sans dépendance Node.js/Playwright à l'exécution ; installation via npm, Homebrew, Cargo ou build depuis les sources.

- **Snapshot d'accessibilité avec refs stables** : `agent-browser snapshot` puis interaction via `@e2`, `@e3`… conçu pour fiabiliser le pilotage par un agent plutôt que par des sélecteurs CSS.

- **Commandes classiques d'automatisation** : navigation, clic, saisie, drag & drop, upload, scroll, souris/clavier bas niveau (avec mouvements humains optionnels), gestion des onglets/fenêtres/frames/dialogues.

- **Batch execution** : exécution de plusieurs commandes en un seul appel CLI (arguments ou JSON via stdin), pour réduire l'overhead de démarrage de process sur des workflows multi-étapes.

- **Réseau et debug** : interception/mock de requêtes, enregistrement HAR, trace, profiling Chrome DevTools, enregistrement vidéo, console/erreurs, diff de snapshots et de captures d'écran.

- **Authentification persistante** : profils Chrome réutilisables, profils persistants, sauvegarde/restauration de session, import depuis un Chrome connecté, et coffre-fort d'identifiants chiffré (« auth vault ») pour se connecter par nom sans exposer de mot de passe au LLM.

- **Sécurité orientée agents** : allowlist de domaines (avec confinement WebRTC), marqueurs de délimitation du contenu de page non fiable, politique d'action statique, confirmation obligatoire pour les actions sensibles (`eval`, `download`…), limite de taille de sortie.

- **React & Web Vitals** : arbre de composants React, inspection de fibers, enregistrement des rendus, limites Suspense, métriques LCP/CLS/TTFB/FCP/INP.

- **Audits d'accessibilité** : moteur axe-core embarqué, fonctionnant hors ligne et sous CSP strict, avec sortie structurée par règle/impact.

- **WebMCP (expérimental)** : découverte et invocation d'outils exposés directement par une page web, avec traitement explicite de ces métadonnées comme du contenu non fiable.

- **Serveur MCP intégré** : `agent-browser mcp` démarre un serveur MCP en stdio avec plusieurs profils d'outils (`core` par défaut, `network`, `state`, `debug`, `tabs`, `react`, `mobile`, `all`) pour limiter le contexte exposé à l'agent.

- **Système de plugins** : extension par exécutables externes déclarant des capacités (`credential.read`, `browser.provider`, `launch.mutate`, `command.run`), installables depuis npm ou GitHub.

## Analyse
|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 49 700 au 11 novembre 2026._

### Points forts

- **Conçu nativement pour les agents IA** plutôt qu'adapté après coup : snapshots avec refs stables, mode batch, serveur MCP par profils, gestion explicite du contenu non fiable des pages.

- **Daemon natif Rust léger**, sans dépendance Node.js/Playwright à l'exécution, ce qui simplifie le déploiement ; les tests indépendants le jugent rapide et économe en contexte par rapport à un échange de captures d'écran, sans benchmark contrôlé face à Playwright.

- **Gestion de l'authentification très aboutie** : coffre-fort chiffré, profils Chrome réutilisables, restauration automatique de session — un point souvent faible dans les outils d'automatisation classiques utilisés par des agents.

- **Modèle de sécurité explicite pour les LLM** : allowlist de domaines, marqueurs de délimitation, politiques d'action et confirmations, traitant frontalement le risque d'injection de prompt via des pages web.

- **Rythme de développement soutenu** pour un projet relativement jeune, publié par Vercel Labs (685 commits, centaines d'issues/PR actives) ; sa popularité mesure l'attention portée au projet, non sa fiabilité sur des scénarios critiques.

- **Fonctionnalités avancées différenciantes** : introspection React/Web Vitals, audits d'accessibilité axe-core embarqués, diff visuel et de snapshot, WebMCP expérimental.

### Limites

- **Dépendance à Chrome/Chromium** : nécessite Chrome for Testing (ou une installation Chrome/Brave existante) ; pas de support natif Firefox/WebKit contrairement à Playwright.

- **Surface fonctionnelle très large**, avec de nombreuses options et variables d'environnement, ce qui peut rendre la prise en main initiale plus complexe qu'un outil plus ciblé.

- **Fonctionnalités expérimentales** (WebMCP notamment) encore en évolution, avec des garde-fous de sécurité présentés comme des indices de provenance et non comme une frontière de sécurité absolue contre l'injection de prompt.

- **Projet jeune comparé à Playwright/Puppeteer** : écosystème et documentation tierce (tutoriels, retours d'expérience communautaires) encore moins développés qu'un outil établi depuis plusieurs années.

- **Pas un socle de QA déterministe** : pour des suites de tests reproductibles, des assertions et une CI, [[Playwright]] reste souvent le meilleur choix ; les scénarios critiques exécutés avec Agent Browser doivent être validés, et l'abstraction ajoutée évolue vite.

- **Isolation toujours nécessaire** : les protections contre l'injection de prompt ne dispensent ni d'isoler les sessions ni de confirmer les actions sensibles ; l'idée de snapshots d'accessibilité pour agents n'est par ailleurs pas totalement nouvelle.

### Qualité

**Commentaire :** documentation exceptionnellement détaillée dans le README (installation, commandes, sécurité, authentification, MCP), avec une réflexion produit clairement centrée sur les besoins spécifiques des agents IA (snapshots stables, traitement du contenu non fiable, coffre-fort de credentials). La précision des descriptions est notée ★★★★☆ : les propriétés de sécurité sont décrites par le projet lui-même et n'ont pas été vérifiées de façon indépendante. La maturité reste légèrement en retrait de projets plus anciens comme Playwright. Voir [[#Avis indépendants|les avis indépendants]].

## Relations

- **Alternative à :** [[Playwright]], Puppeteer

- **S'intègre avec :** [[Claude Code]], Cursor, tout client MCP

- **Utilise :** Chrome for Testing / Chromium (via CDP), Model Context Protocol, axe-core

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Les tests saluent surtout son interface pensée pour les agents : snapshots d’accessibilité compacts, références stables, faible surcharge et commandes faciles à enchaîner. Pour piloter un navigateur depuis un terminal, il est jugé rapide et plus économe en contexte qu’un échange de captures d’écran.

Les avis plus mesurés rappellent que l’idée n’est pas totalement nouvelle et que Playwright reste une base plus mature pour les tests reproductibles. Agent Browser est excellent comme **outil de navigation d’agent**, mais son abstraction supplémentaire, son évolution rapide et ses fonctions expérimentales demandent de valider les scénarios critiques. Les protections contre l’injection de prompt ne suppriment pas le besoin d’isoler les sessions et de confirmer les actions sensibles.

### Comparaison

Face à Playwright CLI, Agent Browser privilégie la sobriété et l’interaction agentique ; Playwright conserve l’avantage pour les suites de tests, les assertions et l’écosystème. Browser Use ajoute une boucle d’agent autonome et le choix des modèles, au prix d’un système plus lourd.

### Verdict

Un très bon choix pour donner un navigateur à un coding agent ; pour du QA déterministe, Playwright reste souvent le meilleur socle.

## Sources

- [GitHub](https://github.com/vercel-labs/agent-browser)

- [Vercel](https://vercel.com/)

### Sources des avis

- [Test indépendant de Agent Browser](https://wasnotwas.com/writing/agent-browser/)
- [Retour après évolution du projet](https://wasnotwas.com/writing/agent-browser-grew-up-playwright-did-too/)
- [Comparaison avec Chrome DevTools MCP](https://www.huuhka.net/browser-verification-for-coding-agents-chrome-devtools-mcp-vs-agent-browser/)

_Dernière analyse : 12 novembre 2026_
