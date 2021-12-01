# Ampel Projekt
# Ich habe "Enum-Klasse" in dieser Datei für das Ampelprojekt verwendet.

from enum import Enum, auto # Die Auto-Funktion vergibt die Nummerierung selbst.Aber hier werde ich die Zahlen selbst einstellen
import time



class Ampel(Enum):
    ROT = 10 # Damit das rote Licht 10 Sekunden lang aufleuchtet
    GELB = 1 # Damit das gelbe Licht 1 Sekunden lang aufleuchtet
    GRUN = 15 #Damit das grüne Licht 15 Sekunden lang aufleuchtet

while True:
    for farben in Ampel:
        if farben == Ampel.ROT:
            print(farben.name)
            time.sleep(farben.value)
        elif farben == Ampel.GELB:
            print(farben.name)
            time.sleep(farben.value)
        elif farben == Ampel.GRUN:
            print(farben.name)
            time.sleep(farben.value)
