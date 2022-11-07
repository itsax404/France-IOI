nombre_table = int(input())
nombre_changement = int(input())
position_personne = [0]*nombre_table
for x in range(nombre_table):
   position = int(input())
   position_personne[x] = position_personne

for y in range(nombre_changement):
   position_1 = int(input())
   positon_2 = int(input())
   temporaire = position_personne[position_1]
   position_personne[position_1] = position_personne[position_2]
   position_personne[positon_2] = temporaire
   
for z in range(nombre_table):
   print(position_personne[z])