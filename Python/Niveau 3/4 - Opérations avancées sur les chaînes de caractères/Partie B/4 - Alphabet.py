for ascii in range(ord("A"), ord("Z")+1):
    if ascii == ord("Z"):
        print(chr(ascii),end ="")
    else:
        print(chr(ascii) + " ", end ="")