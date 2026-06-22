import random
import matplotlib.pyplot as plt

ONE_MAX_LENGTH = 100 #длина подлежащей оптимизации битовой строки

POPULATION_SIZE = 200 #количество индивидуумов в популяции
P_CROSSOVER = 0.9 #вероятность скрещивания
P_MUTATION = 0.1 #вероятность мутации индивидуума
MAX_GENERATIONS = 50 #максимальное количество поколений