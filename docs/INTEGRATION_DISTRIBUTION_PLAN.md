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
