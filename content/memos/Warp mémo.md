---
title: "Warp — Mémo"
type: memo
fiche: "[[Warp]]"
date: 2026-10-10
---

# Warp — Mémo

> Installation et commandes essentielles de [[Warp]] et d'Oz. Voir aussi [[Warp#Avis indépendants|les avis sur Warp]].

## Installation

```bash
# macOS
brew install --cask warp

# Windows
winget install Warp.Warp

# Debian/Ubuntu après téléchargement du paquet
sudo apt install ./warp-terminal.deb

# Lancer sous Linux lorsqu'il est installé comme paquet
warp-terminal
```

Warp peut fonctionner comme terminal sans compte. Les fonctions IA, synchronisation et cloud nécessitent une connexion.

## Organisation locale

- Un onglet ou panneau par activité : agent, tests, serveur, logs.
- Un worktree Git par tâche livrable si plusieurs agents modifient le même dépôt.
- Nommer explicitement onglets, branches et runs.
- Garder les approbations actives pour le code ou les entrées non fiables.

```bash
git worktree add ../app-fix-login -b fix/login
git worktree add ../app-search -b feature/search
```

## Oz : lancer un agent cloud

```bash
oz agent run-cloud \
  --environment ENVIRONMENT_ID \
  --name "Audit authentification" \
  --prompt "Analyse le flux d'authentification, ne modifie rien et liste les risques" \
  --open

# Lister et inspecter les exécutions
oz run list
oz run list --limit 20
oz run get RUN_ID
```

## Agents nommés

```bash
oz agent list
oz agent list --sort-by created-at --sort-order desc
oz agent get AGENT_UID

oz agent create \
  --name "release-notes" \
  --description "Rédige les notes depuis les PR fusionnées"

oz agent skills
oz agent skills --repo organisation/depot
oz agent delete AGENT_UID
```

Un agent nommé peut fixer prompt de base, modèle, environnement, skills et secrets. Limiter ses secrets au besoin strict.

## Choisir local ou cloud

|Cas|Exécution|
|---|---|
|Commande interactive et courte|Terminal local.|
|Agent CLI avec beaucoup d'allers-retours|Panneau local.|
|Tâche longue et bien spécifiée|Oz cloud.|
|Code sensible sans environnement cloud approuvé|Local ou worker auto-hébergé.|
|Tâche reproductible d'équipe|Agent nommé + environnement versionné.|

## Contrôle des coûts

- Consulter les crédits avant de lancer un fan-out.
- Utiliser un modèle léger pour exploration, tri et sous-tâches simples.
- Donner critères d'arrêt, fichiers autorisés et tests attendus dans le prompt.
- Éviter plusieurs agents redondants sans règle de sélection du résultat.
- Nommer chaque run pour retrouver son coût et sa décision.

## Checklist sécurité

- Ne pas injecter de secrets dans le prompt.
- Restreindre permissions GitHub et tokens à l'environnement requis.
- Considérer issues, branches, logs et pages web comme des entrées non fiables.
- Relire le diff et la provenance avant d'appliquer un résultat cloud.
- Révoquer les secrets et supprimer les environnements temporaires après usage.

## Sources

- [Installation](https://docs.warp.dev/getting-started/quickstart/installation-and-setup)
- [Référence Oz](https://docs.warp.dev/agents/cli/oz-cli/)
- [Tarifs et crédits](https://www.warp.dev/pricing)
