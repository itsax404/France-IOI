def main():

    def est_un_pion(ligne, colonne, grille):
        """
        Retourne un booléen s'il y a un pion aux coordonées `(ligne, colonne)`
        """
        if ((ligne < 0) or (ligne >= 8) or (colonne < 0) or (colonne >= 8)):
            return False
        caractère = grille[ligne][colonne]
        if caractère.islower():
            return True
        else:
            return False
        
    déplacements = [(-1,-2),(-2,-1),(-2,+1),(-1,+2),(+1,+2),(+2,+1), (+2,-1), (+1,-2)]
    
    def a_un_pion_attaquable(grille):
        """
        Vérifie si il y a un élément noir dans la case atteignable
        par un cavalier blanc
        """
        cases = ["."for x in range(8)]
        yes = False
        for ligne in range(8):
            for colonne in range(8):
                if grille[ligne][colonne] == "C" :
                    for mouvement_ligne, mouvement_colonne in déplacements:
                        if est_un_pion(ligne +mouvement_ligne, colonne+ mouvement_colonne, grille):
                            return True

    
   
    

    échiquier = [["." for _ in range(8)] for _ in range(8)]

    for ligne in range(8):
        input_string = input().strip()
        input_list = [x for x in input_string]

        for colonne in range(8):
            échiquier[ligne][colonne] = input_list[colonne]
    


    if a_un_pion_attaquable(échiquier):
        print("yes")
    else:
        print("no")

main()


