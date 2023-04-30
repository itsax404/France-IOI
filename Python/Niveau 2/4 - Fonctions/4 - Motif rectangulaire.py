def motif(colonne, longueur, caractere):
	"""
	Entrées :
		colonne : int
		longueur : int
		caractere : str
	Sortie :
		Affiche un motif rectangulaire de colonne * longueur caractere
	"""
	for x in range(colonne):
		for y in range(longueur):
			print(caractere, end="")
		print()

colonne = int(input("Entrez le nombre de colonnes : \n"))
longueur = int(input("Entrez le nombre de lignes : \n"))
caractere = input("Entrez le caractère : \n")
motif(colonne, longueur, caractere)