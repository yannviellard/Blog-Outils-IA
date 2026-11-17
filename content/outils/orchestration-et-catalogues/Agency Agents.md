---
title: "Agency Agents"
type: outil
description: "Plus de 230 définitions de rôles réparties en une quinzaine de divisions d'entreprise ; plus de rôles ne garantit pas de meilleurs résultats."
format: collection
tags:
  - metier/ingenierie
  - metier/produit-design
  - metier/support-client
  - theme/multi-agent
editeur: "msitarzewski"
site: "https://agency-agents.app/"
depot: "https://github.com/msitarzewski/agency-agents"
licence: "MIT"
statut: disponible
derniere_maj: 2026-11-09
etoiles: 168657
forks: 27382
etoiles_releve: 2026-11-16
note_documentation: 3
note_precision: 3
note_maturite: 3
note_popularite: 5
memo: "[[Agency Agents mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Agency Agents

> Collection open source de plus de 230 agents IA spécialisés, organisés en plus de quinze divisions, chacun définissant un rôle, une personnalité, un workflow et des livrables pour des tâches de développement, produit, marketing, design, sécurité et autres domaines.

**Composition** : 232+ agents (rôles).

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Agency Agents mémo]] pour le mémo pratique.

## Résumé

**Agency Agents** est une bibliothèque de définitions d'agents spécialisés destinées principalement aux outils de coding agent et d'IA générative.

Chaque agent est essentiellement un fichier Markdown contenant des instructions structurées : rôle, expertise, comportement, processus de travail et livrables attendus. Le dépôt couvre un très grand nombre de spécialités, de l'ingénierie logicielle au marketing, en passant par le design, la sécurité, la finance ou encore des domaines très spécialisés.

Le projet se positionne davantage comme un **catalogue de spécialistes réutilisables** que comme un framework complet d'orchestration multi-agent. Les agents peuvent être sélectionnés individuellement, adaptés puis intégrés dans différents environnements.

Le dépôt est très actif : le mainteneur indiquait en juin 2026 plus de 230 agents dans 16 divisions (le README liste 18 divisions au 9 octobre 2026), tandis que les commits et pull requests de septembre montrent une évolution toujours soutenue.

## Fonctionnalités

- **Large catalogue d'agents spécialisés** organisés par divisions : engineering, design, marketing, product, security, finance, etc.
    
- **Prompts structurés** décrivant rôle, expertise, processus, personnalité et livrables plutôt que de simples personas.
    
- **Intégrations multi-outils** avec notamment Claude Code, Cursor, OpenCode, Aider, Windsurf et d'autres environnements.
    
- **Scripts d'installation et de conversion** permettant d'adapter les définitions aux formats de différents outils.
    
- **Contribution communautaire** permettant d'ajouter de nouveaux spécialistes et d'améliorer les agents existants.
    
- **MIT License**, permettant l'utilisation et la modification du contenu, y compris commercialement.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★☆☆|
|Précision des descriptions|★★★☆☆|
|Qualité des prompts|★★★☆☆|
|Richesse fonctionnelle|★★★★★|
|Portabilité|★★★★★|
|Maturité|★★★☆☆|
|Popularité|★★★★★|
|Orchestration native|★★☆☆☆|
|Maintenabilité d'une sélection d'agents|★★★☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 168 657 au 16 novembre 2026._

