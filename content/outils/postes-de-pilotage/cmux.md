---
title: "cmux"
type: outil
description: "Terminal macOS natif centré sur les splits, notifications et agents demandant de l'attention."
format: application
tags:
  - metier/ingenierie
  - theme/multi-agent
  - theme/navigateur
editeur: "Manaflow"
logo: "[[cmux.png]]"
site: "https://cmux.com"
depot: "https://github.com/manaflow-ai/cmux"
licence: "GPL-3.0-or-later"
statut: disponible
derniere_maj: 2026-11-11
etoiles: 28795
forks: 2674
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 4
note_maturite: 3
note_popularite: 4
memo: "[[cmux mémo]]"
avis_maj: 2026-10-10
modified: 2026-11-12
---

# cmux

> Terminal macOS natif fondé sur libghostty, avec workspaces, splits, navigateur et notifications conçues pour superviser plusieurs agents CLI sans abandonner un workflow terminal-first.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[cmux mémo]] pour le mémo pratique.

## Résumé

cmux part du constat qu'un développeur n'a pas nécessairement besoin d'un orchestrateur complet : il lui faut parfois surtout voir quelle session travaille, laquelle attend une permission et laquelle vient de terminer. L'application ajoute à un terminal Ghostty des onglets verticaux, splits, statuts Git/PR, notifications, navigateur scriptable et API d'automatisation.

Contrairement à [[Paradev]] ou [[Conductor]], cmux n'impose pas un modèle « une tâche = un worktree ». Cette liberté préserve les habitudes de shell, SSH et tmux, mais laisse à l'utilisateur la responsabilité de l'isolation Git et du parcours de fusion.

## Fonctionnalités

- Terminal natif Swift/AppKit, accéléré par libghostty.
- Workspaces, onglets verticaux et splits avec restauration de disposition.
- Anneaux, badges et panneau de notifications pour les agents.
- Hooks pour Claude Code, Codex, OpenCode, Pi et autres CLI.
- Navigateur intégré pilotable par API d'accessibilité.
- CLI et socket API : créer, diviser, envoyer du texte, lire l'écran, notifier.
- Support natif de Claude Code Teams et attachement à des sessions tmux distantes.
- TUI distincte disponible pour macOS, Linux et Windows.

## Analyse

|Critère|Note|
|---|--:|
|Documentation|★★★★☆|
|Précision des descriptions|★★★★☆|
|Maturité|★★★☆☆|
|Popularité|★★★★☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (11 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 28 795 au 16 novembre 2026._

### Points forts

- Très rapide et cohérent avec les usages terminal existants.
- Notifications réellement utiles lorsqu'un agent attend hors de la vue active.
- Compatible avec n'importe quel programme en ligne de commande.
- Browser et API donnent aux agents davantage qu'un simple pseudo-terminal.
- Gratuit, ouvert et très programmable.

### Limites

- Application principale macOS uniquement.
- Pas de worktree automatique ni de pipeline de revue/merge imposé.
- La puissance de l'API et des splits peut recréer la complexité de tmux.
- Pas de mémoire partagée ou de coordination sémantique entre agents.
- Les fonctions mobiles/cloud récentes ajoutent une surface technique et des bugs potentiels.

### Qualité

**Commentaire :** choix terminal-first pour qui possède déjà une culture terminal, SSH ou tmux. Il remplace efficacement plusieurs fenêtres de terminal, mais pas un véritable gestionnaire de tâches Git.

## Relations

- **Alternative à :** Warp, Ghostty, iTerm2, tmux
- **Complément de :** [[Claude Squad]], Git worktrees manuels
- **S'intègre avec :** [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], SSH, tmux

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 10 octobre 2026._

### Synthèse

cmux reçoit les avis les plus enthousiastes chez les utilisateurs qui possèdent déjà une culture terminal, SSH ou tmux. La rapidité de l'application, les onglets verticaux et la possibilité de sauter immédiatement vers l'agent qui réclame une décision sont ses bénéfices les plus souvent cités.

Les critiques ne contestent pas tellement les performances ; elles portent sur le modèle. Une collection de splits reste une collection de terminaux : sans convention de worktree, de branche et de revue, l'utilisateur peut toujours se perdre. Plusieurs utilisateurs jugent donc cmux puissant mais « clunky » lorsque leur vrai besoin est la coordination Git et la mémoire partagée.

### Avis favorables

- Sensation plus légère et plus calme que les terminaux devenus des IDE complets.
- Très bon remplacement de Ghostty + nombreux onglets.
- Notifications supérieures aux messages génériques de certains agents.
- Fonctionne avec des sessions locales, SSH et tmux distantes.
- Pas de verrouillage sur un fournisseur d'IA ou un harnais particulier.

### Critiques récurrentes

- macOS seulement pour l'application native.
- Worktrees, conflits, PR et priorités restent à organiser séparément.
- Aucun contexte partagé automatique entre les sessions.
- Le nombre d'options, hooks et APIs peut devenir une configuration à maintenir.
- Une session visible comme « terminée » n'est pas nécessairement testée ou prête à fusionner.

### Verdict

Excellent terminal pour superviser des agents ; orchestrateur Git incomplet par conception. Le meilleur choix si l'on veut garder la main, moins bon si l'on attend une application qui organise automatiquement tout le cycle de livraison.

## Sources

- [Dépôt officiel](https://github.com/manaflow-ai/cmux)
- [Documentation](https://cmux.com/docs)
- [API CLI](https://cmux.com/docs/api)

### Sources des avis

- [Retour d'un utilisateur terminal-first](https://www.reddit.com/r/MacStack/comments/1uwudg1/stop_using_bloated_tmux_configs_for_ai_terminals/)
- [Comparaison quotidienne avec Conductor et Superset](https://www.reddit.com/r/ClaudeCode/comments/1rxwkoz/my_thoughts_on_conductor_vs_superset_vs_cmux_vs/)
- [Critique des configurations cmux/tmux](https://www.reddit.com/r/ClaudeCode/comments/1ulblh5/i_tried_conductor_cmux_and_the_rest_for_running/)
- [Documentation officielle](https://cmux.com/docs)

_Dernière analyse : 12 novembre 2026_
