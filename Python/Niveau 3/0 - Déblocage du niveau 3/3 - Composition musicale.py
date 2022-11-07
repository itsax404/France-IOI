notes = list(input())

def test_redondance(longueur_phrase,phrase) :
    for i in range(1,longueur_phrase) :
        if phrase[i]==phrase[i-1] :
            return 0
            break
    return 1

while test_redondance(len(notes),notes)==0 :
    for i in range(1,len(notes)) :
        if notes[i]==notes[i-1] :
            del notes[i]
            del notes[i-1]
            break

phrase="".join(notes)
print(phrase)