# Deploy Relay Agent — Support & Diagnose

## Bei einem Problem

Für eine belastbare Analyse sind hilfreich:

1. sichtbare DRA-Version;
2. Projekt;
3. gewählte Quelle / Commit-SHA;
4. Phase, in der der Fehler auftrat;
5. DRA-Diagnoseexport;
6. ob ein Home-Assistant-Neustart bereits erfolgt ist.

## Diagnose & Logs

DRA besitzt eine eigene Diagnoseoberfläche. Sie zeigt strukturierte Vorgänge statt ausschließlich freien Logtext.

## JSON / Supportdaten

Supportdaten werden redigiert. Tokens und bekannte Secretmuster dürfen nicht in einem Supportexport landen.

## Diagnose nach Git

Der optionale Git-Export schreibt ausschließlich in den reservierten Diagnosebereich des privaten Projekt-/DEV-Repositories und benötigt einen separaten Schreibtoken.

## Keine Secrets veröffentlichen

Vor dem Teilen trotzdem prüfen:

- GitHub-Token;
- API-Keys;
- Passwörter;
- Authorization-Header;
- Cookies;
- private Schlüssel.

## V1-Verbindungsgrenze

WLAN-/Mobilfunk-/VPN-Wechsel während einer langen V1-Operation kann den beobachtenden Client vom laufenden Ablauf trennen. Das ist eine dokumentierte V1-Architekturgrenze und Kernbestandteil der V2-Planung.
