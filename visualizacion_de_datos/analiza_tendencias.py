"""
Analizador de Tendencias de Busqueda en Tiempo Real

en este script utiliamos 'pytrends' para acceder a Google Trends y obtener las tendencias de
busqueda en tiempo real para un conjunto de palabras clave definidas por el usuario. Utiliza Matplotlib
para graficar las tendencias en tiempo real, permitiendo al usuario visualizar la popularidad de estos
términos de busqueda durante la ultima hora.

dependencias:
- pytrends: para la interactuar con Google Trends.
- matplotlib: para visualizar datos en tiempo real.
para instalar activa tu entorno virtual y ejecuta: pip install pytrends matplotlib

"""

# aqui importamos las bibliotecas necesarias
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import time
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# aqui inicializamos la conexion con Google Trends
pytrend = TrendReq()

# aqui definimos una funcion para graficar las tendencias
def plot_trends(keywords):
    pytrend.build_payload(kw_list=keywords, timeframe='now 1-H')
    data = pytrend.interest_over_time()

    if not data.empty:
        plt.clf()
        for keyword in keywords:
            plt.plot(data.index, data[keyword], label=keyword)
    
        plt.legend()
        plt.title("tendencias de busqueda de Google en tiempo real")
        plt.xticks(rotation=45)
        plt.tight_layout()
        # mostramos la grafica
        plt.pause(0.1)


# aqui definimos la funcion principal que observa las tendencias
def main():
    keywords = ["Python", "Javascript", "Java", "C#"]
    print("observando las tendencias para las palabras claves: ", keywords)

    plt.ion()
    try:
        while True:
            plot_trends(keywords)
            time.sleep(60)# actualizamos cada minuto
    except KeyboardInterrupt:
        print("deteniendo el programa...")
        plt.ioff()
        plt.close()
if __name__ == "__main__":
    main()