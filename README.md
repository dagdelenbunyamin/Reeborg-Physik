# Reeborg's World: Staubsauger-Algorithmus 🤖🧹

Dieses Repository enthält eine Python-Lösung für den "Reeborg's World" Roboter. Das Ziel ist es, ein komplettes quadratisches Feld Reihe für Reihe abzufahren – genau wie ein Staubsauger- oder Rasenmäher-Roboter.

## 📋 Aufgabenbeschreibung
Der Roboter startet an der Position **(1, 1)** (unten links) mit Blickrichtung Osten. Er soll das gesamte Gitter abdecken, indem er:
1. Eine komplette Reihe bis zur Wand abfährt.
2. Am Ende der Reihe eine "Schlangenlinien-Wende" macht.
3. In der darüberliegenden Reihe zurückfährt.
4. Dies wiederholt, bis das gesamte Feld gereinigt wurde.



## 🛠️ Verwendete Konzepte
* **Funktionen (`def`):** Zur Kapselung von Drehungen und Fahrlogik.
* **While-Schleifen:** Um flexibel auf Wände zu reagieren (unabhängig von der Feldgröße).
* **Bedingungen (`if/else`):** Zur Steuerung der Wendemanöver.

## 💻 Der Code

```python
# Hilfsfunktion für Rechtsdrehungen
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Logik für eine einzelne Bahn
def fahre_bis_wand():
    while front_is_clear():
        move()

# Hauptprogramm: Schlangenlinien-Logik
while front_is_clear() or not wall_on_left():
    # 1. Reihe nach rechts/vorne fahren
    fahre_bis_wand()
    
    # 2. Prüfen, ob eine Linkswende möglich ist
    if not wall_on_left():
        turn_left()
        if front_is_clear():
            move()
            turn_left()
            # 3. Reihe zurückfahren
            fahre_bis_wand()
            
            # 4. Rechtswende in die nächste Ebene
            if not wall_on_right():
                turn_right()
                if front_is_clear():
                    move()
                    turn_right()
    else:
        # Ziel erreicht (oberste Reihe)
        break
