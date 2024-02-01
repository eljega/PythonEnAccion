import pandas as pd

def calcular_estadisticas_descriptivas(csv_path, column_name):
    """
    calcula estadisticas descriptivas para una columna especifica en un archivo CSV.

    Args:
        csv_path (str): la ruta al archivo CSV.
        column_name (str): el nombre de la columna para calcular las estadisticas.
    
    calcula y muestra la media, mediana, moda y rango de la columna especificada.

    recuerda que debes instalar pandas en tu entorno virtual con pip install pandas
    """
    try:
        data = pd.read_csv(csv_path)
        if column_name not in data.columns:
            print(f"La columna '{column_name}' no se encontro en el archivo CSV.")
            return

        media = data[column_name].mean()
        mediana = data[column_name].median()
        moda = data[column_name].mode()[0] 
        rango = data[column_name].max() - data[column_name].min()

        print(f"Estadisticas para la columna '{column_name}':")
        print(f"Media: {media}")
        print(f"Mediana: {mediana}")
        print(f"Moda: {moda}")
        print(f"Rango: {rango}")

    except FileNotFoundError:
        print(f"No se encontro el archivo: {csv_path}")
    except Exception as e:
        print(f"Se produjo un error al procesar el archivo: {e}")

# Ruta al archivo CSV y nombre de la columna
ruta_csv = "url de el archivo csv"
nombre_columna = "nombre de la columna que deseas"

calcular_estadisticas_descriptivas(ruta_csv, nombre_columna)
