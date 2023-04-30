joueur1 = input()
joueur2 = input()
egalite = 0
minimum_cartes = min(len(joueur1), len(joueur2))
vainqueur = "?"

for x in range(minimum_cartes):
	if joueur1[x] == joueur2[x]:
		egalite = egalite + 1

	elif joueur1[x] < joueur2[x]:
		vainqueur = "1"
		break

	elif joueur2[x] < joueur1[x]:
		vainqueur = "2"
		break

if vainqueur == "?":
	if egalite < len(joueur1):
		vainqueur = "1"
	elif egalite < len(joueur2):
		vainqueur = "2"
	else:
		vainqueur = "="

print(vainqueur)
print(egalite)