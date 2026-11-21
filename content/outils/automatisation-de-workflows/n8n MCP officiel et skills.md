---
title: "n8n MCP officiel et skills"
type: outil
description: "Serveur MCP natif de n8n et pack officiel de skills pour créer, tester et modifier des workflows depuis un assistant de développement."
format: serveur-mcp
tags:
  - metier/ingenierie
  - theme/automatisation
  - theme/mcp
  - theme/tests
editeur: "n8n"
logo: "[[n8n.png]]"
site: "https://n8n.io/mcp/"
depot: "https://github.com/n8n-io/skills"
licence: "Licences n8n pour le serveur · Apache-2.0 pour les skills"
statut: disponible
derniere_maj: 2026-11-11
note_documentation: 4
note_precision: 3
note_maturite: 2
memo: "[[n8n MCP officiel et skills mémo]]"
avis_maj: 2026-11-20
modified: 2026-11-20
---

# n8n MCP officiel et skills

> Le serveur MCP intégré à n8n permet à Codex ou Claude Code d’agir sur une instance n8n. Le pack officiel `n8n-io/skills` guide l’assistant dans la conception des workflows, le choix des nœuds et les tests.

**Composition** — Un serveur au niveau de l’instance, 14 skills spécialisés et un skill d’aiguillage nommé `using-n8n-skills-official`. [Documentation MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) · [Dépôt officiel des skills](https://github.com/n8n-io/skills)

Voir aussi [[#Avis indépendants|Avis indépendants]], [[n8n MCP officiel et skills mémo]] et [[n8n]].

## Résumé

Le [[Model Context Protocol|MCP]] donne à l’assistant des outils pour inspecter, créer, tester et modifier les workflows selon la version de n8n et les droits accordés. Les [[Skill|skills]] sont chargés côté assistant. Ils apportent des consignes et des exemples sur les expressions, les sous-workflows, les boucles, les connexions aux services et la gestion des erreurs. [[Hook|Des hooks]] rappellent au client de consulter le skill adapté lors de certaines opérations. [Référence des outils MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) · [Pack officiel](https://github.com/n8n-io/skills#skills-inside)

## Fonctionnalités

|Besoin|Fonctionnement|
|---|---|
|Rechercher et inspecter|Le client peut découvrir des aperçus de workflows accessibles au compte. L’option **Available in MCP** ouvre l’accès détaillé ou l’action sur un workflow selon les permissions accordées.|
|Construire ou modifier|L’assistant consulte les schémas des nœuds, produit du code pour le Workflow SDK, le valide et enregistre le résultat comme workflow n8n.|
|Tester et publier|Le client peut tester avec des données simulées ou publier un brouillon selon les droits accordés. Les résultats de test permettent de vérifier le chemin parcouru et les sorties.|
|Appliquer les pratiques n8n|Le pack apporte des guides sur la configuration des nœuds, les expressions, la pagination, les données binaires, les agents IA et les erreurs.|

[Accès par workflow](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) · [Référence des outils](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) · [Catalogue des skills](https://github.com/n8n-io/skills#skills-inside)

## Démarrer avec Codex

Dans n8n, ouvrir **Settings → Instance-level MCP → Connect**, choisir **Codex** et autoriser la connexion OAuth. Le serveur utilise l’URL affichée dans n8n, généralement terminée par `/mcp-server/http`. Le pack officiel s’installe séparément dans Codex. Son guide indique Codex 0.142.0 ou une version ultérieure pour l’installation comme plugin. [Connexion Codex](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples#connecting-codex-cli-to-n8n-mcp-server) · [Installation du plugin](https://github.com/n8n-io/skills#codex)

**Exemple de demande.** « Crée un workflow brouillon qui reçoit un article RSS, extrait le titre et l’URL et retourne les champs pour relecture. Teste le cas d’un article avec un titre vide sur un jeu de données fictif. Laisse le workflow en brouillon. »

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Maturité|★★☆☆☆|
|Popularité|—|

### Points forts

- Connexion à un service intégré à l’instance n8n, avec OAuth et permissions par client.
- Accès au schéma des nœuds et au SDK pour vérifier la configuration avant de l’enregistrer.
- Pack spécialisé qui documente les décisions récurrentes, du choix du nœud à la reprise après erreur.

### Limites

- Les outils disponibles et leurs paramètres évoluent avec la version de n8n. Le pack et les outils exposés peuvent donc différer entre deux instances.
- La validation du SDK vérifie la définition du workflow. Un test sur données épinglées ne vérifie pas les véritables échanges avec les services simulés. Certains nœuds d’entrée-sortie sans identifiants peuvent s’exécuter pendant le test. [Référence de test](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference#test_workflow)
- Le dépôt `n8n-io/skills` mesure l’intérêt pour le pack. Le serveur fait partie du dépôt n8n, ce qui explique l’absence d’une note de popularité propre au duo.

### Qualité

La référence précise les versions et les contrats des outils. Les essais tiers corroborent la création de workflows via MCP sur quelques cas. La combinaison avec le pack officiel dispose de moins de recul que le moteur n8n.

## Relations

- **S’intègre avec** [[n8n]], [[OpenAI Codex]] et [[Claude Code]].
- **Alternative communautaire**. [`czlonkowski/n8n-mcp`](https://github.com/czlonkowski/n8n-mcp) et [son propre pack de skills](https://github.com/czlonkowski/n8n-skills) privilégient notamment la recherche de modèles et la validation de JSON. Les opérations de gestion utilisent l’API n8n.
- **Exposer une action précise**. Le [MCP Server Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger) convient pour donner à un assistant un outil métier dédié, tel que la préparation d’un brouillon. Le serveur d’instance fournit les opérations de gestion des workflows.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 20 novembre 2026._

### Ce qui est apprécié

Un utilisateur sur n8n auto-hébergé décrit la création effective d’un workflow depuis Claude.ai à partir des schémas de nœuds. Un autre apprécie la connexion distante et la validation avant l’écriture dans l’éditeur. [Essai de création](https://www.reddit.com/r/n8n/comments/1s6aytd/n8n_214_finally_ships_createupdate_workflow_via/) · [Comparaison des serveurs MCP](https://www.reddit.com/r/mcp/comments/1t7mpll/been_testing_n8ns_updated_official_mcp_against/)

### Ce qui est critiqué

Des utilisateurs rapportent plusieurs passes de correction pour les branches complexes. Une comparaison signale que réécrire la définition SDK lors des itérations peut consommer davantage de contexte que des modifications JSON ciblées. [Retours sur les workflows complexes](https://www.reddit.com/r/n8n/comments/1tnqdmt/does_n8n_mcp_really_that_nice/) · [Comparaison des serveurs MCP](https://www.reddit.com/r/mcp/comments/1t7mpll/been_testing_n8ns_updated_official_mcp_against/)

### Ce qui n’est pas établi

Ces essais portent surtout sur le serveur MCP. Ils ne mesurent pas le gain propre au pack officiel à modèle et workflow identiques.

### Comparaison

Le serveur natif offre une connexion OAuth directe à l’instance et un parcours guidé par le Workflow SDK. Le serveur communautaire propose un catalogue de modèles et des opérations de mise à jour partielle sur les workflows JSON. [Référence du serveur officiel](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference) · [Documentation du serveur communautaire](https://github.com/czlonkowski/n8n-mcp)

### Verdict

Le duo officiel est un point de départ pour créer un brouillon de workflow, l’inspecter dans n8n et le tester sur des entrées représentatives. La qualité des intégrations réelles se vérifie avec leurs propres identifiants et leurs cas d’échec.

## Sources

- [Serveur MCP d’instance](https://docs.n8n.io/connect/connect-to-n8n-mcp-server) et [référence des outils](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference).
- [Dépôt n8n-io/skills](https://github.com/n8n-io/skills) et [guide de connexion Codex](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples#connecting-codex-cli-to-n8n-mcp-server).

### Sources des avis

- [r/n8n, essai de création via MCP](https://www.reddit.com/r/n8n/comments/1s6aytd/n8n_214_finally_ships_createupdate_workflow_via/). Parcours détaillé sur une instance auto-hébergée, mars 2026. Fiabilité moyenne pour ce cas.
- [r/mcp, comparaison des serveurs officiel et communautaire](https://www.reddit.com/r/mcp/comments/1t7mpll/been_testing_n8ns_updated_official_mcp_against/). Retour sur le contexte consommé et les itérations, mai 2026. Fiabilité faible pour une généralisation.
- [r/n8n, discussion sur les workflows complexes](https://www.reddit.com/r/n8n/comments/1tnqdmt/does_n8n_mcp_really_that_nice/). Témoignages de praticiens, mai 2026. Fiabilité faible, conditions d’essai variables.

_Dernière analyse : 20 novembre 2026_
