def min2(nombre1: int, nombre2: int) -> int: # Obligé de le nommer différemment que min() car sinon il y a une erreur
	"""
	Retourne le plus petit des deux nombres passés en paramètre.
	Entrées :
	    nombre1 : int
	    nomnbre2 : int
	Sortie :
		minimum : int
	"""
	return nombre1 if nombre1 < nombre2 else nombre2


nombre = int(input())
minimum = nombre
for loop in range(9):
	nombre = int(input())
	minimum = min2(minimum, nombre)

print(minimum)