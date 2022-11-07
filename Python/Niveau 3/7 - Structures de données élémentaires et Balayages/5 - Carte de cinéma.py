import sys

def main():
    
    liste_cartes = [0 for _ in range(1000000)]

    nombre_cartes = int(sys.stdin.readline().rstrip("\n"))
    str_liste_cartes = sys.stdin.readline().rstrip("\n").split(" ")
    
    for x in str_liste_cartes:
        if liste_cartes[int(x)-1] == 1:
            sys.stdout.write(x)
            exit(0)
        else:
            liste_cartes[int(x)-1] += 1
    sys.stdout.write("-1")

main()
