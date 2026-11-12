---
title: "Supabase — Mémo"
type: memo
fiche: "[[Supabase]]"
date: 2026-10-11
---

# Supabase — Mémo

> Les commandes de la CLI [[Supabase]] pour développer en local, versionner le schéma par migrations, déployer des Edge Functions et générer des types.

## Installation

```bash
npm install supabase --save-dev     # par projet (Node.js 20+), puis npx supabase --help
brew install supabase/tap/supabase  # macOS ou Linux (Homebrew)
```

Windows : `scoop bucket add supabase https://github.com/supabase/scoop-bucket.git` puis `scoop install supabase`. La pile locale tourne dans des conteneurs : un moteur de conteneurs (Docker Desktop, OrbStack sur macOS, Podman, colima…) est requis.

## Pile locale

|Commande|Ce qu'elle fait|
|---|---|
|`supabase init`|Crée le dossier `supabase/` et `config.toml` (fichiers locaux uniquement).|
|`supabase start`|Démarre la pile locale (le premier lancement télécharge les images Docker).|
|`supabase status`|Affiche les URL et clés de la pile locale.|
|`supabase stop`|Arrête la pile sans réinitialiser la base locale.|
|`supabase stop --no-backup`|Arrête et supprime les changements de schéma et de données locaux : à sauvegarder avant.|

## Base de données et migrations

|Commande|Ce qu'elle fait|
|---|---|
|`supabase migration new <nom>`|Crée un fichier de migration vide.|
|`supabase migration up`|Applique les migrations en attente.|
|`supabase db diff`|Compare le schéma à une base fantôme pour produire un diff.|
|`supabase db reset`|Reconstruit la base locale à partir des migrations et des données de seed.|
|`supabase db pull`|Rapatrie les changements du schéma distant dans une nouvelle migration.|
|`supabase db push`|Pousse les migrations locales vers la base distante.|
|`supabase gen types`|Génère des types à partir du schéma.|

## Projet hébergé et fonctions

|Commande|Ce qu'elle fait|
|---|---|
|`supabase login`|Connecte la CLI avec un jeton d'accès personnel.|
|`supabase link`|Lie le dossier local à un projet hébergé.|
|`supabase functions new <nom>`|Crée une Edge Function avec du code de départ.|
|`supabase functions serve`|Sert les fonctions en local.|
|`supabase functions deploy`|Déploie une fonction vers le projet lié.|
|`supabase secrets set NOM=valeur`|Définit des secrets pour le projet lié.|

## Conseils d'utilisation

- **Travailler par migrations versionnées** plutôt que par modifications manuelles dans le tableau de bord.
- **Écrire et tester les politiques RLS en local** avant `db push` : une RLS mal configurée est le premier risque de sécurité.
- **Toujours passer par `db reset`** pour vérifier que les migrations et le seed reconstruisent bien la base.
- **Ne jamais exécuter `stop --no-backup` sans sauvegarde** de ce qui doit être conservé.
- **Surveiller les coûts** : egress et stockage dépendent du profil lecture/écriture.

## Sources

- [Supabase — référence de la CLI](https://supabase.com/docs/reference/cli/introduction)
- [Supabase — démarrer avec la CLI](https://supabase.com/docs/guides/local-development/cli/getting-started)
