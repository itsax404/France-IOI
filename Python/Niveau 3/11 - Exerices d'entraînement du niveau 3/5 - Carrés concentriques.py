import sys


def print(str="\n"):
	"""
	Permet d'afficher plus rapidement
	"""
	sys.stdout.write(str)


def plusieurs_symboles(symbole, nombre_symbole, nombre_apparitions, nombre_lettres):
	"""
	Permet d'afficher une ligne avec différents symboles
	"""
	for x in range(nombre_symbole):
		if x == nombre_symbole - 1:
			for _ in range(nombre_apparitions[nombre_lettres - (x + 1)]):
				print(symbole[x], end="")
		else:
			print(symbole[x], end="")
	if (nombre_symbole - 1) == 1:
		print(symbole[0], end="")
	else:
		for x in range((nombre_symbole - 2), -1, -1):
			print(symbole[x], end="")
	print()


def afficher_ligne(longueur, symbole, nombre_lettres, nombre_apparitions):
	"""
	Permet d'afficher une ligne, avec la longueur `longueur` et d'autres paramètres pour faire une ligne avec
	plusieurs symboles
	"""
	nombre_symbole = len(symbole)
	if nombre_symbole == 1:
		for _ in range(longueur):
			print(symbole[0], end="")
		print()
	else:
		plusieurs_symboles(symbole, nombre_symbole, nombre_apparitions, nombre_lettres)


def main(input=sys.stdin.readline):
	nombre_lettres = int(input())
	mot = input().rstrip("\n")
	liste_mot = list(mot)

	nombre_apparitions = list()
	t = 1
	for x in range(nombre_lettres):
		nombre_apparitions.append(t)
		t += 2

	liste_a_afficher = []

	for x in range(nombre_lettres):
		liste_a_afficher.append(liste_mot[(nombre_lettres - 1) - x])
		afficher_ligne(nombre_apparitions[nombre_lettres - 1], liste_a_afficher, nombre_lettres, nombre_apparitions)
	for x in range(nombre_lettres):
		liste_a_afficher.pop()
		afficher_ligne(nombre_apparitions[nombre_lettres - 1], liste_a_afficher, nombre_lettres, nombre_apparitions)


main()