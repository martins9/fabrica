import csv
from t_limpeza.t_function_limpeza import tirar_pontos_virgulas

n_issue=raw_input("Insira numero do Test Set:")
n_assigne=raw_input("Insire Assigne:")

arquivo='8921.csv'
tirar_pontos_virgulas(arquivo)

arq2 = open('8921_final.csv', 'w')
with open("8921_1.csv", 'rU') as csvIN:

    outCSV=(line for line in csv.reader(csvIN, dialect='excel'))

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