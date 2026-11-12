---
title: "Agency Agents — Mémo"
type: memo
fiche: "[[Agency Agents]]"
date: 2026-09-25
---

# Agency Agents — Mémo

> L'essentiel pour utiliser [[Agency Agents]], la collection de plus de 230 agents spécialisés (ingénierie, design, marketing, ventes, sécurité, produit, finance, jeu vidéo…) à installer dans Claude Code, Codex, Cursor ou Gemini CLI. Chaque agent a un rôle, une personnalité, une méthode et des livrables attendus.

## Installation

```bash
# App de bureau (macOS, Linux, Windows) : parcourir, installer et mettre à jour les agents
brew install --cask msitarzewski/agency-agents/agency-agents

# En ligne de commande, depuis le dépôt cloné
./scripts/install.sh                                             # assistant interactif : outils + équipes
./scripts/install.sh --tool claude-code --division engineering,security
./scripts/install.sh --tool codex --agent frontend-developer,ui-designer
./scripts/install.sh --list teams                                # équipes et nombre d'agents
./scripts/install.sh --tool opencode --division engineering --dry-run
```

Pour Claude Code, les agents sont de simples fichiers Markdown : on peut aussi copier une division à la main (`cp engineering/*.md ~/.claude/agents/`).

## Utiliser un agent

Pas de commande dédiée : on l'appelle par son nom, en langage naturel.

- « Active le mode Frontend Developer et aide-moi à construire ce composant React »
- « Utilise le Code Reviewer pour relire cette PR »
- « Demande au Software Architect de comparer ces deux architectures »

Dans Claude Code, `/agents` liste les agents installés.

## Quelques agents par division

|Division|Exemples d'agents|
|---|---|
|Ingénierie|Frontend Developer, Backend Architect, Software Architect, Code Reviewer, DevOps Automator, SRE, Database Optimizer, Technical Writer, Codebase Onboarding Engineer|
|Design|UI Designer, UX Researcher, Brand Guardian…|
|Marketing / Paid Media / Ventes|Rédaction, réseaux sociaux, campagnes publicitaires, prospection|
|Produit / Gestion de projet|Priorisation, roadmap, suivi de projet|
|Tests / Sécurité|Tests, audits de sécurité|
|Spécialisées|Jeu vidéo (Unity, Unreal, Godot), finance, santé, recherche, SIG…|

La liste complète figure dans le README du dépôt.

## Conseils d'utilisation

- **N'installer que les divisions utiles** (`--division`) : chaque agent installé ajoute sa description au contexte des sessions. Tout installer alourdit Claude Code et brouille le choix de l'agent.
- **Appeler l'agent explicitement par son nom** plutôt que d'espérer que Claude le choisisse seul.
- **Agents seuls pour une tâche rapide, équipe pour une vraie collaboration** : plusieurs agents qui se relisent coûtent plus de tokens, car chacun a son propre contexte.
- **Lire et adapter les fichiers** : ce sont des prompts Markdown. Les ajuster à ta stack et à tes conventions améliore nettement les résultats.
- **OpenCode** n'enregistre qu'environ 119 agents : au-delà, les autres sont ignorés sans message. Installer un sous-ensemble.

## Sources

- [README Agency Agents](https://github.com/msitarzewski/agency-agents)
- [Intégration Claude Code](https://github.com/msitarzewski/agency-agents/blob/main/integrations/claude-code/README.md)
- [Agency Agents — YUV.AI Blog](https://yuv.ai/blog/agency-agents)
- [30 Tips for Claude Code Agent Teams](https://getpushtoprod.substack.com/p/30-tips-for-claude-code-agent-teams)
