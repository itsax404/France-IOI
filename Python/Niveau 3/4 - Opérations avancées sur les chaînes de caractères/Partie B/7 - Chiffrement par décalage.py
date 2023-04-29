def main():
	

	def lettre_dechiffage_positive(lettre, cle):
		"""a"""
		lettre_ord = ord(lettre)
		nouvelle_lettre_ord = lettre_ord - cle
		if lettre.isalpha():
			if lettre.islower():
				if nouvelle_lettre_ord > ord("a"):
					if(lettre == "g"):
						print(f"{lettre=} {nouvelle_lettre_ord=} {chr(nouvelle_lettre_ord) =")
					return chr(nouvelle_lettre_ord)
				elif lettre_ord == ord("a"):
					return chr(ord("z") - cle)
				elif nouvelle_lettre_ord < ord("a"):
					difference = cle - ord("a")
					nouvelle_lettre_ord = ord("z")-difference
					return chr(nouvelle_lettre_ord)
			if lettre.isupper():
				if nouvelle_lettre_ord > ord("A"):
					return chr(nouvelle_lettre_ord)
				elif lettre_ord == ord("A"):
					return chr(ord("Z") - cle)
				elif nouvelle_lettre_ord < ord("A"):
					difference = cle - ord("A")
					nouvelle_lettre_ord = ord("Z")-difference
					return chr(nouvelle_lettre_ord)
		return lettre

	def lettre_dechiffage_negatif(lettre, cle):
		"""a"""
		lettre_ord = ord(lettre)
		cle_positif = -cle
		nouvelle_lettre_ord = lettre_ord + cle_positif
		if lettre.isalpha():
			if lettre.islower():
				if nouvelle_lettre_ord < ord("z"):
					return chr(nouvelle_lettre_ord)
				elif lettre_ord == ord("z"):
					return chr(ord("a") + cle_positif)
				elif nouvelle_lettre_ord > ord("z"):
					difference = cle - ord("z")
					nouvelle_lettre_ord = ord("a") + difference
					return chr(nouvelle_lettre_ord)
			if lettre.isupper():
				if nouvelle_lettre_ord < ord("Z"):
					return chr(nouvelle_lettre_ord)
				elif lettre_ord == ord("Z"):
					return chr(ord("A") + cle_positif)
				elif nouvelle_lettre_ord > ord("Z"):
					difference = cle - ord("Z")
					nouvelle_lettre_ord = ord("A") + difference
					return chr(nouvelle_lettre_ord)
		return lettre

	def dechiffreur(page, numero_page):
		"""Renvoie le texte sans le chiffrement
		>>>dechiffreur("Ikio kyz rg ykiutjk vgmk ja robxk",2)
		Ceci est la seconde page du livre
		"""
		nouvelle_page = ""
		cle_chiffrement = 0
		if numero_page % 2 == 0:
			cle_chiffrement = numero_page * 3
		elif numero_page % 2 == 1 :
			cle_chiffrement == -5*numero_page
		for index_mots in range(len(page)):
			mots = page[index_mots]
			for index_mot in range(len(mots)):
				mot = mots[index_mot]
				for index_lettre in range(len(mot)):
					lettre = mot[index_lettre]
					if cle_chiffrement < 0:		
						nouvelle_page += lettre_dechiffage_negatif(lettre, cle_chiffrement)
					elif cle_chiffrement > 0:
						nouvelle_page += lettre_dechiffage_positive(lettre, cle_chiffrement)
		return nouvelle_page
		
	nombre_pages = int(input())
	
	for pages in range(2,nombre_pages,1):
		page = input()
		print(dechiffreur(page,pages))
		
	
main()
