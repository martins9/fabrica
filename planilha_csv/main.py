# Chama as func criadas pelo Dev
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

# Criando nome do arquivo csv
arq2 = open(n_demanda + '_final.csv', 'w')

# Abrindo arquivo csv e lendo as suas linhas
with open(arquivo, 'rU') as csvIN:
    outCSV = (line for line in csv.reader(csvIN, delimiter=';', dialect='excel'))

    # Primeira linha do arquivo final
    part0 = "Custom field(Test Sets association with a Test);Summary;Assignee;Reporter;Issue Type;Description;" + \
          "Test Type;Manual Test Steps"+"\n"
    arq2.writelines(part0)

    # Count para ignorar a primeira linha do arq original
    count = 0

    # Varrer linha a linha no arquivo outCSV
    for row in outCSV:
        count += 1

        # Condicional para ignorar a primeira linha
        if count > 1:
            # Quebrar linha da coluna 4
            a = row[4].split('\n')

            # Contador para index dos passos no cenário do testes.
            count1 = 0

            # Imputando os dados da part0
            part1=n_issue + ";" + row[3] + ";" + n_assigne + ";;" + "Test;"+'"'+row[2]+'"'+";Manual;"+'"[',
            arq2.writelines(part1)

            # Parte que retira --Manual Test Steps--
            for teste in range(len(a)):
                if teste != (len(a) - 1):
                    part2 = '{ ""index"": ' + str(count1) + ', ' + '""step"": ""' + a[teste].replace("- ","") + \
                            '"", ""data"": ""'+ row[0].split('.')[-1]+" e "+row[1]+ '"", ""result"": """" }, ',
                    arq2.writelines(part2)
                    #print part2
                else:
                    part3 = '{ ""index"": ' + str(count1) + ', ' + '""step"": ""' + a[teste].replace("- ","") + \
                            '"", ""data"": ""'+ row[0].split('.')[-1]+" e "+row[1]+ '"", ""result"": ""' + row[5] + '"" } ]"',
                    arq2.writelines(part3)
                    #print part3
                    arq2.writelines("\n")
                count1 += 1

# Deletar arquivo
#deletar(n_demanda+"_1.csv")