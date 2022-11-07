taxe_actuelle = float(input())
nouvelle_taxe = float(input())
prix_actuel = float(input())

prix_hors_taxe = prix_actuel/(1+(taxe_actuelle/100))

prix_avec_nouvelle_taxe = prix_hors_taxe*(1+(nouvelle_taxe/100))

prix_avec_nouvelle_taxe = round(prix_avec_nouvelle_taxe,2)

print(prix_avec_nouvelle_taxe)