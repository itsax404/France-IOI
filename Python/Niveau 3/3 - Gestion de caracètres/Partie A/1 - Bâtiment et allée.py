nom_auteur = input()
âge_fils = int(input())

chiffre_batiment = -(64 - ord(nom_auteur[0]))
lettre_allée = chr(64 + âge_fils)

print(str(chiffre_batiment) + lettre_allée)