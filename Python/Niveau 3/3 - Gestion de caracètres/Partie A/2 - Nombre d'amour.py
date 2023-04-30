prénoms = input().split("")
nombres_amour = [0]*2

def calcul_nombre_d_amour(prénom: str) -> int:
    """
    Permet de calculer le nombre d'amour à partir du prénom
    et renvoie le `nombre_amour` correspond au prénom
    >>> calcul_nombre_d_amour("ADA")
    3
    >>> calcul_nombre_d_amour("GWOAG")
    3
    """
    nombre_amour = 0
    for caractère in prénom:
        nombre_amour += (ord(caractère) - ord("A"))
    
    while(nombre_amour >= 10):
        somme_chiffre = 0
        while nombre_amour > 0:
            somme_chiffre += nombre_amour %10
            nombre_amour //= 10
        nombre_amour = somme_chiffre
    return nombre_amour

for x in range(2):
    prénom = prénoms[x]
    nombres_amour[x] = calcul_nombre_d_amour(prénom)

print(f"{nombres_amour[0]} {nombres_amour[1]}")