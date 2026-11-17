#!/usr/bin/env python3
"""Génère les mémos PDF de AI Tools Wiki à partir des mémos Markdown.

Chaque mémo (content/memos/<Nom> mémo.md) devient une page HTML mise en forme
(gabarit.css, mise_en_page.js), imprimée en PDF A4 paysage par Google Chrome
sans interface, plus une image d'aperçu (première page, en JPEG). Les deux vont
dans content/memos/pdf/, d'où le site les publie (fiche et page du mémo).

Le mémo Markdown reste la source unique : le PDF n'ajoute aucune commande.

Usage (depuis la racine du projet) :
    python3 scripts/memos_pdf/generer.py "Playwright mémo"     # un mémo
    python3 scripts/memos_pdf/generer.py --modifies            # mémos modifiés depuis leur PDF
    python3 scripts/memos_pdf/generer.py --tous                # tous (après un changement de gabarit)
    python3 scripts/memos_pdf/generer.py --tous --sortie essai --html   # essai hors du site

Dépendances : Python 3 (bibliothèque standard), Google Chrome, sips (macOS) pour l'aperçu.
"""

import argparse
import datetime
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import unicodedata
from concurrent.futures import ThreadPoolExecutor

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.abspath(os.path.join(ICI, "..", ".."))
CONTENU = os.path.join(RACINE, "content")
SITE = "aitoolswiki.viellard.fr"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août",
        "septembre", "octobre", "novembre", "décembre"]

# Couleurs par zone (voir outils/index.md) : fort, moyen, clair.
ZONES = {
    "poste": ("#c0592b", "#efc3a6", "#fbeee5"),
    "construire": ("#28679a", "#a9c8e2", "#e9f1f8"),
    "produire": ("#2c7a57", "#a8d5bf", "#e7f4ed"),
}
FAMILLES = {
    "poste": ["agents-de-developpement", "postes-de-pilotage", "methodes-de-developpement",
              "orchestration-et-catalogues", "memoire-et-contexte"],
    "construire": ["revue-et-securite", "navigateur-et-tests", "backend-et-deploiement",
                   "prototypage-en-ligne", "design-en-code", "modeles"],
    "produire": ["recherche-et-veille", "marketing-et-seo", "image-video-medias",
                 "ecriture-voix-messagerie", "finance-juridique-decision"],
}


# ---------------------------------------------------------------- lecture

def lire_frontmatter(texte):
    """Frontmatter simple (clé: valeur, listes « - x ») et corps."""
    m = re.match(r"^---\n(.*?)\n---\n", texte, re.S)
    if not m:
        return {}, texte
    fm, cle = {}, None
    for ligne in m.group(1).split("\n"):
        if re.match(r"^\s+- ", ligne) and cle:
            fm.setdefault(cle, [])
            if isinstance(fm[cle], list):
                fm[cle].append(ligne.strip()[2:].strip().strip('"'))
            continue
        mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", ligne)
        if mm:
            cle, val = mm.group(1), mm.group(2).strip()
            if len(val) >= 2 and val[0] == val[-1] == '"':
                val = val[1:-1]
            fm[cle] = val if val else []
    return fm, texte[m.end():]


def date_fr(iso):
    try:
        d = datetime.date.fromisoformat(str(iso)[:10])
    except ValueError:
        return str(iso)
    return f"{d.day}{'er' if d.day == 1 else ''} {MOIS[d.month - 1]} {d.year}"


def slug(chemin_relatif):
    """URL Quartz d'une page : chemin sans .md, espaces en tirets, minuscules."""
    s = chemin_relatif[:-3] if chemin_relatif.endswith(".md") else chemin_relatif
    s = s.replace(" ", "-").replace("&", "-and-").replace("%", "-percent")
    s = s.replace("?", "").replace("#", "")
    if s.endswith("/index"):
        s = s[: -len("/index")]
    return s.lower()


def trouver_fiche(nom):
    for dossier in sorted(os.listdir(os.path.join(CONTENU, "outils"))):
        chemin = os.path.join(CONTENU, "outils", dossier, nom + ".md")
        if os.path.isfile(chemin):
            return dossier, chemin
    return None, None


# ---------------------------------------------------------------- en ligne

