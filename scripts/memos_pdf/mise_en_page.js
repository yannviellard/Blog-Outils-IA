// Mise en page des mémos PDF : répartit les blocs dans des pages A4 de trois
// colonnes et choisit la plus grande taille de texte qui tient sur le moins de pages.
// Exécuté par Chrome avant l'impression.
//
// - Les colonnes sont des boîtes de hauteur fixe, remplies l'une après l'autre.
// - Un bloc trop long est coupé entre deux lignes (jamais au milieu d'une ligne de
//   tableau) et reprend dans la colonne suivante sous « Titre (suite) ».
// - La mesure se fait avec une marge de sécurité (classe « mesure ») : à
//   l'impression, le texte se coupe un peu différemment qu'à l'écran.

;(function () {
  const ESSAIS = [
    { pages: 1, tailles: [10.5, 10, 9.5, 9, 8.5, 8, 7.5] },
    { pages: 2, tailles: [10, 9.5, 9, 8.5, 8, 7.5, 7] },
    { pages: 3, tailles: [9.5, 9, 8.5, 8, 7.5, 7] },
  ]
  const COLONNES_PAR_PAGE = 3
  const source = document.getElementById("source")
  const pages = document.getElementById("pages")
  const modelePied = document.getElementById("modele-pied")
  // Problèmes relevés pour le script Python (attribut data-alertes du body)
  let alertes = []
  const titreDe = (bloc) => (bloc.querySelector("h2") ? bloc.querySelector("h2").textContent : "en-tête")

  function nouvellePage() {
    const page = document.createElement("div")
    page.className = "page"
    const grille = document.createElement("div")
    grille.className = "colonnes"
    const colonnes = []
    for (let i = 0; i < COLONNES_PAR_PAGE; i++) {
      const c = document.createElement("div")
      c.className = "colonne"
      grille.appendChild(c)
      colonnes.push(c)
    }
    page.append(grille, modelePied.content.cloneNode(true))
    pages.appendChild(page)
    return colonnes
  }

  function deborde(colonne) {
    return colonne.scrollHeight > colonne.clientHeight + 1
  }

  // Éléments découpables ligne à ligne : tableaux et listes.
  function lignes(el) {
    if (el.tagName === "TABLE") return Array.from(el.querySelectorAll("tr"))
    if (el.tagName === "UL" || el.tagName === "OL") return Array.from(el.children)
    return null
  }

  // Éléments qui annoncent ce qui suit : jamais seuls en bas de colonne.
  function annonce(el) {
    return (
      el.classList.contains("pastille") ||
      el.classList.contains("intertitre") ||
      (el.tagName === "P" && /:\s*$/.test(el.textContent))
    )
  }

  // Remet dans la colonne les premières lignes d'un tableau ou d'une liste qui y tiennent ;
  // le reste (enfant) part dans la suite, avec l'en-tête du tableau répété.
  function garderDebut(enfant, items, corps, colonne) {
    const entete = enfant.tagName === "TABLE" && items[0].querySelector("th") ? 1 : 0
    const partiel = enfant.cloneNode(false)
    corps.appendChild(partiel)
    let n = 0
    for (const item of items) {
      partiel.appendChild(item.cloneNode(true))
      if (deborde(colonne)) {
        partiel.lastElementChild.remove()
        break
      }
      n++
    }
    // Pas de ligne de groupe (titre d'une série de commandes) en dernière ligne
    while (n > entete && items[n - 1].querySelector("td.groupe")) {
      n--
      partiel.lastElementChild.remove()
    }
    // Rien d'utile ne tient (en-tête seul) ou tout tient : pas de coupure
    if (n <= entete || n === items.length) {
      partiel.remove()
      return
    }
    items.slice(0, n).forEach((x) => x.remove())
    if (entete) {
      const premiere = enfant.querySelector("tr")
      premiere.parentNode.insertBefore(items[0].cloneNode(true), premiere)
    }
    // Liste numérotée : la suite reprend la numérotation
    if (enfant.tagName === "OL") {
      enfant.setAttribute("start", String(Number(enfant.getAttribute("start") || 1) + n))
    }
  }

  // Le bloc déborde de la colonne : on garde ce qui tient, le reste part dans un
  // bloc « suite ». Renvoie ce bloc, ou null si rien du bloc ne tient (bloc retiré).
  function scinder(bloc, colonne) {
    const corps = bloc.querySelector(".corps")
    if (!corps) {
      bloc.remove()
      return null
    }
    const suite = bloc.cloneNode(false)
    const titre = bloc.querySelector("h2").cloneNode(true)
    titre.textContent = titre.textContent.replace(/ \(suite\)$/, "") + " (suite)"
    const corpsSuite = document.createElement("div")
    corpsSuite.className = "corps"
    suite.append(titre, corpsSuite)

    while (deborde(colonne) && corps.firstElementChild) {
      const enfant = corps.lastElementChild
      corpsSuite.prepend(enfant)
      if (deborde(colonne)) continue
      // Ça tient sans cet élément : on en remet les premières lignes qui tiennent.
      const items = lignes(enfant)
      if (items && items.length > 1) garderDebut(enfant, items, corps, colonne)
    }
    // Pas d'intertitre ni de phrase d'annonce (« … : ») orphelins en bas de colonne
    while (corpsSuite.firstElementChild && corps.lastElementChild && annonce(corps.lastElementChild)) {
      corpsSuite.prepend(corps.lastElementChild)
    }
    if (!corps.firstElementChild) {
      while (corpsSuite.firstElementChild) corps.appendChild(corpsSuite.firstElementChild)
      bloc.remove()
      return null
    }
    return suite
  }

  // Place tous les blocs en au plus maxPages pages ; renvoie le nombre de pages ou 0.
  function essayer(taille, maxPages) {
    document.documentElement.style.fontSize = taille + "pt"
    pages.innerHTML = ""
    alertes = []
    let colonnes = nouvellePage()
    let n = 1
    let i = 0
    const suivante = () => {
      i++
      if (i < COLONNES_PAR_PAGE) return true
      if (n >= maxPages) return false
      colonnes = nouvellePage()
      n++
      i = 0
      return true
    }
    const file = Array.from(source.children).map((b) => b.cloneNode(true))
    while (file.length) {
      const bloc = file.shift()
      const colonne = colonnes[i]
      const seul = colonne.children.length === 0
      colonne.appendChild(bloc)
      if (!deborde(colonne)) continue
      const suite = scinder(bloc, colonne)
      if (!suite && seul) {
        // Même seul en haut d'une colonne, son premier élément ne tient pas : on le laisse.
        colonne.appendChild(bloc)
        alertes.push("coupé en bas de colonne : " + titreDe(bloc))
        if (!suivante()) return 0
        continue
      }
      if (!suivante()) return 0
      file.unshift(suite || bloc)
    }
    return n
  }

  document.body.classList.add("mesure")
  let resultat = null
  for (const essai of ESSAIS) {
    for (const taille of essai.tailles) {
      const n = essayer(taille, essai.pages)
      if (n) {
        resultat = { taille, n }
        break
      }
    }
    if (resultat) break
  }
  // Mémo très long : au-delà de trois pages, la plus grande taille qui tient sur
  // le moins de pages, plutôt qu'une dernière page presque vide en 7 pt.
  for (let p = 4; p <= 12 && !resultat; p++) {
    for (const taille of [9.5, 9, 8.5, 8, 7.5, 7]) {
      const n = essayer(taille, p)
      if (n) {
        resultat = { taille, n }
        break
      }
    }
  }
  if (!resultat) resultat = { taille: 7, n: essayer(7, 99) }
  document.body.classList.remove("mesure")

  const total = pages.children.length
  pages.querySelectorAll(".numero").forEach((el, k) => {
    el.textContent = total > 1 ? `${k + 1} / ${total}` : ""
  })
  // Contenu plus large que son bloc (ligne de code insécable) : il serait rogné.
  pages.querySelectorAll(".bloc, .entete").forEach((bloc) => {
    if (bloc.scrollWidth > bloc.clientWidth + 1) alertes.push("trop large : " + titreDe(bloc))
  })
  document.body.dataset.pages = String(total)
  document.body.dataset.taille = String(resultat.taille)
  document.body.dataset.alertes = alertes.join(" | ")
})()
