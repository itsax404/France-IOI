from math import sqrt

def distance(x1, y1, x2, y2):
    """
    Calcule la distance euclidienne entre deux points du plan
    Entrées :
        x1, y1 : coordonnées du premier point
        x2, y2 : coordonnées du second point
    Sortie :
        distance : la distance euclidienne entre les deux points
    """
    distance = sqrt((x2-x1)**2 + (y2-y1)**2 )
    print(distance)
   
x1 = float(input("Rentrez la valeur de x1 : \n"))
y1 = float(input("Rentrez la valeur de y1 : \n"))
x2 = float(input("Rentrez la valeur de x2 : \n"))
y2 = float(input("Rentrez la valeur de y2 : \n"))
distance(x1, y1, x2, y2)