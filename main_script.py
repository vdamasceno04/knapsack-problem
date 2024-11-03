import subprocess

#Script parameters
language = 'python3'
file = 'main.py'
itens_number = '20'
execution_number = '5'
seed = '10'

def execute_annealing(t_selector, random_start_flag):
    comand = [language, file, 'annealing', itens_number, '-seed', seed,  '-ex', execution_number, '-ts', t_selector, '-f', random_start_flag]
    result = subprocess.run(comand) 
    print(f"========================================================================\n  {' '.join(comand)} - EXECUTED\n========================================================================\n")

execute_annealing('1', 'True')
