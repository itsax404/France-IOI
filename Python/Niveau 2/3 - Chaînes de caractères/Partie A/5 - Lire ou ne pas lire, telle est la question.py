nombre_livre = int(input())
plus_grand_titre = ""

for x in range(nombre_livre):
   titre = input()
   if titre > plus_grand_titre:
      plus_grand_titre = titre
      print(titre)