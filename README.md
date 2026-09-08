# M450-Client

Client for the M450 Project

## Testübersicht

### UI

| TF-ID    | Klasse | Test                   | Erwartetes Ergebnis              |
| -------- | ------ | ---------------------- | -------------------------------- |
| TF-UI-01 | Button | Maus über Button       | Farbe wird dunkler               |
| TF-UI-02 | Button | Maus ausserhalb Button | Farbe bleibt unverändert         |
| TF-UI-03 | Button | Linksklick innerhalb   | `on_click` wird aufgerufen       |
| TF-UI-04 | Button | Linksklick ausserhalb  | `on_click` wird nicht aufgerufen |
| TF-UI-05 | Button | Rechtsklick innerhalb  | `on_click` wird nicht aufgerufen |
