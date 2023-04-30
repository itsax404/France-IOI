nombre_produits = int(input())
nombre_personnes = int(input())

liste_produits_aimés = [0 for _ in range(nombre_produits)]

for x in range(nombre_personnes):
    numéro_produit = int(input())
    liste_produits_aimés[numéro_produit] += 1
for x in range(nombre_produits):
   print(liste_produits_aimés[x])