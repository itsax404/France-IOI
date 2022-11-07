import sys

def main():

    def est_valide(plan: list) -> int:
        """
        Retourne si le plan est valide
        """
        nombre_parenthèses_ouvertes = 0
        for parenthèse in plan:
            if parenthèse == "(":
                nombre_parenthèses_ouvertes += 1
            elif parenthèse == ")":
                nombre_parenthèses_ouvertes -= 1
            if nombre_parenthèses_ouvertes < 0:
                return 0
        if nombre_parenthèses_ouvertes == 0:
            return 1
        else:
            return 0

    str_nombre_caractères = sys.stdin.readline().rstrip("\n")
    nombre_caractères = int(str_nombre_caractères)

    str_caverne = sys.stdin.readline().rstrip("\n")
    str_caverne.replace(" ", "")

    plan_caverne = list(str_caverne.strip())

    print(est_valide(plan_caverne))

main()