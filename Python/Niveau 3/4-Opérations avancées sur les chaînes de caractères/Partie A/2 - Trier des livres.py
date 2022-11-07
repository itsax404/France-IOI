nombre_livres = int(input())
livres = []

for x in range(nombre_livres):
    livres.append(input())

livres.sort()

for x in range(nombre_livres):
    print(livres[x])