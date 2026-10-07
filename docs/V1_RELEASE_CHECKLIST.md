# DRA V1.0.0 — Release-Checkliste

Status: **ACTIVE — V1 Finalisierung**

## R1 — Runtime-Freeze

- [x] V1.0.0 RC3 auf exaktem Commit `5550b40de7b7eb62439bd88ee175281fc5891d7d` bestimmt
- [x] keine V2-Runtimeänderungen enthalten
- [x] CI grün — Validate #785 SUCCESS
- [x] Runtime-Diff gegen 0.15.30 auf V1-Release-/Public-Härtung begrenzt und dokumentiert

## R2 — Reale HA-Abnahme

- [ ] Startzustand LOCKED
- [ ] Projekte erhalten
- [ ] Seitenleisten-Options-Flow
- [ ] Quelle/Aktualität
- [ ] Preview/SHA-256
- [ ] DEVELOPMENT
- [ ] Einzelinstallation
- [ ] Backup/Restore
- [ ] Sammelupdate
- [ ] Diagnose-Ladeanzeige
- [ ] Diagnose-Git-Reconfigure-Regression
- [ ] Sicherheitsgate

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
- [ ] HACS-Validierung — nur Repository-Topics noch offen; Hassfest bereits SUCCESS
- [ ] manuelle Installation prüfen
- [ ] HACS-Installation prüfen
- [ ] Updatepfad prüfen
- [ ] Deinstallation/Entfernung dokumentieren

## R5 — FINAL

Erst wenn R1–R4 vollständig abgenommen:

- [ ] V1.0.0 FINAL markieren
- [ ] unveränderlichen Tag/Freeze setzen
- [ ] Release Notes finalisieren
- [ ] Public Main = freigegebener V1-Stand
- [ ] Projektseite auf FINAL umstellen
- [ ] V1 als Rückfallpunkt dokumentieren
- [ ] danach V2-05 starten
