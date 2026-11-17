---
title: "Perplexity API Platform MCP Server"
type: outil
description: "Serveur MCP officiel de Perplexity, hébergé ou local : recherche web, réponses sourcées, raisonnement et recherche approfondie, facturés à l'usage."
format: serveur-mcp
tags:
  - metier/direction
  - metier/marketing-ventes
  - theme/mcp
  - theme/recherche
editeur: "Perplexity AI"
site: "https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server"
depot: "https://github.com/perplexityai/modelcontextprotocol"
licence: "MIT"
statut: disponible
derniere_maj: 2026-10-21
etoiles: 2633
forks: 393
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 3
memo: "[[Perplexity MCP mémo]]"
avis_maj: 2026-11-15
modified: 2026-11-15
---

# Perplexity API Platform MCP Server

> Serveur [[Model Context Protocol|MCP]] officiel de Perplexity : il donne à Claude Code, Codex, Cursor ou tout client MCP quatre outils de recherche web (résultats bruts, réponse sourcée, raisonnement, recherche approfondie), facturés à l'usage sur l'API Perplexity.

> [!note] Changement de fiche
> Jusqu'au 15 novembre 2026, cette fiche décrivait `perplexity-control-mcp`, un serveur communautaire dont le dépôt a disparu (erreur 404 constatée le 11 novembre 2026). Elle décrit désormais le serveur officiel maintenu par Perplexity.

**Composition** : 4 outils MCP, un serveur distant hébergé par Perplexity, un paquet npm (`@perplexity-ai/mcp-server`, version 1.3.0) et un plugin Claude Code.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Perplexity MCP mémo]] pour le mémo pratique.

## Résumé

Le serveur relie un agent aux API de Perplexity. Il existe sous deux formes qui exposent les mêmes outils : un **serveur distant** hébergé par Perplexity (`https://api.perplexity.ai/mcp`), qui accepte une connexion OAuth (« Sign in with Perplexity ») ou une clé d'API, et un **serveur local** lancé par `npx`, qui lit la clé dans l'environnement. Le dépôt permet aussi un auto-hébergement en HTTP (Docker ou Node.js).

`perplexity_search` interroge la Search API et renvoie des résultats classés. Les trois autres outils passent par l'Agent API de Perplexity, avec un réglage (« preset ») plus ou moins approfondi : `fast` pour `perplexity_ask`, `medium` pour `perplexity_reason`, `high` pour `perplexity_research`. Jusqu'en 2026, ils appelaient les modèles Sonar (`sonar-pro`, `sonar-reasoning-pro`, `sonar-deep-research`) ; Perplexity règle désormais les presets lui-même, et les résultats peuvent donc évoluer sans changement de version du serveur.

Chaque appel est facturé au tarif de l'API sur la clé ou l'organisation utilisée : 5 $ pour 1 000 recherches avec la Search API (1 $ en mode rapide), et pour l'Agent API des jetons au tarif du modèle plus des frais d'outils, au 15 novembre 2026. Le serveur n'utilise pas un abonnement Perplexity Pro.

## Fonctionnalités

