phrase = input()
longueur_phrase = len(phrase)
liste_phrase = list(phrase)

for x in range(longueur_phrase):
   if liste_phrase[x] == " ":
      liste_phrase[x] = "_"
      
phrase = "".join(liste_phrase)
print(phrase)