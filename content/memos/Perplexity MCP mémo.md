---
title: "Perplexity MCP — Mémo"
type: memo
fiche: "[[Perplexity MCP]]"
date: 2026-09-25
---

# Perplexity MCP — Mémo

> L'essentiel pour utiliser [[Perplexity MCP]] (perplexity-control-mcp), le serveur MCP communautaire qui expose toute l'API Perplexity à Claude Code : réponses sourcées depuis le web, recherche brute, recherche approfondie, embeddings, estimation des coûts.

> [!warning] Dépôt introuvable
> Au 11 novembre 2026, le dépôt GitHub `itsablabla/perplexity-control-mcp` renvoie une erreur 404 : il a été supprimé ou rendu privé, et aucun paquet npm ne porte ce nom. Les commandes ci-dessous, qui partent d'un clone du dépôt, ne fonctionnent plus en l'état.

## Installation

```bash
git clone https://github.com/itsablabla/perplexity-control-mcp
cd perplexity-control-mcp
npm install
cp .env.example .env        # renseigner PERPLEXITY_API_KEY
npm run build

# Ajouter à Claude Code (chemin absolu vers dist/index.js)
claude mcp add perplexity-control -e PERPLEXITY_API_KEY=pplx-... -- node /chemin/absolu/perplexity-control-mcp/dist/index.js
```

Mode HTTP (pour un client distant) : `MCP_TRANSPORT=http MCP_PORT=3001 PERPLEXITY_API_KEY=pplx-... npm start`, puis `http://localhost:3001/mcp`.

## Outils MCP

Claude les appelle lui-même ; les nommer dans la demande aide à choisir le bon.

|Outil|Ce qu'il fait|À demander par exemple|
|---|---|---|
|`sonar_chat`|Réponse rédigée et sourcée depuis le web.|« Avec Perplexity, quelles sont les nouveautés de Next.js ce mois-ci ? »|
|`web_search`|Résultats de recherche bruts avec le contenu des pages (jusqu'à 5 requêtes à la fois).|« Récupère les 10 meilleures sources sur … »|
|`sonar_async_submit` / `sonar_async_get` / `sonar_async_list`|Recherche approfondie en tâche de fond : soumettre, puis récupérer le résultat.|« Lance une deep research sur … et récupère le rapport. »|
|`agent_create`|API Agent de Perplexity : raisonnement en plusieurs étapes avec outils. Presets : `fast-search`, `pro-search`, `deep-research`, `advanced-deep-research`.|—|
|`embeddings_create` / `embeddings_contextualized`|Vecteurs d'embedding (pour une base RAG).|—|
|`estimate_cost`|Estime le coût en dollars **avant** d'envoyer la requête.|« Combien coûterait cette recherche ? »|
|`list_models`|Catalogue des modèles disponibles.|—|
|`health_check`|Vérifie que l'API répond.|—|
|`api_key_generate` / `api_key_revoke` / `api_key_rotate`|Gère les clés API. **La révocation est irréversible.**|—|

## Choisir le modèle Sonar

|Modèle|Usage|
|---|---|
|`sonar`|Question factuelle simple, rapide et peu chère.|
|`sonar-pro`|Bon équilibre, pour la plupart des questions.|
|`sonar-reasoning-pro`|Analyse complexe qui demande un raisonnement.|
|`sonar-deep-research`|Recherche exhaustive multi-sources (plusieurs minutes, nettement plus cher). À lancer en asynchrone.|

## Filtres utiles

|Paramètre|Effet|
|---|---|
|`search_recency_filter`|`day`, `week`, `month`, `year` : limite aux sources récentes.|
|`search_domain_filter`|Liste de domaines à inclure, ou à exclure avec le préfixe `-` (ex. `-pinterest.com`).|
|`search_after_date_filter` / `search_before_date_filter`|Plage de dates précise.|
|`search_mode`|`academic` (sources académiques) ou `sec` (documents financiers américains).|

## Conseils d'utilisation

- **Choisir le modèle le moins cher qui suffit** : `sonar` pour un fait, `sonar-pro` par défaut, la deep research seulement pour un vrai dossier.
- **Passer par `estimate_cost`** avant une recherche lourde : une deep research coûte plusieurs fois une requête simple.
- **Filtrer par date** pour tout sujet qui évolue vite (frameworks, versions, actualité), et par domaine pour s'en tenir à la documentation officielle.
- **Lancer les recherches longues en asynchrone** (`sonar_async_submit`) pour ne pas bloquer la session.
- **Ne jamais laisser l'agent révoquer ou faire tourner les clés sans confirmation** : une clé révoquée casse immédiatement toutes les intégrations qui l'utilisent.
- **Serveur communautaire** : pour un besoin simple (chercher, demander, rechercher, raisonner), le serveur MCP officiel de Perplexity suffit et est maintenu par l'éditeur.

## Sources

- [README perplexity-control-mcp](https://github.com/itsablabla/perplexity-control-mcp)
- [Serveur MCP officiel Perplexity](https://github.com/perplexityai/modelcontextprotocol)
- [Your AI Coding Agent Is Only as Good as Its Search Engine — Medium](https://medium.com/@haberlah/your-ai-coding-agent-is-only-as-good-as-its-search-engine-fba1d34c1f0c)
- [Perplexity API Search Configuration Best Practices](https://www.neura.market/directories/perplexity/rules/perplexity-api-search-configuration-best-practices)
