def main():
   
    def dechiffreur_pair(ligne, cle):
        """a"""
        ligne_dechiffre = ""
        for lettre in ligne:
            if not lettre.isalpha():
                ligne_dechiffre += lettre
            elif lettre.isalpha():
                if lettre.isupper():
                if ord(lettre) - cle < ord("A"):
                    difference = ord(lettre) - ord("A")
                    difference_cle = cle - difference
                    while difference_cle > 26:
                        difference_cle -= 26
                    ligne_dechiffre += chr(ord("[") - difference_cle)
                else:
                    ligne_dechiffre += chr(ord(lettre) - cle) 
                elif lettre.islower():
                if ord(lettre) - cle < ord("a"):
                    difference = ord(lettre) - ord("a")
                    difference_cle = cle - difference
                    while difference_cle > 26:
                        difference_cle -= 26
                    ligne_dechiffre += chr(ord("{") - difference_cle)
                else:
                    ligne_dechiffre += chr(ord(lettre) - cle)      
                else:
                ligne_dechiffre += lettre      
        return ligne_dechiffre
    
    def dechiffreur_impair(ligne, cle):
        """a"""
        ligne_dechiffre = ""
        cle = -cle
        for lettre in ligne:
            if not lettre.isalpha():
                ligne_dechiffre += lettre
            else:
                if lettre.islower():
                if ord(lettre) + cle > ord("z"):
                    difference = (ord(lettre) + cle) - ord("z")
                    while difference > 26:
                        difference -= 26
                    ligne_dechiffre += chr(ord("`") + difference)
                else:
                    ligne_dechiffre += chr(ord(lettre) + cle)
                else:
                if ord(lettre) + cle > ord("Z"):
                    difference = (ord(lettre) + cle) - ord("Z")
                    while difference > 26:
                        difference -= 26
                    ligne_dechiffre += chr(ord("@") + difference)
                else:
                    ligne_dechiffre += chr(ord(lettre) + cle)

        return ligne_dechiffre 

        
    ligne = input()
    nombre_apparitions = [0]*26

    ligne_decode = ""
    for lettre in ligne:
        if not lettre.isalpha():
            ligne_decode += lettre
        else:
            lettre_lower = lettre.lower()
            nombre_apparitions[ord(lettre_lower) - ord("a")] += 1


    apparitions_max = 0   
    index_max = 0
    for x in range(len(nombre_apparitions)):
        if nombre_apparitions[x] > apparitions_max:
            index_max = x
            apparitions_max = nombre_apparitions[x]

    cle = index_max - (ord("e") - ord("a"))   

    if cle < 0:
        print(dechiffreur_impair(ligne, cle))
    else:
        print(dechiffreur_pair(ligne, cle))
main()