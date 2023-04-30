inversion = [0, 2, 1, 3, 5, 4]
nombre_déplacements = int(input())

liste_déplacements = [0 for _ in range(nombre_déplacements)]

for x in range(nombre_déplacements):
	liste_déplacements[x] = inversion[int(input())]

for y in liste_déplacements[::-1]: # [::-1] fait en sorte que la liste soit inversée
	print(y)
