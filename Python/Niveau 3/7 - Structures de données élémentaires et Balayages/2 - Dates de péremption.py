dates_péremptions = []

nombre_opérations = int(input())

for _ in range(nombre_opérations):
    str_nombre_produits, type_opération = input().split(" ")
    nombre_produits = int(str_nombre_produits) 
    if nombre_produits >= 0:
        for _ in range(nombre_produits):
            dates_péremptions.insert(0, type_opération)
    else:
        opérations_faites = 0
        nombre_produits = -nombre_produits
        while(len(dates_péremptions) != 0) and (opérations_faites < nombre_produits):
            opérations_faites += 1
            dates_péremptions.pop(0)

plus_vieille_date_péremption = dates_péremptions[0]

while(len(dates_péremptions) != 0):
    date_péremption = dates_péremptions[0]
    if(date_péremption < plus_vieille_date_péremption):
        plus_vieille_date_péremption = date_péremption
    dates_péremptions.pop(0)

print(plus_vieille_date_péremption)
