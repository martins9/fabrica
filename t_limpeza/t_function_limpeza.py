import sys

def tirar_pontos_virgulas(a):
    try:
        arq1=open(a,'r')
        arq2=open('8921_1.csv','w')

        for line in arq1:
            new_lines=line.replace(";",",")
            arq2.writelines(new_lines)

        arq1.close()
        arq2.close()
    except OSError:
        print "Arquivo vazio"
        sys.exit()