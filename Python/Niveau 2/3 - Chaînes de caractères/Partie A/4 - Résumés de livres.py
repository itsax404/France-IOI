livres = int(input())
longueur_minimum = int(input())

for x in range(livres):
    titre = input()
    resume = input()
    if len(resume) < longueur_minimum:
        print(titre)