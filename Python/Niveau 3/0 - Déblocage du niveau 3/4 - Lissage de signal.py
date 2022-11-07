nombre_valeurs = int(input())
seuil = float(input())
valeurs = [float(input()) for loop in range(nombre_valeurs)]
temp = [0.0] * nombre_valeurs

def lisse():
   """
   Renvoie si la liste est lissé ou pas
   """
   for valeur in range(1,nombre_valeurs):
      if abs( valeurs[valeur] - valeurs[valeur-1] ) > seuil:
         return False
   return True
nbTours = 0

while not lisse():
   nbTours = nbTours + 1
   for valeur in range(1,nombre_valeurs - 1):
      temp[valeur] = (valeurs[valeur - 1] + valeurs[valeur + 1]) / 2
   for valeur in range(1,nombre_valeurs - 1):
      valeurs[valeur] = temp[valeur]
      
