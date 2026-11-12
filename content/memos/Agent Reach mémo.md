---
title: "Agent Reach — Mémo"
type: memo
fiche: "[[Agent Reach]]"
date: 2026-09-25
---

# Agent Reach — Mémo

> Les commandes à connaître pour [[Agent Reach]], qui donne à Claude Code ou Codex un accès à Internet : pages web, YouTube, GitHub, RSS, recherche web, et, après configuration, Twitter/X, Reddit, LinkedIn, Bilibili ou Xiaohongshu. Agent Reach choisit, installe et vérifie les bons outils ; l'agent les appelle ensuite directement.

## Installation

La méthode prévue : donner cette phrase à l'agent.

```text
Install Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md
```

Pour mettre à jour :

```text
Update Agent Reach: https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/update.md
```

Ne pas installer le paquet PyPI du même nom : ce n'est pas ce projet.

## Commandes du CLI

|Commande|Ce qu'elle fait|
|---|---|
|`agent-reach install --env=auto`|Vérifie l'environnement et liste ce qui manque, **sans rien modifier** (comportement par défaut).|
|`agent-reach install --env=auto --dry-run`|Montre ce que l'installation ferait.|
|`agent-reach install --env=auto --system`|Installe réellement les dépendances et enregistre la skill. À n'utiliser qu'après avoir vérifié.|
|`agent-reach doctor`|État de chaque canal : ce qui marche, l'outil utilisé, et comment réparer ce qui est cassé. **Le premier réflexe.**|
|`agent-reach uninstall`|Supprime `~/.agent-reach/` (avec tous les cookies et tokens), les skills et la config MCP.|
|`agent-reach uninstall --dry-run` / `--keep-config`|Prévisualise, ou garde la configuration pour une réinstallation.|

## Ce qui marche sans configuration

Il suffit de demander en langage naturel ; l'agent choisit l'outil.

|Demande|Outil utilisé|
|---|---|
|« Lis cette page »|Jina Reader (`curl https://r.jina.ai/URL`)|
|« Que fait ce dépôt GitHub ? »|`gh repo view owner/repo`|
|« Résume cette vidéo YouTube »|`yt-dlp` (sous-titres)|
|« Cherche sur le web une comparaison de frameworks LLM »|Exa (recherche sémantique via MCP, sans clé)|
|« Abonne-toi à ce flux RSS »|`feedparser`|
|« Cherche des tutos IA sur Bilibili »|`bili search`|

## Ce qui demande une configuration

Demander simplement à l'agent : « Configure Twitter pour moi », « Configure LinkedIn »… Il guide pas à pas.

|Plateforme|Ce que ça débloque|Méthode|
|---|---|---|
|Twitter/X|Recherche, fil, articles longs|Cookies exportés avec l'extension Cookie-Editor|
|Reddit, Facebook, Instagram|Recherche, lecture de posts et commentaires|[[OpenCLI]] avec ta session Chrome|
|Xiaohongshu|Recherche, lecture, commentaires|OpenCLI, ou cookies exportés à la main|
|LinkedIn|Profils, entreprises, offres d'emploi|Serveur MCP LinkedIn|
|GitHub|Dépôts privés, issues, PR|« Connecte-moi à GitHub » (`gh auth login`)|

## Conseils d'utilisation

- **Utiliser des comptes secondaires** pour tout ce qui passe par des cookies (Twitter, Xiaohongshu, Reddit…) : les plateformes peuvent détecter l'automatisation et bannir le compte, et un cookie volé donne un accès complet.
- **Lancer `doctor` dès qu'un canal échoue** : Agent Reach bascule sur un outil de secours quand une plateforme en bloque un, et `doctor` indique lequel est actif.
- **Garder l'installation par défaut en lecture seule**, et n'ajouter `--system` qu'après avoir lu le `--dry-run`.
- **Les identifiants restent en local** dans `~/.agent-reach/config.yaml` (lisible par toi seul) ; ne pas committer ce fichier.
- **Sur un serveur**, certaines plateformes demandent un proxy (environ 1 $/mois) ; ce n'est pas nécessaire sur un ordinateur personnel.

## Sources

- [README Agent Reach (anglais)](https://github.com/Panniantong/Agent-Reach/blob/main/docs/README_en.md)
- [CLAUDE.md du projet](https://github.com/Panniantong/Agent-Reach/blob/main/CLAUDE.md)
- [Agent Reach — explainx.ai](https://explainx.ai/blog/agent-reach-capability-layer-internet-agents-august-2026)
