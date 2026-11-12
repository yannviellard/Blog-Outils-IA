// Plugin local de AI Tools Wiki (écrit à la main, sans étape de compilation :
// Quartz charge directement dist/). Voir README.md.
//
// Transformateur : retire le titre de niveau 1 qui ouvre le corps de la page.
// Quartz affiche déjà le `title` du frontmatter en tête de page ; le `# Titre`
// reste dans les fichiers pour la lecture dans Obsidian.

function retirerTitreInitial() {
  return (tree) => {
    const i = tree.children.findIndex((n) => n.type !== "yaml" && n.type !== "toml")
    const premier = tree.children[i]
    if (premier && premier.type === "heading" && premier.depth === 1) {
      tree.children.splice(i, 1)
    }
  }
}

export default function WikiFiche() {
  return {
    name: "WikiFiche",
    markdownPlugins() {
      return [retirerTitreInitial]
    },
  }
}
