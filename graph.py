import matplotlib.pyplot as plt
import numpy as np

#Plotar função de T
#Histograma
#Resultados mudando no tempo

def plot(values, info, cycles,file_name='teste1.png'):
    maxBest = max(values)
    print('max = ', maxBest)
    if info == 'bestValues':
        ranges = np.linspace(0, maxBest, 21)
        percent_ticks = np.linspace(0, 100, 21)  # De 0 a 100%, 21 ticks para 5% a cada ponto
        plt.xticks(ranges, [f'{int(p)}%' for p in percent_ticks])
        plt.yticks(np.linspace(0, 100, 21))
        weights = np.ones_like(values) / len(values) * 100
        plt.hist(values, bins=ranges, edgecolor='black', weights=weights)
        plt.title('Melhores Valores')
        plt.xlabel('Porcentagem do Valor Máximo')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.savefig("images/" + file_name)
        plt.show()#Comentar para não travar execução do script

    elif info == 'lastValues':
        ranges = np.linspace(0, maxBest, 21)
        percent_ticks = np.linspace(0, 100, 21)  # De 0 a 100%, 21 ticks para 5% a cada ponto
        plt.xticks(ranges, [f'{int(p)}%' for p in percent_ticks])
        plt.yticks(np.linspace(0, 100, 21))
        weights = np.ones_like(values) / len(values) * 100
        plt.hist(values, bins=ranges, edgecolor='black', weights=weights)
        plt.title('Últimos Valores')
        plt.xlabel('Porcentagem do Valor Máximo')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.savefig("images/" + file_name)
        plt.show()#Comentar para não travar execução do script

    elif info == 'bestCycles':
        ranges = np.linspace(0, maxBest, 21)
        percent_ticks = np.linspace(0, 100, 21)  # De 0 a 100%, 21 ticks para 5% a cada ponto
        plt.xticks(ranges, [f'{int(p)}%' for p in percent_ticks])
        plt.yticks(np.linspace(0, 100, 21))
        weights = np.ones_like(values) / len(values) * 100
        plt.hist(values, bins=ranges, edgecolor='black', weights=weights)
        plt.title('Últimos Valores')
        plt.xlabel('Porcentagem do Total de Ciclos')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.savefig("images/" + file_name)
        plt.show()#Comentar para não travar execução do script