somme_dépenses = 0
while True:
   dépense = int(input()) 
   if dépense == -1:
      break
   else:
      somme_dépenses += dépense
      
print(somme_dépenses)