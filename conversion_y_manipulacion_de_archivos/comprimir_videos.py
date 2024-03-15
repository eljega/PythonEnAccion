from moviepy.editor import VideoFileClip

def comprimir_video(ruta_video, ruta_destino=None, bitrate="2000k"):
    """
    Comprime un archivo de video a un bitrate menor para reducir su tamaño.
    
    Args:
    ruta_video (str): Ruta del archivo de video original.
    ruta_destino (str): Ruta del archivo de video comprimido. Si no se especifica, se sobrescribirá el original.
    bitrate (str): Bitrate objetivo para el video comprimido. Default es "2000k".
    """
    if ruta_destino is None:
        ruta_destino = ruta_video

    # cargamos el video original
    clip = VideoFileClip(ruta_video)
    
    # escribimos el video con un bitrate menor
    clip.write_videofile(ruta_destino, bitrate=bitrate)


ruta_video_original = "ruta donde tienes tu video"
ruta_video_comprimido = "ruta donde lo quieres guardar"
comprimir_video(ruta_video_original, ruta_video_comprimido)

print("La compresion del video ha finalizado.")
