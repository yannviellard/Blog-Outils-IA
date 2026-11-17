---
title: "Agentic Inbox"
type: outil
description: "Messagerie Cloudflare auto-hébergée avec agent et accès MCP."
format: application
tags:
  - metier/support-client
  - metier/operations
  - theme/redaction
  - theme/mcp
editeur: "Cloudflare"
logo: "[[cloudflare.png]]"
depot: "https://github.com/cloudflare/agentic-inbox"
licence: "Apache-2.0"
statut: disponible
derniere_maj: 2026-04-17
etoiles: 8772
forks: 1155
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 2
note_popularite: 3
memo: "[[Agentic Inbox mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Agentic Inbox

> Client email auto-hébergé et open source de Cloudflare, s'exécutant entièrement sur Cloudflare Workers, avec un agent IA intégré (Cloudflare Agents SDK + Workers AI) capable de lire, chercher, rédiger et envoyer des e-mails — et exposé aussi comme serveur MCP pour être piloté par des outils externes comme Claude Code ou Cursor.

**Composition** : 1 agent (Email Agent, 9 outils), 1 serveur MCP (`/mcp`).

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours, et [[Agentic Inbox mémo]] pour les commandes à retenir.

## Résumé

Agentic Inbox est un client de messagerie complet — envoi, réception, threading, dossiers, recherche, pièces jointes — qui tourne intégralement sur l'infrastructure Cloudflare : les e-mails entrants arrivent via Cloudflare Email Routing, chaque boîte mail est isolée dans son propre Durable Object avec une base SQLite dédiée, et les pièces jointes sont stockées dans R2. Il n'y a donc ni serveur SMTP/IMAP traditionnel à administrer, ni base de données centralisée à provisionner : toute la persistance et l'isolation par boîte repose sur le modèle Durable Objects de Cloudflare.

Sa particularité est l'intégration d'un agent IA (« Email Agent ») construit avec le Cloudflare Agents SDK (`AIChatAgent`) et Workers AI (modèle `@cf/moonshotai/kimi-k2.5` par défaut), affiché dans un panneau latéral avec 9 outils dédiés à la lecture, la recherche et la rédaction d'e-mails. L'agent peut générer automatiquement un brouillon de réponse dès qu'un nouvel e-mail arrive, mais l'envoi requiert toujours une confirmation explicite de l'utilisateur — un garde-fou volontaire contre l'envoi automatique non supervisé. Chaque boîte mail peut avoir son propre prompt système, et l'historique de conversation avec l'agent est persistant.

Le projet expose aussi un serveur MCP à l'URL `/mcp`, permettant à des agents de code externes (Claude Code, Cursor…) d'opérer directement sur les boîtes mail via ce protocole. Le README souligne un point de sécurité important : l'autorisation d'accès repose entièrement sur la politique Cloudflare Access partagée — tout utilisateur qui la franchit peut accéder à toutes les boîtes mail de l'instance, y compris via le serveur MCP en passant un simple paramètre `mailboxId`, sans autorisation fine par boîte.

## Fonctionnalités

- **Client email complet** : envoi/réception via Cloudflare Email Routing, éditeur de texte riche, threading réponse/transfert, organisation en dossiers, recherche, gestion des pièces jointes.

- **Isolation par boîte mail** : chaque mailbox s'exécute dans son propre Durable Object avec stockage SQLite dédié ; les pièces jointes sont stockées dans R2.

- **Agent IA intégré** : panneau latéral avec 9 outils email (lecture, recherche, rédaction, envoi) construits sur le Cloudflare Agents SDK et Workers AI.

- **Brouillon automatique sur e-mail entrant** : l'agent lit les e-mails reçus et génère un brouillon de réponse, l'envoi restant systématiquement soumis à confirmation explicite.

- **Configuration persistante par boîte** : prompt système personnalisé par mailbox, historique de conversation persistant, réponses en streaming markdown, visibilité des appels d'outils de l'agent.

- **Serveur MCP intégré** (`/mcp`) : permet à des clients MCP externes (Claude Code, Cursor, etc.) d'agir sur n'importe quelle boîte mail de l'instance via un paramètre `mailboxId`.

- **Déploiement en un clic** : bouton « Deploy to Cloudflare » qui provisionne automatiquement R2, Durable Objects et Workers AI, suivi d'étapes de configuration (Email Routing, Email Service, Cloudflare Access).

- **Authentification par Cloudflare Access** : validation JWT obligatoire en production, agissant comme unique frontière de confiance de l'application (pas d'autorisation par boîte au-delà de cette politique).

## Analyse
|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★☆☆☆|
|Popularité|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 8 772 au 16 novembre 2026._

### Points forts

