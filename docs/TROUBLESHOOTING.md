# Deploy Relay Agent — Fehlerbehebung

## Grundregel

Bei Unsicherheit zuerst **nicht weiter mutieren**.

```text
STOP
→ Zustand ansehen
→ Diagnose sichern
→ Quelle/Commit prüfen
→ Backup/Transaktion prüfen
→ erst dann nächsten Schritt ausführen
```

## Projekt zeigt „neuerer empfohlener Stand verfügbar“

Ein beweglicher Ref wie `deploy/dev` wurde seit der letzten Übernahme weitergeschoben.

Lösung:

1. **Aktualisieren**;
2. neuen empfohlenen Commit prüfen;
3. **Quelle übernehmen**;
4. neue Vorschau berechnen.

DRA installiert einen veralteten eingefrorenen Stand nicht still als „aktuell“.

## Vorschau zeigt gleiche Version, aber Dateiänderungen

Versionsmarker und Dateiwahrheit sind getrennte Signale.

Wenn die Versionskennung gleich bleibt, verwaltete Dateien aber abweichen, ist die Dateidrift real und muss geprüft werden.

## Installieren ist gesperrt

Prüfen:

- Quelle übernommen?
- Vorschau frisch?
- Regression bestätigt?
- DEVELOPMENT explizit aktiviert?
- empfohlener Ref inzwischen weitergelaufen?
- Blocker in der Vorschau?

## Neustart erforderlich bleibt sichtbar

Ein Projekt mit Backend-/Mischänderung benötigt vollständigen Home-Assistant-Neustart.

DRA startet HA nicht automatisch neu.

Nach dem echten HA-Neustart wird DRA wieder LOCKED geladen.

## Frontend-Neuladen genügt

Wenn ausschließlich sichere statische Frontendpfade betroffen sind, kann DRA statt HA-Neustart ein Frontend-/Companion-Neuladen empfehlen.

## Restore ist nicht verfügbar

Mögliche Gründe:

- Legacy-Delta-Backup statt vollständigem Snapshot;
- Backup nicht verifiziert;
- Projekt/Sicherungsidentität passt nicht;
- DRA ist LOCKED;
- Sicherheitsprüfung hat den Restore fail-closed blockiert.

## Diagnose-Git-Export ist nicht eingerichtet

Der Diagnoseexport verwendet einen **separaten** Schreibtoken.

Der normale Projekt-/Deploymenttoken soll read-only bleiben.

## Git-Export war eingerichtet und ist nach Reconfigure weg

Für V1 FINAL existiert ein eigener Regressionstest, der genau diesen Fall absichert. Bei einem Kandidaten, der das noch zeigt, V1-Finalisierung stoppen und Diagnose sichern.

## Mobile Verbindung bricht während langer Operation ab

Bekannte V1-Grenze:

- eigentliche Backendarbeit kann bereits serverseitig laufen;
- der aktuelle Client-Request und die UI können jedoch getrennt werden;
- Sammelupdate wird in V1 noch teilweise vom Frontend orchestriert.

Nicht blind erneut dieselbe Mutation starten. Erst DRA-Zustand/Diagnose prüfen.

V2 adressiert diesen Punkt mit serverseitiger Operation-ID und Reconnect.

## RECOVERY_REQUIRED

`RECOVERY_REQUIRED` ist absichtlich ernst.

Es bedeutet: DRA kann keinen eindeutig sicheren Zielzustand beweisen.

Vorgehen:

1. keine weitere Installation;
2. Diagnoseexport sichern;
3. Transaction Journal und Backup identifizieren;
4. Recoverypfad gezielt prüfen;
5. erst nach bewiesenem Zustand weiterarbeiten.

## Supportdaten

Siehe [SUPPORT.md](SUPPORT.md).
