---
title: "LLM Council — Mémo"
type: memo
fiche: "[[LLM Council]]"
date: 2026-09-25
---

# LLM Council — Mémo

> L'essentiel pour utiliser [[LLM Council]], la skill qui soumet une décision difficile à cinq « conseillers » aux angles différents dans Claude Code. Ils se relisent anonymement, puis un président rend un verdict. La méthode est adaptée du LLM Council d'Andrej Karpathy.

## Installation

Pas de terminal nécessaire : demander à Claude.

```text
Please install this Claude skill for me. The SKILL.md file lives in this GitHub repo:
https://github.com/aiwithremy/claude-skills-llm-council
```

Ou télécharger le `SKILL.md` du dépôt et demander à Claude de l'installer. Fonctionne dans Claude Code et Claude Cowork.

## Phrases qui déclenchent le conseil

|Phrase|Exemple|
|---|---|
|`council this`|« council this: dois-je passer d'une formation à 297 $ à un atelier live à 97 $ ? »|
|`run the council on …`|« run the council on mes trois angles de positionnement »|
|`pressure-test this` / `stress-test this`|Sur un texte de landing page, un plan, un pitch|
|`war room this` / `debate this`|Sur une décision risquée|

Aussi déclenché par « je n'arrive pas à décider », « je suis partagé entre… » quand il y a un vrai choix avec des enjeux.

## Les cinq conseillers

|Conseiller|Son angle|
|---|---|
|Le Contradicteur|Cherche ce qui va échouer, le défaut fatal.|
|Le Penseur « premiers principes »|Se demande si c'est la bonne question.|
|L'Expansionniste|Cherche le potentiel inexploité, ce qui pourrait être plus grand.|
|L'Extérieur|Aucun contexte : repère ce qui n'est évident que pour toi.|
|L'Exécutant|« D'accord, mais qu'est-ce qu'on fait lundi matin ? »|

## Déroulé d'une session

1. **Cadrage** : Claude lit le contexte disponible (`CLAUDE.md`, dossier `memory/`, fichiers cités) et reformule la question de façon neutre.
2. **Conseil** : 5 sous-agents répondent en parallèle.
3. **Revue croisée** : 5 sous-agents relisent les réponses anonymisées (A à E).
4. **Synthèse** : le président rend le verdict : points d'accord, désaccords, angles morts révélés par la revue, et une recommandation claire.

## Conseils d'utilisation

- **Réserver le conseil aux décisions coûteuses en cas d'erreur** : prix, positionnement, pivot, embauche. Inutile pour une question factuelle, une rédaction ou un résumé.
- **Donner du contexte** : chiffres, public, contraintes, essais passés. Un `CLAUDE.md` ou un dossier `memory/` bien tenu rend les avis bien plus concrets.
- **Coût élevé** : une session lance 11 appels à des sous-agents (5 avis, 5 revues, 1 synthèse). À ne pas lancer par réflexe.
- **Ne pas chercher une validation** : si tu connais déjà la réponse, le conseil risque surtout de pointer ce que tu préfères ne pas entendre. C'est voulu.
- **Question floue** : la skill pose une seule question de clarification avant de lancer le conseil.

## Sources

- [README LLM Council](https://github.com/aiwithremy/claude-skills-llm-council)
- [SKILL.md](https://github.com/aiwithremy/claude-skills-llm-council/blob/main/SKILL.md)
- [LLM Council d'Andrej Karpathy](https://github.com/karpathy/llm-council)
- [LLM Council — Oli Woodman](https://www.oliwoodman.com/claude-code/llm-council)
