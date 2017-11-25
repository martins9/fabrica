import sys,os

def tirar_pontos_virgulas(a,b):
    try:
        arq1=open(a,'r')
        arq2=open(b+'_1.csv','w')

        for line in arq1:
            new_lines=line.replace(";",",")
            arq2.writelines(new_lines)

        arq1.close()
        arq2.close()
    except OSError:
        print "Arquivo vazio"
        sys.exit()

def deletar(c):
    os.remove(c)