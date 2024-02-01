from PIL import Image
import os

def crear_collage(ruta_imagenes, ruta_salida):
    """
    recuerda instalar las dependencias en este caso pip install Pillow

    Crea un collage combinando imagenes horizontalmente.

    Args:
        ruta_imagenes (str): ruta del directorio que contiene las imagenes a combinar.
        ruta_salida (str): ruta del archivo de imagen resultante.

    Combina todas las imagenes en la ruta especificada en un collage horizontal.
    """
    try:
        # obtenemos la lista de archivos de imagen
        archivos = [f for f in os.listdir(ruta_imagenes) if f.endswith('.jpg') or f.endswith('.png')]
        if not archivos:
            print("No se encontraron imagenes en el directorio.")
            return

        # abrimos las imagenes
        imagenes = [Image.open(os.path.join(ruta_imagenes, archivo)) for archivo in archivos]
        ancho_total = sum(imagen.width for imagen in imagenes)
        max_alto = max(imagen.height for imagen in imagenes)

        # aqui creamos el tamaño de la nueva imagen
        collage = Image.new('RGB', (ancho_total, max_alto))

        x_actual = 0
        for imagen in imagenes:
            collage.paste(imagen, (x_actual, 0))
            x_actual += imagen.width

        # y por ultimo guardamos la nueva imagen creada
        collage.save(ruta_salida)
        print(f"Collage creado exitosamente en: {ruta_salida}")

    except Exception as e:
        print(f"Error al crear el collage: {e}")

directorio_imagenes = "escribe la ruta donde tienes tus imagenes jpg o png"
ruta_salida_collage = "escribe la ruta donde guardaras tu collage, recuerda asignarle un nombre y una extension .png o .jpg"

crear_collage(directorio_imagenes, ruta_salida_collage)
