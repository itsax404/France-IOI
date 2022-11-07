lettre_recherche = input()
nombre_ligne = int(input())
nombre_lettre = 0
for x in range(nombre_ligne):
   phrase = input()
   longueur_phrase = len(phrase)
   for y in range(longueur_phrase):
      if phrase[y] == lettre_recherche:
         nombre_lettre += 1
         
print(nombre_lettre)