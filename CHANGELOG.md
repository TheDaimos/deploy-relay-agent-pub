# Deploy Relay Agent — Public Changelog

## V1.0.0 FINAL — 2026-10-09

DRA V1.0.0 ist als vollständige Home-Assistant-Integration und stabiler Rückfallstand freigegeben.

### RC3

- exakter privater Finalkandidat: `5550b40de7b7eb62439bd88ee175281fc5891d7d`;
- Validate #785: SUCCESS;
- öffentliche Produkt-/Repositoryidentität gehärtet;
- DRA-Selbsterkennung im Sammelupdate über stabile Projekt-ID statt Repositoryname;
- Home-Assistant-Übersetzungstexte Hassfest-kompatibel;
- öffentliche Runtimepromotion über Git-Blob-Provenienz nachweisbar;
- Integrationslogo, HACS-Metadaten und Stable-Kanal vorbereitet;
- reproduzierbarer manueller ZIP-Build vorbereitet.

### Produktisierung

- öffentlicher Projektauftritt erweitert;
- vollständiges Handbuch;
- Installationsanleitung;
- Release-/Featureübersicht;
- Sicherheits- und Supportdokumentation;
- öffentlicher DEV→Release→HACS-Distributionsplan;
- V1→V2-Roadmap.

### Runtime

Die V1.0.0-Runtime basiert funktional auf dem abgenommenen 0.15.30-Stand. Die Releasepromotion selbst führt keine neue Deploymentlogik ein.

### FINAL-Status

- reale V1-Abnahme abgeschlossen;
- HACS/Hassfest/Public Validation grün;
- öffentlicher Stable-Kanal freigegeben;
- Freeze-Ref `freeze/v1.0.0-final` gesetzt;
- V1 als stabiler Produkt- und Rückfallstand dokumentiert;
- V2-00 abgeschlossen und V2-05 freigegeben.

---

## V2 — geplant

Schwerpunkt: serverseitige Operationsarchitektur, Reconnect, Backend-Sammelupdate, Multi-Core/Worker-Audit, Pagination, Mobile-/Akku-Härtung sowie Diagnoseexport V2.
