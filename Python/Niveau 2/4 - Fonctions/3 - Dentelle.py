def motif(longueur):
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