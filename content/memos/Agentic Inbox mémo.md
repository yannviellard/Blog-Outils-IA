---
title: "Agentic Inbox — Mémo"
type: memo
fiche: "[[Agentic Inbox]]"
date: 2026-10-11
---

# Agentic Inbox — Mémo

> Déployer et exploiter [[Agentic Inbox]] sur Cloudflare : étapes de mise en place, commandes de développement et dépannage des erreurs d'accès.

## Déployer

1. **Déployer** depuis le bouton « Deploy to Cloudflare » du dépôt ; indiquer le domaine de réception (`DOMAINS`). Le déploiement provisionne R2, Durable Objects et Workers AI.
2. **Cloudflare Access** : activer l'accès en un clic sur le Worker (Settings > Domains & Routes) ; noter `POLICY_AUD` et `TEAM_DOMAIN`, **à définir comme secrets** du Worker.
3. **Email Routing** : créer une règle « catch-all » qui redirige vers le Worker.
4. **Email Service** : l'activer pour disposer de la liaison `send_email`.
5. **Créer une boîte** dans l'application déployée (par exemple `hello@example.com`).

## Développement local

```bash
npm install
npm run dev
# renseigner le domaine dans wrangler.jsonc
wrangler r2 bucket create agentic-inbox   # crée le bucket R2
npm run deploy
```

## Dépannage

|Message|Cause probable|
|---|---|
|`Invalid or expired Access token`|`POLICY_AUD` ou `TEAM_DOMAIN` erroné : réactiver Access pour obtenir de nouveau les valeurs, puis réinitialiser les secrets.|
|`Cloudflare Access must be configured in production`|Activer Access en un clic et définir les secrets `POLICY_AUD` et `TEAM_DOMAIN`.|

## Accès MCP

Le serveur MCP est exposé sur `/mcp` ; un client comme Claude Code ou Cursor peut agir sur une boîte en passant le paramètre `mailboxId`. **Il n'y a pas d'autorisation par boîte** : toute personne qui franchit la politique Cloudflare Access partagée atteint toutes les boîtes, y compris par MCP.

## Conseils d'utilisation

- **Réserver à une boîte dédiée ou à un petit groupe de confiance** ; ne pas remplacer Gmail ou Outlook sans revue de sécurité.
- **Garder la confirmation d'envoi** : l'agent rédige des brouillons, l'envoi reste manuel.
- **Restreindre la politique Access** au strict nécessaire, puisqu'elle est l'unique frontière de confiance.
- **Prévoir la dépendance à Cloudflare** : aucune portabilité sans réécriture significative.

## Sources

- [Agentic Inbox — dépôt officiel](https://github.com/cloudflare/agentic-inbox)
