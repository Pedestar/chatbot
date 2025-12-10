import json
def lade_daten(datei):
with open(datei, encoding="utf8") as f:
return json.load(f)
def zeige_anzahl_gespraeche(daten):
print(len(daten))
daten = lade_daten("data/conversations.json")
zeige_anzahl_gespraeche(daten)
