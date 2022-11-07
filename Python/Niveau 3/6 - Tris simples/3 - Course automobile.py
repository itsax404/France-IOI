def main():

    valeurs = []
    clés =[]

    nombre_bacs = int(input())

    dictionnaire_bacs = dict()
    for x in range(nombre_bacs):
        identifiant_bac, pollution_bacs = map(int, input().split())
        dictionnaire_bacs[identifiant_bac] = pollution_bacs

    liste_indexs = sorted(dictionnaire_bacs.values())

    

main()