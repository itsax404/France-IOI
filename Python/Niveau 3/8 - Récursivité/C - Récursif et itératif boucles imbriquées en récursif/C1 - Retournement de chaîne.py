def retourne(chaine: str, indice: int) -> None:
	"""
	Permet de retourner la chaîne de caractère `chaine`
	Entrées:
		chaine: str
		indice: int
	Sortie:
		None
	"""
	print(chaine[-indice], end="")
	if indice == (len(chaine)):
		return
	else:
		retourne(chaine, indice+1)

chaine = input()
retourne(chaine, 1)