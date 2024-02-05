import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""
haremos un generador de graficos de distribucion

este script nos permite visualizar la distribucion de datos usando varios tipos de graficos
como histograma, boxplot, densidad y violin a partir de datos en un archivo CSV, yo use uno de prueba con 1.000 datos.

dependencias necesarias:
- Pandas para la manipulacion de datos.
- Matplotlib y Seaborn para la generacion de graficos
  instalacion: pip install pandas matplotlib seaborn

instrucciones de Uso:
1. debemos tener un archivo csv para ejecutarlo y hacer el analisis.
2. debemos modificar la variable 'ruta_archivo_csv' y colocar la ruta donde tenemos el csv de prueba.
3. ajustamos las columnas y tipos de graficos segun tus necesidades.
4. al ejecutar el script deberiamos ver los graficos generados.
"""

ruta_archivo_csv = 'C:/Users/playg/Downloads/datos_ficticios.csv'# coloca aqui la ruta donde tienes el csv
datos = pd.read_csv(ruta_archivo_csv)

sns.set(style="whitegrid")

# funcion de graficos de una columna de densidad
def generar_grafico_densidad(columna):
    plt.figure()
    sns.histplot(datos[columna], kde=True)
    plt.title(f'Grafico de Densidad de {columna}')
    plt.xlabel(columna)
    plt.ylabel('Densidad')
    plt.show()

#funcion de grafico de violin para una columna especifica
def generar_grafico_violin(columna):
    plt.figure()
    sns.violinplot(x=datos[columna])
    plt.title(f'Grafico de Violin de {columna}')
    plt.xlabel(columna)
    plt.show()

# funcion de grafico de caja y bigotes para todas las columnas numericas
def generar_grafico_caja_bigotes():
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=datos.select_dtypes(include=['float64', 'int64']))
    plt.title('Grafico de Caja y Bigotes de Datos Numéricos')
    plt.xticks(rotation=45)
    plt.show()

# funcion de histograma para una columna 
def generar_histograma(columna):
    plt.figure()
    datos[columna].hist(bins=20)
    plt.title(f'Histograma de {columna}')
    plt.xlabel(columna)
    plt.ylabel('Frecuencia')
    plt.show()

#  funcion de boxplot para una columna 
def generar_boxplot(columna):
    plt.figure()
    datos.boxplot(column=columna)
    plt.title(f'Boxplot de {columna}')
    plt.ylabel(columna)
    plt.show()

if __name__ == "__main__":
    # en cada columna debemos incluir las columnas reales de nuestro.
    columna_histograma = 'Edad'
    columna_boxplot = 'Ingresos'
    columna_densidad = 'Puntaje_Satisfaccion'
    columna_violin = 'Ingresos'
    
    # aqui generamos los graficos
    generar_histograma(columna_histograma)
    generar_boxplot(columna_boxplot)
    generar_grafico_densidad(columna_densidad)
    generar_grafico_violin(columna_violin)
    generar_grafico_caja_bigotes()
