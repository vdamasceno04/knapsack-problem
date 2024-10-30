import sys
import math
import numpy as np

#Parametros
#weights = [4, 2, 1, 3]
#values = [500, 400, 300, 450]
#bag_capacity = 5
#Resposta para o exemplo: 850

#weights = [5, 4, 6, 3, 7, 2, 8, 5, 1, 3, 4, 2, 9, 3, 5, 6, 4, 7, 8, 1]
#values = [10, 40, 30, 50, 20, 10, 60, 25, 15, 35, 45, 20, 70, 10, 15, 25, 30, 55, 75, 5]
#bag_capacity = 50
#Resposta para o exemplo: ?
####################################################################

def profit_calculate(state, weights, values, bag_capacity):
    if (sum(state * weights) <= bag_capacity):#Vejo se cabe na mochila
        return sum(state * values)
    else:
        return -1

def temperature_calculate(t_selector, max_temperature, time):
    if t_selector == 0:
        return max_temperature - time
    elif t_selector == 1:
        #COLOQUE NO GEOGEBRA PARA ENTENDER MELHOR
        #f: y=((10)/(2)) (cos(((π)/(10)) x)+1)
        angle = (math.pi*time)/max_temperature #Em rad entre(pi/2 < a < 3/2*pi)
        decay_factor = math.cos(angle) + 1
        return (max_temperature/2)*decay_factor
    elif t_selector == 2:
        if time != 0:
            decay_factor = math.exp(1/(2*time)) -1 
        else:
            decay_factor = 1
        return max_temperature*decay_factor
    else:
        print("VALOR DE TEMPERATURA INVALIDO")
        return -1 

def annealingAlgorithm(weights, values, bag_capacity, t_selector, random_start_flag):
    max_temperature = 1000
    
    time = 0
    states_lenght = len(weights)
    higher_profit, better_state, best_time  = 0, np.zeros(states_lenght, dtype=int), 0
    if random_start_flag == True:
        initial_state = np.random.randint(0, 2, states_lenght) #Criar etado inicial aleatorio. 
    else:
        initial_state = np. concatenate((np.array([1]), np.zeros(states_lenght-1, dtype=int))) #Começa no etado inicial que fica no teto(meio). 
    initial_state_profit = profit_calculate(initial_state, weights, values, bag_capacity)
    e_max = sys.float_info.max #round(math.exp(initial_state_profit), 3)(TODO)
    temperature = temperature_calculate(t_selector, max_temperature, time)
    while temperature > 100:#Nao pode ser > 0 para não estourar no calculo de e nas ultimas execuções(TODO) 
        sucessor_state =  np.random.randint(0, 2, states_lenght)#Pega proximo estado
        sucessor_state_profit = profit_calculate(sucessor_state, weights, values, bag_capacity)
        
        e_value = round(math.exp((sucessor_state_profit - initial_state_profit)/temperature), 3) 
        if (sucessor_state_profit > initial_state_profit or np.random.uniform(0, e_max) <= e_value):
            if sucessor_state_profit > higher_profit:
                higher_profit, better_state, best_time = sucessor_state_profit, sucessor_state, time

            initial_state, initial_state_profit = sucessor_state, sucessor_state_profit 

        time+=1
        temperature = temperature_calculate(t_selector, max_temperature, time)

    return higher_profit, best_time, initial_state_profit, time    
    #return higher_profit, better_state, initial_state_profit, initial_state, best_time   

#####################################################################################
#answer = algorithm(weights, values, bag_capacity, 1, False) 
#print(f'Maior lucro: {answer[0]}\n' 
#        f'Melhor estado: {answer[1]}\n'
#        f'Ultimo lucro: {answer[2]}\n'
#        f'Ultimo estado: {answer[3]}')
