# Ampelprojekt.
# Ich habe die "Enum-Klasse" in dieser .py-Datei nicht verwendet.

import time  # Dieses Modul wird für die Blinkzeit der Leuchte benötigt


farben = ["ROT","GELB","GRÜN"] # Die Ampel wird in dieser Reihenfolge eingeschaltet


while True:  # Endlosschleife
    for farbe in farben:
        if farbe == "ROT":
            print("ROT")
            time.sleep(10)  # Warte 10 Sekunden!
        elif farbe == "GELB":
            print("GELB")
            time.sleep(1)  # Warte 1 Sekunden!
        elif farbe == "GRÜN":
            print("GRÜN")
            time.sleep(15)  # Warte 15 Sekunden!
