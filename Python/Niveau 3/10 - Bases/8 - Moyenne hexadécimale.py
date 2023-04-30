import sys


def main(input=sys.stdin.readline):
	dictionnaire_conversions_hexadecimal = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
	                                        "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
	dictionnaire_conversions_decimal = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
	                                    10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

	def hexadecimal_vers_decimal(str_hexadecimal: str) -> int:
		"""
		Permet de convertir un nombre en base 16 en un entier en
		base 10
		>>> hexadecimal_vers_decimal(64)
		100
		>>> hexadecimal_vers_decimal(aa026)
		696358
		"""
		nombre_hexadecimal = list(str_hexadecimal)
		nombre_decimal = 0
		for x in range(len(nombre_hexadecimal)):
			valeur_decimale = dictionnaire_conversions_hexadecimal[nombre_hexadecimal[x]]
			nombre_decimal += valeur_decimale * (16 ** ((len(nombre_hexadecimal) - 1) - x))
		return nombre_decimal

	def decimal_vers_hexadecimal(nombre_decimal: int) -> str:
		"""
		Permet de convertir un nombre en base 10 en un entier en
		base 16
		>>> decimal_vers_hexadecimal(64)
		40
		>>> hexadecimal_vers_decimal(15026)
		696358
		"""
		liste_hexa = []
		n = nombre_decimal
		while n > 1:
			liste_hexa.insert(0, dictionnaire_conversions_decimal[n % 16])
			n //= 16
		liste_hexa.insert(0, dictionnaire_conversions_decimal[n])
		if liste_hexa[0] == "0":
			liste_hexa.pop(0)
		return "".join(x for x in liste_hexa)

	nombre_valeurs = hexadecimal_vers_decimal((input().rstrip("\n")))

	somme = 0
	for x in range(nombre_valeurs):
		valeur_hexadecimal = input().rstrip("\n")
		valeur_decimale = hexadecimal_vers_decimal(valeur_hexadecimal)
		somme += valeur_decimale
	moyenne = int(somme / nombre_valeurs)
	print(decimal_vers_hexadecimal(moyenne))


main()
