def main():
    triangle = [[False] * 64 for x in range(64)];
    
    def remplissageTriangle(x, y, tailleTriangle):
        """Remplit la liste triangle avec True ou False
        afin de créer le trinagle plus facilement
        """
        if tailleTriangle == 1:
            triangle[x][y] = True
            return
        tailleTriangle = tailleTriangle // 2
        remplissageTriangle(x, y, tailleTriangle)
        remplissageTriangle(x + tailleTriangle, y, tailleTriangle)
        remplissageTriangle(x, y + tailleTriangle, tailleTriangle)
    
    taille = int(input())
    remplissageTriangle(0, 0, taille)
    for y in range(taille):
        for x in range(taille-y):
            if triangle[x][y]:
                print("#", end = "")
            else:
                print(" ", end = "")
        print()
main()