---
title: "Better Auth"
type: outil
description: "Authentification TypeScript auto-gérée, extensible et indépendante du framework."
format: bibliotheque
tags:
  - metier/ingenierie
  - theme/securite
  - theme/backend
editeur: "Better Auth"
logo: "[[better-auth.png]]"
site: "https://better-auth.com/"
depot: "https://github.com/better-auth/better-auth"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 30757
forks: 3086
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 4
note_popularite: 4
memo: "[[Better Auth mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Better Auth

> Framework d'authentification et d'autorisation open source pour TypeScript, framework-agnostic et auto-hébergé. Il fournit la gestion des utilisateurs, sessions, OAuth, organisations et de nombreuses fonctionnalités avancées via un système de plugins extensible.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Better Auth mémo]] pour le mémo pratique.

## Résumé

Better Auth est une bibliothèque TypeScript destinée à intégrer l'authentification et l'autorisation directement dans une application. Contrairement à des services SaaS comme Clerk ou Auth0, l'authentification vit dans le code de l'application et les données peuvent rester dans la base de données du projet.

Le framework supporte notamment email/password, OAuth et les principaux fournisseurs sociaux, sessions, gestion des comptes, organisations et contrôle d'accès. Il fournit également une gestion de base de données et des migrations.

Son principal mécanisme d'extension est son écosystème de plugins. Better Auth fournit aujourd'hui plus de 50 plugins couvrant l'authentification, la sécurité, l'autorisation, les API, les paiements et certaines fonctionnalités enterprise.

Le projet est distribué sous licence MIT et son dépôt principal compte 398 contributeurs au 22 septembre 2026.

## Fonctionnalités

- Authentification email/password et fournisseurs OAuth/social login comme Google, GitHub et Apple.
    
- Gestion des utilisateurs, comptes et sessions avec possibilité de personnaliser le schéma de données.
    
- Support des bases SQLite, PostgreSQL, MySQL et autres configurations, avec génération et migration du schéma.
    
- Écosystème de 50+ plugins : 2FA, passkeys, magic links, OTP, username, organisations, SSO, SCIM, API keys, JWT, OAuth/OIDC, etc.
    
- Plugins serveur et client permettant d'ajouter des endpoints, schémas, middleware, hooks et règles de rate limiting.
    
- Plugin OpenAPI permettant de générer une spécification OpenAPI 3.1.1 des endpoints d'authentification et des plugins.
    
- Plugins orientés agents et MCP, notamment Agent Auth et MCP authentication.
    
- Plugin API Key pour créer, gérer et vérifier des clés d'API avec expiration, rate limiting et support des clés liées aux organisations.
    
- Possibilité de créer ses propres plugins et de les intégrer à la fois côté serveur et côté client.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★★☆|
|Popularité|★★★★☆|
|Extensibilité|★★★★★|
|Contrôle / faible lock-in|★★★★★|
|Couverture fonctionnelle|★★★★★|
|Intégration native mobile|★★☆☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 30 757 au 16 novembre 2026._

**Commentaire :** Better Auth est devenu un framework d'authentification très complet, avec une architecture particulièrement extensible grâce aux plugins et une forte maîtrise des données puisqu'il s'intègre directement au backend et à la base de données de l'application. Le projet est très actif : le dépôt principal compte 398 contributeurs et des mises à jour encore publiées en septembre 2026.

La principale réserve concerne son positionnement : Better Auth est d'abord un framework **TypeScript côté serveur/client web**. Il ne fournit pas de SDK Swift officiel équivalent à certaines solutions orientées BaaS/mobile. L'utilisation depuis une application native peut donc nécessiter des appels HTTP directs ou une implémentation cliente tierce.

### Points forts

- **Open source et MIT** : possibilité d'héberger et de contrôler entièrement la couche d'authentification.
    
- **Très grande extensibilité** grâce aux plugins officiels et communautaires.
    
- **Pas limité à un fournisseur de base de données** : PostgreSQL, MySQL, SQLite et autres configurations sont supportés.
    
- **Architecture framework-agnostic**, avec intégration de nombreux frameworks TypeScript et runtimes.
    
- **Large couverture fonctionnelle** allant de l'authentification classique aux organisations, SSO, SCIM, API keys et protocoles OAuth/OIDC.
    
- **Extensible par ses propres plugins**, ce qui permet d'adapter le modèle de données et les endpoints aux besoins d'une application.
    
