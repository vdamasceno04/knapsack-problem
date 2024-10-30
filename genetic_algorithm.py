import random
import math

def geneticAlgorithm(valuesList, weightList, capacity, populationSize, numGenerations, mutationRate):
    population = generatePopulation(valuesList, weightList, capacity, populationSize)
    bestOfAll = 0
    bestGen = 0
    #print('pop = ', population)
    for i in range(numGenerations):
        #print('\ngen = ', i)
        adapted = adaptation(population, valuesList, weightList, capacity)
        #print('adapt = ', adapted)
        if adapted == False: #if all individuals have value > capacity
            return bestOfAll, bestGen, lastBest
        selected = selection(population, adapted)
        #print('sel = ', selected)
        children = crossover(selected)
        #print('child = ', children)
        mutated = mutation(children, mutationRate)
        #print('mut', mutated)
        best = getBest(population, valuesList, weightList, capacity)
        #print('best ', best)
        population = mutated
        if best >= bestOfAll:
            bestOfAll = best
            bestGen = i
        lastBest = best
    return bestOfAll, bestGen, lastBest


def generateIndividual(size):
    individual = random.choices([0, 1], k = size)
    return individual
    
def generatePopulation(values, weights, capacity, populationSize):
    population = [] 
    while(len(population) < populationSize):
        individual = generateIndividual(len(values))
        fit = doesFit(individual, capacity, values, weights)
        if fit: #Doesnt allow individuals that dont fit in initial population
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
        return 0
    return value

def adaptation(population, values, weights, capacity):
    totalSum = 0
    adapted = []
    for individual in population:
        fitness = doesFit(individual, capacity, values, weights)
        adapted.append(fitness)
        totalSum += fitness
    for i in range(len(adapted)): 
        if totalSum == 0: #if all individuals have value > capacity
            return False
        else:
            adapted[i] = adapted[i]/totalSum
    return adapted

def selection(population, adapted): 
    """selects individuals based on their adaptation
    an individual can be selected more than once"""
    length = len(population)        
    if length % 2 != 0:
        length -= 1
    selected = random.choices(population, weights=adapted, k = length)
    return selected

def crossover(selected):
    """generates 2 children mixing 2 parents
    child1 is 90% parent1 and 10% parent2
    child2 is 90% parent2 and 10% parent1"""                        
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