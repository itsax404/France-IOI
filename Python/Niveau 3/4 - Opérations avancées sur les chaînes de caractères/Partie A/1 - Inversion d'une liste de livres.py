nombre_livres = int(input())
livres = []

for x in range(nombre_livres):
    livres.append(input())

livres.reverse()

for x in range(nombre_livres):
    print(livres[x])