---
title: "Backend, authentification et déploiement"
type: famille
description: "Services et bibliothèques sur lesquels on construit et met en ligne une application."
modified: 2026-11-12
---

# Backend, authentification et déploiement

> Services et bibliothèques sur lesquels on construit et met en ligne une application.

Zone : [[outils/index#Construire et livrer|Construire et livrer]] · Barème : [[Comparatif global des outils]]

## En bref

Briques éprouvées et indépendantes des agents ; la note de maturité reflète le recul et l'adoption attestée, pas la facilité de démarrage.

## Les outils

|Outil|En bref|Format|Mémo|
|---|---|---|:-:|
|[[Supabase]]|Backend PostgreSQL managé ou auto-hébergé : données, auth, stockage et temps réel.|Plateforme|[[Supabase mémo\|Mémo]]|
|[[Better Auth]]|Authentification TypeScript auto-gérée, extensible et indépendante du framework.|Bibliothèque|[[Better Auth mémo\|Mémo]]|
|[[Vercel]]|Déploiement web intégré à Git, previews, CDN et fonctions managées.|Plateforme|[[Vercel mémo\|Mémo]]|

## Points d'attention

- Modéliser tôt les droits, les coûts et le verrouillage fournisseur.

## Notes

Notes sur le barème du [[Comparatif global des outils]] : Documentation, Précision des descriptions et Maturité, notées sur 5 et totalisées sur 15. La Popularité, calculée depuis les étoiles GitHub, s'affiche à part et n'entre pas dans le total.

|Outil|Documentation|Précision|Maturité|Total /15|Popularité|Justification|
|---|:-:|:-:|:-:|:-:|:-:|---|
|[[Supabase]]|★★★★★|★★★★☆|★★★★☆|**13**|★★★★★|Doc de référence ; RLS et coûts exigent de la compétence ; SDK mobiles moins mûrs.|
|[[Better Auth]]|★★★★☆|★★★★☆|★★★★☆|**12**|★★★★☆|Doc claire ; auth auto-gérée ; moins d'historique que les solutions établies.|
|[[Vercel]]|★★★★★|★★★★☆|★★★★★|**14**|★★★★☆|Doc de référence ; coûts et portabilité à anticiper ; plateforme établie.|

## Critères propres à la famille

|Outil|Nature|Point de vigilance|Alternative|
|---|---|---|---|
|[[Supabase]]|BaaS PostgreSQL|RLS mal configurée, egress, SDK mobiles moins mûrs|Firebase, Appwrite|
|[[Better Auth]]|Bibliothèque d'authentification auto-gérée|Sécurité et exploitation à votre charge|Clerk, Auth.js, Supabase Auth|
|[[Vercel]]|Plateforme de déploiement|Coûts imprévisibles, verrouillage|Netlify, Cloudflare, AWS|

## Absents notables

Outils cités comme alternatives dans ces fiches, sans fiche dans le wiki pour l'instant : [[Firebase]], [[Clerk]], [[Auth0]], [[Supabase Auth]], [[Netlify]], [[Cloudflare Pages]], [[AWS Amplify]].

_Dernière analyse : 12 novembre 2026_
