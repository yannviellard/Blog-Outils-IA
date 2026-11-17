# CLAUDE.md — AI Tools Wiki

Base de connaissances en Markdown (coffre Obsidian + site Quartz) qui recense les outils, frameworks, skills et agents IA, principalement autour de Claude Code. Contexte, décisions et publication : [projet.md](projet.md) ; plan de refonte et décisions de structure : [architecture.md](architecture.md). Langue : **français**, ton neutre et factuel.

## Structure

`content/` contient tout le contenu (coffre Obsidian et dossier de contenu Quartz) :

| Emplacement | Contenu |
|---|---|
| `index.md` | Accueil : par métier, par famille, concepts, guides, mémos, méthode |
| `outils/<famille>/Nom.md` | Fiches, une par outil, rangées dans le dossier de leur famille |
| `outils/<famille>/index.md` | Page de la famille : outils, points d'attention, **notes justifiées** (référence des notes), critères propres, absents notables |
| `outils/index.md` | Vue d'ensemble : les 16 familles par zone, avec leurs outils |
| `memos/Nom mémo.md`, `memos/index.md` | Mémos pratiques et leur bibliothèque |
| `memos/pdf/` | Mémos en PDF et leur aperçu JPEG, générés par `scripts/memos_pdf/generer.py` : ne pas modifier à la main |
| `metiers/` | Six pages métier : besoins, outils recommandés, points d'attention |
| `concepts/` | Notions de base (MCP, skill, plugin, hook, sous-agents, harnais, worktree, mémoire) |
| `guides/` | Guides transversaux |
| `methode/` | À propos (`index.md`), `Comparatif global des outils.md` (barème et tableau « Toutes les notes »), `Taxonomie.md` (familles, formats, statuts, métiers, thèmes, types de pages) |
| `tags/` | Pages de description des tags, une par tag de la Taxonomie |
| `_modeles/` | Gabarits de fiche, de mémo, de famille et de concept (exclus du site, comme `.obsidian/` et toute page `draft: true`) |

