---
title: "Playwright — Mémo"
type: memo
fiche: "[[Playwright]]"
date: 2026-10-11
---

# Playwright — Mémo

> Les commandes à connaître pour écrire, lancer et déboguer des tests avec [[Playwright]], puis le brancher à un agent de code via le CLI dédié ou le serveur MCP.

## Installation

```bash
npm init playwright@latest        # nouveau projet (yarn create playwright, pnpm create playwright)
npx playwright install --with-deps  # installer ou mettre à jour les navigateurs
npm install -D @playwright/test@latest   # mettre à jour la bibliothèque
```

## Lancer les tests

|Commande|Ce qu'elle fait|
|---|---|
|`npx playwright test`|Lance tous les tests.|
|`npx playwright test tests/login.spec.ts`|Limite aux fichiers qui correspondent au motif.|
|`npx playwright test -g "connexion"`|Ne lance que les tests dont le titre correspond à l'expression.|
|`npx playwright test --project chromium`|Ne lance qu'un projet (navigateur) nommé.|
|`npx playwright test --headed`|Exécute dans des navigateurs visibles.|
|`npx playwright test --ui`|Mode UI interactif.|
|`npx playwright test --debug`|Ouvre le Playwright Inspector.|
|`npx playwright test -j 1` (`--workers`)|Nombre de workers ; `1` désactive le parallélisme.|
|`npx playwright test --retries 2`|Nombre maximal de relances d'un test instable.|
|`npx playwright test --reporter html`|Choisit le ou les reporters (séparés par des virgules).|
|`npx playwright test --last-failed`|Relance seulement les échecs précédents.|
|`npx playwright test -x` (`--max-failures`)|S'arrête après N échecs.|
|`npx playwright test --list`|Liste les tests sans les exécuter.|
|`npx playwright test --shard 1/3`|Exécute un fragment de la suite (CI).|
|`npx playwright test --forbid-only`|Échoue si `test.only` est présent (utile en CI).|
|`npx playwright test -u` (`--update-snapshots`)|Met à jour les captures de référence.|

## Outils

|Commande|Ce qu'elle fait|
|---|---|
|`npx playwright codegen [url]`|Enregistre les actions et génère du code de test.|
|`npx playwright show-report`|Sert le rapport HTML du dernier run (port 9323 par défaut).|
|`npx playwright show-trace trace.zip`|Ouvre le Trace Viewer sur une trace.|
|`npx playwright merge-reports <dossier>`|Fusionne des rapports « blob » (tests découpés en shards).|
|`npx playwright install-deps`|Installe les dépendances système des navigateurs.|
|`npx playwright clear-cache`|Vide les caches de Playwright.|

## Pour un agent de code

**CLI pour agents** (commandes concises, peu de contexte) :

```bash
npm install -g @playwright/cli@latest
playwright-cli install --skills        # skills installables (-g : partagées entre projets)
playwright-cli open https://example.com
playwright-cli snapshot                # page avec références d'éléments
playwright-cli click <ref>
playwright-cli fill <ref> "texte"
playwright-cli screenshot --filename=page.png
playwright-cli close
```

Sessions persistantes : `playwright-cli open <url> -s=nom --persistent`, `playwright-cli list`, `playwright-cli close-all`. Sans `--persistent`, le profil est perdu à la fermeture ; une session headless s'arrête après une heure sans commande.

**Serveur MCP** :

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

Options utiles du serveur : `--headless`, `--browser=chrome|firefox|webkit|msedge`, `--isolated` (session neuve), `--user-data-dir`, `--extension` (onglets du navigateur existant), `--config <fichier>`.

## Conseils d'utilisation

- **Playwright pour le déterminisme, DevTools pour le diagnostic** : voir [[Chrome DevTools MCP]] pour déboguer un échec réseau ou de performance.
- **Concevoir données, sélecteurs et CI avec soin** : Playwright ne supprime pas l'instabilité due à de mauvaises données.
- **Utiliser `--forbid-only` et `--shard` en CI**, et conserver traces et rapports comme artefacts.
- **Préférer le CLI au MCP pour un agent de code** quand la consommation de contexte compte ; le MCP convient aux sessions exploratoires avec état.

## Sources

- [Playwright — ligne de commande des tests](https://playwright.dev/docs/test-cli)
- [Playwright — installation](https://playwright.dev/docs/intro)
- [Playwright — CLI pour agents de code](https://playwright.dev/docs/getting-started-cli)
- [Playwright — serveur MCP](https://playwright.dev/docs/getting-started-mcp)
