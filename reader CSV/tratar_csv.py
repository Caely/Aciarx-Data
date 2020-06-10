import csv
import re
from os import listdir

def csv_func(file):
    matrix = []
    matrix = csv_reader(file)
    remove_empty_valors(matrix)
    titles = get_titles(matrix)
    table = get_all_valors(matrix)
    treat_valors(table,titles)
    name = get_new_file_name(file)
    write_csv(name,table,titles)


def csv_reader(file):
    with open(file) as fp:
        file = csv.reader(fp,delimiter=',')
        csv_array = []
        for i in file:
            csv_array.append(i)
        return csv_array


def remove_empty_valors(matrix):
    while([] in matrix):
        matrix.remove([])


def get_titles(matrix):
    titles = []
    titles = str(matrix[0]).split(";\\t")
    titles = re.findall(r'([A-Zk\/]+[\s\/_]?[A-Z0-9]*\s?\(?[\/\sA-Z%a-z0-9]+\)?)', str(matrix[0]))
    carbono = re.findall(r'([A-Zk\/]+[\s\/_]?[A-Z0-9]*\s?\(?[\/\sA-Z%a-z0-9]+\)?)', str(matrix[2]))
    titles.append(carbono[0])
    return titles


def get_valors(matrix):
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


def get_all_valors(matrix):
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


def treat_valors(table,titles):

    for i in range(len(table)):
        for j in range(len(table[i])):
            if('.' in str(table[i][j]) and '%' in str(titles[j])):
                splite = table[i][j].split('.')
                if(splite[0].isdigit() and splite[1].isdigit()):
                    if(float(table[i][j]) > 100):
                        table[i][j] = 100.00


def write_csv(name,table,titles):
    table.insert(0,titles)
    with open(name,"w") as file:
        csv_file = csv.writer(file)
        for i in table:
            csv_file.writerow(i)


def get_date(file):
    date = re.findall(r'\d+_\d+_\d+_\d+', file)
    date = date[0].split('_')
    return date


def get_new_file_name(file):
    time = get_date(file)
    dia = time[0]
    mes = time[1]
    ano = time[2]
    hora = time[3]
    new_name = "RELATORIO_PRODUCAO_{}_{}_{}_{}_.csv".format(dia,mes,ano,hora)
    return new_name