Hors de `content/` : le moteur Quartz 5 (`quartz/`, `package.json`, `quartz.config.yaml`, `quartz.ts`), le plugin local `plugins/wiki-fiche/` (encadré « Fiche » et titre unique), `images/logos/` (logos, non affichés pour l'instant), `scripts/verifier_liens.py` (contrôle des liens), `scripts/memos_pdf/` (génération des mémos PDF) et `.github/workflows/deploy.yml` (mise en ligne). Le site construit va dans `public/`, non versionné.

- **Liens** : Obsidian et Quartz résolvent `[[Nom]]` par nom de fichier. Chaque nom de fichier doit donc rester unique (hors `index.md`), y compris sans tenir compte des majuscules. Vers une page de dossier, donner le chemin : `[[outils/agents-de-developpement/index|Agents de développement]]`.
- **URLs** : elles sont générées depuis les chemins, en minuscules (`/outils/agents-de-developpement/claude-code`). Ne pas renommer ni déplacer les fichiers existants ; changer un outil de famille change son URL. Ne pas toucher à `.obsidian/`.

## Construire le site (Quartz 5)

Depuis la racine du projet, avec Node 22 ou plus :

```bash
npm ci                      # première fois : dépendances et plugins
npx quartz build --serve    # site sur http://localhost:8080, reconstruit à chaque modification de content/
```

- **Configuration** : `quartz.config.yaml` (titre, langue `fr-FR`, exclusions `_modeles`, `.obsidian`, plugins) ; ordre de l'explorateur dans `quartz.ts`. Relancer le serveur après une modification de la configuration ou du plugin local.
- **Titre** : le site affiche le `title` du frontmatter en tête de page et masque le `# Titre` qui ouvre le corps (gardé pour Obsidian). Les deux doivent être identiques (contrôle n° 7).
- **Encadré « Fiche »** : sur une fiche, le plugin `plugins/wiki-fiche/` affiche le format, l'éditeur, le statut, la licence, le site, le dépôt, les notes et le total /15, la Popularité, le mémo, la date des avis et les tags, à partir du frontmatter. Rien n'est à recopier dans le corps.
- **Mémos PDF** : sur une fiche dont le mémo a un PDF dans `memos/pdf/`, le plugin ajoute le lien « PDF » dans l'encadré et insère une section « Mémo pratique » (aperçu et téléchargement) avant « Avis indépendants » ; la page du mémo reçoit le lien de téléchargement. Rien n'est à écrire dans les fichiers.
- **Liens sans cible** : affichés grisés, ils mènent à la page 404 ; ils servent de liste des fiches à écrire.
- **LaTeX désactivé** : le `$` des prix s'écrit sans précaution.
- **Mise en ligne** : chaque push sur `main` déclenche `.github/workflows/deploy.yml`, qui construit le site et le publie sur GitHub Pages (`aitoolswiki.viellard.fr`) en une à deux minutes ; résultat dans l'onglet Actions du dépôt. Les mémos PDF ne sont pas générés en ligne : les régénérer et les committer avant le push. Le plugin local est installé par `npx quartz plugin install --from-config`, car `quartz.lock.json` garde un chemin propre au Mac.

## Les fichiers d'un outil

| Fichier | Rôle | Frontmatter |
|---|---|---|
| `outils/<famille>/Nom.md` | Fiche, basée sur le gabarit ; elle contient la synthèse des avis (section `## Avis indépendants`) | `type: outil`, `format`, `tags`, `editeur`, `statut`, notes, étoiles, forks, `avis_maj` (voir le gabarit) ; pas de champ `famille` : c'est le dossier |
| `memos/Nom mémo.md` | Mémo pratique (sauf outils de `SANS_MEMO`) | `title: "Nom — Mémo"`, `type: memo`, `fiche: "[[Nom]]"`, `date` |

Historique : le 11 novembre 2026, les fichiers d'avis séparés ont été fusionnés dans les fiches ; le 12 novembre 2026, les fiches ont été rangées par famille, les mémos renommés (`Nom_cheatsheet.md` → `memos/Nom mémo.md`) et le tableau d'en-tête remplacé par les propriétés du frontmatter, puis le `title` aligné sur le `# Titre` (79 pages) pour le site Quartz, et les 60 mémos publiés aussi en PDF (`memos/pdf/`).

## Procédure pour ajouter un nouvel outil

Faire **toutes** les étapes ; un outil n'est terminé que lorsque la liste de contrôle en bas passe.

1. **Recherche** : documentation officielle, dépôt (étoiles, forks, contributeurs, licence, dernier commit/release, issues), puis **au moins trois sources indépendantes** (tests, discussions, études). Vérifier les chiffres par le web ; ne jamais inventer une valeur (utiliser « — »).
2. **Fiche `outils/<famille>/Nom.md`** à partir de `_modeles/Template Article "Nom du projet".md` : frontmatter (`title` = nom exact du produit, identique au `# Titre` ; `type: outil` ; `format` unique, `tags` : 1 à 3 `metier/…` et 0 à 4 `theme/…`, tous pris dans `Taxonomie.md` ; `description` = phrase « En bref » de la page de famille ; notes identiques à la page de famille ; `etoiles`, `forks` et `etoiles_releve` relevés par l'API GitHub le jour même ; `modified` = date du jour) ; titre et résumé ; ligne **Composition** pour une collection, un plugin ou un serveur MCP ; ligne « Voir aussi » (`[[#Avis indépendants|Avis indépendants]]` et `[[Nom mémo]]`) ; résumé ; fonctionnalités ; analyse ; points forts ; limites ; relations (`[[wikilinks]]`, alternatives réelles, complémentaires) ; sources ; `_Dernière analyse : <date du jour>_`.
   - Pas de tableau d'en-tête : site, dépôt, licence, étoiles et date de mise à jour sont des propriétés du frontmatter.
   - `derniere_maj` = date du dernier commit ou release du dépôt, jamais la date du jour. Produit sans dépôt : supprimer le champ.
   - Ne laisser aucun commentaire `<!-- … -->` du gabarit ni artefact de citation (`contentReference`, `oaicite`).
3. **Section `## Avis indépendants`** de la fiche, juste avant `## Sources` : ligne datée (« Synthèse des retours publiés, mise à jour le … », même date que `avis_maj`), puis `### Ce qui est apprécié`, `### Ce qui est critiqué`, `### Ce qui n'est pas établi`, `### Comparaison` (face aux alternatives réelles), `### Verdict`. Les sources des avis vont dans `## Sources`, sous `### Sources des avis`, avec leur nature et leur fiabilité. Tableau « En bref » des tendances quand la matière est abondante (comme dans `Claude Code.md`). Indiquer la partialité d'une source (éditeur, concurrent, affilié) et les chiffres non reproduits. Les avis fusionnés le 11 novembre 2026 gardent leurs sections d'origine (Synthèse, Comparaison, Verdict…) jusqu'à leur révision.
4. **Mémo `memos/Nom mémo.md`**, à partir de `_modeles/Template Mémo.md`, seulement si l'outil a des commandes, une configuration ou une API à retenir (CLI, SDK, raccourcis, déploiement). Pour une application en ligne sans commandes à retenir, ne pas créer de mémo : l'ajouter à la liste `SANS_MEMO` ci-dessous, supprimer le champ `memo` de la fiche et mettre « — » dans la colonne Mémo de la page de famille. Frontmatter : `title: "Nom — Mémo"`, identique au titre `# Nom — Mémo`. Structure : `# Nom — Mémo`, citation d'une phrase, `## Installation`, `## Commandes principales` (tableaux), sections propres à l'outil, `## Conseils d'utilisation`, `## Sources`. Chaque commande doit venir de la documentation officielle (vérifiée sur le web) ; ne rien inventer. Ajouter le mémo dans `memos/index.md`, sur la ligne de sa famille. Générer ensuite son PDF depuis la racine du projet : `python3 scripts/memos_pdf/generer.py "Nom mémo"` (à refaire après chaque modification du mémo ou de sa fiche : `--modifies` régénère tous les PDF périmés) ; relire l'aperçu `memos/pdf/Nom mémo.jpg` et corriger tout point « À REVOIR ».
5. **Pages de classement** :
   - **page de famille** `outils/<famille>/index.md` : une ligne dans « Les outils » (En bref, format, mémo), une ligne dans « Notes » (3 notes + total /15 + Popularité + justification d'une ligne), une ligne dans « Critères propres à la famille » ; compléter les points d'attention si besoin. Si aucune famille ne convient, en créer une : dossier et page à partir de `_modeles/Template Famille.md` (avec sa lecture de deux phrases), puis l'ajouter à `Taxonomie.md`, à `outils/index.md`, à l'accueil et à la section « Notes par famille » du comparatif ;
   - **vue d'ensemble** `outils/index.md` : ajouter le lien dans la liste de la famille ;
   - **pages métier** `metiers/…` : ajouter l'outil dans la ou les lignes de besoin pertinentes, avec le point d'attention, en cohérence avec ses tags `metier/…` ;
   - **comparatif** `methode/Comparatif global des outils.md` : une ligne dans « Toutes les notes », à sa place dans le tri par total.
   Les quatre notes de la fiche doivent être **identiques** à celles de la page de famille.
6. **Liens croisés** : si l'outil a des alternatives ou des complémentaires dans le wiki, ajouter la relation réciproque dans leurs fiches (sections « Relations »). Lier les notions aux pages de `concepts/` (`[[Skill|skills]]`, `[[Model Context Protocol|MCP]]`, `[[Subagents|sous-agents]]`…).
7. **Liste de contrôle** (commandes ci-dessous) avant de conclure.

## Barème des notes ★ (résumé ; détail dans le comparatif)

Trois critères communs, notés sur 5 : **Documentation**, **Précision des descriptions** (fidélité du discours aux faits confirmés par des tiers), **Maturité** (recul, stabilité, usage attesté).

- Plafond de maturité : moins de 6 mois ≤ ★★ ; 6 à 12 mois ≤ ★★★ ; 1 à 2 ans ≤ ★★★★ ; ★★★★★ seulement au-delà de 2 ans. Préversion, bêta ou Labs : ≤ ★★.
- Sources uniquement éditeur : précision ≤ ★★★.
- **Popularité**, quatrième note, **calculée** et jamais saisie : partie entière de log10(étoiles), bornée entre 1 et 5 (moins de 100 : ★ ; 100 000 et plus : ★★★★★). Seul compte un dépôt public consacré à l'outil ; sans dépôt public, ou pour un dépôt partagé (l'outil n'en est qu'un sous-dossier) ou annexe (SDK, skill d'accompagnement) : « — ». Elle n'entre pas dans le total /15 et ne fait monter aucune autre note. Une hausse brutale d'étoiles sans hausse des forks ni de l'activité est vérifiée avant d'être reportée (risque de fausses étoiles).
- Critères propres à l'outil (sécurité, couverture, coût…) : autorisés dans la fiche, hors barème, justifiés dans le texte.
- Changer une note : modifier d'abord la page de famille (justification comprise), puis la fiche et le tableau « Toutes les notes » du comparatif.

## Règles d'objectivité

- Aucun superlatif sans source indépendante ; attribuer les affirmations d'éditeur (« selon Anthropic », « annoncé par le projet »).
- Reporter dans la fiche les limites et risques majeurs de l'avis (sécurité, coûts, licence, controverses, recul faible).
- Les « Alternative à » nomment les vrais concurrents ; ne pas lier des outils de catégories différentes.
- Dates absolues (« 22 septembre 2026 »), jamais « récemment ».
- Un article modifié reçoit la date du jour dans `_Dernière analyse : … _` ; la section « Avis indépendants » (avec `avis_maj`) et le mémo sont revus en même temps si la fiche change sur le fond.

## Liste de contrôle (à exécuter depuis `content/`)

```bash
# 1. Fiches sans section d'avis ou sans mémo (SANS_MEMO : outils en ligne sans commandes à retenir)
SANS_MEMO="Banana Prompts|Claude Design|Gemini Deep Research|Higgsfield-ai-platform|NotebookLM|Opal by Google|Open Generative AI|Pomelli|Stitch by Google|Wispr Flow"
for f in outils/*/*.md; do b=$(basename "$f" .md); [ "$b" = index ] && continue; grep -q "^## Avis indépendants$" "$f" && grep -q "^### Sources des avis$" "$f" || echo "SANS AVIS : $b"; [ -f "memos/$b mémo.md" ] || echo "$b" | grep -qxE "$SANS_MEMO" || echo "SANS MÉMO : $b"; done

# 2. Fiches absentes de leur page de famille, de la vue d'ensemble, des pages métier ou du comparatif ; mémos absents de la bibliothèque
for f in outils/*/*.md; do b=$(basename "$f" .md); [ "$b" = index ] && continue; grep -qF "|[[$b]]|" "$(dirname "$f")/index.md" || echo "HORS FAMILLE : $b"; grep -qF "[[$b]]" outils/index.md || echo "HORS VUE D'ENSEMBLE : $b"; grep -qF "[[$b]]" metiers/*.md || echo "HORS MÉTIER : $b"; grep -qF "|[[$b]]|" "methode/Comparatif global des outils.md" || echo "HORS COMPARATIF : $b"; done
for f in memos/*.md; do b=$(basename "$f" .md); [ "$b" = index ] && continue; grep -qF "[[$b|" memos/index.md || echo "HORS BIBLIOTHÈQUE : $b"; done

# 3. Artefacts à ne pas publier (les gabarits gardent volontairement leur commentaire)
grep -rl -E "contentReference|oaicite|<!-- Métadonnées" --include="*.md" . | grep -v "_modeles/"

# 4. Frontmatter des fiches : type, tags de la Taxonomie, Popularité cohérente avec les étoiles
OK=$(grep -o -E '`(metier|theme)/[a-z-]+`' methode/Taxonomie.md | tr -d '`')
for f in outils/*/*.md; do [ "$(basename "$f")" = index.md ] && continue; grep -qx "type: outil" "$f" || echo "TYPE : $f"; for t in $(awk '/^---$/{n++; next} n==1 && /^tags:/{g=1; next} n==1 && /^[a-z_]+:/{g=0} n==1 && g && /^  - /{print $2}' "$f"); do echo "$OK" | grep -qx "$t" || echo "TAG HORS LISTE : $f : $t"; done; e=$(sed -n 's/^etoiles: //p' "$f"); p=$(sed -n 's/^note_popularite: //p' "$f"); if [ -n "$e" ]; then n=$(( ${#e} - 1 )); [ $n -lt 1 ] && n=1; [ $n -gt 5 ] && n=5; [ "$p" = "$n" ] || echo "POPULARITÉ : $f ($e étoiles, note $p, attendu $n)"; fi; done

# 5. Notes : la fiche, sa page de famille et le tableau « Toutes les notes » concordent
for f in outils/*/*.md; do b=$(basename "$f" .md); [ "$b" = index ] && continue; v=$(sed -n 's/^note_documentation: //p; s/^note_precision: //p; s/^note_maturite: //p' "$f" | tr '\n' ' '); r=$(grep -F "|[[$b]]|" "$(dirname "$f")/index.md" | grep "★" | awk -F'|' '{for(i=3;i<=5;i++){s=$i; printf "%d ", gsub(/★/,"",s)}}'); [ "$v" = "$r" ] || echo "NOTES : $b (fiche $v, famille $r)"; t=$(grep -F "|[[$b]]|" "methode/Comparatif global des outils.md" | awk -F'|' '{print $(NF-2)}'); [ "$t" = "$(echo "$v" | awk '{print $1+$2+$3}')" ] || echo "TOTAL : $b (comparatif $t, fiche $v)"; done

# 6. Liens : doublons de noms, liens ambigus, chemins et ancres introuvables
python3 ../scripts/verifier_liens.py

# 7. Titres : le « # Titre » qui ouvre une page reprend exactement son `title` (le site affiche le `title` et masque le « # Titre »)
find . -name "*.md" -not -path "./_modeles/*" -print0 | while IFS= read -r -d '' f; do h=$(awk '/^---$/{n++; next} n>=2 && NF{print; exit}' "$f"); case "$h" in "# "*) t=$(awk '/^---$/{n++; next} n==1 && /^title:/{sub(/^title: */,""); gsub(/^"|"$/,""); print; exit}' "$f"); [ "# $t" = "$h" ] || echo "TITRE : $f ($t / $h)";; esac; done

# 8. Site : la construction aboutit sans erreur (depuis la racine du projet)
(cd .. && npx quartz build 2>&1 | grep -iE "error|erreur|failed|✗")

# 9. Mémos PDF absents, plus anciens que leur mémo ou leur fiche, ou orphelins (régénérer : python3 ../scripts/memos_pdf/generer.py --modifies)
python3 ../scripts/memos_pdf/generer.py --verifier
```

Relever à nouveau les étoiles et les forks (API publique de GitHub) avant chaque publication, et mettre à jour `etoiles_releve`.

## Ce qu'il ne faut pas faire

- Ne pas publier, pousser ni committer sans demande explicite (publication manuelle, voir `projet.md`).
- Ne pas supprimer, renommer, déplacer ou fusionner de fichiers sans demande.
- Ne pas recopier les textes des sources : synthétiser, avec liens.
