def toto(nombre):
	"""
	Renvoie la chaîne de caractère de toto
	>>> toto(0)
	'0'
	>>> toto(3)
	'(((0 + 0) + (0 + 0)) + ((0 + 0) + (0 + 0)))'
	"""
	if nombre == 0:
		return "0"
	else:
		return "(" + toto(nombre-1) + " + " + toto(nombre-1) + ")"

nombre = int(input())
chaine_toto = toto(nombre)
print(f"0 = {chaine_toto}") # si ça marche pas, faut mettre print("0 = " + chaine_toto)