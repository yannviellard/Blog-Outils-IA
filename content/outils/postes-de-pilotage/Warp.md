---
title: "Warp"
type: outil
description: "Terminal multiplateforme avec agent intégré et orchestration cloud Oz."
format: application
tags:
  - metier/ingenierie
  - theme/multi-agent
editeur: "Warp"
site: "https://www.warp.dev"
depot: "https://github.com/warpdotdev/warp"
licence: "AGPL-3.0 ; composants UI MIT"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 65981
forks: 5773
etoiles_releve: 2026-11-11
note_documentation: 5
note_precision: 4
note_maturite: 4
note_popularite: 4
memo: "[[Warp mémo]]"
avis_maj: 2026-10-10
modified: 2026-11-12
---

# Warp

> Environnement de développement agentique né comme terminal moderne, désormais complété par Warp Agent et Oz pour lancer et superviser des agents locaux ou cloud sur macOS, Linux et Windows.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Warp mémo]] pour le mémo pratique.

## Résumé

Warp conserve un shell normal mais structure chaque commande et sa sortie sous forme de Block. Au-dessus du terminal, il ajoute édition riche, recherche, workflows partagés, agent multi-modèles, fichiers, diff et conversations. Oz étend l'ensemble à l'exécution distante : environnement cloud, agent nommé, compétences, secrets, historique et contrôle programmatique.

Warp accepte aussi des agents tiers comme Codex et Claude Code. Il est donc à la fois un remplacement du terminal et une plateforme agentique. Cette ambition le rend plus complet que [[cmux]], mais aussi plus dense et plus dépendant d'un compte, de crédits et de services Warp pour les fonctions avancées.

## Fonctionnalités

- Terminal multiplateforme avec Blocks, éditeur moderne, complétions et palettes.
- Warp Agent intégré avec choix de modèles et contrôles d'autonomie.
- Exécution de CLI tierces dans des onglets et panneaux.
- Oz : agents cloud, environnements, agents nommés, skills, secrets et API.
- Sessions partageables et Warp Drive pour workflows et notebooks.
- Possibilité d'apporter ses propres clés ou endpoints selon l'offre.
- Client terminal ouvert sous AGPL-3.0 ; services cloud commerciaux.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★★|
|Précision des descriptions|★★★★☆|
|Maturité|★★★★☆|
|Popularité|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (11 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 65 981 au 11 novembre 2026._

### Points forts

- Seul outil de cette sélection proposant une expérience cohérente sur les trois OS majeurs.
- Très bon terminal généraliste, utilisable sans agents.
- Passage pratique entre shell, agent local et exécution cloud.
- Contrôles d'équipe, dépenses, partage et observabilité plus développés que les outils locaux.
- Projet client désormais ouvert et très actif.

### Limites

- Facturation par crédits et calcul cloud moins prévisible qu'une CLI utilisant directement un abonnement.
- Interface devenue complexe à mesure que les fonctions agentiques se sont ajoutées.
- Le worktree par tâche n'est pas le principe central : il faut définir soi-même l'isolation Git locale.
- Valeur maximale liée aux services Warp et à un compte en ligne.
- Les utilisateurs cherchant un terminal minimal peuvent préférer [[cmux]] ou Ghostty.

### Qualité

**Commentaire :** choix pertinent pour les équipes multiplateformes et les agents cloud, mais pas nécessairement le plus simple pour superviser quelques agents locaux. Voir [[#Avis indépendants|les avis indépendants]] et [[Warp mémo]].

## Relations

- **Alternative à :** [[cmux]], Ghostty, iTerm2, Windows Terminal
- **Complément de :** Git worktrees, [[Claude Squad]]
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], GitHub, Slack

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 10 octobre 2026._

### Synthèse

Warp reste apprécié pour son rendu, son éditeur de commande, ses Blocks et sa disponibilité sur macOS, Linux et Windows. L'intégration de modèles et d'agents cloud donne une continuité qu'aucun autre terminal de cette sélection ne propose à la même échelle.

Une partie des anciens utilisateurs estime toutefois que le produit a perdu la simplicité qui faisait son attrait. Les changements d'interface autour d'Oz et du basculement terminal/agent sont décrits comme déroutants ; le prix et la mécanique de crédits sont également contestés. Le débat oppose ainsi deux attentes : un terminal moderne discret ou un environnement de développement complet.

### Avis favorables

- Installation et fonctionnement cohérents sur plusieurs systèmes.
- Interface plus accessible que tmux pour les nouveaux utilisateurs.
- Agent intégré pratique pour expliquer des commandes et effectuer des tâches ponctuelles.
- Oz permet de lancer des travaux longs sans garder la machine locale active.
- Apport de clés personnelles et client ouvert réduisent une partie du verrouillage.

### Critiques récurrentes

- Interface perçue comme chargée et changeante.
- Crédits, compute et options payantes difficiles à comparer à un abonnement CLI direct.
- Certains utilisateurs préfèrent Claude Code ou Codex pour le code et Warp seulement comme terminal.
- Moins opinionated sur les worktrees et la revue locale que [[Superset]] ou [[Conductor]].
- Un terminal cloud plus puissant élargit aussi la surface de permissions et de secrets à gouverner.

### Interprétation

Les critiques ne signifient pas que Warp est un mauvais produit ; elles révèlent une divergence de positionnement. Pour qui veut « juste un terminal », le surplus fonctionnel est une nuisance. Pour une équipe qui souhaite exécuter et observer des agents distants, ce surplus constitue précisément la valeur du produit.

### Verdict

À privilégier pour les équipes multiplateformes et les agents cloud. Pour deux ou trois agents locaux sur Mac, [[cmux]] ou [[Superset]] seront souvent plus directs.

## Sources

- [Dépôt du client](https://github.com/warpdotdev/warp)
- [Documentation](https://docs.warp.dev)
- [Oz](https://www.warp.dev/oz)
- [Tarifs](https://www.warp.dev/pricing)

### Sources des avis

- [Discussion sur les changements d'interface et Oz](https://www.reddit.com/r/warpdotdev/comments/1r404b6/what_have_you_done_to_warp_terminal/)
- [Discussion sur les changements tarifaires](https://www.reddit.com/r/warpdotdev/comments/1oktdy9/warp_terminal_unbelievably_bad_price_changes/)
- [Discussion cmux contre Warp](https://www.reddit.com/r/PiCodingAgent/comments/1tkp4x4/cmux_vs_warp_for_pi/)
- [Tarifs officiels](https://www.warp.dev/pricing)

_Dernière analyse : 12 novembre 2026_
