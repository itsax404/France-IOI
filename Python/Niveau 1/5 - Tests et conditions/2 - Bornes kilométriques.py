borne_départ = int(input())
borne_arrivée = int(input())

différence = 0

if(borne_arrivée >= borne_départ):
    différence = borne_arrivée - borne_départ
else:
    différence = borne_départ - borne_arrivée

print(différence)