#import csv
from t_limpeza.t_function_limpeza import *

# Insercao de informacoes
n_demanda = raw_input("Insira o numero da demanda:")
arquivo = raw_input("Insira o nome do arquivo:")
n_issue = raw_input("Insira numero do Test Set:")
n_assigne = raw_input("Insire Assigne:")

# Substituir virgula por ponto
#substituir_pontos(n_demanda,arquivo)

# Substituir virgulas do arquivo por ponto
#substituir_ponto_virgula(n_demanda)

# Tirando tracos do arquivo
#tirar_tracos(n_demanda)

arq2 = open(n_demanda + '_final.csv', 'w')
with open(arquivo, 'rU') as csvIN:
    outCSV = (line for line in csv.reader(csvIN, delimiter=';', dialect='excel'))

    for row in outCSV:
        print row[0]