---
title: Taxonomie
type: guide
description: "Les classements du wiki : familles, formats, métiers et thèmes, avec leurs définitions et leurs règles d'attribution."
modified: 2026-11-20
---

# Taxonomie

Chaque outil du wiki est décrit selon trois axes indépendants, chacun avec une liste fermée de valeurs :

| Axe | Question du lecteur | Valeurs | Où il est noté |
|---|---|---|---|
| **Famille** | Que fait cet outil, à quoi le comparer ? | 17 familles, **une seule** par outil | le dossier de la fiche, `outils/<identifiant>/` |
| **Format** | Qu'est-ce que j'installe concrètement ? | 10 formats, un seul par outil | champ `format` |
| **Métier** | Qu'est-ce qui sert à mon équipe ? | 6 métiers, de 1 à 3 par outil | tags `metier/…` |

Les **thèmes** transverses (sécurité, MCP, vidéo…) complètent ces axes : de 0 à 4 par outil, en tags `theme/…`.

Les notes ★ sont définies à part, dans le [[Comparatif global des outils]].

## Familles

La famille regroupe les outils qui se comparent entre eux. Les familles sont rangées en trois zones.

### Le poste de travail de l'agent

| Famille | Identifiant | Ce qu'elle regroupe |
|---|---|---|
| [[outils/agents-de-developpement/index\|Agents de développement]] | `agents-de-developpement` | Agents complets qui lisent un dépôt, modifient le code et exécutent des commandes ; ils servent de socle aux autres outils. |
| [[outils/postes-de-pilotage/index\|Postes de pilotage multi-agent]] | `postes-de-pilotage` | Applications et terminaux qui font travailler plusieurs agents en parallèle, chacun sur sa branche, avec un point de revue commun. |
| [[outils/methodes-de-developpement/index\|Méthodes de développement]] | `methodes-de-developpement` | Processus prêts à l'emploi (clarification, plan, tests, revue) qui encadrent le travail d'un agent. |
| [[outils/orchestration-et-catalogues/index\|Orchestration et catalogues d'agents]] | `orchestration-et-catalogues` | Couches qui coordonnent plusieurs agents, et bibliothèques de rôles, d'agents ou de skills où piocher. |
| [[outils/memoire-et-contexte/index\|Mémoire et contexte]] | `memoire-et-contexte` | Outils qui conservent ou structurent ce que l'agent sait d'un projet, d'une session à l'autre. |

### Construire et livrer

| Famille | Identifiant | Ce qu'elle regroupe |
|---|---|---|
| [[outils/revue-et-securite/index\|Revue, sécurité et création de skills]] | `revue-et-securite` | Contrôle de la qualité du code et des extensions produits avec un agent. |
| [[outils/navigateur-et-tests/index\|Navigateur et tests]] | `navigateur-et-tests` | Pilotage d'un navigateur ou d'une application par l'agent, pour tester, diagnostiquer ou automatiser. |
| [[outils/backend-et-deploiement/index\|Backend, authentification et déploiement]] | `backend-et-deploiement` | Services et bibliothèques sur lesquels on construit et met en ligne une application. |
| [[outils/prototypage-en-ligne/index\|Prototypage en ligne]] | `prototypage-en-ligne` | Applications web qui génèrent une interface ou une mini-application à partir d'une description. |
| [[outils/design-en-code/index\|Design en code]] | `design-en-code` | Outils pour concevoir des interfaces dans le code et relier leur implémentation aux maquettes et bibliothèques de design. |
| [[outils/modeles/index\|Modèles]] | `modeles` | Modèles d'IA spécialisés, accessibles par API ou à déployer à partir de poids téléchargeables. |

### Produire et décider

| Famille | Identifiant | Ce qu'elle regroupe |
|---|---|---|
| [[outils/automatisation-de-workflows/index\|Automatisation de workflows]] | `automatisation-de-workflows` | Moteurs d’automatisation visuelle et extensions pour concevoir, tester ou piloter leurs workflows. |
| [[outils/recherche-et-veille/index\|Recherche et veille]] | `recherche-et-veille` | Accès au web et synthèse de sources, pour l'agent ou pour l'utilisateur. |
| [[outils/marketing-et-seo/index\|Marketing et SEO]] | `marketing-et-seo` | Skills et applications pour la stratégie marketing, le contenu et le référencement. |
| [[outils/image-video-medias/index\|Image, vidéo et médias]] | `image-video-medias` | Génération d'images et de vidéos, et production vidéo programmable. |
| [[outils/ecriture-voix-messagerie/index\|Écriture, voix et messagerie]] | `ecriture-voix-messagerie` | Rédaction, dictée et traitement des e-mails. |
| [[outils/finance-juridique-decision/index\|Finance, juridique et décision]] | `finance-juridique-decision` | Workflows métier spécialisés et aides à la décision. |

## Formats

Le format décrit l'objet qu'on installe ou qu'on utilise, pas la fonction de l'outil.

| Format | Définition |
|---|---|
| `agent` | Agent autonome qui reçoit une tâche et l'exécute : lecture, édition, commandes. |
| `skill` | Un skill isolé : instructions et ressources qu'un agent charge à la demande. |
| `collection` | Ensemble de skills, d'agents, de commandes ou de plugins distribués ensemble, y compris une méthode outillée ou un plugin qui regroupe des dizaines de skills. |
| `plugin` | Plugin unique pour un agent (hooks, commandes, sous-agents), avec une fonction précise. |
| `serveur-mcp` | Serveur Model Context Protocol qui expose des outils à un agent. |
| `cli` | Outil en ligne de commande ou outil de développement local. |
| `api` | Service consommé par API, en général facturé à l'usage. |
| `bibliotheque` | Bibliothèque ou framework intégré au code d'une application. |
| `application` | Application de bureau ou web utilisée directement. |
| `plateforme` | Service cloud sur lequel on construit et héberge une application. |

## Statut

Le champ `statut` reprend ce que déclare l'éditeur ; il ne juge pas la stabilité réelle de l'outil, que mesure la note de maturité.

| Statut | Définition |
|---|---|
| `disponible` | Accessible sans mention de préversion. |
| `preversion` | Annoncé par l'éditeur comme préversion, bêta, Labs ou expérimental. La maturité est alors plafonnée à ★★ (voir le [[Comparatif global des outils]]). |
| `retire` | Produit arrêté, dépôt archivé ou introuvable. |

## Métiers

Chaque métier a sa page, avec les besoins, les outils recommandés et leurs points d'attention : [[metiers/index|Métiers]].

| Tag | Métier | Pour |
|---|---|---|
| `metier/direction` | Direction et gouvernance | Stratégie, décision, finances, organisation de l'entreprise. |
| `metier/ingenierie` | Ingénierie et développement | Concevoir, coder, tester, sécuriser, déployer et maintenir les applications. |
| `metier/produit-design` | Produit et design | Besoins utilisateurs, prototypes, cohérence de l'interface. |
| `metier/marketing-ventes` | Commercial et marketing | Marché, campagnes, contenu, référencement, déclinaison de la marque. |
| `metier/support-client` | Succès client et support | Réponses aux clients, base de connaissances, suivi de l'adoption. |
| `metier/operations` | Opérations et fonctions support | Juridique, administration, finance, RH, automatisations internes. |

## Thèmes

| Tag | Définition |
|---|---|
| `theme/contexte` | Ce que l'agent sait du projet : fichiers d'instructions, conventions, chargement du contexte. |
| `theme/memoire` | Conservation des informations d'une session à l'autre. |
| `theme/multi-agent` | Plusieurs agents qui travaillent en parallèle ou se répartissent une tâche. |
| `theme/planification` | Découpage d'une tâche en plan avant l'exécution. |
| `theme/mcp` | Outils qui exposent ou consomment des serveurs MCP. |
| `theme/navigateur` | Pilotage d'un navigateur web par un agent. |
| `theme/automatisation` | Enchaînements de tâches qui tournent sans intervention. |
| `theme/revue-de-code` | Relecture de modifications de code, par un agent ou avec son aide. |
| `theme/tests` | Tests, débogage et évaluation. |
| `theme/frontend` | Interface web côté client. |
| `theme/backend` | Serveur, base de données, API. |
| `theme/design-system` | Cohérence visuelle et composants d'interface. |
| `theme/accessibilite` | Accessibilité des interfaces. |
| `theme/securite` | Sécurité applicative, authentification, garde-fous. |
| `theme/recherche` | Recherche d'information et synthèse de sources. |
| `theme/seo` | Référencement naturel. |
| `theme/image` | Génération ou retouche d'images. |
| `theme/video` | Génération ou production de vidéos. |
| `theme/voix` | Dictée, audio et voix. |
| `theme/redaction` | Écriture et révision de textes. |
| `theme/deploiement` | Hébergement, mise en ligne, intégration continue. |
| `theme/extraction-donnees` | Extraction et structuration de données issues du web ou de documents. |

## Règles d'attribution

- **Famille** : une seule ; elle donne le dossier de la fiche, et l'outil est noté et comparé dans la page de cette famille.
- **Format** : un seul, l'objet installé. Un plugin qui regroupe des dizaines de skills est une `collection`.
- **Métiers** : de 1 à 3, parmi les pages métier où l'outil figure.
- **Thèmes** : de 0 à 4, seulement si le thème décrit un usage direct de l'outil. Un thème ne double pas une famille : il n'y a pas de thème « finance » ou « juridique ».
- **Aucun tag hors de ces listes.** Pour ajouter une valeur, modifier d'abord cette page, puis les fiches.
- Le champ `type` décrit la page, pas l'outil (voir ci-dessous).

## Types de pages

| `type` | Page | Emplacement |
|---|---|---|
| `outil` | Fiche d'un outil, avec sa synthèse des avis | `outils/<famille>/` |
| `memo` | Mémo pratique d'un outil | `memos/` |
| `famille` | Page d'une famille : outils, notes, critères | `outils/<famille>/index.md` |
| `metier` | Page d'un métier : besoins, outils, points d'attention | `metiers/` |
| `concept` | Définition d'une notion | `concepts/` |
| `guide` | Guide transversal ou page de méthode | `guides/`, `methode/` |
| `index` | Page d'accueil ou de section | `index.md` de chaque dossier |
| `tag` | Description d'un tag | `tags/` |

_Dernière analyse : 20 novembre 2026_
