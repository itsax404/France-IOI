def abs(nombre):
    """
    Retourne la valeur absolue du nombre `nombre`
    Entrée:
        nombre: int
    Sortie:
        nombre: int
    >>> abs(-12)
    12
    >>> abs(12)
    12
    >>> abs(-150)
    150
    >>> abs(48)
    48
    """
    return nombre if nombre > 0 else -nombre

def chercher_le_plus_proche(question: int, liste: list[int], nombre_blocs: int) -> int:
    """
    Cette fonction permet d'envoyer l'élément le plus proche dans `liste`
    Entrées:
        question: int
        liste: list[int]
        nombre_blocs: int
    Sortie:
        réponse: int
    """
    if question >= liste[nombre_blocs-1]:
        return liste[nombre_blocs-1]
    elif question <= liste[0]:
        return liste[0]
    else:
        minimum = 0
        maximum = nombre_blocs-1
        milieu = -1
        while(minimum < maximum-1):
            milieu = minimum+(maximum-minimum) //2
            if(liste[milieu] > question):
                maximum = milieu
            else:
                minimum = milieu
        if abs(question - liste[minimum]) <= abs(question - liste[maximum]):
            return liste[minimum]
        else:
            return liste[minimum+1]

nombre_blocs = int(input())

liste_densité = list(map(int, input().split(" ")))

liste_densité.sort()

nombre_questions = int(input())

for _ in range(nombre_questions):
    question = int(input())
    print(chercher_le_plus_proche(question, liste_densité, nombre_blocs))