def colorer_commande(code):
    """Coloration d'une commande shell : programme, options, chaînes, paramètres."""
    jetons = re.findall(r'"[^"]*"|\'[^\']*\'|<[^>\s][^>]*>|\[[^\]\s]+\]|\s+|[^\s"\'<]+|.', code)
    sortie, premier = [], True
    for j in jetons:
        e = html.escape(j)
        if j.isspace():
            sortie.append(e)
            continue
        if j[0] in "\"'":
            sortie.append(f'<span class="s">{e}</span>')
        elif (j.startswith("<") and j.endswith(">")) or (j.startswith("[") and j.endswith("]")):
            sortie.append(f'<span class="p">{e}</span>')
        elif premier and not j.startswith("-"):
            sortie.append(f'<span class="k">{e}</span>')
        elif j.startswith("-") and len(j) > 1:
            # Option courte : pas de coupure après le tiret (« -- / retries »)
            classe = "o insecable" if len(j) <= 22 else "o"
            sortie.append(f'<span class="{classe}">{e}</span>')
        else:
            sortie.append(e)
        premier = False
    return "".join(sortie)


def colorer_bloc(code):
    """Bloc non shell (json, python, toml…) : seules les chaînes et commentaires."""
    sortie = []
    for ligne in code.split("\n"):
        m = re.match(r"^(\s*)(#|//)(.*)$", ligne)
        if m:
            sortie.append(html.escape(m.group(1)) + f'<span class="cm">{html.escape(m.group(2) + m.group(3))}</span>')
            continue
        morceaux = re.split(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', ligne)
        sortie.append("".join(
            f'<span class="s">{html.escape(x)}</span>' if i % 2 else html.escape(x)
            for i, x in enumerate(morceaux)))
    return "\n".join(sortie)


def en_ligne(texte):
    """Markdown en ligne : code, liens, wikiliens, gras, italique."""
    # Le code est mis de côté (marqueurs) pour que le gras puisse l'englober.
    codes = []

    def garder(m):
        codes.append(f"<code>{colorer_commande(m.group(1))}</code>")
        return f"\x00{len(codes) - 1}\x00"

    e = re.sub(r"`([^`]+)`", garder, texte)
    e = html.escape(e, quote=False)
    e = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', e)
    e = re.sub(r"\[\[([^\]|#]+)(?:#[^\]|]*)?\|([^\]]+)\]\]", r'<span class="lien-wiki">\2</span>', e)
    e = re.sub(r"\[\[([^\]|#]+)(?:#[^\]|]*)?\]\]", r'<span class="lien-wiki">\1</span>', e)
    e = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", e)
    e = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", e)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], e)


# ---------------------------------------------------------------- blocs

def separer_commentaire(ligne):
    """« commande   # commentaire » → (commande, commentaire), hors guillemets."""
    dans, guillemet = False, None
    for i, c in enumerate(ligne):
        if c in "\"'":
            if not dans:
                dans, guillemet = True, c
            elif c == guillemet:
                dans = False
        elif c == "#" and not dans and i > 0 and ligne[i - 1].isspace():
            return ligne[:i].rstrip(), ligne[i + 1:].strip()
    return ligne.rstrip(), ""


def bloc_shell(lignes):
    """Bloc bash en tableau deux colonnes, à la manière d'un aide-mémoire."""
    groupes, courant = [], []
    for l in lignes:
        if not l.strip():
            if courant:
                groupes.append(courant)
            courant = []
        elif (l.lstrip().startswith("#") and courant and not courant[-1].lstrip().startswith("#")
              and not courant[-1].rstrip().endswith("\\")):
            # Un commentaire placé après des commandes ouvre un nouveau groupe
            groupes.append(courant)
            courant = [l]
        else:
            courant.append(l)
    if courant:
        groupes.append(courant)

    rangs = []
    for g in groupes:
        titres = []
        while g and g[0].lstrip().startswith("#"):
            titres.append(g.pop(0).lstrip()[1:].strip())
        # Commandes, en recollant les lignes continuées par « \ »
        cmds, tampon = [], ""
        for l in g:
            tampon = tampon + "\n" + l if tampon else l
            if not l.rstrip().endswith("\\"):
                cmds.append(tampon)
                tampon = ""
        if tampon:
            cmds.append(tampon)
        paires = [separer_commentaire(c) if "\n" not in c else (c, "") for c in cmds]
        avec_commentaire = any(d for _, d in paires)
        titre = " ".join(titres)
        if titre and not avec_commentaire:
            code = "\n".join(colorer_commande(c) for c, _ in paires)
            rangs.append(f'<tr><td class="c"><code>{code}</code></td><td class="d">{en_ligne(titre)}</td></tr>')
            continue
        if titre:
            rangs.append(f'<tr><td class="groupe" colspan="2">{en_ligne(titre)}</td></tr>')
        for c, d in paires:
            if d:
                rangs.append(f'<tr><td class="c"><code>{colorer_commande(c)}</code></td><td class="d">{en_ligne(d)}</td></tr>')
            else:
                rangs.append(f'<tr><td class="c" colspan="2"><code>{colorer_commande(c)}</code></td></tr>')
    return f'<table class="cmd">{"".join(rangs)}</table>'


def bloc_tableau(lignes):
    def cellules(l):
        l = l.strip()
        l = l[1:] if l.startswith("|") else l
        l = l[:-1] if l.endswith("|") else l
        # « | » échappé ou dans du code : on ne coupe pas à l'intérieur des `…`
        res, cur, dans = [], "", False
        for c in l:
            if c == "`":
                dans = not dans
            if c == "|" and not dans:
                res.append(cur.strip())
                cur = ""
            else:
                cur += c
        res.append(cur.strip())
        return res

    entete = cellules(lignes[0])
    corps = [cellules(l) for l in lignes[2:]]
    if len(entete) == 2:
        classe = "cmd"
        tete = ""
        if entete != ["Commande", "Ce qu'elle fait"]:
            tete = f"<tr><th>{en_ligne(entete[0])}</th><th>{en_ligne(entete[1])}</th></tr>"
        rangs = "".join(
            f'<tr><td class="c">{en_ligne(r[0])}</td><td class="d">{en_ligne(r[1] if len(r) > 1 else "")}</td></tr>'
            for r in corps)
        return f'<table class="{classe}">{tete}{rangs}</table>'
    tete = "<tr>" + "".join(f"<th>{en_ligne(c)}</th>" for c in entete) + "</tr>"
    rangs = "".join("<tr>" + "".join(f"<td>{en_ligne(c)}</td>" for c in r) + "</tr>" for r in corps)
    return f'<table class="grille">{tete}{rangs}</table>'


def blocs_markdown(lignes):
    """Convertit le contenu d'une section (sans son titre ##) en HTML."""
    sortie, i = [], 0
    debut_bloc = re.compile(r"^(```|### |\||\s*[-*] |\s*\d+\. |>)")
    while i < len(lignes):
        l = lignes[i]
        if not l.strip():
            i += 1
            continue
        if l.startswith("```"):
            langue = l[3:].strip()
            j = i + 1
            while j < len(lignes) and not lignes[j].startswith("```"):
                j += 1
            code = lignes[i + 1:j]
            if langue in ("bash", "sh", "shell", "zsh", "powershell", ""):
                sortie.append(bloc_shell(code))
            else:
                sortie.append(f"<pre>{colorer_bloc(chr(10).join(code))}</pre>")
            i = j + 1
        elif l.startswith("### "):
            sortie.append(f'<div class="pastille">{en_ligne(l[4:].strip())}</div>')
            i += 1
        elif l.startswith("#### "):
            sortie.append(f'<div class="intertitre">{en_ligne(l[5:].strip())}</div>')
            i += 1
        elif l.startswith("|"):
            j = i
            while j < len(lignes) and lignes[j].startswith("|"):
                j += 1
            sortie.append(bloc_tableau(lignes[i:j]))
            i = j
        elif re.match(r"^\s*([-*]|\d+\.) ", l):
            ordonnee = bool(re.match(r"^\s*\d+\. ", l))
            items, j = [], i
            while j < len(lignes) and lignes[j].strip():
                m = re.match(r"^\s*(?:[-*]|\d+\.) (.*)$", lignes[j])
                if m:
                    items.append(m.group(1))
                elif items:
                    items[-1] += " " + lignes[j].strip()
                j += 1
            balise = "ol" if ordonnee else "ul"
            sortie.append(f"<{balise}>" + "".join(f"<li>{en_ligne(x)}</li>" for x in items) + f"</{balise}>")
            i = j
        elif l.startswith(">"):
            j, texte = i, []
            while j < len(lignes) and lignes[j].startswith(">"):
                texte.append(lignes[j][1:].strip())
                j += 1
            # Encadré Obsidian « > [!warning] Titre » : titre en gras, puis le texte
            m = re.match(r"^\[!(\w+)\][+-]?\s*(.*)$", texte[0])
            if m:
                titre = m.group(2).strip() or m.group(1).capitalize()
                if titre[-1] not in ".:!?":
                    titre += "."
                texte = [f"**{titre}**"] + texte[1:]
            sortie.append(f'<p class="note">{en_ligne(" ".join(t for t in texte if t))}</p>')
            i = j
        else:
            j, texte = i, []
            while j < len(lignes) and lignes[j].strip() and not debut_bloc.match(lignes[j]):
                texte.append(lignes[j].strip())
                j += 1
            sortie.append(f"<p>{en_ligne(' '.join(texte))}</p>")
            i = j
    return "".join(sortie)


# ---------------------------------------------------------------- page

def construire_html(nom_memo):
    chemin = os.path.join(CONTENU, "memos", nom_memo + ".md")
    fm, corps = lire_frontmatter(open(chemin, encoding="utf-8").read())
    lignes = corps.split("\n")

    nom_outil = re.sub(r"^\[\[|\]\]$", "", fm.get("fiche", "")).split("|")[0] or nom_memo
    famille, chemin_fiche = trouver_fiche(nom_outil)
    ffm = lire_frontmatter(open(chemin_fiche, encoding="utf-8").read())[0] if chemin_fiche else {}
    zone = next((z for z, fs in FAMILLES.items() if famille in fs), "construire")
    fort, moyen, clair = ZONES[zone]
    titre_famille = ""
    if famille:
        titre_famille = lire_frontmatter(open(os.path.join(CONTENU, "outils", famille, "index.md"),
                                              encoding="utf-8").read())[0].get("title", famille)
    nom_affiche = ffm.get("title") or nom_outil

    # Découpage : avant le premier ##, puis une section par ## (hors blocs de code)
    sections, avant, courant, dans_code = [], [], None, False
    for l in lignes:
        if l.startswith("```"):
            dans_code = not dans_code
        if l.startswith("## ") and not dans_code:
            courant = [l[3:].strip(), []]
            sections.append(courant)
        elif courant is None:
            avant.append(l)
        else:
            courant[1].append(l)

    # Résumé : le premier paragraphe de citation ; le reste (encadrés…) suit tel quel
    debut = next((k for k, l in enumerate(avant) if l.startswith(">") and not l.startswith("> [!")), None)
    resume, autres = "", avant
    if debut is not None:
        fin = debut
        while fin < len(avant) and avant[fin].startswith(">"):
            fin += 1
        resume = " ".join(l[1:].strip() for l in avant[debut:fin])
        autres = avant[:debut] + avant[fin:]
    autres = [l for l in autres if not l.startswith("# ")]

    meta = []
    if titre_famille:
        meta.append(f"<b>Famille</b> {html.escape(titre_famille)}")
    if ffm.get("editeur"):
        meta.append(f"<b>Éditeur</b> {html.escape(ffm['editeur'])}")
    if ffm.get("licence"):
        meta.append(f"<b>Licence</b> {html.escape(ffm['licence'])}")
    notes = [ffm.get(k) for k in ("note_documentation", "note_precision", "note_maturite")]
    ligne2 = []
    if all(n and str(n).isdigit() for n in notes):
        ligne2.append(f"<b>Note du wiki</b> {sum(int(n) for n in notes)}/15")
    if fm.get("date"):
        ligne2.append(f"<b>Commandes vérifiées le</b> {date_fr(fm['date'])}")
    url_fiche = f"{SITE}/{slug(os.path.relpath(chemin_fiche, CONTENU))}" if chemin_fiche else SITE
    entete = (
        '<div class="entete">'
        '<div class="surtitre">AI Tools Wiki · Mémo</div>'
        f"<h1>{html.escape(nom_affiche)} <em>mémo</em></h1>"
        + (f'<p class="resume">{en_ligne(resume)}</p>' if resume else "")
        + (blocs_markdown(autres) if any(l.strip() for l in autres) else "")
        + '<p class="meta">' + " · ".join(meta)
        + ("<br>" + " · ".join(ligne2) if ligne2 else "")
        + f'<br><b>Fiche, notes et avis</b> <a href="https://{url_fiche}">{html.escape(url_fiche)}</a></p>'
        "</div>"
    )

    blocs = [entete]
    for titre, contenu in sections:
        classe = "bloc sources" if titre.lower().startswith("sources") else "bloc"
        if titre.lower().startswith("sources"):
            titre = "Sources (documentation officielle)"
        blocs.append(f'<section class="{classe}"><h2>{en_ligne(titre)}</h2>'
                     f'<div class="corps">{blocs_markdown(contenu)}</div></section>')

    aujourd_hui = date_fr(datetime.date.today().isoformat())
    pied = (
        '<template id="modele-pied"><div class="pied">'
        f'<span><a href="https://{SITE}">AI Tools Wiki</a> · {html.escape(SITE)}</span>'
        f"<span>Mémo {html.escape(nom_affiche)} · PDF généré le {aujourd_hui} depuis la page du mémo</span>"
        '<span class="numero"></span>'
        "</div></template>"
    )
    css = open(os.path.join(ICI, "gabarit.css"), encoding="utf-8").read()
    js = open(os.path.join(ICI, "mise_en_page.js"), encoding="utf-8").read()
    return (
        "<!doctype html><html lang=\"fr\"><head><meta charset=\"utf-8\">"
        f"<title>{html.escape(nom_affiche)} — Mémo · AI Tools Wiki</title>"
        f"<style>{css}\n:root{{--fort:{fort};--moyen:{moyen};--clair:{clair};}}</style>"
        "</head><body>"
        f'<div id="source">{"".join(blocs)}</div><div id="pages"></div>{pied}'
        f"<script>{js}</script></body></html>"
    )


# ---------------------------------------------------------------- impression

def lanceur():
    """Préfixe de lancement de Chrome. Sur un Mac Apple Silicon, un Python Intel (Rosetta)
    lancerait Chrome en x86_64, environ quatre fois plus lent : on force l'architecture native."""
    try:
        arm = subprocess.run(["sysctl", "-n", "hw.optional.arm64"], capture_output=True, text=True).stdout
    except OSError:
        return []
    return ["/usr/bin/arch", "-arm64"] if arm.strip() == "1" and os.path.exists("/usr/bin/arch") else []


def compter_pages(pdf):
    with open(pdf, "rb") as f:
        return len(re.findall(rb"/Type\s*/Page[^s]", f.read()))


def controler(dom):
    """Taille du texte retenue et problèmes relevés dans la page mise en page."""
    body = re.search(r"<body[^>]*>", dom)
    attrs = dict(re.findall(r'data-(\w+)="([^"]*)"', body.group(0))) if body else {}
    alertes = [a for a in html.unescape(attrs.get("alertes", "")).split(" | ") if a]
    pages = dom.split('<div id="pages">', 1)[-1]
    pages = re.sub(r"<(code|pre)\b.*?</\1>", " ", pages, flags=re.S)  # « **/*.ts » est du code
    texte = html.unescape(re.sub(r"<[^>]+>", " ", pages))
    for marque in ("**", "[[", "]]", "```", "](", "<!--"):
        if marque in texte:
            alertes.append(f"Markdown non converti : « {marque} »")
    return attrs.get("taille", "?"), alertes


def imprimer(nom_memo, sortie, profil, dossier_html):
    page_html = os.path.join(dossier_html, nom_memo + ".html")
    pdf = os.path.join(sortie, nom_memo + ".pdf")
    apercu = os.path.join(sortie, nom_memo + ".jpg")
    with open(page_html, "w", encoding="utf-8") as f:
        f.write(construire_html(nom_memo))
    # Un seul appel : impression du PDF et page après mise en page (pour les contrôles)
    res = subprocess.run(
        lanceur() + [CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
         f"--user-data-dir={profil}", "--no-pdf-header-footer", "--virtual-time-budget=10000",
         f"--print-to-pdf={pdf}", "--dump-dom", "file://" + page_html],
        check=True, capture_output=True)
    if shutil.which("sips"):
        # Aperçu de la première page pour la fiche : JPEG de 1 100 px (environ 280 Ko ;
        # un PNG pèserait plus que le PDF lui-même). sips écrit les noms en Unicode
        # décomposé (« e » + accent) : l'URL « …-mémo.jpg » ne le trouverait pas sur un
        # serveur Linux. On passe par un nom ASCII, puis on renomme en forme composée.
        provisoire = os.path.join(sortie, f".apercu-{os.getpid()}-{threading.get_ident()}.jpg")
        subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "70", "-Z", "1100",
                        pdf, "--out", provisoire], check=True, capture_output=True)
        if os.path.exists(apercu):
            os.remove(apercu)
        os.replace(provisoire, unicodedata.normalize("NFC", apercu))
    taille, alertes = controler(res.stdout.decode("utf-8", "replace"))
    return nom_memo, compter_pages(pdf), taille, alertes


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("memos", nargs="*", help="noms des mémos, sans .md (ex. « Playwright mémo »)")
    ap.add_argument("--tous", action="store_true", help="tous les mémos de content/memos/")
    ap.add_argument("--modifies", action="store_true",
                    help="seulement les mémos sans PDF, ou modifiés (mémo ou fiche) depuis leur PDF")
    ap.add_argument("--sortie", default=os.path.join(CONTENU, "memos", "pdf"),
                    help="dossier de sortie des PDF et aperçus JPEG (par défaut : content/memos/pdf)")
    ap.add_argument("--html", action="store_true",
                    help="garder la page HTML intermédiaire dans le dossier de sortie (pour ajuster le gabarit)")
    ap.add_argument("--parallele", type=int, default=3, help="nombre de Chrome en parallèle")
    ap.add_argument("--verifier", action="store_true",
                    help="liste les PDF absents, périmés ou orphelins, sans rien générer (liste de contrôle)")
    args = ap.parse_args()

    sortie = os.path.abspath(args.sortie)
    if args.verifier:
        tous = sorted(f[:-3] for f in os.listdir(os.path.join(CONTENU, "memos")) if f.endswith(" mémo.md"))
        for m in tous:
            if a_regenerer(m, sortie):
                print(f"PDF À RÉGÉNÉRER : {m}")
        signaler_orphelins(sortie, tous)
        return
    if not os.path.exists(CHROME):
        sys.exit("Google Chrome est introuvable : " + CHROME)
    if args.html and os.path.commonpath([sortie, CONTENU]) == CONTENU:
        sys.exit("--html : Quartz publierait la page intermédiaire ; choisir une sortie hors de content/.")
    tous = sorted(f[:-3] for f in os.listdir(os.path.join(CONTENU, "memos")) if f.endswith(" mémo.md"))
    memos = args.memos
    if args.tous or args.modifies:
        memos = tous
    if args.modifies:
        memos = [m for m in memos if a_regenerer(m, sortie)]
        if not memos:
            print("Tous les PDF sont à jour.")
            return
    if not memos:
        sys.exit("Aucun mémo indiqué (noms, --tous ou --modifies).")
    for m in memos:
        if not os.path.isfile(os.path.join(CONTENU, "memos", m + ".md")):
            sys.exit(f"Mémo introuvable : content/memos/{m}.md")

    os.makedirs(sortie, exist_ok=True)
    a_revoir = 0
    with tempfile.TemporaryDirectory() as tmp:
        profils = [os.path.join(tmp, f"profil-{i}") for i in range(len(memos))]
        dossier_html = sortie if args.html else tmp
        with ThreadPoolExecutor(max_workers=max(1, args.parallele)) as ex:
            for nom, pages, taille, alertes in ex.map(imprimer, memos, [sortie] * len(memos), profils,
                                                      [dossier_html] * len(memos)):
                print(f"{nom} : {pages} page{'s' if pages > 1 else ''}, {taille} pt")
                for a in alertes:
                    print(f"  À REVOIR : {a}")
                a_revoir += bool(alertes)
    print(f"{len(memos)} mémo(s) générés dans {sortie} ; {a_revoir} à revoir.")
    signaler_orphelins(sortie, tous)


