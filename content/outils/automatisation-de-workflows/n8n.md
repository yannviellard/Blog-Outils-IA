---
title: "n8n"
type: outil
description: "Éditeur visuel et moteur d’automatisation pour relier des applications, des API et des étapes IA."
format: application
tags:
  - metier/operations
  - metier/ingenierie
  - theme/automatisation
  - theme/mcp
editeur: "n8n"
logo: "[[n8n.png]]"
site: "https://n8n.io/"
depot: "https://github.com/n8n-io/n8n"
licence: "Sustainable Use License et n8n Enterprise License"
statut: disponible
derniere_maj: 2026-11-21
etoiles: 211578
forks: 61597
etoiles_releve: 2026-11-21
note_documentation: 5
note_precision: 4
note_maturite: 5
note_popularite: 5
memo: "[[n8n mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# n8n

> n8n relie des applications, des API et des bases de données dans un éditeur visuel. Un workflow peut se lancer à la réception d’un webhook, sur un horaire ou à la suite d’un événement dans une application.

Voir aussi [[#Avis indépendants|Avis indépendants]] et [[n8n mémo]].

## Résumé

Un **déclencheur** démarre le workflow. Chaque **nœud** reçoit des données, les transforme ou appelle un service, puis transmet son résultat aux étapes suivantes. On peut filtrer les entrées, créer des branches, regrouper des données ou appeler un sous-workflow réutilisable. Les expressions référencent les données entre les étapes. Un nœud Code prend le relais pour les transformations spécifiques. [Premier workflow](https://docs.n8n.io/build-your-first-workflow.md) · [Documentation n8n](https://docs.n8n.io/)

**Exemple éditorial.** Toutes les heures, n8n lit un flux RSS, écarte les liens déjà traités, extrait les champs utiles et crée un brouillon à relire. Une étape IA peut proposer un résumé. La décision de publier reste dans le processus éditorial.

## Fonctionnalités

- **Connecter des services.** Utiliser un nœud applicatif ou appeler une API avec HTTP Request. Les connexions s’appuient sur des identifiants enregistrés dans n8n.
- **Transformer les données.** Mapper les champs avec des expressions, gérer les branches et la pagination, puis réutiliser les séquences communes dans des sous-workflows.
- **Tester et diagnostiquer.** Lancer une exécution manuelle, examiner les entrées et sorties des nœuds, épingler des données de test et configurer un workflow d’erreur.
- **Ajouter de l’IA.** Insérer une tâche d’extraction ou de classification dans un workflow, ou brancher des outils sur un nœud AI Agent. [Documentation de l’IA dans n8n](https://docs.n8n.io/advanced-ai/)
- **Choisir l’hébergement.** n8n Cloud fournit le service hébergé. La Community Edition peut tourner sur sa propre infrastructure. Les offres payantes affichent des quotas d’exécutions de workflows et des fonctionnalités différentes selon le plan. [Offres](https://n8n.io/pricing/) · [Installation Docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker.md)

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★★|
|Précision des descriptions|★★★★☆|
|Maturité|★★★★★|
|Popularité|★★★★★|

### Points forts

- Le même éditeur permet de partir de nœuds prêts à l’emploi puis de descendre au niveau de l’API lorsque nécessaire.
- L’historique d’exécution aide à localiser une donnée inattendue ou un appel en échec.
- L’auto-hébergement donne la maîtrise de l’infrastructure qui exécute et stocke les workflows.

### Limites

- Les workflows longs demandent une gestion explicite des erreurs, des doublons et des limites des services appelés.
- En auto-hébergement, l’équipe assume les mises à jour, les sauvegardes et la disponibilité. Les services externes et les modèles restent facturés selon leurs propres conditions.
- Le code est accessible sous des licences avec des conditions d’usage. Pour héberger n8n en tant que service payant ou l’intégrer à un produit commercial, vérifier les usages autorisés et les conditions de l’offre. [Licence du dépôt](https://github.com/n8n-io/n8n/blob/master/LICENSE.md)

### Qualité

La documentation couvre l’éditeur, l’exécution et le déploiement. Les retours de terrain confirment la souplesse des branches et des intégrations, avec des coûts d’exploitation variables. Le [dépôt public](https://github.com/n8n-io/n8n) et son historique attestent plusieurs années de développement.

## Relations

- **Alternatives**. [Make](https://www.make.com/) et [Zapier](https://zapier.com/) pour l’automatisation visuelle de services.
- **Extension**. [[n8n MCP officiel et skills]] pour construire et tester des workflows depuis un assistant externe.
- **MCP dans un workflow**. Le [MCP Server Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger) expose des actions choisies. Le [MCP Client Tool](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp) donne à un agent n8n accès à des outils externes.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

Les équipes qui déploient n8n apprécient la souplesse des branches, les appels API personnalisés et la possibilité de gérer leur propre hébergement. [Retour d’Osher Digital](https://osher.com.au/blog/n8n-review-powerful-workflow-automation-tool/) · [Retour de Metanow](https://www.metanow.com/blog/process-engineering-26/self-hosted-n8n-vs-zapier-and-make-what-we-learned-740)

### Ce qui est critiqué

Le déploiement et l’entretien demandent davantage de compétences techniques qu’un service géré. Le coût complet dépend du temps consacré à la reprise après incident, aux mises à jour et aux sauvegardes. [Retour de Metanow](https://www.metanow.com/blog/process-engineering-26/self-hosted-n8n-vs-zapier-and-make-what-we-learned-740) · [Essai d’Accelrio](https://www.accelrio.com/make-vs-n8n/)

### Ce qui n’est pas établi

Les comparatifs consultés reposent sur des workflows et des volumes particuliers. Leurs seuils de rentabilité dépendent du prix de l’hébergement, des abonnements et du temps de maintenance. [Essai d’Accelrio](https://www.accelrio.com/make-vs-n8n/)

### Comparaison

Make et Zapier conviennent aux équipes qui cherchent à connecter rapidement des services SaaS dans un environnement géré. L’intérêt de n8n augmente lorsque le processus implique des branches complexes, des API spécifiques ou une contrainte d’hébergement. [Retour de Metanow](https://www.metanow.com/blog/process-engineering-26/self-hosted-n8n-vs-zapier-and-make-what-we-learned-740)

### Verdict

n8n convient aux équipes qui ont un processus récurrent à formaliser et une personne capable de suivre ses exécutions. Les gains de mise en place se mesurent autant à la reprise sur erreur qu’au premier workflow réussi.

## Sources

- [Documentation n8n](https://docs.n8n.io/) et [dépôt officiel](https://github.com/n8n-io/n8n).
- [Dernière version stable au 20 novembre 2026](https://github.com/n8n-io/n8n/releases/tag/n8n%402.48.7).
- [Offres](https://n8n.io/pricing/) et [texte des licences](https://github.com/n8n-io/n8n/blob/master/LICENSE.md).

### Sources des avis

- [Osher Digital](https://osher.com.au/blog/n8n-review-powerful-workflow-automation-tool/). Retour d’une agence qui déploie des automatisations chez ses clients. Fiabilité moyenne pour les observations de terrain.
- [Metanow](https://www.metanow.com/blog/process-engineering-26/self-hosted-n8n-vs-zapier-and-make-what-we-learned-740). Retour d’un intégrateur sur trois plateformes. Fiabilité moyenne, contexte propre à ses projets.
- [Accelrio](https://www.accelrio.com/make-vs-n8n/). Essai comparatif sur deux workflows. Fiabilité moyenne pour ce périmètre, liens d’affiliation déclarés avec Zapier et Fiverr.

_Dernière analyse : 20 novembre 2026_
