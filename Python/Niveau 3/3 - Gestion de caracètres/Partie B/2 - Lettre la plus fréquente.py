phrase = input().upper()

alphabet = [0 for _ in range(26)]

for caractère in phrase:
    code_unicode = ord(caractère)
    if (code_unicode >= 65) and (code_unicode <= 90):
        alphabet[code_unicode-65] += 1

nombre_apparitions_max = max(alphabet)

lettre_la_plus_apparue = chr(alphabet.index(nombre_apparitions_max) + 65)

print(lettre_la_plus_apparue)