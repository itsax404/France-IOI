n = int(input())
male_male = []
male_femelle = []
femelle_femelle = []
for _ in range(n):
    c_1, c_2, longueur = map(int, input().split())
    if c_1 == c_2 == 1:
        male_male.append(longueur)
    elif c_1 == c_2 == 0:
        femelle_femelle.append(longueur)
    else:
        male_femelle.append(longueur)

male_male.sort()
#male_femelle.sort()
femelle_femelle.sort()

if male_male == []:
    ans = -1
else:
    ans = male_male.pop()
    ans += sum(male_femelle)
    n1 = len(male_male)
    n2 = len(femelle_femelle)
    n = min(n1, n2)
    for _ in range(n):
        ans += male_male.pop() + femelle_femelle.pop()

print(ans)
