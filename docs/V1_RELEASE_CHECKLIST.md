# DRA V1.0.0 — Release-Checkliste

Status: **FINAL / FROZEN — 2026-10-09**

## R1 — Runtime-Freeze

- [x] V1.0.0 RC3 auf exaktem Commit `5550b40de7b7eb62439bd88ee175281fc5891d7d` bestimmt
- [x] keine V2-Runtimeänderungen enthalten
- [x] CI grün — Validate #785 SUCCESS
- [x] Runtime-Diff gegen 0.15.30 auf V1-Release-/Public-Härtung begrenzt und dokumentiert

## R2 — Reale HA-Abnahme

- [x] Startzustand LOCKED
- [x] Projekte erhalten
- [x] Seitenleisten-Options-Flow
- [x] Quelle/Aktualität
- [x] Preview/SHA-256
- [x] DEVELOPMENT
- [x] Einzelinstallation
- [x] Backup/Restore — bestehender Pfad freigegeben; echter Restore nicht erneut ausgeführt, da seit vorheriger Realerprobung keine Runtimeänderung
- [x] Sammelupdate
- [x] Diagnose-Ladeanzeige
- [x] Diagnose-Git-Reconfigure-Regression
- [x] Sicherheitsgate

## R3 — Produktisierung

- [x] öffentliche Projektseite
- [x] V1↔V2-Roadmap
- [x] Hi-Res-Roadmapgrafik
- [x] Handbuch
- [x] Installationsanleitung
- [x] Featureübersicht
- [x] Releaseinformationen
- [x] Sicherheitsdokumentation
- [x] Support/Fehlerbehebung
- [x] V1→V2-Upgradeversprechen
- [x] öffentliche Integrationsdateien aus RC3 deterministisch promoviert
- [x] HACS-Metadaten vorbereitet
- [x] GPL-3.0-only / Copyright / Branding / Drittkomponenten festgelegt
- [x] deterministisches Release-Paket + SHA-256-Build vorbereitet

## R4 — Öffentliche Integration

Zielstruktur:

```text
custom_components/deploy_relay/
hacs.json
README.md
docs/
```

- [x] ausschließlich RC3-SHA mit Runtime-Provenienznachweis
- [x] keine DEV-/Diagnoseartefakte im vorgesehenen Releasepaket
- [x] keine Tokens/Secrets im Public-Paket; privater DEV-Repo-Pfad wird im Runtimecode CI-seitig abgewiesen
- [x] HACS-Validierung + Hassfest SUCCESS
- [x] manuelle/öffentliche Installationsstruktur geprüft
- [x] HACS-Installationsweg freigegeben; früher real erprobt, unveränderter Runtimecode
- [x] Update-/Self-Update-Pfad mehrfach real geprüft
- [x] Deinstallation/Entfernung dokumentiert und als bestehender unveränderter Pfad freigegeben

## R5 — FINAL

Erst wenn R1–R4 vollständig abgenommen:

- [x] V1.0.0 FINAL markieren
- [x] unveränderlichen Freeze-Ref setzen
- [x] Release Notes finalisieren
- [x] Public Main = freigegebener V1-Stand
- [x] Projektseite auf FINAL umstellen
- [x] V1 als Rückfallpunkt dokumentieren
- [x] V1-Freigabe für V2-05 erteilt


## Finalentscheid 2026-10-09

DRA V1.0.0 wurde als **FINAL / FROZEN** freigegeben. Grundlage ist der unveränderte RC3-Runtimekern `5550b40de7b7eb62439bd88ee175281fc5891d7d`. Bereits früher real erprobte Restore-/Frischinstallationspfade wurden aufgrund fehlender Runtimeänderungen nicht erneut vollständig provoziert und vom Projektverantwortlichen ausdrücklich als nicht releaseblockierend akzeptiert.
