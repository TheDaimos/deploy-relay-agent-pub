# Deploy Relay Agent V1 — Installation

> Status: **V1.0.0 FINAL · FROZEN**  
> Öffentliche Integrationsverteilung: **FINAL freigegeben**  
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

## Bevorzugter Installationsweg — HACS

DRA V1.0.0 FINAL wird über HACS als benutzerdefiniertes Repository bereitgestellt. HACS-Struktur, Metadaten und Validierung sind Bestandteil des freigegebenen Public-Standes.

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

Der öffentliche Repository-Link und der stabile Releasekanal sind mit V1.0.0 FINAL freigegeben.

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

## FINAL freigegeben

Diese Installationsschritte gelten für DRA V1.0.0 FINAL. Der stabile V1-Stand bleibt als Rückfallpunkt erhalten.
