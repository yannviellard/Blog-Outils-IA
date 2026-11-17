---
title: "Ingénierie et développement"
type: metier
description: "Pour concevoir, coder, tester, sécuriser, déployer et maintenir les applications."
modified: 2026-11-12
---

# Ingénierie et développement

Pour concevoir, coder, tester, sécuriser, déployer et maintenir les applications.

| Sous-fonction                            | Outils recommandés                                                                                | Point d'attention                                                                                             |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Agent de développement principal         | [[Claude Code]], [[OpenAI Codex]], [[OpenCode]], [[Hermes Agent]]                                 | Choisir selon le besoin d'exploration, de délégation, d'ouverture ou de persistance.                          |
| Poste de pilotage multi-agent            | [[Paradev]], [[Conductor]], [[Parallel Code]], [[cmux]], [[Warp]], [[Claude Squad]]              | Isoler les tâches par worktree et limiter le nombre de travaux simultanés à ce qui peut réellement être relu. |
| Planification et exécution               | [[Superpowers]], [[GStack]], [[BMAD Method]], [[Planning with Files]], [[Everything Claude Code]] | Adapter la cérémonie à la taille de la tâche.                                                                 |
| Orchestration multi-agent                | [[Oh My Claude]], [[Ruflo]], [[Wshobson Agents]], [[Agency Agents]]                               | Mesurer le gain réel face à un agent unique bien cadré.                                                       |
| Compréhension du code                    | [[Graphify]], [[Claude-Mem]], [[MemPalace]]                                                       | Éviter que la mémoire ou le graphe devienne obsolète.                                                         |
| Revue et sécurité                        | [[Claude Code Review]], [[Security Guidance]], [[Skill Creator]]                                  | Compléter avec tests, SAST/SCA et revue humaine.                                                              |
| Tests et navigateur                      | [[Playwright]], [[Agent Browser]], [[Chrome DevTools MCP]], [[OpenCLI]]                           | Playwright pour le déterminisme, DevTools pour le diagnostic, profils isolés pour les agents.                 |
| Backend, authentification et déploiement | [[Supabase]], [[Better Auth]], [[Vercel]]                                                         | Modéliser tôt les droits, les coûts et le verrouillage fournisseur.                                           |

Le guide [[Architecture multi-repos et harnais Claude Code]] propose une organisation complète lorsque le produit est réparti entre web, mobile, backend, produit et marketing.

Toutes les fiches utiles à ce métier : [[tags/metier/ingenierie|métier « Ingénierie et développement »]]. Les autres métiers : [[metiers/index|Métiers]].

_Dernière analyse : 12 novembre 2026_
