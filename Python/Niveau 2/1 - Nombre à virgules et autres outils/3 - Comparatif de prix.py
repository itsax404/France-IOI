nombre_légumes = int(input())
for i in range(nombre_légumes):
   poids = float(input())
   age = float(input())
   prix = float(input())
   prix_au_kilo = prix/poids
   print(prix_au_kilo)