**Commentaire :** projet très riche et actif, mais dont la valeur vient principalement de la qualité et de la diversité des définitions d'agents, qui n'est pas évaluée de façon indépendante (note de qualité des prompts à ★★★☆☆, maturité à ★★★☆☆ en l'absence de releases formelles). Il ne constitue pas à lui seul un framework d'orchestration multi-agent complet. La qualité peut également varier selon les agents, car le catalogue est fortement communautaire. Une discussion du dépôt soulève notamment la question de la provenance et de la validation des profils spécialisés.

### Points forts

- **Catalogue très large** : plus de 230 agents répartis en plus d'une quinzaine de divisions ; l'ampleur est une force de découverte, pas une garantie de résultats (voir Limites).
    
- **Spécialisation fine** permettant de sélectionner uniquement les rôles pertinents pour un workflow.
    
- **Format simple et transparent** : les agents sont principalement des fichiers Markdown facilement inspectables et personnalisables.
    
- **Très bonne portabilité** entre différents outils d'IA.
    
- **Écosystème communautaire actif** : nombreuses contributions et demandes d'intégration. En septembre 2026, le dépôt comptait notamment des dizaines de PR ouvertes et plusieurs centaines de PR déjà fusionnées.
    
- **Bonne séparation entre définition de rôle et outil d'exécution** : le même agent peut être adapté à plusieurs environnements.
    
- **Licence MIT**, favorable à la réutilisation et à l'adaptation.
    

### Limites

- **Ce n'est pas un véritable framework multi-agent** : les définitions d'agents ne fournissent pas à elles seules mémoire, orchestration, planification distribuée ou gestion avancée de l'état.
    
- **Qualité hétérogène possible** : tous les agents n'ont pas nécessairement le même niveau de validation ou d'expertise métier.

- **Plus de rôles ne garantit pas de meilleurs résultats** : des praticiens rapportent que quelques agents généralistes bien cadrés sont souvent plus efficaces que des dizaines de personas ; une spécialisation artificielle ajoute du routage, des tokens et de la coordination sans gain mesuré. Un rôle n'a de sens que s'il nécessite un contexte, des critères de sortie ou des outils réellement distincts.

- **Agents tiers à relire comme du code de dépendance** : un échange du dépôt interroge déjà la provenance et la validation de certains profils.
    
- **Risque de surinstallation** : installer l'ensemble du catalogue peut augmenter inutilement la complexité et le contexte disponible.
    
- **Chevauchement avec d'autres skills/workflows** : certains agents peuvent reproduire une partie des fonctions de frameworks de développement ou de skills spécialisés.
    
- **Maintenance potentiellement importante** pour une équipe qui personnalise un grand nombre d'agents.
    
- **Scripts d'installation à examiner avant exécution** : le projet rappelle lui-même que les scripts shell sont exécutables et doivent être inspectés.
    
- **Pas de releases GitHub formelles** : le projet fonctionne principalement via le développement continu sur `main`.
    

## Relations

- **Alternative à :** collections de personas/agents spécialisées ou catalogues de prompts similaires
    
- **S'intègre avec :** Claude Code, Cursor, OpenCode, Aider, Windsurf et plusieurs autres coding agents
    
- **Utilise :** principalement des fichiers Markdown et des scripts d'installation/conversion
    

### Positionnement dans une stack Claude Code

Agency Agents est surtout une **couche de spécialisation des rôles** :

```text
Claude Code
    │
    ├── Workflow / méthodologie
    │       └── Superpowers
    │
    ├── État / planification
    │       └── Planning with Files
    │
    └── Spécialistes
            └── Agency Agents
```

Il est donc préférable de sélectionner quelques agents pertinents plutôt que d'installer tout le catalogue.

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

La collection séduit par son ampleur et par la clarté de ses rôles : elle permet de partir d’un spécialiste déjà décrit plutôt que d’écrire soi-même un long prompt. Les utilisateurs de sous-agents jugent ce type de catalogue utile lorsqu’un rôle a réellement besoin d’un contexte, de critères de sortie ou d’outils distincts.

Le principal reproche adressé aux grands catalogues d’agents est aussi pertinent ici : **plus de rôles ne garantit pas de meilleurs résultats**. Des praticiens rapportent que quelques agents généralistes bien cadrés sont souvent plus efficaces que des dizaines de personas. La spécialisation artificielle peut ajouter du routage, des tokens et du travail de coordination sans gain mesurable. La qualité varie nécessairement d’un fichier à l’autre, et les agents tiers doivent être relus comme du code de dépendance.

### Comparaison

Agency Agents est plus simple et plus orienté « fiches métier » que Ruflo ou BMAD, qui orchestrent un processus complet. Face à `wshobson/agents`, il privilégie le choix d’un personnage spécialisé plutôt qu’un marketplace de plugins et de commandes.

### Verdict

Excellent réservoir d’idées et de rôles à adapter ; moins convaincant comme équipe à installer en bloc. Mieux vaut sélectionner quelques agents et mesurer leur apport.

## Sources

- [GitHub](https://github.com/msitarzewski/agency-agents)
    
- [Agency Agents](https://agency-agents.app/)
    
- [License](https://github.com/msitarzewski/agency-agents/blob/main/LICENSE)
    
- [Contributing](https://github.com/msitarzewski/agency-agents/blob/main/CONTRIBUTING.md)
    
- [Issues](https://github.com/msitarzewski/agency-agents/issues)
    
- [Discussions](https://github.com/msitarzewski/agency-agents/discussions)
    

### Sources des avis

- [Site du projet](https://agency-agents.app/)
- [Discussion sur la valeur réelle des agents spécialisés](https://www.reddit.com/r/ClaudeAI/comments/1r6kub4/how_many_and_which_agentssubagents_do_you_really/)
- [Étude sur la maintenance des marketplaces de plugins](https://arxiv.org/abs/2608.28497)

_Dernière analyse : 12 novembre 2026_