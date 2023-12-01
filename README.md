# Projektarbeit Programmierung II

## Das Spiel 2048 mit Python

- Lina Schuppan (LS)
- Bashkim Mehmeti (BM)
- Eike Gosch (EG)
- Marcel Tams (MT)

## Steuerung:
 
- Schaltflächen grundsätzlich mit der Maus
- Das Spiel kann aus dem Homebildschirm mit der Leertaste gestartet werden
- Im Spiel werden die Pfeiltasten benutzt
- Im Spiel kann mit der Taste "q" das Spiel beendet werden
- In der GameOver Anzeige kann der Name direkt eingegeben werden und wird mit Return bestätigt

## Voraussetzungen

- Python 3.6
- Pygame
- Pytest

## Arbeitsmatrix

| Task                          | Beteiligt | Beschreibung                                              |
|-------------------------------|-----------|-----------------------------------------------------------|
| Konzeptionierung              | alle      | Bestimmung des Vorgehens                                  |
| Erstellung "ePK"              | LS, MT    | Darstellung der Game-Logik                                |
| Erstellung Grafiken           | LS        | Benötigte Grafikkomponenten                               |
| Components mit Vererbung      | LS, MT    | Klassen für die Komponenten mit Superklasse               |
| Kontrolle "ePK"               | alle      | Logische Prüfung                                          |
| Aufbau Grundgerüst            | alle      | Game-Loop aufbauen in gemeinsamer Session                 |
| Szenen Manager implementieren | MT        | Der Game Loop ruft die Methoden auf der aktiven Szene auf |
| Tests aufsetzen               | MT        | Testing mit Pytest vorbereiten                            |
| Resolver erstellen            | MT, EG    | testgetriebene Erstellung der Spiellogik                  |
| Score Tracking                | MT        | Observer für die Erfassung der Highscores                 |
| Name Input                    | MT        | Eingabefeld für den Namen                                 |
| Highscore-Liste               | EG, BM    | Erstellung der Highscore-Liste                            |
| Logik des Farbzugriffs        | MT, BM    | Die Kacheln werden nach dem Text gefärbt                  |
| Zeichnen des Spielfelds       | BM        | Wertzuweisung in den Kacheln                              |
| Schützen der Klassenvar.      | BM        | Klassenvar. -> private, getter/setter                     |
| Szenen als Enums              | MT        | Die Sznenen werden über Enums angesprochen                |
