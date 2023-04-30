def séparer_entrée(valeur: str) -> tuple:
	"""
	Sépare la valeur en deux parties, la première étant un nombre flottant et la seconde étant une unité de mesure.
	:param valeur: La valeur à séparer.
	:return: Un tuple contenant le nombre flottant et l'unité de mesure.
	"""
	valeur_flottant = float(valeur[:-1])
	return (valeur_flottant, valeur[len(valeur) - 1])


nombre_conversions = int(input())

for loop in range(nombre_conversions):
	valeur = input()
	quantité, unité = séparer_entrée(valeur)
	if unité == "m":
		quantité /= 0.3048
		print(round(quantité, 6), "p")
	elif unité == "g":
		quantité *= 0.002205
		print(round(quantité, 6), "l")
	else:
		quantité = quantité * 1.8 + 32
		print(round(quantité, 6), "f")
