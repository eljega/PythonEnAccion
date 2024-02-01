import os
from collections import defaultdict
from datetime import datetime
import shutil

def organizar_descargas(path_descargas):
    """
    Organiza los archivos en el directorio de descargas en carpetas basadas en la extensión del archivo por ejemplo
    archivos .jpg, .png .avif etc.

    Args:
        path_descargas (str): Ruta del directorio de descargas a organizar.
    """
    archivos_por_tipo = defaultdict(list)

    # for que recorrer todos los archivos en el directorio de descargas
    for archivo in os.listdir(path_descargas):
        ruta_completa = os.path.join(path_descargas, archivo)
        if os.path.isdir(ruta_completa):
            continue
        ext = os.path.splitext(archivo)[1].lower()
        archivos_por_tipo[ext].append(ruta_completa)

    for ext, archivos in archivos_por_tipo.items():
        # Si la extension esta vaciia con archivos sin extension, usar 'Otros'
        if ext == "":
            ext = "Otros"
        nombre_dir = f"{ext[1:]}_archivos" if ext else ext
        dir_path = os.path.join(path_descargas, nombre_dir)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for ruta in archivos:
            shutil.move(ruta, dir_path)
            print(f"Movido: {ruta} a {dir_path}/")

# cambia esto a la ruta de tu directorio de descargas
directorio_descargas = "escribe la ruta de tu carpeta de descargas"
organizar_descargas(directorio_descargas)
