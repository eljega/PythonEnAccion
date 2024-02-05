import os
from pptx import Presentation
import fitz
from docx import Document

"""
Extractor de Contenido de Documentos

Este script extrae texto, imágenes y tablas de documentos PDF, Word y PowerPoint
y los organiza en carpetas separadas según el tipo de contenido.

Dependencias a instalar:
- pip install python-docx PyMuPDF python-pptx

Instrucciones de Uso:
1. Coloca los documentos de los que deseas extraer contenido en un directorio accesible.
2. Asegúrate de ajustar las rutas de los archivos en las variables correspondientes.
3. Ejecuta el script. El contenido extraído se organizará en carpetas separadas.
"""

def extraer_de_pdf(ruta_pdf):
    doc = fitz.open(ruta_pdf)
    texto = ""
    for pagina in doc:
        texto += pagina.get_text()
    
    # Guardar texto
    # Para guardar texto extraído de PDF
    with open(os.path.join("C:/Users/playg/escritorio/trabajo/python/repo_github", "pdf_texto.txt"), "w", encoding='utf-8') as f:
        f.write(texto)

    
    # Extraer imágenes (ejemplo básico)
    for i, pagina in enumerate(doc):
        imagenes = pagina.get_images(full=True)
        for img_index, img in enumerate(imagenes, start=1):
            base_image = doc.extract_image(img[0])
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = f"C:/Users/playg/escritorio/trabajo/python/repo_github{i+1}_img_{img_index}.{image_ext}"
            with open(image_path, "wb") as f:
                f.write(image_bytes)

def extraer_de_word(ruta_docx):
    doc = Document(ruta_docx)
    texto = "\n".join([p.text for p in doc.paragraphs])
    
    # Guardar texto
    with open(os.path.join("C:/Users/playg/escritorio/trabajo/python/repo_github", "word_texto.txt"), "w", encoding='utf-8') as f:
        f.write(texto)
    
    # Extraer imágenes (ejemplo básico)
    # Nota: python-docx no soporta extracción directa de imágenes. Considerar alternativas o manual.

def extraer_de_ppt(ruta_pptx):
    prs = Presentation(ruta_pptx)
    texto = ""
    for slide in prs.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                texto += shape.text + "\n"
    
    # Guardar texto
    with open(os.path.join("C:/Users/playg/escritorio/trabajo/python/repo_github", "ppt_texto.txt"), "w", encoding='utf-8') as f:
        f.write(texto)
    
    # Extraer imágenes (ejemplo básico)
    # Nota: python-pptx no soporta extracción directa de imágenes como PyMuPDF. Considerar alternativas o manual.

# Asegúrate de crear las carpetas necesarias o ajustar las rutas según tu estructura de directorios
if __name__ == "__main__":
    # Ejemplo de uso
    ruta_pdf = "C:/Users/playg/Downloads/torax.pdf"
    ruta_docx = "C:/Users/playg/Downloads/Base.docx"
    ruta_pptx = "C:/Users/playg/Downloads/CLASE.pptx"
    
    extraer_de_pdf(ruta_pdf)
    extraer_de_word(ruta_docx)
    extraer_de_ppt(ruta_pptx)
