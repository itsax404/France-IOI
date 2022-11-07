position = int(input())
village = int(input())
villages_atteignables = 0

for x in range(village):
    distance = int(input())
    distance = distance - position
    if distance < 0:
        distance = -distance
    if distance <= 50:
        villages_atteignables += 1
print(villages_atteignables)