def main():

    def a_tous_les_nombres(taille_grille: int, grille:list) -> bool:
        """
        Retourne un booléen si tous les éléments de `grille` sont 
        valides
        """
        valeur_max = taille_grille* taille_grille+1
        nombres_présents = [False] * valeur_max
        for ligne in grille:
            for nombre in ligne:
                if(nombre <= 0) or (nombre >= valeur_max) or nombres_présents[nombre]:
                    return False
                else:
                    nombres_présents[nombre] = True
        return True
    
    def total_direction(ligne_départ: int, colonne_départ: int, tuple_déplacements: tuple, taille_grille:int , grille: list)-> int:
        """
        Renvoie le total d'une direction, établie par 4 paramètres :
        - La ligne de départ
        - La colonne de départ
        - Le déplacement, pour la ligne, qu'il faut faire pour atteindre la case d'après
        - Le déplacement, pour la colonne, qu'il faut faire pour atteindre la case d'après
        """
        ligne, colonne = ligne_départ, colonne_départ
        total_direction = 0
        déplacement_ligne = tuple_déplacements[0]
        déplacement_colonne = tuple_déplacements[1]
        for _ in range(taille_grille):
            total_direction += grille[ligne][colonne]
            ligne += déplacement_ligne
            colonne += déplacement_colonne
        return total_direction

    def grille_correcte(taille_grille, grille):
        """
        Renvoie True si la grille est un carré magique
        sinon renvoie False
        >>> grille_correcte(3,[[6,1,8],[7,5,3],[2,9,4]])
        True
        """
        informations_déplacements = [(1,0),(0,1),(1,1),(-1,1)]
        
        nombre_de_base = total_direction(0,0,informations_déplacements[0], taille_grille, grille)
        for x in range(taille_grille):
            if total_direction(x, 0, informations_déplacements[1], taille_grille, grille) != nombre_de_base:
                return False
            if total_direction(0, x, informations_déplacements[0], taille_grille, grille) != nombre_de_base:
                return False
        if total_direction(0,0, informations_déplacements[2], taille_grille, grille) != nombre_de_base:
            return False
        if total_direction(taille_grille-1, 0, informations_déplacements[3], taille_grille, grille) != nombre_de_base:
            return False
        return True    
    
    taille_grille = int(input())
    grille = [[0 for _ in range(taille_grille)] for _ in range(taille_grille)]
    for ligne in range(taille_grille):
        entrée = list(map(int, input().split()))
        for colonne in range(taille_grille):
            grille[ligne][colonne] = entrée[colonne]
    
    if a_tous_les_nombres(taille_grille, grille) and grille_correcte(taille_grille, grille):
        print("yes")
    else:
        print("no")

main()