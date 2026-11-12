---
title: "Vercel — Mémo"
type: memo
fiche: "[[Vercel]]"
date: 2026-10-11
---

# Vercel — Mémo

> Les commandes de la CLI [[Vercel]] pour déployer, gérer les variables d'environnement, lire les logs et revenir en arrière.

## Installation et connexion

```bash
npm i -g vercel          # pnpm i -g vercel, yarn global add vercel, bun add -g vercel
vercel --version
vercel login             # connexion interactive
vercel link              # relie le dossier courant à un projet Vercel
```

En CI, créer un jeton et définir la variable d'environnement `VERCEL_TOKEN` (recommandé) ou passer `--token`.

## Déployer

|Commande|Ce qu'elle fait|
|---|---|
|`vercel` (ou `vercel deploy`)|Déploiement de prévisualisation du projet.|
|`vercel deploy --prod`|Déploiement en production.|
|`vercel dev`|Reproduit l'environnement Vercel en local.|
|`vercel build` / `vercel build --prod`|Construit le projet localement ou dans votre CI.|
|`vercel list`|Liste les déploiements récents du projet.|
|`vercel inspect <url>`|Informations sur un déploiement (`--logs`, `--wait`).|
|`vercel logs <url>`|Logs d'exécution d'un déploiement (`--follow` pour suivre).|
|`vercel redeploy <url>`|Reconstruit et redéploie un déploiement existant.|
|`vercel rollback [url]`|Revient à un déploiement de production précédent.|
|`vercel promote <url>`|Promeut un déploiement existant en déploiement courant.|

## Configuration

|Commande|Ce qu'elle fait|
|---|---|
|`vercel env ls`|Liste les variables d'environnement.|
|`vercel env add NOM [environnement]`|Ajoute une variable (idem `update`, `rm`).|
|`vercel env pull [fichier]`|Écrit les variables dans un fichier local.|
|`vercel env run -- <commande>`|Exécute une commande avec les variables injectées.|
|`vercel pull`|Récupère variables et réglages du projet distant.|
|`vercel domains ls` / `add` / `rm`|Gère les domaines (`vercel domains add <domaine> <projet>`).|
|`vercel alias set <url> <domaine>`|Associe un domaine à un déploiement.|
|`vercel switch [équipe]`|Change d'équipe.|

## Pour un agent de code

|Commande|Ce qu'elle fait|
|---|---|
|`vercel agent init`|Génère un `AGENTS.md` avec les bonnes pratiques de déploiement.|
|`vercel setup`|Installe le plugin Vercel pour Claude Code et Codex et connecte AI Gateway.|
|`vercel mcp`|Configure un client MCP pour le projet.|
|`vercel skills`|Découvre les skills d'agent pertinentes pour le projet.|

## Conseils d'utilisation

- **Utiliser les déploiements de prévisualisation par pull request** avant de passer en production.
- **`vercel rollback` avant d'investiguer** si la production est cassée : le retour arrière est rapide.
- **Passer par `VERCEL_TOKEN`** en CI plutôt que par `--token`, visible dans les listes de processus.
- **Surveiller `vercel usage`** : les coûts augmentent avec le trafic et l'usage des fonctions managées.

## Sources

- [Vercel — vue d'ensemble de la CLI](https://vercel.com/docs/cli)
