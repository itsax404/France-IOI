nombre_lignes, nombre_mots = map(int, input().split(" "))
histogramme = [0] * 101
for loop in range(nombre_lignes):
   mots = input().split(" ")
   for index_mot in range(nombre_mots):
      longueur = len(mots[index_mot])
      histogramme[longueur] = histogramme[longueur] + 1
for longueur in range(101):
   if histogramme[longueur] > 0:
      print("{} : {}".format(longueur, histogramme[longueur]))