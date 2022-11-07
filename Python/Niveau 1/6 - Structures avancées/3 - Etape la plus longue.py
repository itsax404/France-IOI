nombre_jours = int(input())
distance_maximale = 0

for x in range(nombre_jours):
  distance_jour = int(input())
  if distance_jour > distance_maximale:
    distance_maximale = distance_jour
print(distance_maximale)