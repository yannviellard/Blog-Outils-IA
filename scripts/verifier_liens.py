"""Contrôle des wikilinks de content/, résolus comme Obsidian et Quartz (markdownLinkResolution: shortest).

Signale les noms de fichiers en double (hors index.md, sans tenir compte de la casse), les liens ambigus,
les chemins introuvables, les ancres #Titre absentes, les images ou PDF introuvables (champ `logo` des
fiches : [[claude.svg]]) et les noms de fichiers non normalisés (NFD).
Les liens vers une page qui n'existe pas encore sont comptés à part : ce sont les fiches à écrire (option -v pour les lister).
Usage : python3 scripts/verifier_liens.py [-v]
"""
import os, re, sys, unicodedata, collections
N = lambda s: unicodedata.normalize("NFC", s)
C = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content")
files = {}
pieces = collections.defaultdict(list)  # fichiers non Markdown (logos, PDF) : [[claude.svg]]
for r, ds, fs in os.walk(C):
    if ".obsidian" in r: continue
    for f in fs:
        rel = os.path.relpath(os.path.join(r, f), C)
        if f.endswith(".md"):
            if N(rel) != rel: print("NFD :", rel)
            files[N(rel)[:-3]] = open(os.path.join(r, f), encoding="utf-8").read()
        elif not f.startswith("."):
            pieces[N(f).lower()].append(N(rel))
base = collections.defaultdict(list)
for k in files: base[k.split("/")[-1].lower()].append(k)
dups = {b: v for b, v in base.items() if len(v) > 1 and b != "index"}
print("noms en double (hors index) :", dups or "aucun")
def heads(k):
    t = re.sub(r"```.*?```", "", files[k], flags=re.S)
    return {h.strip() for h in re.findall(r"^#{1,6} (.+)$", t, re.M)}
prob = collections.Counter(); unres = collections.Counter(); n = 0
for k, t in files.items():
    if k.startswith("_modeles/"): continue
    body = re.sub(r"```.*?```", "", t, flags=re.S)
    body = re.sub(r"`[^`\n]*`", "", body)
    for m in re.finditer(r"\[\[([^\]]+?)\]\]", body):
        n += 1
        raw = m.group(1).replace("\\|", "|").split("|")[0]
        tg, _, anc = raw.partition("#"); tg = N(tg.strip())
        if re.search(r"\.(png|svg|webp|jpe?g|gif|pdf)$", tg, re.I):
            c = pieces.get(tg.split("/")[-1].lower(), [])
            if "/" in tg: c = [p for p in c if p == tg]
            if len(c) != 1: prob[f"fichier {'ambigu' if c else 'introuvable'} : {k} -> {raw}"] += 1
            continue
        if not tg: dest = k
        elif "/" in tg:
            dest = tg if tg in files else None
            if not dest: prob[f"chemin introuvable : {k} -> {raw}"] += 1; continue
        else:
            c = base.get(tg.lower(), [])
            if tg.lower() == "index": dest = "index"
            elif len(c) == 1: dest = c[0]
            elif not c: unres[tg] += 1; continue
            else: prob[f"ambigu : {k} -> {raw}"] += 1; continue
        if anc and anc.strip() not in heads(dest): prob[f"ancre absente : {k} -> {raw}"] += 1
print(n, "liens contrôlés ;", sum(prob.values()), "problèmes ;", len(unres), "cibles sans page (", sum(unres.values()), "liens )")
for p, c in sorted(prob.items()): print(" ", c, p)
if "-v" in sys.argv:
    print(", ".join(f"{k}({v})" for k, v in unres.most_common()))
