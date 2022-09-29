import streamlit as st
import requests
from transform.transform_market import transform_to_pandas
from transform.set_coins import coins_usd
from graphics import statistic_per_day

def estadistica_por_dia():
    coins = coins_usd()
    cripto = st.sidebar.selectbox("Seleccione una Criptomoneda", coins)
    def choose_cripto(cripto):
        api ='https://ftx.com/api/markets/'

        r = requests.get(api+cripto+"/candles?resolution=86400&start_time=1559881511")

        return r.json()["result"]
    data=choose_cripto(cripto)
    datos = transform_to_pandas(data)
    años = datos["Año"].value_counts().index.to_list()
    años.sort()
    anio = st.sidebar.selectbox("Seleccione el Año",años)
    df = datos.loc[datos.Año == anio]
    mes = df["Mes"].value_counts().index.to_list()
    mes = st.sidebar.selectbox("Seleccione el mes",mes)
    dfmes = df.loc[df.Mes == mes]
    moving = ["cada 2 días","cada 5 días", "cada 7 días"]
    question = ["Si","No"]
    showdata = st.sidebar.selectbox("¿Mostrar dato por día?",question)
    showmedia = st.sidebar.selectbox("¿Mostrar media móvil?",question)
    if showmedia == "Si":
        media = st.sidebar.selectbox("Seleccione la media móvil",moving)
    else:
        media = None
    if showdata == "No" and showmedia == "No":
        st.title("Por favor seleccione el tipo de tabla.")
    else:
        fig = statistic_per_day(dfmes,media,showdata)
        st.plotly_chart(fig)
