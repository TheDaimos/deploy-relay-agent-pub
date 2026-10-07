# DRA V1.0.0 — Release-Checkliste

Status: **ACTIVE — V1 Finalisierung**

## R1 — Runtime-Freeze

- [ ] V1.0.0 RC auf exaktem Commit bestimmen
- [ ] keine V2-Runtimeänderungen enthalten
- [ ] CI grün
- [ ] Runtime-Diff gegen 0.15.30 ausschließlich freigegeben

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
- [ ] öffentliche Integrationsdateien
- [ ] HACS-Metadaten
- [ ] Lizenz-/Nutzungsentscheidung vor öffentlicher Codeverteilung
- [ ] Release-Paket

## R4 — Öffentliche Integration

Zielstruktur:

```text
custom_components/deploy_relay/
hacs.json
README.md
docs/
```

- [ ] ausschließlich abgenommener Final-SHA
- [ ] keine DEV-/Diagnoseartefakte
- [ ] keine Tokens/Secrets
- [ ] HACS-Validierung
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
