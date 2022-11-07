nombre_produits = int(input())

stocks = list(map(int, input().split(" ")))

nombre_opérations = int(input())

for x in range(nombre_opérations):
    type_produit, quantité_produit = map(int, input().split(" "))
    stocks[type_produit-1] += quantité_produit


print(" ".join(str(x) for x in stocks))