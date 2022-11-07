nombre_variables = int(input())

def validité_variable(nom_variable: str) -> bool:
    """
    Renvoie True si `nom_variable` est correct
    sinon renvoie False
    >>> validité_variable("Bonjour32")
    True
    >>> validité_variable("r~ussi")
    False
    >>> validité_variable("_toto_")
    True
    >>> validité_variable("passe-partout)
    False
    >>> validité_variable("2_fois")
    False
    """
    somme_caractère_valable = 0
    if(nom_variable[0].isalpha()) or (nom_variable[0] == "_"):
        for caractère in nom_variable:
            if(caractère.isalpha()) or  (caractère == "_") or (caractère.isdigit()):
                somme_caractère_valable += 1
    else:
        return False
    
    if(somme_caractère_valable == len(variable)):
        return True
    else: 
        return False

for x in range(nombre_variables):
    variable = input()
    print("YES" if validité_variable(variable) else "NO")