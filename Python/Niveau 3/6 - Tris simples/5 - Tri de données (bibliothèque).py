def main():

    nombre_bacs = int(input())

    bacs = list(map(int, input().split()))

    bacs_triés = sorted(bacs)

    for bac in bacs_triés:
        print(bac, end =" ")

main()