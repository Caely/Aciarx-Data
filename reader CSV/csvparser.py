import csv
import re

def main():
    matrix = []
    matrix = csvReader("RELATORIO_PRODUCAO_17_3_2020_6.CSV")
    cleanMatrix(matrix)
    titles = getTitles(matrix)
    #valors = getValors(matrix)
    table = getALLValors(matrix)
    treatValors(table,titles)
    writeCSV(table,titles)


def csvReader(file):
    with open(file) as fp:
        file = csv.reader(fp,delimiter=',')
        matrix = []
        for i in file:
            matrix.append(i)
        return matrix


def cleanMatrix(matrix):
    while([] in matrix):
        matrix.remove([])


def getTitles(matrix):
    titles = []
    titles = str(matrix[0]).split(";\\t")
    titles = re.findall(r'([A-Zk\/]+[\s\/_]?[A-Z0-9]*\s?\(?[\/\sA-Z%a-z0-9]+\)?)', str(matrix[0]))
    carbono = re.findall(r'([A-Zk\/]+[\s\/_]?[A-Z0-9]*\s?\(?[\/\sA-Z%a-z0-9]+\)?)', str(matrix[2]))
    titles.append(carbono[0])
    return titles


def getValors(matrix):
    aux = ",".join(matrix[3])
    valores = []
    valores = re.findall(r'([A-Z]*|[\d]*[,]?[\d]*)', aux)

    while('' in valores):
        valores.remove('')

    return valores


def getNruns(matrix):
    size = 0
    head = 3
    while(bool(re.search(r'[\d]{5,10}',str(matrix[head])))):
        head = head + 1
    size = head - 3
    return size


def getALLValors(matrix):
    table = []
    size = getNruns(matrix)
    for i in range(3,size+3):
        aux = ".".join(matrix[i])
        valores = []
        valores = re.findall(r'([A-Z]*|[\d]*[.]?[\d]*)', aux)
        while('' in valores):
            valores.remove('')
        table.append(valores)
    return table


def treatValors(table,titles):

    for i in range(len(table)):
        for j in range(len(table[i])):
            if('.' in str(table[i][j]) and '%' in str(titles[j])):
                splite = table[i][j].split('.')
                if(splite[0].isdigit() and splite[1].isdigit()):
                    if(float(table[i][j]) > 100):
                        table[i][j] = 100.00


def writeCSV(table,titles):
    table.insert(0,titles)
    with open("teste.csv","w") as file:
        csv_file = csv.writer(file)
        for i in table:
            csv_file.writerow(i)


main()