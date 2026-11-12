---
title: "Architecture multi-repos et harnais Claude Code spécialisés"
type: guide
date: 2026-10-02
tags:
  - metier/ingenierie
  - metier/produit-design
  - theme/multi-agent
  - theme/contexte
  - theme/revue-de-code
  - theme/securite
---

# Architecture multi-repos et harnais Claude Code spécialisés

> Synthèse des choix recommandés pour organiser un produit décliné sur le web, iOS et Android, avec un backend commun, un espace produit/UX, un dispositif marketing et un référentiel d’architecture transverse. Chaque dépôt dispose d’un harnais Claude Code spécialisé, tandis que des contrats explicites assurent la cohérence de l’ensemble.

## Conclusion générale

L’organisation la plus cohérente est une **architecture multi-repos gouvernée par des sources de vérité clairement attribuées**. La séparation par dépôt est pertinente lorsque les plateformes ont des stacks, des cycles de livraison, des tests et des contraintes de sécurité réellement différents.

La cible recommandée est :

|Dépôt|Responsabilité principale|
|---|---|
|`product-ux`|Vision produit, recherche utilisateur, PRD, parcours et design system|
|`web`|Application web et expérience frontend|
|`backend` ou `platform`|API, logique métier serveur, données, authentification et traitements asynchrones|
|`ios`|Application native iOS|
|`android`|Application native Android|
|`marketing`|Positionnement, SEO, social, campagnes et production de contenu|
|`system-architecture`|Architecture globale, décisions transversales et politiques de compatibilité|
|`.github`|Standards communs de contribution et automatisations organisationnelles|

Cette structure facilite la spécialisation des agents : Claude Code ne charge dans chaque dépôt que les agents, skills, hooks et outils réellement utiles au domaine concerné.

Le principal risque n’est pas d’installer plusieurs projets reconnus. Le risque est de laisser plusieurs frameworks décider simultanément de la même chose. Un harnais efficace peut combiner [[GStack]], [[Superpowers]], [[BMAD Method]], [[Planning with Files]] et des skills spécialisées, à condition d’attribuer un rôle précis à chacun.

## Principes directeurs

### Un dépôt correspond à une frontière de responsabilité

Créer un dépôt séparé est justifié lorsqu’au moins plusieurs des éléments suivants diffèrent :

- stack technique ;
- équipe ou propriétaires ;
- cycle de release ;
- infrastructure de build et de déploiement ;
- politique de sécurité ;
- droits d’accès ;
- versionnement ;
- processus de validation.

Il ne faut pas créer un dépôt uniquement parce qu’un sujet possède un nom distinct. Chaque séparation augmente le coût de coordination, le nombre de pull requests et le risque de divergence documentaire.

### Une information possède une seule source de vérité

Le même PRD, le même design system ou la même spécification OpenAPI ne doivent pas être modifiés manuellement dans plusieurs dépôts.

|Information|Propriétaire canonique|
|---|---|
|Vision, public, problèmes et résultats attendus|`product-ux`|
|Parcours, UX, états et principes visuels|`product-ux`|
|Frontières entre systèmes et décisions transversales|`system-architecture`|
|Schéma de l’API exécutable|`backend`|
|Schéma et migrations de données|`backend`|
|Architecture interne Swift|`ios`|
|Architecture interne Kotlin|`android`|
|Architecture interne frontend|`web`|
|Positionnement, message et calendrier éditorial|`marketing`|
|Standards GitHub communs|`.github`|

### Les contrats relient les dépôts

Le backend devrait publier des contrats versionnés plutôt que demander aux clients de deviner son comportement :

- OpenAPI ou GraphQL pour les API synchrones ;
- AsyncAPI ou schémas d’événements pour les messages ;
- JSON Schema ou Protobuf pour les structures échangées ;
- SDK généré pour TypeScript, Swift et Kotlin ;
- tests de contrat côté consommateurs ;
- politique de dépréciation et de compatibilité ;
- matrice des versions mobiles supportées.

Le schéma exécutable reste dans le dépôt qui l’implémente. Le dépôt d’architecture décrit la politique, les flux et les versions publiées, sans recopier manuellement le contrat.

### Rendre Produit et Architecture visibles en lecture seule

Le dépôt `ios` peut consommer les référentiels `product-ux` et `system-architecture` sans en devenir propriétaire. La solution la plus explicite et reproductible consiste à les monter comme **sous-modules Git** dans un répertoire réservé au contexte :

