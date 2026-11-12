---
title: "Superset — Mémo"
type: memo
fiche: "[[Superset]]"
date: 2026-10-10
---

# Superset — Mémo

> Démarrage, commandes et garde-fous pour [[Superset]]. Voir aussi [[Superset#Avis indépendants|les avis sur Superset]]. La CLI est encore annoncée en bêta : vérifier `superset --help` après une mise à jour.

## Installation

```bash
# CLI autonome : macOS ou Linux
curl -fsSL https://superset.sh/cli/install.sh | sh

# Alternative Homebrew
brew install superset-sh/tap/superset

# Vérifier
superset --version
superset --help
```

L'application de bureau inclut aussi la CLI dans `~/.superset/bin`. Ajouter ce dossier au `PATH` pour l'utiliser depuis un terminal externe.

## Cycle minimal

```bash
# Enregistrer un dépôt local
superset projects create --name "mon-app" --local --import /chemin/mon-app

# Lister projets et workspaces
superset projects list
superset workspaces list --local

# Créer un worktree isolé
superset workspaces create \
  --project PROJECT_ID \
  --name "fix-login" \
  --branch fix/login \
  --local

# Créer et démarrer directement un agent
superset workspaces create \
  --project PROJECT_ID \
  --name "fix-login" \
  --branch fix/login \
  --local \
  --agent codex \
  --prompt "Corrige le bug et lance les tests ciblés"

# Session temporaire sans projet existant
superset workspaces create --session --local --agent claude --prompt "Explore cette idée"
```

## Configuration d'un projet

Créer `.superset/config.json` :

```json
{
  "setup": [
    "bun install",
    "cp \"$SUPERSET_ROOT_PATH/.env\" .env"
  ],
  "teardown": ["docker compose down"],
  "run": ["./.superset/run.sh"]
}
```

|Étape|Conseil|
|---|---|
|`setup`|Installer ou lier les dépendances et préparer les fichiers ignorés.|
|`run`|Attribuer un port distinct à chaque workspace.|
|`teardown`|Arrêter conteneurs, watchers et ressources temporaires.|
|Secrets|Ne jamais les committer ; les copier depuis le checkout racine ou un gestionnaire.|

## Commandes pratiques

```bash
superset workspaces list --json
superset workspaces list --quiet
superset tasks list --status in_progress --json
superset automations list
superset automations run AUTOMATION_ID
superset automations logs AUTOMATION_ID
superset config check
```

`--json` convient aux scripts et `--quiet` renvoie seulement les identifiants lorsque cela est possible.

## Choisir le bon mode

|Situation|Mode conseillé|
|---|---|
|Deux fonctionnalités indépendantes|Deux worktrees et deux branches.|
|Implémentation puis revue du même diff|Même workspace, sessions distinctes.|
|Exploration jetable|Session sans projet.|
|Petite correction dans le checkout courant|`--checkout local`, avec prudence.|
|Agents modifiant les mêmes fichiers|Séquentiel, ou branches puis fusion explicite.|

## Routine de livraison

1. Lire le diff et les fichiers non suivis.
2. Exécuter tests, lint et build dans le workspace.
3. Envoyer les commentaires de revue à un agent distinct.
4. Commit et push seulement après validation.
5. Créer la PR, vérifier la CI, puis fusionner.
6. Archiver le workspace et exécuter le teardown.

## Sources

- [Premiers pas avec la CLI](https://docs.superset.sh/cli/getting-started)
- [Référence CLI](https://docs.superset.sh/cli/cli-reference)
- [Scripts de cycle de vie](https://docs.superset.sh/setup-teardown-scripts)
