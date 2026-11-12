---
title: "Remotion — Mémo"
type: memo
fiche: "[[Remotion]]"
date: 2026-10-11
---

# Remotion — Mémo

> Les commandes de [[Remotion]] pour créer un projet vidéo en React, le prévisualiser dans le Studio et le rendre en MP4 ou en image fixe.

## Démarrer

```bash
npx create-video@latest      # crée un nouveau projet (Node.js requis)
npx remotion studio          # lance le Studio (alias : npx remotion preview)
```

Dans le Studio, la touche `s` rouvre l'interface dans le navigateur.

## Commandes principales

|Commande|Ce qu'elle fait|
|---|---|
|`npx remotion studio [entrée]`|Lance le Studio : aperçu, timeline, édition des propriétés.|
|`npx remotion compositions [entrée]`|Affiche les identifiants de compositions (`--quiet` : seulement les identifiants).|
|`npx remotion render <composition-id> <sortie>`|Rend une vidéo (ou une séquence d'images, ou un GIF).|
|`npx remotion still <composition-id> <sortie>`|Rend une image fixe (sans `composition-id`, une sélection est proposée ; sans sortie, le fichier va dans `out/`).|

## Options de `render` à retenir

|Option|Effet|
|---|---|
|`--props`|Passe des propriétés d'entrée (sous Windows, utiliser un fichier plutôt que du JSON en ligne).|
|`--codec`|Codec de sortie : h264 (défaut), h265, av1, prores, mp3…|
|`--crf`|Qualité à débit variable ; incompatible avec `--video-bitrate`.|
|`--scale`|Multiplie la taille de sortie (de 0 à 16, défaut 1).|
|`--frames`|Rend une plage d'images ou une sélection (ex. `--frames=0,30,90 --image-format=png`).|
|`--muted`|Désactive l'audio.|
|`--overwrite`|Autorise l'écrasement d'un fichier existant (actif par défaut ; `--overwrite=false` pour l'éviter).|
|`--log`|Verbosité : error, warn, info (défaut), verbose.|
|`--every-nth-frame`|Ne rend qu'une image sur n (GIF uniquement).|

Options utiles du Studio : `--port`, `--props`, `--no-open`, `--public-dir`, `--browser`.

## Conseils d'utilisation

- **Penser « code = source de vérité »** : versionner les compositions et les paramètres plutôt que les rendus.
- **Paramétrer par `--props`** pour produire des variantes en lot à partir de données.
- **Vérifier la licence** avant un usage commercial important : elle distingue les particuliers et petites organisations des entreprises au-delà de certains critères.
- **Prévoir l'infrastructure de rendu** (Lambda, Cloud Run) si le volume est important : le coût de rendu est à budgéter.
- **Pas de générateur IA** : Remotion compose une vidéo reproductible ; pour des plans générés, voir [[Higgsfield-ai-platform]]. Alternative HTML/CSS : [[HyperFrames]].

## Sources

- [Remotion — dépôt officiel](https://github.com/remotion-dev/remotion)
- [Remotion — `render`](https://www.remotion.dev/docs/cli/render)
- [Remotion — `still`](https://www.remotion.dev/docs/cli/still)
- [Remotion — `studio`](https://www.remotion.dev/docs/cli/studio)
- [Remotion — `compositions`](https://www.remotion.dev/docs/cli/compositions)
