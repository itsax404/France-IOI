prix_au_kilo = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
poids_total = 0
for loop in range(10):
   poids_ingrédients = int(input())
   poids_total = poids_total + poids_ingrédients * (prix_au_kilo[loop])
print(poids_total)