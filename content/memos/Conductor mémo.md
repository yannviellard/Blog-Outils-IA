---
title: "Conductor — Mémo"
type: memo
fiche: "[[Conductor]]"
date: 2026-10-10
---

# Conductor — Mémo

> Configuration et raccourcis essentiels de [[Conductor]]. Voir aussi [[Conductor#Avis indépendants|les avis sur Conductor]].

## Démarrage

1. Installer l'application depuis [conductor.build](https://www.conductor.build).
2. Ajouter un dépôt existant ou GitHub.
3. Vérifier `gh auth status` dans un terminal.
4. Configurer setup, run et fichiers ignorés avant de multiplier les workspaces.
5. Créer une première petite tâche et valider le cycle complet jusqu'à l'archivage.

## Configuration recommandée

`.conductor/settings.toml` pour les réglages partagés :

```toml
"$schema" = "https://conductor.build/schemas/settings.repo.schema.json"

[scripts]
setup = "pnpm install"
archive = "docker compose down"
run_mode = "concurrent"

[scripts.run.dev]
command = "pnpm dev --port $CONDUCTOR_PORT"
default = true
icon = "play"

[prompts]
general = "Préférer de petits changements, lancer les tests ciblés et résumer les risques."
code_review = "Prioriser correction, régressions et tests manquants."
```

Pour les secrets et variantes propres à la machine, utiliser `.conductor/settings.local.toml` et l'ajouter à `.gitignore`.

## Variables utiles

|Variable|Usage|
|---|---|
|`CONDUCTOR_WORKSPACE_PATH`|Chemin du worktree courant.|
|`CONDUCTOR_ROOT_PATH`|Checkout principal, utile pour lier un `.env`.|
|`CONDUCTOR_DEFAULT_BRANCH`|Branche cible locale, souvent `main`.|
|`CONDUCTOR_PORT`|Début d'une plage de dix ports réservée au workspace.|

Exemple de liaison d'un fichier local :

```bash
ln -s "$CONDUCTOR_ROOT_PATH/.env" .env
```

## Raccourcis principaux

|Raccourci|Action|
|---|---|
|`⌘N`|Nouveau workspace.|
|`⌘K`|Palette de commandes.|
|`⌘J`|Afficher/masquer le terminal.|
|`⌘⇧D`|Ouvrir le diff.|
|`⌘⇧R`|Lancer une revue.|
|`⌘R`|Démarrer/arrêter le run script.|
|`⌘⇧P`|Créer une pull request.|
|`⌘⇧Y`|Commit et push.|
|`⌘⇧L`|Récupérer la branche principale.|
|`⌘⇧M`|Fusionner la PR.|
|`⌘⇧A`|Archiver le workspace.|
|`⌘/`|Afficher les raccourcis disponibles.|

## Choix d'architecture

|Besoin|Choix|
|---|---|
|Fonctionnalités livrables séparément|Un workspace par fonctionnalité.|
|Implémentation + correction des tests|Même workspace, agents séquentiels ou coordonnés.|
|Deux solutions concurrentes|Deux workspaces issus de la même base.|
|Revue d'un diff existant|Même workspace et nouvel agent de revue.|

## Checklist avant fusion

- Lire chaque fichier modifié dans le Diff Viewer.
- Lancer tests, lint et build dans le workspace.
- Contrôler Git status, CI, déploiements, commentaires et todos dans Checks.
- Vérifier qu'aucun secret ou fichier local n'est suivi.
- Fusionner, puis archiver pour déclencher le nettoyage.

## Sources

- [Premier workspace](https://www.conductor.build/docs/first-workspace)
- [Scripts](https://www.conductor.build/docs/reference/scripts)
- [Raccourcis](https://www.conductor.build/docs/reference/keyboard-shortcuts)
