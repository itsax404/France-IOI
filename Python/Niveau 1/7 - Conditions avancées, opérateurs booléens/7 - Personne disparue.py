numéro_recherché = int(input())
longuer_registre = int(input())
estSorti = False

for _ in range(longuer_registre):
   numéro_a_vérifier = int(input())
   if numéro_recherché == numéro_a_vérifier:
       print("Sorti de la ville")
       estSorti = True
   
if not (estSorti):
   print("Encore dans la ville")