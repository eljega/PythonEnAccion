from pytube import YouTube
import requests

def download_thumbnail(url, path='.'):
    """
    Descarga la miniatura del video de YouTube especificado por la URL.

    Args:
        url (str): URL del video de YouTube.
        path (str): Directorio de destino para la miniatura descargada.
    """
    try:
        yt = YouTube(url)
        thumbnail_url = yt.thumbnail_url
        if not thumbnail_url:
            raise Exception("No se pudo obtener la URL de la miniatura")

        response = requests.get(thumbnail_url)
        if response.status_code != 200:
            raise Exception("No se pudo descargar la miniatura")

        # Extrae el ID del video de YouTube para usarlo como nombre de archivo
        video_id = yt.video_id
        filename = f"{video_id}_thumbnail.jpg"
        filepath = f"{path}/{filename}"
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
            print(f"Miniatura guardada en: {filepath}")
    except Exception as e:
        print(f"Error al descargar la miniatura: {e}")

# URL del video de YouTube
video_url = "url del video"

# Llamada a la función
download_thumbnail(video_url)
