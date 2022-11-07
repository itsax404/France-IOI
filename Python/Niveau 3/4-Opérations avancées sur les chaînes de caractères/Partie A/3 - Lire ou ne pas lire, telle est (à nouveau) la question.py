nombre_livres = int(input())

livre_précédent = ""
for x in range(nombre_livres):
    livre = input()
    if livre > livre_précédent:
        print(livre)
        livre_précédent = livre