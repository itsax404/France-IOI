phrase = input().upper()

alphabet = [0 for _ in range(26)]

code_a_majuscule = ord("A")

nombre_caractères = 0
for caracètre in phrase:
    if "A" <= caracètre <= "Z":
        alphabet[ord(caracètre) - code_a_majuscule] += 1
        nombre_caractères += 1

for x in range(26):
    moyenne_caractère = (alphabet[x]/nombre_caractères)
    print(round(moyenne_caractère,6))