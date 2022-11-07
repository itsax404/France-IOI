def croix(nombre1):
    for loop in range(nombre1):
        print("X", end = "")
    print()
def rectangle(longueur, largeur):
    if longueur == 1 :
        for x in range(largeur):
            print("#")
    else:
        for loop in range(longueur-1):
            print("#", end = "")
        print("#")
        for loop in range(largeur-2):
            print("#", end = "")
            for loop in range(longueur-2):
                print(" ",end = "")
            print("#")
        for loop in range(longueur):
            print("#", end = "")
        print()
def triangle(hauteur):
    print("@")
    for x in range(hauteur - 2):
        print("@", end="")
        for _ in range(x):
            print(" ", end="")
        print("@")
    for loop in range(hauteur):
        print("@", end = "")

nombre = int(input())
croix(nombre)