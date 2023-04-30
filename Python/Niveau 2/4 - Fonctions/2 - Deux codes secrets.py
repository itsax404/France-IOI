def deux_codes() -> None:
	"""
	Entrée : Deux codes secrets.
	Sortie : Affiche "Premier code bon." si le premier code est bon, "Bravo." si le deuxième code est bon.
	"""
	while True:
		print("Entrez le code :")
		essai = int(input())
		if essai == 4242:
			print("Premier code bon.")
		elif essai == 2121:
			print("Bravo.")
			return
deux_codes()