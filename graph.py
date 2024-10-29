import matplotlib.pyplot as plt
import numpy as np

#Plotar função de T
#Histograma
#Resultados mudando no tempo

def plot(values, info, file_name='histograma_faixas_percentual.png'):
    #if info == 'bestValues':
        maxBest = max(values)
        print('max = ', maxBest)
        ranges = np.linspace(0, maxBest, 21)
        percent_ticks = np.linspace(0, 100, 21)  # De 0 a 100%, 21 ticks para 5% a cada ponto
        plt.xticks(ranges, [f'{int(p)}%' for p in percent_ticks])
        plt.yticks(np.linspace(0, 100, 21))
        weights = np.ones_like(values) / len(values) * 100
        plt.hist(values, bins=ranges, edgecolor='black', weights=weights)
        plt.title('Histograma com Faixas de Valores em Porcentagem')
        plt.xlabel('Porcentagem do Valor Máximo')
        plt.ylabel('Frequência')
        plt.grid(True)
        plt.savefig("images/" + file_name)
        #plt.show()#Comentar para não travar execução do script