# M450-Client

Client for the M450 Project

## Testübersicht

### UI

| TF-ID    | Klasse | Test                        | Erwartetes Ergebnis               |
| -------- | ------ | --------------------------- | --------------------------------- |
| TF-UI-01 | Button | Maus über Button            | hover = True                      |
| TF-UI-02 | Button | Maus ausserhalb Button      | hover = False                     |
| TF-UI-03 | Button | Linksklick innerhalb        | `on_click` wird aufgerufen        |
| TF-UI-04 | Button | Linksklick ausserhalb       | `on_click` wird nicht aufgerufen  |
| TF-UI-05 | Button | Rechtsklick innerhalb       | `on_click` wird nicht aufgerufen  |
| TF-UI-06 | Input  | Initialisierung             | Input ist leer und inaktiv        |
| TF-UI-07 | Input  | Klick innerhalb             | Input wird aktiviert              |
| TF-UI-08 | Input  | Klick ausserhalb            | Input wird deaktiviert            |
| TF-UI-09 | Input  | Zeichen eingeben            | Zeichen wird zum Wert hinzugefügt |
| TF-UI-10 | Input  | Mehrere Zeichen eingeben    | Alle Zeichen werden übernommen    |
| TF-UI-11 | Input  | Backspace                   | Letztes Zeichen wird entfernt     |
| TF-UI-12 | Input  | Enter                       | Aktueller Wert wird zurückgegeben |
| TF-UI-13 | Input  | Zeichen bei inaktivem Input | Wert bleibt unverändert           |

### Maps

| TF-ID     | Klasse | Test                                    | Erwartetes Ergebnis                              |
| --------- | ------ | --------------------------------------- | ------------------------------------------------ |
| TF-MAP-01 | Map    | Startposition liegt auf einer Wand      | Startposition ist nie eine Wand                  |
| TF-MAP-02 | Map    | Startposition ausserhalb des Spielfelds | Startposition liegt immer innerhalb des Grids    |
| TF-MAP-03 | Map    | Lücke im Aussenrand                     | Kompletter Rand ist eine Wand                    |
| TF-MAP-04 | Map    | Bereich durch Hindernis eingeschlossen  | Alle freien Felder sind vom Start aus erreichbar |
| TF-MAP-05 | Map    | Zwei Maps mit gleichem Namen            | Alle Map-Namen sind eindeutig                    |
| TF-MAP-06 | Map    | Hindernis im Innenbereich von Classic   | Classic hat keine inneren Hindernisse            |
