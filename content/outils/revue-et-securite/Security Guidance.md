---
title: "Security Guidance"
type: outil
description: "Garde-fou de sécurité pendant la génération et avant commit ou push."
format: plugin
tags:
  - metier/ingenierie
  - metier/operations
  - theme/securite
  - theme/revue-de-code
editeur: "Anthropic"
logo: "[[claude.svg]]"
site: "https://code.claude.com/"
depot: "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance"
licence: "Anthropic Commercial Terms"
statut: disponible
derniere_maj: 2026-11-10
note_documentation: 4
note_precision: 4
note_maturite: 3
memo: "[[Security Guidance mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Security Guidance

> Plugin officiel de Claude Code qui ajoute une couche de contrôle de sécurité au code généré ou modifié par Claude, grâce à des règles de détection rapide, une revue LLM des modifications et une revue agentique des commits.

**Composition** : 1 agent.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Security Guidance mémo]] pour le mémo pratique.

## Résumé

**Security Guidance** est un plugin officiel du marketplace `claude-plugins-official` destiné à identifier les vulnérabilités introduites ou modifiées pendant une session Claude Code.

Il combine trois niveaux de contrôle : détection par patterns lors des modifications, analyse LLM du diff en fin de tour et revue agentique lors des commits. Le plugin est conçu comme une **aide à la revue de sécurité**, et non comme un remplacement d'un SAST, d'un DAST, d'un scan de dépendances ou d'un pentest.

Installation :

```text
/plugin install security-guidance@claude-plugins-official
```

Le plugin nécessite Claude Code CLI ≥ **2.1.144**, Python 3.8+ et un chemin d'accès fonctionnel à un modèle.

## Fonctionnalités

- **Pattern warnings** : détection rapide d'environ 25 patterns dangereux lors des opérations `Edit`, `Write`, `MultiEdit` et `NotebookEdit`.
    
- **LLM diff review** : analyse du code modifié en fin de tour et retour des problèmes de sécurité importants à Claude afin qu'il puisse les corriger.
    
- **Agentic commit review** : analyse des fichiers liés au changement lors d'un `git commit`, avec exploration du code via `Read`, `Grep` et `Glob`.
    
- Détection de classes telles que **XSS, injection, SSRF, secrets en dur, IDOR, contournement d'authentification, désérialisation dangereuse et path traversal**.
    
- **Règles de sécurité spécifiques au projet** via `.claude/claude-security-guidance.md`.
    
- **Patterns personnalisés** via `security-patterns.yaml` ou `security-patterns.json`.
    
- Configuration indépendante des différentes couches via variables d'environnement.
    
- Mode `SG_DUAL_OR=on` permettant deux analyses parallèles pour augmenter le rappel, au prix d'environ deux fois plus d'appels API.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Couverture sécurité|★★★☆☆|
|Intégration Claude Code|★★★★★|
|Automatisation|★★★★★|
|Précision|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|—|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité non notée : l'outil est un sous-dossier du dépôt `anthropics/claude-plugins-official`, dont les étoiles mesurent l'ensemble._

