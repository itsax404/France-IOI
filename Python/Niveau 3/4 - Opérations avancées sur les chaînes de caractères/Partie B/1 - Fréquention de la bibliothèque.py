somme_des_chiffres = 0

while True:
    try:
        entrée = list(map(int, input().split()))
        somme_des_chiffres += sum(entrée)
    except EOFError:
        break

print(somme_des_chiffres)
