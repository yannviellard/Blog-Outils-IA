---
title: "Déployer un harnais Product Design UX/UI"
type: guide
description: "Équiper Claude Code et Codex pour cadrer le produit, travailler dans Figma et vérifier l’interface à partir des mêmes règles de design."
date: 2026-11-20
tags:
  - metier/produit-design
  - metier/ingenierie
  - theme/design-system
  - theme/mcp
  - theme/accessibilite
---

# Déployer un harnais Product Design UX/UI

Ce guide reprend le [[Harnais d'agent|harnais]] de MAE Product Design UX/UI. Il relie les décisions produit, les tokens de design, les maquettes Figma et la revue de l’interface. La configuration se partage dans Git et chaque membre de l’équipe autorise l’accès Figma avec son propre compte. Le premier test consiste à lire un écran Figma, puis à vérifier une petite modification sur une copie de travail. [Dépôt privé de référence MAE Product Design UX/UI](https://github.com/yannviellard/MAE-Product-Design-UX-UI)

## 1. Préparer le dépôt

Prévoir Git, [[Claude Code]] ou [[OpenAI Codex|Codex CLI]], un compte Figma et un fichier de test. Pour utiliser le script d’installation de MAE, prévoir aussi Bash, `curl`, Python 3 et Node.js avec `npx`.

**Depuis un clone de MAE**, la configuration et les skills sont déjà versionnées. Le moteur natif d’[[Impeccable]] est installé localement et ignoré par Git. Pour le remettre en place, exécuter la commande suivante depuis le clone, où les fichiers de configuration existent déjà. Le script utilise les versions prévues par le dépôt et vérifie la somme SHA-256 du moteur.

```bash
bash ./install-ux-stack.sh .
```

**Pour un nouveau dépôt**, créer les fichiers indiqués ci-dessous et adapter leurs règles au projet. Les membres qui ont accès au dépôt MAE peuvent partir de sa configuration. Le script MAE cherche ses fichiers de départ dans un dossier `templates/` absent du dépôt actuel. Préparer ces fichiers avant d’utiliser le script sur un dossier vide.

| À versionner                                                               | Rôle                                                                                                                                    |
| -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `AGENTS.md` et `CLAUDE.md`                                                 | Donner le même rôle de responsable UX/UI aux deux agents. Dans la configuration MAE, `CLAUDE.md` importe `AGENTS.md` avec `@AGENTS.md`. |
| `.mcp.json`, `.claude/settings.json`, `.codex/config.toml`                 | Déclarer le même serveur distant Figma pour les deux clients.                                                                           |
| `.claude/skills/` et `.agents/skills/`                                     | Partager les versions des skills et conserver les réglages d’invocation propres à chaque client.                                        |
| `.impeccable/config.json`                                                  | Reprendre les réglages locaux d’Impeccable. MAE désactive les hooks et la vérification automatique des mises à jour.                    |
| `PRODUCT.md`, `BRAND.md`, `EXPERIENCE.md`, `DESIGN.md` et `design/tokens/` | Partager les décisions produit, les règles de design et les valeurs utilisées dans Figma et dans le code.                               |

## 2. Donner une source de référence à chaque décision

| Décision                                                   | Référence                                     |
| ---------------------------------------------------------- | --------------------------------------------- |
| Utilisateurs, besoins et périmètre                         | `PRODUCT.md`                                  |
| Identité, positionnement et lien vers le fichier Figma     | `BRAND.md`                                    |
| Parcours, interactions et états d’erreur ou d’attente      | `EXPERIENCE.md`                               |
| Principes visuels et règles d’usage                        | `DESIGN.md`                                   |
| Valeurs exactes de couleur, d’espacement et de typographie | `design/tokens/*.tokens.json`, au format DTCG |
| Composition d’un écran approuvé                            | La maquette Figma correspondante              |
| Comportement livré                                         | Les composants et leurs tests                 |

Séparer dans les tokens les valeurs de base, comme une teinte, et leurs rôles, comme le fond d’un écran. Quand un rôle change, modifier le token sémantique dans Git, puis mettre à jour la variable Figma et les éventuelles copies dans `DESIGN.md` et le code. Le format DTCG décrit les valeurs et leurs références. La synchronisation doit être effectuée et vérifiée par l’équipe ou par son outillage. [Spécification DTCG](https://www.designtokens.org/tr/drafts/format/)

Dans MAE, **« La mémoire d’éléphant »** est la direction d’identité approuvée dans `BRAND.md`. Lors du déploiement, vérifier que chaque valeur approuvée a bien été reportée dans les tokens avant de la propager à une bibliothèque Figma.

## 3. Connecter Figma au projet

Le [[Figma MCP]] distant utilise `https://mcp.figma.com/mcp`. Pour Claude Code, fusionner cette déclaration dans le fichier `.mcp.json` à la racine. [Configuration du serveur distant Figma](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)

```json
{
  "mcpServers": {
    "figma": {
      "type": "http",
      "url": "https://mcp.figma.com/mcp"
    }
  }
}
```

Pour Codex CLI, ajouter la déclaration équivalente dans `.codex/config.toml`.

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
```

- **Claude Code** — démarrer depuis la racine du dépôt, approuver le serveur si l’agent le demande, puis ouvrir `/mcp`, choisir `figma` et lancer l’authentification. Revenir dans `/mcp` pour vérifier la connexion. [Configuration Figma pour Claude Code](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/#claude-code)
- **Codex CLI** — ouvrir le dépôt et lui accorder la confiance nécessaire pour charger sa configuration locale. Depuis sa racine, exécuter les commandes suivantes, puis démarrer une session dans ce dossier. [Configuration Figma pour Codex](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/#codex)

```bash
codex mcp login figma
codex mcp list
```

L’accès au serveur s’autorise avec le compte Figma de chaque personne. Pour modifier le canvas, vérifier que ce compte a le droit de modifier le fichier et que l’offre et le client utilisés donnent accès à cette fonction. Pour les premiers essais, utiliser un fichier de test ou une copie adaptée à l’équipe. [Conditions d’accès à l’écriture dans Figma](https://developers.figma.com/docs/figma-mcp-server/write-to-canvas/)

## 4. Affecter un rôle à chaque skill

Installer les mêmes six skills dans `.claude/skills/` et `.agents/skills/`. Pour une équipe, consigner le dépôt et la révision de chaque copie afin de pouvoir reproduire l’installation ou revenir à une version connue.

| Skill                      | Déclenchement dans MAE | Travail confié                                                                                                                                 |
| -------------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| [[Figma Use]]              | Automatique            | Guider la lecture et la modification du canvas via la Plugin API. Charger la skill avant l’usage de l’outil `use_figma`.                       |
| [[FrontEnd Design]]        | Automatique            | Implémenter dans le code une direction visuelle déjà approuvée.                                                                                |
| [[Figma Generate Library]] | Manuel                 | Construire les variables, composants et variantes d’une bibliothèque Figma à partir d’une base de code existante. L’utiliser avec `figma-use`. |
| [[Impeccable]]             | Manuel                 | Lancer une critique visuelle ou un audit, puis appliquer une correction ciblée avec `polish` ou `harden` si elle a été demandée.               |
| [[UI UX Pro Max]]          | Manuel                 | Consulter les pratiques UX d’un domaine ou d’une stack. Dans MAE, les propositions restent ponctuelles et s’utilisent sans `--persist`.        |
| [[Web Design Guidelines]]  | Manuel                 | Relire le code UI et relever les écarts d’accessibilité ou d’ergonomie à vérifier sur le rendu.                                                |

Déclarer les skills manuelles avec `disable-model-invocation: true` dans leur `SKILL.md` côté Claude Code, et `policy.allow_implicit_invocation: false` dans leur `agents/openai.yaml` côté Codex. Par exemple, appeler `/impeccable critique` dans Claude Code ou `$impeccable critique` dans Codex en nommant l’écran à examiner.

Le dépôt MAE contient aussi six skills supplémentaires côté Claude Code, issues de [[UI UX Pro Max|UI/UX Pro Max]] : `brand`, `design`, `design-system`, `ui-styling`, `banner-design` et `slides`. L’installeur configure le socle commun de six skills pour les deux clients. Pour reprendre une extension, préciser son rôle dans `AGENTS.md` afin que les arbitrages d’identité, de design et de tokens restent dans les fichiers de référence.

## 5. Valider le déploiement sur un écran

1. **Vérifier les règles chargées.** Demander à l’agent où chercher l’identité, les états d’écran et les valeurs des tokens. Il doit identifier `BRAND.md`, `EXPERIENCE.md` et `design/tokens/`.
2. **Lire la maquette.** Donner le lien d’un écran de test et demander les principaux composants et les styles ou variables identifiables. Comparer la réponse à Figma avant de lancer une écriture.
3. **Tester une modification ciblée.** Dans le fichier de test, demander une petite modification, par exemple une variante d’état vide qui réutilise le composant et les variables existants. Ouvrir le résultat dans Figma et vérifier le composant, le texte et les variables liées.
4. **Faire la revue.** Comparer le résultat à l’état attendu dans `EXPERIENCE.md`. Si un écran est déjà implémenté, lancer une critique avec Impeccable et une revue du code avec Web Design Guidelines, puis vérifier les constats sur le rendu. Consigner les arbitrages dans le fichier qui en est propriétaire.

Quand une application web existe, ajouter [[Playwright]] pour tester les parcours en navigateur et `@axe-core/playwright` pour automatiser une partie des contrôles d’accessibilité. Storybook peut servir à examiner les états de composants en isolation, avec son addon d’accessibilité. MAE prévoit ces outils dans son README comme options pour le dépôt applicatif. [Tests d’accessibilité avec Playwright](https://playwright.dev/docs/accessibility-testing) · [Tests d’accessibilité avec Storybook](https://storybook.js.org/docs/writing-tests/accessibility-testing)

### Dépannage

| Symptôme                                        | Vérification                                                                                                                                                    |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Figma n’apparaît pas dans l’agent.              | Vérifier le dossier de lancement, l’emplacement du fichier de configuration et son chargement. Côté Claude Code, vérifier l’approbation du serveur dans `/mcp`. |
| La lecture fonctionne, mais l’écriture échoue.  | Vérifier les droits d’édition du compte sur le fichier cible et l’accès du client à l’écriture sur le serveur distant.                                          |
| Une skill est introuvable.                      | Vérifier la présence de son `SKILL.md` sous `.claude/skills/` ou `.agents/skills/`, puis redémarrer la session.                                                 |
| Impeccable est détecté, mais son moteur manque. | Dans un clone de MAE disposant déjà des fichiers versionnés, relancer `bash ./install-ux-stack.sh .` pour installer le binaire correspondant au poste.          |
| Une variable Figma diffère du token.            | Comparer le token sémantique, sa valeur de base et la variable liée dans Figma, puis synchroniser depuis la référence DTCG.                                     |

Pour partager le contexte produit et design avec les dépôts d’implémentation, voir [[Architecture multi-repos et harnais Claude Code]].
