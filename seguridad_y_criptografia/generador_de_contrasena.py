import random
import string

"""
Generador de Contraseñas Seguras

Este script genera una contraseña segura que cumple con criterios especificos de complejidad.
la contraseña generada incluye una combinacion de letras mayusculas, minusculas, numeros y simbolos

Dependencias:
- ninguna, solo el modulo 'random' y 'string' de la biblioteca estandar de Python.

Instrucciones:
- ejecuta el script.
- elige la longitud de la contraseña que deseas generar.
- la contraseña generada se imprimira en la consola.

Este script es util para crear contraseñas para nuevas cuentas o para actualizar contraseñas existentes con una mas segura.
"""

# Funcion para generar contraseñas seguras
def generar_contraseña_segura(longitud):
    """
    Genera una contraseña segura con la longitud dada.
    
    Args:
        longitud (int): La longitud deseada para la contraseña.

    Returns:
        str: Una contraseña segura generada aleatoriamente.
    """
    
    if longitud < 8:
        raise ValueError("La longitud minima para una contraseña segura es 8.")
    
    # definimos un conjunto de caracteres para construir la contraseña
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    simbolos = string.punctuation

    # combinamos los caracteres
    mezcla = random.sample(letras_mayusculas, 2) + random.sample(letras_minusculas, 2) + \
             random.sample(digitos, 2) + random.sample(simbolos, 2)

    if longitud > 8:
        mezcla += random.choices(letras_mayusculas + letras_minusculas + digitos + simbolos, k=longitud - 8)

    # Mezcla los caracteres para asegurar aleatoriedad
    random.shuffle(mezcla)

    # convertimos y retornamos la contraseña
    return ''.join(mezcla)

if __name__ == "__main__":
    longitud_deseada = int(input("Introduce la longitud deseada para tu contraseña (mínimo 8 caracteres): "))
    contraseña_segura = generar_contraseña_segura(longitud_deseada)
    print(f"Tu nueva contraseña segura es: {contraseña_segura}")
