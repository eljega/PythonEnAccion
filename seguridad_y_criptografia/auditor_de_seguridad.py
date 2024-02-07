"""
auditor de seguridad para scripts de Python
Este script automatiza el proceso de analisis de seguridad en scripts de Python dentro de un directorio,
usando Bandit para buscar vulnerabilidades o malas practicas de seguridad

Instrucciones de uso:
1. debemos instalar bandit en nuestro venv.
2. recuerda modificar la variable 'directorio_objetivo' ingresando la carpeta que contiene tus scripts de python.
3. ejecuta este script y luego de unos segundos "o minutos" los resultados del analisis de seguridad se mostraran en la consola.

dependencias:
- bandit: `pip install bandit`
"""

import subprocess
import sys
# ingresamos la ruta de la carpeta de tu script o proyecto
directorio_objetivo = 'aqui escribes la ruta relativa de tu carpeta o proyecto'

def analizar_con_bandit(directorio):
    comando = ['bandit', '-r', directorio]
    try:
        resultado = subprocess.run(comando, check=True, capture_output=True, text=True)
        print("Resultados del analisis de seguridad con Bandit:")
        print(resultado.stdout)
    except subprocess.CalledProcessError as e:
        print("Bandit encontro uno o mas problemas de seguridad o malas practicas:")
        print(e.stdout)
        if e.stderr:
            print("Erroren la informacion adicional de Bandit:")
            print(e.stderr)

if __name__ == "__main__":
    # aqui verificamos si el directorio es valido
    if not directorio_objetivo:
        print(" asegurate de configurar bien la ruta de tu carpeta")
        sys.exit(1)
    # y ejecutamos la verificacion
    analizar_con_bandit(directorio_objetivo)
