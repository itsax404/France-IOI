nombre_zones = int(input())
zone = 24
distance = nombre_zones % zone

if distance < 0:
   print(-distance)
else:   
   print(distance)