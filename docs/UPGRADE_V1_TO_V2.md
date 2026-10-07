# DRA V1 → V2 — Upgradeversprechen

## Ziel

DRA V2 soll als normale Weiterentwicklung einer bestehenden V1-Installation funktionieren.

Eine Neuinstallation nur wegen der neuen Operationsarchitektur ist **nicht** das Ziel.

## Zu erhaltende V1-Daten

Der V2-Upgradepfad muss mindestens erhalten:

- Home-Assistant-Config-Entry;
- konfigurierte Projekte/Subentries;
- GitHub-Lesetokens;
- separaten Diagnose-Git-Zugang;
- Backup-Retention je Projekt;
- Seitenleistenoption;
- gewählte Quellen/Projektmetadaten;
- vorhandene Backups;
- vorhandene Transaction Journals.

## Was V2 neu ergänzt

- Operation Manager;
- serverseitige Operation-IDs;
- Operationspersistenz;
- Queue-/Lockzustand;
- Reconnect;
- Parent-/Child-Aufträge;
- neues Diagnose-/Exportschema.

## Migration

Neue V2-Daten werden in einem DRA-eigenen Bereich unter `/config/deploy_relay/` verwaltet.

Keine direkte Manipulation von Home Assistants `.storage`.

## Rückfall

V1 FINAL bleibt als dokumentierter Rückfallpunkt verfügbar.

Eine V2-Migration darf bestehende V1-Sicherungen nicht still unbrauchbar machen.

## Finales V2-Gate

V2 wird erst FINAL, wenn Migration und Rückfall auf einer realen Home-Assistant-DEV-Instanz vollständig nachgewiesen sind.
