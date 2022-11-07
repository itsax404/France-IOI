def main():

    nombre_bacs_stocks, nombre_bacs_insérer = map(int, input().split())
    ligne_2 = input().strip()
    ligne_3 = input().strip()

    liste_stocks_initiale = [ int(x) for x in ligne_2.split()]
    liste_stocks_inserer = [ int(x) for x in ligne_3.split()]

    liste_index = [0 for _ in range(len(liste_stocks_inserer))]

    for y in liste_stocks_inserer:
        for x in range(len(liste_stocks_initiale)):
            if x == 0:
                if y <= liste_stocks_initiale[x]:
                    liste_index.append(x)
                    liste_stocks_initiale.append(y)
                    liste_stocks_initiale.sort()
            if x == (len(liste_stocks_initiale)-1):
                if y > liste_stocks_initiale[x]:
                    liste_stocks_initiale.append(y)
                    liste_stocks_initiale.sort()
                    liste_index.append(x)
            else:
                if liste_stocks_initiale[x-1] < y <= liste_stocks_initiale[x]:
                    liste_index.append(x+1)
                    liste_stocks_initiale.append(y)
                    liste_stocks_initiale.sort()
                else:
                    if liste_stocks_initiale[x-1] <= y < liste_stocks_initiale[x]:
                        liste_index.append(x)
                        liste_stocks_initiale.append(y)
                        liste_stocks_initiale.sort()    


    for x in range(len(liste_stocks_initiale)):
        print(liste_stocks_initiale[x], end= " ")




main()