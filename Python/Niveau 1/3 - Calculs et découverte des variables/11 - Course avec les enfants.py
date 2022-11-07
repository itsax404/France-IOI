from robot import*

for x in range(1, 11):
    for y in range(1,x):
        droite()
        ramasser()
    for y in range(1,x):
        gauche()
        deposer()