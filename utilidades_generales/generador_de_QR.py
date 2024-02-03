import qrcode

"""
Generador de codigos QR

en este script generamos codigos QR para cualquier texto, URL o informacion de contacto y 
guardamos el codigo en una imagen .png

Dependencias a instalar:
- la biblioteca qrcode y Pillow para generar los codigos e imagenes qr.
  Instalacion: pip install qrcode[pil]

instrucciones de Uso:
1. instala las dependencias.
2. debes modificar la variable de 'datos' ingresando la URL o informacion que vas a convertir a codigo QR.
3. ejecuta el script y automaticamente se guardara una imagen png con tu qr, puedes cambiar la ruta si quieres.

Nota: Puedes practicar modificando la configuracion de parametros en (qrcode.make).
"""

datos = "https://my-portfolio-six-psi-44.vercel.app" # aqui ingresas el link de la url a convertie

archivo_salida = "codigo_qr.png"# aqui ingresas el nombre con el que se guarda la imagen, puedes cambiarlo

# generamos el codigo qr
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(datos)
qr.make(fit=True)

# creamos la imagen a partir del codigo y guardamos el archivo
img = qr.make_image(fill_color="black", back_color="white")
img.save(archivo_salida)

print(f"Codigo QR generado con exito y guardado como '{archivo_salida}'.")
