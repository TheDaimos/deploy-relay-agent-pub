# Deploy Relay Agent — FAQ

## Ist DRA ein automatischer Updater?

Nein. DRA verlangt bewusste Quellenauswahl, Vorschau und Freigabe.

## Startet DRA Home Assistant automatisch neu?

Nein.

## Warum friert DRA einen Commit ein?

Branches und andere Git-Refs können sich verändern. Der exakte Commit macht die ausgeführte Quelle reproduzierbar.

## Ist V1 clientseitig?

Nicht vollständig. Git-, Datei-, Hash-, Backup- und Installationsarbeit läuft bereits im Home-Assistant-Backend. In V1 sind jedoch Ablaufbegleitung, Teile der Fortschrittsdarstellung und die Sammelupdate-Orchestrierung noch stärker an den verbundenen Browser gebunden.

## Was verbessert V2?

V2 soll den vollständigen Auftrag serverseitig besitzen, reconnect-fähig machen, große Vorschauen paginieren und vorhandene Serverressourcen kontrolliert besser nutzen.

## Wird V2 Multi-Core nutzen?

Geplant ist begrenzte, messwertgestützte Parallelität. Die Anzahl sichtbarer vCPU wird nicht 1:1 zur Workerzahl.

## Muss ich für V2 neu installieren?

Das ist nicht das Ziel. V1 soll die stabile Datenbasis für ein späteres Update auf V2 bilden.

## Kann DRA private Repositories verwenden?

Ja, mit einem möglichst eng berechtigten Fine-grained Lesetoken.

## Warum gibt es einen zweiten Token für Diagnose-Git-Export?

Damit der normale Projektzugang read-only bleiben kann.
