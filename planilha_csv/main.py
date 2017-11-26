import csv
from t_limpeza.t_function_limpeza import tirar_pontos_virgulas,deletar

# Insercao de informacoes
n_demanda = raw_input("Insira o numero da demanda:")
arquivo = raw_input("Insira o nome do arquivo:")
n_issue = raw_input("Insira numero do Test Set:")
n_assigne = raw_input("Insire Assigne:")

# Tirando as virgulas do arquivo
tirar_pontos_virgulas(arquivo, n_demanda)

arq2 = open(n_demanda + '_final.csv', 'w')
with open(n_demanda + "_1.csv", 'rU') as csvIN:
    outCSV = (line for line in csv.reader(csvIN, dialect='excel'))

    part0 = "Custom field(Test Sets association with a Test);Summary;Assignee;Reporter;Issue Type;Description;" + \
          "Test Type;Manual Test Steps"+"\n"
    arq2.writelines(part0)

    count = 0
    for row in outCSV:
        count += 1
        if count > 1:
            a = row[1].split('\n')
            count1 = 0

            part1=n_issue + ";" + row[0] + ";" + n_assigne + ";;" + "Test;;Manual;"+'"[',
            arq2.writelines(part1)

            for teste in range(len(a)):
                if teste != (len(a) - 1):
                    part2 = '{ ""index"": ' + str(count1) + ', ' + '""step"": ""' + a[teste] + '"", ""data"": """", ""result"": """" }, ',
                    arq2.writelines(part2)
                else:
                    part3 = '{ ""index"": ' + str(count1) + ', ' + '""step"": ""' + a[teste] + '"", ""data"": """", ""result"": ""' + \
                            row[2].replace("\n",". ") + '"" } ]"',
                    arq2.writelines(part3)
                    arq2.writelines("\n")
                count1 += 1

# Deletar arquivo
deletar(n_demanda+"_1.csv")

csvIN.close()
arq2.close()