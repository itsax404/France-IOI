nombre_mots = int(input())
première_langue = []
seconde_langue = []
dictionnaire = dict()

for x in range(nombre_mots):
    mot_première_langue, mot_deuxième_langue = input().split()
    seconde_langue.append(mot_deuxième_langue)
    première_langue.append(mot_première_langue)
    dictionnaire[mot_première_langue] = mot_deuxième_langue
  
première_langue.sort()

for x in range(nombre_mots):   
    print(première_langue[x], dictionnaire[première_langue[x]])
