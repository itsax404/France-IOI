nombre_pierres_max = int(input())
hauteur = 0
nombre_pierres_nécessaire = 0
while (nombre_pierres_nécessaire + (hauteur+1)*(hauteur+1)) <= nbPierresMax:
   hauteur = hauteur + 1
   nombre_pierres_nécessaire += (hauteur*hauteur)

print(hauteur)
print(nombre_pierres_nécessaire)