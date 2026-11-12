---
title: "Humanizer — Mémo"
type: memo
fiche: "[[Humanizer]]"
date: 2026-09-25
---

# Humanizer — Mémo

> L'essentiel pour utiliser [[Humanizer]], la skill qui réécrit un texte « qui sonne IA » pour qu'il sonne humain, sans en changer le fond. Elle repère 25 tics d'écriture tirés de la page Wikipédia *Signs of AI writing*.

## Installation

```bash
# Skills CLI (tous les agents compatibles) ; sans --global = projet courant seulement
npx skills add blader/humanizer --global

# Ou plugin Claude Code (≥ 2.1.142)
/plugin marketplace add blader/humanizer
/plugin install humanizer@humanizer
```

La commande est `/humanizer` (skill) ou `/humanizer:humanizer` (plugin).

## Commandes et usages

|Usage|Comment|
|---|---|
|Réécrire un texte collé|`/humanizer` puis coller le texte|
|En langage naturel|« Humanise ce texte : … »|
|Réécrire un fichier|« Humanise la prose de `docs/launch-post.md` » : seul le texte change, pas le code, les données, le frontmatter ni les liens.|
|Imiter ta voix|`/humanizer`, puis « Voici un échantillon de mon écriture : » (2 ou 3 paragraphes), puis le texte à réécrire.|

Quand tu colles un texte, Humanizer montre une première réécriture, une courte critique de ce qui sonne encore artificiel, puis la version finale.

## Les tics repérés (par famille)

|Famille|Exemples|
|---|---|
|Mise en scène au lieu d'affirmer|« Ce n'est pas X, c'est Y », phrases chocs en fin de paragraphe, « Plongeons dans… », objections que personne n'a soulevées|
|Rythme mécanique|Listes de trois systématiques, débuts de phrases répétés, tirets partout, empilement de nuances|
|Emphase et fausse autorité|« Véritable témoignage de… », « marquant un tournant », « Les experts pensent que… », langage publicitaire|
|Mise en forme décorative|Gras partout, titres avec emojis, « Titres En Majuscules »|
|Restes de conversation|« Excellente question ! », « J'espère que cela vous aide ! », avertissements sur les limites de connaissance|

## Conseils d'utilisation

- **Donner un échantillon de ta propre écriture** : la réécriture reprend ton rythme, ton vocabulaire et ta ponctuation.
- **Ne pas attendre d'invention** : Humanizer n'ajoute ni nom, ni chiffre, ni date, ni citation absents du texte. S'il manque un détail concret, il le demande. Fournir tes notes (dates, lieux, anecdotes) donne un texte bien plus vivant.
- **Une demande ciblée** : un texte, un public, un objectif, et ce qui ne doit pas changer.
- **Deux passes** : d'abord retirer les tics, puis resserrer pour la voix et la fidélité au fond.
- **Relire la version finale** : un texte technique doit rester neutre, un texte personnel garde ses opinions et ses particularités.
- **Pensée pour l'anglais** : la liste de mots « typiquement IA » vient de Wikipédia anglophone. Sur un texte en français, les tics de structure (triades, phrases chocs, emphase) restent pertinents ; vérifier le reste à la relecture.

## Sources

- [README Humanizer](https://github.com/blader/humanizer)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [Humanizer Skill: The Complete Guide — Agentpedia](https://agentpedia.codes/blog/humanizer-claude-code-skill-guide)
- [Using the Humanizer Skill — DeepWiki](https://deepwiki.com/blader/humanizer/2.2-using-the-humanizer-skill)
