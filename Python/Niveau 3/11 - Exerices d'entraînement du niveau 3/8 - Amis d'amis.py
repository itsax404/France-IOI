import sys

def main(input=sys.stdin.readline):
    identifiant_ami = int(input())

    set_identifiant_enregistrés = set()

    liste_identifiants = [set() for _ in range(65000)]

    nombre_relations = int(input())

    for _ in range(nombre_relations):
        identifiant, ami = map(int, input().split(" "))

        liste_identifiants[ami].add(identifiant)
        liste_identifiants[identifiant].add(ami)


    déjà_vu = set()
    réponse = 0

    for x in liste_identifiants[identifiant_ami]:
        for y in liste_identifiants[x]:
            if y not in liste_identifiants[identifiant_ami] and y not in déjà_vu and y != identifiant_ami:
                réponse += 1
                déjà_vu.add(y)

    print(réponse)

main()