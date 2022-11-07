hauteur = int(input())
nombre_folioles = int(input())

if( hauteur >= 10):
    if(nombre_folioles <= 7):
        print("Dorthonion")
    else:
        print("Calaelen")
    
else:
    if(nombre_folioles <= 5):
        print("Falarion")
    else:
        print("Tinuviel")
