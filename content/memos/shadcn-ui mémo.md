---
title: "shadcn/ui — Mémo"
type: memo
fiche: "[[shadcn-ui]]"
date: 2026-10-11
---

# shadcn/ui — Mémo

> La CLI de [[shadcn-ui]] copie le code des composants dans votre projet et le tient à jour : les commandes à connaître pour initialiser, ajouter, comparer et migrer.

## Commandes principales

|Commande|Ce qu'elle fait|
|---|---|
|`npx shadcn@latest init`|Initialise le projet et installe les dépendances (`-t`/`--template`, `-p`/`--preset`, `-d`/`--defaults`, `-f`/`--force`, `--monorepo`).|
|`npx shadcn@latest add <composant>`|Ajoute un composant (`-o`/`--overwrite`, `-a`/`--all`, `-p`/`--path`).|
|`npx shadcn@latest add <composant> --dry-run`|Simule l'ajout sans écrire de fichier.|
|`npx shadcn@latest add <composant> --diff [chemin]`|Affiche les différences avec la version amont avant de fusionner.|
|`npx shadcn@latest search` (alias `list`)|Cherche dans les registres (`-q`/`--query`, `-l`/`--limit`).|
|`npx shadcn@latest view <élément>`|Affiche un élément du registre.|
|`npx shadcn@latest docs <composant>`|Récupère la documentation et les références d'API (`--json`).|
|`npx shadcn@latest info`|Informations sur votre projet (`--json`).|
|`npx shadcn@latest apply --preset <code>`|Applique un preset à un projet existant (`--only` pour une partie).|
|`npx shadcn@latest preset decode\|resolve\|url\|open`|Décode, résout, donne l'URL ou ouvre un code de preset.|
|`npx shadcn@latest build`|Construit les composants d'un registre shadcn (`-o`/`--output`).|
|`npx shadcn@latest migrate`|Lance une migration : `cn`, `icons`, `base-color`, `rtl`, `radix` (`-l`/`--list`).|
|`npx shadcn@latest eject`|Intègre `shadcn/tailwind.css` et retire la dépendance shadcn.|

Options communes : `-y`/`--yes` (sans confirmation), `-c`/`--cwd` (autre dossier), `-s`/`--silent`.

## Mise à jour sans écrasement

1. `npx shadcn@latest add <composant> --dry-run` : vérifier ce qui changerait.
2. `npx shadcn@latest add <composant> --diff` : lire les différences avec vos modifications locales.
3. Fusionner à la main, puis relancer sans `--overwrite` pour ne rien écraser.

## Conseils d'utilisation

- **Les composants vous appartiennent** : aucune mise à jour automatique ; planifier la revue des correctifs amont.
- **Passer par la CLI plutôt que recopier le code** d'un composant à la main, surtout avec un agent.
- **Utiliser `info` et `docs`** pour donner à un agent de code le contexte réel du projet.
- **Documenter les écarts locaux** : après modification, `--diff` devient la seule façon fiable de suivre l'amont.
- **Prévoir un thème propre** : le style neutre par défaut contribue à l'uniformité des interfaces.

## Sources

- [shadcn/ui — CLI](https://ui.shadcn.com/docs/cli)
