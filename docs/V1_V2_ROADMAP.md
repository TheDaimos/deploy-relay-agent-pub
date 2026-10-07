# DRA V1 → V2 — Evolution

## Kurzfassung

DRA V1 ist der stabile Deployment- und Recovery-Werkzeugkasten.

DRA V2 soll daraus eine **serverseitig besessene Deployment-Engine** machen.

## Was bleibt?

Die bewährten V1-Sicherheitsprinzipien bleiben erhalten:

- LOCKED;
- explizite DEVELOPMENT-Freigabe;
- exakter Commit-SHA;
- Preview vor Mutation;
- Backup vor Mutation;
- Verifikation;
- Rollback;
- Recovery;
- keine automatischen HA-Neustarts.

## Was ändert sich?

| Bereich | DRA V1 | DRA V2 |
|---|---|---|
| Schwerarbeit | bereits im HA-Backend | weiterhin Backend |
| Auftragsbesitz | Client-Request begleitet den Ablauf | Server besitzt den Auftrag |
| Sammelupdate | Frontend orchestriert Sequenz | Backend orchestriert Gesamtauftrag |
| Clientverlust | sichtbarer Ablauf kann getrennt werden | Auftrag läuft unabhängig weiter |
| Reconnect | kein eigener Auftragszustand | Wiederanbindung über Operation-ID |
| Fortschritt | teilweise angenähert im Browser | serverseitiger Zustand/Zähler |
| Große Preview | große Antwort/DOM-Last möglich | Pagination / bedarfsgerechtes Laden |
| Mobile | funktional, aber mehr WebView-Aktivität | deutlich weniger lokale UI-Last |
| Multi-Core | keine aggressive Nutzung | gemessene, begrenzte Workerparallelität |
| Diagnose | Run-/Fehlerdiagnose | Operationszeitlinie inkl. Queue/Worker/Reconnect |
| HA-Neustart | laufender Browserzustand endet | persistente Recovery soll Zustand erklären |

## Zielbild

```text
Handy / Notebook / Tablet
        │
        │ START / STATUS / STEUERUNG
        ▼
DRA Operation Manager
        │
        ├─ Operation-ID
        ├─ Queue
        ├─ Phase
        ├─ Progress
        ├─ Projekt
        ├─ Commit-SHA
        ├─ Backup / Verify / Recovery
        └─ Diagnose
        │
        ▼
GitHub + /config
```

## Performanceziel

V2 soll nicht einfach „mehr Threads“ verwenden.

Stattdessen:

1. HA-Haupt-Ereignisschleife schützen;
2. RAM-Spitzen begrenzen;
3. I/O kontrollieren;
4. Client-/Mobile-Last reduzieren;
5. sichere read-only Phasen begrenzt parallelisieren;
6. erst dann Laufzeit optimieren.

## Verbindung

V2-Ziel:

```text
Handy startet Auftrag im WLAN
→ Display aus
→ WLAN verlassen
→ Mobilfunk/VPN wechselt
→ DRA arbeitet auf dem HA-Server weiter
→ später Notebook öffnen
→ denselben Auftrag weiter beobachten
```

## Status

V2 ist **geplant**, nicht veröffentlicht. Die Architektur ist im privaten Entwicklungsrepository als verbindlicher Umbauplan festgehalten. V1 wird vorher vollständig als stabile Integration fertiggestellt.
