nombre_charettes = int(input())
liste_poids = [0 for _ in range(nombre_charettes)]
poids_total = 0
for x in range(nombre_charettes):
    poids = float(input())
    poids_total += poids
    liste_poids[x] = poids

moyenne_poids = poids_total / nombre_charettes

for x in range(nombre_charettes):
   liste_poids[x] -= moyenne_poids

for x in range(nombre_charettes):
   print(liste_poids[x])