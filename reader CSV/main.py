from tratar_csv import *

def main():
    
    #tratamento do csv
    files_array = listdir()
    regex = r"RELATORIO_PRODUCAO_\d+_\d+_\d+_\d+.CSV"
    for file in files_array:
        if(re.search(regex,file)):
            csv_func(file)
    
    #acumulado mensal do mes do arquivo passado como parametro
    array = get_acumulado(files_array[0])
    print(array[0], array[1])
    print(array[0]/array[1])

    #media de corridas por turno no mes
    media = media_corrida_turno_mes(listdir(),3,2020)
    print("Numero de corridas: {0}\nNumero de turnos:{1}\nMedia: {2:.2f}"
    .format(media[0],media[1],media[0]/media[1]))

    #quantidade de corridas por cada turma no mes
    resultado = get_turma_freq_mes(listdir(),3,2020)
    print(resultado)

    csv = csv_reader("RELATORIO_PRODUCAO_15_3_2020_21_.csv")
    print(media_dia_ligado(csv))
    return 0


def get_numero_corridas(file):
    matrix = []
    matrix = csv_reader(file)
    return len(matrix) - 1 


def media_corrida_turno_mes(files,mes,ano):
    total = 0
    n = 0
    regex = generate_month_year_regex(mes,ano)
    for file in files:
        if(re.search(regex,file)):
            total = total + get_numero_corridas(file)
            n = n + 1
    return [total,n]


def get_turma_freq_dia(matrix,resultado):
    for i in range(1,len(matrix)): 
        turma = matrix[i][1]
        if(turma == "0"):
            continue
        if(turma in resultado.keys()):
            resultado[turma] = resultado[turma] + 1
        else:
            resultado[turma] = 1
    return resultado


def get_turma_freq_mes(files,mes,ano):
    resultado = {}
    regex = generate_month_year_regex(mes,ano)
    for file in files:
        if(re.search(regex,file)):
            matrix = []
            matrix = csv_reader(file)
            get_turma_freq_dia(matrix,resultado)
    return resultado


def get_acumulado(file):
    date = get_date(file)
    dia = date[0]
    mes = date[1]
    ano = date[2]
    hora = date[3]
    files_array = listdir()
    regex = generate_month_year_regex(mes,ano)
    acumulado = 0.0
    n = 0
    for i in files_array:
        if(re.search(regex,i)):
            matrix = csv_reader(i)
            novo_valor = float(matrix[len(matrix)-1][3])
            if(novo_valor != 0):
                n = n + 1
                acumulado = acumulado + novo_valor
    return [acumulado,n]


def generate_month_year_regex(month,year):
    formato = "{0}_{1}".format(month,year)
    regex = r"\d+_" + re.escape(formato) + r"_\d+_.csv"
    return regex



def get_power_on(array):
    return float(array[17])

def get_power_off(array):
    return float(array[16])

def get_ttt(array):
    return float(array[18])

def media_dia_ligado(csv):
    csv.pop(0)
    total_power_on = 0
    total_power_off = 0
    total_ttt = 0
    for corrida in csv:
        total_power_on = total_power_on + get_power_on(corrida)
        total_power_off = total_power_off + get_power_off(corrida)
        total_ttt = total_ttt + get_ttt(corrida)
    return total_power_on

main()