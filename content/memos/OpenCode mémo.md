---
title: "OpenCode — Mémo"
type: memo
fiche: "[[OpenCode]]"
date: 2026-10-11
---

# OpenCode — Mémo

> Les commandes de [[OpenCode]] : lancer la TUI, exécuter un prompt en script, brancher fournisseurs et serveurs MCP, et reprendre ses sessions.

## Lancer

|Commande|Ce qu'elle fait|
|---|---|
|`opencode [projet]`|Démarre l'interface terminal (comportement par défaut).|
|`opencode run "message"`|Exécute un prompt sans interface, pratique en script (`-m` modèle, `--agent`, `-f` fichier, `-c` continuer, `-s` session).|
|`opencode serve`|Serveur HTTP sans interface.|
|`opencode web`|Serveur et interface web dans le navigateur.|
|`opencode attach [url]`|Connecte la TUI à un serveur déjà lancé.|
|`opencode pr <numéro>`|Récupère et bascule sur la branche d'une PR GitHub, puis lance OpenCode.|

## Fournisseurs et modèles

|Commande|Ce qu'elle fait|
|---|---|
|`opencode auth login`|Ajoute une clé d'API de fournisseur (stockée dans `~/.local/share/opencode/auth.json`).|
|`opencode auth list` / `auth logout`|Liste les fournisseurs authentifiés / retire des identifiants.|
|`opencode models [fournisseur]`|Liste les modèles disponibles au format `fournisseur/modèle` (`--refresh`).|

## Agents, MCP et extensions

|Commande|Ce qu'elle fait|
|---|---|
|`opencode agent create` / `agent list`|Crée un agent personnalisé / liste les agents.|
|`opencode mcp add` / `mcp list`|Ajoute un serveur MCP local ou distant / liste les serveurs et leur état.|
|`opencode mcp auth <nom>`|Authentification OAuth d'un serveur MCP.|
|`opencode plugin <module>`|Installe un plugin et met à jour la configuration.|
|`opencode github install`|Met en place le workflow GitHub Actions.|

## Sessions et suivi

|Commande|Ce qu'elle fait|
|---|---|
|`opencode session list`|Liste les sessions.|
|`opencode stats`|Consommation de tokens et coût (`--days`, `--models`, `--project`).|
|`opencode export [session]` / `import <fichier>`|Exporte une session en JSON / en importe une.|
|`opencode upgrade [cible]`|Met à jour OpenCode.|

Options globales : `--help`, `--version`, `--log-level`, `--print-logs`, `--pure` (sans plugins externes).

## Dans la TUI

|Commande|Ce qu'elle fait|
|---|---|
|`/init`|Crée ou met à jour `AGENTS.md` de façon guidée.|
|`/connect`|Ajoute un fournisseur et sa clé.|
|`/models`|Liste et change de modèle (`ctrl+x m`).|
|`/new` (alias `/clear`)|Nouvelle session (`ctrl+x n`).|
|`/sessions` (alias `/resume`)|Liste et change de session (`ctrl+x l`).|
|`/compact`|Compacte la session (`ctrl+x c`).|
|`/undo` / `/redo`|Annule / rétablit le dernier message et ses modifications de fichiers (dépôt Git requis).|
|`/share` / `/unshare`|Partage la session / retire le partage.|
|`/export`|Exporte la conversation en Markdown dans votre éditeur.|
|`/thinking`|Affiche ou masque les blocs de raisonnement.|

Syntaxe : `@fichier` ajoute un fichier à la conversation ; `!commande` exécute une commande shell dont la sortie est ajoutée. Touche leader par défaut : `ctrl+x`.

## Conseils d'utilisation

- **Choisir le modèle par tâche** : la qualité dépend du fournisseur sélectionné ; vérifier le coût API d'un modèle premium.
- **Vérifier les politiques d'authentification** des fournisseurs avant de compter sur un abonnement grand public.
- **Exporter ou versionner `AGENTS.md`** pour garder les conventions du dépôt d'un agent à l'autre.
- **Passer par `opencode stats`** pour suivre la dépense réelle.

## Sources

- [OpenCode — CLI](https://opencode.ai/docs/cli/)
- [OpenCode — TUI](https://opencode.ai/docs/tui/)
