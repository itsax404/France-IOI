x_min = int(input())
x_max = int(input())
y_min = int(input())
y_max = int(input())
nombre_maisons = int(input())
nombre_maisons_suspectes = 0
for _ in range(nombre_maisons):
    x = int(input())
    y = int(input())
    if (x >= x_min)and (x <= x_max) and (y >= y_min) and (y <=y_max):
        nombre_maisons_suspectes += 1
print(nombre_maisons_suspectes)