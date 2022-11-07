from sys import stdin

def main():

    nombre = int(stdin.readline())

    nombre_binaire = bin(nombre).lstrip("0b")

    print(2**(len(nombre_binaire)-1))


main()