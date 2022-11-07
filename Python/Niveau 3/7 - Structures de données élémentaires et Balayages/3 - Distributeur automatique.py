import sys


def main():

    file = []

    def ajouter(nombre):
        """
        TODO docstring
        """
        file.append(nombre)
    
    def enlever():
        file.pop(0)

    def premier_terme():
        return file[0]

    def est_plus_ancien():
        minimum = premier_terme()
        while len(file) != 0:
            date_a_tester = premier_terme()
            minimum = min(minimum, date_a_tester)
            enlever()
        return minimum

    nombre_opérations = int(sys.stdin.readline().rstrip("\n"))

    for _ in range(nombre_opérations):
        nombre_produit, type_opération = map(int, sys.stdin.readline().rstrip("\n").split(" "))
        if nombre_produit > 0:
            for x in range(nombre_produit):
                ajouter(type_opération)
        else:
            nombre_produit = -nombre_produit
            for _ in range(nombre_produit):
                enlever()
    
    
    print(est_plus_ancien())

main()