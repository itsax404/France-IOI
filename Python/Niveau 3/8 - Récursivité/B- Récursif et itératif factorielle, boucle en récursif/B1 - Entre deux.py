def boucle_recursive(nombre: int, max: int) -> None:
	"""
	Permet d'afficher les nombres entre `nombre` et `max`
	Entrées:
		nombre: int
		max: int
	Sortie:
		None
	>>> boucle_recursive(1, 4)
	1 2 3 4
	>>> boucle_recursive(4, 7)
	4 5 6 7
	>>> boucle_recursive(1, 1)
	1
	"""
	print(nombre, end="")
	if nombre == max:
		print()
		return
	else:
		print(" ", end="")
		boucle_recursive(nombre + 1, max)

debut, fin = map(int, input().split())
boucle_recursive(debut, fin)
