def main():

    nombre_bacs_stocks, bacs_transportables = map(int, input().split())

    input_string = input().strip()
    liste_stocks = [ int(x) for x in input_string.split()]
    
    liste_stocks_reversed = sorted(liste_stocks, reverse=True)

    for item in range(bacs_transportables):
        print(liste_stocks_reversed[item], end=" ")
    

main()