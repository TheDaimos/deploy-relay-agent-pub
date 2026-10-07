# Deploy Relay Agent V1 — Installation

> Status: **V1.0.0 RC3 · Finalkandidat**  
> Öffentliche Integrationsverteilung: **technisch vorbereitet · noch nicht FINAL freigegeben**  
> DRA V2 ist eine spätere Architekturentwicklung und nicht Bestandteil der V1-Installation.

## Zielbild

DRA V1 ist als normale Home-Assistant-Custom-Integration für die öffentliche Distribution vorbereitet. Die öffentliche Distribution wird bewusst vom privaten Entwicklungsrepository getrennt:

```text
privates DEV-Repository
        │
        │ geprüfter Release-Stand
        ▼
öffentliches DRA-Repository
        │
        ├─ Home-Assistant-Integration
        ├─ Release Notes
        ├─ Dokumentation
        └─ HACS-Distribution
```

Der öffentliche Stand enthält ausschließlich freigegebene Release-Inhalte. Diagnoseexports, interne Recovery-Daten und Entwicklungsartefakte bleiben im privaten DEV-Bereich.

## Geplanter bevorzugter Installationsweg — HACS

Nach Abschluss der V1-Finalabnahme wird DRA über HACS als benutzerdefiniertes Repository freigegeben. Die HACS-Struktur und Metadaten sind im RC3-Public-Kandidaten bereits vorhanden.

**Repository für HACS — Copy & Paste:**

```text
https://github.com/TheDaimos/deploy-relay-agent-pub
```

1. HACS öffnen.
2. **Integrationen** öffnen.
3. Über das Menü **Benutzerdefinierte Repositories** auswählen.
4. die oben angegebene Repository-URL einfügen.
5. Kategorie **Integration** auswählen und das Repository hinzufügen.
6. **Deploy Relay Agent** installieren.
7. Home Assistant vollständig neu starten.
8. Unter **Einstellungen → Geräte & Dienste → Integration hinzufügen** nach **Deploy Relay Agent** suchen.
9. DRA konfigurieren.
10. DRA startet grundsätzlich im Zustand **GESPERRT / LOCKED**.

Der exakte öffentliche Repository-Link und der stabile Releasekanal werden mit V1 FINAL freigeschaltet.

## Manueller Installationsweg

Als Rückfallweg wird V1 zusätzlich als Release-Paket bereitgestellt.

Nach Veröffentlichung:

1. Release-Paket herunterladen.
2. Verzeichnis `custom_components/deploy_relay/` vollständig nach `/config/custom_components/deploy_relay/` kopieren.
3. Home Assistant vollständig neu starten.
4. **Deploy Relay Agent** als Integration hinzufügen.

Manuelles Überschreiben einzelner Dateien wird nicht empfohlen. Ein Release muss immer als zusammengehöriger Integrationsstand behandelt werden.

## Ersteinrichtung

DRA benötigt für private GitHub-Projekte einen Fine-grained Lesetoken mit möglichst kleinen Rechten:

```text
Metadata: Read
Contents: Read
```

Für den optionalen Diagnoseexport wird bewusst ein **separater** Schreibtoken verwendet. Der normale Projekt-/Deploymenttoken bleibt read-only.

## Sicherheitszustand nach Installation

Nach jedem vollständigen Home-Assistant-Neustart:

```text
DRA = LOCKED
```

Schreibzugriffe erfordern eine explizite DEVELOPMENT-Freigabe. DRA aktiviert DEVELOPMENT nicht dauerhaft und startet Home Assistant niemals automatisch neu.

## Update V1

Ein stabiler V1-Release wird nur gegen einen unveränderlichen Release-/Tag-Stand ausgeliefert. Der bewegliche Entwicklungszweig `deploy/dev` ist **kein stabiler Endnutzerkanal**.

## Späteres Update V1 → V2

Die V2-Entwicklung muss bestehende V1-Daten übernehmen können:

- Config Entry;
- Projekte;
- GitHub-Lesetokens;
- separaten Diagnose-Git-Zugang;
- Backup-Retention;
- Seitenleistenoption;
- vorhandene DRA-Backups und Journale.

Eine Neuinstallation nur wegen V2 ist ausdrücklich nicht das Ziel.

## Noch nicht freigegeben

Solange V1.0.0 noch RC3 / Finalkandidat ist, dienen die öffentlichen Installationsschritte der Abnahme und Vorbereitung. Die Freigabe für normale Nutzung erfolgt erst nach bestandener V1-Final- und Distributionsabnahme.
