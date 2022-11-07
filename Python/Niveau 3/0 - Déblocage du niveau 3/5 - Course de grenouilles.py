nbGrenouilles = int(input())
nombre_tours = int(input())
positions = [0] * (nbGrenouilles + 1)
nombre_tours_en_tête = [0] * (nbGrenouilles + 1)
maximum = 0
 
for loop in range(nombre_tours - 1):
    grenouille,bond = map(int,input().split())
    positions[grenouille] += bond
    if positions[grenouille] > maximum:
        nombre_tours_en_tête[grenouille] += 1
        maximum = positions[grenouille]
        grenouille_en_tête = grenouille
    elif positions[grenouille] == maximum:
        grenouille_en_tête = 0
    nombre_tours_en_tête[grenouille_en_tête] += 1
 
nombre_tours_en_tête[0] = 0
grenouille_gagnante = 1
nombre_tours_gagnante = 0
for grenouille,nombre_tour in enumerate(nombre_tours_en_tête):
   if nombre_tours_gagnante < nombre_tour:
      nombre_tours_gagnante = nombre_tour
      grenouille_gagnante = grenouille
 
print(grenouille_gagnante)