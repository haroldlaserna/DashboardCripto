import requests
import re

def coins_usd():
    r = requests.get('https://ftx.com/api/markets')
    data = r.json()["result"]
    names = []
    for i in range(len(data)):
        names.append(data[i]["name"])
    USD=re.compile("/USD")
    dolar_names = []

    for i in range(len(names)):
        if USD.search(names[i]):
            dolar_names.append(names[i])

    return dolar_names
