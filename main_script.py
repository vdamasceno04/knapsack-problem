import subprocess

#Script parameters
language = 'python3'
file = 'main.py'
itens_number = '30' #ALTERAR NUMERO DE ITENS AQUI(TODO)
execution_number = '1000'
seed = '10'

def execute_annealing(t_selector, random_start_flag):
    if random_start_flag == 'False':
        comand = [language, file, 'annealing', itens_number, '-seed', seed,  '-ex', execution_number, '-ts', t_selector]
    elif random_start_flag == 'True':
        comand = [language, file, 'annealing', itens_number, '-seed', seed,  '-ex', execution_number, '-ts', t_selector, '-f']
    subprocess.run(comand) 
    print(f"========================================================================\n  {' '.join(comand)} - EXECUTED\n========================================================================\n")

execute_annealing('0', 'False')
execute_annealing('1', 'False')
execute_annealing('2', 'False')
execute_annealing('0', 'True')
execute_annealing('1', 'True')
execute_annealing('2', 'True')

