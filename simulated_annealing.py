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

def annealingAlgorithm(weights, values, bag_capacity, t_selector, random_start_flag):
    max_temperature = 1000
    time = 0
    states_lenght = len(weights)
    higher_profit, best_time  = 0, 0
    
    if random_start_flag == True:
        initial_state = np.random.randint(0, 2, states_lenght) #Random state
    else:
        initial_state = np.zeros(states_lenght, dtype=int) #All zeros state, global minimum
    
    initial_state_profit = profit_calculate(initial_state, weights, values, bag_capacity)
    temperature = temperature_calculate(t_selector, max_temperature, time)
    while temperature >= 1:#VER SE ESSA CONDICAO AINDA É NECESSÁRIA 
        temperature = temperature_calculate(t_selector, max_temperature, time)
        
        sucessor_state =  np.random.randint(0, 2, states_lenght)#New random state
        sucessor_state_profit = profit_calculate(sucessor_state, weights, values, bag_capacity)
        
        if sucessor_state_profit == -1:
            continue
        
        delta = sucessor_state_profit - initial_state_profit
        if delta < 0:
            e_value = round(math.exp(delta/temperature), 3) #calculate e only if next move is worse
        if (delta >= 0 or np.random.uniform(0, 1) <= e_value): 
            #if next state is better or random number is in range of e_value
            initial_state, initial_state_profit = sucessor_state, sucessor_state_profit 
            if sucessor_state_profit > higher_profit:
                higher_profit, best_time = sucessor_state_profit, time
        time += 1
    return higher_profit, best_time, initial_state_profit, (time -1)   

def profit_calculate(state, weights, values, bag_capacity):
    if (sum(state * weights) <= bag_capacity):#if fits in the bag
        return sum(state * values)
    else:
        return -1

def temperature_calculate(t_selector, max_temperature, time):
    if t_selector == 0:
        return max_temperature - time
    elif t_selector == 1:
        if time != 0:
            decay_factor = math.exp(1/(2*time)) -1 #TESTAR ADICIONAR ALGUMA COEFICIENTE
        else:
            decay_factor = 1
        return max_temperature*decay_factor
    else:
        print("Invalid temperature selector")
        return -1 