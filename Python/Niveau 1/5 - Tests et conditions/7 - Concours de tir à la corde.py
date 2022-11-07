nombre_participants = int(input())

poids_total_équipe1 = 0
poids_total_équipe2 = 0

for x in range(nombre_participants):
    poids_membre1 = int(input())
    poids_membre2 = int(input())
    poids_total_équipe1 += poids_membre1
    poids_total_équipe2 += poids_membre2

if poids_total_équipe1 < poids_total_équipe2:
    print("L'équipe 2 a un avantage")
else:
    print("L'équipe 1 a un avantage")
print("Poids total pour l'équipe 1 :", poids_total_équipe1)
print("Poids total pour l'équipe 2 :", poids_total_équipe2)