```text
ios/
├── Context/
│   ├── Product/       → product-ux
│   └── Architecture/  → system-architecture
├── Sources/
├── Tests/
├── CLAUDE.md
└── .claude/
```

Depuis le dépôt `ios` :

```bash
git submodule add git@github.com:<organisation>/product-ux.git Context/Product
git submodule add git@github.com:<organisation>/system-architecture.git Context/Architecture
git add .gitmodules Context/
git commit -m "chore: add product and architecture context"
```

Un sous-module ne copie pas librement le contenu : le dépôt `ios` enregistre le commit exact de chaque référentiel. Une branche iOS donnée reste donc associée à une version précise et reproductible du contexte produit et architectural.

Le clonage initial doit inclure les sous-modules :

```bash
git clone --recurse-submodules git@github.com:<organisation>/ios.git
```

Pour un clone déjà présent :

```bash
git submodule update --init --recursive
```

La mise à jour vers une nouvelle version des référentiels doit être une action volontaire, idéalement matérialisée par une pull request dans `ios` :

```bash
git submodule update --remote Context/Product Context/Architecture
git add Context/Product Context/Architecture
git commit -m "chore: update shared product and architecture context"
```

Cette pull request rend le changement de contexte visible, révisable et réversible. Elle permet aussi de déclencher les tests de compatibilité de l’application.

#### Trois niveaux distincts de lecture seule

La lecture seule doit être pensée à trois niveaux. Aucun mécanisme isolé ne couvre à lui seul tous les usages.

|Niveau|Mécanisme recommandé|Ce qu’il garantit|
|---|---|---|
|GitHub|Rôle `Read`, deploy key sans écriture ou GitHub App avec `contents: read`|L’identité utilisée ne peut pas pousser dans les repos amont|
|Claude Code|Règles `deny` dans `.claude/settings.json` et consignes dans `CLAUDE.md`|L’agent ne doit pas modifier les dossiers de contexte pendant son travail normal|
|Système local ou CI|Montage réellement non inscriptible, identité GitHub limitée et sandbox adaptée|Barrière technique plus forte contre les écritures locales ou distantes|

Les permissions GitHub sont la garantie principale pour empêcher une écriture distante. Pour une personne, il faut lui attribuer uniquement le rôle `Read` sur les deux dépôts. Pour l’automatisation, une deploy key est en lecture seule par défaut ; une GitHub App peut recevoir seulement la permission `Contents: read` sur les repos sélectionnés.

Le `GITHUB_TOKEN` d’un workflow GitHub Actions est limité au dépôt dans lequel le workflow s’exécute. Un workflow du repo `ios` qui doit cloner deux repos privés externes doit donc utiliser une GitHub App ou un jeton dédié disposant uniquement d’un accès en lecture aux dépôts concernés. Le secret doit rester dans GitHub Actions et ne jamais être ajouté au dépôt.

#### Garde-fous Claude Code dans `ios`

Le dépôt `ios` peut ajouter les règles suivantes dans `.claude/settings.json` :

```json
{
  "permissions": {
    "deny": [
      "Edit(/Context/Product/**)",
      "Edit(/Context/Architecture/**)",
      "Bash(git -C Context/Product *)",
      "Bash(git -C Context/Architecture *)"
    ]
  }
}
```

Les règles `Edit` expriment clairement que le contenu amont est consultable mais non modifiable. Les règles `Bash` réduisent les modifications Git accidentelles dans les sous-modules. Elles ne constituent toutefois pas une frontière de sécurité absolue : les règles portant sur les commandes Bash dépendent de la forme de la commande. Pour une isolation stricte, il faut également utiliser des droits de fichier ou un environnement sandboxé en lecture seule.

Le `CLAUDE.md` du repo `ios` devrait compléter les permissions techniques avec des règles de responsabilité :

```markdown
## Contexte amont

- `Context/Product/` et `Context/Architecture/` sont des sources amont en lecture seule.
- Utiliser ces documents pour vérifier les intentions produit, les parcours et les contraintes transversales.
- Ne jamais corriger directement leur contenu depuis ce dépôt.
- Si une incohérence est détectée, produire une proposition à ouvrir dans le dépôt propriétaire.
- Ne pas mettre à jour les pointeurs de sous-modules sans demande explicite.
- En cas de divergence, signaler le document, son commit et l’impact sur iOS.
```