- **Architecture serverless cohérente et 100% Cloudflare** : Durable Objects pour l'isolation par boîte, R2 pour les pièces jointes, Workers AI pour l'agent — une démonstration concrète et complète de la stack agentique de Cloudflare (Agents SDK, Workers AI, Email Routing/Service, MCP) dans un seul projet réel.

- **Garde-fou explicite sur l'automatisation** : l'auto-génération de brouillons sans envoi automatique est un choix de conception assumé, qui évite le risque d'un agent envoyant des e-mails sans supervision humaine.

- **Exposition MCP native**, permettant de piloter sa messagerie directement depuis un agent de code externe plutôt que de se limiter à l'interface web fournie.

- **Documentation transparente sur les limites de sécurité** : le README énonce explicitement que l'autorisation repose entièrement sur Cloudflare Access et qu'il n'existe pas d'autorisation fine par boîte mail — une honnêteté rare qui évite les malentendus en déploiement partagé.

- **Porté par Cloudflare** : projet de référence publié par l'éditeur de la plateforme (forte audience en peu de commits, indicateur d'attention plutôt que de robustesse) ; dernière mise à jour visible : 17 avril 2026.

### Limites

- **Absence d'autorisation par boîte mail** : n'importe quel utilisateur validé par la politique Cloudflare Access peut accéder à toutes les mailboxes de l'instance, y compris via MCP — un modèle de confiance adapté à un usage personnel/petite équipe mais risqué pour un déploiement multi-utilisateurs sans confiance mutuelle.

- **Dépendance totale à l'écosystème Cloudflare** (Workers, Durable Objects, R2, Email Routing/Service, Workers AI, Access) : aucune portabilité vers un autre hébergeur sans réécriture significative.

- **Projet jeune avec peu de commits/contributeurs visibles** malgré la traction en étoiles, ce qui suggère une maturité encore limitée en termes de robustesse opérationnelle à grande échelle.

- **Configuration multi-étapes non triviale** (Email Routing, Email Service, Cloudflare Access, secrets `POLICY_AUD`/`TEAM_DOMAIN`) au-delà du simple bouton de déploiement, comme le souligne le README lui-même.

### Qualité

**Commentaire :** projet bien documenté et explicite sur ses propres limites de sécurité (voir [[#Avis indépendants|les avis indépendants]]), avec une architecture serverless exemplaire pour illustrer l'usage combiné du Cloudflare Agents SDK, de Workers AI et de MCP sur un cas d'usage concret (messagerie). La maturité reste celle d'un jeune projet de démonstration/référence plutôt que d'une solution de messagerie professionnelle éprouvée à grande échelle.

## Relations

- **Alternative à :** clients email self-hosted classiques (Roundcube, Mailcow) sans agent IA intégré

- **S'intègre avec :** [[Claude Code]], Cursor (via le serveur MCP), Cloudflare Access

- **Utilise :** Cloudflare Workers, Durable Objects (SQLite), R2, Cloudflare Email Routing/Email Service, Cloudflare Agents SDK (`AIChatAgent`), Workers AI (`@cf/moonshotai/kimi-k2.5`), AI SDK v6, Hono, React 19, React Router v7

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le projet est apprécié comme démonstration cohérente du stack Cloudflare : Workers, Durable Objects, R2, Email Routing, Workers AI et MCP forment une boîte mail auto-hébergée sans serveur traditionnel. Le brouillon automatique avec confirmation avant envoi est également perçu comme un garde-fou raisonnable.

Les réserves sont importantes pour un usage professionnel : configuration Cloudflare non triviale, dépendance forte à cet écosystème et autorisation encore grossière entre boîtes. La documentation indique qu’un utilisateur admis par la politique Cloudflare Access peut atteindre toutes les boîtes de l’instance. Le projet est donc davantage un excellent exemple technique ou une base à durcir qu’un remplaçant immédiat de Gmail, Outlook ou Superhuman.

### Comparaison

Gmail et Outlook offrent maturité, recherche, conformité et administration. Agentic Inbox gagne sur le contrôle du code, l’isolation par Durable Object et l’accès MCP, mais demande de prendre en charge sécurité et exploitation.

### Verdict

Très intéressant pour des agents ou boîtes dédiées ; déconseillé comme messagerie d’entreprise principale sans revue de sécurité et contrôle d’accès supplémentaire.

## Sources

- [GitHub](https://github.com/cloudflare/agentic-inbox)

### Sources des avis

- [Revue Agentic Inbox](https://www.promptquorum.com/power-local-llm/agentic-inbox-review)
- [Retour du créateur et discussion Cloudflare](https://www.reddit.com/r/CloudFlare/comments/1upmx2d/i_built_a_selfhosted_email_client_on_top_of/)
- [Dépôt officiel](https://github.com/cloudflare/agentic-inbox)

_Dernière analyse : 12 novembre 2026_
