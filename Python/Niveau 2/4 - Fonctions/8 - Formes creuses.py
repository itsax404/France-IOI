def croix(nombre1: int) -> None:
	"""
	Permet d'afficher une ligne de "X" de la longueur du nombre entré
	:param nombre1: int
	:return: None
	"""
	for loop in range(nombre1):
		print("X", end="")
	print()


def rectangle(longueur: int, largeur: int) -> None:
	"""
	Permet d'afficher un rectangle de "#" de la longueur et largeur entrées
	:param longueur: int
	:param largeur: int
	:return: None
	"""
	if longueur == 1:
		for x in range(largeur):
			print("#")
	else:
		for loop in range(longueur - 1):
			print("#", end="")
		print("#")
		for loop in range(largeur - 2):
			print("#", end="")
			for loop in range(longueur - 2):
				print(" ", end="")
			print("#")
		for loop in range(longueur):
			print("#", end="")
		print()


def triangle(hauteur: int) -> None:
	"""
	Permet d'afficher un triangle de "*" de la hauteur entrée
	:param hauteur: int
	:return: None
	"""
	print("@")
	for x in range(hauteur - 2):
		print("@", end="")
		for _ in range(x):
			print(" ", end="")
		print("@")
	for loop in range(hauteur):
		print("@", end="")


nombre_croix = int(input())
nombre_rectangle_ligne = int(input())
nombre_rectangle_colonne = int(input())
nombre_triangle = int(input())

croix(nombre_croix)
print()
rectangle(nombre_rectangle_colonne, nombre_rectangle_ligne)
print()
triangle(nombre_triangle)