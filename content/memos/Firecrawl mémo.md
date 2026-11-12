---
title: "Firecrawl — Mémo"
type: memo
fiche: "[[Firecrawl]]"
date: 2026-09-25
---

# Firecrawl — Mémo

> Les commandes à connaître pour utiliser [[Firecrawl]] depuis Claude Code ou Codex : rechercher sur le web, récupérer une page en Markdown propre, cartographier ou parcourir un site entier. Firecrawl s'utilise via une skill + CLI, ou via un serveur MCP.

## Installation

```bash
# Skill + CLI pour Claude Code, Cursor, OpenCode… (redémarrer l'agent ensuite)
npx -y firecrawl-cli@latest init --all --browser

# Se connecter (1 000 crédits offerts à l'inscription)
firecrawl login --browser
firecrawl --status        # vérifie l'authentification et les crédits restants
```

Serveur MCP (alternative) :

```json
{
  "mcpServers": {
    "firecrawl-mcp": {
      "command": "npx",
      "args": ["-y", "firecrawl-mcp"],
      "env": { "FIRECRAWL_API_KEY": "fc-VOTRE_CLE" }
    }
  }
}
```

## Commandes principales

|Commande|Ce qu'elle fait|Coût indicatif|
|---|---|---|
|`firecrawl search "requête" --limit 5`|Cherche sur le web et renvoie le contenu des résultats (`--scrape` pour le contenu complet).|1 crédit par requête|
|`firecrawl scrape <url>`|Récupère une page en Markdown propre.|1 crédit par page|
|`firecrawl scrape <url> --only-main-content`|Retire menus, pieds de page et publicités.|1 crédit|
|`firecrawl scrape <url> --format markdown,links -o page.json`|Plusieurs formats en JSON, sauvegardés dans un fichier.|1 crédit|
|`firecrawl scrape <url> --schema schema.json`|Extrait des données structurées selon un schéma.|—|
|`firecrawl map <url> --search "pricing"`|Liste les URL d'un site, triées par pertinence, **sans les récupérer**.|faible|
|`firecrawl crawl <url> --limit 100 --max-depth 2 --wait`|Parcourt un site entier et récupère toutes les pages.|1 crédit par page|
|`firecrawl interact exec --prompt "Clique sur le premier résultat"`|Agit sur une page déjà récupérée, en langage naturel.|—|
|`firecrawl agent "tâche de recherche" --max-credits 50`|Recherche autonome sur plusieurs pages, avec plafond de crédits.|variable|
|`firecrawl monitor create …`|Surveille les changements d'une page.|—|

Options utiles : `--wait-for` (attendre le rendu JavaScript), `--include-paths` (limiter le crawl), `--pretty` (JSON lisible), `--api-url` (instance auto-hébergée).

## Outils MCP (si tu utilises le serveur MCP)

|Outil|Quand l'utiliser|
|---|---|
|`firecrawl_scrape`|URL connue, contenu en Markdown ou en JSON selon un schéma.|
|`firecrawl_search`|Recherche web avec contenu des résultats.|
|`firecrawl_map`|Découvrir les URL d'un site avant de crawler.|
|`firecrawl_crawl`|Plusieurs pages d'un même site, avec limites.|

## Choisir la bonne commande

|Besoin|Commande|
|---|---|
|Je connais l'URL|`scrape`|
|Je cherche une information sur le web|`search`|
|Je veux savoir ce que contient un site|`map`|
|Je veux tout le contenu d'une section|`map` puis `crawl` avec `--include-paths`|
|Je dois cliquer ou remplir avant de lire|`scrape` puis `interact`|

## Conseils d'utilisation

- **Toujours `map` avant `crawl`** : tu sais combien de pages (donc de crédits) le crawl va consommer.
- **Borner les crawls** avec `--limit`, `--max-depth` et `--include-paths`.
- **`--only-main-content` par défaut** : moins de bruit, moins de tokens dans le contexte de Claude.
- **Préférer la skill au serveur MCP** si tu veux économiser du contexte : une skill se charge à la demande, un serveur MCP déclare tous ses outils dès le début.
- **Attention à la facturation d'Extract** : l'extraction structurée par IA a une facturation séparée des crédits, source fréquente de mauvaises surprises.
- **Plafonner `agent`** avec `--max-credits` : la recherche autonome peut visiter beaucoup de pages.

## Sources

- [README Firecrawl](https://github.com/firecrawl/firecrawl)
- [Documentation CLI et skill](https://docs.firecrawl.dev/sdks/cli)
- [Firecrawl dans Claude Code — documentation](https://docs.firecrawl.dev/quickstarts/claude-code)
- [Serveur MCP Firecrawl](https://github.com/firecrawl/firecrawl-mcp-server)
- [I Wired Firecrawl into Claude via MCP — Towards AI](https://pub.towardsai.net/i-wired-firecrawl-into-claude-via-mcp-heres-the-honest-breakdown-673a5e288849)
