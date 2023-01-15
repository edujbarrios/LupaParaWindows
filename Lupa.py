import cv2
import numpy as np
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller

def zoom(zoom_level):
    # Obtener captura de pantalla
    img = np.array(cv2.grab())
    height, width = img.shape[:2]

    # Obtener la posición del cursor
    mouse = Controller()
    x, y = mouse.position

    # Ajustar la posición del recuadro de acuerdo al nivel de zoom
    if zoom_level == "in":
        x1, y1, x2, y2 = x-100, y-100, x+100, y+100
    elif zoom_level == "out":
        x1, y1, x2, y2 = x-50, y-50, x+50, y+50

    # Crear una ventana para mostrar la imagen
    cv2.namedWindow("Zoom", cv2.WINDOW_NORMAL)

    if zoom_level == "in":
        # Aumentar el tamaño de la imagen gradualmente
        for i in range(10):
            keyboard = Controller()
            keyboard.press(Key.ctrl)
            keyboard.press("+")
            keyboard.release("+")
            keyboard.release(Key.ctrl)
            img = np.array(cv2.grab())
            cv2.imshow("Zoom", img[y1:y2, x1:x2])
            cv2.waitKey(100)
    elif zoom_level == "out":
        # Reducir el tamaño de la imagen gradualmente
        for i in range(10):
            keyboard = Controller()
            keyboard.press(Key.ctrl)
            keyboard.press("-")
            keyboard.release("-")
            keyboard.release(Key.ctrl)
            img = np.array(cv2.grab())
            cv2.imshow("Zoom", img)
            cv2.waitKey(100)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

zoom_level = input("Ingrese 'in' para acercar o 'out' para alejar: ")
zoom(zoom_level)
