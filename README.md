<div align="center">

<img
  src="https://raw.githubusercontent.com/TheDaimos/deploy-relay-agent-pub/main/assets/branding/dra-logo-transparent-1254.png"
  width="190"
  alt="Deploy Relay Agent Logo">

# Deploy Relay Agent

### Kontrollierte Git-Deployments für Home Assistant

**Exakter Commit · Vorschau · Sicherung · Verifikation · Rollback · Diagnose**

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Custom%20Integration-41BDF5?logo=home-assistant&logoColor=white)
![Version](https://img.shields.io/badge/DRA-V1.0.0%20FINAL-16c7ee)
![Status](https://img.shields.io/badge/V1-FINAL-2ea96b)
![HACS](https://img.shields.io/badge/HACS-bereit-2ea96b)
![V2](https://img.shields.io/badge/DRA%20V2-Roadmap%20festgelegt-d6a648)
![License](https://img.shields.io/badge/Code-GPL--3.0--only-lightgrey)

**[🚀 Projektseite](https://thedaimos.github.io/deploy-relay-agent-pub/)** ·
**[📦 Installation](docs/INSTALLATION.md)** ·
**[📖 Handbuch](docs/HANDBUCH.md)** ·
**[⚙️ Funktionen](docs/FEATURES.md)** ·
**[🛡️ Sicherheit](docs/SECURITY.md)**

</div>

> [!IMPORTANT]
> **DRA V1.0.0 ist FINAL / FROZEN.**  
> Der freigegebene V1-Runtimekern basiert unverändert auf **RC3** (`5550b40d…`, Validate #785 SUCCESS). Die öffentliche Integrationsstruktur, HACS-/Hassfest-Prüfung, Runtime-Provenienz und das reproduzierbare Releasepaket sind freigegeben. V1 dient ab jetzt als stabiler Produkt- und Rückfallstand für die weitere V2-Entwicklung.

<p align="center">
  <img
    src="https://raw.githubusercontent.com/TheDaimos/deploy-relay-agent-pub/main/assets/roadmap/dra-v1-v2-roadmap-hires.webp"
    width="1000"
    alt="DRA V1 FINAL und DRA V2 Roadmap">
</p>

**Vollständiger Überblick:** [Projektseite](https://thedaimos.github.io/deploy-relay-agent-pub/) ·
**Bedienung:** [docs/HANDBUCH.md](docs/HANDBUCH.md) ·
**V1 → V2:** [docs/V1_V2_ROADMAP.md](docs/V1_V2_ROADMAP.md)

---

## Schnellnavigation

[Was ist DRA?](#was-ist-dra) ·
[DRA V1](#dra-v1--stabiler-deployment--und-recovery-werkzeugkasten) ·
[Installation](#installation) ·
[Sicherheitsmodell](#sicherheitsmodell) ·
[Diagnose](#diagnose--nachvollziehbarkeit) ·
[DRA V2](#dra-v2--die-nächste-generation) ·
[Dokumentation](#dokumentation) ·
[Lizenz](#lizenz-und-branding)

---

# Was ist DRA?

Deploy Relay Agent ist eine Home-Assistant-Integration für **kontrollierte Git-basierte Deployments in Entwicklungsumgebungen**.

DRA behandelt eine Aktualisierung nicht als bloße Dateikopie. Stattdessen wird aus einer beweglichen Git-Quelle ein **nachvollziehbarer, eingefrorener und verifizierbarer Bereitstellungsvorgang**:

```text
Git-Quelle
→ exakten Commit-SHA einfrieren
→ Vorschau + SHA-256
→ DEVELOPMENT bewusst freigeben
→ Staging
→ Sicherung
→ Installation
→ Verifikation
→ SUCCESS / ROLLBACK / RECOVERY_REQUIRED
```

Das Ziel ist nicht maximale Automatisierung um jeden Preis, sondern ein reproduzierbarer Ablauf mit klarer Quelle, sichtbaren Änderungen, Rückfallmöglichkeit und beweisbarem Zielzustand.

> [!NOTE]
> DRA ist bewusst **kein Shell-Runner**, kein allgemeiner Git-Client und kein stiller Auto-Updater.  
> Schreibzugriffe bleiben gesperrt, bis sie ausdrücklich freigegeben werden.

---

# DRA V1 — stabiler Deployment- und Recovery-Werkzeugkasten

DRA V1 bündelt die heute bewährten Funktionen zu einem stabilen ersten Release.

## V1 auf einen Blick

| Bereich | DRA V1 |
| --- | --- |
| **Git-Quelle** | Branch, Tag oder Commit bewusst auswählen |
| **Commit-Freeze** | beweglichen Ref auf exakten SHA einfrieren |
| **Vorschau** | Neu / Geändert / Entfernt / Unverändert sichtbar machen |
| **Integrität** | SHA-256-Dateivergleich |
| **Sicherheit** | LOCKED → explizites DEVELOPMENT |
| **Staging** | Quellstand vor Mutation kontrolliert vorbereiten |
| **Sicherung** | Wiederherstellungspunkt vor jeder Mutation |
| **Verifikation** | Zielbestand nach Installation erneut prüfen |
| **Rollback** | bei Fehler kontrolliert auf sicheren Stand zurück |
| **Recovery** | `RECOVERY_REQUIRED`, wenn Sicherheit nicht beweisbar ist |
| **Restore** | projektbezogene Vollsicherungen mit Retention |
| **Sammelupdate** | mehrere Projekte prüfen und sequenziell installieren |
| **Lifecycle** | Frontend-Neuladen oder HA-Neustart empfehlen |
| **Diagnose** | strukturierte Logs, Supportdaten und Git-Export |
| **Oberfläche** | Desktop, Tablet und Companion App |

## Was DRA besonders macht

- **Commit statt Hoffnung** — ein beweglicher Branch wird vor der Ausführung auf einen exakten SHA eingefroren.
- **Vorschau vor Mutation** — reale Dateidifferenzen bleiben sichtbar.
- **Sicherung vor Änderung** — kein kontrolliertes Deployment ohne Rückfallpunkt.
- **Verifikation nach Änderung** — Erfolg wird nicht nur behauptet, sondern geprüft.
- **Fail closed** — unsichere Zustände werden nicht still als Erfolg behandelt.
- **Keine automatischen HA-Neustarts** — Nachaktionen bleiben bewusst beim Benutzer.
- **Getrennte GitHub-Rechte** — normale Projektzugänge bleiben read-only; Diagnoseexport erhält einen eigenen, eng begrenzten Schreibweg.

---

# Installation

## Bevorzugter Weg — HACS

Der öffentliche HACS-Weg ist für **DRA V1.0.0 FINAL** freigegeben.

**Repository für HACS — Copy & Paste:**

```text
https://github.com/TheDaimos/deploy-relay-agent-pub
```

1. in HACS unter **Benutzerdefinierte Repositories** die oben angegebene URL einfügen;
2. als Typ **Integration** auswählen und das Repository hinzufügen;
3. **Deploy Relay Agent** installieren;
4. Home Assistant vollständig neu starten;
5. unter **Einstellungen → Geräte & Dienste → Integration hinzufügen** nach **Deploy Relay Agent** suchen;
6. DRA konfigurieren.

Vollständige Anleitung: **[docs/INSTALLATION.md](docs/INSTALLATION.md)**

## GitHub-Zugriff

Für private Projekt-Repositories sollte der normale Fine-grained Token möglichst nur folgende Rechte besitzen:

```text
Metadata: Read
Contents: Read
```

Der optionale Diagnose-Git-Export verwendet bewusst einen **separaten Schreibtoken**.

---

# Sicherheitsmodell

DRA startet nach einem vollständigen Home-Assistant-Neustart grundsätzlich im Zustand:

```text
LOCKED
```

Schreibzugriffe erfordern eine ausdrückliche DEVELOPMENT-Freigabe.

Der normale Installationspfad:

```text
Quelle prüfen
→ Commit einfrieren
→ frischer Preflight
→ Staging
→ Integrität prüfen
→ Sicherung
→ Zielidentität erneut prüfen
→ Mutation
→ Verifikation
```

Mögliche Endzustände:

```text
SUCCESS
ROLLBACK SUCCESS
RECOVERY_REQUIRED
```

DRA:

- schreibt nicht direkt in Home Assistants private `.storage`-Dateien;
- akzeptiert keine beliebigen Shellskripte;
- führt keine stillen Schreiboperationen aus einer Vorschau heraus aus;
- speichert DEVELOPMENT nicht dauerhaft;
- startet Home Assistant niemals automatisch neu.

Mehr dazu: **[docs/SECURITY.md](docs/SECURITY.md)**

---

# Sicherungen und Wiederherstellung

Sicherungen sind projektbezogen.

Aktuelle Retention:

```text
Standard: 10 Wiederherstellungspunkte
Minimum:   3
Maximum:   100
```

Ein Restore erfordert:

1. ausdrückliche DEVELOPMENT-Freigabe;
2. separate Restorebestätigung;
3. Sicherheitssicherung **vor** der Wiederherstellung;
4. kontrollierte Wiederherstellung;
5. Hash-/Scope-Verifikation.

Details: **[Handbuch](docs/HANDBUCH.md)**

---

# Sammelupdate

DRA V1 kann mehrere Projekte gemeinsam prüfen und anschließend sequenziell installieren.

Dabei gilt:

- jedes Projekt behält seine eigene Vorschau und Sicherheitskette;
- ein Installationsfehler stoppt den weiteren Ablauf;
- bereits erfolgreich installierte Projekte bleiben nachvollziehbar abgeschlossen;
- DRA selbst wird — wenn ausgewählt — zuletzt aktualisiert.

> [!NOTE]
> In V1 liegt die übergeordnete Sammel-Orchestrierung noch teilweise im Frontend.  
> DRA V2 verschiebt diesen gesamten Ablauf in einen serverseitigen Auftrag.

---

# Diagnose & Nachvollziehbarkeit

DRA protokolliert nicht nur „ging“ oder „ging nicht“.

Die Diagnose arbeitet unter anderem mit:

- Vorgangs-/Run-IDs;
- Phasen und Dauer;
- Quell- und Zielidentität;
- Dateiklassifikationen;
- SHA-/Integritätsdaten;
- Fehlerfamilien und Fingerprints;
- redigierten Supportdaten;
- optionalem Diagnose-Git-Export.

Secrets werden vor Persistenz und Export redigiert.

Der Diagnose-Git-Export:

- ist optional;
- verwendet einen getrennten Schreibtoken;
- schreibt nur in den reservierten Diagnosebereich;
- erweitert den normalen Projekt-Token **nicht** um Schreibrechte.

Support & Diagnose: **[docs/SUPPORT.md](docs/SUPPORT.md)**

---

# DRA V2 — die nächste Generation

## Deploymentablauf auf die nächste Ebene heben

**DRA V1 ist bereits ein stabiler Deployment- und Recovery-Werkzeugkasten und V2 legt noch eine Schippe drauf!**

DRA V2 ersetzt diese Basis nicht. Die nächste Generation verschiebt **Auftragsbesitz, Orchestrierung, Fortschritt und Wiederanbindung vollständig zum Home-Assistant-Server**.

Die schwere Git-, Datei-, Hash-, Backup- und Installationsarbeit läuft bereits in V1 im Backend. V2 beseitigt zusätzlich die verbleibende Abhängigkeit des Ablaufs vom gerade verbundenen Client.

### Maximale Flexibilität · maximale Effizienz.

| DRA V1 | DRA V2 |
| --- | --- |
| Client begleitet lange Requests | **Server besitzt den Auftrag** |
| Sammelupdate wird im Frontend fortgeschaltet | **Sammelupdate läuft vollständig im Backend** |
| Clientverlust kann den sichtbaren Ablauf trennen | **Auftrag läuft ohne Client weiter** |
| kein eigener Reconnect-Auftrag | **Wiederanbindung über Operation-ID** |
| Fortschritt teilweise browserseitig angenähert | **serverseitige Phasen und echte Zähler** |
| große Vorschau kann Browser belasten | **Pagination / bedarfsgerechtes Laden** |
| mehr WebView-Aktivität auf Mobile | **deutlich weniger lokale Last** |
| konservative Einzelarbeit | **gemessene Multi-Core-/Worker-Nutzung** |
| Diagnose pro Run | **Operationszeitlinie inkl. Queue, Worker und Wiederanbindung** |

## Zielbild V2

```text
Handy startet Auftrag im WLAN
→ App darf in den Hintergrund
→ WLAN / Mobilfunk / VPN darf wechseln
→ DRA arbeitet auf Home Assistant weiter
→ später Notebook öffnen
→ denselben Auftrag weiter beobachten
```

Geplante V2-Schwerpunkte:

- serverseitiger Operation Manager;
- persistente Operationsmetadaten;
- Wiederanbindung und Clientwechsel;
- serverseitiges Sammelupdate;
- echte Backend-Fortschrittsdaten;
- Pagination großer Vorschauen;
- kontrollierte Multi-Core-/Worker-Nutzung;
- Mobile-/Akku-Härtung;
- erweitertes Diagnose-/Exportmodell;
- Recovery über Home-Assistant-Neustarts hinweg.

Vollständige Roadmap: **[docs/V1_V2_ROADMAP.md](docs/V1_V2_ROADMAP.md)**

---

# V1 → V2 ohne Neustart bei null

DRA V1 wird bewusst als stabile Datenbasis für die spätere V2-Generation behandelt.

Das Ziel für ein Update auf V2 ist die Übernahme von:

- Config Entry;
- Projekten;
- GitHub-Lesetokens;
- separatem Diagnose-Git-Zugang;
- Backup-Retention;
- Seitenleistenoption;
- vorhandenen Sicherungen und Journaldaten.

Eine Neuinstallation nur wegen V2 ist **nicht** das Ziel.

Details: **[docs/UPGRADE_V1_TO_V2.md](docs/UPGRADE_V1_TO_V2.md)**

---

# Projektseite

Die ausführliche öffentliche DRA-Projektseite mit V1-/V2-Evolution, visueller Roadmap, Architektur und Installation:

### **https://thedaimos.github.io/deploy-relay-agent-pub/**

---

# Dokumentation

| Dokument | Inhalt |
| --- | --- |
| **[Handbuch](docs/HANDBUCH.md)** | Bedienung und vollständiger Funktionsumfang |
| **[Installation](docs/INSTALLATION.md)** | HACS-Zielweg, manueller Rückfallweg und Ersteinrichtung |
| **[Funktionen](docs/FEATURES.md)** | V1-Funktionsumfang und geplanter V2-Ausbau |
| **[Releaseinformationen](docs/RELEASES.md)** | V1 RC/FINAL und V2-Ausblick |
| **[V1 → V2 Roadmap](docs/V1_V2_ROADMAP.md)** | Architekturvergleich und Entwicklungsziel |
| **[Sicherheit](docs/SECURITY.md)** | Sicherheitsversprechen und Grenzen |
| **[Datenschutz](docs/PRIVACY.md)** | Umgang mit Tokens, Diagnose- und Clientdaten |
| **[Support & Diagnose](docs/SUPPORT.md)** | Supportdaten und Fehleranalyse |
| **[Fehlerbehebung](docs/TROUBLESHOOTING.md)** | typische Fehlerbilder und sichere Reaktion |
| **[Projektmanifest](docs/PROJECT_MANIFEST.md)** | Grundlagen von `deploy-relay.json` |
| **[V1 → V2 Upgrade](docs/UPGRADE_V1_TO_V2.md)** | Migrationsversprechen |
| **[V1 Release-Checkliste](docs/V1_RELEASE_CHECKLIST.md)** | Gate bis FINAL |
| **[Distributionsplan](docs/INTEGRATION_DISTRIBUTION_PLAN.md)** | DEV → Public → HACS |
| **[Drittkomponenten](THIRD_PARTY.md)** | Runtime-/Plattformabhängigkeiten und Auditstatus |

---

# Repositoryrollen

Dieses öffentliche Repository ist der **Produkt-, Dokumentations- und zukünftige Distributionspunkt** für freigegebene DRA-Versionen.

Private Entwicklung, interne Diagnoseexports und Recovery-/DEV-Artefakte bleiben davon getrennt.

---

# Lizenz und Branding

Soweit nicht ausdrücklich reservierte Branding-Materialien oder Drittmaterial mit eigener Lizenz betroffen sind, stehen Quellcode und Dokumentation unter **GNU GPL Version 3 only (`GPL-3.0-only`)**.

Copyright © 2026 **Christian Köhler / TheDaimos**.

Siehe [LICENSE](LICENSE), [COPYRIGHT.md](COPYRIGHT.md), [AUTHORS.md](AUTHORS.md), [BRANDING.md](BRANDING.md) und [THIRD_PARTY.md](THIRD_PARTY.md).

Der Name **Deploy Relay Agent / DRA**, Logos, Icons, Artwork und die visuelle Identität sind nicht Bestandteil der GPL-3.0-only-Freigabe. Forks und abgeleitete Projekte müssen ein eigenes Branding verwenden, sofern keine separate Erlaubnis vorliegt.

---

<div align="center">

### C.K. – Eine Idee weiter gedacht.

**Deploy Relay Agent · kontrollierte Entwicklungsinfrastruktur für Home Assistant**

</div>
