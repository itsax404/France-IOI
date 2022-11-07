dé_1 = int(input())
dé_2 = int(input())

somme_dés = dé_1 + dé_2

if somme_dés >= 10:
    print("Taxe spéciale !")
    print(36)
else:
    print("Taxe régulière")
    print(somme_dés * 2)