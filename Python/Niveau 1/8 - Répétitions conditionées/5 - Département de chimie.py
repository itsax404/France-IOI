nombre_tests = int(input())
température_min = int(input())
température_max = int(input())
 
for i in range(nombre_tests):
    température_test = int(input())
    if température_min <= température_test <= température_max:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break