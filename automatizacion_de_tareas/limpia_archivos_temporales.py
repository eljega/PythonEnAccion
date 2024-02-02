import os
import fnmatch

"""
limpiador automatico de Archivos Temporales

Este script recorre un directorio especifico, identifica archivos temporales
o innecesarios basados en extensiones comunes de archivos temporales y los elimina.

Instrucciones de Uso:
- Modifica la variable 'directorio_trabajo' para ingresar al directorio que deseas limpiar.
- modifica la lista 'patrones_a_eliminar' para incluir los patrones de nombres de archivo que deseas eliminar.
- Ejecuta el script. en la terminal te pedira verificar si estas seguro de eliminarlos.

Importante:
- Usa este script con cuidado. asegurate de que los patrones definidos no incluyan archivos importantes.
"""
directorio_trabajo = 'ruta de el directorio'
patrones_a_eliminar = ['*.tmp', '*.log', '*.bak', '*~']

def limpiar_directorio(directorio, patrones):
    """
    Busca y elimina archivos basados en una lista de patrones de nombres de archivo.
    
    Args:
        directorio (str): El directorio a limpiar.
        patrones (list): Lista de patrones de nombres de archivo para eliminar.
    """
    for raiz, _, archivos in os.walk(directorio):
        for patron in patrones:
            for archivo in fnmatch.filter(archivos, patron):
                archivo_completo = os.path.join(raiz,archivo)
                try:
                    os.remove(archivo_completo)
                    print(f"archivo eliminado: {archivo_completo}")
                except OSError as e:
                    print(f"Error al eliminar {archivo_completo}: {e}")
if __name__ == "__main__":
    print(f"Limpiando el directorio: {directorio_trabajo}")
    confirmacion = input("¿Estás seguro de que deseas eliminar archivos temporales? (s/n): ")
    if confirmacion.lower() == 's':
        limpiar_directorio(directorio_trabajo, patrones_a_eliminar)
        print("Limpieza completada.")
    else:
        print("Operacion cancelada.")