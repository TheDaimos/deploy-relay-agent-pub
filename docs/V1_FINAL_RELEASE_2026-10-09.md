# Deploy Relay Agent V1.0.0 — FINAL / FROZEN

Freigabe: **2026-10-09**

## Finalstatus

Deploy Relay Agent V1.0.0 ist als **FINAL / FROZEN** freigegeben.

Verbindliche technische Herkunft:

- private Runtimebasis: `TheDaimos/deploy-relay-agent-dev`
- RC3-Runtimecommit: `5550b40de7b7eb62439bd88ee175281fc5891d7d`
- private CI: Validate #785 SUCCESS
- öffentliche Runtime-Provenienz: `docs/RUNTIME_PROVENANCE.json`
- öffentlicher FINAL-Stand: `main` / `stable` / `freeze/v1.0.0-final`
- Stable-Ref: `stable`
- Freeze-Ref: `freeze/v1.0.0-final`

Der FINAL-Dokumentationsstand verändert den freigegebenen RC3-Runtimeinhalt nicht.

## Abnahmeentscheidung

Die aktuelle Finalabnahme bestätigte unter anderem:

- Startzustand LOCKED nach Home-Assistant-Neustart;
- Erhalt bestehender Projekte und Konfigurationen;
- Seitenleistenpersistenz;
- Quellenauflösung auf exakten Commit;
- read-only Vorschau und SHA-256;
- explizite DEVELOPMENT-Freigabe;
- Staging, Backup, Installation und Zielverifikation;
- sequenzielles Sammelupdate und Stop-on-Failure-Logik;
- DRA-Selbstupdate zuletzt;
- Diagnoseoberfläche;
- separaten Diagnose-Git-Schreibzugang;
- Reconfigure ohne Verlust des Diagnoseexports;
- Tokenredaction und Sicherheitsregressionen;
- bekannte V1-Grenzen und deren Übernahme in die V2-Roadmap.

Restore- und frische Installationspfade wurden bereits in früheren Realtests erprobt. Da seit diesen Erprobungen keine Runtimeänderungen an den betreffenden Pfaden vorgenommen wurden, wurden sie für diese FINAL-Entscheidung ausdrücklich als nicht erneut releaseblockierend akzeptiert. Die aktuellen Schutzdialoge, Restore-Sicherheitskette und automatisierten Regressionstests wurden zusätzlich erneut geprüft.

## Releasevertrag

DRA V1.0.0 bleibt der stabile Produkt- und Rückfallstand.

Für V1 gelten weiterhin insbesondere:

- LOCKED als Standardzustand;
- DEVELOPMENT nur ausdrücklich und runtime-only;
- exakter Commit-Freeze;
- Preview vor Mutation;
- Backup vor Mutation;
- Verifikation nach Mutation;
- Rollback / RECOVERY_REQUIRED bei unsicherem Zustand;
- kein automatischer Home-Assistant-Neustart;
- getrennte Lese- und Diagnose-Schreibzugänge;
- redigierte Diagnose- und Exportdaten.

## V2

Mit dieser Freigabe ist **V2-00 abgeschlossen**. V2 darf auf Basis des eingefrorenen V1-Referenzstandes fortgesetzt werden.

V1 bleibt dabei unverändert als Rückfall- und Vergleichsbasis erhalten.

---

**C.K. – Eine Idee weiter gedacht.**
