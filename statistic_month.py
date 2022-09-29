import streamlit as st
import requests
from transform.transform_market import transform_to_pandas
from transform.set_coins import coins_usd
from graphics import statistic_per_month
def estadistica_por_mes():
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


    fig = statistic_per_month(df)
    st.plotly_chart(fig)
