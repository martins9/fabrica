import sys,os,csv,re

def deletar(c):
    os.remove(c)

def tirar_tracos(d):
    try:
        arq3 = open(d + '_1.csv', 'w')
        with open(d + '_2.csv', 'rU') as f:
            text = (line for line in csv.reader(f,delimiter='|',dialect='excel'))
            for row in text:
                #row_new = row[2].split("\n")
                #row_new_1 =row[3].split("\n")

                print row[0]

                #arq3.writelines(row_new_2)

        arq3.close()
        f.close()
    except OSError:
        print "Arquivo vazio"
        sys.exit()

def substituir_pontos(e,f):
    arq4 = open(e + '_1.csv', 'w')
    with open(f, 'rU') as f:
        outCSV = (line for line in csv.reader(f, delimiter=';', dialect='excel'))

        part0 = "Custom field(Test Sets association with a Test);Summary;Assignee;Reporter;Issue Type;Description;" + \
                "Test Type;Manual Test Steps" + "\n"
        print part0

        count=0
        for row in outCSV:
            count += 1
            if count > 1:

                part1 = n_issue + ";" + row[0] + ";" + n_assigne + ";;" + "Test;;Manual;" + '"[',
                a = row[0].split('\n')
                for i in a:
                    b = re.sub('(?<=\d),(?=\d)', '.', i)
                    final1=b+','+row[1]+','
                    arq4.writelines(final1)

                b = row[2].split('\n')
                for t in b:
                    row[2].replace("-","")



    arq4.close()
    f.close()

def substituir_ponto_virgula(b):
    try:
        arq1=open(b + '_1.csv','r')
        arq2=open(b + '_2.csv','w')

        for line in arq1:
            new_lines=line.replace(";",",")
            arq2.writelines(new_lines)

        arq1.close()
        arq2.close()
    except OSError:
        print "Arquivo vazio"
        sys.exit()