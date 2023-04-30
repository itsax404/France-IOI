import sys


def main(input=sys.stdin.readline):
	hauteur, largeur, distance = map(int, input().split(" "))
	données = []
	for x in range(hauteur):
		données.append(list(map(int, input().split(" "))))

	def marquer(hauteur, largeur):
		"""
		Permet de marquer l'endroit où on est passé
		aux coordonneés "x" et "y"
		"""
		données[hauteur][largeur] = 2

	def peut_se_déplacer(x, y):
		"""
		Permet de renvoyer un booléen si on peut se déplacer aux coordonnées
		("x", "y").
		"""
		return données[x][y] == 0

	def déplacer(x, y, précédent_x, précédent_y) -> tuple:
		"""
		Permet de se déplacer jusqu'au prochain point
		"""
		vecteur_x = x - précédent_x
		vecteur_y = y - précédent_y

		if vecteur_x != 0:

			x += vecteur_x
			if 0 <= x < hauteur:
				if peut_se_déplacer(x, y):
					marquer(x, y)
					return (x, y)
			x -= vecteur_x
			y += 1
			if y < largeur:
				if peut_se_déplacer(x, y):
					marquer(x, y)
					return (x, y)
			y -= 2
			if y >= 0:
				if peut_se_déplacer(x, y):
					marquer(x, y)
					return (x, y)

		else:

			y += vecteur_y
			if 0 <= y < largeur:
				if peut_se_déplacer(x, y):
					marquer(x, y)
					return (x, y)
			y -= vecteur_y
			x += 1
			if x < hauteur:
				if peut_se_déplacer(x, y):
					marquer(x, y)
					return (x, y)
			x -= 2
			if x >= 0:
				if peut_se_déplacer(x, y):
					marquer(x, y)
					return (x, y)

	def afficher() -> str:
		"""
		Permet d'afficher la carte
		"""
		carte_str = "[Début de la carte]\n"
		for x in range(hauteur):
			for y in range(largeur):
				carte_str += "|" + str(données[x][y]) + "|"
			carte_str += "\n"
		carte_str += "[Fin de la carte]"
		return carte_str

	précédent_x = 0
	précédent_y = -1
	x = 0
	y = 0
	déplacement = 0

	while not ((y == largeur - 1) and (x == hauteur - 1)):
		nouveau_x, nouveau_y = déplacer(x, y, précédent_x, précédent_y)
		précédent_x = x
		précédent_y = y
		y = nouveau_y
		x = nouveau_x
		if not déplacement == distance:
			déplacement += 1
		else:
			print(précédent_x, précédent_y)
			déplacement = 0
	if déplacement == distance:
		print(x, y)


main()