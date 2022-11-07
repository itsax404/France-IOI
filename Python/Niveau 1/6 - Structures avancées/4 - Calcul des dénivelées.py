nombre_variation = int(input())
nombre_montées = 0
nombre_descentes = 0

for x in range(nombre_variation):
    degres = int(input())
    if degres < 0:
        nombre_descentes += -degres
    else:
        nombre_montées += degres

print(nombre_montées)
print(nombre_descentes)