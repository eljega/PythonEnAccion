"""

Script de Clasificacion de Imágenes con Traduccion al Español
-------------------------------------------------------------

- en este script utilizamos ImageAI y un modelo ResNet50 preentrenado para clasificar el contenido de una imagen
  mostrando las predicciones con sus probabilidades. las predicciones se traducen al español utilizando la
  biblioteca 'googletrans'.

requisitos:
- Python 3.8 o superior
- ImageAI, googletrans==4.0.0-rc1, TensorFlow, Keras

instalacion de dependencias:
pip install imageai googletrans==4.0.0-rc1 tensorflow

Uso:
1. Coloca una imagen en el directorio del script (ej. 'carro.jpg').
2. Descarga el modelo ResNet50 ('resnet50-19c8e357.pth') desde el repositorio
    de ImageAI y guárdalo en el mismo directorio, aqui te dejo el link: https://imageai.readthedocs.io/en/latest/prediction/index.html
3. Ejecuta el script

El script identificará los objetos en la imagen y mostrará los resultados traducidos al español.
mostrara principalmente la prediccion con mayor probabilidad y su respectiva traduccion y otros
objetos que pueda identificar en la imagen.
La eficacia de la traduccion puede variar segun la precision del servicio Google Translate.

"""



from imageai.Classification import ImageClassification
import os
from googletrans import Translator, LANGUAGES

# establecemos el directorio actual para ejecutar el script
execution_path = os.getcwd()

# creamos una instancia de la clase ImageClassification
prediction = ImageClassification()

# seleccionamos el modelo ResNet50 para la clasificacion
prediction.setModelTypeAsResNet50()
prediction.setModelPath(os.path.join(execution_path, "resnet50-19c8e357.pth")) # debes colocar la ruta exacta donde tienes este archivo

# cargamos el modelo
prediction.loadModel()

# realizamos la clasificacion de la imagen y obtenemos las predicciones y sus probabilidades
predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "telefono.jpg"), result_count=5)

# creamos una instancia de la clase Translator
translator = Translator()

# imprimimos las predicciones y sus probabilidades
for eachPrediction, eachProbability in zip(predictions, probabilities):
    try:
        # traducimos la prediccion al español
        translated = translator.translate(eachPrediction, src='en', dest='es')
        prediction_text = translated.text
    except Exception as e:
        print(f"Error al traducir '{eachPrediction}': {e}")
        prediction_text = eachPrediction  # si no se puede traducir usamos la prediccion original
    
    print(f"{prediction_text} : {eachProbability:.2f}%")

# traducimos la prediccion con mayor probabilidad al español
try:
    major_translation = translator.translate(predictions[0], src='en', dest='es').text
    second_major_translation = translator.translate(predictions[1], src='en', dest='es').text
except Exception as e:
    major_translation = predictions[0]
    second_major_translation = predictions[1]

print(f"\nTu imagen contiene un '{major_translation}' con una probabilidad de {probabilities[0]:.2f}%.")
print(f"\nO tambien puede ser '{second_major_translation}' con una probabilidad de {probabilities[0]:.2f}%.")
