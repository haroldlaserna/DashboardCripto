import streamlit as st
import requests
from statistic_month import estadistica_por_mes
from statistic_day import estadistica_por_dia
dashboard = ["Media móvil por mes","Datos por día"]
tipo = st.sidebar.selectbox("Seleccione dashboard", dashboard)

st.title(tipo)

if tipo == dashboard[0]:
    estadistica_por_mes()
elif tipo == dashboard[1]:
    estadistica_por_dia()
