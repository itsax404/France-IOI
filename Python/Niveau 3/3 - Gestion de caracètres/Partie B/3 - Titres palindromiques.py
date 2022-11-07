nombre_livres = int(input())

for _ in range(nombre_livres):
    titre = input()
    titre_en_minuscule = titre.lower()
    titre_sans_espace = titre_en_minuscule.replace(" ", "")
    lettres_en_communs = 0
    for x in range(len(titre_sans_espace)//2):
        if titre_sans_espace[x] == titre_sans_espace[-(x+1)]:
            lettres_en_communs += 1
    if lettres_en_communs == len(titre)//2:
        print(titre)