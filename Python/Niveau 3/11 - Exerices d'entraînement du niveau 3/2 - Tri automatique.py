import sys


def main(input=sys.stdin.readline):
	nombre_bacs_batiment_a = int(input())
	liste_bacs_a = list(map(int, input().rstrip('\n').split(" ")))
	nombre_bacs_batiment_b = int(input())
	liste_bacs_b = list(map(int, input().rstrip('\n').split(" ")))

	for x in liste_bacs_b:
		liste_bacs_a.append(x)

	liste_rangée = sorted(liste_bacs_a)
	print(" ".join(str(x) for x in liste_rangée))


main()
