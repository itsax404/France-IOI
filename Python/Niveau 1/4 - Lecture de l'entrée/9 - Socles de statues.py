etage_max = int(input())
etage_min = int(input())
volume = 0

for x in range(etage_min, etage_max + 1):
  volume = volume + x*x
print(volume)