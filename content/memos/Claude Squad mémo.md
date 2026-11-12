---
title: "Claude Squad — Mémo"
type: memo
fiche: "[[Claude Squad]]"
date: 2026-10-10
---

# Claude Squad — Mémo

> Installation, profils et raccourcis de [[Claude Squad]]. Voir aussi [[Claude Squad#Avis indépendants|les avis sur Claude Squad]].

## Prérequis et installation

```bash
# Prérequis macOS
brew install tmux gh
gh auth status

# Installer Claude Squad
brew install claude-squad
ln -s "$(brew --prefix)/bin/claude-squad" "$(brew --prefix)/bin/cs"

# Alternative officielle
curl -fsSL https://raw.githubusercontent.com/smtg-ai/claude-squad/main/install.sh | bash

# Diagnostic
cs debug
cs version
```

## Lancer

```bash
# Agent par défaut : claude
cs

# Codex
cs -p "codex"

# Gemini ou Aider
cs -p "gemini"
cs -p "aider --model ollama_chat/gemma3:1b"

# Auto-accept expérimental — VM/conteneur jetable uniquement
cs -y
```

## Raccourcis TUI

|Touche|Action|
|---|---|
|`n`|Nouvelle session.|
|`N`|Nouvelle session avec prompt.|
|`D`|Supprimer la session sélectionnée.|
|`↑`/`j`, `↓`/`k`|Naviguer entre les sessions.|
|`Entrée` ou `o`|Attacher la session.|
|`Ctrl+Q`|Se détacher et revenir à la liste.|
|`Tab`|Basculer aperçu terminal / diff.|
|`s`|Commit et push de la branche.|
|`c`|Checkout : commit puis pause.|
|`r`|Reprendre une session en pause.|
|`?`|Aide.|
|`q`|Quitter l'interface.|

## Profils

Le fichier se trouve généralement dans `~/.claude-squad/config.json` ; confirmer avec `cs debug`.

```json
{
  "default_program": "claude",
  "profiles": [
    { "name": "claude", "program": "claude" },
    { "name": "codex", "program": "codex" },
    { "name": "gemini", "program": "gemini" },
    { "name": "opencode", "program": "opencode" }
  ]
}
```

Utiliser `←` et `→` dans l'écran de création pour changer de profil.

## Préparer le dépôt

- Partir d'un `git status` propre ou comprendre exactement les changements présents.
- Installer les CLI d'agents et vérifier leur authentification avant de lancer `cs`.
- Prévoir un script de préparation des worktrees pour `.env`, dépendances et ports.
- Définir une tâche livrable et non chevauchante par session.

## Routine sûre

1. Créer la session avec un prompt contenant fichiers, critères et tests.
2. Vérifier le diff avec `Tab` avant toute opération Git.
3. Se rattacher avec `o` pour demander corrections et résumé.
4. Lancer manuellement les tests critiques.
5. Utiliser `s` seulement après revue.
6. Supprimer les sessions fusionnées et exécuter `git worktree prune` si nécessaire.

## Dépannage

|Problème|Action|
|---|---|
|Session tmux en timeout|Mettre à jour la CLI d'agent.|
|Variables absentes|Relancer tmux après export ou utiliser un script de setup.|
|Prompt envoyé trop tôt|Attendre le démarrage complet de la CLI avant l'injection.|
|État Git confus|`git worktree list`, `git branch -vv`, puis inspection manuelle.|
|Windows|Préférer WSL2 ou une machine Unix ; le support natif reste fragile.|

## Sources

- [README officiel](https://github.com/smtg-ai/claude-squad)
- [Issues](https://github.com/smtg-ai/claude-squad/issues)
