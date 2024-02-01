import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def generar_mapa_calor(datos_clics):
    """
    recuerda instalar las dependencias en tu entorno virtual, en este caso pip install matplotlib seaborn pandas numpy

    generamos un mapa de calor a partir de los datos de clics en un sitio web.
    Asegúrate de que los datos de clics sean un DataFrame de pandas con las columnas 'x' y 'y'.
    """
    if datos_clics.empty or 'x' not in datos_clics.columns or 'y' not in datos_clics.columns:
        print("Los datos de clics estan vacíos o no tienen las columnas 'x' y 'y' requeridas.")
        return
    
    plt.figure(figsize=(10, 6))
    sns.kdeplot(data=datos_clics, x='x', y='y', fill=True, cmap="Reds", bw_adjust=0.5)
    plt.title("Mapa de Calor de Clics en el Sitio Web")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.show()

datos_clics = pd.DataFrame({
    'x': np.random.normal(loc=50, scale=10, size=100),
    'y': np.random.normal(loc=50, scale=10, size=100)
})

generar_mapa_calor(datos_clics)