- **Orientation moderne vers les agents IA**, avec des fonctionnalités Agent Auth et MCP présentes dans l'écosystème officiel.
    
- **OpenAPI intégré**, facilitant la documentation et la génération éventuelle de clients pour des consommateurs non-TypeScript.
    

### Limites

- **Pas un Backend-as-a-Service** : contrairement à Supabase, Better Auth ne fournit pas PostgreSQL, Storage, Realtime ou les autres briques d'un backend complet.
    
- **Responsabilité d'infrastructure** : le déploiement, la base de données, les emails transactionnels et les autres services nécessaires restent à intégrer et exploiter.
    
- **Écosystème principalement TypeScript** : moins adapté lorsqu'une application cliente native doit disposer d'un SDK officiel dans un autre langage.
    
- **Complexité potentielle** : le grand nombre de plugins et d'options peut nécessiter davantage de décisions d'architecture qu'une solution SaaS très intégrée.
    
- **La sécurité et l'exploitation passent à l'équipe** : contrairement à un service managé comme Clerk (plus rapide à mettre en place), l'équipe porte les migrations, les e-mails transactionnels, les correctifs et la revue de sécurité de sa couche d'authentification ; choisir une bibliothèque auto-gérée n'élimine pas la nécessité d'une revue de sécurité sérieuse.
    
- **Moins d'historique que les solutions établies** : l'écosystème est dynamique mais plus récent que celui d'Auth.js ou de Clerk.
    
- **Plugins communautaires à évaluer individuellement** : Better Auth précise que les plugins communautaires ne sont ni officiels ni vérifiés par l'équipe du projet.
    
- **OpenAPI encore en développement** : le plugin OpenAPI est actuellement présenté comme étant à un stade précoce.
    

## Relations

- **Alternative à :** [[Clerk]] (tout compris, avec coût et dépendance fournisseur), [[Auth0]], [[Supabase Auth]] (logique si l'on utilise déjà Supabase), Auth.js (familier dans les applications Next.js existantes, souvent critiqué pour sa documentation et sa longue transition de versions)
    
- **S'intègre avec :** PostgreSQL · MySQL · SQLite · OAuth · OpenID Connect · Stripe · MCP
    
- **Utilise :** TypeScript · Web APIs · bases SQL
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le sentiment développeur est nettement favorable : documentation jugée plus claire, cœur TypeScript indépendant du framework, données conservées dans sa propre base et système de plugins couvrant des besoins B2B avancés. De nombreux utilisateurs venant d’Auth.js décrivent une configuration et des erreurs plus prévisibles.

Les nuances concernent le compromis entre bibliothèque auto-gérée et service managé. Clerk reste plus rapide à mettre en place et prend en charge davantage d’opérations ; Better Auth transfère à l’équipe la sécurité, les migrations, les e-mails et l’exploitation. Son écosystème, bien que dynamique, a moins d’historique que les solutions établies. Le choix n’élimine donc pas la nécessité d’une revue de sécurité sérieuse.

### Comparaison

Auth.js reste familier dans les applications Next.js existantes mais est souvent critiqué pour sa documentation et sa longue transition de versions. Clerk offre la meilleure expérience « tout compris » et des fonctions B2B prêtes à l’emploi, avec coût et dépendance fournisseur. Supabase Auth est logique lorsqu’on utilise déjà Supabase.

### Verdict

Probablement le meilleur compromis actuel pour une équipe TypeScript qui veut posséder son authentification sans tout écrire ; Clerk reste préférable si l’exploitation minimale prime.

## Sources

- [Website](https://better-auth.com/)
    
- [Documentation](https://better-auth.com/docs/introduction)
    
- [Plugins](https://better-auth.com/docs/plugins)
    
- [GitHub](https://github.com/better-auth/better-auth)
    
- [GitHub Releases](https://github.com/better-auth/better-auth/releases)
    

Mémo : [[Better Auth mémo]] pour les commandes à retenir.

### Sources des avis

- [Discussion Auth.js vs Better Auth](https://www.reddit.com/r/nextjs/comments/1kf2jrp/authjs_vs_better_auth/)
- [Comparatif Better Auth, Auth.js et Clerk](https://www.pkgpulse.com/guides/better-auth-vs-nextauth-v5-vs-clerk-2026)
- [Guide de choix avec Supabase Auth](https://www.sentinu.com/blog/saas-authentication-2026-clerk-authjs-supabase-better-auth/)

_Dernière analyse : 12 novembre 2026_