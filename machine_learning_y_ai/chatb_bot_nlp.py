import nltk
from nltk.corpus import wordnet as wn
from nltk.metrics import edit_distance

# nltk.download('punkt') # Descomenta si es la primera vez que ejecutas NLTK
# nltk.download('wordnet') # Descomenta si es la primera vez que ejecutas NLTK
# nltk.download('omw-1.4') # Descomenta si es la primera vez que ejecutas NLTK

"""
Bot de Chat Simple con NLTK

Este script crea un bot de chat simple que puede reconocer saludos y responder a ellos.
Utiliza NLTK, una biblioteca para la construccion de programas Python que trabajan con datos de lenguaje humano.

Instrucciones:
- nos aseguramos de que NLTK esta instalado: `pip install nltk`
- necesitamos descargar los recursos de NLTK 'punkt' y 'wordnet' si es la primera vez que lo usamos NLTK.
- Ejecuta el script y comienza a chatear con el bot escribiendo tus saludos.
- Escribe 'salir' para finalizar el chat.

Este bot esta pensado como una demostracion basica de NLP y no es un bot de chat avanzado, pero puede servir como un punto de partida para tu proyecto.
"""

lemmatizer = nltk.WordNetLemmatizer()

saludos = {
    'hola': '¡Hola! ¿Cómo estás?',
    'qué tal': 'Bien, ¿y tú qué tal?',
    'buenos días': '¡Buenos días! Espero que tengas un día maravilloso.',
    'buenas tardes': 'Buenas tardes, ¿en qué puedo ayudarte hoy?',
    'buenas noches': 'Buenas noches. ¿Todo bien?'
}

def encontrar_saludo_cercano(entrada_usuario):
    distancia_minima = float('inf')
    saludo_cercano = None
    for saludo in saludos.keys():
        distancia = edit_distance(entrada_usuario, saludo)
        if distancia < distancia_minima:
            distancia_minima = distancia
            saludo_cercano = saludo
    return saludo_cercano if distancia_minima < len(saludo_cercano) / 2 else None

def obtener_respuesta(entrada_usuario):
    entrada_usuario = ' '.join([lemmatizer.lemmatize(palabra) for palabra in nltk.word_tokenize(entrada_usuario.lower())])
    saludo_cercano = encontrar_saludo_cercano(entrada_usuario)
    if saludo_cercano:
        return saludos[saludo_cercano]
    return "Lo siento, no entendí eso. ¿Puedes decirlo de otra manera?"

def chat_bot():
    print("Bot de Chat (escribe 'salir' para terminar)")
    while True:
        entrada_usuario = input("Tú: ")
        if entrada_usuario.lower() == 'salir':
            print("Bot: ¡Adiós! Fue un placer charlar contigo.")
            break
        respuesta = obtener_respuesta(entrada_usuario)
        print(f"Bot: {respuesta}")

if __name__ == "__main__":
    chat_bot()
