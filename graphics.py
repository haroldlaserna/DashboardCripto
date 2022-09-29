from plotly.subplots import make_subplots
import plotly.graph_objects as go
from mathematic_statistic.average import average_std_month, moving_average

def statistic_per_month(datos):
    grafica1 = average_std_month(datos,"Cierre")
    grafica2 = average_std_month(datos,"Abre")
    grafica3 = average_std_month(datos,"Alto")
    grafica4 = average_std_month(datos,"Bajo")





    fig = make_subplots(rows=4, cols=2)

    fig.add_trace(
        go.Scatter(y=grafica1.Promedio, x=grafica1.Mes, name='Promedio-Cierre'),
        row=1, col=1
        )

    fig.add_trace(
        go.Scatter(y=grafica1["Desviación"], x=grafica1.Mes,  name='Desviación Estándar-Cierre'),
        row=1, col=2
        )

    fig.add_trace(
        go.Scatter(y=grafica2.Promedio, x=grafica2.Mes, name='Promedio-Apertura'),
        row=2, col=1
        )

    fig.add_trace(
        go.Scatter(y=grafica2["Desviación"], x=grafica2.Mes,  name='Desviación Estándar-Apertura'),
        row=2, col=2
        )

    fig.add_trace(
        go.Scatter(y=grafica3.Promedio, x=grafica3.Mes, name='Promedio-Alto'),
        row=3, col=1
        )

    fig.add_trace(
        go.Scatter(y=grafica3["Desviación"], x=grafica3.Mes,  name='Desviación Estándar-Alto'),
        row=3, col=2
        )

    fig.add_trace(
        go.Scatter(y=grafica4.Promedio, x=grafica4.Mes, name='Promedio-Bajo'),
        row=4, col=1
    )

    fig.add_trace(
        go.Scatter(y=grafica4["Desviación"], x=grafica4.Mes,  name='Desviación Estándar-Bajo'),
        row=4, col=2
    )
    fig.update_layout(height=1200, width=800)

    fig.update_layout(legend=dict(

        y=0.6,

        x=1
    ))
    return fig

def statistic_per_day(datos,media,showdata):
    if media != None:
        media_movil1 = moving_average(datos,media,"Cierre")
        media_movil2 = moving_average(datos,media,"Abre")
        media_movil3 = moving_average(datos,media,"Alto")
        media_movil4 = moving_average(datos,media,"Bajo")




    fig = make_subplots(rows=4, cols=1)
    if showdata == "Si":
        fig.add_trace(
            go.Scatter(y=datos.Cierre, x=datos.Dia, name='Cierre'),
            row=1, col=1
            )
        fig.add_trace(
            go.Scatter(y=datos.Abre, x=datos.Dia, name='Apertura'),
            row=2, col=1
            )

        fig.add_trace(
            go.Scatter(y=datos.Alto, x=datos.Dia, name='Alto'),
            row=3, col=1
            )

        fig.add_trace(
            go.Scatter(y=datos.Bajo, x=datos.Dia, name='Bajo'),
            row=4, col=1
            )
    if media != None:
        fig.add_trace(
            go.Scatter(y=media_movil1.Promedio, x=media_movil1.Dia, name='Media móvil-Cierre'),
            row=1, col=1
            )
        fig.add_trace(
            go.Scatter(y=media_movil2.Promedio, x=media_movil2.Dia, name='Media móvil-Cierre'),
            row=2, col=1
            )
        fig.add_trace(
            go.Scatter(y=media_movil3.Promedio, x=media_movil3.Dia, name='Media móvil-Cierre'),
            row=3, col=1
            )
        fig.add_trace(
            go.Scatter(y=media_movil4.Promedio, x=media_movil4.Dia, name='Media móvil-Cierre'),
            row=4, col=1
            )
    fig.update_layout(height=1200, width=800)


    fig.update_layout(legend=dict(

        y=0.6,

        x=1
    ))
    fig['layout']['xaxis']['title']='Día'
    fig['layout']['yaxis']['title']='Valor'
    fig['layout']['xaxis2']['title']='Día'
    fig['layout']['yaxis2']['title']='Valor'
    fig['layout']['xaxis3']['title']='Día'
    fig['layout']['yaxis3']['title']='Valor'
    fig['layout']['xaxis4']['title']='Día'
    fig['layout']['yaxis4']['title']='Valor'
    return fig
