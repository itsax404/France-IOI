from math import *
nombre_habitants = int(input())
fortune = [0]*nombre_habitants
for x in range(nombre_habitants):
   a = int(input())
   fortune[x]= a
fortune.sort()


if nombre_habitants % 2 == 1:
    milieu = (nombre_habitants-1)//2
    print(fortune[milieu])
else:
    milieu = nombre_habitants //2
    print( (fortune[milieu-1] + fortune[milieu])/2)