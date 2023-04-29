mot_a_trouver = input()
phrase = input().lower()

mots = phrase.split(" ")

somme_tics = 0

for mot in mots:
    if mot_a_trouver == mot:
        somme_tics += 1 

print(somme_tics)