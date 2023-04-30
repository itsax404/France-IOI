lettre_par_ordre = {x: y for x,y in zip("abcdefghijklmnopqrstuvwxyz", range(26))}

def dechiffreur(ligne_chiffrée, clé_chiffrement):
    """
    Renvoie la ligne déchiffrée.
    Entrées:
        ligne_chiffrée: str
        clé_chiffrement: int
    Sortie:
        ligne_déchiffrée: str
    >>> dechiffreur("Xiyqigd !", "qwertyuiopasdfghjklzxcvbnm")
    'Bonjour !'

    >>> dechiffreur("Ehaot tpot am spvzm !", "lkcjszyafpqheruoxgmtwnvbid")
    'Salut tout le monde !'

    >>> dechiffreur("Xpvdon, cpssmvt to whe ?", "lkcjszyafpqheruoxgmtwnvbid")
    'Bonjour, comment tu vas ?'
    """

    caractères_déchiffrés = []
    for caractère in ligne_chiffrée:
        if caractère.isalpha():
            emplacement_caractère_déchiffrée = lettre_par_ordre[caractère.lower()]
            caractères_déchiffré = clé_chiffrement[emplacement_caractère_déchiffrée]
            if caractère.isupper():
                caractères_déchiffrés.append(caractères_déchiffré.upper())
            else:
                caractères_déchiffrés.append(caractères_déchiffré)
        else:
            caractères_déchiffrés.append(caractère)
    return "".join(caractères_déchiffrés)

clé_chiffrement = input()
mot_chiffré = input()

print(dechiffreur(mot_chiffré, clé_chiffrement))