- `perplexity_search` : résultats classés avec titre, URL, extrait et dates de publication ; filtres de récence (`search_recency_filter`) et de domaines (`search_domain_filter`) ; mode rapide et moins cher (`search_type: "fast"`).
- `perplexity_ask` : réponse rédigée et sourcée à partir d'une recherche web en temps réel.
- `perplexity_reason` : raisonnement en plusieurs étapes pour une question analytique.
- `perplexity_research` : recherche approfondie avec citations ; elle peut durer plusieurs minutes, et le serveur transmet sa progression aux clients qui la demandent.
- Budgets de contexte réglables pour `perplexity_ask` et `perplexity_reason` (`max_tokens`, jusqu'à 120 000 ; `max_tokens_per_page`, jusqu'à 20 000).
- Serveur distant avec OAuth, sans clé à copier ; serveur local en stdio ; mode HTTP auto-hébergé, limité par défaut à l'interface locale (`BIND_ADDRESS=127.0.0.1`).
- Proxy d'entreprise (`PERPLEXITY_PROXY`), délai réglable (`PERPLEXITY_TIMEOUT_MS`, 5 minutes par défaut), journalisation (`PERPLEXITY_LOG_LEVEL`).
- Plugin Claude Code et format Agent Plugins ; bibliothèque Node.js (`createPerplexityServer`) pour embarquer le serveur dans une autre application.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (15 novembre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 2 633 au 16 novembre 2026._

### Points forts

- Maintenu par l'éditeur de l'API, sous licence MIT.
- Serveur hébergé : rien à installer ni à mettre à jour, et la connexion OAuth évite de manipuler une clé.
- Quatre outils gradués, de la recherche brute à la recherche approfondie : l'agent peut choisir le niveau de coût et de latence.
- Réponses sourcées : une question factuelle demande moins d'appels d'outils qu'avec un moteur qui renvoie des liens (selon ChatForest).
- Options d'entreprise documentées : proxy, auto-hébergement fermé par défaut aux autres machines, délai réglable.

### Limites

- Payant dès le premier appel : une clé d'API demande un moyen de paiement, sans offre gratuite, alors que Brave Search, Tavily et Exa offrent des crédits mensuels (selon ContextBolt).
- Coût difficile à prévoir pour `perplexity_ask`, `perplexity_reason` et `perplexity_research` : il dépend des jetons et des outils que le preset utilise.
- `perplexity_research` peut dépasser le délai de nombreux clients MCP (souvent 60 secondes) : il faut relever le délai du serveur et celui du client.
- Les outils de synthèse ne montrent à l'agent que la réponse de Perplexity : les pages sources restent à vérifier.
- Le contenu web renvoyé n'est pas marqué comme non fiable : une proposition en ce sens est ouverte depuis le 13 octobre 2026 (risque d'injection de consignes par une page web).
- Les limites de débit des nouveaux comptes sont basses et augmentent avec les dépenses cumulées (selon ChatForest).

### Qualité

**Commentaire :** contrairement aux autres serveurs officiels de recherche, qui renvoient des résultats à lire, il fournit à l'agent des réponses rédigées et sourcées (« le chemin le plus court de la question à la réponse », selon ChatForest), à condition d'accepter un coût à l'usage et de vérifier les sources. La documentation est complète (serveur distant, local, auto-hébergé, proxy, dépannage) ; la maturité reste limitée par le passage récent des modèles Sonar aux presets de l'Agent API et par l'absence de test indépendant en conditions réelles.

## Relations

- **Alternative à :** les serveurs MCP officiels de Brave Search, Tavily et Exa, qui renvoient des résultats à lire plutôt qu'une réponse rédigée
- **Complémentaire de :** [[Firecrawl]], pour extraire les pages citées dans une réponse
- **S'intègre avec :** [[Claude Code]] · [[OpenAI Codex]] · Cursor · VS Code · Claude Desktop · Windsurf · Kiro · tout client MCP
- **Utilise :** [[Perplexity API]] (Search API et Agent API) · [[Model Context Protocol]]

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 15 novembre 2026._

### Ce qui est apprécié

- Les réponses rédigées avec citations raccourcissent le chemin entre une question et une réponse vérifiable ; ChatForest le note 4 sur 5 pour cette raison.
- Le serveur hébergé supprime l'installation locale, et la maintenance par l'éditeur inspire plus confiance que les nombreux serveurs communautaires (ChatForest).
- Le dépôt compte peu de problèmes ouverts (24 issues et pull requests au 15 novembre 2026).
- Sur le produit de recherche approfondie de Perplexity, sur lequel s'appuie `perplexity_research`, HundredTabs a jugé les citations les plus précises des trois outils testés, chaque affirmation renvoyant à une source numérotée.

### Ce qui est critiqué

