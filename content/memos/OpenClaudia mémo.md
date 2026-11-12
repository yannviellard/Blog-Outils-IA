---
title: "OpenClaudia — Mémo"
type: memo
fiche: "[[OpenClaudia]]"
date: 2026-09-25
---

# OpenClaudia — Mémo

> Les commandes à connaître pour [[OpenClaudia]], la boîte à outils marketing open source pour Claude Code et Codex : SEO, rédaction, e-mails, réseaux sociaux, publicité, analytics. Particularité : beaucoup de skills **agissent** (publier, envoyer, poster) via des API, au lieu de seulement proposer du texte.

## Installation

```bash
# Toutes les skills
npx openclaudia install --all

# Seulement certaines
npx openclaudia install seo-audit write-blog email-sequence

# Via le CLI skills
npx skills add OpenClaudia/openclaudia-skills --skill seo-audit
```

Les clés API sont optionnelles : sans elles, les skills fonctionnent avec moins de données. Chaque skill indique la clé dont elle a besoin quand on l'appelle.

## Exemples de commandes

|Commande|Ce qu'elle fait|
|---|---|
|`/seo-audit https://monsite.com`|Audit SEO technique et on-page, avec corrections.|
|`/write-blog "10 conseils de croissance SaaS"`|Article optimisé SEO, avec balises meta.|
|`/publish-article`|Contrôles avant publication : titre recherché, vrai auteur, image sous licence, sources liées.|
|`/email-sequence --type product-launch`|Séquence d'e-mails, **envoyée** via l'API Resend si configurée.|
|`/competitor-analysis concurrent.com`|Analyse SEO, contenu et positionnement d'un concurrent.|
|`/discord-bot "Nouvelle fonctionnalité !"`|Publie un message sur Discord.|

## Les skills par catégorie

|Catégorie|Skills principales|
|---|---|
|SEO|`seo-audit`, `keyword-research`, `serp-analyzer`, `backlink-audit`, `schema-markup`, `programmatic-seo`, `geo-query-finder` (visibilité dans les réponses de ChatGPT)|
|Rédaction|`write-blog`, `write-landing`, `copywriting`, `copy-editing`, `content-strategy`, `seo-content-brief`, `content-gap-analysis`, `content-repurposing`|
|E-mail|`email-sequence`, `email-subject-lines`|
|Réseaux sociaux|`social-content`, `thread-writer`, `content-calendar`, `linkedin-content`, `reddit-marketing`, `bluesky`|
|Publicité et conversion|`google-ads`, `facebook-ads`, `linkedin-ads`, `page-cro`, `ab-test-setup`|
|Analytics (API)|`google-analytics`, `search-console`, `semrush-research`, `youtube-analytics`, `similarweb-traffic`|
|Stratégie|`marketing-ideas`, `icp-builder`, `growth-strategy`, `pricing-strategy`, `launch-strategy`, `product-marketing`|
|Notifications|`slack-bot`, `discord-bot`, `telegram-bot`, `task-banner` (notification macOS quand Claude a fini)|

## Clés API courantes

|Variable|Pour|
|---|---|
|`SEMRUSH_API_KEY`|Recherche de mots-clés et veille concurrentielle|
|`RESEND_API_KEY`|Envoi des séquences d'e-mails|
|Google OAuth|GA4, Search Console, Google Ads|
|`DISCORD_WEBHOOK_URL`, `SLACK_WEBHOOK_URL`|Publication sur Discord et Slack|
|`OPENAI_API_KEY`, `UNSPLASH_CLIENT_ID`|Génération d'images, photos libres|

## Conseils d'utilisation

- **Attention aux skills qui publient ou envoient** : relire le contenu et demander explicitement une confirmation avant tout envoi réel (e-mail, post, message).
- **Clés en variables d'environnement**, jamais écrites dans un fichier de skill ou committées.
- **N'installer que les skills utiles** plutôt que les 78 : moins de contexte, moins de risque d'envoi involontaire.
- **Passer par `publish-article` avant publication** pour vérifier sources, auteur et droits sur les images.
- **Certaines skills s'appuient sur des API payantes** (SemRush, Enception…) : vérifier le coût avant de les utiliser à grande échelle.

## Sources

- [README OpenClaudia](https://github.com/openclaudia/openclaudia-skills)
- [Guide d'utilisation (USAGE.md)](https://github.com/OpenClaudia/openclaudia-skills/blob/main/USAGE.md)
- [Site openclaudia.com](https://openclaudia.com)
