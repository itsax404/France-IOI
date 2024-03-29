def main():
   
    def a_le_meme_acronyme(titre, acronyme):
        """
        Renvoie True si le titre à le même acronyme
        Entrée :
            titre (str)
        Sortie :
            bool
        >>>a_le_meme_acronyme("Le Petit Prince", "LPP")
        True
        >>>a_le_meme_acronyme("Le Petit Chat", "LPP")
        False
        """
        titre_maj = titre.upper()
        acronyme_titre = ""
        mots = titre_maj.split()
        for x in range(len(mots)):
            mot = mots[x]
            acronyme_titre = acronyme_titre + mot[0]
        if acronyme_titre == acronyme:
            return True
        else:
            return False  
         
    def titre_correct(titre):
        """
        Renvoie le titre prêt à être afficher
        Entrée:
            titre (str)
        Sortie:
            str
        >>>titre_correct("le petit prince")
        "Le Petit Prince"
        >>>titre_correct("le petit chat")
        "Le Petit Chat"
        """
        titre_minuscule = titre.lower()
        mots = titre_minuscule.split()
        nouveau_titre = ""
        for x in range(len(mots)):
            mot = mots[x]
            for y in range(len(mot)):
                if y == 0:
                    nouveau_titre = nouveau_titre + mot[0].upper()
                else:
                    nouveau_titre = nouveau_titre + mot[y]
            nouveau_titre = nouveau_titre + " "
        return nouveau_titre
               
       
   
    acronyme = input()
    nombre_livres = int(input())
    for x in range(nombre_livres):
        titre_input = input()
        if a_le_meme_acronyme(titre_input, acronyme):
            print(titre_correct(titre_input))

main()