import sys

base_départ, nombre_chiffre = map(int, sys.stdin.readline().rstrip("\n").split(" "))

nombre = 1

for x in range(nombre_chiffre-1):
    nombre *= base_départ

liste_entiers = list(map(int, sys.stdin.readline().rstrip("\n").split(" ")))

réponse = 0

for x in range(nombre_chiffre):
    entier = liste_entiers[x]
    réponse += nombre * entier
    nombre //= base_départ
sys.stdout.write(str(réponse))
