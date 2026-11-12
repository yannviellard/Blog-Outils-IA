// Composant « Fiche » de AI Tools Wiki : affiche en français les propriétés du
// frontmatter que le panneau de Quartz montrerait avec leurs clés brutes.
//   - fiche outil (type: outil) : format, éditeur, statut, licence, site, dépôt,
//     notes et total /15, popularité, mémo, avis, métiers et thèmes ;
//   - mémo (type: memo) : lien vers la fiche de l'outil ;
//   - autre page avec des tags : métiers et thèmes.
// Les libellés des tags viennent des pages de content/tags/.

import { h } from "preact"
import { resolveRelative, slugTag } from "@quartz-community/utils/path"

const FORMATS = {
  agent: "Agent",
  skill: "Skill",
  collection: "Collection",
  plugin: "Plugin",
  "serveur-mcp": "Serveur MCP",
  cli: "Outil en ligne de commande",
  api: "API",
  bibliotheque: "Bibliothèque",
  application: "Application",
  plateforme: "Plateforme",
}

const STATUTS = {
  disponible: "Disponible",
  preversion: "Préversion",
  retire: "Retiré",
}

const nombre = (n) => Number(n).toLocaleString("fr-FR")

function date(d) {
  if (!d) return null
  const x = d instanceof Date ? d : new Date(String(d))
  if (Number.isNaN(x.getTime())) return String(d)
  return x.toLocaleDateString("fr-FR", { day: "numeric", month: "long", year: "numeric", timeZone: "UTC" })
}

function etoiles(n) {
  const v = Math.max(0, Math.min(5, Number(n) || 0))
  return h("span", { class: "fiche-etoiles", "aria-label": `${v} sur 5` }, "★".repeat(v) + "☆".repeat(5 - v))
}

