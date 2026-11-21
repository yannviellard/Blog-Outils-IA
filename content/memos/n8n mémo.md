---
title: "n8n — Mémo"
type: memo
fiche: "[[n8n]]"
date: 2026-11-20
---

# n8n — Mémo

> Démarrer une instance locale et vérifier un workflow avant sa publication.

## Installation

n8n Cloud ouvre directement l’éditeur. Pour un essai local avec Docker et un volume de données persistant, exécuter ces commandes puis ouvrir `http://localhost:5678`.

```bash
docker volume create n8n_data
docker run -it --rm --name n8n \
  -p 127.0.0.1:5678:5678 \
  -e GENERIC_TIMEZONE="Europe/Paris" \
  -e TZ="Europe/Paris" \
  -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true \
  -v n8n_data:/home/node/.n8n \
  n8nio/n8n
```

## Commandes principales

|Dans l’éditeur|Usage|
|---|---|
|Manual Trigger|Démarrer explicitement un premier essai.|
|Edit Fields (Set)|Définir et mapper les champs.|
|Execute workflow|Exécuter le brouillon manuellement.|
|Pin data|Réutiliser la sortie d’un nœud en test.|
|Executions|Consulter l’historique.|
|Publish|Mettre la version courante en service.|

## Conseils d’utilisation

- Tester avec une entrée valide, une entrée incomplète et un doublon.
- Configurer les identifiants dans n8n. Garder le volume persistant et sauvegarder les données ainsi que la clé de chiffrement.
- Pour un flux planifié, contrôler le fuseau du workflow et examiner sa première exécution après publication.

## Sources

- [Installation Docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker.md)
- [Premier workflow](https://docs.n8n.io/build-your-first-workflow.md)
- [Épinglage des données](https://docs.n8n.io/data/data-pinning/)
