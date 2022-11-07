heure_arrivée = int(input())
prix_chambre = 10
prix_total = 5 * heure_arrivée + prix_chambre

if(prix_total > 53):
    print(53)
else:
    print(prix_total)