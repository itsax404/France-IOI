nombre_karva = int(input())

for x in range(nombre_karva):
  poids_karva = int(input())
  age_karva = int(input())
  longueur_cornes_karva = int(input())
  hauteur_garrot_karva = int(input())
  note = longueur_cornes_karva * hauteur_garrot_karva + poids_karva
  print(note)