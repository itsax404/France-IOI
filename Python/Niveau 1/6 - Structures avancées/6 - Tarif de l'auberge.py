age = int(input())
poids_bagages = int(input())
ecu = 0

if age == 60:
    ecu = 0
else:
    if age < 10:
        ecu = 5
    else:
        ecu = 30
        if poids_bagages >= 20:
            ecu = 40
print(ecu)