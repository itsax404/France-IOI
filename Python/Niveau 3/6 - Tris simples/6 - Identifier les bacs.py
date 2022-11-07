nombre_bacs = int(input())

id_bacs = []

dictionnaire_bacs = dict()

for x in range(nombre_bacs):
    identifiant_bac, pollution_bac = map(int, input().split())
    id_bacs.append(identifiant_bac)
    dictionnaire_bacs[identifiant_bac] = pollution_bac

liste_items_triés = sorted(dictionnaire_bacs.items(), key=lambda x: x[1])

for x in range(len(liste_items_triés)):
    if x == len(liste_items_triés)-1:
        break
    clé_x = liste_items_triés[x][0]
    valeur_x = liste_items_triés[x][1]
    clé_x_1 = liste_items_triés[x+1][0]
    valeur_x_1 = liste_items_triés[x+1][1]
    
    if valeur_x == valeur_x_1:
        if clé_x_1 < clé_x:
            temporaire = liste_items_triés[x]
            liste_items_triés[x] = liste_items_triés[x+1]
            liste_items_triés[x+1] = temporaire


for x in liste_items_triés:
    print(x[0], x[1])
