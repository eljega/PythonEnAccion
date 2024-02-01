import time

"""
script de Control de Tiempo

este script nos puede ayudar a saber cuanto tiempo pasamos en diferentes tareas.
podemos iniciar una tarea cambiar a otra, y al final, ver un resumen del tiempo total 
pasado en cada tarea.

Instrucciones:
- ejecuta el script.
- sigue las instrucciones en la consola para iniciar o cambiar tareas y para detener el seguimiento.
- usa la opcion 'informe' para ver un resumen del tiempo dedicado a cada tarea.

no usamos dependencias externas
"""

tareas_tiempo = {}
tarea_actual = None
inicio_tarea_actual = None

def iniciar_tarea(nombre_tarea):
    global tarea_actual, inicio_tarea_actual
    if tarea_actual:
        finalizar_tarea()
    tarea_actual = nombre_tarea
    inicio_tarea_actual = time.time()
    print(f"Tarea '{tarea_actual}' iniciada.")

def finalizar_tarea():
    global tareas_tiempo, tarea_actual, inicio_tarea_actual
    if tarea_actual:
        duracion = time.time() - inicio_tarea_actual
        if tarea_actual not in tareas_tiempo:
            tareas_tiempo[tarea_actual] = 0
        tareas_tiempo[tarea_actual] += duracion
        print(f"Tarea '{tarea_actual}' finalizada. Duración: {duracion:.2f} segundos.")
        tarea_actual = None

def informe():
    print("\nInforme de Tiempo:")
    total = 0
    for tarea, segundos in tareas_tiempo.items():
        total += segundos
        print(f"Tarea '{tarea}': {segundos:.2f} segundos.")
    print(f"Tiempo total: {total:.2f} segundos.")

def controlador_tiempo():
    try:
        while True:
            comando = input("\nComandos disponibles: 'iniciar <tarea>', 'finalizar', 'informe', 'salir'\n> ")
            if comando.startswith('iniciar '):
                _, nombre_tarea = comando.split(' ', 1)
                iniciar_tarea(nombre_tarea)
            elif comando == 'finalizar':
                finalizar_tarea()
            elif comando == 'informe':
                informe()
            elif comando == 'salir':
                finalizar_tarea()
                print("Saliendo del controlador de tiempo.")
                break
            else:
                print("Comando no reconocido.")
    except KeyboardInterrupt:
        finalizar_tarea()
        print("\nSaliendo del controlador de tiempo (Interrupción por teclado).")

if __name__ == "__main__":
    print("Bienvenido al Script de Control de Tiempo.")
    controlador_tiempo()
    informe()
