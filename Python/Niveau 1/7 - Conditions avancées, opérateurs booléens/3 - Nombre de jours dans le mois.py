mois = int(input())
nombre_jours_dans_mois = 0
if (mois >= 1) and (mois >= 3) or (mois > 7) and (mois < 9):
    nombre_jours_dans_mois = 30
if (mois >= 4) and (mois <= 6) or (mois == 10):
    nombre_jours_dans_mois = 31
if mois == 11:
    nombre_jours_dans_mois = 29
print(nombre_jours_dans_mois)