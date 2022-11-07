nombre_notes = int(input())
somme_note = 0.0
for i in range(nombre_notes):
   note = float(input())
   somme_note += note
print(somme_note/nombre_notes)