---
title: "Higgsfield Skills — Mémo"
type: memo
fiche: "[[Higgsfield-skills]]"
date: 2026-09-25
---

# Higgsfield Skills — Mémo

> Les commandes à connaître pour [[Higgsfield-skills]], les skills officielles qui donnent à Claude Code, Codex ou Cursor accès à la plateforme [[Higgsfield-ai-platform|Higgsfield]] : génération d'images, de vidéos et d'audio (30+ modèles), personnage persistant, photos produit, identité de marque, sites web, miniatures YouTube.

## Installation

```bash
# Recommandé, tous agents (installe aussi le CLI Higgsfield et gère la connexion)
npx skills add higgsfield-ai/skills

# Claude Code
/plugin marketplace add higgsfield-ai/skills
/plugin install higgsfield@higgsfield
```

Un compte Higgsfield est nécessaire : chaque génération consomme des crédits, selon le modèle et la résolution.

## Les skills

|Commande|Ce qu'elle fait|
|---|---|
|`/higgsfield:generate`|Image, vidéo, 3D ou audio à partir d'un prompt. Inclut **Marketing Studio** (pubs de marque avec avatar, produit, accroche) et le **Virality Predictor** (note l'accroche et l'attention d'une vidéo terminée).|
|`/higgsfield:soul-id`|Entraîne un personnage fidèle à un visage, à partir de 5 à 20 photos. Renvoie un `reference_id` réutilisable.|
|`/higgsfield:product-photoshoot`|Photos produit de qualité marque, en 10 modes (voir ci-dessous).|
|`/higgsfield:brandkit`|Crée ou étend une identité visuelle : palettes, logos SVG éditables, typographie, maquettes, packaging, brandbook PPTX/PDF.|
|`/higgsfield:marketplace-cards`|Visuels produit pour marketplaces : image principale conforme, images secondaires, modules type A+.|
|`/higgsfield:youtube-thumbnail`|Miniatures YouTube et couvertures verticales (Shorts, Reels), avec variantes contrôlées.|
|`/higgsfield:video-explainer`|Vidéo explicative narrée (voix + visuels), assemblée en MP4.|
|`/higgsfield:websites`|Crée, modifie et déploie un site full-stack (React 19 + TanStack Start sur Cloudflare).|
|`/higgsfield:game-generation`|Jeu navigateur jouable, ou assets de jeu (sprites, textures, 3D, sons).|

## Modes utiles

|Skill|Modes|
|---|---|
|`product-photoshoot`|`product_shot` (fond neutre), `lifestyle_scene`, `closeup_product_with_person`, `moodboard_pin` (Pinterest), `hero_banner`, `social_carousel` (3–10 slides), `ad_creative_pack`, `virtual_model_tryout`, `conceptual_product`, `restyle`|
|Marketing Studio (`generate`)|`ugc` (par défaut), `ugc_how_to`, `ugc_unboxing`, `product_showcase`, `product_review`, `tv_spot`, `wild_card`, `ugc_virtual_try_on`, `virtual_try_on`|

## Enchaînements types

|Besoin|Enchaînement|
|---|---|
|Des visuels avec ton propre visage|`/higgsfield:soul-id` (une fois) → `/higgsfield:generate` avec l'identifiant obtenu (`--soul-id`)|
|Animer une image|`/higgsfield:generate` avec `--start-image` (Seedance 2.0 par défaut, Kling 3.0 moins cher)|
|Identité de marque complète|`/higgsfield:brandkit`, puis `product-photoshoot` et `marketplace-cards` avec la charte obtenue|
|Site avec visuels sur mesure|`/higgsfield:websites` + `/higgsfield:generate` pour les images et vidéos d'en-tête|
|Vidéo → miniature|`/higgsfield:youtube-thumbnail` une fois le sujet et la direction visuelle fixés|

## Conseils d'utilisation

- **Surveiller les crédits** : les modèles vidéo et la 4K coûtent nettement plus. Demander d'abord une image basse résolution pour valider la direction.
- **Choisir le modèle moins cher en repli** : Kling 3.0 plutôt que Seedance pour animer une image quand la qualité maximale n'est pas nécessaire.
- **Soul ID** : fournir 5 à 20 photos variées (angles, lumières) du même visage, et seulement avec l'accord de la personne.
- **Brandkit valide chaque étape** : relire palette et logo avant de lancer les déclinaisons, qui en dépendent.
- **Virality Predictor** : utile pour comparer deux montages avant publication, pas comme vérité absolue.

## Sources

- [README Higgsfield Skills](https://github.com/higgsfield-ai/skills)
- [Guide d'installation](https://github.com/higgsfield-ai/skills/blob/main/INSTALL.md)
- [Higgsfield Skills — site officiel](https://higgsfield.ai/skills)
- [Accéder à Higgsfield via CLI et skills — Help Center](https://higgsfield.ai/creator-hub/help-center/integrations/how-do-i-access-higgsfield-via-cli)
