# Deploy Relay Agent — Featureübersicht

## DRA V1

### Quellen & Git

- empfohlene Deploymentkanäle;
- Branch-, Tag-, Release- und Commitauswahl;
- Auflösung auf exakten Commit-SHA;
- sichtbare Erkennung, wenn ein beweglicher Ref weitergelaufen ist;
- bewusste Übernahme statt stiller Quellenänderung.

### Vorschau & Integrität

- Neu / Geändert / Entfernt / Unverändert;
- SHA-256-Vergleich;
- Versionsmarker;
- Regression-/Downgradewarnungen;
- Lifecycle-Klassifikation;
- read-only Vorschau.

### Deployment

- explizites DEVELOPMENT;
- frischer Preflight unmittelbar vor Installation;
- Staging;
- Integritätsprüfung;
- Backup vor Mutation;
- kontrollierte Dateimutationen;
- Post-Install-Verifikation;
- Rollback;
- RECOVERY_REQUIRED.

### Sicherung & Restore

- projektbezogene Retention;
- vollständige `replace_directory`-Snapshots;
- Sicherheitssicherung vor Restore;
- Hash-/Scope-Prüfung nach Restore;
- Lifecycle-Nachaktion;
- Legacy-Backup-Schutz.

### Mehrere Projekte

- Projektverwaltung;
- Sammelprüfung;
- Sammelinstallation;
- DRA-Selbstupdate zuletzt;
- Stop beim ersten Installationsfehler.

### Oberfläche

- Home-Assistant-Seitenleiste;
- Options Flow;
- Desktop;
- Tablet;
- Android/iOS Companion App;
- geführter Ablauf;
- Live-Status;
- Fortschrittsanzeige;
- mobile Aktionslayouts.

### Diagnose

- strukturierte Ereignisse;
- Run-IDs;
- Phasen;
- Fehlerfamilie;
- exakter Fingerprint;
- Fehlerhistorie;
- Supporttext;
- JSON;
- Git-Export;
- Redaction.

---

## DRA V2 — geplanter Ausbau

### Server Operation Manager

- Operation-ID;
- serverseitiger Auftrag;
- Queue;
- Phasenmodell;
- Ergebniszustand;
- Reconnect;
- mehrere Beobachter.

### Backend-Sammelupdate

- kompletter Gesamtauftrag im Backend;
- Child-Operation je Projekt;
- DRA-Selbstupdate zuletzt;
- serverseitiger Stop-on-Failure.

### Performance & Ressourcen

- kontrollierte Worker;
- Multi-Core dort, wo Messungen Nutzen zeigen;
- RAM-/I/O-Grenzen;
- Event-Loop-Schutz;
- ressourcenbasierte Abnahme.

### Große Projekte

- Pagination;
- serverseitige Filter;
- bedarfsgerechte Detaildaten;
- kleinere WebSocket-Antworten;
- weniger DOM-/WebView-Last.

### Mobile & Verbindung

- weniger UI-Renders;
- keine künstlichen Fortschrittstimer;
- reduzierte Hintergrundaktivität;
- Weiterlauf bei Clientverlust;
- Reconnect nach WLAN/Mobilfunk/VPN-Wechsel.

### Diagnose V2

- Operationszeitlinie;
- Queue-/Lock-Wartezeiten;
- Workerinformationen;
- Ressourcen-Snapshots;
- Parent-/Child-Hierarchie;
- Reconnecthistorie;
- Recoveryzusammenhang.
