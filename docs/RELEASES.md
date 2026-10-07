# Deploy Relay Agent — Releases

## DRA V1.0.0 RC3 — Finalkandidat

V1 ist der geplante stabile Abschluss der bisherigen DRA-Architektur. Der aktuelle Finalkandidat ist RC3 auf dem privaten Commit `5550b40de7b7eb62439bd88ee175281fc5891d7d` mit Validate #785 SUCCESS.

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

### Final-Gate

V1 wird erst als FINAL veröffentlicht, wenn der reale Home-Assistant-Abnahmelauf **und** die öffentliche HACS-/Installationsabnahme vollständig bestanden sind.

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
