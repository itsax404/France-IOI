inversion = [0, 2, 1, 3, 5, 4]
nombre_déplacements = int(input())

liste_déplacements = [0]*nombre_déplacements

for x in range(nombre_déplacements):
   liste_déplacements[x] = inversion[ int(input()) ]
      
for y in liste_déplacements[::-1]:
   print(y)