date_début= int(input())
date_fin = int(input())
nombre_entrées = int(input())
personnes_suspectes = 0
for x in range(nombre_entrées):
    jour_entrée_suspect = int(input())
    if (jour_entrée_suspect >= date_début) and (jour_entrée_suspect <= date_fin):
        personnes_suspectes += 1
print(personnes_suspectes)