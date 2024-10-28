import math
import numpy as np

#Parametros
#weights = [4, 2, 1, 3]
#values = [500, 400, 300, 450]
#bag_capacity = 5
#Resposta para o exemplo: 850

weights = [5, 4, 6, 3, 7, 2, 8, 5, 1, 3, 4, 2, 9, 3, 5, 6, 4, 7, 8, 1]
values = [10, 40, 30, 50, 20, 10, 60, 25, 15, 35, 45, 20, 70, 10, 15, 25, 30, 55, 75, 5]
bag_capacity = 50
#Resposta para o exemplo: 270


def profit_calculate(state, weights, values, bag_capacity):
    if (sum(state * weights) <= bag_capacity):#Vejo se cabe na mochila
        return sum(state * values)
    else:
        return -1

def temperature_calculate(temperature=None):
    max_temperature = 1000
    if temperature == None:
        return max_temperature
    else: 
        return temperature - 1

def algorithm(weights, values, bag_capacity):
    states_lenght = len(weights)
    higher_profit, better_state  = 0, np.zeros(states_lenght)
    initial_state = np.random.randint(0, 2, states_lenght) #Criar etado inicial aleatorio 
    initial_state_profit = profit_calculate(initial_state, weights, values, bag_capacity)
    
    max_temperature = temperature = temperature_calculate()
    while temperature >0:
        sucessor_state =  np.random.randint(0, 2, states_lenght)#Pega proximo estado
        while np.array_equal(sucessor_state, initial_state) == True: 
            sucessor_state =  np.random.randint(0, 2, states_lenght)#Pega proximo estado
        sucessor_state_profit = profit_calculate(sucessor_state, weights, values, bag_capacity)
        
        e_value = math.exp((initial_state_profit - sucessor_state_profit)/temperature) 
        if (sucessor_state_profit > initial_state_profit or np.random.randint(0,max_temperature+1) <= e_value):
            if sucessor_state_profit > higher_profit:
                higher_profit, better_state = sucessor_state_profit, sucessor_state

            initial_state, initial_state_profit = sucessor_state, sucessor_state_profit 

        temperature = temperature_calculate(temperature)
    
    return higher_profit, better_state, initial_state_profit, initial_state  

answer = algorithm(weights, values, bag_capacity) 
print(f'Maior lucro: {answer[0]}\n' 
        f'Melhor estado: {answer[1]}\n'
        f'Ultimo lucro: {answer[2]}\n'
        f'Ultimo estado: {answer[3]}')
