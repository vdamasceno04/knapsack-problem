import random

def geneticAlgorithm(valuesList, weightList, capacity, populationSize, numGenerations, mutationRate):
    population = generatePopulation(valuesList, weightList, capacity, populationSize)
    print('pop = ', population)
    a = 1
    return a, a, a


def generateIndividual(size):
    individual = random.choices([0, 1], k = size)
    return individual
    
def generatePopulation(values, weights, capacity, populationSize):
    population = []
    while(len(population) < populationSize):
        individual = generateIndividual(len(values))
        fit = doesFit(individual, capacity, values, weights)
        if fit:
            population.append(individual)
    return population

def doesFit(individual, capacity, values, weights):
    value = 0
    weight = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            value += values[i]
            weight += weights[i]
    if weight > capacity:
        return False
    return value
