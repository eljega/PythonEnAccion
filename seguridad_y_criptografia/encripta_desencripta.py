from cryptography.fernet import Fernet

"""
Encriptada y Desencripta Archivos

Este script nos da una forma de cifrar y descifrar archivos utilizando una clave generada por nosotros.
Utiliza el algoritmo de cifrado simetrico AES a traves de la biblioteca 'cryptography' de Python.

Dependencias:
- cryptography: Una biblioteca que proporciona herramientas criptograficas en Python.
  Instalacion: pip install cryptography

Instrucciones:
- ejecuta el script y sigue las instrucciones para cifrar o descifrar un archivo.
- nos aseguramos de guardar la clave generada en un lugar seguro para poder descifrar el archivo más tarde.
- usa la misma clave para cifrar y descifrar el archivo.

"""

# Funcion que una clave de cifrado
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Funcion que la clave de cifrado
def cargar_clave():
    return open("clave.key", "rb").read()

# Funcion que cifrar el archivo
def cifrar_archivo(archivo_a_cifrar, clave):
    f = Fernet(clave)
    with open(archivo_a_cifrar, "rb") as file:
        archivo_info = file.read()
    datos_cifrados = f.encrypt(archivo_info)
    with open(archivo_a_cifrar, "wb") as file:
        file.write(datos_cifrados)

# Funcion que descifrar el archivo
def descifrar_archivo(archivo_a_descifrar, clave):
    f = Fernet(clave)
    with open(archivo_a_descifrar, "rb") as file:
        datos_cifrados = file.read()
    datos_descifrados = f.decrypt(datos_cifrados)
    with open(archivo_a_descifrar, "wb") as file:
        file.write(datos_descifrados)

if __name__ == "__main__":
    opcion = input("¿Deseas (C)ifrar o (D)escifrar un archivo? ").upper()
    if opcion == 'C':
        generar_clave()
        clave = cargar_clave()
        archivo_a_cifrar = input("Ingresa el nombre del archivo a cifrar: ")
        cifrar_archivo(archivo_a_cifrar, clave)
        print(f"El archivo {archivo_a_cifrar} ha sido cifrado.")
    elif opcion == 'D':
        clave = cargar_clave()
        archivo_a_descifrar = input("Ingresa el nombre del archivo a descifrar: ")
        descifrar_archivo(archivo_a_descifrar, clave)
        print(f"El archivo {archivo_a_descifrar} ha sido descifrado.")
    else:
        print("Opcion no válida. Por favor, elige 'C' o 'D'.")
