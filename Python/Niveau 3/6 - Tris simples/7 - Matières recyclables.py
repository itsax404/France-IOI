nombre_matières = int(input())

liste_matières = []

for x in range(nombre_matières):
    liste_matières.append(input())

liste_matières_triées = sorted(liste_matières)

for x in liste_matières_triées:
    print(x)