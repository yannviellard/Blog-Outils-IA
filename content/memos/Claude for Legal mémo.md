---
title: "Claude for Legal — Mémo"
type: memo
fiche: "[[Claude for Legal]]"
date: 2026-09-25
---

# Claude for Legal — Mémo

> Les commandes à connaître pour [[Claude for Legal]], la suite de plugins juridiques d'Anthropic pour Claude Code et Claude Cowork : contrats, sociétés, données personnelles, produit, droit du travail, gouvernance de l'IA, réglementaire, propriété intellectuelle, contentieux, formation. Chaque sortie est un brouillon destiné à un avocat ou juriste, jamais un avis juridique.

**Attention :** les plugins sont conçus pour le droit américain (juridictions d'États, FMLA, Westlaw…). Pour un usage en France ou en Europe, adapter le profil de pratique et vérifier chaque référence.

## Installation dans Claude Code

```bash
/plugin marketplace add anthropics/claude-for-legal
/plugin install commercial-legal@claude-for-legal
/plugin install privacy-legal@claude-for-legal
/plugin install corporate-legal@claude-for-legal
```

Redémarrer Claude Code, puis **lancer l'entretien de démarrage pour chaque plugin installé** :

```bash
/commercial-legal:cold-start-interview
```

Il pose des questions sur ta pratique (grille de négociation, circuit d'escalade, style maison), lit des documents de référence (un contrat signé, une grille, un mémo) et écrit un profil de pratique dans `~/.claude/plugins/config/claude-for-legal/<plugin>/CLAUDE.md`. Compter 10 à 20 minutes ; une option rapide existe.

## Les plugins

|Plugin|Pour|
|---|---|
|`commercial-legal`|Contrats fournisseurs, NDA, abonnements SaaS, suivi des renouvellements.|
|`corporate-legal`|Due diligence M&A, annexes de divulgation, check-list de closing, procès-verbaux.|
|`privacy-legal`|Données personnelles : analyses d'impact, revue de DPA, demandes d'accès (DSAR).|
|`product-legal`|Revue de lancement produit, allégations marketing, questions rapides.|
|`employment-legal`|Embauche, licenciement, qualification des travailleurs, enquêtes internes.|
|`ai-governance-legal`|Cas d'usage IA, analyses d'impact, revue des fournisseurs d'IA.|
|`regulatory-legal`|Veille réglementaire, écarts entre politique et réglementation.|
|`ip-legal`|Marques, liberté d'exploitation, mises en demeure, open source.|
|`litigation-legal`|Dossiers contentieux, chronologies, préparation de dépositions.|
|`law-student` / `legal-clinic`|Apprentissage (sans donner la réponse) et cliniques juridiques.|
|`legal-builder-hub`|Installer des skills juridiques communautaires avec contrôle de sécurité.|

## Commandes les plus utiles

|Commande|Ce qu'elle fait|
|---|---|
|`/commercial-legal:review`|Revue clause par clause d'un contrat fournisseur, NDA ou SaaS selon ta grille.|
|`/commercial-legal:amendment-history`|Retrace les modifications d'un contrat et de ses avenants.|
|`/commercial-legal:renewal-tracker`|Contrats dont la date limite de résiliation tombe dans les 90 jours.|
|`/commercial-legal:escalation-flagger`|Oriente un problème vers la bonne personne et rédige la demande.|
|`/corporate-legal:tabular-review`|Revue en tableau : une ligne par document, chaque cellule sourcée.|
|`/corporate-legal:closing-checklist`|Ce qui bloque le closing, avec le chemin critique.|
|`/privacy-legal:dpa-review`|Revue d'un accord de traitement des données.|
|`/privacy-legal:dsar-response`|Réponse à une demande d'accès aux données.|
|`/product-legal:is-this-a-problem`|Tri rapide d'une question juridique posée par une équipe.|
|`/litigation-legal:chronology`|Construit la chronologie d'un dossier.|
|`/ip-legal:oss-review`|Conformité des licences open source.|
|`/legal-builder-hub:skills-qa`|Contrôle qualité et sécurité d'une skill communautaire avant installation.|

Dans Word (Claude pour Microsoft 365), les revues de contrat sortent en **modifications suivies**, à accepter ou refuser comme une relecture humaine.

## Conseils d'utilisation

- **Ne jamais sauter l'entretien de démarrage** : c'est la première cause de résultats génériques. Plus il y a de documents de référence, meilleure est la revue.
- **Connecter un outil de recherche juridique d'abord** (CourtListener, Trellis…) : sans lui, les citations viennent de la mémoire du modèle et sont marquées `[verify]`.
- **Corriger le profil directement** pour les petits ajustements (seuil d'escalade, nouvelle intégration) ; relancer l'entretien si la pratique change beaucoup.
- **Traiter chaque sortie comme un brouillon** : un avocat relit, vérifie et en prend la responsabilité.
- **Vérifier les skills communautaires** avec `legal-builder-hub` : une skill a accès aux dossiers, au profil de pratique et aux connecteurs.

## Sources

- [README claude-for-legal](https://github.com/anthropics/claude-for-legal)
- [Claude for the legal industry — blog Anthropic](https://claude.com/blog/claude-for-the-legal-industry)
- [Claude for Lawyers — Clio](https://www.clio.com/blog/anthropic-legal/)
- [Claude for Legal in 2026: Pros, Cons, and the Privilege Question — GC AI](https://gc.ai/blog/claude-legal-ai)
