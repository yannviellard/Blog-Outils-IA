---
title: "Glif"
type: outil
description: "Passerelle MCP vers des workflows créatifs image, vidéo et audio réutilisables."
format: serveur-mcp
tags:
  - metier/marketing-ventes
  - theme/mcp
  - theme/image
  - theme/video
editeur: "Glif"
site: "https://glif.app/"
depot: "https://github.com/glifxyz/glif-mcp-server"
licence: "MIT (dépôt de métadonnées ; serveur hébergé propriétaire)"
statut: disponible
derniere_maj: 2026-10-08
etoiles: 218
forks: 32
etoiles_releve: 2026-11-16
note_documentation: 4
note_precision: 3
note_maturite: 3
note_popularite: 2
memo: "[[Glif MCP mémo]]"
avis_maj: 2026-09-24
modified: 2026-11-12
---

# Glif

> Agent créatif multimodal capable de générer et d'éditer des images, vidéos et audios en orchestrant automatiquement différents modèles et outils. Glif expose cette capacité aux agents externes via un serveur MCP hébergé.

**Composition** : 100+ skills, 1 agent, 1+ outil MCP.

Voir aussi : la section [[#Avis indépendants|Avis indépendants]] pour une synthèse des retours et réserves, et [[Glif MCP mémo]] pour le mémo pratique.

## Résumé

Glif est une plateforme de création multimodale orientée vers les contenus visuels et marketing. Depuis Glif 2.0, le produit repose sur un agent créatif unique disposant de plus de 100 outils natifs : génération et édition d'images, vidéo, audio, lipsync, traitement média, code, recherche web et composition multi-étapes. L'agent sélectionne automatiquement les modèles et les enchaîne en fonction du brief.

Glif agrège notamment des modèles et services comme OpenAI, Claude, Gemini, FLUX, Veo, Kling, Runway, ElevenLabs, Ideogram, Recraft et d'autres fournisseurs. La plateforme cherche ainsi à abstraire le choix du modèle et l'orchestration technique derrière une interface conversationnelle unique.

Le serveur MCP permet d'utiliser Glif depuis Claude, Claude Code, Codex, Cursor, VS Code et d'autres clients MCP via un endpoint HTTP hébergé. L'authentification utilise OAuth 2.1 et ne nécessite pas de clé API.

## Fonctionnalités

- Génération et édition multimodale : images, vidéos, audio et contenus textuels.
    
- Orchestration automatique de plusieurs modèles et étapes à partir d'un brief en langage naturel.
    
- Création de campagnes, product shots, vidéos promotionnelles, contenus sociaux, UGC ads, pitch visuals et autres assets marketing.
    
- Conservation du contexte et des références au sein d'un projet pour maintenir une cohérence visuelle entre les assets.
    
- Accès aux capacités de Glif depuis des agents externes grâce au MCP.
    
- Traitement multimédia et composition via des outils comme FFmpeg et Remotion, en plus des modèles génératifs.
    

## Analyse

|Critère|Note|
|---|---|
|Documentation|★★★★☆|
|Précision des descriptions|★★★☆☆|
|Facilité d'intégration MCP|★★★★★|
|Couverture multimodale|★★★★★|
|Orchestration multi-modèles|★★★★☆|
|Contrôle technique|★★★☆☆|
|Maturité|★★★☆☆|
|Popularité|★★☆☆☆|
|Intérêt pour les agents|★★★★☆|
|Pérennité du repository MCP|★★☆☆☆|

> _Notes Documentation, Précision et Maturité alignées sur le [[Comparatif global des outils|barème global]] (10 octobre 2026). Popularité calculée depuis les étoiles du dépôt GitHub : 218 au 16 novembre 2026._

**Commentaire :** Glif présente une proposition particulièrement intéressante comme couche d'exécution créative pour des agents : un seul MCP donne accès à un ensemble évolutif de modèles et d'outils multimédias. La principale réserve concerne le niveau d'abstraction et de contrôle : l'utilisateur délègue à Glif une partie importante du choix des modèles et de l'orchestration. Par ailleurs, le repository `glif-mcp-server` n'est plus le serveur MCP lui-même : il sert désormais principalement de métadonnées pour le serveur hébergé, le code du serveur étant propriétaire.

### Points forts

- **Abstraction multi-modèles :** Glif permet d'utiliser de nombreux modèles image, vidéo et audio sans intégrer individuellement chaque fournisseur.
    
- **Agent créatif natif :** le système choisit les outils et les modèles nécessaires à partir d'un brief plutôt que d'imposer la construction manuelle d'un workflow.
    
- **Très bon fit avec les agents MCP :** Claude Code, Codex, Cursor et autres agents peuvent déclencher directement des opérations créatives.
    
- **Large couverture marketing :** product photography, campagnes, vidéos promotionnelles, UGC, thumbnails, TikTok et autres formats sont explicitement pris en charge.
    
- **Évolution rapide :** l'abstraction permet potentiellement de bénéficier de nouveaux modèles sans modifier chaque intégration applicative.
    
- **Installation simple :** le MCP est un endpoint HTTP avec OAuth 2.1, sans gestion manuelle de clés API.
    

### Limites

- **Repository GitHub déprécié :** `glif-mcp-server` n'est plus le serveur local recommandé ; Glif recommande désormais son MCP hébergé.
    
- **Serveur propriétaire :** le repository public contient essentiellement les métadonnées d'enregistrement ; le serveur lui-même fait partie de la plateforme Glif et n'est pas open source.
    
- **Moins de contrôle :** le routage des modèles et une partie de l'orchestration sont délégués à Glif.
    
- **Dépendance à une plateforme tierce :** disponibilité, tarification, crédits et modèles disponibles dépendent de Glif.
    
- **Reproductibilité potentiellement moindre :** une abstraction qui choisit automatiquement le modèle peut rendre certaines générations moins déterministes qu'une intégration directe d'un modèle précis.
    
- **Coût à surveiller :** les opérations de génération consomment des crédits du compte Glif, tandis que les outils en lecture seule sont gratuits.
    
- **Confidentialité et surface d'attaque :** les requêtes, références et médias transitent par un serveur hébergé tiers ; comme tout serveur MCP tiers, il élargit les capacités et la surface d'attaque de l'agent.
    
- **Peu de retours indépendants détaillés :** la qualité dépend du workflow créatif et des modèles appelés plus que du connecteur MCP ; latence, crédits et stabilité sont à évaluer sur ses propres cas (voir [[#Avis indépendants|les avis indépendants]]).
    

## Relations

- **Alternative à :** intégrations directes multiples avec [[Runway]], [[Kling]], [[FLUX]], [[Veo]], [[ElevenLabs]]
    
- **S'intègre avec :** Claude · Claude Code · Codex · Cursor · VS Code · autres clients MCP
    
- **Utilise :** OpenAI · Anthropic · Google · FLUX · Kling · Runway · Veo · ElevenLabs · Replicate · autres modèles et services multimodaux
    

## Avis indépendants

_Synthèse des retours publiés, mise à jour le 24 septembre 2026._

### Synthèse

Glif MCP est surtout apprécié pour rendre des capacités créatives (image, vidéo, audio) accessibles depuis Claude et d'autres clients MCP sans recoder l'enchaînement de modèles. Depuis Glif 2.0 (changelog du 24 mars 2026), le produit repose sur un agent créatif unique qui sélectionne et enchaîne les modèles ; certaines présentations antérieures, centrées sur des « glifs » individuels, ne décrivent donc plus exactement l'offre actuelle.

Les retours indépendants détaillés sont encore rares. La qualité dépend davantage de l'agent Glif et des modèles sous-jacents que du serveur MCP lui-même. Il faut surveiller crédits, latence, confidentialité des entrées et reproductibilité (le choix automatique du modèle rend les générations moins déterministes). Comme tout serveur MCP tiers, il élargit aussi les capacités et la surface d'attaque de l'agent, et le dépôt `glif-mcp-server` est déprécié au profit d'un serveur hébergé propriétaire.

### Comparaison

ComfyUI donne plus de contrôle local et de reproductibilité mais demande une configuration technique. Replicate et fal proposent des API de modèles plus directes. Higgsfield Skills vise un studio image/vidéo intégré. Glif se distingue par son agent multi-modèles et l'assemblage no-code de workflows créatifs derrière un seul endpoint MCP.

### Verdict

Une passerelle pratique pour déclencher des créations multimodales depuis un agent ; la valeur doit être évaluée sur ses propres briefs (qualité, coût en crédits, latence) plutôt qu'au niveau du connecteur seul.

## Sources

- [Website](https://glif.app/)
    
- [MCP](https://glif.app/mcp)
    
- [GitHub](https://github.com/glifxyz/glif-mcp-server)
    
- [Glif 2.0 — One Agent, Many Tools](https://glif.app/changelog/2026-03-24-glif-2)
    
- [Glif Documentation](https://docs.glif.app/)
    

### Sources des avis

- [Site Glif](https://glif.app/)
- [Serveur MCP officiel](https://github.com/glifxyz/glif-mcp-server)
- [Guide sur le risque de chaîne d’approvisionnement des outils agentiques](https://www.techradar.com/pro/ai-agent-skills-are-becoming-the-next-enterprise-supply-chain-risk-heres-how-to-govern-them)

_Dernière analyse : 12 novembre 2026_