#Lecture de l'entrée
nombre_erosions = int(input())
ligne_image, colonne_image = map(int, input().split())

image = [["." for _ in range(colonne_image)] for _ in range(ligne_image)]

for ligne in range(ligne_image):
    entrée = list(input().strip())
    for colonne in range(colonne_image):
        image[ligne][colonne] = entrée[colonne]

def érosion(ligne, colonne):
    """
    TODO
    """
    directions = [(-1,0),(0,-1),(1,0),(0,1)]
    if (ligne-1 >= 0) and (ligne+1 <= ligne_image-1) and (colonne-1 >= 0) and (colonne+1 <= colonne_image-1):
        pions_érodables = 0
        for direction in directions:
            index_ligne = direction[0]
            index_colonne = direction[1]
            if(image[ligne+index_ligne][colonne+index_colonne] == "#"):
                pions_érodables += 1
        if pions_érodables == 4:
            image[ligne][colonne] = "."
            for direction in directions:
                index_ligne = direction[0]
                index_colonne = direction[1]
                image[ligne+index_ligne][colonne+index_colonne] = "."

for ligne in range(ligne_image):
    for colonne in range(colonne_image):
        if(image[ligne][colonne] == "#"):
            érosion(ligne,colonne)
    
print()
for ligne in range(ligne_image):
    for colonne in range(colonne_image):
        print(image[ligne][colonne], end="")
    print()