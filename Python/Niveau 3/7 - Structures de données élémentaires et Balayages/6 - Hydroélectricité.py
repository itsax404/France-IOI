from sys import stdin, stdout

def main():

    longueur_centrale, longueur_rivière = map(int, stdin.readline().rstrip("\n").split(" "))

    liste_courant = list(map(int, stdin.readline().rstrip("\n").split(" ")))

    maximum = sum(liste_courant[x] for x in range(0,longueur_centrale))      

    somme = maximum

    for x in range(longueur_centrale, longueur_rivière):
        chiffre1 = liste_courant[x]
        chiffre2 = liste_courant[x-longueur_centrale]
        somme_1 = chiffre1 - chiffre2
        somme += somme_1
        if(somme > maximum):
            maximum = somme

    stdout.write(str(maximum))

main()   