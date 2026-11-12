---
title: "Skill"
type: concept
description: "Dossier d'instructions et de ressources qu'un agent charge seulement quand la tâche le demande."
aliases:
  - Skills
  - Agent Skills
modified: 2026-11-12
---

# Skill

> Dossier d'instructions et de ressources qu'un agent charge seulement quand la tâche le demande.

Un **skill** est un dossier qui contient un fichier `SKILL.md` (des instructions en Markdown précédées d'un en-tête YAML) et, au besoin, des fichiers d'appui : références, exemples, scripts. L'agent l'utilise quand la tâche s'y prête, ou l'utilisateur l'appelle directement (dans Claude Code, avec `/nom-du-skill`). Les skills de Claude Code suivent le standard ouvert [Agent Skills](https://agentskills.io) ; [[OpenAI Codex]] et [[OpenCode]] ont aussi leurs skills.

## Fonctionnement

- **Chargement progressif** : seule la description de chaque skill reste en permanence dans le contexte de l'agent, pour qu'il sache quand s'en servir. Le contenu de `SKILL.md` n'est chargé qu'à l'appel du skill, les fichiers d'appui seulement si besoin, et les scripts sont exécutés sans être chargés.
- **Emplacements dans Claude Code** : `~/.claude/skills/<nom>/SKILL.md` (personnel, pour tous les projets), `.claude/skills/<nom>/SKILL.md` (projet, partagé avec le dépôt), ou dans un [[Plugin]] (`<plugin>/skills/<nom>/SKILL.md`, appelé par `/plugin:skill`).
- **Commandes** : dans Claude Code, les anciennes commandes personnalisées (`.claude/commands/`) ont été fusionnées avec les skills ; les deux créent la même commande `/nom`.
- **Taille** : la documentation recommande de garder `SKILL.md` sous 500 lignes et de déplacer le détail dans des fichiers séparés.

## Points de vigilance

- **Un skill est du code à auditer.** Il peut contenir des scripts et des commandes exécutées sur la machine. Dans Claude Code, le champ `allowed-tools` d'un skill accorde des outils sans demande d'approbation pendant le tour où il est appelé, y compris dans un dossier non approuvé : la documentation recommande de relire les skills d'un dépôt avant d'y lancer l'agent.
- **Coût en contexte.** Chaque description reste dans le contexte, même quand le skill ne sert pas : les collections de centaines de skills alourdissent chaque session (voir [[outils/orchestration-et-catalogues/index|Orchestration et catalogues d'agents]]).
- **Une description soignée ne prouve pas l'efficacité.** [[Skill Creator]] propose d'évaluer un skill sur des cas réels, avec un jeu de validation séparé.

## Dans le wiki

- **Skills isolés** : [[FrontEnd Design]], [[Huashu Design]], [[Humanizer]], [[Impeccable]], [[LLM Council]], [[Planning with Files]], [[Skill Creator]], [[UI UX Pro Max]], [[Web Design Guidelines]].
- **Collections de skills** : voir les familles [[outils/methodes-de-developpement/index|Méthodes de développement]], [[outils/orchestration-et-catalogues/index|Orchestration et catalogues d'agents]] et [[outils/marketing-et-seo/index|Marketing et SEO]].

## Sources

- [Claude Code, Skills](https://code.claude.com/docs/en/skills) : documentation officielle, consultée le 12 novembre 2026.
- [Agent Skills](https://agentskills.io) : site du standard ouvert.
- [Anthropic, Equipping agents for the real world with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) : article de l'éditeur.

_Dernière analyse : 12 novembre 2026_
