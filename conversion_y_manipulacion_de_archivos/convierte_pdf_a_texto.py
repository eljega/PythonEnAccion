import PyPDF2

def convertir_pdf_a_texto(ruta_pdf, ruta_salida_txt):
    """
    recuerda instalar las dependencias en este caso pip install PyPDF2

    convierte un archivo PDF en un archivo de texto.

    Args:
        ruta_pdf (str): es la ruta del archivo PDF a convertir.
        ruta_salida_txt (str): es la ruta del archivo de texto donde se guardara el contenido.

    lee el archivo PDF, extrae su contenido y lo guarda en un archivo de texto.
    """
    try:
        # Abrimos el archivo PDF en modo lectura binaria
        with open(ruta_pdf, 'rb') as archivo_pdf:
            lector_pdf = PyPDF2.PdfReader(archivo_pdf)
            num_paginas = len(lector_pdf.pages)

            # extraemos el texto de cada pagina del PDF
            texto_completo = ""
            for pagina in range(num_paginas):
                pagina_obj = lector_pdf.pages[pagina]
                texto_completo += pagina_obj.extract_text()

            # y por ultimo guardamos el texto en un archivo de texto
            with open(ruta_salida_txt, 'w', encoding='utf-8') as archivo_txt:
                archivo_txt.write(texto_completo)

            print(f"Archivo PDF convertido a texto en: {ruta_salida_txt}")

    except Exception as e:
        print(f"Error al convertir el archivo PDF: {e}")

ruta_pdf = "escribe la ruta de tu archivo pdf"
ruta_salida_txt = "escribe la salida o donde se guardara la salida debe ser .txt"

convertir_pdf_a_texto(ruta_pdf, ruta_salida_txt)
