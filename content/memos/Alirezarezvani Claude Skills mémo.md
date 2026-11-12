---
title: "Alirezarezvani Claude Skills — Mémo"
type: memo
fiche: "[[Alirezarezvani Claude Skills]]"
date: 2026-09-25
---

# Alirezarezvani Claude Skills — Mémo

> Les commandes à connaître pour [[Alirezarezvani Claude Skills]], une très grande bibliothèque de skills, d'agents et de « personas » pour Claude Code, Codex, Gemini CLI ou Cursor : ingénierie, produit, marketing, conformité, finance, conseil de direction.

## Installation

```bash
# Claude Code : ajouter la marketplace
/plugin marketplace add alirezarezvani/claude-skills

# Puis installer par domaine
/plugin install engineering-skills@claude-code-skills            # ingénierie de base
/plugin install engineering-advanced-skills@claude-code-skills   # 25 skills avancées (« POWERFUL »)
/plugin install product-skills@claude-code-skills
/plugin install marketing-skills@claude-code-skills
/plugin install c-level-skills@claude-code-skills                # conseil de direction (CTO, CFO…)
/plugin install skill-security-auditor@claude-code-skills        # audit de sécurité des skills

# Codex
npx agent-skills-cli add alirezarezvani/claude-skills --agent codex

# Autres outils (Cursor, Aider…) : convertir puis installer, depuis le dépôt cloné
./scripts/convert.sh --tool all
./scripts/install.sh --tool cursor --target /chemin/du/projet
```

## Utiliser une skill

Nommer la skill dans la demande :

- « Avec la skill senior-architect, revois notre architecture microservices et identifie les 3 principaux risques de montée en charge. »
- « Avec la skill content-creator, écris un article sur le développement assisté par IA, optimisé pour le SEO. »

## Skills avancées à connaître

|Skill|Ce qu'elle fait|
|---|---|
|`pr-review-expert`|Revue de PR : impact des changements, sécurité, évolution de la couverture.|
|`adversarial-reviewer`|Revue par trois relecteurs « hostiles » (saboteur, nouvel arrivant, auditeur sécurité), chacun obligé de trouver au moins un problème.|
|`tech-debt-tracker`|Repère et priorise la dette technique.|
|`dependency-auditor`|Audit des dépendances et des licences, plan de mise à jour.|
|`ci-cd-pipeline-builder`|Génère la CI (GitHub Actions, GitLab CI) selon la stack.|
|`mcp-server-builder`|Construit un serveur MCP à partir d'une spec OpenAPI.|
|`database-schema-designer`|Des besoins aux migrations, types, données de test et règles d'accès.|
|`codebase-onboarding` / `runbook-generator`|Documentation d'intégration et runbooks à partir du code.|
|`git-worktree-manager`|Développement parallèle avec des worktrees isolés.|
|`env-secrets-manager`|Gestion des `.env`, détection de fuites de secrets.|

## Personas

Des identités d'agent qui combinent plusieurs skills et une façon de travailler.

|Persona|Pour|
|---|---|
|Startup CTO|Choix d'architecture et de stack, due diligence technique|
|Growth Marketer|Stratégie de lancement, croissance par le contenu|
|Solo Founder|Projet solo ou MVP : tous les rôles à la fois|

Installation pour Claude Code : `cp agents/personas/startup-cto.md ~/.claude/agents/`

## Scripts Python fournis (sans dépendance)

|Commande|Ce qu'elle fait|
|---|---|
|`python3 engineering/skill-security-auditor/scripts/skill_security_auditor.py <dossier-skill>`|Vérifie une skill avant de l'installer (injection, exfiltration, prompt injection) : PASS / WARN / FAIL.|
|`python3 c-level-advisor/cto-advisor/scripts/tech_debt_analyzer.py <codebase>`|Note la dette technique.|
|`python3 product-team/product-manager-toolkit/scripts/rice_prioritizer.py features.csv`|Priorisation RICE.|
|`python3 marketing-skill/content-production/scripts/brand_voice_analyzer.py article.txt`|Analyse la voix de marque d'un texte.|

## Conseils d'utilisation

- **Installer par domaine, pas tout** : la bibliothèque compte des centaines de skills ; chaque plugin installé ajoute ses descriptions au contexte.
- **Nommer la skill voulue** dans la demande pour éviter que Claude en choisisse une autre.
- **Auditer les skills tierces** avec `skill-security-auditor` avant de les installer, y compris celles d'autres dépôts.
- **Combiner persona et skills** pour un projet complet : par exemple Startup CTO pour construire, puis Growth Marketer pour lancer.

## Sources

- [README claude-skills](https://github.com/alirezarezvani/claude-skills)
- [Guide d'installation](https://github.com/alirezarezvani/claude-skills/blob/main/INSTALLATION.md)
- [Site de la bibliothèque](https://alirezarezvani.github.io/claude-skills/)
- [Personas (wiki)](https://github.com/alirezarezvani/claude-skills/wiki/Personas-Overview)
