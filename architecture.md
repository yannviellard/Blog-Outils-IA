# Proposition d'architecture — AI Tools Wiki

_Proposition du 10 novembre 2026, établie après une passe complète sur `content/`. Mise à jour le 11 novembre 2026 avec les décisions prises (§ 14) et le bilan des phases 2 et 3, puis le 12 novembre 2026 avec le bilan des phases 4 et 6 (§ 13)._

## 1. Bilan de la passe

**Inventaire** : 70 fiches d'outils, 1 guide, 70 avis, 60 mémos, l'index, le comparatif global, le gabarit et deux fichiers vides (`Design.md`, supprimé depuis, et `Subagents.md`).

**Ce qui tient** :

- la liste de contrôle de `CLAUDE.md` passe entièrement : aucune fiche sans avis, aucun mémo manquant hors `SANS_MEMO`, toutes les fiches sont dans l'index et le comparatif, aucun artefact de citation ;
- le barème unique, justifié ligne à ligne, est un vrai point fort pour un site public ;
- les tableaux « par secteur » de l'index, avec leur colonne « Point d'attention », ont une valeur éditoriale propre ;
- les avis sont sourcés et signalent la partialité des sources.

**Ce qui pose problème** :

| # | Constat | Exemple ou chiffre | Conséquence |
|---|---|---|---|
| 1 | **Six classements se chevauchent sans correspondre** : `type` (14 valeurs), tags, tableau « Domains », index « par secteur » (6), index « par nature » (8 sections), familles du comparatif (14, A à N). | `agent-orchestrator` regroupe Ruflo (famille C), AI Berkshire (H) et quatre postes de pilotage (N). `platform` regroupe Vercel, Warp, Stitch et Banana Prompts. Graphify est « Connecteurs » dans l'index mais « Mémoire » dans le comparatif ; Playwright est « Frameworks » d'un côté, « Navigateur et tests » de l'autre. | Le lecteur ne sait pas quel classement fait foi ; chaque ajout demande de trancher trois fois. |
| 2 | **Ajouter un outil demande cinq saisies manuelles** dans deux longs fichiers. | Index par secteur, index par nature, compteur final, notes du comparatif, critères du comparatif ; puis recopie des notes dans la fiche. | Risque de divergence (la règle « notes identiques » ne tient que par discipline). |
| 3 | **Pages d'entrée trop longues pour un site** (corrigé en phase 4 : accueil court, pages de famille et de métier). | Index : 238 lignes, 14 tableaux. Comparatif : 382 lignes, deux tableaux par famille. | Lecture difficile, surtout sur mobile. |
| 4 | **Tags non contrôlés** (corrigé en phase 2 : 28 tags définis dans `Taxonomie`). | 97 tags distincts pour 70 fiches, dont 42 utilisés une seule fois. Synonymes : `automation/workflow` / `automation/workflows`, `security/application` / `security/application-security`, `agent-engineering/tooling` / `agent-engineering/tool-integration`, `automation/browser` / `development/browser-automation`, `content-creation/video` / `media/video-generation`, `agent-engineering/orchestration` / `development/agent-orchestration`. | Quartz crée une page par tag : environ cent pages, la plupart avec une seule entrée. |
| 5 | **Aucune page de concepts** (corrigé en phase 4 : 8 pages dans `concepts/`). | 135 cibles de liens manquantes (185 occurrences). MCP apparaît sous trois graphies (9 occurrences) ; `Skills`, `Hooks`, `Plugins`, `Claude` sont liés sans page ; `Subagents.md` existe mais est vide. | Le vocabulaire de base (skill, plugin, MCP, harnais, worktree) n'est expliqué nulle part. |
| 6 | **Liens vers des fiches existantes sous un autre nom** (corrigé en phase 1). | `[[Codex]]`, `[[gstack]]`, `[[everything-claude-code]]`, `[[Google Stitch]]`, `[[Frontend Design]]`. | Ces liens s'affichaient comme des pages à écrire. |
| 7 | **Gabarit inégalement appliqué** (corrigé en phases 1 et 4 : tableaux d'en-tête et « Domains » supprimés). | 38 fiches sans ligne « Voir aussi », 22 incomplètes (corrigé en phase 1). Tableau « Domains » absent de 3 fiches et de sens variable ailleurs. En-têtes en anglais (Website, Repository, Stars, Domains) sur un site francophone. | Fiches peu homogènes d'une page à l'autre. |
| 8 | **Pas de date dans le frontmatter des fiches** (corrigé en phase 2 : `modified`, `derniere_maj`, `etoiles_releve`). | Seule la ligne `_Dernière analyse : …_` en pied de page. | Quartz ne peut ni afficher la date ni alimenter « Notes récentes ». |
| 9 | **206 fichiers à plat** (corrigé en phase 4 : sous-dossiers). | Trois fichiers par outil, triés par ordre alphabétique. | L'explorateur latéral de Quartz serait illisible. |

## 2. Principe : un axe, un endroit

Remplacer les six classements par **trois axes indépendants**, chacun stocké à un seul endroit.

| Axe | Question du lecteur | Valeurs | Où il est stocké | Ce qui l'affiche |
|---|---|---|---|---|
| **Famille** | « Que fait cet outil, à quoi le comparer ? » | 17 familles, **une seule** par outil | le **dossier** de la fiche | la page de la famille (`index.md` du dossier) et l'explorateur |
| **Métier** | « Qu'est-ce qui sert à mon équipe ? » | 6 métiers, plusieurs possibles | tags `metier/…` | les pages métier et les pages de tag |
| **Format** | « Qu'est-ce que j'installe concrètement ? » | 10 formats | champ `format` | une colonne des tableaux, le panneau de propriétés |

Les **thèmes transverses** (sécurité, MCP, vidéo…) restent possibles en tags `theme/…`, sur une liste fermée d'une vingtaine de valeurs définies.

## 3. Familles

Les familles du comparatif sont déjà le classement le plus fin et le mieux justifié : elles deviennent l'unique classement « par nature » et donnent les sous-dossiers de `outils/`. Elles sont regroupées en trois zones pour l'accueil et perdent leurs lettres A à N.

Décidé le 11 novembre 2026 : « Design et UI » est scindée en deux familles, et une famille « Modèles » est créée pour Jev et Nano Banana, deux modèles propriétaires accessibles par API. On passe de 14 à 16 familles. Le 20 novembre 2026, la famille « Automatisation de workflows » porte le total à 17.

### Zone 1 — Le poste de travail de l'agent

| Famille | Outils |
|---|---|
| Agents de développement | Claude Code, OpenAI Codex, OpenCode, Hermes Agent |
| Postes de pilotage multi-agent | Superset, Conductor, Parallel Code, Claude Squad, cmux, Warp |
| Méthodes de développement | Superpowers, GStack, BMAD Method, Planning with Files, Everything Claude Code |
| Orchestration et catalogues d'agents | Ruflo, Oh My Claude, Agency Agents, Wshobson Agents, Alirezarezvani Claude Skills |
| Mémoire et contexte | Claude-Mem, MemPalace, Graphify |

### Zone 2 — Construire et livrer

| Famille | Outils |
|---|---|
| Revue, sécurité et création de skills | Claude Code Review, Security Guidance, Skill Creator |
| Navigateur et tests | Playwright, Agent Browser, Chrome DevTools MCP, OpenCLI |
| Backend, authentification et déploiement | Supabase, Better Auth, Vercel |
| Prototypage en ligne | Claude Design, Stitch by Google, Opal by Google |
| Design en code | FrontEnd Design, Huashu Design, Impeccable, Taste Skill, UI UX Pro Max, Web Design Guidelines, shadcn-ui |
| Modèles | Jev, Nano Banana |

### Zone 3 — Produire et décider

| Famille | Outils |
|---|---|
| Recherche et veille | Firecrawl, Agent Reach, Perplexity MCP, Gemini Deep Research, NotebookLM |
| Marketing et SEO | Ai-Marketing-Claude, Marketing Skills from Corey Haines, Claude SEO, OpenClaudia, Pomelli |
| Image, vidéo et médias | Banana Prompts, Glif MCP, Higgsfield-ai-platform, Higgsfield-skills, Open Generative AI, Remotion, HyperFrames |
| Écriture, voix et messagerie | Humanizer, Wispr Flow, Agentic Inbox |
| Finance, juridique et décision | Claude for Financial Services, Claude for Legal, Small Business, AI Berkshire, LLM Council |

Total : 70 outils, chacun dans une seule famille.

**Remarques** :

- **Modèles** compte deux outils qui ne se comparent pas directement (décisions typées pour Jev, images pour Nano Banana) ; la famille a vocation à accueillir d'autres modèles. Nano Banana y est rangé parce que sa fiche le présente comme une famille de modèles ; il reste cité dans la page « Image, vidéo et médias ».
- **LLM Council** est aujourd'hui « Orchestration » dans l'index et « Décision » dans le comparatif ; la proposition retient « Décision ».

## 4. Formats (remplace l'actuel `type` des fiches)

Le champ `type` mélange aujourd'hui la nature de la page (`review`, `cheatsheet`, `guide`, `index`) et le format de l'outil (`skill`, `platform`…). Proposition : `type` décrit **la page** partout (`outil`, `memo`, `famille`, `metier`, `concept`, `guide`, `index`) et un nouveau champ `format` décrit **ce qu'on installe**.

| Format | Ce que c'est | Anciennes valeurs de `type` |
|---|---|---|
| `agent` | Agent autonome qui exécute des tâches | `agent-harness` |
| `skill` | Un skill isolé | `skill` |
| `collection` | Ensemble de skills, agents, commandes ou plugins | `skill-collection`, `plugin-catalog`, `agent-collection`, `methodology` |
| `plugin` | Plugin unique (hooks, commandes, sous-agents) | `plugin` |
| `serveur-mcp` | Serveur MCP | `mcp-server` |
| `cli` | Outil en ligne de commande ou outil de développement local | `developer-tool` |
| `api` | Service consommé par API | `api-service` |
| `bibliotheque` | Bibliothèque ou framework de code | `library-framework` |
| `application` | Application de bureau ou web utilisée directement | `application`, une partie de `platform` |
| `plateforme` | Service cloud sur lequel on construit (backend, hébergement) | une partie de `platform` |

**Cas à trancher** (le format actuel décrit la fonction plutôt que l'objet installé) :

- `agent-orchestrator` (7) : Superset, Conductor, Parallel Code → `application` ; Claude Squad → `cli` ; Ruflo, Oh My Claude → `cli` ou `collection` ; AI Berkshire → `collection`.
- `platform` (7) : Supabase, Vercel → `plateforme` ; Warp, Stitch, Opal, Banana Prompts, Higgsfield-ai-platform → `application`.
- `plugin` regroupant des dizaines de skills (Small Business, Everything Claude Code) → `collection`.
- cmux (`developer-tool`) → `application` ; MemPalace (`application`) → à vérifier (`cli` + serveur MCP).

## 5. Métiers et thèmes (tags en français)

**Décidé** : tags en français. Les identifiants restent sans accents ni espaces (URL propres : `/tags/metier/ingenierie`) ; les libellés accentués et la définition de chaque tag vont dans sa page de description (`content/tags/…`).

**Métiers** (repris des six secteurs de l'index) : `metier/direction`, `metier/ingenierie`, `metier/produit-design`, `metier/marketing-ventes`, `metier/support-client`, `metier/operations`.

**Thèmes** (liste fermée) :

| Thème | Remplace notamment |
|---|---|
| `theme/contexte` | `agent-engineering/context` |
| `theme/memoire` | `agent-engineering/memory`, `knowledge-management` |
| `theme/multi-agent` | `agent-engineering/orchestration`, `development/agent-orchestration` |
| `theme/planification` | `agent-engineering/planning` |
| `theme/mcp` | `mcp/server`, `agent-engineering/tool-integration`, `agent-engineering/tooling` (pour les outils qui exposent ou consomment MCP) |
| `theme/navigateur` | `automation/browser`, `development/browser-automation`, `automation/web-scraping` |
| `theme/automatisation` | `automation/workflow`, `automation/workflows` |
| `theme/revue-de-code` | `development/code-review` |
| `theme/tests` | `development/testing`, `development/debugging` |
| `theme/frontend` | `development/frontend`, `code-generation/frontend` |
| `theme/backend` | `development/backend`, `data/database` |
| `theme/design-system` | `design/ui`, `design/ux`, `design/design-system` |
| `theme/accessibilite` | `design/accessibility`, `development/accessibility` |
| `theme/securite` | `security/*` |
| `theme/recherche` | `research/*`, `productivity/research` |
| `theme/seo` | `marketing/seo` |
| `theme/image` | `content-creation/image`, `media/image-generation`, `design/image-editing` |
| `theme/video` | `content-creation/video`, `media/video-generation` |
| `theme/voix` | `content-creation/audio`, `productivity/dictation` |
| `theme/redaction` | `content-creation/writing`, `content-creation/editing`, `marketing/copywriting` |
| `theme/deploiement` | `infrastructure/*` |
| `theme/extraction-donnees` | `data/extraction`, `data/classification` |

Les tags `finance/…`, `legal/…`, `business/…` sont couverts par la famille « Finance, juridique et décision » et les tags métier. Règle : 1 à 3 tags métier, 1 à 4 thèmes, aucun tag hors liste.

## 6. Arborescence du site

**Décidé** : rangement en sous-dossiers. Proposition : un sous-dossier **par famille** dans `outils/`, à faire **avant la première mise en ligne**.

```
content/
├── index.md                                  Accueil : 3 zones, 6 métiers, notes récentes
│
├── outils/
│   ├── index.md                              « Tous les outils » : les 17 familles par zone
│   ├── agents-de-developpement/
│   │   ├── index.md                          Page de la famille : lecture, comment choisir, critères, notes ★
│   │   ├── Claude Code.md                    Fiche complète, avis intégré
│   │   ├── Hermes Agent.md
│   │   ├── OpenAI Codex.md
│   │   └── OpenCode.md
│   ├── postes-de-pilotage/                   Superset, Conductor, Parallel Code, Claude Squad, cmux, Warp
│   ├── methodes-de-developpement/            Superpowers, GStack, BMAD Method, Planning with Files, Everything Claude Code
│   ├── orchestration-et-catalogues/          Ruflo, Oh My Claude, Agency Agents, Wshobson Agents, Alirezarezvani Claude Skills
│   ├── memoire-et-contexte/                  Claude-Mem, MemPalace, Graphify
│   ├── revue-et-securite/                    Claude Code Review, Security Guidance, Skill Creator
│   ├── navigateur-et-tests/                  Playwright, Agent Browser, Chrome DevTools MCP, OpenCLI
│   ├── backend-et-deploiement/               Supabase, Better Auth, Vercel
│   ├── prototypage-en-ligne/                 Claude Design, Stitch by Google, Opal by Google
│   ├── design-en-code/                       FrontEnd Design, Huashu Design, Impeccable, Taste Skill, UI UX Pro Max, Web Design Guidelines, shadcn-ui
│   ├── modeles/                              Jev, Nano Banana
│   ├── automatisation-de-workflows/          n8n, n8n MCP officiel et skills
│   ├── recherche-et-veille/                  Firecrawl, Agent Reach, Perplexity MCP, Gemini Deep Research, NotebookLM
│   ├── marketing-et-seo/                     Ai-Marketing-Claude, Marketing Skills…, Claude SEO, OpenClaudia, Pomelli
│   ├── image-video-medias/                   Banana Prompts, Glif MCP, Higgsfield (×3), Remotion, HyperFrames
│   ├── ecriture-voix-messagerie/             Humanizer, Wispr Flow, Agentic Inbox
│   └── finance-juridique-decision/           Claude for Financial Services, Claude for Legal, Small Business, AI Berkshire, LLM Council
│
├── memos/
│   ├── index.md                              Bibliothèque des mémos, tous téléchargeables
│   ├── Claude Code mémo.md                   Source vérifiée, consultable en page web
│   ├── Claude Code mémo.pdf                  Généré : une page A4
│   ├── Claude Code mémo.png                  Généré : aperçu affiché dans la fiche
│   └── …                                     (60 mémos)
│
├── metiers/
│   ├── index.md
│   ├── Direction et gouvernance.md           Tableaux « Besoin / Outils / Point d'attention » de l'index
│   ├── Ingénierie et développement.md
│   ├── Produit et design.md
│   ├── Commercial et marketing.md
│   ├── Succès client et support.md
│   └── Opérations et fonctions support.md
│
├── concepts/
│   ├── index.md                              Glossaire
│   ├── Model Context Protocol.md             titre « MCP (Model Context Protocol) », alias : MCP, MCP Protocol
│   ├── Skill.md · Plugin.md · Hook.md
│   ├── Subagents.md                          titre affiché « Sous-agents »
│   └── Harnais d'agent.md · Worktree.md · Mémoire d'agent.md
│
├── guides/
│   ├── index.md
│   └── Architecture multi-repos et harnais Claude Code.md
│
├── methode/
│   ├── index.md                              À propos : ce que mesure le wiki, comment il est écrit
│   ├── Comparatif global des outils.md       Barème, règles, lecture transversale, classement global
│   └── Taxonomie.md                          Familles, formats, métiers, thèmes, avec définitions
│
├── tags/                                     Pages de description des tags (titre accentué, définition)
│   ├── metier/ingenierie.md …
│   └── theme/securite.md …
│
└── _modeles/                                 Gabarits fiche, mémo, famille, concept (exclus du site)
```

**Ce que voit le lecteur** : dans l'explorateur, Outils (17 familles repliées), Mémos, Métiers, Concepts, Guides, Méthode. Une famille ouverte liste directement ses outils : le classement par nature devient la navigation elle-même, sans tableau à maintenir.

**Conventions** :

- **Dossiers** : minuscules, sans accents, avec tirets (URL propres, ex. `/outils/agents-de-developpement/Claude-Code`) ; le titre accentué affiché vient de l'`index.md` du dossier.
- **Fiches** : noms de fichiers actuels conservés, donc les liens `[[Claude Code]]` restent valables (la configuration fournie avec Quartz 5 résout les liens par nom de fichier, `markdownLinkResolution: shortest`).
- **Mémos** : `Nom_cheatsheet.md` devient `Nom mémo.md` ; les liens sont réécrits par script.
- **Avis** : les fichiers disparaissent (voir § 8) ; l'exception historique `Hermes Agent_avis.md` disparaît avec eux.
- **Liens vers une famille** : plusieurs fichiers s'appelant `index.md`, le lien doit donner le chemin : `[[outils/agents-de-developpement/index|Agents de développement]]`.
- **Ordre des familles** dans l'explorateur : celui des zones, par un tri personnalisé (option `sortFn` de l'explorateur, dans `quartz.ts`, phase 6) ; les rubriques suivent l'ordre Outils, Mémos, Métiers, Concepts, Guides, Méthode.
- **Changer un outil de famille change son URL** : à éviter après la mise en ligne.

## 7. La fiche outil

### Frontmatter

```yaml
---
title: Claude Code
type: outil
description: Une phrase « En bref », reprise par les tableaux, la recherche et l'aperçu des liens.
format: agent
tags:
  - metier/ingenierie
  - theme/contexte
editeur: …
site: …
depot: …
licence: …
statut: disponible          # disponible | preversion | retire (ce que déclare l'éditeur)
derniere_maj: …             # date du dernier commit ou release ; absent sans dépôt
etoiles: …                  # nombre d'étoiles GitHub
forks: …                    # nombre de forks, relevé avec les étoiles
etoiles_releve: …           # date du relevé
note_documentation: 5
note_precision: 4
note_maturite: 4
note_popularite: 5          # calculée depuis `etoiles`, jamais saisie à la main
memo: "[[Claude Code mémo]]"
avis_maj: …                 # date de la dernière mise à jour de la section Avis
modified: …                 # = Dernière analyse
---
```

Posés en phase 2 sur les 70 fiches : tous les champs sauf `editeur`, `statut` et `avis_maj`, ajoutés en phase 3. En phase 4 : `famille` supprimé (c'est le dossier), `forks` ajouté (repris du relevé du 11 novembre 2026, pour repérer une hausse d'étoiles suspecte), `memo` pointe vers `[[Nom mémo]]`. Les `aliases` sont posés sur les pages de concepts ; les fiches n'en ont pas eu besoin.

### Corps, dans un ordre fixe

1. Titre et résumé d'une phrase.
2. Encadré **Verdict** : deux lignes reprises de la section Avis, pour le lecteur pressé.
3. Ligne d'accès : « Mémo : consulter · télécharger le PDF · Avis indépendants : plus bas ». Assurée depuis le 12 novembre 2026 par l'encadré « Fiche » (lignes Mémo, avec le lien PDF, et Avis).
4. `## Résumé`
5. `## Fonctionnalités`
6. `## Analyse` : les quatre notes ★, points forts, limites.
7. `## Relations`
8. `## Mémo pratique` : aperçu (image de la page du mémo) et lien de téléchargement. Insérée par le plugin `wiki-fiche` à la construction du site, sans être écrite dans le fichier (§ 9).
9. `## Avis indépendants` (voir § 8).
10. `## Sources` : sources officielles, puis sources des avis avec leur fiabilité.
11. `_Dernière analyse : …_`

### Ce qui change par rapport au gabarit actuel

- Le tableau d'en-tête anglais (Website, Repository, Stars…) est remplacé par un encadré « Fiche » alimenté par le frontmatter, avec des libellés français (plugin local `plugins/wiki-fiche/`, phase 6). Le panneau de propriétés de Quartz (NoteProperties) est masqué : il affiche les clés brutes (`note_documentation`) sous un titre « Properties » non traduit.
- **Étoiles conservées** et affichées avec leur date de relevé (« 148 k au 10 octobre 2026 ») ; elles alimentent le critère Popularité ci-dessous.
- Le tableau « Domains / Skills / Agents / MCP tools » disparaît (redondant avec familles et tags) ; une ligne « Composition » subsiste pour les collections et plugins (nombre de skills, agents, commandes, outils MCP).

### Critère Popularité (décidé le 11 novembre 2026)

Les étoiles deviennent un **quatrième critère noté**, calculé et non éditorial.

**Formule** : une étoile par ordre de grandeur, soit la partie entière de log10(étoiles), bornée entre 1 et 5. C'est ln(étoiles) / 2,3, très proche de l'idée de départ ln(étoiles) / 2.

| Étoiles GitHub | Popularité |
|---|---|
| moins de 100 | ★☆☆☆☆ |
| 100 à 999 | ★★☆☆☆ |
| 1 000 à 9 999 | ★★★☆☆ |
| 10 000 à 99 999 | ★★★★☆ |
| 100 000 et plus | ★★★★★ |

Pourquoi pas ln(étoiles) / 2 tel quel : la note arrondie atteint 5 dès 8 103 étoiles. Sur les 56 outils du wiki qui ont des étoiles, 46 auraient ★★★★★ et le critère ne départagerait presque personne. Avec log10 et le relevé du 11 novembre 2026, la répartition est de 2 outils à ★★, 8 à ★★★, 24 à ★★★★ et 17 à ★★★★★ ; 19 outils ne sont pas notés.

**Règles** :

- **Dépôt compté** : le dépôt public consacré à l'outil. Un dépôt annexe (skill, SDK, exemple) ne compte pas : Jev affichait les 2,1 k étoiles de son skill, pas celles du modèle ; le dépôt public de Stitch est son SDK. Un dépôt partagé ne compte pas non plus quand l'outil n'en est qu'un sous-dossier (Claude Code Review, FrontEnd Design, Security Guidance, Skill Creator, Small Business, Web Design Guidelines).
- **Non noté (« — »)** : 19 outils au 11 novembre 2026 : 10 sans dépôt public (Claude Design, NotebookLM, Gemini Deep Research, Pomelli, Wispr Flow…), 2 dont le lien de dépôt est mort (Opal by Google, Perplexity MCP), 6 en dépôt partagé et 1 en dépôt annexe.
- **Total** : il reste sur /15 avec les trois critères éditoriaux, et la Popularité s'affiche à côté (décidé le 11 novembre 2026). Ainsi les outils non notés en popularité restent comparables aux autres, et une note mesurée (l'audience) ne se mélange pas avec des notes de jugement (fiabilité de l'information).
- **Fraîcheur** : la note n'a de sens que si le relevé est récent. Les étoiles des 56 dépôts sont relevées par l'API publique de GitHub (60 requêtes par heure sans compte, suffisant), datées, puis mises à jour avant chaque publication.
- **Limite à signaler sur le site** : des étoiles peuvent être achetées. L'étude StarScout (Carnegie Mellon, NC State et Socket, [arXiv 2412.13459](https://arxiv.org/abs/2412.13459)) estime à environ 4,5 millions les étoiles suspectées d'être fausses sur GitHub entre 2019 et 2024. Une hausse brutale et isolée est donc à vérifier avant d'être reportée.
- Les trois autres notes restent indépendantes des étoiles : la Popularité ne fait monter ni la Documentation, ni la Précision, ni la Maturité.

## 8. Avis intégrés à la fiche

**Décidé le 11 novembre 2026 : oui.** L'avis devient la section `## Avis indépendants`, juste avant `## Sources`.

**Structure de la section** :

```
## Avis indépendants
_Synthèse des retours publiés, mise à jour le …_
### Ce qui est apprécié
### Ce qui est critiqué
### Ce qui n'est pas établi
### Comparaison
### Verdict
```

Les sources de l'avis rejoignent `## Sources`, sous « Sources des avis », avec leur fiabilité et la partialité éventuelle (éditeur, concurrent, affilié).

**Fait le 11 novembre 2026.** 57 avis sur 70 étaient rédigés en paragraphes (Synthèse, Comparaison, Verdict) et non en rubriques « apprécié / critiqué ». Pour fusionner sans perte de texte, chaque avis garde ses sections d'origine, décalées d'un niveau sous `## Avis indépendants` ; la structure cible ci-dessus s'applique aux nouveaux outils et aux avis révisés, lors du dédoublonnage famille par famille. Les 70 fichiers d'avis sont dans la Corbeille (dossier « AI Tools Wiki - avis fusionnés le 11 novembre 2026 »).

**Gains** :

- une seule page par outil : le lecteur n'a plus à changer de page, 70 fichiers en moins ;
- les limites de l'avis n'ont plus à être recopiées dans la fiche (règle actuelle de `CLAUDE.md`) : elles sont écrites une fois ;
- la procédure d'ajout et de révision se simplifie (fiche et avis toujours revus ensemble).

**Coûts et précautions** :

- **Longueur** : mesurée après fusion, la médiane passe de 1 000 à 1 230 mots par fiche. Les quatre fiches dont l'avis suit le format long (Claude Code, OpenAI Codex, Hermes Agent, Jev) font de 4 150 à 5 200 mots ; la table des matières de Quartz suffit à s'y repérer.
- **Doublons** : « Points forts / Limites » (analyse de la rédaction) et « Apprécié / Critiqué » (ce que disent les tiers) se recoupent. La fusion se fait d'abord sans perte de texte ; le dédoublonnage se fait ensuite famille par famille, en gardant cette distinction.
- **Contrôle d'objectivité** : la séparation fiche/avis a servi de garde-fou lors de l'audit du 9 octobre 2026 (l'avis faisait foi face à une fiche flatteuse). La section garde donc sa propre date et ses propres sources.
- **Liens** : 191 liens vers des avis, réécrits par script : vers `[[#Avis indépendants|…]]` dans la fiche elle-même, vers `[[Nom#Avis indépendants|…]]` ailleurs (index, mémos, autres fiches).

## 9. Mémos téléchargeables

**Objectif** : voir en un coup d'œil l'essentiel de chaque outil, dans un fichier téléchargeable inclus dans la fiche.

### Ce que permet NotebookLM (vérifié le 10 novembre 2026)

- La page d'aide officielle de Google, désormais titrée « Gemini Notebook », décrit des **infographies téléchargeables en PNG**, avec orientation, niveau de détail et style réglables. La génération se fait dans l'interface. Google précise : « Infographics are AI-generated and may contain visual or factual inaccuracies. »
- Les **diaporamas** s'exportent en PDF ou PPTX selon des guides tiers.
- **Pas d'API officielle** pour générer une infographie : l'API de NotebookLM Enterprise couvre la gestion des notebooks ; seuls des SDK et serveurs MCP non officiels automatisent la génération.

### Limites pour cet usage

- **Exactitude** : `CLAUDE.md` exige que chaque commande vienne de la documentation officielle. Un texte rendu dans une image générée peut être déformé : chaque image devrait être relue commande par commande, à chaque régénération.
- **Texte dans une image** : ni recherche dans le site, ni copier-coller des commandes, ni lecture par un lecteur d'écran.
- **Maintenance** : 60 mémos à régénérer à la main à chaque mise à jour, avec une mise en page qui change à chaque génération.

### Proposition

1. **Le mémo Markdown reste la source unique** et vérifiée, publiée en page web (recherche et copier-coller possibles).
2. **Un PDF d'une page est généré automatiquement** depuis ce Markdown avec un gabarit commun (A4 paysage, deux ou trois colonnes, mêmes couleurs pour tous), ainsi qu'une image d'aperçu pour la fiche. Un script les régénère avant chaque publication. Les mémos actuels s'y prêtent : médiane de 500 mots et 20 lignes de tableau ; seuls 3 dépassent 1 200 mots (jusqu'à 2 284 pour OpenAI Codex) et demanderont une section « L'essentiel » ou deux pages.
3. **NotebookLM en complément** : une infographie « vue d'ensemble » pour quelques outils phares, générée à partir du seul mémo vérifié, relue avant publication et signalée comme générée avec NotebookLM.

**Pilote** : trois mémos (Claude Code, Playwright, Supabase) produits selon les deux approches, puis choix sur pièces.

**Pilote PDF fait le 12 novembre 2026**, sur le modèle des aide-mémoire de référence fournis par l'auteur (DataCamp pour l'essentiel, aussi Docker, Enthought, PyCharm) : A4 paysage, trois colonnes de blocs à bandeau de couleur, commandes à gauche et description à droite, couleur selon la zone de la famille. Script `scripts/memos_pdf/generer.py` (Python sans dépendance, impression par Chrome) ; résultats dans un dossier provisoire `pilote-memos/`, mis à la corbeille le 12 novembre 2026 une fois les PDF publiés. Playwright tient sur une page en 9 pt, Supabase en 10,5 pt ; Claude Code (292 lignes) demande trois pages. NotebookLM n'a pas été essayé : il se pilote depuis le compte Google de l'auteur.

**Style validé et 60 mémos générés le 12 novembre 2026** (en une minute environ). 56 tiennent sur une page (de 7 à 10,5 pt) ; GStack (9 pt) et Jev (7 pt) sur deux, Claude Code sur trois (7,5 pt), OpenAI Codex sur quatre (8 pt). La relecture des 60 aperçus a fait corriger la mise en page : en-tête de tableau répété dans la suite (et jamais seul en bas de colonne), numérotation reprise dans une liste coupée, phrase d'annonce (« … : ») gardée avec ce qu'elle annonce, commentaire `#` au milieu d'un bloc bash traité comme une description, `## ` dans un bloc de code non pris pour une section, encadré Obsidian (`> [!warning]`) rendu en encadré. Le script signale désormais les blocs coupés, le contenu trop large et le Markdown non converti (aucun sur les 60).

Côté Quartz : tout fichier non Markdown placé dans `content/` (PDF, PNG) est publié tel quel ; une image s'affiche dans la page, un PDF se télécharge par lien. L'affichage d'un PDF directement dans la page n'est pas documenté.

**Publiés dans le site le 12 novembre 2026.** Les PDF et leur aperçu (JPEG de 1 100 px, environ 280 Ko : un PNG pèserait plus que le PDF) sont dans `content/memos/pdf/` (26 Mo pour les 60). Le plugin `wiki-fiche` lit leur présence à la construction : lien « PDF » dans la ligne Mémo de l'encadré, section « Mémo pratique » (aperçu et téléchargement) insérée avant « Avis indépendants » sur la fiche, ligne « PDF » sur la page du mémo. Aucun fichier Markdown n'est modifié, donc aucune date de « Dernière analyse » ne bouge ; dans Obsidian, la section n'apparaît pas. Le script régénère seulement les PDF périmés (`--modifies`) et les signale dans la liste de contrôle (n° 9 de `CLAUDE.md`). Les noms de fichiers sont gardés en Unicode composé : `sips` écrivait « mémo » décomposé, que l'URL n'aurait pas trouvé sur le serveur.

## 10. Autres gabarits

- **Page de famille** (`outils/<famille>/index.md`) : lecture en deux phrases (reprise du comparatif) ; tableau des outils (Outil, En bref, Format, trois notes éditoriales, total /15, Popularité, Mémo) ; « Comment choisir » (points d'attention de l'index) ; critères propres à la famille ; justification des notes ; « Absents notables » (outils cités sans fiche, voir § 12).
- **Page métier** : introduction, puis le tableau actuel « Besoin / Outils recommandés / Point d'attention » de l'index, sans changement de fond.
- **Page concept** : définition, fonctionnement, points de vigilance, outils du wiki qui en relèvent, sources. Les variantes de nom passent en `aliases`.
- **Accueil** : deux phrases d'introduction et ce que mesure le wiki ; « Par métier » (6 liens) ; « Par famille » (3 zones, 16 liens) ; « Comprendre » (concepts) et « Assembler » (guides) ; notes récentes ; principes de sélection (conservés).

## 11. Ce que ça change pour l'ajout d'un outil

| Étape | Aujourd'hui | Après |
|---|---|---|
| Fiche et avis | 2 fichiers | 1 fiche, l'avis en est une section |
| Mémo | 1 fichier | 1 fichier ; PDF et aperçu générés par script |
| Classement « par nature » | ligne manuelle dans l'index | la fiche est créée dans le dossier de sa famille (liste automatique) |
| Classement « par secteur » | ligne manuelle dans l'index | ligne manuelle dans la page métier |
| Compteur de l'index | manuel | supprimé (Quartz affiche les listes de dossier et de tag) |
| Notes ★ | comparatif + recopie dans la fiche | page de famille (référence, avec la justification), recopiées dans le frontmatter de la fiche et le tableau « Toutes les notes » du comparatif, concordance vérifiée par le contrôle n° 5 ; Popularité calculée depuis les étoiles |
| Justification et critères | comparatif | page de la famille |

**Bases dans Quartz** : Quartz 5 documente un plugin communautaire, BasesPage, qui affiche les fichiers `.base` d'Obsidian sous forme de tableaux triables avec filtres et formules (utile pour le total /15). Il est marqué « nouveau en v5 ». **Essai du 12 novembre 2026** (sur une copie, famille « Agents de développement ») : un fichier `.base` intégré à la page de famille (`![[Notes agents.base]]`) filtre bien les fiches du dossier, calcule le total /15 par formule et trie par total. Limites : les notes s'affichent en chiffres et non en étoiles (le moteur de formules n'a pas de fonction de répétition) ; la justification, qui n'est pas dans le frontmatter, ne peut pas figurer dans le tableau ; chaque fichier `.base` devient aussi une page du site et de l'explorateur. **Décision du 12 novembre 2026 : les tableaux de notes restent manuels**, sans Bases ; le contrôle n° 5 de `CLAUDE.md` vérifie leur concordance avec les fiches.

## 12. Contenu à prévoir

- **Concepts** (8 pages) : MCP, Skill, Plugin, Hook, Sous-agent (remplit `Subagents.md`), Harnais d'agent, Worktree, Mémoire d'agent.
- **Fiches manquantes les plus citées** : Cursor (12 liens), GitHub Copilot (4), Gemini CLI (3), Figma (3). Les trois premières sont de vrais concurrents dans la famille « Agents de développement », qui n'en compte que quatre.
- **Fiche NotebookLM** : elle ne mentionne ni les infographies ni les diaporamas ; à mettre à jour si l'outil sert à produire les mémos.

## 13. Plan de migration

| Phase | Contenu | Risque |
|---|---|---|
| 1. Corrections | **Faite le 10 novembre 2026** : « Voir aussi » ajouté sur 38 fiches, complété du mémo sur 5, remonté sous le tableau sur 17 (61 fiches modifiées) ; 6 liens corrigés ; `Design.md` mis à la Corbeille. `Subagents.md` reporté avec les concepts. | — |
| 2. Taxonomie et barème | **Faite le 11 novembre 2026** : page `Taxonomie` ; étoiles, forks et date du dernier commit relevés pour 59 dépôts (API GitHub et flux Atom) ; section « Le critère Popularité » et colonne Popularité dans le comparatif ; frontmatter des 70 fiches (`type: outil`, format, famille, tags en français, description, site, dépôt, licence, notes, étoiles datées, mémo) ; ligne Popularité dans le tableau Analyse ; tableau d'en-tête mis à jour ; gabarit et `CLAUDE.md` (barème, procédure, contrôle n° 4) mis à jour. Tags : 97 → 28. | — |
| 3. Fusion des avis | **Faite le 11 novembre 2026** : section « Avis indépendants » dans les 70 fiches (sections d'origine conservées), sources des avis sous « Sources des avis », 191 liens réécrits, 70 fichiers d'avis mis à la Corbeille ; champs `editeur`, `statut` et `avis_maj` ; 39 chiffres d'étoiles retirés du texte de 35 fiches (désormais portés par la note Popularité) ; index, gabarit, `Taxonomie` et `CLAUDE.md` mis à jour. Non fait : la colonne « Contributors », que l'API publique de GitHub ne donne pas de façon fiable pour les gros dépôts ; elle disparaîtra avec le tableau d'en-tête en phase 4. | — |
| 4. Dossiers et pages | **Faite le 12 novembre 2026** : 70 fiches rangées dans `outils/<famille>/` et champ `famille` supprimé ; 60 mémos renommés `memos/Nom mémo.md` (`type: memo`, champ `fiche`), 194 liens réécrits ; tableau d'en-tête supprimé (données dans le frontmatter, `forks` ajouté, colonne Contributors abandonnée) ; tableau « Domains » remplacé par une ligne « Composition » sur 44 fiches ; 16 pages de famille (notes, justifications et critères déplacés du comparatif, points d'attention de l'ancien index, absents notables) ; `outils/index.md` ; 6 pages métier (tableaux de l'ancien index) ; 8 concepts ; accueil réécrit ; `methode/` (À propos, comparatif réduit au barème et au tableau « Toutes les notes », Taxonomie avec les types de pages) ; `guides/` ; 31 pages de tags ; gabarits de mémo, de famille et de concept dans `_modeles/` ; `CLAUDE.md` (procédure, contrôles n° 2, 5 et 6) ; script `scripts/verifier_liens.py`. Non fait : encadré Verdict, ligne d'accès et section « Mémo pratique » du § 7 (avec le dédoublonnage et la phase 5). | — |
| 5. Mémos téléchargeables | Pilote sur 3 outils (gabarit PDF et NotebookLM), choix, puis génération des 60. **Faite le 12 novembre 2026** (§ 9) : pilote, style validé, 60 PDF générés et publiés dans `content/memos/pdf/`, avec aperçu et lien dans la fiche et la page du mémo. À décider : traitement des mémos longs (Claude Code, OpenAI Codex, Jev, GStack), NotebookLM. | Faible |
| 6. Quartz | **Faite le 12 novembre 2026** : Quartz 5.0.0 installé à la racine depuis `quartz-5.zip` (moteur seul, sans sa documentation ni ses workflows) ; `quartz.config.yaml` partie du modèle « obsidian » : titre « AI Tools Wiki », `fr-FR`, `baseUrl` `aitoolswiki.viellard.fr`, exclusions `_modeles`, `.obsidian` et du canvas vide, LaTeX désactivé (les prix en `$` étaient lus comme des formules), aucune mesure d'audience, pages chiffrées désactivées, liens sans cible grisés, fil d'Ariane « Accueil » ; plugin local `plugins/wiki-fiche/` (encadré « Fiche » en français, retrait du `# Titre` en double) ; `title` aligné sur le `# Titre` dans 79 pages (18 fiches corrigées, 60 mémos et le guide complétés) ; explorateur dans l'ordre des zones (`quartz.ts`) ; essai Bases (§ 11) ; contrôles n° 7 (titres) et n° 8 (build) dans `CLAUDE.md`. Build : 201 pages, environ 20 s ; 1 807 liens internes, dont 205 grisés vers 122 fiches à écrire, comme le relève `verifier_liens.py`. Non fait : notes récentes (toutes les pages ont la date du 12 novembre 2026, la liste serait arbitraire), workflow de déploiement (avec la publication). | — |
| 7. Documentation | `CLAUDE.md` (procédure, liste de contrôle) et `projet.md` (décisions). | Faible |

## 14. Décisions

**Prises le 10 novembre 2026** :

- tags en français (identifiants sans accents) ;
- étoiles conservées et affichées avec leur date de relevé ;
- rangement en sous-dossiers.

**Prise le 11 novembre 2026** :

- arborescence du § 6 validée : un sous-dossier par famille dans `outils/`, plus `memos/`, `metiers/`, `concepts/`, `guides/`, `methode/`, `tags/` et `_modeles/` ;
- avis intégrés aux fiches (§ 8) ;
- « Design et UI » scindée en « Prototypage en ligne » et « Design en code » ;
- nouvelle famille « Modèles » (Jev, Nano Banana) ;
- étoiles comme critère de notation « Popularité », calculé (§ 7) ;
- total maintenu sur /15, Popularité affichée à côté.

**Prise le 12 novembre 2026** :

- tableaux de notes manuels dans les pages de famille et le comparatif, sans Bases, après essai (§ 11).

**À prendre** :

1. ~~Mémos : PDF généré depuis le Markdown~~ : fait le 12 novembre 2026 (§ 9). Restent ouverts : mémos longs (section « L'essentiel » ou plusieurs pages), NotebookLM en complément.
2. ~~Superset, renommé Paradev~~ : fait le 15 novembre 2026. Fiche et mémo renommés (`Paradev.md`, `Paradev mémo.md`, URL `/outils/postes-de-pilotage/paradev`) avant la mise en ligne ; licence MIT depuis le 4 novembre 2026, nouvelles adresses du site, du dépôt et de la CLI.
3. ~~Perplexity MCP, dont le dépôt a disparu~~ : fait le 15 novembre 2026. La fiche (même fichier, même URL) décrit désormais le serveur officiel `perplexityai/modelcontextprotocol` ; une note y rappelle l'ancien sujet.
4. Encadré « Verdict » en tête de fiche (§ 7) : à rédiger fiche par fiche, avec le dédoublonnage des avis. La ligne d'accès est assurée par l'encadré « Fiche ».
5. ~~Titre en double~~ : réglé en phase 6. Le `title` reprend le `# Titre` (nom exact du produit), et le plugin local masque le `# Titre` à l'affichage ; les fichiers le gardent pour Obsidian (contrôle n° 7).
