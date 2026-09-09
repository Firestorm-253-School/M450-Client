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

### Maps

| TF-ID     | Klasse | Test                                     | Erwartetes Ergebnis                                    |
| --------- | ------ | ------------------------------------------ | --------------------------------------------------------- |
| TF-MAP-01 | Map    | Anzahl Spawnpunkte (max. 4 Spieler)       | Jede Map hat genau 4 Spawnpunkte                           |
| TF-MAP-02 | Map    | Spawnpunkt liegt auf einer Wand            | Kein Spawnpunkt ist eine Wand                              |
| TF-MAP-03 | Map    | Spawnpunkt ausserhalb des Spielfelds       | Alle Spawnpunkte liegen innerhalb des Grids                |
| TF-MAP-04 | Map    | Lücke im Aussenrand                        | Kompletter Rand ist eine Wand                              |
| TF-MAP-05 | Map    | Bereich durch Hindernis eingeschlossen     | Alle freien Felder sind vom Spawnpunkt aus erreichbar      |
| TF-MAP-06 | Map    | Zwei Maps mit gleichem Namen                | Alle Map-Namen sind eindeutig                              |
| TF-MAP-07 | Map    | Hindernis im Innenbereich von Classic       | Classic hat keine inneren Hindernisse                      |

### Snake

| TF-ID       | Klasse | Test                                   | Erwartetes Ergebnis                                |
| ----------- | ------ | ----------------------------------------- | ------------------------------------------------------ |
| TF-SNAKE-01 | Snake  | Spawn auf Solo-Spawnpunkt (oben links)   | Kopf der Snake liegt exakt auf `start_for(0)`           |
| TF-SNAKE-02 | Snake  | Spawn erzeugt zwei Segmente               | Snake besteht aus zwei benachbarten Feldern             |
| TF-SNAKE-03 | Snake  | Beide Segmente an jedem Spawnpunkt        | Kopf UND Schwanz liegen nie auf einer Wand              |

### Networking

| TF-ID     | Klasse     | Test                                  | Erwartetes Ergebnis                              |
| --------- | ---------- | ---------------------------------------- | --------------------------------------------------- |
| TF-NET-01 | GameClient | Nachricht senden ohne aktive Verbindung  | Nachricht landet in der Sende-Warteschlange          |
| TF-NET-02 | GameClient | Zustand direkt nach Erstellung           | Empfangs-Warteschlange ist leer                      |

### GameScreen (Server-Anbindung)

| TF-ID    | Klasse     | Test                                  | Erwartetes Ergebnis                                        |
| -------- | ---------- | ---------------------------------------- | --------------------------------------------------------------- |
| TF-GS-01 | GameScreen | Level wird gestartet                     | `create_game`-Nachricht wird an den Server geschickt             |
| TF-GS-02 | GameScreen | Pfeiltaste gedrückt                      | Passende `set_direction`-Nachricht wird geschickt                |
| TF-GS-03 | GameScreen | Server schickt neue Kopfposition         | Bewegungsrichtung wird korrekt aus der Positionsänderung abgeleitet |
| TF-GS-04 | GameScreen | Server schickt unveränderte Position     | Bewegungsrichtung bleibt unverändert                             |
| TF-GS-05 | GameScreen | Server schickt `game_over`               | `game_over`-Status wird gesetzt                                  |
