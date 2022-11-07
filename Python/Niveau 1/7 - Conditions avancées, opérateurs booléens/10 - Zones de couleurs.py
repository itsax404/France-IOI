nombre_jetons = int(input())

for _ in range(nombre_jetons):
    x = int(input())
    y = int(input())

    estDansLaFeuille = (((0 <= x) and (x <= 90)) and ((0 <= y) and (y <= 70)))
    estDaneZone1Rouge = (((60 <= y) and (y <= 70)) and ((15 <= x) and (x <= 45)))
    estDaneZone2Rouge = (((60 <= y) and (y <= 70)) and ((60 <= x) and (x <= 85)))
    estDansZoneRouge = (estDaneZone1Rouge and estDaneZone2Rouge)

    estDaneZone1Bleue = (((10 <= y) and (y <= 20)) and ((10 <= x) and (x <= 85)))
    estDaneZone2Bleue = (((20 <= y) and (y <= 45)) and ((10 <= x) and (x <= 25)))
    estDaneZone3Bleue = (((20 <= y) and (y <= 45)) and ((50 <= x) and (x <= 85)))
    estDaneZone4Bleue = (((45 <= y) and (y <= 55)) and ((10 <= x) and (x <= 85)))
    estDansZoneBleue = (estDaneZone1Bleue  or estDaneZone2Bleue  or estDaneZone3Bleue  or estDaneZone4Bleue)

    if not estDansLaFeuille:
        print("En dehors de la feuille")
    elif estDansZoneRouge:
        print("Dans une zone rouge")
    elif estDansZoneBleue:
        print("Dans une zone bleue")
    else:
        print("Dans une zone jaune")