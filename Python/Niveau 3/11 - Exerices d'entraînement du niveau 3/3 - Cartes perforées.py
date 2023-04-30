import sys


def main(input=sys.stdin.readline):
	liste_alphabet = [chr(x) for x in range(65, 91)]

	mot = ""

	nombre_ligne = int(input())
	for x in range(nombre_ligne):
		ligne = list(input().rstrip("\n"))
		for x in range(26):
			if ligne[x] == "O":
				mot += liste_alphabet[x]
	print(mot)


main()