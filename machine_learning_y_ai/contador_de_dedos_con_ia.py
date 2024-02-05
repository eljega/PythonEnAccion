"""
contador de Dedos con MediaPipe y OpenCV

este script puede detectar manos en tiempo real utilizando la camara
y contar el numero de dedos levantados. detecta tanto manos izquierdas como derechas y
mostrando el conteo en la pantalla.

Dependencias:
- OpenCV: lo usamos para el manejo de imagenes y la captura de video.
- MediaPipe: son los modelos de machine learning para la deteccion de manos y dedos.
  instalacion: pip install opencv-python mediapipe

Instrucciones:
1. debemos instalar las dependencias en un venv.
4. ejecuta y la aplicacion mostrara el feed de la camara web ya detectara tus manos, la primera vezz en ejecutar demora un poco.
5. Para salir de la ejecucion presiona la tecla q

que puede hacer:
- deteccion de manos en tiempo real.
- conteo de dedos levantados para cada mano detectada.
- diferencia mano izquierda y derecha.
- muestra el resultado del conteo directamente en la ventana de la camara.

"""
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

def count_fingers(hand_landmarks, hand_no):
    tip_ids = [mp_hands.HandLandmark.THUMB_TIP, mp_hands.HandLandmark.INDEX_FINGER_TIP,
               mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.HandLandmark.RING_FINGER_TIP,
               mp_hands.HandLandmark.PINKY_TIP]
    pip_ids = [mp_hands.HandLandmark.THUMB_IP, mp_hands.HandLandmark.INDEX_FINGER_PIP,
               mp_hands.HandLandmark.MIDDLE_FINGER_PIP, mp_hands.HandLandmark.RING_FINGER_PIP,
               mp_hands.HandLandmark.PINKY_PIP]

    finger_open = 0
    if hand_no == 0:  # Mano derecha
        if hand_landmarks.landmark[tip_ids[0]].x < hand_landmarks.landmark[pip_ids[0]].x:
            finger_open += 1
    else:  # Mano izquierda
        if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[pip_ids[0]].x:
            finger_open += 1

    for i in range(1, 5):
        if hand_landmarks.landmark[tip_ids[i]].y < hand_landmarks.landmark[pip_ids[i]].y:
            finger_open += 1

    return finger_open

cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("ignorando frame vacio.")
        continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            hand_no = idx % 2
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            fingers_counted = count_fingers(hand_landmarks, hand_no)
            cv2.putText(image, f'Hand {hand_no}: {fingers_counted}', (10, 50 + (30 * idx)), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('contador de dedos', image)
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