// Nom de fichier visé par un wikilink « [[Nom]] » ou « [[Nom|texte]] ».
function cibleWikilink(valeur) {
  const m = /^\[\[([^\]|#]+)/.exec(String(valeur ?? "").trim())
  return m ? m[1].trim() : null
}

function trouverParNom(allFiles, nom) {
  return allFiles.find((f) => {
    const p = String(f.filePath ?? "")
    const base = p.slice(p.lastIndexOf("/") + 1).replace(/\.md$/, "")
    return base === nom
  })
}

function lienInterne(slug, cible, texte) {
  return h("a", { href: resolveRelative(slug, cible.slug), class: "internal" }, texte ?? cible.frontmatter?.title)
}

function lienExterne(url, texte) {
  return h("a", { href: url, class: "external", rel: "noopener noreferrer" }, texte)
}

function texteSite(url) {
  try {
    const u = new URL(url)
    return (u.hostname.replace(/^www\./, "") + u.pathname).replace(/\/$/, "")
  } catch {
    return url
  }
}

function texteDepot(url) {
  const m = /github\.com\/([^/]+\/[^/#?]+)/.exec(url)
  return m ? m[1].replace(/\.git$/, "") : texteSite(url)
}

// Libellé d'un tag : titre de sa page de description, sans le préfixe « Métier : ».
function libelleTag(allFiles, tag) {
  const page = allFiles.find((f) => f.slug === `tags/${tag}`)
  const titre = page?.frontmatter?.title
  if (!titre) return tag
  const i = titre.indexOf(" : ")
  return i >= 0 ? titre.slice(i + 3) : titre
}

function puces(slug, allFiles, tags) {
  return tags.map((tag) =>
    h(
      "a",
      { href: resolveRelative(slug, `tags/${slugTag(tag)}`), class: "internal fiche-tag" },
      libelleTag(allFiles, tag),
    ),
  )
}

function ligne(libelle, ...contenu) {
  const valeurs = contenu.flat().filter((c) => c !== null && c !== undefined && c !== false && c !== "")
  if (valeurs.length === 0) return null
  return h("div", { class: "fiche-ligne" }, h("dt", null, libelle), h("dd", null, ...valeurs))
}

function lignesTags(slug, allFiles, tags) {
  const liste = Array.isArray(tags) ? tags.map(String) : []
  const metiers = liste.filter((t) => t.startsWith("metier/"))
  const themes = liste.filter((t) => t.startsWith("theme/"))
  const autres = liste.filter((t) => !t.startsWith("metier/") && !t.startsWith("theme/"))
  return [
    metiers.length ? ligne(metiers.length > 1 ? "Métiers" : "Métier", puces(slug, allFiles, metiers)) : null,
    themes.length ? ligne(themes.length > 1 ? "Thèmes" : "Thème", puces(slug, allFiles, themes)) : null,
    autres.length ? ligne("Tags", puces(slug, allFiles, autres)) : null,
  ]
}

function ficheOutil(slug, fm, allFiles) {
  const dossier = slug.slice(0, slug.lastIndexOf("/"))
  const famille = allFiles.find((f) => f.slug === `${dossier}/index`)
  const memo = cibleWikilink(fm.memo) ? trouverParNom(allFiles, cibleWikilink(fm.memo)) : null

  const notes = [fm.note_documentation, fm.note_precision, fm.note_maturite].map(Number)
  const noteOk = notes.every((n) => Number.isInteger(n))
  const total = noteOk ? notes.reduce((a, b) => a + b, 0) : null

  const popularite =
    fm.note_popularite !== undefined && fm.note_popularite !== null && fm.note_popularite !== ""
      ? [
          etoiles(fm.note_popularite),
          fm.etoiles
            ? ` ${nombre(fm.etoiles)} étoiles${fm.forks ? ` et ${nombre(fm.forks)} forks` : ""} sur GitHub` +
              (fm.etoiles_releve ? `, relevé du ${date(fm.etoiles_releve)}` : "")
            : null,
        ]
      : "— (pas de dépôt public consacré à l'outil)"

  return [
    ligne("Format", FORMATS[fm.format] ?? fm.format),
    ligne("Éditeur", fm.editeur),
    ligne("Statut", STATUTS[fm.statut] ?? fm.statut),
    ligne("Licence", fm.licence),
    ligne("Site", fm.site ? lienExterne(fm.site, texteSite(fm.site)) : null),
    ligne(
      "Dépôt",
      fm.depot ? lienExterne(fm.depot, texteDepot(fm.depot)) : null,
      fm.depot && fm.derniere_maj ? `, dernière activité le ${date(fm.derniere_maj)}` : null,
    ),
    noteOk
      ? ligne(
          "Notes",
          h(
            "span",
            { class: "fiche-notes" },
            h("strong", null, `${total}/15`),
            h("span", null, "Documentation ", etoiles(notes[0])),
            h("span", null, "Précision ", etoiles(notes[1])),
            h("span", null, "Maturité ", etoiles(notes[2])),
          ),
          famille
            ? h("span", { class: "fiche-renvoi" }, "Justification : page ", lienInterne(slug, famille), ".")
            : null,
        )
      : null,
    ligne("Popularité", popularite),
    ligne("Mémo", memo ? lienInterne(slug, memo) : null),
    ligne(
      "Avis",
      fm.avis_maj
        ? h("a", { href: "#avis-indépendants", class: "internal" }, `synthèse du ${date(fm.avis_maj)}`)
        : null,
    ),
    ...lignesTags(slug, allFiles, fm.tags),
  ]
}

function ficheMemo(slug, fm, allFiles) {
  const nom = cibleWikilink(fm.fiche)
  const fiche = nom ? trouverParNom(allFiles, nom) : null
  return [ligne("Fiche", fiche ? lienInterne(slug, fiche) : nom), ...lignesTags(slug, allFiles, fm.tags)]
}

const style = `
.fiche {
  margin: 1rem 0 1.5rem;
  padding: 0.6rem 1rem;
  border: 1px solid var(--lightgray);
  border-radius: 6px;
  font-size: 0.92rem;
}
.fiche dl {
  margin: 0;
}
.fiche-ligne {
  display: grid;
  grid-template-columns: 7.5rem 1fr;
  gap: 0.75rem;
  padding: 0.3rem 0;
  border-bottom: 1px solid var(--lightgray);
}
.fiche-ligne:last-child {
  border-bottom: none;
}
/* Sélecteurs renforcés : le thème de Quartz met une marge sur « html[saved-theme] body dd ». */
html body .fiche .fiche-ligne dt {
  margin: 0;
  color: var(--gray);
  font-weight: 600;
}
html body .fiche .fiche-ligne dd {
  margin: 0;
  color: var(--darkgray);
}
.fiche-etoiles {
  color: var(--secondary);
  letter-spacing: 0.05em;
  white-space: nowrap;
}
.fiche-notes {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem 1rem;
}
.fiche-notes span {
  white-space: nowrap;
}
.fiche-renvoi {
  display: block;
  color: var(--gray);
}
.fiche a.fiche-tag {
  display: inline-block;
  margin: 0 0.4rem 0.2rem 0;
  padding: 0 0.45rem;
  border-radius: 6px;
  background-color: var(--highlight);
  font-size: 0.88rem;
}
@media all and (max-width: 600px) {
  .fiche-ligne {
    grid-template-columns: 1fr;
    gap: 0.1rem;
  }
}
`

function FicheConstructeur() {
  const Fiche = ({ fileData, allFiles, displayClass }) => {
    const fm = fileData?.frontmatter ?? {}
    const slug = fileData?.slug ?? ""
    const fichiers = allFiles ?? []
    let lignes
    if (fm.type === "outil") lignes = ficheOutil(slug, fm, fichiers)
    else if (fm.type === "memo") lignes = ficheMemo(slug, fm, fichiers)
    else lignes = lignesTags(slug, fichiers, fm.tags)
    lignes = lignes.filter(Boolean)
    if (lignes.length === 0) return null
    const classes = ["fiche", displayClass].filter(Boolean).join(" ")
    return h("section", { class: classes, "aria-label": "Fiche" }, h("dl", null, ...lignes))
  }
  Fiche.css = style
  return Fiche
}

export { FicheConstructeur as Fiche }
