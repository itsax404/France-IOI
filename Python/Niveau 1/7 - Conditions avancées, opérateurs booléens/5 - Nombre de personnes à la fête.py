personnes_fête = int(input())
personnes_simultanée = 0
personnes_max = 0

for x in range(personnes_fête * 2):
    action = int(input())
    if action > 0:
        personnes_simultanée += 1
    
        if personnes_simultanée > personnes_max:
            personnes_max = personnes_simultanée
    else:
        personnes_simultanée -= 1
    
print(personnes_max)