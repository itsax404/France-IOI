nombre_lettres = int(input())
taille_cadre = 2*nombre_lettres -1

def lettre(nombre_lignes, nombre_colonnes):
    nombre_lignes = min(nombre_lignes, taille_cadre - 1 -nombre_lignes)
    nombre_colonnes = min(nombre_colonnes, taille_cadre - 1 - nombre_colonnes)
    return chr(ord('a') + min(nombre_lignes, nombre_colonnes))
   
nombre_lignes = 0
for x in range(taille_cadre):
    nombre_colonnes = 0
    for y in range(taille_cadre):
        print(lettre(nombre_lignes, nombre_colonnes), end = "")
        nombre_colonnes += 1
    nombre_lignes += 1 
    print("")