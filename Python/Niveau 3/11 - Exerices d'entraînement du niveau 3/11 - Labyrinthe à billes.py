dictionnaire_vecteurs = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}
nombre_lignes, nombre_colonnes = map(int, input().split(" "))
plateau = []
liste_pions = list()
nombre_pions = 0

for ligne in range(nombre_lignes):
	liste_input = list(input())
	plateau.append(liste_input)
	for colonne in range(nombre_colonnes):
		if liste_input[colonne] == "x":
			liste_pions.append((ligne, colonne))
			nombre_pions += 1

nombre_deplacements = int(input())
liste_déplacements = list(input())
if len(liste_déplacements) != nombre_deplacements:
	raise ValueError(str(liste_déplacements))


def est_déplaçable(ligne, colonne):
	"""
	Renvoie True si l'élément situé aux coordonnées (ligne, colonne)
	est un élément où la bille peut se déplacer (un espace vide ou un trou)
	Si l'élément se déplace un mur ou une autre bille, cela renvoie False
	"""
	if ligne < 0 or ligne >= nombre_lignes:
		return False
	elif colonne < 0 or colonne >= nombre_colonnes:
		return False
	elif plateau[ligne][colonne] == "#" or plateau[ligne][colonne] == "x":
		return False
	else:
		return True


def déplacer_élément(ligne, colonne, nvlle_ligne, nvlle_colonne, est_un_trou=False):
	"""
	Permet de déplacer l'élément situé aux coordonnées (ligne, colonne) aux
	coordonnées (nvlle_ligne, nvlle_colonne)
	"""
	if not est_un_trou:
		plateau[ligne][colonne] = "."
		plateau[nvlle_ligne][nvlle_colonne] = "x"
	else:
		plateau[ligne][colonne] = "."


def déplacer(liste_billes, orientation):
	"""
	Permet faire de déplacer le pion (id_pion) dans l'orientation
	donnée jusqu'à se fasse arrêter par un mur, une autre bille ou
	qu'elle tombe dans un trou
	"""
	ordre_billes = donne_ordre_bille(orientation, liste_billes)
	for i in range(len(ordre_billes)):
		x, y = ordre_billes[i]
		delta_x, delta_y = dictionnaire_vecteurs[orientation]
		while est_déplaçable(x + delta_x, y + delta_y):
			if plateau[x + delta_x][y + delta_y] == "O":
				déplacer_élément(x, y, x + delta_x, y + delta_y, True)
				ordre_billes[i] = None
				break
			else:
				déplacer_élément(x, y, x + delta_x, y + delta_y)
				x += delta_x
				y += delta_y
				ordre_billes[i] = (x, y)
	return [x for x in ordre_billes if x != None]


def donne_ordre_bille(direction, liste_billes):
	"""
	Renvoie une liste de billes où elles sont rangées selon
	le sens auquelle les billes doivent se déplacer
	"""
	if direction == "N" or direction == "S":
		tri = lambda p: (p[0], p[1])
		return sorted(liste_billes, key=tri, reverse=direction == "S")
	elif direction == "O" or direction == "E":
		tri = lambda p: (p[1], p[0])
		return sorted(liste_billes, key=tri, reverse=direction == "E")
	else:
		print(direction)
		raise ValueError(str(direction))
		return liste_billes


for i in range(nombre_deplacements):
	orientation = liste_déplacements[i]
	liste_pions = déplacer(liste_pions, orientation)
# for orientation in liste_déplacements:
#    liste_pions = déplacer(liste_pions, orientation)

print(len(liste_pions))