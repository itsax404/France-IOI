def abs(nombre):
    """
    docstring
    """
    return nombre if nombre > 0 else -nombre

def chercher_le_plus_proche(question, liste, nombre_blocs):
    """
    docstring
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