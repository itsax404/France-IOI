def binaire(nombre):
	"""
	Convertir un entier en base 10 en binaire.
	Entrées:
		entier_base_10: int
	Sortie:
		binaire: str

	>>> binaire(5)
	'101'
	>>> binaire(25)
	'11001'
	>>> binaire(1245420)
	'100110000000011101100'
	"""
	liste_chiffre = []
	n = nombre
	while n > 1:
		liste_chiffre.insert(0, n % 2)
		n //= 2
	liste_chiffre.insert(0, n)
	if liste_chiffre[0] == 0:
		liste_chiffre.pop(0)
	return "".join([str(x) for x in liste_chiffre])

nombre = int(input())
lignes_multiplication = list()
for i in range(1, nombre +1):
	lignes_multiplication.append(" ".join([binaire(i*j) for j in range(1, nombre+1)]))
table = "\n".join(lignes_multiplication)
print(table)