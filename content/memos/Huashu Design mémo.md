---
title: "Huashu Design — Mémo"
type: memo
fiche: "[[Huashu Design]]"
date: 2026-09-25
---

# Huashu Design — Mémo

> L'essentiel pour utiliser [[Huashu Design]], la skill qui transforme Claude Code, Codex ou Cursor en studio de design : prototypes d'app cliquables, présentations (HTML et PPTX éditable), animations exportées en MP4/GIF, infographies, revue de design. Tout se pilote en langage naturel.

## Installation

```bash
npx skills add alchaincyf/huashu-design
```

**Vérifier l'installation** : le dossier installé (ex. `~/.claude/skills/huashu-design/`) doit contenir `references/`, `assets/`, `scripts/` et `demos/`, pas seulement `SKILL.md`. Sinon, ton CLI `skills` est trop ancien (bug corrigé en 1.5.19) :

```bash
npm i -g skills@latest
# ou, en dernier recours
git clone https://github.com/alchaincyf/huashu-design.git ~/.claude/skills/huashu-design
```

## Ce qu'on peut demander

|Livrable|Exemple de demande|Durée indicative|
|---|---|---|
|Prototype d'app ou de site|« Fais un prototype iOS d'une app Pomodoro, 4 écrans cliquables »|10–15 min|
|Présentation|« Fais une présentation sur la psychologie de l'IA, propose-moi 3 directions de style »|15–25 min|
|Animation|« Transforme cette logique en animation de 60 s, exporte en MP4 et GIF »|8–12 min|
|Variantes de design|« Montre 3 variantes côte à côte de cette page »|10 min|
|Infographie|« Fais une infographie imprimable de ces données, export PDF »|10 min|
|Conseil de direction|« Je ne sais pas quel style choisir » → 3 propositions visuelles réelles|5 min|
|Revue de design|« Fais une revue en 5 dimensions de ce design »|3 min|

## Les mécanismes à connaître

|Mécanisme|Ce qu'il fait|
|---|---|
|**Protocole de marque**|Dès qu'une marque est citée : demande la charte, cherche la page brand officielle, télécharge les assets, extrait les vraies couleurs, écrit `brand-spec.md`. Ne devine jamais une couleur de marque de mémoire.|
|**Conseiller de direction**|Si le besoin est flou : 3 approches en parallèle (tirage aléatoire parmi 60 styles, référence à un site primé, philosophie d'un grand studio), chacune avec un vrai visuel.|
|**Workflow « junior designer »**|Pose ses questions en une fois, montre tôt des blocs gris et ses hypothèses, puis itère : contenu, variantes, réglages.|
|**Revue en 5 dimensions**|Cohérence, hiérarchie visuelle, exécution, fonctionnalité, innovation (0–10 chacune), avec une liste « garder / corriger / gains rapides ».|

## Scripts d'export fournis

|Script|Rôle|
|---|---|
|`render-video.js`|HTML vers MP4.|
|`convert-formats.sh`|MP4 vers 60 fps et GIF optimisé.|
|`add-music.sh`|Ajoute une musique de fond.|
|`export_deck_pptx.mjs` / `html2pptx.js`|Présentation HTML vers PowerPoint avec de vraies zones de texte éditables.|
|`export_deck_pdf.mjs`|Présentation vers PDF.|

L'agent les appelle lui-même ; il suffit de demander le format voulu.

## Conseils d'utilisation

- **Fournir ses assets de marque** (logo, couleurs, captures) : sans eux, la qualité baisse nettement, de l'aveu même de l'auteur.
- **Demander plusieurs directions** quand le style n'est pas fixé, et choisir sur les visuels plutôt que sur une description.
- **Valider les premières étapes** : l'agent montre tôt une ébauche, c'est le moment le moins cher pour corriger la direction.
- **Limites** : pas de 3D, de physique ni de particules complexes ; pas d'export en calques éditables vers Figma.
- **Données locales** : le rendu et les exports tournent en local. Les fonctions cloud (voix off, revue vidéo par IA) sont optionnelles et demandent ta propre clé.

## Sources

- [README Huashu Design (anglais)](https://github.com/alchaincyf/huashu-design/blob/master/README.en.md)
- [Huashu Design — Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/1161/huashu-design-claude-code-skill-chinese)
- [Huashu Design — PyShine](https://pyshine.com/Huashu-Design-HTML-Native-Design-Skill-Claude-Code/)
