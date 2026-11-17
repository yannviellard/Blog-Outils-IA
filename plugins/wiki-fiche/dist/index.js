// Plugin local de AI Tools Wiki (écrit à la main, sans étape de compilation :
// Quartz charge directement dist/). Voir README.md.
//
// Transformateurs :
// 1. retire le titre de niveau 1 qui ouvre le corps de la page. Quartz affiche
//    déjà le `title` du frontmatter en tête de page ; le `# Titre` reste dans les
//    fichiers pour la lecture dans Obsidian ;
// 2. mémo PDF : si content/memos/pdf/<Nom mémo>.pdf existe (généré par
//    scripts/memos_pdf/generer.py), note ses caractéristiques dans file.data.memoPdf
//    (lues par l'encadré « Fiche ») et, sur une fiche outil, insère une section
//    « Mémo pratique » (aperçu et lien de téléchargement) avant « Avis indépendants ».

import fs from "fs"
import path from "path"
import { slugifyFilePath } from "@quartz-community/utils/path"

function retirerTitreInitial() {
  return (tree) => {
    const i = tree.children.findIndex((n) => n.type !== "yaml" && n.type !== "toml")
    const premier = tree.children[i]
    if (premier && premier.type === "heading" && premier.depth === 1) {
      tree.children.splice(i, 1)
    }
  }
}

// Nom de fichier visé par un wikilink « [[Nom]] » ou « [[Nom|texte]] ».
function cibleWikilink(valeur) {
  const m = /^\[\[([^\]|#]+)/.exec(String(valeur ?? "").trim())
  return m ? m[1].trim() : null
}

function texte(noeud) {
  if (noeud.type === "text" || noeud.type === "inlineCode") return noeud.value
  return (noeud.children ?? []).map(texte).join("")
}

// Le PDF du mémo et son aperçu, s'ils ont été générés.
function infosPdf(contenu, nomMemo) {
  const base = path.join(contenu, "memos", "pdf", nomMemo)
  if (!fs.existsSync(base + ".pdf")) return null
  const octets = fs.readFileSync(base + ".pdf")
  return {
    pdf: slugifyFilePath(`memos/pdf/${nomMemo}.pdf`),
    apercu: fs.existsSync(base + ".jpg") ? slugifyFilePath(`memos/pdf/${nomMemo}.jpg`) : null,
    memo: slugifyFilePath(`memos/${nomMemo}.md`),
    pages: (octets.toString("latin1").match(/\/Type\s*\/Page[^s]/g) ?? []).length,
    ko: Math.round(octets.length / 1024),
  }
}

// « 1 page A4 paysage, 190 Ko »
function descriptionPdf(infos) {
  const pages = `${infos.pages} page${infos.pages > 1 ? "s" : ""}`
  return `${pages} A4 paysage, ${infos.ko.toLocaleString("fr-FR")} Ko`
}

const lien = (url, ...enfants) => ({ type: "link", url, title: null, children: enfants })
const txt = (value) => ({ type: "text", value })

function insererSection(tree, infos, titre) {
  const titre2 = (nom) =>
    tree.children.findIndex((n) => n.type === "heading" && n.depth === 2 && texte(n).trim() === nom)
  let i = titre2("Avis indépendants")
  if (i < 0) i = titre2("Sources")
  if (i < 0) i = tree.children.length

  const section = [{ type: "heading", depth: 2, children: [txt("Mémo pratique")] }]
  if (infos.apercu) {
    section.push({
      type: "paragraph",
      children: [
        lien(infos.pdf, {
          type: "image",
          url: infos.apercu,
          title: null,
          alt: `Aperçu de la première page du mémo PDF de ${titre}`,
          // A4 paysage, aperçu de 1 100 px : dimensions connues, pas de saut de mise en page
          data: { hProperties: { className: ["memo-apercu"], width: 1100, height: 778, loading: "lazy" } },
        }),
      ],
    })
  }
  section.push({
    type: "paragraph",
    children: [
      lien(infos.pdf, txt("Télécharger le mémo en PDF")),
      txt(` (${descriptionPdf(infos)}). Il est généré depuis la `),
      lien(infos.memo, txt("page du mémo")),
      txt(", qui reste la version de référence : commandes à copier, recherche dans le site."),
    ],
  })
  tree.children.splice(i, 0, ...section)
}

function memoPdf(ctx) {
  const contenu = path.resolve(ctx?.argv?.directory ?? "content")
  return () => (tree, file) => {
    const fm = file.data?.frontmatter ?? {}
    let nom = null
    if (fm.type === "outil") nom = cibleWikilink(fm.memo)
    else if (fm.type === "memo") nom = path.basename(String(file.path ?? ""), ".md")
    if (!nom) return
    const infos = infosPdf(contenu, nom)
    if (!infos) return
    file.data.memoPdf = { ...infos, description: descriptionPdf(infos) }
    if (fm.type === "outil") insererSection(tree, infos, fm.title ?? nom)
  }
}

export default function WikiFiche() {
  return {
    name: "WikiFiche",
    markdownPlugins(ctx) {
      return [retirerTitreInitial, memoPdf(ctx)]
    },
  }
}
