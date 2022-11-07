nombre_marchands= int(input())
index_marchand_min = 0
prix_min = 1000000

for x in range(1, nombre_marchands+1):

  prix = int(input())
  
  if prix < prix_min:
    prix_min = prix
    index_marchand_min = x
  
  if prix == prix_min:
    index_marchand_min = x

print(index_marchand_min)