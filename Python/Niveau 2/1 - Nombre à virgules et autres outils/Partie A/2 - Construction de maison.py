from math import ceil

quantité_ciment = float(input())

nombre_sacs_nécessaire = ceil(quantité_ciment/60)

prix = nombre_sacs_nécessaire *45

print(prix)