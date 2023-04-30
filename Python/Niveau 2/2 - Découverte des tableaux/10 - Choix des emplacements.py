nombre_emplacements = int(input())
emplacements = [0 for _ in range(nombre_emplacements)]

for x in range(nombre_emplacements):
   emplacement_actuel = int(input())
   emplacements[emplacement_actuel] = x
   
for y in range(nombre_emplacements):
   print(emplacements[y])