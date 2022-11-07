population_actuelle = int(input())
croissance = float(input())

population_future =( population_actuelle + (croissance * population_actuelle)/100)

print(int(population_future))