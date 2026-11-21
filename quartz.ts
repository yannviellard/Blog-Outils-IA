import { loadQuartzConfig, loadQuartzLayout } from "./quartz/plugins/loader/config-loader"
import { componentRegistry } from "./quartz/components/registry"

// Explorateur : rubriques et familles dans l'ordre du wiki (zones de la page
// outils/index.md) plutôt que par ordre alphabétique. La fonction est recopiée
// telle quelle dans le navigateur : elle ne doit utiliser aucune variable extérieure.
componentRegistry.setOptionOverrides("@quartz-community/explorer", {
  sortFn: (a: any, b: any) => {
    const ordre = [
      "outils", "memos", "metiers", "concepts", "guides", "methode",
      "agents-de-developpement", "postes-de-pilotage", "methodes-de-developpement",
      "orchestration-et-catalogues", "memoire-et-contexte",
      "revue-et-securite", "navigateur-et-tests", "backend-et-deploiement",
      "prototypage-en-ligne", "design-en-code", "modeles",
      "automatisation-de-workflows", "recherche-et-veille", "marketing-et-seo", "image-video-medias",
      "ecriture-voix-messagerie", "finance-juridique-decision",
    ]
    const ia = a.isFolder ? ordre.indexOf(a.slugSegment) : -1
    const ib = b.isFolder ? ordre.indexOf(b.slugSegment) : -1
    if (ia !== -1 && ib !== -1) return ia - ib
    if (a.isFolder !== b.isFolder) return a.isFolder ? -1 : 1
    if (ia !== -1 || ib !== -1) return ia !== -1 ? -1 : 1
    return a.displayName.localeCompare(b.displayName, "fr", { numeric: true, sensitivity: "base" })
  },
})

const config = await loadQuartzConfig()
export default config

export const layout = await loadQuartzLayout()