Il faut conserver une distinction nette entre :

- **consulter le contenu**, autorisé pendant l’analyse et l’implémentation ;
- **modifier le contenu amont**, interdit depuis `ios` ;
- **mettre à jour le pointeur du sous-module**, autorisé seulement dans une tâche dédiée et révisée par pull request.

#### Limite de confidentialité des sous-modules

Un sous-module donne accès au dépôt référencé dans son ensemble. GitHub ne permet pas d’accorder un droit de lecture limité à certains dossiers d’un même repo. Si `product-ux` contient des entretiens confidentiels, des données personnelles, des éléments de stratégie ou des recherches qui ne doivent pas être exposés aux équipes clientes, il ne faut pas monter directement ce dépôt.

Dans ce cas, créer un dépôt filtré tel que `shared-product-context` :

```text
shared-product-context/
├── PRODUCT.md
├── EXPERIENCE.md
├── DESIGN-SYSTEM.md
├── GLOSSARY.md
├── RELEASE-CONSTRAINTS.md
└── CHANGELOG.md
```

`product-ux` reste alors la source de vérité complète, tandis que `shared-product-context` publie uniquement le contexte approuvé et nécessaire aux clients. Ce dépôt filtré peut être généré ou synchronisé par une pull request contrôlée, puis consommé comme sous-module par `ios`, `android` et `web`.

#### Alternative pour un usage local ponctuel

Lorsque les repos sont clonés côte à côte, Claude Code peut recevoir des répertoires supplémentaires sans créer de dépendance Git :

```bash
claude --add-dir ../product-ux --add-dir ../system-architecture
```

La même intention peut être déclarée avec `permissions.additionalDirectories`. Cette approche est pratique pour une exploration locale, mais elle est moins adaptée au fonctionnement d’une équipe : elle ne fixe pas de version du contexte, ne voyage pas automatiquement avec le clone et dépend de l’organisation des dossiers sur chaque machine.

La recommandation de départ est donc :

1. utiliser deux sous-modules épinglés dans `ios/Context/` ;
2. limiter les identités GitHub à la lecture ;
3. déclarer les répertoires en lecture seule dans le harnais Claude Code ;
4. mettre à jour les pointeurs uniquement par pull request ;
5. remplacer `product-ux` par un dépôt de contexte filtré dès que sa confidentialité l’exige.

## Modèle de configuration Claude Code

Claude Code distingue plusieurs couches complémentaires :

|Élément|Fonction|Emplacement projet|
|---|---|---|
|`CLAUDE.md`|Contexte permanent, conventions et routage du harnais|Racine ou `.claude/CLAUDE.md`|
|Agent|Rôle spécialisé avec outils et responsabilité propres|`.claude/agents/<agent>.md`|
|Skill|Procédure chargée seulement lorsqu’elle est pertinente|`.claude/skills/<skill>/SKILL.md`|
|Plugin|Ensemble versionné de skills, agents, hooks et éventuellement MCP|Activé dans `.claude/settings.json`|
|Hook|Contrôle déterministe à un événement du cycle de travail|Plugin ou `.claude/settings.json`|
|MCP|Connexion à un outil ou système externe|`.mcp.json` ou plugin|

Les plugins réutilisables doivent être installés en **portée projet** chaque fois que possible :

```bash
claude plugin install <plugin>@<marketplace> --scope project
```

Claude Code conserve le plugin dans son cache local, mais son activation est enregistrée dans le dépôt via `.claude/settings.json`. Les collaborateurs installent le binaire sur leur machine, tandis que le repo déclare le harnais attendu.

### Ce qui peut rester global

L’installation globale doit se limiter à des capacités réellement universelles :

- créateur de skills ;
- utilitaires de diagnostic ;
- éventuellement GStack, dont le mode équipe repose actuellement sur une installation machine ;
- préférences personnelles non liées à un projet.

Les instructions Swift, Kotlin, SQL, SEO ou design ne doivent pas être chargées dans tous les projets.

## Répartition entre Superpowers, GStack et BMAD

Ces trois projets ont une valeur réelle, mais leurs territoires doivent être explicités.

### Superpowers : méthode d’implémentation

[[Superpowers]] est responsable de :

- brainstorming avant le code ;
- clarification de la solution ;
- plan d’implémentation ;
- TDD ;
- découpage en petits incréments ;
- développement par sous-agents ;
- revue intermédiaire ;
- vérification finale.

