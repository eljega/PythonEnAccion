import shutil
import os
from datetime import datetime

def backup_folder(src, dst):
    """
    realiza una copia de seguridad de la carpeta 'src' en la carpeta 'dst'.
    
    Args:
        src (str): Ruta de la carpeta de origen.
        dst (str): Ruta de la carpeta de destino donde se almacenara la copia de seguridad.

    El nombre de la carpeta de copia de seguridad incluira la fecha y hora para evitar sobreescrituras.
    """
# Obtener la fecha y hora actual para crear un nombre unico de carpeta de backup
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f"backup_{now}"
    backup_path = os.path.join(dst, backup_name)
    
    try:
        # Copiar toda la carpeta de src a dst
        shutil.copytree(src, backup_path)
        print(f"La copia de seguridad se completó exitosamente en '{backup_path}'")
    except Exception as e:
        print(f"Error al realizar la copia de seguridad: {e}")

# debes usar rutas absolutas para evitar problemas con las rutas relativas
source_folder = "escribe la ruta de la carpeta que quieres copiar"
destination_folder = "escribe la ruta donde se guardara tu backup"

# llama a la funcion con las rutas correspondientes
backup_folder(source_folder, destination_folder)
