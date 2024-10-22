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

    if args.algorithm == 'random':
        start = time.time()
        value, weight, items = randomAlgorithm(valuesList, weightList, capacity)
        end = time.time()
        print('Elapsed time random: ', end - start)
        print('Value: ', value)
        print('Weight: ', weight)
        print('Items: ', items)

    elif args.algorithm == 'annealing':
        start = time.time()
        #annealingAlgorithm()
        end = time.time()
        print('Elapsed time annealing: ')

    elif args.algorithm == 'genetic':
        if not args.populationSize or not args.numGenerations or not args.mutationRate:
            print('ERROR: Missing parameters for genetic algorithm')
            return
        start = time.time()
        geneticAlgorithm(valuesList, weightList, capacity, args.populationSize, args.numGenerations, args.mutationRate)
        end = time.time()
        print('Elapsed time genetic: ')

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