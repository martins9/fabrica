# -*- coding: utf-8 -*-

import csv
from t_limpeza.t_function_limpeza import tirar_pontos_virgulas

# Insercao de informacoes
n_demanda=raw_input("Insira o numero da demanda:")
arquivo=raw_input("Insira o nome do arquivo:")
n_issue=raw_input("Insira numero do Test Set:")
n_assigne=raw_input("Insire Assigne:")

# Tirando as virgulas do arquivo
tirar_pontos_virgulas(arquivo,n_demanda)

arq2 = open(n_demanda+'_final.csv', 'w')
with open(n_demanda+"_1.csv", 'rU') as csvIN:

    outCSV=(line for line in csv.reader(csvIN, dialect='excel'))

    for row in outCSV:
        print row

    print "Custom, field(Test Sets association with a Test),Summary,Assignee,Reporter,Issue Type,Description," + \
            "Test Type, Manual Test Steps"

    count = 0
    for row in outCSV:
        count += 1
        if count > 1:
            a=row[1].split('\n')
            count1=0
            for teste in range(len(a)):
                count1 += 1
                if teste!=(len(a)-1):
                    print n_issue+","+row[0]+","+n_assigne+",,"+"Test,,Manual,"+'[{"index":'+str(count1)+','+'"step:"'+a[teste].decode('latin_1')+'","data:"","result":""},',
                else:
                    print '{"index":' + str(count1) + ',' + '"step:"' + a[teste].decode('latin_1') + '","data:"",' + \
                          '"result":'+row[2].decode('latin_1')+'}]'+'\n',

            #print row[1].decode('latin_1').replace()
            #arq2.writelines(row[0]+","+row[1]+","+row[2]+"\n")