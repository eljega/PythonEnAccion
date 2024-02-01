import requests
from bs4 import BeautifulSoup

def extraer_noticias(url, archivo_salida):
    """
    recuerda instalar las dependencias en este caso request y beautifulsoup4 con pip install

    extraemos las ultimas noticias de un portal de noticias y las guarda en un archivo de texto.

    Args:
        url (str):es la URL del portal de noticias del cual extraer las noticias.
        archivo_salida (str): esta es la ruta del archivo de texto donde se guardaran las noticias.
    """
    try:
        # enviamos la solicitud HTTP al portal de noticias
        respuesta = requests.get(url)
        respuesta.raise_for_status() 

        # se analiza el contenido HTML de la pagina
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        # IMPORTANTE: debemos ajustar el selector segun la estructura del portal de noticias.
        elementos_noticias = soup.find_all('h2', class_='title-container')   #esto se debe ajustar segun la pagina de noticias, en mi caso es el portal de eltiempo

        with open(archivo_salida, 'w', encoding='utf-8') as archivo:
            for noticia in elementos_noticias:
                titulo = noticia.text.strip()
                archivo.write(f"{titulo}\n\n")

        print(f"Las noticias han sido guardadas exitosamente en {archivo_salida}")

    except requests.HTTPError as e:
        print(f"Error al realizar la solicitud HTTP: {e}")
    except Exception as e:
        print(f"Error al extraer las noticias: {e}")

url_portal_noticias = "https://www.eltiempo.com" #aqui colocas la url de el portal o web a la que haras scrapin yo use eltiempo
archivo_salida_noticias = "noticias.txt" # puedes modificar la extension segun tus necesidades .txt .pdf etc.

extraer_noticias(url_portal_noticias, archivo_salida_noticias)
