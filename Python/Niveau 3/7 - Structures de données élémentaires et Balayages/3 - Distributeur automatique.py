import sys


def main():

    file = []

    def ajouter(nombre: int) -> None:
        """
        Permet d'ajouter `nombre`à la pile (soit à la fin)
        Entrée:
            nombre: int
        Sortie:
            None
        """
        file.append(nombre)
    
    def enlever():
        """
        Permet d'enlever un élément à la pile (soit le premier élément de la liste)
        Entrée:
            None
        Sortie:
            None
        """
        file.pop(0)

    def premier_terme() -> int:
        """
        Permet de retourner le premier élément de la pile
        Entrée:
            None
        Sortie:
            nombre: int
        """
        return file[0]

    def est_plus_ancien() -> int:
        """
        Permet de retourner la date de péremption la plus ancienne en dépilant les éléments
        Entrée:
            None
        Sortie:
            minimum: int
        """
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