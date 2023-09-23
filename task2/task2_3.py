population = int(input("Enter the population of the universe: "))

if population % 2 == 0:
    survivors = population // 2
else:
    survivors = (population + 1) // 2

print(survivors)
