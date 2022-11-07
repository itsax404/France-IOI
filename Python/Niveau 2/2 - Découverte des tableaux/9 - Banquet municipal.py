nombre_table = int(input())
nombre_changement = int(input())
position_table = [0]*nombre_table
for x in range(nombre_table):
    pos = int(input())
    position_table[x] = pos

for y in range(nombre_changement):
    position_1 = int(input())
    position_2 = int(input())
    temporaire = position_table[position_1]
    position_table[position_1] = position_table[position_2]
    position_table[position_2] = temporaire
   
for z in range(nombre_table):
    print(position_table[z])