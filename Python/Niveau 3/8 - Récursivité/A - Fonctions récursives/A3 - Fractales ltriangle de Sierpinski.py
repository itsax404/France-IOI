def main():
	triangle = [[False for _ in range(64)] for x in range(64)];

	def remplissageTriangle(x: int, y: int, tailleTriangle: int) -> None:
		"""Remplit la liste triangle avec True ou False
		afin de créer le triangle plus facilement
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
	sortie = list()
	for y in range(taille):
		for x in range(taille - y):
			if triangle[x][y]:
				sortie.append("#")
			else:
				sortie.append(" ")
		sortie.append("\n")
	print("".join(sortie))

main()