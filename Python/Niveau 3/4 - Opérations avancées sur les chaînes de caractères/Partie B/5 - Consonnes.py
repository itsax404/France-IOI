voyelles = [ord("a"),ord("e"),ord("i"),ord("o"),ord("u"),ord("y")]
for ascii in range(ord("a"), ord("z")+1):
    if ascii not in voyelles:
        print(chr(ascii)+" ",end= "")