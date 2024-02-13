"""
script de clasificacion de imagenes con interfaz grafica y traduccion al español
--------------------------------------------------------------------------------

- en este script utilizamos ImageAI y un modelo ResNet50 preentrenado para clasificar el contenido de una imagen
  mostrando las predicciones con sus probabilidades, incorporando una interfaz grafica de usuario
  mediante Tkinter. las predicciones se traducen al español utilizando la
  biblioteca 'googletrans'.


requisitos:
- Python 3.8 o superior.
- Bibliotecas: ImageAI, googletrans==4.0.0-rc1, TensorFlow, Keras, Pillow (para manejo de imagenes en Tkinter).

- instalacion de Dependencias:
    Para instalar todas las dependencias necesarias, ejecuta el siguiente comando en tu terminal:
    pip install imageai googletrans==4.0.0-rc1 tensorflow pillow


uso:
1. Descarga el modelo ResNet50 ('resnet50-19c8e357.pth') desde el repositorio de 
    ImageAI y guardalo en el mismo directorio, aqui te dejo el link: https://imageai.readthedocs.io/en/latest/prediction/index.html
2. ejecuta el script y se abrira la interfaz grafica.
3. Utiliza el boton "Seleccionar Imagen" para elegir una imagen desde tu sistema de archivos.
4. El script clasificara la imagen seleccionada y mostrara las predicciones con sus probabilidades en la interfaz
    La prediccion de mayor probabilidad se mostrara traducida al español junto con otras
    posibles identificaciones en la imagen.

"""

# importamos las bibliotecas necesarias
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from imageai.Classification import ImageClassification
from googletrans import Translator
from PIL import Image, ImageTk

# inicializamos la clasificacion de imagen y carga el modelo
def load_model():
    execution_path = os.getcwd()
    prediction.setModelTypeAsResNet50()
    prediction.setModelPath(os.path.join(execution_path, "resnet50-19c8e357.pth"))
    prediction.loadModel()

# funcion para seleccionar una imagen desde el sistema de archivos
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        predictions, probabilities = prediction.classifyImage(file_path, result_count=5)
        image = Image.open(file_path)
        image = image.resize((200, 200), Image.Resampling.LANCZOS)  # Modificado aqui
        image_tk = ImageTk.PhotoImage(image)
        panel_image.config(image=image_tk)
        panel_image.image = image_tk
        show_predictions(predictions, probabilities)

# muestra las predicciones en la interfaz grafica
def show_predictions(predictions, probabilities):
    text = ""
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        try:
            translated = translator.translate(eachPrediction, src='en', dest='es')
            prediction_text = translated.text
        except Exception as e:
            prediction_text = eachPrediction
        text += f"{prediction_text} : {eachProbability:.2f}%\n"
    text_predictions.config(text=text)

# configuramos de la interfaz grafica
def configure_gui():
    window.title("clasificador de imagenes con Tkinter")
    window.geometry('400x400')

    btn_cargar_image = tk.Button(window, text="Seleccionar imagen", command=select_image)
    btn_cargar_image.pack()

    global panel_image
    panel_image = tk.Label(window)
    panel_image.pack()

    global text_predictions
    text_predictions = tk.Label(window, text="", justify=tk.LEFT)
    text_predictions.pack()

if __name__ == "__main__":
    prediction = ImageClassification()
    translator = Translator()

    load_model()

    window = tk.Tk()
    panel_image = None
    text_predictions = None

    configure_gui()
    
    window.mainloop()