- Pas d'offre gratuite et un moyen de paiement obligatoire, la barrière d'entrée la plus haute de la catégorie selon ChatForest ; ContextBolt fait le même constat.
- Coût imprévisible des outils fondés sur l'Agent API (ChatForest, ContextBolt).
- Délais : une recherche approfondie dure plusieurs minutes et dépasse le délai par défaut de nombreux clients (ChatForest).
- La synthèse peut omettre des détails à vérifier (ContextBolt) ; HundredTabs a constaté que la recherche approfondie de Perplexity manquait parfois des sources trouvées par ChatGPT ou Gemini, avec une analyse moins poussée que celle de ChatGPT.
- Avec `npx`, des messages d'installation peuvent corrompre le flux MCP dans les clients stricts (erreurs EOF) ; le README recommande `npx -yq`.

### Ce qui n'est pas établi

- Aucune source indépendante n'a testé le serveur en conditions réelles : ChatForest, rédigé par un agent IA, se fonde sur la documentation et les dépôts ; ContextBolt ne compare que les tarifs.
- La qualité des presets de l'Agent API par rapport aux anciens modèles Sonar n'a pas été comparée.
- L'affirmation de ChatForest selon laquelle `perplexity_research` serait l'outil de recherche approfondie le plus capable de l'écosystème MCP n'est pas démontrée.

### Comparaison

Les serveurs de Brave Search (index propre, 5 $ de crédits par mois), de Tavily (1 000 crédits gratuits par mois, recherche, extraction et crawl) et d'Exa (recherche sémantique, contenu nettoyé, 10 $ de crédits par mois) renvoient des sources que l'agent lit lui-même. Perplexity renvoie une réponse rédigée. Les comparatifs recommandent Perplexity pour une réponse rapide et sourcée, et un moteur de résultats quand l'agent ou l'utilisateur doit lire les sources. [[Firecrawl]] intervient ensuite pour extraire les pages.

### Verdict

Choix adapté pour obtenir des réponses sourcées dans un agent, si l'on accepte une facturation à l'usage. Pour démarrer sans payer ou pour garder la main sur les sources, préférer un serveur qui renvoie des résultats bruts. Dans tous les cas, vérifier les sources primaires des réponses importantes.

## Sources

- [Dépôt officiel](https://github.com/perplexityai/modelcontextprotocol)
- [Documentation : serveur MCP](https://docs.perplexity.ai/docs/getting-started/integrations/mcp-server)
- [Tarifs de l'API](https://docs.perplexity.ai/docs/getting-started/pricing)
- [Paquet npm `@perplexity-ai/mcp-server`](https://www.npmjs.com/package/@perplexity-ai/mcp-server)
- [Proposition : signaler les résultats comme non fiables (issue ouverte le 13 octobre 2026)](https://github.com/perplexityai/modelcontextprotocol/issues)

### Sources des avis

- [Perplexity MCP Server — ChatForest](https://chatforest.com/reviews/perplexity-mcp-server/) : revue publiée le 14 mars 2026 et mise à jour le 14 août 2026, rédigée par un agent IA à partir de la documentation, des dépôts et de retours publics, sans test pratique ; la page contient un lien de parrainage vers Claude.
- [Web Search MCP Servers: 7 Compared, and What Each Costs — ContextBolt](https://contextbolt.com/blog/web-search-mcp-servers/) : comparatif de tarifs publié le 24 août 2026 et mis à jour le 4 novembre 2026, sans test de qualité ; l'éditeur vend des produits voisins, mais pas de serveur de recherche.
- [Perplexity Deep Research vs ChatGPT vs Gemini — HundredTabs](https://hundredtabs.com/blog/deep-research-comparison-2026) : cinq tâches soumises aux trois outils (avril 2026), sans grille de notation ; porte sur le produit de recherche approfondie, pas sur le serveur MCP ; liens d'affiliation.
- [Issues du dépôt](https://github.com/perplexityai/modelcontextprotocol/issues) : problèmes et propositions publics.

_Dernière analyse : 15 novembre 2026_
