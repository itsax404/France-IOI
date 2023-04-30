def main():
	def deplacer(n: int, origine: int, destination: int, temporaire: int) -> None:
		"""
		Déplace n disques depuis l'origine jusqu'à destination en utilisant un espace temporaire
		"""
		if n == 0:
			return
		else:
			deplacer(n - 1, origine, temporaire, destination)
			print("{} -> {}".format(origine, destination))
			deplacer(n - 1, temporaire, destination, origine)

	nombre_disque = int(input())
	deplacer(nombre_disque, 1, 3, 2)


main()