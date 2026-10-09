# Deploy Relay Agent — Releases

## DRA V1.0.0 FINAL

V1.0.0 ist der freigegebene stabile Abschluss der bisherigen DRA-Architektur. Der FINAL-Stand basiert unverändert auf dem RC3-Runtimekern `5550b40de7b7eb62439bd88ee175281fc5891d7d` mit Validate #785 SUCCESS. Der öffentliche Runtimeinhalt bleibt bytegenau über `docs/RUNTIME_PROVENANCE.json` diesem Stand zugeordnet.

### Highlights

- Home-Assistant-Custom-Integration;
- sichere Git-basierte Deploymentpipeline;
- Commit-SHA-Freeze;
- read-only Vorschau;
- SHA-256-Dateiwahrheit;
- Versions-/Regressionsschutz;
- LOCKED → explizites DEVELOPMENT;
- Staging;
- Backup vor Mutation;
- Verifikation nach Installation;
- automatischer Rollback;
- RECOVERY_REQUIRED;
- projektbezogene Sicherungen und Restore;
- Sammelupdate;
- Frontend-/Restart-Lifecycle;
- Diagnose & Git-Export;
- mobile Oberfläche;
- Seitenleistenoption;
- Ressourcen-Härtung;
- stabile Diagnose-Ladeanzeige.

### Sicherheitsversprechen

DRA V1:

- startet Home Assistant nicht automatisch neu;
- führt keine beliebigen Shellskripte aus;
- schreibt nicht direkt in `.storage`;
- speichert DEVELOPMENT nicht dauerhaft;
- trennt Lesetoken und Diagnose-Schreibtoken;
- mutiert erst nach expliziter Freigabe.

### Finalstatus

**FINAL / FROZEN — 2026-10-09**

Die V1-Finalisierung wurde nach wiederholter realer Nutzung und Abnahme des unveränderten RC3-Codes freigegeben. Die bewusst nicht erneut ausgeführten Restore-/Frischinstallationsschritte wurden als bereits zuvor erprobte, seitdem unveränderte Pfade akzeptiert. Es wurden dafür keine zusätzlichen V1-Runtimeänderungen vorgenommen.

V1.0.0 ist damit der stabile Produkt- und Rückfallstand für die V2-Entwicklung.

---

## DRA V2 — geplant

V2 ist keine kosmetische Versionserhöhung, sondern die nächste Ausführungsarchitektur.

### Schwerpunkt

**Vom clientbegleiteten Deployment zur serverseitigen Deployment-Engine.**

Geplant:

- serverseitige Aufträge mit Operation-ID;
- Weiterlauf bei Clientverlust;
- Reconnect und Clientwechsel;
- serverseitiges Sammelupdate;
- Persistenz und Recovery;
- echte Backend-Fortschrittsdaten;
- Event-/Subscription-Modell;
- Pagination großer Previewdaten;
- reduzierte Browser-/WebView-Last;
- Akkuoptimierung auf Mobile;
- kontrollierte Multi-Core-/Worker-Nutzung;
- erweitertes Diagnose-/Exportmodell.

### Performance

V2 soll vorhandene Serverressourcen kontrolliert besser nutzen.

Dabei gilt:

> Mehr Kerne sind kein Freibrief für mehr Worker.

CPU, RAM, I/O und Home-Assistant-Reaktionsfähigkeit werden gemeinsam gemessen. Workerzahlen werden aus realen Benchmarks abgeleitet, nicht aus `os.cpu_count()`.

### Verbindungsunabhängigkeit

Die eigentliche schwere Git-/Hash-/Backup-/Installationsarbeit liegt bereits in V1 im Home-Assistant-Backend. V2 verschiebt zusätzlich **Auftragsbesitz und Orchestrierung** vollständig dorthin.

Dadurch soll die Bedienung nicht mehr davon abhängen, ob der beobachtende Client gerade über:

- LAN;
- WLAN;
- Mobilfunk;
- VPN;
- Companion App;
- Notebook

verbunden ist.

---

## Versionsstrategie

```text
V1.0.0 FINAL
= stabiler Produkt-/Rückfallstand

V2.x DEV
= neue serverseitige Operationsarchitektur

V2 FINAL
= erst nach vollständiger Realabnahme
```
