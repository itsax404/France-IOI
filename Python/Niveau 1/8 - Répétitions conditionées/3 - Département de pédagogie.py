nombre_essais = 1
nombre_a_trouver = int(input())

while True:
   essai = int(input())
   if essai < nombre_a_trouver:
      print("c'est plus")
      nombre_essais += 1
   elif essai < nombre_a_trouver:
      print("c'est moins")
      nombre_essais += 1
   else:
      break

print("Nombre d'essais nécessaires :")
print(nombre_essais)
