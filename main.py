from argparse import ArgumentParser

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

if __name__ == '__main__':
    main() 