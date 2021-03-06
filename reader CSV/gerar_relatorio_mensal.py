import csv
import re
from os import listdir
from main import *
from operator import itemgetter

def gerar_relatorio_mensal(mes,ano):
    file_name = "RELATORIO_MEDIA_" + str(mes) + '_' + str(ano) + ".csv"
    titulos = ["Dia","Produçāo Acumulada","N Corridas","Pon (Min)","Poff (Min)","Pon Extra (Min)", "Poff Extra (Min)",
    "Sucata (T)","Potencia (MW)","Potencia (kWh)","kWh/T Acumulado", "kwh/min Acumulado",
    "Lan O2 (Nm3)","Carvāo (Kg)","CJ O2 (Nm3)","CJ GN (Nm3)"]
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
    sucata = get_sucata(table)
    potencia_mw = get_potencia_mw(table)
    potencia_kwh = get_potencia_kwh(table)
    kwh_t = get_acumulado_dia_kwh_t(table)
    kwh_min = get_acumulado_dia_kwh_min(table)
    lan_o2 = get_lan_o2(table)
    carvao = get_carvao(table)
    cj_o2 = get_cj_o2(table)
    cj_gn = get_cj_gn(table)

    index = check_dia(csv,dia)
    if(index == -1):
        valores.append(dia)
        valores.append(acumulado)
        valores.append(n_corridas)
        valores.append(pon_poff_values[0])
        valores.append(pon_poff_values[1])
        valores.append(pon_poff_values[2])
        valores.append(pon_poff_values[3])
        valores.append(sucata)
        valores.append(potencia_mw)
        valores.append(potencia_kwh)
        valores.append(kwh_t)
        valores.append(kwh_min)
        valores.append(lan_o2)
        valores.append(carvao)
        valores.append(cj_o2)
        valores.append(cj_gn)

        csv.append(valores)
    else:
        csv[index][1] = float(csv[index][1]) + float(acumulado)
        csv[index][2] = float(csv[index][2]) + float(n_corridas)
        csv[index][3] = float(csv[index][3]) + float(pon_poff_values[0])
        csv[index][4] = float(csv[index][4]) + float(pon_poff_values[1])
        csv[index][5] = float(csv[index][5]) + float(pon_poff_values[2])
        csv[index][6] = float(csv[index][6]) + float(pon_poff_values[3])
        csv[index][7] = float(csv[index][7]) + float(sucata)
        csv[index][8] = float(csv[index][8]) + float(potencia_mw)
        csv[index][9] = float(csv[index][9]) + float(potencia_kwh)
        csv[index][10] = float(csv[index][10]) + float(kwh_t)
        csv[index][11] = float(csv[index][11]) + float(kwh_min)
        csv[index][12] = float(csv[index][12]) + float(lan_o2)
        csv[index][13] = float(csv[index][13]) + float(carvao)
        csv[index][14] = float(csv[index][14]) + float(cj_o2)
        csv[index][15] = float(csv[index][15]) + float(cj_gn)

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


#pode transformar em um metodo so
def get_sucata(table):
    total_sucata = 0
    size = len(table)
    for i in range(0,size):
        total_sucata = total_sucata + float(table[i][4])
    return total_sucata


def get_potencia_mw(table):
    total_potencia_mw = 0
    size = len(table)
    for i in range(0,size):
        total_potencia_mw = total_potencia_mw + float(table[i][6])
    return total_potencia_mw


def get_potencia_kwh(table):
    total_potencia_kwh = 0
    size = len(table)
    for i in range(0,size):
        total_potencia_kwh = total_potencia_kwh + float(table[i][7])
    return total_potencia_kwh

def get_lan_o2(table):
    total= 0
    size = len(table)
    for i in range(0,size):
        total = total + float(table[i][12])
    return total

def get_carvao(table):
    total= 0
    size = len(table)
    for i in range(0,size):
        total = total + float(table[i][13])
    return total

def get_cj_o2(table):
    total= 0
    size = len(table)
    for i in range(0,size):
        total = total + float(table[i][14])
    return total

def get_cj_gn(table):
    total= 0
    size = len(table)
    for i in range(0,size):
        total = total + float(table[i][15])
    return total
#

#metodos acumulados podem ser apenas 1 ao se passar o indice
def get_acumulado_dia_kwh_t(table):
    size = len(table)
    acumulado_dia = table[size-1][9]
    return acumulado_dia

def get_acumulado_dia_kwh_min(table):
    size = len(table)
    acumulado_dia = table[size-1][11]
    return acumulado_dia


gerar_relatorio_mensal(3,2020)