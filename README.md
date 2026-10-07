# Deploy Relay Agent

**Kontrollierte Git-Deployments für Home Assistant — mit nachvollziehbarer Quelle, Vorschau, Sicherung, Verifikation und Recovery.**

> **DRA V1.0.0:** Release Candidate / Finalisierung läuft  
> **DRA V2:** nächste Architektur bereits verbindlich geplant

[Projektseite](https://thedaimos.github.io/deploy-relay-agent-pub/) · [Handbuch](docs/HANDBUCH.md) · [Installation](docs/INSTALLATION.md) · [V1 → V2](docs/V1_V2_ROADMAP.md) · [Releases](docs/RELEASES.md) · [Sicherheit](docs/SECURITY.md)

---

## DRA V1 — stabiler Deployment- und Recovery-Werkzeugkasten

DRA V1 macht aus einem Git-Stand einen kontrollierten Home-Assistant-Deploymentlauf:

```text
Git-Quelle
→ exakten Commit-SHA einfrieren
→ Vorschau + SHA-256
→ DEVELOPMENT bewusst freigeben
→ Staging
→ Backup
→ Installation
→ Verifikation
→ SUCCESS / ROLLBACK / RECOVERY_REQUIRED
```

### V1 Highlights

| Bereich | Funktion |
|---|---|
| Quelle | Branch/Tag/Commit auf exakten SHA einfrieren |
| Vorschau | Neu / Geändert / Entfernt / Unverändert |
| Integrität | SHA-256-Dateivergleich |
| Sicherheit | LOCKED → explizites DEVELOPMENT |
| Installation | Staging vor Mutation |
| Recovery | Backup, Rollback, RECOVERY_REQUIRED |
| Sicherungen | projektbezogene Vollsicherungen + Retention |
| Restore | Sicherheitssicherung vor Wiederherstellung |
| Sammelupdate | mehrere Projekte sequenziell prüfen/installieren |
| Lifecycle | Frontend-Neuladen oder vollständiger HA-Neustart |
| Diagnose | strukturierte Logs, Supportdaten, Git-Export |
| Mobile | Desktop, Tablet und Companion App |

---

## DRA V2 — vom clientbegleiteten Ablauf zur serverseitigen Deployment-Engine

V2 ist keine kosmetische Versionserhöhung. Die nächste Generation verschiebt **Auftragsbesitz, Orchestrierung, Fortschritt und Wiederanbindung vollständig zum Home-Assistant-Server**.

Wichtig: Die schwere Git-/Datei-/Hash-/Backup-/Installationsarbeit läuft bereits in V1 im Backend. V2 beseitigt zusätzlich die verbleibende Abhängigkeit des Ablaufs vom gerade verbundenen Client.

| DRA V1 | DRA V2 |
|---|---|
| Client begleitet lange Requests | Server besitzt den Auftrag |
| Sammelupdate wird im Frontend fortgeschaltet | Sammelupdate läuft als Backendauftrag |
| Clientverlust kann den sichtbaren Ablauf trennen | Auftrag läuft ohne Client weiter |
| kein eigener Reconnect-Auftrag | Wiederanbindung über Operation-ID |
| Fortschritt teilweise browserseitig angenähert | echte Backendphasen/-zähler |
| große Vorschau kann Browser belasten | Pagination / bedarfsgerechtes Laden |
| mehr WebView-Aktivität auf Mobile | deutlich weniger lokale Last |
| konservative Einzelarbeit | gemessene Multi-Core-/Worker-Nutzung |
| Diagnose pro Run | Operationszeitlinie inkl. Queue/Worker/Reconnect |

### V2 Ziel

```text
Handy startet Auftrag im WLAN
→ App darf in den Hintergrund
→ WLAN/Mobilfunk/VPN darf wechseln
→ DRA arbeitet auf Home Assistant weiter
→ später Notebook öffnen
→ denselben Auftrag weiter beobachten
```

Mehr dazu: **[DRA V1 → V2 Roadmap](docs/V1_V2_ROADMAP.md)**

---

## Installation

Der bevorzugte öffentliche Installationsweg für V1 FINAL wird **HACS**. Das öffentliche Repository ist bereits als Distributions- und Dokumentationsort vorbereitet.

Bis zum abgeschlossenen Realtest bleibt V1.0.0 als Release Candidate gekennzeichnet.

→ **[Installationsanleitung](docs/INSTALLATION.md)**  
→ **[Integrations-/Distributionsplan](docs/INTEGRATION_DISTRIBUTION_PLAN.md)**

---

## Sicherheit

DRA bleibt absichtlich restriktiv:

- LOCKED nach jedem HA-Neustart;
- DEVELOPMENT nur explizit;
- keine beliebigen Shellskripte;
- keine stillen Projektwrites;
- exakter Commit-SHA statt beweglichem Ref als Ausführungsidentität;
- Backup vor Mutation;
- Verifikation danach;
- getrennte GitHub-Lese- und Diagnose-Schreibtokens;
- kein automatischer Home-Assistant-Neustart.

→ **[Sicherheitsmodell](docs/SECURITY.md)**

---

## Dokumentation

- **[Handbuch](docs/HANDBUCH.md)** — Bedienung und Funktionsumfang
- **[Installation](docs/INSTALLATION.md)** — HACS-Zielweg, manueller Rückfallweg, Ersteinrichtung
- **[Releases](docs/RELEASES.md)** — V1 RC/FINAL und V2-Ausblick
- **[V1 → V2 Roadmap](docs/V1_V2_ROADMAP.md)** — Architekturvergleich
- **[Sicherheit](docs/SECURITY.md)** — Sicherheitsversprechen
- **[Support & Diagnose](docs/SUPPORT.md)** — Supportdaten und Fehleranalyse
- **[FAQ](docs/FAQ.md)** — häufige Fragen
- **[Integrations-/Distributionsplan](docs/INTEGRATION_DISTRIBUTION_PLAN.md)** — DEV → Public → HACS

---

## Repositoryrollen

Dieses öffentliche Repository ist der **Projekt-, Dokumentations- und zukünftige Distributionspunkt** für freigegebene DRA-Versionen.

Die eigentliche Entwicklung, interne Diagnoseexports und Recovery-/DEV-Artefakte bleiben getrennt im privaten Entwicklungsbereich.

---

**C.K. – Eine Idee weiter gedacht.**
