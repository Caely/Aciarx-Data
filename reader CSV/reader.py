import csv
import re

#le o csv e atribui na matrix matrix
with open("RELATORIO_PRODUCAO_17_3_2020_6.CSV") as file:
    csv = csv.reader(file,delimiter=',')
    matrix = []
    for i in csv:
        matrix.append(i)

#remove espacos vazios
while([] in matrix):
    matrix.remove([])


titles = []
titles = str(matrix[0]).split(";\\t")
titles = re.findall(r'([A-Zk\/]+[\s\/_]?[A-Z0-9]*\s?\(?[\/\sA-Z%a-z0-9]+\)?)', str(matrix[0]))
carbono = re.findall(r'([A-Zk\/]+[\s\/_]?[A-Z0-9]*\s?\(?[\/\sA-Z%a-z0-9]+\)?)', str(matrix[2]))
titles.append(carbono[0])
#for i in titles:
 #   print(i)

aux = ",".join(matrix[3])
valores = []
valores = re.findall(r'([A-Z]*|[\d]*[,]?[\d]*)', aux)

while('' in valores):
    valores.remove('')

for i in valores:
    print(i)