Il constitue le moteur quotidien des repos de code : web, backend, iOS et Android.

### GStack : équipe de revue et d’exploitation

[[GStack]] est responsable de :

- challenge produit avec `office-hours` et `plan-ceo-review` ;
- revue d’architecture avec `plan-eng-review` ;
- revue design avec `plan-design-review` ;
- investigation par cause racine ;
- revue de complétude ;
- QA réelle ;
- sécurité avec `cso` ;
- documentation et release ;
- QA spécialisée iOS sur appareil réel.

GStack ne remplace pas le plan d’implémentation de Superpowers. Il le challenge avant le code et évalue le résultat après l’implémentation.

Pour éviter les collisions de commandes, l’installation avec préfixe est préférable :

```bash
cd ~/.claude/skills/gstack
./setup --prefix
```

On distingue ainsi `/code-review`, `/superpowers:...` et `/gstack-review`.

### BMAD : documents produit et solution

[[BMAD Method]] est responsable des artefacts durables :

- recherche ;
- product brief ;
- PRFAQ ;
- PRD ;
- spécification ;
- UX ;
- architecture de haut niveau ;
- epics et stories.

BMAD est central dans `product-ux` et utile dans `system-architecture`. Il n’est pas nécessaire dans chaque dépôt d’implémentation lorsque le travail produit est déjà cadré en amont.

### Planning with Files : persistance, pas conception

[[Planning with Files]] conserve l’état d’une tâche longue :

- plan actif ;
- découvertes ;
- erreurs déjà rencontrées ;
- progression ;
- reprise après compaction ou interruption ;
- contrôle de complétion.

Il ne doit pas créer un plan concurrent. Superpowers ou BMAD définissent le travail ; Planning with Files suit son exécution.

## Harnais du dépôt `product-ux`

### Responsabilité

Ce dépôt possède le **pourquoi** et le **comportement attendu** du produit :

- vision et principes ;
- publics et problèmes ;
- recherche utilisateur ;
- hypothèses ;
- décisions produit ;
- PRD ;
- parcours ;
- architecture de l’information ;
- `DESIGN.md` ;
- `EXPERIENCE.md` ;
- règles d’accessibilité ;
- critères de succès.

### Harnais recommandé

```text
BMAD
+ GStack
+ Planning with Files
+ UI/UX Pro Max
+ Frontend Design
+ Impeccable
+ outils de prototypage et validation visuelle
```

|Composant|Rôle|
|---|---|
|BMAD|Produit les documents canoniques|
|GStack|Challenge le scope, le produit et le design|
|[[UI UX Pro Max]]|Apporte la base de connaissances UX et design system|
|[[FrontEnd Design]]|Produit une première direction visuelle distinctive|
|[[Impeccable]]|Critique, audite et polit un prototype existant|
|Planning with Files|Suit les initiatives longues|
|Playwright/Chrome DevTools|Valide les prototypes rendus|

### Workflow type

```text
BMAD recherche et product brief
→ GStack plan-ceo-review
→ BMAD PRD
→ BMAD UX : DESIGN.md + EXPERIENCE.md
→ GStack plan-design-review
→ UI/UX Pro Max pour le design system
→ GStack design-shotgun pour explorer plusieurs directions
→ Frontend Design pour le prototype
→ Impeccable pour critique et polish
→ validation navigateur
```

Superpowers n’est ajouté à ce dépôt que si celui-ci contient du code de prototype significatif.

## Harnais du dépôt `web`

### Responsabilité

Le repo web possède :

- le code frontend ;
- la navigation web ;
- le rendu responsive ;
- l’accessibilité web ;
- la performance frontend ;
- le SEO technique ;
- les tests unitaires, intégration et end-to-end ;
- l’instrumentation analytics côté navigateur.

Il ne possède pas le positionnement marketing ni le schéma de données métier.

### Harnais recommandé

```text
Superpowers
+ GStack
+ Planning with Files
+ UI/UX Pro Max
+ Frontend Design
+ Impeccable
+ Web Design Guidelines
+ Playwright
+ Chrome DevTools
+ Security Guidance
+ Claude Security
+ /code-review
```

### Répartition

