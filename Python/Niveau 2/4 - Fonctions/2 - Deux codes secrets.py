def deux_codes():
   while True:
      print("Entrez le code :")      
      essai = int(input())
      if essai == 4242:
         print("Premier code bon.")
      elif essai == 2121:
         print("Bravo.")
         return
deux_codes()