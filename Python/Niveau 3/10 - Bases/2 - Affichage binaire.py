import sys

nombre = int(sys.stdin.readline().rstrip("\n"))

nombre_binaire = bin(nombre).lstrip("0b")

if nombre_binaire == "":
    print(0)
else:
    print(nombre_binaire)