def main():
   
    def trouver_clé_chiffrement(numéro_page: int) -> int:
        """
        Renvoie la clé de chiffrement selon le numéro de la page
        >>> trouver_clé_chiffrement(5)
        -25
        >>> trouver_clé_chiffrement(18)
        54
        """
        if numéro_page % 2 == 0:
            return numéro_page * 3
        else:
            return -5 * numéro_page

    def déchiffreur_lettre_minuscule(lettre: str, clé_chiffrement: int) -> str:
        """
        Renvoie `lettre` déchiffrée, qui est en minuscule, à l'aide de la
        `clé_chiffrement` 
        """
        code_lettre = ord(lettre)
        if(code_lettre- clé_chiffrement) < ord("a"):
            difference = code_lettre - ord("a")
            a_supprimer = clé_chiffrement - difference
            return chr(ord("z")- a_supprimer)
        elif code_lettre == ord("a"):
            return chr(ord("z") - clé_chiffrement)
        else:
            return chr(code_lettre - clé_chiffrement)
    
    def déchiffreur_lettre_majuscule(lettre, clé_chiffrement):
        """
        Renvoie `lettre` déchiffrée, qui est en majusucule, à l'aide de la
        `clé_chiffrement` 
        """
        code_lettre = ord(lettre)
        if(code_lettre - clé_chiffrement) <= ord("A"):
            difference = code_lettre - ord("A")
            a_supprimer = clé_chiffrement - difference
            return chr(ord("A") - a_supprimer)
        elif code_lettre == ord("A"):
            return chr(ord("Z") - clé_chiffrement)
        else:
            return chr(code_lettre - clé_chiffrement)
    def dechiffreur(page: str, numero_page:int) -> str:
        """Renvoie le texte sans le chiffrement
        >>>dechiffreur("Ikio kyz rg ykiutjk vgmk ja robxk",2)
        Ceci est la seconde page du livre
        """
        cle_chiffrement = trouver_clé_chiffrement(numero_page)
        ligne = ""
        for index_mots in range(len(page)):
            mots = page[index_mots]
            for index_mot in range(len(mots)):
                mot = mots[index_mot]
            for index_lettre in range(len(mots)):
                lettre = mots[index_lettre]
                if lettre.isalpha():
                    if lettre.islower():
                        lettre_déchiffré = déchiffreur_lettre_minuscule(lettre, cle_chiffrement)
                        ligne += lettre_déchiffré
                    elif lettre.upper():
                        lettre_déchiffré = déchiffreur_lettre_majuscule(lettre, cle_chiffrement)
                        ligne += lettre_déchiffré
                else:
                    ligne += lettre
        return ligne
        
    nombre_pages = int(input())

    for page in range(2, nombre_pages):
        str_page = input()
        print(dechiffreur(page, str_page))
main()