date_début_fête = int(input())
date_fin_fête= int(input())
nombre_invités = int(input())
espion = 0
for loop in range(nombre_invités):
   date_entrée_invité = int(input())
   date_sortie_invité = int(input())
   if not ((date_fin_fête < date_entrée_invité) or (date_sortie_invité < date_début_fête)):
      espion = espion + 1
print(espion)