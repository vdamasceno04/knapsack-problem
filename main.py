from argparse import ArgumentParser
import re
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from genetic_algorithm import geneticAlgorithm

def parse_args():
    parser = ArgumentParser(description = 'Knapsack Problem')
    parser.add_argument('algorithm', help = 'Possible algoritms: random, annealing, genetic')
    parser.add_argument('totalItems', type = int, help = 'Total number of items')
    parser.add_argument('-seed', dest = 'seed',  type = int, required = False, help = 'Test generator seed')
    parser.add_argument('-v', action = 'store', dest = 'values', required = False,
                        help = 'Items values list(ex: [60,100,120])')
    parser.add_argument('-w', action = 'store', dest = 'weights', required = False,
                        help = 'Items weights list (ex: [1,2,3])')
    parser.add_argument('-W', action = 'store', dest = 'W', type = int, required = False,
                        help = 'Knapsack capacity')
    parser.add_argument('-ex', action = 'store', dest = 'exec', type = int, required = False,
                        help = 'Times to execute the algorithm')
    parser.add_argument('-ps', action = 'store', dest = 'populationSize', type = int, required = False,
                        help = 'only for genetic algorithm')
    parser.add_argument('-ng', action = 'store', dest = 'numGenerations', type = int, required = False,
                        help = 'only for genetic algorithm')
    parser.add_argument('-mr', action = 'store', dest = 'mutationRate', type = float, required = False,
                        help = 'only for genetic algorithm')

    return parser.parse_args()

def main():
    args = parse_args()
    print(args)
    if(args.values is not None and args.weights is not None and args.W is not None):
        valueList = [int(s) for s in re.findall(r'\b\d+\b', args.values)]
        weightList = [int(s) for s in re.findall(r'\b\d+\b', args.weights)]

        if len(valueList) != args.totalItems or len(weightList) != args.totalItems:
            print("ERROR: Number of items in values and weights must be equal to totalItems")
            return

        if args.W <= 0:
            print("ERROR: Capacity must be greater than zero")
            return

        capacity = args.W

    else:
        if args.seed is not None:
            random.seed(args.seed)
        valuesList = random.sample(range(1, 9999), int(args.totalItems))
        weightList = random.sample(range(1, 9999), int(args.totalItems))

        if args.W is not None:
            capacity = args.W
        else:
            capacity = random.randint(1, 99999)

    print('Values list: ',valuesList)
    print('Weights list: ', weightList)
    print('Capacity: ', capacity)

    if args.exec is None:
        args.exec = 1
    contExec = 0
    bestValues = [523, 24, 734, 56, 725, 688, 888, 995, 888, 888]
    lastValues = []
    bestCycles = []
    while(contExec < args.exec):
        if args.algorithm == 'random':
            start = time.time()
            value, weight, items = randomAlgorithm(valuesList, weightList, capacity)
            end = time.time()
            print('Elapsed time random: ', end - start)
            print('Value: ', value)
            print('Weight: ', weight)
            print('Items: ', items)

        elif args.algorithm == 'annealing':
            #start = time.time()
            bestValue, bestCycle, lastValue = 1,1,1#annealingAlgorithm(valuesList, weightList, capacity, blablabla)
            bestValues.append(bestValue)
            lastValues.append(lastValue)
            bestCycles.append(bestCycle)
            #end = time.time()
            #print('Elapsed time annealing: ')

        elif args.algorithm == 'genetic':
            if not args.populationSize or not args.numGenerations or not args.mutationRate:
                print('ERROR: Missing parameters for genetic algorithm')
                return
            #start = time.time()
            bestValue, bestCycle, lastValue = geneticAlgorithm(valuesList, weightList, capacity, args.populationSize, args.numGenerations, args.mutationRate)
            bestValues.append(bestValue)
            lastValues.append(lastValue)
            bestCycles.append(bestCycle)
            #end = time.time()
            #print('Elapsed time genetic: ') #resultado de tempo é relevante??
        
        contExec += 1
    #plot(bestValues, 'bestValues')


def plot(values, info):
    if info == 'bestValues':
        maxBest = max(values)
        print('max = ', maxBest)
        ranges = np.linspace(0, maxBest, 21)
        percent_ticks = np.linspace(0, 100, 21)  # De 0 a 100%, 21 ticks para 5% a cada ponto
        plt.xticks(ranges, [f'{int(p)}%' for p in percent_ticks])
        plt.yticks(np.linspace(0, 100, 21))
        weights = np.ones_like(values) / len(values) * 100
        plt.hist(values, bins=ranges, edgecolor='black', weights=weights)
        plt.title('Histograma com Faixas de Valores em Porcentagem')
        plt.xlabel('Porcentagem do Valor Máximo')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.savefig('histograma_faixas_percentual.png')
        plt.show()

#################################################################



def randomAlgorithm(values, weights, capacity):
    """Inserts random items in the knapsack until it tries 
    to insert an item that would exceed the capacity. """
    currentWeight = 0
    currentValue = 0
    knapsackValues = []
    while currentWeight < capacity and len(values):
        item = random.randint(0, len(values) - 1)
        if currentWeight + weights[item] <= capacity:
            currentWeight += weights[item]
            currentValue += values[item]
            knapsackValues.append(values[item])
            weights.pop(item)
            values.pop(item)
        else:
            break
    return currentValue, currentWeight, knapsackValues
            

if __name__ == '__main__':
    main()             