- Superpowers : plan, TDD, implémentation et délégation ;
- GStack : revue d’architecture, QA, design review, performance et release ;
- UI/UX Pro Max : tokens, règles UX, palettes et choix techniques ;
- Frontend Design : direction artistique initiale ;
- Impeccable : audit et finition ;
- [[Web Design Guidelines]] : audit sémantique accessibilité, formulaires, focus, motion et responsive ;
- [[Playwright]] et [[Chrome DevTools MCP]] : vérification réelle du navigateur ;
- Security Guidance : surveillance continue ;
- Claude Security : audit approfondi avant une release sensible ;
- `/code-review` : revue technique indépendante du diff.

### Workflow type

```text
spécification issue de product-ux
→ Superpowers brainstorming ciblé
→ plan d’implémentation
→ GStack plan-eng-review et plan-design-review
→ TDD et implémentation par sous-agents
→ captures mobile/desktop
→ Impeccable + Web Design Guidelines
→ Playwright et Chrome DevTools
→ /code-review high
→ GStack review, benchmark et ship
```

## Harnais du dépôt `backend` ou `platform`

### Responsabilité

Le backend ne doit pas être réduit à « gérer les bases de données ». Il possède :

- logique métier serveur ;
- API ;
- authentification et autorisations ;
- schéma et migrations ;
- politiques RLS ;
- fonctions serveur ;
- webhooks ;
- files et jobs ;
- intégrations externes ;
- audit et journalisation ;
- observabilité ;
- spécifications de contrat ;
- génération des SDK clients.

### Harnais recommandé

```text
Superpowers
+ GStack
+ Planning with Files
+ Security Guidance
+ Claude Security
+ tests de contrat
+ skill spécialisée pour la base choisie
+ /code-review
```

Si le projet utilise [[Supabase]], seules les skills Supabase réellement nécessaires doivent être ajoutées : migrations, RLS, Edge Functions et revue de sécurité. Elles ne remplacent pas la compréhension du domaine ni les tests de permissions.

### Agents locaux suggérés

```text
.claude/agents/
├── backend-architect.md
├── database-migration-reviewer.md
├── api-contract-reviewer.md
└── security-reviewer.md
```

### Workflow type

```text
contrat fonctionnel
→ Superpowers plan et TDD
→ GStack plan-eng-review
→ revue migration/RLS
→ implémentation
→ tests unitaires, intégration et contrat
→ Security Guidance
→ /code-review high
→ Claude Security pour auth/données sensibles
→ publication du schéma et des SDK
→ GStack ship
```

## Harnais du dépôt `ios`

### Harnais recommandé

```text
Superpowers
+ GStack iOS
+ Planning with Files
+ UI/UX Pro Max
+ Security Guidance
+ Claude Security
+ skills Xcode propres au projet
+ /run, /verify et /code-review
```

### Particularité de GStack iOS

GStack fournit la chaîne la plus spécialisée identifiée dans l’inventaire :

- `ios-qa` : exploration et test sur iPhone réel ;
- `ios-fix` : reproduction par snapshot, correction, rebuild et nouvelle vérification ;
- `ios-design-review` : audit visuel et alignement avec les Apple HIG ;
- `ios-sync` : synchronisation du bridge et des accesseurs ;
- `ios-clean` : retrait propre de l’instrumentation de debug.

### Agents locaux suggérés

```text
.claude/agents/
├── ios-architect.md
├── swiftui-implementer.md
└── ios-test-reviewer.md
```

### Skill locale prioritaire

Une skill `ios-build-verify` doit enregistrer :

- workspace et scheme ;
- destinations simulateur et appareil ;
- commandes `xcodebuild` ;
- version minimale d’iOS ;
- règles de signature ;
- configuration de tests ;
- définition de terminé.

Elle peut être amorcée avec `/run-skill-generator`, puis commitée dans `.claude/skills/`.

### Workflow type

```text
Superpowers brainstorming et plan
→ GStack plan-eng-review
→ GStack plan-design-review si interface
→ TDD et implémentation Swift
→ /verify
→ /code-review high
→ GStack ios-qa
→ GStack ios-design-review
→ GStack review et ship
```

## Harnais du dépôt `android`

### Harnais recommandé

```text
Superpowers
+ GStack général
+ Planning with Files
+ UI/UX Pro Max
+ Security Guidance
+ Claude Security
+ skills Gradle/Compose propres au projet
+ /run, /verify et /code-review
```

