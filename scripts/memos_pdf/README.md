# Mémos PDF

Génère, pour chaque mémo de `content/memos/`, un aide-mémoire PDF au format A4 paysage, sur le modèle des fiches de référence (DataCamp, Enthought) : trois colonnes de blocs à bandeau de couleur, commandes à gauche et description à droite.

Le mémo Markdown reste la **source unique** : le script ne fait que le mettre en page. Une commande corrigée dans le mémo est corrigée dans le PDF à la génération suivante.

## Utilisation

Depuis la racine du projet :

```bash
python3 scripts/memos_pdf/generer.py "Playwright mémo"
```

```bash
python3 scripts/memos_pdf/generer.py --modifies
```

```bash
python3 scripts/memos_pdf/generer.py --tous
```

```bash
python3 scripts/memos_pdf/generer.py --verifier
```

- un ou plusieurs mémos nommés : après la création ou la modification d'un mémo ;
- `--modifies` : les mémos sans PDF, ou dont le mémo ou la fiche est plus récent que le PDF (la fiche fournit l'en-tête : famille, éditeur, licence, note) ;
- `--tous` : tous les mémos, après une modification du gabarit (`gabarit.css`, `mise_en_page.js`, `generer.py`) ;
- `--verifier` : ne génère rien ; liste les PDF absents ou périmés et les fichiers orphelins (contrôle n° 9 de `CLAUDE.md`).

Les fichiers vont dans `content/memos/pdf/`, d'où le site les publie : `Nom mémo.pdf` et `Nom mémo.jpg` (aperçu de la première page, 1 100 px, environ 280 Ko). Le plugin `plugins/wiki-fiche/` les affiche sur la fiche (section « Mémo pratique ») et sur la page du mémo. Pour un essai hors du site : `--sortie <dossier> --html` (garde aussi la page HTML intermédiaire, à ouvrir dans un navigateur pour ajuster le gabarit ; refusé dans `content/`, que Quartz publierait). Compter une minute environ pour les 60 mémos (`--parallele`, 3 Chrome par défaut).

Le script affiche, pour chaque mémo, le nombre de pages et la taille de texte retenue, puis :

- **À REVOIR** : bloc coupé en bas de colonne (élément trop haut pour une colonne entière, donc rogné), contenu trop large pour son bloc (ligne de code insécable, rognée), Markdown non converti (`**`, `[[`, ```` ``` ````… hors code) ;
- **SANS MÉMO** : PDF ou aperçu d'un mémo supprimé ou renommé, à supprimer ;
- **NOM DÉCOMPOSÉ** : nom de fichier dont les accents sont en Unicode décomposé ; l'URL ne le trouverait pas sur le serveur. Le script écrit les noms en forme composée ; ce message ne devrait apparaître que pour un fichier copié à la main.

Dépendances : Python 3 (bibliothèque standard seule), Google Chrome (impression PDF sans interface, avec un profil temporaire), `sips` de macOS pour l'aperçu, polices système Avenir Next et Menlo. Sur un Mac Apple Silicon, Chrome est lancé en mode natif (`arch -arm64`) : depuis un Python Intel, qui tourne sous Rosetta, il démarrerait en x86_64, environ quatre fois plus lent.

## Fonctionnement

- `generer.py` lit le mémo et sa fiche (famille, éditeur, licence, notes), convertit le Markdown (titres `##` et `###`, tableaux, blocs de code, listes, citations et encadrés Obsidian, gras, code, liens) en blocs HTML, puis fait imprimer la page par Chrome.
- Dans un bloc `bash`, une ligne `# commentaire` devient la description des commandes qui la suivent ; un commentaire en fin de ligne devient la description de cette commande.
- `mise_en_page.js` remplit les colonnes une à une et choisit la plus grande taille de texte (de 10,5 à 7 pt) qui tient sur une page, sinon deux, sinon trois ; au-delà, la plus grande taille qui tient sur le moins de pages. La mesure garde 4 % de marge, car le texte se coupe un peu autrement à l'impression.
- Coupures : un bloc trop long reprend dans la colonne suivante sous « Titre (suite) », entre deux lignes de tableau ou de liste. L'en-tête du tableau est répété dans la suite, une liste numérotée garde sa numérotation, et un intertitre ou une phrase d'annonce (« … : ») ne reste jamais seul en bas de colonne.
- `gabarit.css` : mise en forme. Couleur selon la zone de la famille de l'outil (orange : poste de travail de l'agent ; bleu : construire et livrer ; vert : produire et décider).

Les wikiliens du mémo deviennent du texte en gras. Le pied de page indique l'adresse du site et la date de génération ; l'en-tête, l'adresse de la fiche.
