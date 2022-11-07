nombre_livre = int(input())
longueur_titre2 = 0
for x in range(nombre_livre):
   titre = input()
   ltitre = len(titre)
   if ltitre > longueur_titre2:
      ltitre2 = ltitre
      print(titre)