import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


preguntas = [
    {"pregunta": "¿En qué año nació Akira Toriyama?", "opciones": ["1955", "1960", "1950", "1945"], "correcta": "1955", "imagen": "imagenes/akira_1.png"},
    {"pregunta": "¿Cuál es la obra más famosa de Akira Toriyama?", "opciones": ["Naruto", "One Piece", "Dragon Ball", "Bleach"], "correcta": "Dragon Ball", "imagen": "imagenes/akira_2.png"},
    {"pregunta": "¿Qué personaje de Dragon Ball fue diseñado primero?", "opciones": ["Goku", "Bulma", "Vegeta", "Piccolo"], "correcta": "Goku", "imagen": "imagenes/akira_3.png"},
    {"pregunta": "¿Cuál es el verdadero nombre de Goku?", "opciones": ["Kakarot", "Yamcha", "Gohan", "Trunks"], "correcta": "Kakarot", "imagen": "imagenes/akira_4.jpg"},
    {"pregunta": "¿De qué planeta es Vegeta?", "opciones": ["Tierra", "Namek", "Vegeta", "Marte"], "correcta": "Vegeta", "imagen": "imagenes/akira_5.png"},
    {"pregunta": "¿Cómo se llama la esposa de Goku?", "opciones": ["Bulma", "Chi-Chi", "Videl", "Pan"], "correcta": "Chi-Chi", "imagen": "imagenes/akira_6.png"},
    {"pregunta": "¿Cuál de estos personajes NO es un Saiyajin?", "opciones": ["Goku", "Vegeta", "Frieza", "Gohan"], "correcta": "Frieza", "imagen": "imagenes/akira_7.png"},
    {"pregunta": "¿Quién es el creador de los androides?", "opciones": ["Dr. Gero", "Dr. Brief", "Bulma", "Dr. Myuu"], "correcta": "Dr. Gero", "imagen": "imagenes/akira_8.png"},
    {"pregunta": "¿Qué objeto se usa para convocar al dragón Shenron?", "opciones": ["Esferas del Dragón", "Tarjetas de héroe", "Cristales mágicos", "Piedras eternas"], "correcta": "Esferas del Dragón", "imagen": "imagenes/akira_9.png"},
    {"pregunta": "¿Cuál es el nombre del maestro de Goku?", "opciones": ["Maestro Roshi", "Maestro Karin", "Maestro Mutaito", "Mr. Popo"], "correcta": "Maestro Roshi", "imagen": "imagenes/akira_10.png"},
]

ventana = tk.Tk()
ventana.title("Tributo a Akira Toriyama")

pregunta_actual = 0
puntaje = 0

def seleccionar_respuesta(opcion, boton):
    global pregunta_actual, puntaje
    correcta = preguntas[pregunta_actual]["correcta"]
    if opcion == correcta:
        puntaje += 1
        boton.config(bg="green")
    else:
        boton.config(bg="red")
    ventana.after(2000, siguiente_pregunta)

def siguiente_pregunta():
    global pregunta_actual
    pregunta_actual += 1
    if pregunta_actual < len(preguntas):
        cargar_pregunta()
    else:
        mostrar_resultados()
    for boton in botones_respuesta:
        boton.config(bg='SystemButtonFace')

from PIL import Image, ImageTk

def cargar_pregunta():
    global imagen_actual
    texto_pregunta.config(text=preguntas[pregunta_actual]["pregunta"])

    ruta_imagen = preguntas[pregunta_actual]["imagen"]
    imagen_original = Image.open(ruta_imagen)
    
    ancho_maximo = 450
    alto_maximo = 250
    
    factor_de_escalado = min(ancho_maximo / imagen_original.width, alto_maximo / imagen_original.height)
    ancho_nuevo = int(imagen_original.width * factor_de_escalado)
    alto_nuevo = int(imagen_original.height * factor_de_escalado)

    imagen_redimensionada = imagen_original.resize((ancho_nuevo, alto_nuevo), Image.Resampling.LANCZOS)
    
    imagen_actual = ImageTk.PhotoImage(imagen_redimensionada)
    imagen_pregunta.config(image=imagen_actual)

    for i, opcion in enumerate(preguntas[pregunta_actual]["opciones"]):
        botones_respuesta[i].config(text=opcion, 
                                    command=lambda o=opcion, b=botones_respuesta[i]: seleccionar_respuesta(o, b), 
                                    bg='SystemButtonFace', 
                                    relief='raised')


def mostrar_resultados():
    mensaje_final = f"Gracias por jugar. Tu puntaje fue: {puntaje}/{len(preguntas)}. Gracias, Akira Toriyama, por darnos la mejor infancia posible a través de tus historias."
    messagebox.showinfo("Fin del juego", mensaje_final)
    ventana.destroy()

texto_pregunta = tk.Label(ventana, text="", wraplength=300)
texto_pregunta.pack(pady=(20, 10))

imagen_pregunta = tk.Label(ventana)
imagen_pregunta.pack(pady=10)

botones_respuesta = []
for _ in range(4):
    boton = tk.Button(ventana, text="", command=lambda: None, width=20)
    boton.pack(pady=5)
    botones_respuesta.append(boton)

ventana.geometry("500x500")

cargar_pregunta()
ventana.mainloop()
