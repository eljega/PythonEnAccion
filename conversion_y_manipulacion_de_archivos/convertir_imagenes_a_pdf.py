import os
from PIL import Image
from reportlab.pdfgen import canvas

def convert_png_to_pdf(source_folder, output_pdf):
    png_files = [f for f in os.listdir(source_folder) if f.endswith('.png')]
    png_files.sort()

    if not png_files:
        print("no se encontraron archivos .png en la carpeta.")
        return

    c = canvas.Canvas(output_pdf)

    for png_file in png_files:
        img_path = os.path.join(source_folder, png_file)
        try:
            img = Image.open(img_path)
            if img.mode == "RGBA":
                img = img.convert("RGB")
            
            width, height = img.size
            c.setPageSize((width, height))
            c.drawImage(img_path, 0, 0, width=width, height=height)
            c.showPage()
        except Exception as e:
            print(f"error al procesar {png_file}: {e}")

    c.save()
    print(f"PDF generado con exito: {output_pdf}")

source_folder = 'ruta donde tienes tus imagenes'
output_pdf = 'ruta donde guardaras tu archivo y nombre de tu .pdf'
convert_png_to_pdf(source_folder, output_pdf)