UI/UX Pro Max couvre Jetpack Compose, mais GStack ne fournit pas encore un équivalent aussi complet de sa boucle iOS sur appareil réel. Le repo Android doit donc investir davantage dans des skills locales.

### Skills locales suggérées

```text
.claude/skills/
├── android-build-verify/
├── android-device-qa/
├── compose-ui-review/
├── gradle-dependency-review/
└── android-security-review/
```

### Agents locaux suggérés

```text
.claude/agents/
├── android-architect.md
├── compose-implementer.md
└── android-test-reviewer.md
```

Les recettes doivent documenter les modules Gradle, build variants, versions SDK, émulateurs de référence, tests instrumentés, règles de signature et commandes de capture d’écran.

## Harnais du dépôt `marketing`

### Responsabilité

Le repo marketing possède :

- positionnement ;
- audiences ;
- messages ;
- offres ;
- stratégie SEO éditoriale ;
- clusters de mots-clés ;
- briefs et contenus ;
- calendrier social ;
- campagnes payantes ;
- prompts et storyboards créatifs ;
- scripts et automatisations marketing ;
- taxonomie analytics ;
- rapports et apprentissages.

### Harnais recommandé

```text
Claude SEO
+ AI Marketing Claude
+ Marketing Skills from Corey Haines
+ Humanizer
+ Planning with Files
+ outils de recherche
+ outils de génération image
+ outils de génération vidéo
+ GStack pour les campagnes impliquant du code ou une landing page
```

La sélection exacte dépend des canaux employés. Les collections marketing doivent être installées de manière granulaire plutôt qu’en bloc.

|Besoin|Outils candidats de l’inventaire|
|---|---|
|SEO|[[Claude SEO]], [[Semrush]] si connecté|
|Stratégie et campagnes|[[Ai-Marketing-Claude]], [[Marketing Skills from Corey Haines]]|
|Réécriture et ton|[[Humanizer]]|
|Images|[[Nano Banana]], [[Banana Prompts]], [[Higgsfield-skills]]|
|Vidéo|[[Higgsfield-ai-platform]], [[Remotion]]|
|Recherche|[[Perplexity MCP]], [[Firecrawl]], Gemini Deep Research|

### Gestion des médias

Les exports vidéo, images haute résolution et fichiers générés ne doivent pas gonfler indéfiniment l’historique Git.

Git doit conserver en priorité :

- briefs ;
- prompts ;
- scripts ;
- storyboards ;
- métadonnées ;
- manifestes d’assets ;
- sources raisonnablement petites ;
- liens vers le stockage des rendus.

Les binaires volumineux doivent utiliser Git LFS ou un stockage d’objets. Les secrets d’API publicitaire ou de génération ne doivent jamais être commités.

## Harnais du dépôt `system-architecture`

### Responsabilité

Ce dépôt constitue la vue transverse du système :

- contexte global ;
- cartographie des composants ;
- flux d’authentification et de données ;
- décisions architecturales ;
- classification des données ;
- exigences de sécurité ;
- observabilité et SLO ;
- environnements ;
- politiques de versionnement ;
- compatibilité entre clients et API ;
- catalogue de services ;
- RFC transversales.

Il ne doit pas devenir une copie des README et fichiers d’architecture internes de chaque projet.

### Structure suggérée

```text
system-architecture/
├── CLAUDE.md
├── SYSTEM_CONTEXT.md
├── SERVICE_CATALOG.md
├── SECURITY_MODEL.md
├── DATA_CLASSIFICATION.md
├── OBSERVABILITY.md
├── RELEASE_COMPATIBILITY.md
├── adr/
├── diagrams/
├── contracts/
├── environments/
└── rfcs/
```

### Harnais recommandé

```text
BMAD Architecture
+ GStack plan-eng-review
+ Planning with Files
+ Diagram
+ Security Guidance ou GStack cso
+ revue de contrats
```

Superpowers est utile seulement lorsque ce dépôt contient des scripts, générateurs ou validateurs significatifs. Pour la documentation et les décisions, BMAD et GStack suffisent généralement.

### Workflow d’une décision transverse

```text
problème documenté dans une RFC
→ BMAD architecture propose les options
→ GStack plan-eng-review cherche les angles morts
→ revue sécurité et données
→ décision enregistrée dans un ADR
→ issues créées dans les repos concernés
→ contrats et matrice de compatibilité mis à jour
```

## Dépôt organisationnel `.github`

