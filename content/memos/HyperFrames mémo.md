---
title: "HyperFrames — Mémo"
type: memo
fiche: "[[HyperFrames]]"
date: 2026-09-25
---

# HyperFrames — Mémo

> Les commandes à connaître pour [[HyperFrames]], le framework open source de HeyGen qui transforme du HTML/CSS animé en vidéo MP4, pensé pour être piloté par Claude Code, Codex ou Cursor. L'agent écrit une page HTML ; HyperFrames la rend image par image dans Chrome puis l'encode avec FFmpeg.

## Installation

```bash
# Skills pour l'agent (choisir le groupe « Core Skills » dans le sélecteur)
GIT_LFS_SKIP_SMUDGE=1 npx skills add heygen-com/hyperframes

# Pour un agent ou un script non interactif : installe exactement le jeu de base
npx hyperframes skills update
```

`GIT_LFS_SKIP_SMUDGE=1` évite de télécharger ~240 Mo de vidéos de test inutiles. Prérequis : Node.js 22+ et FFmpeg.

## Démarrer avec l'agent

La skill `/hyperframes` est le point d'entrée : elle choisit le bon workflow. Exemple :

> Avec `/hyperframes`, crée une intro produit de 10 secondes : titre en fondu, vidéo en arrière-plan, musique discrète.

## Workflows de création

|Skill|Quand l'utiliser|
|---|---|
|`/product-launch-video`|Vidéo de lancement ou démo d'un **site web** (depuis son URL, un brief ou un script). Idéal entre 30 et 90 s.|
|`/faceless-explainer`|Expliquer un sujet à partir d'un texte, sans produit ni site : typographie, schémas, data-viz.|
|`/pr-to-video`|Transformer une **pull request GitHub** en vidéo (nouveauté, correctif, changelog).|
|`/embedded-captions`|Ajouter des sous-titres à une vidéo face caméra existante.|
|`/talking-head-recut`|Habiller une interview ou un podcast vidéo : bandeaux, chiffres, citations.|
|`/motion-graphics`|Animation courte sans voix (< 10 s) : logo, chiffre clé, titre animé.|
|`/music-to-video`|Vidéo synchronisée sur le rythme d'une musique.|
|`/slideshow`|Présentation navigable (pas une vidéo rendue).|
|`/general-video`|Tout le reste : formats longs, multi-scènes, bande-annonce.|
|`/remotion-to-hyperframes`|Migrer une composition [[Remotion]] vers HyperFrames.|

Skills spécialisées chargées à la demande : `/hyperframes-animation`, `/hyperframes-creative`, `/media-use` (musique, sons, voix, images), `/hyperframes-audio`, `/hyperframes-cli`, `/figma`…

## Commandes du CLI

|Commande|Ce qu'elle fait|
|---|---|
|`npx hyperframes init mon-video`|Crée un projet.|
|`npx hyperframes preview`|Aperçu dans le navigateur avec rechargement à chaud.|
|`npx hyperframes lint` / `check`|Vérifie que la composition est valide.|
|`npx hyperframes snapshot`|Capture des images clés pour contrôle.|
|`npx hyperframes render`|Rend la vidéo en MP4.|
|`npx hyperframes add data-chart`|Ajoute un bloc du catalogue (transitions, overlays, graphiques…).|
|`npx hyperframes catalog`|Parcourt le catalogue de blocs.|
|`npx hyperframes doctor`|Diagnostique l'installation (FFmpeg, Chrome…).|
|`npx hyperframes cloud render`|Rendu dans le cloud HeyGen (aussi `lambda deploy` / `lambda render` pour AWS).|

## Conseils d'utilisation

- **Toujours passer par `/hyperframes`** : il confirme le brief avant de lancer un workflow, ce qui évite de rendre une vidéo à côté du sujet.
- **Boucle courte** : `preview` pour itérer, `lint` avant chaque rendu, `render` seulement à la fin (c'est l'étape la plus lente).
- **Réutiliser le catalogue** (`hyperframes add`) avant de faire coder une transition ou un graphique à la main.
- **Utiliser `frame.md`** pour adapter ton design system (couleurs, typo) au format vidéo, et garder une identité cohérente.
- **Rendu déterministe** : même entrée, même vidéo. Pratique pour générer des vidéos en série (CI, variantes).
- **Mettre à jour les skills** avec `npx hyperframes skills update` : le registre `skills add` peut avoir quelques heures de retard.

## Sources

- [README HyperFrames](https://github.com/heygen-com/hyperframes)
- [Documentation HyperFrames](https://hyperframes.heygen.com)
- [HeyGen HyperFrames Beginner Guide — Medium](https://new2026.medium.com/heygen-hyperframes-beginner-guide-how-to-use-claude-code-to-turn-html-css-and-gsap-into-video-cf6e14dc8064)
- [Claude Code + HyperFrames Hands-On — Apito](https://apito.ai/en/blog/dev-guides/claude-code-hyperframes-video-generation/)
