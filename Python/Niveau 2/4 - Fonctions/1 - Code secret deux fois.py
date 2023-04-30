def check4242() -> None:
	"""
	Permet de faire un code et vérifier si le code est 4242.
	"""
	while True:
		print("Entrez le code :")
		essai = int(input())
		if essai == 4242:
			return


check4242()
print("Encore une fois.")
check4242()
print("Bravo.")