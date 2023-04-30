def motif(longueur):
   """
   Affiche un motif de longueur donnée
   Entrée : longueur, un entier
   """
   for loop in range(longueur):
      print("X", end = "")
   print()
   for loop in range(longueur):
      print("#", end = "")
   print()
   for loop in range(longueur):   
      print("i", end = "")
   print()
   
motif(int(input()))