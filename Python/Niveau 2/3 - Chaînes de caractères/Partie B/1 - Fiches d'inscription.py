nombre_personnes = int(input())

for x in range(nombre_personnes):
    ligne = input()
    mots = ligne.split(" ")
    print(f"{mots[1]} {mots[0]}")
