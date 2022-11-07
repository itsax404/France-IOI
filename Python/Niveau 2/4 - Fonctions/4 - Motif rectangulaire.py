def motif(colonne, longueur, caractere):
   for loop in range(colonne):
      for loop in range(longueur):
         print(caractere, end = "")
      print()

motif( int(input()), int(input()), input())