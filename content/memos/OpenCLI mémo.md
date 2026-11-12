---
title: "OpenCLI — Mémo"
type: memo
fiche: "[[OpenCLI]]"
date: 2026-09-25
---

# OpenCLI — Mémo

> Les commandes à connaître pour [[OpenCLI]], le CLI qui transforme des sites web en commandes en réutilisant ta session Chrome connectée, et qui permet à Claude Code ou Codex de piloter ton navigateur. Voir aussi [[OpenCLI#Avis indépendants|les avis sur OpenCLI]].

## Installation

```bash
npm install -g @jackwener/opencli   # Node.js ≥ 20.18.1 (ou l'app OpenCLIApp sur macOS/Windows)
# Puis installer l'extension « OpenCLI » depuis le Chrome Web Store
opencli doctor                      # vérifie la connexion au navigateur

# Skills pour Claude Code, Codex, Cursor…
npx skills add jackwener/opencli
```

## Commandes de base

|Commande|Ce qu'elle fait|
|---|---|
|`opencli list`|Liste toutes les commandes disponibles.|
|`opencli <site> <commande>`|Lance un adaptateur, ex. `opencli hackernews top --limit 5`, `opencli reddit hot`.|
|`opencli <site> <commande> -f json`|Sortie en JSON (aussi `yaml`, `md`, `csv`, `table` par défaut).|
|`opencli doctor`|Diagnostique l'extension et le démon local.|
|`opencli profile list` / `profile use work`|Gère plusieurs profils Chrome.|
|`opencli <commande> -v`|Mode verbeux, pour déboguer.|

## Exemples d'adaptateurs

|Commande|Résultat|
|---|---|
|`opencli twitter trending`|Tendances X/Twitter.|
|`opencli bilibili hot --limit 5`|Vidéos populaires Bilibili.|
|`opencli linkedin search …`|Recherche LinkedIn.|
|`opencli gemini deep-research …`|Lance une recherche Gemini Deep Research.|
|`opencli notebooklm source-list`|Sources d'un notebook NotebookLM.|
|`opencli twitter download <compte> --output ./dossier`|Télécharge les médias (yt-dlp requis pour les vidéos Bilibili).|

## Skills pour agents

|Skill|Quand l'utiliser|
|---|---|
|`opencli-usage`|« Quelles commandes OpenCLI existent pour Twitter ? »|
|`opencli-browser`|Piloter Chrome librement : naviguer, remplir un formulaire, extraire des données.|
|`opencli-adapter-author`|Écrire un adaptateur réutilisable pour un nouveau site.|
|`opencli-autofix`|Réparer un adaptateur cassé (« `opencli zhihu hot` renvoie vide, corrige-le »).|
|`opencli-browser-sitemap` / `opencli-sitemap-author`|Utiliser ou enregistrer la carte des parcours d'un site.|

## Pilotage du navigateur (utilisé par les agents)

|Commande|Ce qu'elle fait|
|---|---|
|`opencli browser <session> open <url>`|Ouvre une page dans une session nommée.|
|`opencli browser <session> state`|Snapshot DOM structuré de la page.|
|`opencli browser <session> click` / `fill` / `select` / `keys`|Interactions.|
|`opencli browser <session> extract`|Extrait des données.|
|`opencli browser <session> network`|Intercepte les réponses API.|
|`opencli browser <session> tab list` / `tab new` / `tab select`|Gère les onglets.|
|`opencli browser <session> close`|Libère la session.|

## Étendre

|Commande|Ce qu'elle fait|
|---|---|
|`opencli plugin install github:user/repo`|Installe un adaptateur communautaire.|
|`opencli external register <nom>`|Expose un CLI local (gh, docker…) via OpenCLI.|
|`opencli adapter eject <site>` / `adapter reset <site>`|Modifie localement un adaptateur officiel, puis revient à l'original.|

## Codes de sortie (pour les scripts)

`0` succès · `66` résultat vide · `69` extension déconnectée · `75` délai dépassé · `77` authentification requise · `78` erreur de configuration.

## Conseils d'utilisation

- **Utiliser un profil Chrome dédié**, sans connexion à ta banque ni à ta messagerie principale : l'agent agit avec toutes les sessions ouvertes du profil.
- **Rester en lecture seule sur les plateformes sensibles** : des comptes Xiaohongshu ont été bannis après des actions d'écriture automatisées.
- **Espacer les requêtes** sur un même site : les rafales déclenchent les protections anti-automatisation, et les commandes renvoient alors un résultat vide sans erreur.
- **Résultat vide ou « Unauthorized »** : la session a probablement expiré. Se reconnecter au site dans Chrome.
- **Préférer un adaptateur à `opencli-browser`** pour une tâche répétée : l'adaptateur ne consomme aucun token à l'exécution.

## Sources

- [README OpenCLI](https://github.com/jackwener/opencli)
- [Site officiel](https://opencli.info/)
- [Issue #677 — compte Xiaohongshu banni](https://github.com/jackwener/opencli/issues/677)
- [Issue #2470 — rythme des requêtes Xiaohongshu](https://github.com/jackwener/opencli/issues/2470)
