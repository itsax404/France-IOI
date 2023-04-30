nombre_livres, nombre_jours = map(int, input().split())
temps_restants_livres = [0 for _ in range(nombre_livres)]
id_livre = 0

for loop in range(nombre_livres):
	temps_restants_livres[id_livre] = 0
	id_livre += 1

for loop in range(nombre_jours):
	nombre_clients = int(input())
	for loop in range(nombre_clients):
		livre, temps = map(int, input().split())
		if (temps_restants_livres[livre] <= 0):
			temps_restants_livres[livre] = temps
			print(1)
		else:
			print(0)
	id_livre = 0
	for loop in range(nombre_livres):
		temps_restants_livres[id_livre] -= 1
		id_livre += 1
