"""
Script de Automatizacion para Configuracion de Proyectos Python

Este script facilita la configuracion inicial de proyectos de Python automatizando varias tareas comunes como:
- Creacion de un entorno virtual en el directorio actual o especificado.
- Inicializacion de un repositorio Git.
- Generacion de archivos comunes como .gitignore, README.md y Requirements.txt.
- Opcion para crear o actualizar un archivo requirements.txt con las dependencias actuales del entorno virtual.
- Opcion para instalar dependencias desde un archivo requirements.txt existente.
- Todo de manera automatica!

Instrucciones de Uso:
1. Deberas instalar Virtualvenv previamente.
2. Coloca este script en el directorio raiz de tu proyecto.
3. Ejecuta el script utilizando Python: python "nombre_del_script".py o con la ejecucion de vscode 
4. Sigue las instrucciones en pantalla para generar el entorno virtual, inicializar Git, y manejar las dependencias.

Funcionalidades:
- **Creacion de Entorno Virtual**: Automaticamente crea un entorno virtual denominado 'env' en el directorio actual, a menos que se especifique otro nombre o ruta.
- **Inicializacion de Git**: Inicia un nuevo repositorio Git si no existe uno en el directorio actual.
- **Archivos Comunes**: Genera archivos .gitignore y README.md con contenido basico para comenzar.
- **Manejo de Dependencias**:
    - Genera un archivo requirements.txt vacío o con las dependencias actuales del entorno virtual, según la eleccion del usuario.
    - Permite al usuario instalar dependencias desde un archivo requirements.txt existente.

¿Para Qué Sirve?
Este script te ahorra el tener que crear la configuracion inicial de tu proyecto,
asegurando que tengas un entorno de desarrollo consistentemente configurado y listo para comenzar a programar.

IMPORTANTE: Este script asume que se ejecuta en un sistema Windows para la ruta del intérprete de Python en el entorno virtual.
Si estas utilizando otro sistema operativo, ajusta la ruta del intérprete de Python en las funciones correspondientes.
"""

import subprocess
import os
import sys

venv_path = "env"  # puedes cambiar el valor de esta variable si quieres que tu entorno tenga otro nombre

def create_venv():
    if venv_path:
        target_dir = venv_path
    else:
        target_dir = os.path.join(os.getcwd(), "env")

    if not os.path.exists(target_dir):
        try:
            subprocess.run(["python", "-m", "virtualenv", target_dir], check=True)
            print(f"entorno virtual creado en {target_dir}.")
        except Exception as e:
            print(f"error al crear el entorno virtual: {e}")
    else:
        print("entorno virtual ya existe.")

#funcion para inicializar el repositorio
def init_git_repo():
    if not os.path.exists(".git"):
        try:
            subprocess.run(["git", "init"], check=True)
            print("repositorio Git inicializado.")
        except Exception as e:
            print(f"error al inicializar el repositorio Git: {e}")
    else:
        print("tu repo ya esta inicializado")

def is_venv_active():
    return os.environ.get('VIRTUAL_ENV') is not None

def create_requirements_file():
    requirements_path = os.path.join(os.getcwd(), "requirements.txt")
    # aqui verificamos si el archivo existe
    if not os.path.exists(requirements_path):
        with open(requirements_path, 'w') as file:
            pass  #en principio creamos un archivo vacio
        print("archivo requirements.txt creado.")

    #aqui preguntamos al usuario si quiere si quiere generar el requirements
    respuesta = input("Quieres generar el requirements.txt a partir de las dependencias actuales del entorno virtual? (S/N): ")
    if respuesta.lower() == 's':
        python_exec_path = os.path.join(os.getcwd(), venv_path, 'Scripts', 'python.exe')  # Ajustado para Windows
        try:
            #usamos el subprocess.check_output para capturar la salida de pip freeze
            output = subprocess.check_output([python_exec_path, "-m", "pip", "freeze"], universal_newlines=True)
            with open(requirements_path, 'w') as file:
                file.write(output)
            print("archivo requirements.txt generado con las dependencias actuales.")
        except subprocess.CalledProcessError as e:
            print(f"error al generar requirements.txt: {e}")
    else:
        print("generacion de requirements.txt omitida.")


def install_dependencies():
    #preguntamos al usuario si quiere instalar las dependencias
    ### SOLO INSTALARA LAS DEPENDENCIAS QUE ESTEN PREVIAMENTE ASIGNADAS AL REQUIREMENTS.TXT###
    instalar = input("quieres instalar las dependencias? (S/N): ")
    if is_venv_active() and instalar.lower() == "s":
        requirements_path = os.path.join(os.getcwd(), "requirements.txt")
        if os.path.exists(requirements_path):
            try:
                #ejecutamos la instalacion de dependencias desde el archvivo requirements
                subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path], check=True)
                print("dependencias instaladas correctamente.")
            except Exception as e:
                print(f"error al instalar dependencias: {e}")
        else:
            print("archivo requirements.txt no encontrado.")
    elif instalar.lower() != "s":
        pass
    else:
        print(f"el entorno virtual no esta activo. activalo con el comando: .\{venv_path}\Scripts\\activate")

#funcion para crear carpetas basicas
def create_common_files(project_name):
    common_files = {
        #puedes asignar mas archivos a los diferentes ficheros si lo requieres
        ".gitignore": f"{venv_path}/\n__pycache__/",
        "README.md": f"# {project_name}\n\nDescripción del proyecto."
    }
    for filename, content in common_files.items():
        with open(os.path.join(os.getcwd(), filename), 'w') as file:
            file.write(content)
    print("Archivos comunes creados.")


if __name__ == "__main__":
    create_venv()
    create_common_files("proyecto de prueba")#reemplaza esto por el nombre real de tu proyecto
    create_requirements_file()
    init_git_repo()
    install_dependencies()
