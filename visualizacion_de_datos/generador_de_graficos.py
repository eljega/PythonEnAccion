import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def generar_graficos(datos):
    """
    nuevamente recuerda instalar las dependencias en tu entorno virtual, en este caso pip install matplotlib seaborn pandas numpy
    
    Generamos varios tipos de graficos a partir de un conjunto de datos.

    graficos en barras
    graficos en lineas 
    histogramas

    Args:
        datos (DataFrame): Un DataFrame de pandas que contiene los datos para visualizar.
    """
    # configuramos seaborn
    sns.set_theme(style="whitegrid")

    # creamos un grafico de lineas
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=datos)
    plt.title("Grafico de Líneas")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.savefig("grafico_lineas.png")
    plt.show()

    # creamos un grafico de barras
    plt.figure(figsize=(10, 6))
    sns.barplot(x=datos.index, y=datos['Columna1'])  # Ajusta 'Columna1' según tus datos
    plt.title("Grafico de Barras")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.savefig("grafico_barras.png")
    plt.show()

    # y aqui creamos un histograma
    plt.figure(figsize=(10, 6))
    sns.histplot(data=datos['Columna1'], kde=True)  # Ajusta 'Columna1' según tus datos
    plt.title("Histograma")
    plt.xlabel("Valor")
    plt.ylabel("Frecuencia")
    plt.savefig("histograma.png")
    plt.show()

# aqui creamos datos de ejemplos
datos = pd.DataFrame({
    'Columna1': np.random.rand(10),
    'Columna2': np.random.rand(10)
}, index=pd.date_range(start='1/1/2022', periods=10, freq='D'))

generar_graficos(datos)
