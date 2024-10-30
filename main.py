from argparse import ArgumentParser
import re
import random
import time

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
    bestValues = []
    lastValues = []
    bestCycles = []
    while(contExec < args.exec):
        if args.algorithm == 'annealing':
            bestValue, bestCycle, lastValue = 1,1,1#annealingAlgorithm(valuesList, weightList, capacity, blablabla)
            bestValues.append(bestValue)
            lastValues.append(lastValue)
            bestCycles.append(bestCycle)

        elif args.algorithm == 'genetic':
            if not args.populationSize or not args.numGenerations or not args.mutationRate:
                print('ERROR: Missing parameters for genetic algorithm')
                return
            bestValue, bestCycle, lastValue = geneticAlgorithm(valuesList, weightList, capacity, args.populationSize, args.numGenerations, args.mutationRate)
            bestValues.append(bestValue)
            lastValues.append(lastValue)
            bestCycles.append(bestCycle)
            
        contExec += 1
    print('\nBest value: ', bestValues)
    print('Best cycle: ', bestCycles)
    print('Last value: ', lastValues)
    if args.algorithm == 'genetic':
        cycles = args.numGenerations
        testName = 'mr'+str(args.mutationRate)+'_ps'+str(args.populationSize)+'_ng'+str(args.numGenerations)+'.png'

    elif args.algorithm == 'annealing':
        #PARAMETRO DE CICLOS 
        #cycles =
        #testName =
        cycles = 1
        testName = 'xxxxx.png'
    graph.plot(bestValues, 'bestValues', cycles, 'best'+testName)
    graph.plot(lastValues, 'lastValues', cycles, 'last'+testName)
    graph.plot(bestCycles, 'bestCycles', cycles, 'cycle'+testName)
#################################################################
import graph

if __name__ == '__main__':
    main()             