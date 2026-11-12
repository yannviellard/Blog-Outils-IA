---
title: "Hermes Agent — Mémo"
type: memo
fiche: "[[Hermes Agent]]"
date: 2026-10-11
---

# Hermes Agent — Mémo

> Les commandes de [[Hermes Agent]] à connaître : installation, configuration du modèle, passerelle de messagerie, tâches planifiées et contrôle de la mémoire.

## Installation et premier lancement

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash   # Linux, macOS, WSL2
source ~/.zshrc                      # ou ~/.bashrc

hermes setup                         # assistant de configuration complet
hermes model                         # choisir fournisseur et modèle
hermes --tui                         # interface moderne (recommandée) ; `hermes` : CLI classique
hermes --continue                    # reprendre la session
```

Windows (PowerShell) : `iex (irm https://hermes-agent.nousresearch.com/install.ps1)`.

## Commandes du terminal

|Commande|Ce qu'elle fait|
|---|---|
|`hermes chat`|Démarre une conversation interactive ou ponctuelle.|
|`hermes gateway setup` / `hermes gateway` / `hermes gateway status`|Configure, démarre et vérifie la passerelle de messagerie.|
|`hermes cron`|Inspecte et gère les tâches planifiées.|
|`hermes pause` / `hermes resume`|Arrête / relance globalement les tâches planifiées, kanban et passerelle.|
|`hermes profile`|Gère des profils (instances isolées).|
|`hermes skills`|Parcourt, installe, publie et audite les skills.|
|`hermes memory`|Configure un fournisseur de mémoire externe.|
|`hermes mcp`|Gère les serveurs MCP, ou lance Hermes comme serveur MCP.|
|`hermes sessions`|Parcourt, exporte, supprime les sessions.|
|`hermes status` / `hermes usage` / `hermes insights`|État de l'agent / limites du compte / coûts et activité.|
|`hermes doctor`|Diagnostique la configuration et les dépendances.|
|`hermes security audit`|Audit de vulnérabilités de la chaîne d'approvisionnement.|
|`hermes backup` / `hermes import`|Sauvegarde le dossier Hermes en archive / la restaure.|
|`hermes update`|Met à jour Hermes et réinstalle les dépendances.|
|`hermes claw`|Aides à la migration depuis OpenClaw.|

## Commandes dans une session

|Commande|Ce qu'elle fait|
|---|---|
|`/new` (alias `/reset`)|Nouvelle session ; à utiliser aux changements naturels de tâche pour garder la mémoire propre.|
|`/model`|Affiche ou change le modèle et le fournisseur.|
|`/memory`|Examine et approuve ou rejette les écritures de mémoire en attente.|
|`/learn`|Distille une skill réutilisable à partir d'une source décrite.|
|`/skills`|Recherche, installe et gère les skills.|
|`/refine`|Lance maintenant la revue d'auto-amélioration (mémoire et skills).|
|`/compress`|Compresse le contexte.|
|`/context`|Répartition de l'usage de la fenêtre de contexte.|
|`/goal`, `/plan`, `/loop`|Objectif durable, plan Markdown sans exécution, relance périodique d'un prompt.|
|`/rollback`, `/diff`|Restaure des points de contrôle de fichiers, montre les changements Git.|
|`/approvals`, `/yolo`|Mode d'approbation des commandes dangereuses ; `/yolo` les désactive.|
|`/usage`, `/insights`|Tokens, coût et limites ; analytique des 30 derniers jours.|

## Conseils d'utilisation

- **Commencer par un profil, une tâche étroite et des permissions minimales**, puis élargir quand le workflow est fiable.
- **Vérifier ce qui est réellement mémorisé** (`MEMORY.md`, `USER.md`, `/memory`) : la confirmation textuelle du modèle ne prouve pas une écriture.
- **Maîtriser les coûts** : la revue d'arrière-plan peut être désactivée, plafonnée ou confiée à un modèle moins cher.
- **Isoler l'agent** : Docker ou autre sandbox, compte non-root, et éviter `/yolo` hors environnement jetable.
- **Créer de nouvelles sessions régulièrement** plutôt que de laisser un fil de messagerie grossir.
- **Contrôler les fournisseurs appelés** après une mise à jour (`hermes doctor`, journaux réseau).

## Sources

- [Hermes Agent — démarrage rapide](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Hermes Agent — commandes du terminal](https://hermes-agent.nousresearch.com/docs/reference/cli-commands)
- [Hermes Agent — commandes slash](https://hermes-agent.nousresearch.com/docs/reference/slash-commands)
