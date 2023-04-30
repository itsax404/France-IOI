lettre_par_ordre = {x: y for x, y in zip("abcdefghijklmnopqrstuvwxyz", range(26))}
position_par_lettre = {x: y for x, y in zip(range(26), "abcdefghijklmnopqrstuvwxyz")}


def dechiffrement(lettre: str, cle_dechiffrement: int) -> str:
	"""
	Permet de déchiffrer la lettre 'lettre' avec la clé de déchiffrement 'cle_dechiffrement'
	Entrées:
		lettre: str
		cle_dechiffrement: int
	Sortie:
		lettre_dechiffree: str

	>>> dechiffrement("i", 6)
	'c'
	>>> dechiffrement("N", 9)
	'E'
	>>> dechiffrement("o", -2)
	'q'
	>>> dechiffrement("W", -6)
	'C'
	"""
	if not lettre.isalpha():
		return lettre
	else:
		lettre_minuscule = lettre.lower()
		emplacement_lettre_dechiffree = (lettre_par_ordre[lettre_minuscule] - cle_dechiffrement) % 26
		lettre_dechiffree = position_par_lettre[emplacement_lettre_dechiffree]
		if lettre.isupper():
			return lettre_dechiffree.upper()
		return lettre_dechiffree


def dechiffrement_ligne(ligne: str, cle_dechiffrement: int) -> str:
	"""
	Permet de déchiffrer une ligne entière `ligne`et la clé de déchiffrement `clé_déchiffrement`
	Entrées:
		ligne: str
		cle_dechiffrement: int
	Sortie:
		ligne_dechiffree: str
	>>> dechiffrement_ligne("Mufon, wiggyhn wu pu ?", -6)
	'Salut, comment ca va ?'
	>>> dechiffrement_ligne("Edjgfjdx yt hjxh jc stktadeetjg ?", 15)
	'Pourquoi je suis un developpeur ?'
	>>> dechiffrement_ligne("Xs giwg ib szsjsif rs Dmhvcb.", -12)
	'Je suis un eleveur de Python.'
	"""
	ligne_dechiffree = list()
	for lettre in ligne:
		ligne_dechiffree.append(dechiffrement(lettre, cle_dechiffrement))
	return "".join(ligne_dechiffree)


def calculer_frequence_apparition(ligne: str) -> str:
	"""
	Permet de trouver la lettre `lettre`qui apparait le plus dans la ligne.
	Entrée:
		ligne: str
	Sortie:
		lettre: str
	>>> calculer_frequence_apparition("Bcig towgcbg qcbtwobqs o rsg fomcbg L.")
	'b'
	>>> calculer_frequence_apparition("Jc upqjaxhit ht utgp ap bpaat p Sxhctnapcs.")
	'p'
	>>> calculer_frequence_apparition("Uvj uvdfej ivgfikrzvek tvj uviezvivj trirmrevj.")
	'v'
	"""
	frequence = [0 for _ in range(26)]
	for lettre in ligne:
		if (lettre.isalpha()):
			lettre = lettre.lower()
			frequence[lettre_par_ordre[lettre]] += 1
	max_apparitions = -1
	lettre = "a"
	for i in range(26):
		if frequence[i] > max_apparitions:
			max_apparitions = frequence[i]
			lettre = position_par_lettre[i]
	return lettre


def calcul_decalage(lettre: str) -> int:
	"""
	Permet de calculer le décalage, qui est la différence de position entre `lettre` et la lettre 'e', la
	plus présente dans la langue française
	Entrée:
		lettre: str
	Sortie:
		décalage: int
	>>> calcul_decalage("b")
	-3
	>>> calcul_decalage("g")
	2
	>>> calcul_decalage("q")
	12
	"""
	ordre_e = lettre_par_ordre["e"]
	ordre_lettre = lettre_par_ordre[lettre]
	return ordre_lettre - ordre_e


def main():
	ligne_chiffree = input()
	lettre_la_plus_apparue = calculer_frequence_apparition(ligne_chiffree)
	decalage = calcul_decalage(lettre_la_plus_apparue)
	print(dechiffrement_ligne(ligne_chiffree, decalage))


main()
