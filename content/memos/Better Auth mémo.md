---
title: "Better Auth — Mémo"
type: memo
fiche: "[[Better Auth]]"
date: 2026-10-11
---

# Better Auth — Mémo

> Mise en place de [[Better Auth]] dans une application TypeScript et commandes de sa CLI pour générer le schéma, vérifier l'installation et administrer.

## Installation

```bash
npm install better-auth
```

Serveur (`auth.ts`) :

```ts
import { betterAuth } from "better-auth";

export const auth = betterAuth({
  emailAndPassword: { enabled: true },
});
```

Route Next.js (`/app/api/auth/[...all]/route.ts`) :

```ts
import { auth } from "@/lib/auth";
import { toNextJsHandler } from "better-auth/next-js";

export const { POST, GET } = toNextJsHandler(auth);
```

Client React (`lib/auth-client.ts`) :

```ts
import { createAuthClient } from "better-auth/react";

export const authClient = createAuthClient({ baseURL: "http://localhost:3000" });
```

## Commandes de la CLI

La CLI s'exécute avec `npx auth@latest <commande>` (ou `pnpm dlx`, `yarn dlx`, `bun x`).

|Commande|Ce qu'elle fait|
|---|---|
|`npx auth@latest init`|Initialise Better Auth dans le projet (`--name`, `--framework`, `--plugins`, `--database`).|
|`npx auth@latest generate`|Génère le schéma pour Prisma, Drizzle ou un fichier SQL Kysely (`--adapter`, `--dialect`, `--output`, `--config`, `-y`).|
|`npx auth@latest migrate`|Applique le schéma directement en base ; uniquement avec l'adaptateur Kysely (les autres passent par leur ORM).|
|`npx auth@latest check`|Lance les vérifications disponibles sur la configuration (`--config`).|
|`npx auth@latest check schema`|Vérifie que le schéma peut contenir ce que Better Auth écrit, sans rien créer.|
|`npx auth@latest create-admin`|Crée un premier administrateur (plugin Admin et base persistante requis ; `--email`, `--name`, `--role`).|
|`npx auth@latest info`|Diagnostic de l'installation, valeurs sensibles masquées (`--json`).|
|`npx auth@latest secret`|Génère une clé secrète pour l'instance.|
|`npx auth@latest upgrade`|Met à jour `better-auth` et les paquets `@better-auth/*` synchronisés.|

## Conseils d'utilisation

- **Relancer `generate` après chaque ajout de plugin** : la plupart ajoutent des tables.
- **Garder les secrets hors du dépôt** (`secret`) et en production uniquement via variables d'environnement.
- **Évaluer chaque plugin communautaire** : ils ne sont ni officiels ni vérifiés par l'équipe du projet.
- **Revue de sécurité nécessaire** : posséder son authentification transfère à l'équipe migrations, e-mails, correctifs et audit.

## Sources

- [Better Auth — installation](https://better-auth.com/docs/installation)
- [Better Auth — CLI](https://better-auth.com/docs/concepts/cli)
