quantité_liste = [0 for _ in range(10)]
nombre_opérations = int(input())
for loop in range(nombre_opérations):
    numéro = int(input())
    quantité = int(input())
    quantité_liste[numéro -1] += quantité
   
for n in range(10):
   print(quantité_liste[n])