def main():

    nombre_bacs = int(input())
    liste_bacs = list(map(int, input().split()))

    liste_bacs_rangés = sorted(liste_bacs)

    for x in liste_bacs_rangés:
        print(x, end=" ")

main()