"""
generador de reportes automatizado en Python

este script es un ejemplo simplificado de como recolectar, analizar y generar un reporte de datos
automatizado en un HTML. para este ejemplo, los datos son estaticos y definidos
directamente dentro del script, el analisis se centra en generar estadisticas descriptivas basicas
y una visualizacion de las ventas de productos. Finalmente, el script genera un reporte en HTML
que incluye los resultados del analisis y una imagen del grafico de ventas.

Dependencias:
- pandas: Para analisis de datos y estadisticas descriptivas.
- matplotlib: Para generar graficos a partir de los datos.

Instrucciones de Uso:
1. instala las dependencias ejecutando: pip install pandas matplotlib
2. ejecuta el script
5. revisa los archivos generados `reporte.html` y `ventas.png` para ver el resultado.

Este es un ejemplo simplificado de lo que se puede hacer con Python para automatizar tareas
"""

import pandas as pd
import matplotlib.pyplot as plt

# datos estaticos para el ejemplo
datos = {
    "Producto": ["Producto A", "Producto B", "Producto C"],
    "Ventas": [100, 150, 200]
}
# funcion para analizar los datos
def analizar_datos(datos):
    df = pd.DataFrame(datos)
    grafico = df.plot(kind="bar", x="Producto", y="Ventas", legend=False)
    grafico.set_ylabel("Unidades Vendidas")
    plt.tight_layout()
    plt.savefig("ventas.png")
    return df.describe().to_html()

# funcion para generar el reporte
def generar_reporte(analisis_html):

    html_content = f"""
    <html>
    <head>
        <title>Reporte de Ventas</title>
    </head>
    <body>
        <h1>Analisis de Ventas</h1>
        <p>A continuacion, se muestra un analisis basico de las ventas de productos:</p>
        {analisis_html}
        <p>Grafico de ventas:</p>
        <img src="ventas.png" alt="Grafico de Ventas">
    </body>
    </html>
    """
    with open("reporte.html", "w") as f:
        f.write(html_content)


if __name__ == "__main__":
    analisis_html = analizar_datos(datos)
    generar_reporte(analisis_html)
    print("reporte generado con exito, revisa el archivo 'reporte.html' y 'ventas.png'.")
