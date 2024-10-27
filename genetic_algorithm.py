import random
import math

def geneticAlgorithm(valuesList, weightList, capacity, populationSize, numGenerations, mutationRate):
    population = generatePopulation(valuesList, weightList, capacity, populationSize)
    #print('pop = ', population)
    for i in range(numGenerations):
        print('\n gen = ', i)
        adapted = adaptation(population, valuesList, capacity)
        print('adapt = ', adapted)
        selected = selection(population, adapted)
        #print('sel = ', selected)
        children = crossover(selected)
        #print('child = ', children)
        mutated = mutation(children, mutationRate)
        #print('mut', mutated)
        best = getBest(population, valuesList, weightList, capacity)
        print('best ', best)
        population = mutated

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

def adaptation(population, values, capacity):
    totalSum = 0
    adapted = []
    for individual in population:
        indValue = 0
        for i in range(len(individual)):
            indValue += individual[i] * values[i]
        if indValue > capacity:
            indValue = 0
        adapted.append(indValue)
        totalSum += indValue
    for i in range(len(adapted)):
        adapted[i] = adapted[i]/totalSum
    return adapted

def selection(population, adapted):
    length = len(population)
    if length % 2 != 0:
        length -= 1
    selected = random.choices(population, weights=adapted, k = length)
    return selected

def crossover(selected):
    crosspoint = len(selected) - math.ceil((len(selected[0])*0.01))
    for i in range(len(selected)):
        if i%2 == 0:
            child1 = selected[i][:crosspoint] + selected[i+1][crosspoint:]
            child2 = selected[i+1][:crosspoint] + selected[i][crosspoint:]
            selected[i] = child1
            selected[i+1] = child2
    return selected


def mutation(children, mutationRate):
    for child in children:
        for i in range(len(child)):
            if random.random() < mutationRate:
                if child[i] == 0:
                    child[i] = 1
                else:
                    child[i] = 0
    return children

def getBest(population, values, weights, capacity):
    best = 0
    for individual in population:
        value = 0
        weight = 0
        for i in range(len(individual)):
            value += individual[i] * values[i]
            weight += individual[i] * weights[i]
        if weight <= capacity and value > best:
            best = value
    return best

#gera populacao escolhendo um vetor de 0s e 1s aleatoriamente
#verifica se o individuo cabe na mochila
#se couber, adiciona na populacao
#funcao de adaptacao calcula um valor entre 0 e 1 para
#cada individuo conforme valor  