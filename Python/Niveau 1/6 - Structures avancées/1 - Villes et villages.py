nombre_villes = int(input())

nombre_villes_valides = 0

for x in range(nombre_villes):
    nombre_habitants = int(input())
    if nombre_habitants > 10000:
        nombre_villes_valides += 1;
print(nombre_villes_valides)