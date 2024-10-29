import simulated_annealing as sa
import genetic_algorithm as ga
import graph as gp 

##PARAMETROS##############################################################################
weights = [5, 4, 6, 3, 7, 2, 8, 5, 1, 3, 4, 2, 9, 3, 5, 6, 4, 7, 8, 1]
values = [10, 40, 30, 50, 20, 10, 60, 25, 15, 35, 45, 20, 70, 10, 15, 25, 30, 55, 75, 5]
bag_capacity = 50
##########################################################################################

def execute_and_save(file_path, execution_number, algorithm, param1, param2, param3=None):
    with open(file_path, 'w') as file:
        for i in range(execution_number):
            if algorithm == 0:
                result = sa.algorithm(weights, values, bag_capacity, t_selector=param1, random_start_flag=param2)
                #higher_profit[0], better_state[1], last_state_profit[2], last_state[3]
                result = f"{i+1}; {result[0]}; {result[2]};\n"
            elif algorithm == 1:
                result = ga.geneticAlgorithm(valuesList=values, weightList=weights, capacity=bag_capacity, populationSize=param1, numGenerations=param2, mutationRate=param3)
                #(TODO)COLOCAR UMA STRING COMO A QUE ESTA A CIMA COM OS VALORES DE INTERESE SEPARADOS POR ;
            file.write(result)

def read_and_plot(file_path, algorithm):
    file_name = file_path.split('/')[-1]
    if algorithm == 0 :
        higher_profit = [] 
        last_state_profit = []
        with open(file_path, 'r') as file:
            for line in file:
                result = line.split(';')
                higher_profit     += [int(result[1])]
                last_state_profit += [int(result[2])]
        gp.plot(higher_profit, 'bestValues','histograma_faixas_percentual_' + file_name + '_maior.png')
        gp.plot(last_state_profit, 'bestValues','histograma_faixas_percentual_' + file_name + '_ultimo.png')
    elif algorithm == 1:
        #higher_profit = [] 
        with open(file_path, 'r') as file:
            for line in file:
                #result = line.split(';')
                #higher_profit     += [int(result[1])]
                #(TODO)PRENCHER AQUI COM OS PARAMETRO DE INTERESE COMO O EXEMPLO A CIMA
                print("TODO")
        #gp.plot(higher_profit, 'bestValues','histograma_faixas_percentual_' + file_name + '_maior.png')
    
##########################################################################################
execution_number = 1000
#simulated_annealing
execute_and_save('txts/sa_afim_no',  execution_number, 0, 0, False)
read_and_plot('txts/sa_afim_no', 0)
print("TERMINOU 1")

execute_and_save('txts/sa_afim_yes', execution_number, 0, 0, True)
read_and_plot('txts/sa_afim_yes', 0)
print("TERMINOU 2")

execute_and_save('txts/sa_cos_no',   execution_number, 0, 1, False)
read_and_plot('txts/sa_cos_no', 0)
print("TERMINOU 3")

execute_and_save('txts/sa_cos_yes',  execution_number, 0, 1, True)
read_and_plot('txts/sa_cos_yes', 0)
print("TERMINOU 4")
#genetic_algorithm
#execute_and_save('txts/NOME_DO ARQUIVO_AQUI',  execution_number, 1, PARAM1, PARAM2, PARAM3)
#(TODO)PRENCHER AQUI COM AS TROCAS DE PARAMETRO DE INTERESE COMO O EXEMPLO A CIMA




    
    
    