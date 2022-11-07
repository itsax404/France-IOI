position_départ = int(input())
largeur_emplacement = int(input())
nombre_vendeurs = int(input())

print(position_départ)
for _ in range(nombre_vendeurs):
    position_départ += largeur_emplacement
    print(position_départ)