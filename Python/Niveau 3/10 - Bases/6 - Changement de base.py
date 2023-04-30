base_depart, base_arrivee, nombre_chiffre = map(int, input().split())
chiffres = list(reversed(list(map(int, input().split()))))


def convertir_chiffre_decimal(liste_chiffres, base_depart: int) -> int:
	"""
	Permet de convertir la liste de chiffres `liste_chiffres`, dans la base `base_depart` en entier dans la base 10
	Entrées:
		liste_chiffres: list[int]
		base_depart: int
	Sortie:
		entier_base_10: int
	>>> convertir_chiffre_decimal([4, 5, 3, 2, 1], 7)
	3273
	>>> convertir_chiffre_decimal([7, 7, 3, 4, 0, 3, 7], 8)
	1935615
	>>> convertir_chiffre_decimal([9, 5, 7], 14)
	1451
	>>> convertir_chiffre_decimal([3, 16, 5, 13], 17)
	65589
	"""
	nombre = 0
	for i in range(len(liste_chiffres)):
		nombre += liste_chiffres[i] * (base_depart ** i)
	return nombre


chiffre_depart = convertir_chiffre_decimal(chiffres, base_depart)

def convertir_base_arrivée(entier_base_10: int, base_arrivée: int):
	"""
	Convertir un entier en base 10 dans la base `base_arrivée`.
	Entrées:
		entier_base_10: int
		base_arrivée: int
	Sortie:
		liste_chiffres: list[str]
	>>> convertir_base_arrivée(120, 3)
	['1', '1', '1', '1', '0']
	>>> convertir_base_arrivée(95742, 19)
	['13', '18', '4', '1']
	"""
	if base_arrivée == 10:
		liste_chiffre = list(str(entier_base_10))
		return [x for x in liste_chiffre]

	liste_chiffre = []
	n = entier_base_10
	while n > 1:
		liste_chiffre.insert(0, n % base_arrivée)
		n //= base_arrivée
	liste_chiffre.insert(0, n)
	if liste_chiffre[0] == 0:
		liste_chiffre.pop(0)
	return [str(x) for x in liste_chiffre]

entier_base_arrivée = convertir_base_arrivée(chiffre_depart, base_arrivee)
print(" ".join(entier_base_arrivée))
