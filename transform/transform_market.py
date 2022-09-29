import requests
import pandas as pd

def transform_to_pandas(data):

	abertura = []
	cierre = []
	alto = []
	bajo = []
	anio = []
	mes = []
	dia = []

	for i in range(len(data)):
		abertura.append(data[i]["open"])
		cierre.append(data[i]["close"])
		alto.append(data[i]["high"])
		bajo.append(data[i]["low"])
		anio.append(int(data[i]["startTime"][0:4]))
		mes.append(int(data[i]["startTime"][5:7]))
		dia.append(int(data[i]["startTime"][8:10]))
	datos = pd.DataFrame({"Abre":abertura, "Cierre":cierre,"Alto":alto,
						"Bajo":bajo,"Año":anio, "Mes":mes,"Dia":dia})
	replace_mes = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril",
				   5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre",
				   10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
	datos = datos.replace({"Mes":replace_mes})
	return datos
