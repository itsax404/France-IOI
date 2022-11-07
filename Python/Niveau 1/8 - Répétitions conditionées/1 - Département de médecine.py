population_totale = int(input())
population_malade = 1
nombre_jour = 1

while population_malade < population_totale:
   nombre_jour += 1
   population_malade = population_malade + (population_malade*2)
   
print(nombre_jour)