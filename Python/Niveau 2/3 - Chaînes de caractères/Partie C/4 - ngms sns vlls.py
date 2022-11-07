titre = input()
auteur = input()
titre_sans_voyelles = ''.join([k for k in titre if k not in [" ", 'A', 'E', 'I', 'O', 'U', 'Y'] ])
auteur_sans_voyelles = ''.join([k for k in auteur if k not in [" ", 'A', 'E', 'I', 'O', 'U', 'Y'] ])

print(titre_sans_voyelles)
print(auteur_sans_voyelles)