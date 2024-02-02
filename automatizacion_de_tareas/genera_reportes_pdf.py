import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import Image


"""
generador automatico de reportes en PDF

este script recopila datos de un archivo CSV y genera un reporte automatico y directo en formato PDF,
incluyendo tablas y visualizaciones de los datos.

Dependencias:
- Pandas: Para leer y procesar los datos del CSV.
- Matplotlib: Para generar visualizaciones de los datos.
- ReportLab: Para crear el reporte en PDF.

Instrucciones:
1. Instala las dependencias: pip install pandas matplotlib reportlab pyarrow
2. Modifica las variables 'csv_file_path' y 'pdf_file_path' segun sea necesario para tus archivos
3. ejecuta el script para generar el reporte en PDF.
"""

csv_file_path = 'C:/Users/playg/Downloads/csv_archivos/pruebacsv.csv'  # Ruta al archivo CSV con los datos
pdf_file_path = 'C:/Users/playg/Downloads/csv_archivos/mi_reporte.pdf'  # Ruta al archivo de reporte PDF generado
datos = pd.read_csv(csv_file_path)

# Generar una visualizacion simple
plt.figure(figsize=(8, 6))
datos['columna numerica'].hist()  # recuerda cambiar 'columna numerica' con el nombre de una columna numerica de tus datos
plt.title('Distribución de columna numerica') #remplaza aqui tambien 'columna numerica'
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.savefig('ruta/donde/guardaras/tu/archivo/histograma.png')#selecciona la ruta y 'opcional' cambia el nombre histograma
plt.close()

# Crear un documento PDF y añadir los datos en una tabla
doc = SimpleDocTemplate(pdf_file_path, pagesize=letter)
elements = []
data = [datos.columns.values.tolist()] + datos.values.tolist()

# creamos la tabla
table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
    ('GRID', (0,0), (-1,-1), 1, colors.black),
]))

elements.append(table)

# añadimos la imagen al pdf
imagen_histograma = Image('ruta/donde/guardaras/tu/archivo/histograma.png', width=400, height=300)
elements.append(imagen_histograma)
doc.build(elements)

print(f'Reporte generado con éxito en: {pdf_file_path}')