def signaler_orphelins(sortie, tous):
    """PDF ou aperçus restés d'un mémo supprimé ou renommé, ou au nom mal encodé."""
    if not os.path.isdir(sortie):
        return
    for f in sorted(os.listdir(sortie)):
        base, ext = os.path.splitext(f)
        if ext not in (".pdf", ".jpg"):
            continue
        if base not in tous and unicodedata.normalize("NFC", base) in tous:
            print(f"NOM DÉCOMPOSÉ : {f} (accents en Unicode décomposé : URL introuvable sur le serveur)")
        elif base not in tous:
            print(f"SANS MÉMO : {f} (mémo supprimé ou renommé ?)")


def a_regenerer(nom_memo, sortie):
    """Vrai si le PDF manque ou si le mémo, ou sa fiche, a été modifié depuis."""
    pdf = os.path.join(sortie, nom_memo + ".pdf")
    if not os.path.isfile(pdf) or not os.path.isfile(os.path.join(sortie, nom_memo + ".jpg")):
        return True
    chemin = os.path.join(CONTENU, "memos", nom_memo + ".md")
    fm, _ = lire_frontmatter(open(chemin, encoding="utf-8").read())
    nom_outil = re.sub(r"^\[\[|\]\]$", "", fm.get("fiche", "")).split("|")[0]
    sources = [chemin, trouver_fiche(nom_outil)[1]]
    return any(s and os.path.getmtime(s) > os.path.getmtime(pdf) for s in sources)


if __name__ == "__main__":
    main()
