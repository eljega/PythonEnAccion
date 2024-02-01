from pytube import YouTube
import cv2
import os

def download_video(url, path='.'):
    """
    Descarga el video de YouTube y retorna la ruta del archivo descargado.

    Args:
        url (str): URL del video de YouTube.
        path (str): Directorio de destino para el video descargado.

    Returns:
        str: Ruta al video descargado.
    """
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video_path = stream.download(output_path=path)
        return video_path
    except Exception as e:
        raise Exception(f"Error al descargar el video: {e}")

def extract_thumbnail(video_path, frame_size=(1920, 1280)):
    """
    Extrae una miniatura del video y la guarda como archivo de imagen.

    Args:
        video_path (str): Ruta al archivo de video.
        frame_size (tuple): Dimensiones deseadas (ancho, alto) para la miniatura.

    Raises:
        Exception: Si falla la extracción de la miniatura.
    """
    try:
        video_capture = cv2.VideoCapture(video_path)
        if not video_capture.isOpened():
            raise Exception("No se pudo abrir el archivo de video")

        total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        if total_frames == 0:
            raise Exception("El video no contiene frames")

        middle_frame_index = total_frames // 2
        video_capture.set(cv2.CAP_PROP_POS_FRAMES, middle_frame_index)
        success, frame = video_capture.read()
        video_capture.release()

        if not success:
            raise Exception("No se pudo leer el frame del video")

        frame = cv2.resize(frame, frame_size)
        thumbnail_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}_thumbnail.jpg"
        cv2.imwrite(thumbnail_filename, frame)
        print(f"Miniatura guardada como: {thumbnail_filename}")
    except Exception as e:
        raise Exception(f"Error al extraer la miniatura: {e}")

# URL del video de YouTube
video_url = "URL del video"

try:
    # Descarga el video
    video_path = download_video(video_url)
    print(f"Video descargado en: {video_path}")

    # Extrae y guarda la miniatura
    extract_thumbnail(video_path)
except Exception as e:
    print(e)