Un repo `.github` permet de mutualiser :

- `CONTRIBUTING.md` ;
- `SECURITY.md` ;
- templates d’issues ;
- templates de pull requests ;
- conventions de labels ;
- documentation de gouvernance ;
- workflows GitHub Actions réutilisables.

Les règles propres aux stacks ne doivent pas être placées dans un `CLAUDE.md` global. Swift, Kotlin, frontend, données et marketing conservent leurs instructions dans leurs repos respectifs.

## Coordination des initiatives inter-repos

Une fonctionnalité peut produire plusieurs pull requests :

```text
product-ux
→ system-architecture
→ backend
→ web
→ ios
→ android
→ marketing
```

Pour conserver la traçabilité, chaque initiative reçoit un identifiant partagé :

```text
INIT-042 — Connexion par passkey

product-ux#84
system-architecture#31
backend#122
web#204
ios#178
android#166
marketing#57
```

Les pratiques recommandées sont :

- un GitHub Project transversal ;
- un identifiant d’initiative dans les issues et PR ;
- des ADR pour les décisions transversales ;
- des contrats versionnés ;
- des SDK générés ;
- des tests de compatibilité ;
- une matrice de versions ;
- des changelogs par dépôt ;
- des règles explicites de dépréciation ;
- une politique de synchronisation des documents produit et design.

## Exemple de routage commun dans `CLAUDE.md`

```markdown
## Harness ownership

- BMAD owns durable product and architecture artifacts.
- Superpowers owns implementation planning, TDD and subagent-driven development.
- GStack challenges plans and reviews completed work; it does not replace the approved implementation plan.
- Planning with Files persists execution state for long-running work; it does not create a competing plan.
- UI/UX Pro Max provides design knowledge.
- Frontend Design owns initial visual generation.
- Impeccable owns design critique and final polish.
- Security Guidance runs continuously.
- Claude Security is reserved for explicit deep scans.
- `/code-review` performs technical diff review.
- `/gstack-review` performs release-readiness review.
```

Chaque repo complète ce bloc avec ses propres commandes, agents et critères de fin.

## Projets à ne pas installer intégralement

Certaines collections restent utiles comme catalogues, sans être de bons harnais complets lorsqu’un autre système est déjà en place.

### Everything Claude Code

[[Everything Claude Code]] chevauche fortement GStack, Superpowers, Planning with Files et les outils de sécurité. L’installer en plus créerait plusieurs propriétaires pour la planification, la mémoire, la revue et le TDD.

### Wshobson Agents

[[Wshobson Agents]] est un excellent catalogue granulaire. Il doit servir à combler un manque identifié — par exemple un reviewer spécialisé — et non être installé intégralement au-dessus du harnais principal.

### Alirezarezvani Claude Skills

[[Alirezarezvani Claude Skills]] est également une bibliothèque dans laquelle sélectionner des composants unitaires. Sa largeur est son avantage, mais une installation globale introduirait de nombreux déclencheurs redondants.

### Claude-Mem et MemPalace

[[Claude-Mem]] ou [[MemPalace]] deviennent intéressants lorsque plusieurs dépôts et agents doivent retrouver une grande quantité de connaissances historiques. Au départ, `CLAUDE.md`, les documents canoniques, les ADR et Planning with Files offrent une mémoire plus simple, inspectable et contrôlable.

### Taste Skill et Frontend Design

[[Taste Skill]] et Frontend Design cherchent tous deux à orienter la génération visuelle. Frontend Design peut servir de valeur par défaut ; Taste est préférable dans une branche d’exploration où une variance plus forte est explicitement recherchée. Les deux ne doivent pas imposer simultanément une direction artistique.

## Ordre de mise en place conseillé

### Phase 1 — Gouvernance

1. Créer l’organisation GitHub et le repo `.github`.
2. Créer `product-ux` et `system-architecture`.
3. Définir les sources de vérité et le format des ADR.
4. Définir l’identifiant commun des initiatives.
5. Écrire les premiers `CLAUDE.md`.

### Phase 2 — Plateforme et contrats

1. Créer `backend` ou `platform`.
2. Définir le premier contrat d’API.
3. Mettre en place migrations et tests de permissions.
4. Publier les SDK ou clients générés.
5. Documenter la compatibilité dans `system-architecture`.

### Phase 3 — Expériences clientes

