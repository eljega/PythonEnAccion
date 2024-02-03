from transformers import pipeline

"""
Detector de Sentimiento en Texto

Este script utiliza un modelo preentrenado de NLP de la biblioteca 'transformers'
para analizar el sentimiento (positivo, negativo, neutral) de un texto ingresado por el usuario
como el modelo solo comprende ingles usaremos otro modelo de Helsinki de la misma biblioteca
transformers para traducir el texto antes de analizarlo.

Dependencias:
- Transformers y PyTorch.
  Instalación: pip install transformers torch sentencepiece

Instrucciones de Uso:
1. Instala las dependencias si aún no lo has hecho.
2. Ejecuta el script. Se te pedirá que ingreses un texto.
3. El script analizará el sentimiento del texto y mostrará el resultado.

este script es un ejemplo muy basico de comprension de sentimientos, te recomiendo experimentar
y leer su documentacion para profundizar en el.
"""

# aqui inicializamos el traductor para cambiar el texto de español a ingles
traductor = pipeline('translation', model='Helsinki-NLP/opus-mt-es-en')

# inicializamos pipeline para analizar el sentimiento
analizador_sentimientos = pipeline('sentiment-analysis')

def traducir_y_analizar_sentimiento(texto_espanol):
    """
    aqui se traduce el texto del español al ingles y luego analiza su sentimiento.

    Args:
        texto_espanol (str): Texto para analizar.
    """

    traduccion = traductor(texto_espanol, max_length=512)
    texto_ingles = traduccion[0]['translation_text']
    print(f"Texto traducido al inglés: {texto_ingles}")

    resultado_sentimiento = analizador_sentimientos(texto_ingles)
    sentimiento = resultado_sentimiento[0]['label']
    confianza = resultado_sentimiento[0]['score']
    print(f"Sentimiento detectado: {sentimiento} con una confianza del {confianza:.2f}")

if __name__ == "__main__":
    texto_usuario = input("escribe una frase o di como te sientes: ")
    traducir_y_analizar_sentimiento(texto_usuario)
