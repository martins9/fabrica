import csv

arq2=open('book2.csv','w')
with open("book1.csv", 'rU') as csvIN:

    outCSV=(line for line in csv.reader(csvIN, dialect='excel'))
    count=0

    arq2.writelines("Custom field(Test Sets association with a Test),Summary,Assignee,Reporter,Issue Type," + \
                    "Description,Test Type,Manual Test Steps" + "\n")

    print "[",
    for row in outCSV:
        count +=1
        if count > 1:

            a=row[1].split('\n')

            count1=0

            for teste in range(len(a)):
                count1 += 1
                if teste!=(len(a)-1):
                    print '{"index":'+str(count1)+','+'"step:"'+a[teste].decode('latin_1')+',"data:"","result":""},'
                else:
                    print '{"index":' + str(count1) + ',' + '"step:"' + a[teste].decode('latin_1') + ',"data:"",' + \
                          '"result":'+row[2].decode('latin_1')+'}'

            #print row[1].decode('latin_1').replace()
            #arq2.writelines(row[0]+","+row[1]+","+row[2]+"\n")