1. Créer `web`, `ios` et `android`.
2. Installer Superpowers et les outils de revue en portée projet.
3. Ajouter les skills de build et de vérification propres à chaque plateforme.
4. Brancher les clients générés du backend.
5. Ajouter les tests de contrat et les workflows de QA.

### Phase 4 — Go-to-market

1. Créer `marketing`.
2. Importer positionnement, audiences et taxonomie analytics.
3. Installer uniquement les skills correspondant aux canaux réellement utilisés.
4. Définir le stockage des assets et la politique Git LFS.
5. Relier les résultats marketing au repo produit.

### Phase 5 — Évaluation des harnais

Après quelques fonctionnalités réelles, mesurer pour chaque plugin ou skill :

- fréquence d’utilisation ;
- temps économisé ;
- qualité des défauts trouvés ;
- coût en contexte et en appels ;
- taux de retouche humaine ;
- faux positifs ;
- conflits avec un autre composant ;
- fraîcheur et maintenabilité.

Un composant populaire ou très étoilé mérite d’être testé, mais sa conservation dépend de sa contribution mesurable au workflow du repo.

## Synthèse finale des harnais

|Repo|Harnais cible|
|---|---|
|`product-ux`|BMAD + GStack + Planning with Files + UI/UX Pro Max + Frontend Design + Impeccable|
|`web`|Superpowers + GStack + Planning with Files + UI/UX Pro Max + Frontend Design + Impeccable + Web Design Guidelines + Playwright + sécurité|
|`backend`|Superpowers + GStack + Planning with Files + Security Guidance + Claude Security + skill base de données|
|`ios`|Superpowers + GStack iOS + Planning with Files + UI/UX Pro Max + sécurité + skills Xcode locales|
|`android`|Superpowers + GStack + Planning with Files + UI/UX Pro Max + sécurité + skills Gradle/Compose locales|
|`marketing`|Claude SEO + AI Marketing Claude + skills marketing ciblées + Humanizer + outils image/vidéo|
|`system-architecture`|BMAD Architecture + GStack plan-eng-review + Planning with Files + Diagram + revue de sécurité et contrats|

## Verdict

L’organisation multi-repos proposée est pertinente pour un produit multi-plateforme et s’accorde bien avec Claude Code. Elle permet de construire des harnais réellement spécialisés plutôt qu’une installation globale indistincte.

La réussite du système repose sur cinq conditions :

1. une seule source de vérité par type d’information ;
2. des contrats exécutables entre les projets ;
3. un routage explicite entre BMAD, Superpowers et GStack ;
4. des agents et skills locales pour les particularités de chaque codebase ;
5. une évaluation régulière de la valeur réelle de chaque composant installé.

La structure recommandée peut se résumer ainsi :

```text
Produit       : product-ux
Architecture  : system-architecture
Plateforme    : backend
Expériences   : web, ios, android
Go-to-market  : marketing
Gouvernance   : .github
```

Le nombre de dépôts et de skills n’est alors plus un problème en soi : les frontières, les responsabilités et les contrats rendent l’ensemble compréhensible et maintenable.

## Sources et fiches associées

- [[GStack]]
- [[Superpowers]]
- [[BMAD Method]]
- [[Planning with Files]]
- [[UI UX Pro Max]]
- [[Impeccable]]
- [[FrontEnd Design]]
- [[Web Design Guidelines]]
- [[Security Guidance]]
- [[Claude Code Review]]
- [[Claude SEO]]
- [[Ai-Marketing-Claude]]
- [[Marketing Skills from Corey Haines]]
- [[Humanizer]]
- [Claude Code — skills](https://code.claude.com/docs/en/skills)
- [Claude Code — agents spécialisés](https://code.claude.com/docs/en/sub-agents)
- [Claude Code — plugins et portée d’installation](https://code.claude.com/docs/en/discover-plugins)
- [Claude Code — permissions](https://code.claude.com/docs/en/permissions)
- [Git — sous-modules](https://git-scm.com/book/fr/v2/Utilitaires-Git-Sous-modules)
- [GitHub — gestion des deploy keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys)
- [GitHub — authentification d’une GitHub App dans GitHub Actions](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/making-authenticated-api-requests-in-a-github-actions-workflow)
- [GitHub — fichiers communautaires par défaut](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- [GitHub — limites des repositories et fichiers volumineux](https://docs.github.com/en/repositories/creating-and-managing-repositories/repository-limits)
