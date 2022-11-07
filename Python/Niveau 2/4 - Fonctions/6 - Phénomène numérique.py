def syracuse(nombre1):
    x = nombre1
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            print(x, end = " ")
        else:
            x = x*3 +1
            print(x, end = " ")
      
nombre = int(input())
syracuse(nombre)