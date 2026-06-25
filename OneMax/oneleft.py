import random
import matplotlib.pyplot as plt
import numpy as np

#ONE_MAX_LENGTH = 100 #длина подлежащей оптимизации битовой строки
ONE_MAX_LENGTH = 100 #длина подлежащей оптимизации битовой строки
MAX_FITNESS = 1275

POPULATION_SIZE = 200 #количество индивидуумов в популяции
P_CROSSOVER = 0.9 #вероятность скрещивания
P_MUTATION = 0.1 #вероятность мутации индивидуума
MAX_GENERATIONS = 60 #максимальное количество поколений

RANDOM_SEED = 142
random.seed(RANDOM_SEED)

class FitnessMax():
    def __init__(self):
        self.values = [0]

class Individual(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.fitness = FitnessMax()

def oneMaxFitness(ind):
    m = [-x * (i - len(ind) / 2) if i > len(ind) / 2 else (len(ind) / 2 - i) * x for i, x in enumerate(ind)]
    return sum(m),
    #return sum(ind), # тюпл

def individualCreator():
    return Individual(
        [random.randint(0, 1) for _ in range(ONE_MAX_LENGTH)],
    )

def populationCreator(n = 0):
    return list([individualCreator() for i in range(n)])

population = populationCreator(n = POPULATION_SIZE)
generationCounter = 0

fitnessValues = list(map(oneMaxFitness, population))

for individual, fitnessValue in zip(population, fitnessValues):
    individual.fitness.values = fitnessValue

maxFitnessValues = []
meanFitnessValues = []

def clone(value):
    ind = Individual(value[:])
    ind.fitness.values[0] = value.fitness.values[0]
    return ind

def selTournament(pop, p_len):
    result = []
    for n in range(p_len):
        i1 = i2 = i3 = 0
        while i1 == i2 or i1 == i3 or i2 == i3:
            i1, i2, i3 = random.randint(0, p_len - 1), random.randint(0, p_len - 1), random.randint(0, p_len - 1)

        result.append(max([pop[i1], pop[i2], pop[i3]], key=lambda ind: ind.fitness.values[0]))
    return result

def cxOnePoint(ch1, ch2):
    s = random.randint(2, len(ch1) - 3)
    ch1[s:], ch2[s:] = ch2[s:], ch1[s:]

def mutFlipBit(mtnt, indpb=0.01):
    for indx in range(len(mtnt)):
        if random.random() < indpb:
            mtnt[indx] = 0 if mtnt[indx] == 1 else 1

fitnessValues = [individual.fitness.values[0] for individual in population]

while max(fitnessValues) < MAX_FITNESS and generationCounter < MAX_GENERATIONS:
    generationCounter += 1
    offspring = selTournament(population, len(population))
    offspring = list(map(clone, offspring))

    for child1, child2 in zip(offspring[::2], offspring[1::2]):
        if random.random() < P_CROSSOVER:
            cxOnePoint(child1, child2)

    for mutant in offspring:
        if random.random() < P_MUTATION:
            mutFlipBit(mutant, indpb=1.0/ONE_MAX_LENGTH)

    freshFitnessValues = list(map(oneMaxFitness, offspring))
    for individual, fitnessValue in zip(offspring, freshFitnessValues):
        individual.fitness.values = fitnessValue

    population[:] = offspring

    fitnessValues = [ind.fitness.values[0] for ind in population]

    maxFitness = max(fitnessValues)
    meanFitness = sum(fitnessValues) / len(population)
    maxFitnessValues.append(maxFitness)
    meanFitnessValues.append(meanFitness)
    print (f"Generation {generationCounter}: max fitness = {maxFitness}, mean fitness = {meanFitness}")

    best_index = fitnessValues.index(max(fitnessValues))
    print("Best individual: ", *population[best_index], "")
    #worst_index = fitnessValues.index(min(fitnessValues))
    #print("Worse individual: ", *population[worst_index], "\n")

plt.plot(maxFitnessValues, color='red')
plt.plot(meanFitnessValues, color='green')
plt.xlabel("Generation")
plt.ylabel("max/mean fitness")
plt.title("How max and mean fitness depends on generation")
plt.show()