import http.client
import csv
from io import StringIO

def obtener_pronostico_clima_visual_crossing(ciudad):
    """
    vamos a obtener el pronostico del tiempo para una ciudad específica utilizando la API de Visual Crossing Weather
    esta api es totalmente gratis con limite de usos mensuales y la encuentras en RaidApi.

    Args:
        ciudad (str): Ciudad para la cual se desea obtener el pronostico, en formato "Ciudad,Estado,Pais".

    Imprime la informacion relevante del pronostico del tiempo.
    """
    conn = http.client.HTTPSConnection("visual-crossing-weather.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "aqui colocas tu api-key",
        'X-RapidAPI-Host': "aqui el host por defecto de la api"
    }

    ciudad_formateada = ciudad.replace(' ', '%2C')

    try:
        conn.request("GET", f"/forecast?aggregateHours=24&location={ciudad_formateada}&contentType=csv&unitGroup=us&shortColumnNames=0", headers=headers)
        res = conn.getresponse()
        data = res.read().decode("utf-8")

        csv_reader = csv.DictReader(StringIO(data))
        for fila in csv_reader:
            print(f"Pronostico del tiempo para {ciudad}:")
            print(f"Fecha: {fila['Date time']}")
            print(f"Temperatura Mínima: {fila['Minimum Temperature']}°F")
            print(f"Temperatura Máxima: {fila['Maximum Temperature']}°F")
            print(f"Precipitaciones: {fila['Precipitation']} pulgadas")
            print(f"Descripcion: {fila['Conditions']}")
            break 

    except Exception as e:
        print(f"Error al obtener el pronostico del clima: {e}")

    finally:
        conn.close()


ciudad = "Washington,DC,USA"
obtener_pronostico_clima_visual_crossing(ciudad)
