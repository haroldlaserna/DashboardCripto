import numpy as np
import pandas as pd

def average_std_month(data,columna):
    mes = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
            'Diciembre']
    average = []
    std = []
    for i in range(len(mes)):
        calculate = data.loc[data.Mes == mes[i]]
        average.append(calculate[columna].mean())
        std.append(calculate[columna].std())
    return pd.DataFrame({"Mes":mes,"Promedio":average, "Desviación": std})


def moving_average(datos,media,tipo):

    average = []
    dia = []
    listdia = datos["Dia"].to_list()
    if media == "cada 2 días":

        for i in range(len(datos)-2):
            average.append(datos[tipo][i:i+2].mean())
            dia.append(listdia[i+2]-2)

    if media == "cada 5 días":
        for i in range(len(datos)-5):
            average.append(datos[tipo][i:i+5].mean())
            dia.append(listdia[i+5]-2.5)
    if media == "cada 7 días":
        for i in range(len(datos)-7):
            average.append(datos[tipo][i:i+7].mean())
            dia.append(listdia[i+7]-3.5)
        print(dia)
    return pd.DataFrame({"Dia":dia,"Promedio":average})
