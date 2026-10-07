# Deploy Relay Agent V1 — Handbuch

## 1. Was ist DRA?

Deploy Relay Agent ist eine Home-Assistant-Integration für kontrollierte Git-basierte Deployments in einer Entwicklungsumgebung.

DRA behandelt ein Update nicht als bloße Dateikopie. Ein normaler Ablauf besteht aus:

```text
Quelle ermitteln
→ exakten Commit einfrieren
→ Vorschau und Integrität prüfen
→ Schreibzugriff bewusst freigeben
→ Staging
→ Sicherung
→ Installation
→ Verifikation
→ Erfolg / Rollback / Recovery
```

## 2. Grundprinzipien

### GESPERRT ist der Normalzustand

Nach einem Home-Assistant-Neustart startet DRA immer **LOCKED**.

### Ein Git-Ref ist keine endgültige Identität

Ein Branch wie `main` oder `deploy/dev` kann sich bewegen. DRA löst ihn deshalb auf einen exakten Commit-SHA auf und friert diesen Stand ein.

### Vorschau ist read-only

Die Vorschau darf keine Zieldateien verändern. Sie zeigt den geplanten Zustand:

- Neu
- Geändert
- Entfernt
- Unverändert

### Sicherung vor Mutation

Vor jeder kontrollierten Installation entsteht ein Wiederherstellungspunkt.

### Verifikation nach Mutation

Nach der Installation prüft DRA den verwalteten Zielbereich erneut.

## 3. Oberfläche

Die DRA-Oberfläche besteht aus:

- Projektauswahl;
- Quelle & Version;
- geführtem Ablauf;
- Vorschau;
- Schreibfreigabe;
- Installation;
- Sicherungen;
- Sammelupdate;
- Diagnose & Logs;
- Einstellungen über den Home-Assistant-Options-Flow.

## 4. Projekt hinzufügen

Ein Projekt benötigt:

- GitHub-Repository;
- Deployment-Manifest `deploy-relay.json`;
- gegebenenfalls einen read-only GitHub-Token.

Das Manifest legt fest:

- Projekt-ID;
- Repositoryidentität;
- verwaltete Quellen;
- Zielpfade;
- Deploymentmodus;
- Lifecycle nach Installation;
- Sicherheitsgrenzen.

## 5. Quelle übernehmen

DRA kann empfohlene Deploymentkanäle über `deploy-relay-channel.json` erkennen.

Ein typischer DEV-Kanal:

```text
channel: dev
kind: branch
ref: deploy/dev
```

Beim Übernehmen wird der aktuelle Ref auf einen konkreten Commit eingefroren.

## 6. Vorschau

Die Vorschau prüft unter anderem:

- Manifest;
- Source Inventory;
- Zielinventar;
- SHA-256;
- Version;
- Regression/Downgrade;
- Lifecycle;
- Dateiänderungen;
- Löschungen.

Eine grüne Vorschau bedeutet: **Berechnung erfolgreich**. Sie bedeutet nicht automatisch, dass keine Änderungen oder Warnungen existieren.

## 7. DEVELOPMENT freigeben

Schreibzugriff wird nur bewusst aktiviert.

DRA speichert DEVELOPMENT nicht als dauerhaften Zustand. Nach HA-Neustart ist wieder LOCKED aktiv.

## 8. Installation

Vor der ersten Mutation baut DRA den Quellstand serverseitig nochmals frisch auf.

Die Sicherheitskette:

```text
fresh preflight
→ frozen source rebuild
→ staging
→ integrity check
→ backup
→ target identity recheck
→ mutation
→ verify
```

Endzustände:

- SUCCESS
- ROLLED_BACK
- RECOVERY_REQUIRED

## 9. Lifecycle nach Installation

DRA unterscheidet:

### Frontend-only

Änderungen ausschließlich in eindeutig statischen Frontendpfaden können ein Frontend-/Companion-Neuladen erlauben.

### Backend / gemischt

Python-, Manifest- oder gemischte Änderungen benötigen einen vollständigen Home-Assistant-Neustart.

DRA führt diesen Neustart **nie automatisch** aus.

## 10. Sicherungen

Sicherungen sind projektbezogen.

Standard-Retention:

```text
10 Wiederherstellungspunkte
Minimum 3
Maximum 100
```

Bei `replace_directory` können vollständige verwaltete Snapshots wiederhergestellt werden.

## 11. Wiederherstellung

Restore erfordert:

1. DEVELOPMENT-Freigabe;
2. separate Restorebestätigung;
3. Sicherheitssicherung **Vor Wiederherstellung**;
4. Wiederherstellung;
5. Hash-/Scope-Verifikation.

## 12. Sammelupdate

V1 kann mehrere Projekte prüfen und sequenziell installieren.

Wichtig:

- jedes Projekt erhält eigene Vorschau und Sicherheitskette;
- ein Fehler stoppt die weitere Installation;
- bereits erfolgreich installierte Projekte bleiben abgeschlossen;
- DRA selbst wird im Sammelupdate zuletzt installiert.

### Bekannte V1-Grenze

Die Orchestrierung des Sammelupdates liegt in V1 noch teilweise im Browser. V2 verschiebt den vollständigen Auftrag ins Backend.

## 13. Diagnose & Logs

DRA besitzt strukturierte Diagnose mit:

- Run-ID;
- Phasen;
- Fehlerfamilie;
- exaktem Fingerprint;
- Historie;
- Source-/Targetinformationen;
- Export als Supportdaten.

Secrets werden vor Speicherung/Export redigiert.

## 14. Diagnose nach Git

Der Diagnose-Git-Export:

- ist optional;
- braucht einen separaten Schreibtoken;
- schreibt ausschließlich in den reservierten Diagnosepfad;
- verleiht dem normalen Projekt-Token keine Schreibrechte.

## 15. Mobile Nutzung

V1 ist für Desktop, Tablet und Companion App optimiert.

Bekannte Grenzen:

- lange Operationen sind noch an den aktuellen Client-Request gekoppelt;
- Netzwechsel/VPN-Verlust kann die sichtbare Bedienoperation trennen;
- große Vorschauen belasten mobile WebViews stärker;
- Fortschritt enthält noch browserseitige UI-Aktivität.

Diese Punkte bilden einen Kern des DRA-V2-Umbaus.

## 16. DRA V2 — nächste Architektur

V2 macht den Server zum Besitzer eines Auftrags.

```text
V1:
Client startet und begleitet den Ablauf

V2:
Client startet
→ Server besitzt Auftrag
→ Client darf verschwinden
→ Auftrag läuft weiter
→ gleicher oder anderer Client verbindet sich erneut
```

Geplant:

- serverseitiger Operation Manager;
- Reconnect;
- Clientwechsel;
- persistente Operationsmetadaten;
- backendseitiges Sammelupdate;
- echte serverseitige Fortschrittswerte;
- Pagination großer Vorschauen;
- kontrollierte Multi-Core-Nutzung;
- Mobile-/Akku-Härtung;
- Diagnoseexport V2;
- Recovery über HA-Neustarts hinweg.

## 17. Support

Siehe `docs/SUPPORT.md`.

## 18. Sicherheit

Siehe `docs/SECURITY.md`.

## 19. Installation

Siehe `docs/INSTALLATION.md`.

## 20. Releaseübersicht

Siehe `docs/RELEASES.md`.
