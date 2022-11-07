from collections import Counter

dictionnaire_densité = Counter()

nombre_blocs = int(input())

entrée_itérateur = map(int, input().split(" "))

for x in entrée_itérateur:
    dictionnaire_densité[x] += 1

nombre_questions = int(input())

for _ in range(nombre_questions):
    question = int(input())
    if dictionnaire_densité[question] > 1:
        print(1)
    else:
        print(dictionnaire_densité[question])