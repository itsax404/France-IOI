longueur_coté = int(input())

plateau = [[0 for _ in range(longueur_coté)] for _ in range(longueur_coté)]

for ligne in range(longueur_coté):
    entrée = list(map(int, input().split()))
    for colonne in range(longueur_coté):
        plateau[ligne][colonne] = entrée[colonne]

directions = [(-1,1),(0,1),(1,1),(1,0)]

def est_dans_le_plateau(ligne, colonne):
    """
    Retourne un booléen si les coordonnées (`ligne`,`colonne`) est
    dans le plateau
    """
    if (ligne < 0) or (ligne >= longueur_coté) or (colonne < 0) or (colonne >= longueur_coté):
        return False
    return True

for ligne in range(longueur_coté):
    for colonne in range(longueur_coté):
        joueur = plateau[ligne][colonne]
        if joueur != 0:
            for direction in directions:
                ligne_temporaire = ligne
                colonne_temporaire = colonne
                alignés = 1
                for _ in range(4):
                    ligne_temporaire += direction[0]
                    colonne_temporaire += direction[1]
                    if est_dans_le_plateau(ligne_temporaire, colonne_temporaire):
                        if(plateau[ligne_temporaire][colonne_temporaire] == joueur):
                            alignés += 1
                if alignés == 5:
                    print(joueur)
                    exit(0)
print(0)