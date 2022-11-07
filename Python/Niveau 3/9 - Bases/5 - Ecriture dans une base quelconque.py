from sys import stdin, stdout
import sys

def afficher(liste):
    """
    a
    """
    print(len(liste))
    print(" ".join(str(x) for x in liste))
    exit(0)

entier_a_convertir, base_arrivée = map(int, stdin.readline().rstrip("\n").split(" "))

if entier_a_convertir == 0:
    afficher([0])

quotient = entier_a_convertir

reste = 0

liste_entiers = []

while True:
    if quotient >= base_arrivée:
        a, b = divmod(quotient, base_arrivée) 
        quotient = a
        liste_entiers.append(a)
    else:
        liste_entiers.append(reste)
        afficher(liste_entiers)
