nombre,base_cible = map( int, input().split() )
chiffres = list()

encore_un_chiffre = True

while encore_un_chiffre:
    chiffres.append(nombre % base_cible)
    nombre = nombre // base_cible
    encore_un_chiffre = (nombre > 0)

print(len(chiffres))
print(" ".join([str(x) for x in reversed(chiffres)]))