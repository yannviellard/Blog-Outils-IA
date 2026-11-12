---
title: "Parallel Code — Mémo"
type: memo
fiche: "[[Parallel Code]]"
date: 2026-10-10
---

# Parallel Code — Mémo

> Démarrage et raccourcis pour [[Parallel Code]]. Voir aussi [[Parallel Code#Avis indépendants|les avis sur Parallel Code]].

## Installation

1. Télécharger le `.dmg` macOS, l'AppImage ou le `.deb` Linux depuis les [releases](https://github.com/johannesjo/parallel-code/releases).
2. Installer au moins un agent : Codex, Claude Code, Gemini, Copilot CLI ou agent personnalisé.
3. Ouvrir un dépôt Git.
4. Créer une première petite tâche et vérifier le diff avant fusion.

Depuis les sources :

```bash
git clone https://github.com/johannesjo/parallel-code.git
cd parallel-code
npm install
npm run dev
```

## Cycle d'une tâche

1. `Ctrl/Cmd+N` : nouvelle tâche.
2. Choisir l'agent et écrire un prompt avec critères d'acceptation.
3. L'application crée branche + worktree puis lance la CLI.
4. Suivre l'état et répondre aux demandes de permission.
5. Examiner Changed Files et le diff.
6. Lancer tests et contrôles dans le terminal de la tâche.
7. Fusionner avec `Ctrl/Cmd+Shift+M` ou ouvrir une PR.

## Raccourcis

|Raccourci|Action|
|---|---|
|`Ctrl/Cmd+N`|Nouvelle tâche.|
|`Ctrl/Cmd+Enter`|Envoyer le prompt.|
|`Ctrl/Cmd+Shift+M`|Fusionner dans la branche principale.|
|`Ctrl/Cmd+Shift+P`|Push vers le remote.|
|`Ctrl/Cmd+Shift+T`|Nouveau terminal dans la tâche.|
|`Ctrl/Cmd+Shift+D`|Terminal autonome.|
|`Ctrl/Cmd+B`|Afficher/masquer la barre latérale.|
|`Ctrl/Cmd+Shift+F`|Mode focus.|
|`Alt+flèches`|Changer de panneau.|
|`Ctrl/Cmd+/` ou `F1`|Afficher tous les raccourcis.|

## Quand utiliser Arena

- Décision d'architecture réellement réversible.
- Comparaison Codex/Claude/Gemini sur une même spécification.
- Correctif difficile avec tests objectifs.
- Jamais uniquement pour « produire plus » sans critère de sélection.

Comparer sur : tests, taille du diff, complexité, risques, temps et coût. Ne pas fusionner les deux résultats automatiquement.

## Isolation Docker

Ajouter un `.parallel-code/Dockerfile` spécifique au projet lorsque l'agent ne doit pas s'exécuter directement sur l'hôte.

Avant lancement :

- Inspecter les variables exportées dans le shell.
- Retirer `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GH_TOKEN`, AWS et autres secrets inutiles.
- Ne monter que les chemins requis.
- Rappeler que le réseau et les identifiants ne sont pas isolés par un simple worktree.

## Checklist de fusion

- La branche part de la bonne base.
- Aucun fichier ignoré ou secret n'a été ajouté.
- Tests et lint ont été lancés dans le worktree.
- Le diff respecte exactement le périmètre demandé.
- Les migrations et changements d'API ont été revus séparément.
- Les tâches concurrentes ne modifient pas les mêmes contrats.

## Sources

- [README et raccourcis](https://github.com/johannesjo/parallel-code)
- [Releases](https://github.com/johannesjo/parallel-code/releases)
- [Confidentialité et isolation](https://github.com/johannesjo/parallel-code/blob/main/PRIVACY.md)
