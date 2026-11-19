---
title: "Paperclip — Mémo"
type: memo
fiche: "[[Paperclip]]"
date: 2026-11-19
---

# Paperclip — Mémo

> Démarrer une instance locale, connecter un premier agent et retrouver ses exécutions. Voir la [[Paperclip|fiche]] et les [[Paperclip#Avis indépendants|avis indépendants]].

## Installation

Utiliser Node.js 24.11 ou plus. L'exemple épingle la version stable vérifiée le 19 novembre 2026 et impose une écoute locale. Paperclip démarre avec PostgreSQL embarqué.

```bash
node --version
npx paperclipai@2026.1117.0 onboard \
  --yes --bind loopback
```

Ouvrir `http://localhost:3100` si le port par défaut est utilisé. Ce mode donne les droits d'administration aux connexions locales. Pour un serveur partagé, utiliser un mode authentifié.

## Premier agent

1. Créer une organisation et lui donner un objectif court.
2. Choisir l'adaptateur Claude Code ou Codex. Installer et authentifier la CLI correspondante sur l'hôte. La connexion par abonnement local demande aussi Python 3.
3. Utiliser **Test your agent** dans son formulaire, puis affecter une tâche interne et examiner son exécution dans **Audit → Runs**.

## Commandes principales

Les commandes d'observation s'exécutent dans un autre terminal. Après `connect`, suivre les instructions affichées et utiliser le profil de l'organisation. Sans binaire installé, préfixer `paperclipai` par `npx`.

|Commande|Rôle|
|---|---|
|`paperclipai connect`|Enregistrer un profil et son contexte pour l'instance.|
|`paperclipai company list`|Lister les organisations accessibles.|
|`paperclipai run list`|Lister les exécutions de l'organisation active.|
|`paperclipai run log <run-id>`|Lire le journal d'une exécution. Remplacer le paramètre par son identifiant.|
|`paperclipai budget overview`|Afficher les plafonds et la dépense enregistrée.|
|`paperclipai doctor`|Diagnostiquer l'installation locale.|
|`paperclipai run`|Relancer l'instance locale au premier plan.|

## Conseils d'utilisation

- Définir un budget initial et rapprocher les dépenses du relevé du fournisseur. Une exécution peut rester sans coût calculé.
- Tester d'abord l'affectation d'une tâche avant d'activer des réveils périodiques. Pour un premier essai, conserver des droits limités et une validation humaine avant une action externe.

## Sources

- [Installation et démarrage](https://docs.paperclip.ing/reference/cli/installation/) et [premier agent](https://docs.paperclip.ing/guides/getting-started/your-first-agent/).
- [Commandes d'exécution](https://docs.paperclip.ing/reference/cli/run/) et [budgets](https://docs.paperclip.ing/reference/cli/cost/).
- [Commandes de configuration](https://docs.paperclip.ing/reference/cli/setup-commands/) et [profils CLI](https://docs.paperclip.ing/reference/cli/overview/).
