import csv
import re
from os import listdir
from main import *
from operator import itemgetter

def gerar_relatorio_mensal(mes,ano):
    file_name = "RELATORIO_MEDIA_" + str(mes) + '_' + str(ano) + ".csv"
    titulos = ["Dia","Produçāo Acumulada","N Corridas","Pon (Min)","Poff (Min)","Pon Extra (Min)", "Poff Extra (Min)"]
    valores = []
    table = []
    files_array = listdir()
    regex = generate_month_year_regex(3,2020)
    for file in files_array:
        if(re.search(regex,file)):
            valores = get_medias_dia(file,valores)
    valores.sort(key=itemgetter(0))
    write_csv(file_name,valores,titulos)


def get_medias_dia(file,csv):
    valores = []
    date = get_date(file)
    dia = date[0]
    table = csv_reader(file)
    acumulado = get_acumulado_dia(table)
    n_corridas = get_numero_corridas_dia(table)
    pon_poff_values = get_pon_poff(table,29.5,9.5)
    index = check_dia(csv,dia)
    if(index == -1):
        valores.append(dia)
        valores.append(acumulado)
        valores.append(n_corridas)
        valores.append(pon_poff_values[0])
        valores.append(pon_poff_values[1])
        valores.append(pon_poff_values[2])
        valores.append(pon_poff_values[3])
        csv.append(valores)
    else:
        csv[index][1] = float(csv[index][1]) + float(acumulado)
        csv[index][2] = float(csv[index][2]) + float(n_corridas)
        csv[index][3] = float(csv[index][3]) + float(pon_poff_values[0])
        csv[index][4] = float(csv[index][4]) + float(pon_poff_values[1])
        csv[index][5] = float(csv[index][5]) + float(pon_poff_values[2])
        csv[index][6] = float(csv[index][6]) + float(pon_poff_values[3])
    return csv


def get_acumulado_dia(table):
    size = len(table)
    acumulado_dia = table[size-1][3]
    return acumulado_dia

def get_numero_corridas_dia(table):
    numero = len(table) - 1
    return numero

def get_pon_poff(csv,meta_pon,meta_poff):
    csv.pop(0)
    total_power_on = 0
    total_power_off = 0
    for corrida in csv:
        total_power_on = total_power_on + get_power_on(corrida)
        total_power_off = total_power_off + get_power_off(corrida)
   
    n_corridas = len(csv)
    meta_dia_pon = meta_pon * n_corridas
    meta_dia_poff = meta_poff * n_corridas
    
    tempo_extra_pon = meta_dia_pon - total_power_on
    tempo_extra_poff = meta_dia_poff - total_power_off
    
    return [total_power_on,total_power_off,tempo_extra_pon,
    tempo_extra_poff]


def check_dia(valores, dia):
    if(valores == []):
        return -1

    for i in range(0,len(valores)):
        if(valores[i][0] == dia):
            return i
    return -1



gerar_relatorio_mensal(3,2020)