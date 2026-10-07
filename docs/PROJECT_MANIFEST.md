# Deploy Relay Agent — Projektmanifest

DRA-Projekte beschreiben ihren verwalteten Deploymentbereich über:

```text
deploy-relay.json
```

## Minimalprinzip

Ein Manifest beantwortet:

- Welches Projekt ist das?
- Aus welchem Repository kommt es?
- Welche Quellpfade gehören dazu?
- Wohin dürfen sie unter `/config` geschrieben werden?
- Wie wird der Zielbereich behandelt?
- Welche Nachaktion ist nach Installation erforderlich?
- Welche Sicherheitslimits gelten?

## Beispiel

```json
{
  "schema": "deploy-relay.deployment.v1",
  "project": {
    "id": "example_project",
    "name": "Example Project"
  },
  "source": {
    "repository": "OWNER/REPOSITORY",
    "mode": "repository_contents"
  },
  "deployment": {
    "root": "/config",
    "groups": [
      {
        "id": "integration",
        "source": "custom_components/example_project",
        "target": "custom_components/example_project",
        "mode": "replace_directory"
      }
    ]
  },
  "lifecycle": {
    "after_install": "home_assistant_restart"
  },
  "policy": {
    "allow_symlinks": false,
    "max_files": 1000,
    "max_uncompressed_bytes": 52428800
  }
}
```

## `replace_directory`

DRA behandelt den verwalteten Zielbaum als vollständigen Sollzustand.

Dadurch können Dateien nicht nur hinzugefügt/geändert, sondern auch bewusst entfernt werden.

Genau deshalb sind Preview, Backup und Verifikation Pflichtbestandteile.

## Lifecycle

Mögliche fachliche Nachaktionen werden konservativ behandelt.

Für eine typische Home-Assistant-Integration:

```json
"lifecycle": {
  "after_install": "home_assistant_restart"
}
```

DRA kann bei rein statischen Frontendänderungen eine leichtere Nachaktion klassifizieren, führt aber keine Nachaktion still automatisch aus.

## Sicherheitslimits

Limits schützen vor falsch konfigurierten oder unerwartet großen Deployments.

Das Manifest ist keine Möglichkeit, DRA in einen beliebigen Dateischreiber umzuwandeln.

## Empfohlener Kanal

Zusätzlich kann ein Projekt eine Datei:

```text
deploy-relay-channel.json
```

bereitstellen. Sie beschreibt den empfohlenen beweglichen Ref, zum Beispiel `deploy/dev`.

DRA löst diesen Ref beim Übernehmen auf einen exakten Commit-SHA auf.
