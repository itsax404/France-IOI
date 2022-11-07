def min2(nombre1, nombre2):
   if nombre1 < nombre2:
      return nombre1
   else:
      return nombre2


nombre = int(input())
minimum = nombre
for loop in range(9):
    nombre = int(input())
    minimum = min2(minimum, nombre)

print(minimum)