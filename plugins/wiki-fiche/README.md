# wiki-fiche

Plugin local de Quartz pour AI Tools Wiki, déclaré dans `quartz.config.yaml` (`source: ./plugins/wiki-fiche`).

- **Encadré « Fiche »** (`dist/components/index.js`) : affiche en français, en tête de page, les propriétés du frontmatter. Sur une fiche outil : format, éditeur, statut, licence, site, dépôt, notes et total /15, popularité, mémo, date des avis, métiers et thèmes. Sur un mémo : le lien vers la fiche. Sur les autres pages : les tags. Le panneau de propriétés de Quartz, qui montre les clés brutes sous le titre « Properties », est masqué.
- **Titre unique** (`dist/index.js`) : retire du rendu le `# Titre` qui ouvre le corps de la page, puisque Quartz affiche déjà le `title` du frontmatter. Le `# Titre` reste dans les fichiers pour Obsidian ; il doit reprendre exactement le `title` (contrôle n° 7 de `CLAUDE.md`).

Le code est écrit directement en JavaScript dans `dist/`, sans étape de compilation : Quartz charge `dist/` tel quel. Les dépendances (`preact`, `@quartz-community/utils`) sont celles du projet.

Après une modification, relancer `npx quartz build --serve`. Si Quartz ne trouve plus le plugin : `npx quartz plugin install --from-config`.
