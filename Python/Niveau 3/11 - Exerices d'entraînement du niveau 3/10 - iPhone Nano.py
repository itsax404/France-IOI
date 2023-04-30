nombre_mots = int(input())

liste_mots_par_longueur = [list() for _ in range(20)]

for x in range(nombre_mots):
    mot = input()
    liste_mots_par_longueur[len(mot)-1].append(mot)

longueur_mot = int(input())
liste_mots_valabes = liste_mots_par_longueur[longueur_mot-1]

for x in range(longueur_mot):
    liste_mots_temporaire = list()
    lettres = input()
    déja_vu = set()
    for lettre in lettres:
        for mot in liste_mots_valabes:
            lettre_a_tester = mot[x]
            if lettre_a_tester != lettre:
                pass
            else:
                if mot in déja_vu:
                    pass
                else:
                    liste_mots_temporaire.append(mot)
                    déja_vu.add(mot)
    liste_mots_valabes = liste_mots_temporaire

set_mot_valabes = set(liste_mots_valabes)

if len(liste_mots_valabes) == 1:
    print(liste_mots_valabes[0])
else:
    for mot in liste_mots_par_longueur[longueur_mot-1]:
        if mot in set_mot_valabes:
            print(mot)
            exit(0)