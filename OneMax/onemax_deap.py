import numpy as np
from deap import base, creator, tools, algorithms

import random
import matplotlib.pyplot as plt

ONE_MAX_LENGTH = 100 #длина подлежащей оптимизации битовой строки

POPULATION_SIZE = 200 #количество индивидуумов в популяции
P_CROSSOVER = 0.9 #вероятность скрещивания
P_MUTATION = 0.1 #вероятность мутации индивидуума
MAX_GENERATIONS = 50 #максимальное количество поколений

RANDOM_SEED = 142
random.seed(RANDOM_SEED)

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness = creator.FitnessMax)

def oneMaxFitness(ind):
    return sum(ind), # тюпл

# def oneMaxFitness(ind):
#     m = [x * (i - len(ind) / 2) if i > len(ind) / 2 else -(len(ind) / 2 - i) * x for i, x in enumerate(ind)]
#     return sum(m),

# def oneMaxFitness(ind):
#     m = [-x * (i - len(ind) / 2) if i > len(ind) / 2 else (len(ind) / 2 - i) * x for i, x in enumerate(ind)]
#     return sum(m),

# def oneMaxFitness(ind):
#     m = [
#         -x * abs(len(ind)/2 - i) if abs( len(ind)/2 - i )  > 10
#         else x * ( len(ind)/2 - abs(len(ind)/2 - i) )
#         for i, x in enumerate(ind)
#     ]
#     return sum(m),

toolbox = base.Toolbox()
toolbox.register("zeroOrOne", random.randint, 0, 1)
toolbox.register(
    "individualCreator",
    tools.initRepeat,
    creator.Individual,
    toolbox.zeroOrOne,
    ONE_MAX_LENGTH)
toolbox.register(
    "populationCreator",
    tools.initRepeat,
    list,
    toolbox.individualCreator)

population =  toolbox.populationCreator(n = POPULATION_SIZE)
generationCounter = 0

fitnessValues = list(map(oneMaxFitness, population))

for individual, fitnessValue in zip(population, fitnessValues):
    individual.fitness.values = fitnessValue

maxFitnessValues = []
meanFitnessValues = []

toolbox.register("evaluate", oneMaxFitness)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", tools.cxOnePoint)
toolbox.register("mutate", tools.mutFlipBit, indpb = 1.0 / ONE_MAX_LENGTH)

stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("max", np.max)
stats.register("mean", np.mean)
stats.register("values", np.array)

population, logbook = algorithms.eaSimple(
    population, toolbox,
    cxpb=P_CROSSOVER,
    mutpb=P_MUTATION,
    ngen=MAX_GENERATIONS,
    stats=stats,
    verbose=True
)

maxFitnessValues, meanFitnessValues, vals = logbook.select("max", "mean", "values")

#print (len(vals))

import time

plt.ion()
fig, ax = plt.subplots()

line, = ax.plot(vals[0], ' o', markersize=1)
ax.set_ylim(40, 110)

for v in vals:
    line.set_ydata(v)

    plt.draw()
    plt.gcf().canvas.flush_events()

    time.sleep(0.5)

plt.ioff()
plt.show()

# plt.plot(maxFitnessValues, color='red')
# plt.plot(meanFitnessValues, color='green')
# plt.xlabel("Generation")
# plt.ylabel("max/mean fitness")
# plt.title("How max and mean fitness depends on generation")
# plt.show()

# maxFitness = max(maxFitnessValues)
# print (maxFitness)
# best_ind = next((ind for ind in population if ind.fitness.values == maxFitness), None)
# print(best_ind)