**Commentaire :** le plugin est profondément intégré au système de hooks de Claude Code et propose une approche intéressante en profondeur : règles déterministes rapides, revue LLM puis analyse agentique du contexte du code. Sa principale limite reste celle de toute analyse de sécurité assistée par LLM : faux positifs et vulnérabilités manquées restent possibles, d'où des notes de couverture et de précision de ★★★☆☆ en l'absence de mesure indépendante (voir [[#Avis indépendants|les avis indépendants]]). Anthropic recommande explicitement de le compléter par une revue humaine, du SAST/DAST, du dependency scanning et du pentest.

### Points forts

- **Trois niveaux complémentaires** de détection, des patterns simples jusqu'à l'analyse multi-fichiers.
    
- Fonctionne directement dans le workflow Claude Code via les hooks, sans étape manuelle supplémentaire.
    
- Capable, selon sa documentation, de détecter des vulnérabilités qui dépassent un simple pattern matching, notamment **IDOR, auth bypass et SSRF cross-file** ; les benchmarks comparant LLM et analyse statique montrent des forces différentes de celles de CodeQL, Snyk ou SonarQube.
    
- Très bonne extensibilité avec des règles de sécurité propres au projet.
    
- Les règles peuvent être versionnées dans le repository avec `.claude/claude-security-guidance.md`.
    
- Les revues sont basées sur le **diff réellement produit pendant la session**, plutôt que de réanalyser systématiquement tout le projet.
    

### Limites

- Ce n'est **pas un outil de sécurité exhaustif** et ne remplace ni SAST/DAST, ni les scanners de dépendances, ni une revue humaine.
    
- Les analyses LLM peuvent produire des faux positifs ou manquer certaines vulnérabilités.
    
- Les revues LLM transmettent le code modifié au modèle configuré ; la politique de traitement des données dépend donc du provider utilisé.
    
- La revue agentique peut lire des fichiers supplémentaires du repository pour suivre les flux de données.
    
- Les règles spécifiques du fichier `claude-security-guidance.md` sont actuellement intégrées à la revue LLM, mais pas à la revue agentique des commits.
    
- Le mode `SG_DUAL_OR` augmente la couverture mais environ double le coût API des reviews concernées.
    
- Un hook exécuté à chaque tour peut ralentir ou coûter cher sur de gros changements ; le plugin analyse ce qu'il voit et ne réalise pas DAST, SCA, gestion des secrets ni threat modeling complet.
    

## Relations

- **Complémentaire de :** CodeQL (flux de données et requêtes reproductibles), Semgrep (rapide et personnalisable), Snyk (SAST, dépendances, conteneurs et politiques), SonarQube — jamais un contrôle unique

- **Alternative à :** outils de security review intégrés directement dans le workflow de développement, comme `/security-review` de Claude Code
    
- **S'intègre avec :** [[Claude Code]], Git, hooks Claude Code
    
- **Utilise :** Claude LLM, Claude Agent SDK, Git diff
    

## Architecture

```text
Claude Code
    │
    ├── Edit / Write
    │      └── Pattern rules
    │             └── warnings immédiats
    │
    ├── Fin de tour
    │      └── Git diff
    │             └── LLM security review
    │                    └── findings → Claude
    │
    └── git commit
           └── Agentic security review
                  ├── Read
                  ├── Grep
                  └── Glob
                         └── analyse du flux de données
```

Le plugin utilise notamment les hooks `UserPromptSubmit`, `PostToolUse` et `Stop` pour orchestrer ces contrôles.

## Configuration

Les principales variables disponibles sont :

```text
SECURITY_GUIDANCE_DISABLE=1
ENABLE_PATTERN_RULES=0
ENABLE_CODE_SECURITY_REVIEW=0
ENABLE_STOP_REVIEW=0
ENABLE_COMMIT_REVIEW=0
SECURITY_REVIEW_MODEL=claude-opus-4-7
SG_DUAL_OR=on
```

Les règles propres au projet peuvent être placées dans :

```text
.claude/claude-security-guidance.md
.claude/security-patterns.yaml
.claude/security-patterns.json
```

Le plugin permet également un fichier local gitignoré pour les règles spécifiques à un environnement.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Le plugin est apprécié comme garde-fou « dans le flux » : il rappelle les pratiques de sécurité au moment d’écrire, puis peut revoir les changements avant commit ou push. L’intégration native à Claude Code et la prise en compte du contexte lui permettent de signaler des problèmes que des règles syntaxiques simples ne voient pas.

Il ne doit pas être pris pour un scanner complet. Les LLM produisent faux positifs et faux négatifs, et les benchmarks de vulnérabilités montrent que leurs forces diffèrent de celles de CodeQL, Snyk ou SonarQube. Un hook peut aussi ralentir ou coûter cher sur de gros changements. Le plugin analyse ce qu’il voit ; il ne réalise pas automatiquement DAST, SCA, gestion des secrets ou threat modeling complet.

### Comparaison

CodeQL excelle sur les flux de données et requêtes reproductibles ; Snyk réunit SAST, dépendances, conteneurs et politiques ; Semgrep est rapide et personnalisable. Security Guidance apporte surtout une revue contextuelle et des conseils de correction dans l’agent.

### Verdict

Excellent complément précoce, jamais un contrôle unique. Combiner avec SAST/SCA, tests, revue humaine et exigences de conformité adaptées.

## Sources

- [GitHub — security-guidance](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance)
    
- [README](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/security-guidance/README.md)
    
- [Plugin manifest](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/security-guidance/.claude-plugin/plugin.json)
    
- [Claude Code — hooks](https://github.com/anthropics/claude-code/blob/main/plugins/security-guidance/hooks/hooks.json)
    

### Sources des avis

- [Documentation du plugin](https://github.com/anthropics/claude-code/blob/main/plugins/security-guidance/README.md)
- [Benchmark LLM vs analyse statique](https://arxiv.org/abs/2508.04448)
- [Panorama des outils SAST](https://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)

_Dernière analyse : 12 novembre 2026_