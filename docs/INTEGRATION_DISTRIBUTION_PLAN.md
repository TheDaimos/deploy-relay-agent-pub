# DRA V1 — Integrations- und Distributionsplan

## Ziel

DRA V1 soll nach der Finalabnahme als öffentlich installierbare Home-Assistant-Custom-Integration bereitstehen.

## Repositoryrollen

### Private DEV

Quelle für:

- Entwicklung;
- Tests;
- Diagnoseexports;
- interne Recoveryinformationen;
- V2-Arbeit.

### Public

Quelle für:

- Projektseite;
- Handbuch;
- Installationsanleitung;
- freigegebene V1-Integration;
- Release Notes;
- HACS-Metadaten;
- stabile Releaseartefakte.

## Promotion

Nur ein vollständig abgenommener Commit darf von DEV nach Public promoviert werden.

```text
DEV candidate
→ CI
→ HA Realtest
→ exact final SHA
→ release freeze
→ public package
→ HACS/release
```

## Vor öffentlicher Codeverteilung

Bevor die Integrationsdateien aus dem privaten DEV-Repository in dieses öffentliche Repository übernommen werden, werden zusätzlich festgelegt und geprüft:

- [x] Lizenz-/Nutzungsmodell für den veröffentlichten Code festgelegt: `GPL-3.0-only`;
- [x] Copyright-/Autorenschaft dokumentiert;
- [x] Branding ausdrücklich vom GPL-Code getrennt;
- [x] Drittkomponenten-/Abhängigkeitsaudit dokumentiert;
- [ ] welche Integrationsdateien öffentlich distribuiert werden;
- welche DEV-, Diagnose- und Recoveryartefakte ausdrücklich privat bleiben;
- automatischer Secret-/Token-Scan;
- HACS-Validierung;
- reproduzierbare Zuordnung zum exakten V1-Final-SHA.

Die Produktseite und Dokumentation können bereits öffentlich sein. Der Integrationscode wird erst nach dieser Freigabe promotet.

## Geplante HACS-Struktur

```text
custom_components/
└── deploy_relay/
    ├── __init__.py
    ├── manifest.json
    ├── config_flow.py
    ├── ...
    └── frontend/

hacs.json
README.md
LICENSE / Hinweise
docs/
```

## Stable vs DEV

Öffentliche Endnutzer sollen nicht automatisch `deploy/dev` folgen.

```text
stable / release tag
→ normale V1-Installation

deploy/dev
→ private Entwicklung / Test
```

## V1 → V2

Der öffentliche Integrationsweg soll später ein normales Update auf V2 ermöglichen. Config Entry, Projekte, Tokens, Backups und Optionen dürfen nicht durch den Architekturwechsel unnötig neu angelegt werden müssen.


## Lizenz- und Copyright-Gate

Status: **ABGESCHLOSSEN — 2026-10-07**

Festgelegt:

```text
Code + Dokumentation:
GPL-3.0-only

Copyright:
Copyright © 2026 Christian Köhler / TheDaimos

Reserviert:
Deploy Relay Agent / DRA
offizielle Logos und Icons
Artwork / Roadmapgrafiken
visuelle Identität

Drittkomponenten:
keine vendorten Drittbibliotheken im V1-Integrationscode gefunden
```

Verbindliche Dateien:

- `LICENSE`
- `COPYRIGHT.md`
- `AUTHORS.md`
- `BRANDING.md`
- `THIRD_PARTY.md`

Damit ist das rechtliche Veröffentlichungsmodell für den öffentlichen V1-Code festgelegt.
