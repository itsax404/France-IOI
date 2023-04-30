def encadrer(nombre: str, nombre_fois: int):
	"""
	Permet d'encadrer le nombre avec des crocrets par récursitivité.
	Entrée:
	    nombre: str
	    nombre_fois: int

	>>> encadrer("26", 0)
	'26'
	>>> encadrer("43", 4)
	'[[[[43]]]]'
	>>> encadrer("458", 15)
	'[[[[[[[[[[[[[[[458]]]]]]]]]]]]]]]'
	"""
	if nombre_fois == 0:
		return nombre
	else:
		return "[" + encadrer(nombre, nombre_fois-1) + "]"

def main():
	nombre, nombre_fois = map(int, input().split())
	print(encadrer(str(nombre), nombre_fois))

main()