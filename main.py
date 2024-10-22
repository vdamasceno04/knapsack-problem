from argparse import ArgumentParser
import re
import random
import time

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
        valueList = random.sample(range(1, 9999), int(args.totalItems))
        weightList = random.sample(range(1, 9999), int(args.totalItems))

        if args.W is not None:
            capacity = args.W
        else:
            capacity = random.randint(1, 99999)

    print(valueList)
    print(weightList)
    print(capacity)

    if args.algorithm == 'random':
        start = time.time()
        #randomAlgorithm()
        end = time.time()
        print('Elapsed time random: ')

    elif args.algorithm == 'annealing':
        start = time.time()
        #annealingAlgorithm()
        end = time.time()
        print('Elapsed time annealing: ')

    elif args.algorithm == 'genetic':
        start = time.time()
        #geneticAlgorithm()
        end = time.time()
        print('Elapsed time genetic: ')

if __name__ == '__main__':
    main() 