import numpy as np
import tensorflow as tf
from keras.api._v2.keras import datasets, layers, models
import matplotlib.pyplot as plt


"""
Clasificador de Imagenes con TensorFlow

vamos a construir y entrenar un modelo simple de clasificacion de imagenes
utilizando TensorFlow y un conjunto de datos CIFAR-10. este modelo consiste en una secuencia de
capas convolucionales seguidas de capas de pooling y capas densas.

Dependencias:
- TensorFlow
  Instalacion: pip install tensorflow

Como usar:
1. nos aseguramos de haber instalado TensorFlow esta instalado en el entorno virtual.
2. ejecutamos este script para entrenar el modelo. Se descargara automaticamente el CIFAR-10
   durante el proceso.
3. Una vez entrenado el modelo se evaluara con un conjunto de datos de prueba.
4. Puedes utilizar la funcion 'predict_image' para hacer predicciones usando el modelo entrenado.
5. El modelo se guarda en el sistema de archivos para su posterior uso.

"""

# cargamos y preparamos del conjunto de datos CIFAR-10
(train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
train_images, test_images = train_images / 255.0, test_images / 255.0

# definimos de las etiquetas de clase para el conjunto de datos CIFAR-10
class_names = ['avión', 'automóvil', 'pájaro', 'gato', 'venado',
               'perro', 'rana', 'caballo', 'barco', 'camión']

# definimos del modelo de clasificacion de imagenes
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10, validation_data=(test_images, test_labels))

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nPrecision del conjunto de prueba:', test_acc)

# Funcion para realizar predicciones con el modelo
def predict_image(image, model, class_names):
    """Realiza una prediccion usando el modelo entrenado para una única imagen."""
    image = np.expand_dims(image, 0)  # Agregar la imagen en un batch de tamaño 1
    prediction = model.predict(image)
    plt.figure()
    plt.imshow(image[0], cmap=plt.cm.binary)
    plt.title(class_names[np.argmax(prediction)])
    plt.show()
    print(f"Esta imagen probablemente pertenece a: {class_names[np.argmax(prediction[0])]}")

predict_image(test_images[1], model, class_names)

# guardamos el modelo entrenado para uso futuro
model.save('mi_modelo_clasificador.h5')