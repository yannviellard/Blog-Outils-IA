---
title: "n8n MCP officiel et skills — Mémo"
type: memo
fiche: "[[n8n MCP officiel et skills]]"
date: 2026-11-20
---

# n8n MCP officiel et skills — Mémo

> Connecter Codex à une instance n8n puis créer et tester un brouillon depuis le chat.

## Installation

Dans n8n, activer **Settings → Instance-level MCP**. Dans **Connect**, sélectionner Codex et copier l’URL du serveur. Pour le pack officiel en mode plugin, le guide demande Codex 0.142.0 ou ultérieur.

## Commandes principales

```bash
# Ajouter le serveur et autoriser OAuth
codex mcp add n8n-mcp --url "URL_DU_SERVEUR"
codex mcp login n8n-mcp
```

```bash
# Installer les skills officiels
codex plugin marketplace add n8n-io/skills
codex plugin add n8n-skills@n8n-io
```

Redémarrer Codex. Si Codex affiche la demande de confiance pour les hooks du plugin, l’approuver pour activer les rappels.

## Premier essai

1. Pour intervenir sur un workflow existant, activer **Available in MCP** dans ses paramètres et vérifier les permissions OAuth.
2. Demander à Codex de créer un brouillon avec un déclencheur manuel et un nœud Edit Fields.
3. Tester le résultat sur des données fictives et l’ouvrir dans l’éditeur n8n.

## Conseils d’utilisation

- `validate_workflow` vérifie la définition SDK.
- `test_workflow` exécute avec des données simulées pour les nœuds concernés. Certains nœuds sans identifiants s’exécutent réellement.
- Publier depuis l’éditeur après vérification des branches et des effets externes.

## Sources

- [Connexion OAuth à Codex](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-client-examples#connecting-codex-cli-to-n8n-mcp-server)
- [Installation des skills officiels](https://github.com/n8n-io/skills#codex)
- [Référence des outils MCP](https://docs.n8n.io/connect/connect-to-n8n-mcp-server/mcp-server-tools-reference)
