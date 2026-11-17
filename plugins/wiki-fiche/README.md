# wiki-fiche

Plugin local de Quartz pour AI Tools Wiki, déclaré dans `quartz.config.yaml` (`source: ./plugins/wiki-fiche`).

- **Encadré « Fiche »** (`dist/components/index.js`) : affiche en français, en tête de page, les propriétés du frontmatter. Sur une fiche outil : format, éditeur, statut, licence, site, dépôt, notes et total /15, popularité, mémo, date des avis, métiers et thèmes. Sur un mémo : le lien vers la fiche. Sur les autres pages : les tags. Le panneau de propriétés de Quartz, qui montre les clés brutes sous le titre « Properties », est masqué.
- **Thème clair par défaut** (`Fiche.beforeDOMLoaded`, dans `dist/components/index.js`) : le plugin `darkmode` suit le réglage du système, sans option pour changer ce comportement. Un court script enregistre donc le thème clair (clé `theme` du `localStorage`) à la première visite ; le bouton du plugin `darkmode` permet toujours de passer en sombre, et le choix est retenu. Le script est chargé avec toutes les pages, car l'encadré fait partie de la mise en page commune.
- **Mémo PDF** (`dist/index.js` et encadré) : si `content/memos/pdf/<Nom mémo>.pdf` existe (généré par `scripts/memos_pdf/generer.py`), le transformateur relève son nombre de pages et son poids (`file.data.memoPdf`). Sur la fiche, l'encadré ajoute le lien « PDF » à la ligne Mémo, et une section « Mémo pratique » (aperçu `.jpg` cliquable et lien de téléchargement) est insérée avant « Avis indépendants », ou avant « Sources » à défaut. Sur la page du mémo, l'encadré ajoute une ligne « PDF ». Rien n'est écrit dans les fichiers Markdown : la section n'existe que sur le site.
- **Titre unique** (`dist/index.js`) : retire du rendu le `# Titre` qui ouvre le corps de la page, puisque Quartz affiche déjà le `title` du frontmatter. Le `# Titre` reste dans les fichiers pour Obsidian ; il doit reprendre exactement le `title` (contrôle n° 7 de `CLAUDE.md`).

Le code est écrit directement en JavaScript dans `dist/`, sans étape de compilation : Quartz charge `dist/` tel quel. Les dépendances (`preact`, `@quartz-community/utils`) sont celles du projet.

Après une modification, relancer `npx quartz build --serve`. Si Quartz ne trouve plus le plugin : `npx quartz plugin install --from-config`.

## Particularités de Quartz 5 relevées en le construisant

- Le CSS des composants est placé dans la couche `@layer quartz-base`, qui perd face au thème (non rangé dans une couche) quelle que soit la spécificité : une règle qui doit l'emporter sur le thème demande `!important`.
- La mise en page exportée par `quartz.ts` (`export const layout`) n'est pas utilisée pour générer les pages : Quartz relit `quartz.config.yaml`. Seules les options de composants passent par `quartz.ts` (`componentRegistry.setOptionOverrides`, clé = la `source` du plugin, par exemple `@quartz-community/explorer`).
- La fonction de tri de l'explorateur est recopiée sous forme de texte dans le navigateur : elle ne peut utiliser aucune variable ni fonction extérieure.
- Un lien ou une image ajoutés à l'arbre Markdown par un transformateur passent ensuite par `crawl-links`, qui calcule le chemin relatif : il suffit de donner le chemin depuis la racine du contenu (`memos/pdf/playwright-mémo.pdf`). Les fichiers non Markdown (PDF, images) font partie des pages connues, donc leurs liens ne sont pas grisés comme liens sans cible.
- Les noms de fichiers doivent être en Unicode composé (NFC) : un « é » décomposé (écrit ainsi par certains outils macOS, comme `sips`) donne une URL que le serveur ne trouve pas.
