n = int(input())
nombres = set(map(int, input().split()))

déjà_vu = set()
nb_doublons = 0
for x in nombres:
    if -x in déjà_vu:
        nb_doublons += 1
    déjà_vu.add(x)

print(nb_doublons)
