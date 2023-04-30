lettre_par_ordre = {x: y for x, y in zip("abcdefghijklmnopqrstuvwxyz", range(26))}
position_par_lettre = {x: y for x, y in zip(range(26), "abcdefghijklmnopqrstuvwxyz")}

def dechiffrement(lettre: str, cle_dechiffrement : int) -> str:
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

def main():
	nombre_lignes = int(input())
	lignes_déchifrées = list()
	for i in range(2, nombre_lignes+1):
		ligne_chiffrée = input()
		cle = 3*i if i % 2 == 0 else -5*i
		lignes_déchifrées.append(dechiffrement_ligne(ligne_chiffrée, cle))
	print("\n".join(lignes_déchifrées))

main()