def main():

    nombre_lignes, nombre_colonnes = map(int, input().split())

    infographie = []
   
    for x in range(nombre_colonnes):
        a = []
        for y in range(nombre_lignes):
            a.append(".")
        infographie.append(a)

    nombre_rectangles = int(input())

    for x in range(nombre_rectangles):
        entrée = input().split()
        ligne_min = int(entrée[0])
        colonne_min = int(entrée[1])
        ligne_max = int(entrée[2])
        colonne_max = int(entrée[3])
        symbole = entrée[4]
        for ligne in range(ligne_min, ligne_max+1):
            for colonne in range(colonne_min, colonne_max+1):
                infographie[colonne][ligne] = symbole

    for ligne in range(nombre_lignes):
        for colonne in range(nombre_colonnes):
            print(infographie[colonne][ligne], end="")
        print("")
main()