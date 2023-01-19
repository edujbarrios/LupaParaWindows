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
    
    def draw_shape(img, shape_type):
    if shape_type == "circle":
        # Obtener la posición del cursor
        mouse = Controller()
        x, y = mouse.position

        # Dibujar un círculo en la posición del cursor
        cv2.circle(img, (x, y), 50, (0, 0, 255), -1)
    elif shape_type == "rectangle":
        # Obtener la posición del cursor
        mouse = Controller()
        x, y = mouse.position

        # Dibujar un rectángulo en la posición del cursor
        cv2.rectangle(img, (x-50, y-50), (x+50, y+50), (0, 255, 0), -1)
    elif shape_type == "line":
        # Obtener la posición del cursor
        mouse = Controller()
        x1, y1 = mouse.position
        print("Press the mouse button again at the end point of the line")
        with mouse.pressed(Button.left):
            x2, y2 = mouse.position
        # Dibujar una línea desde la posición del cursor inicial hasta la posición final
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 5)
    cv2.imshow("Shape", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

zoom_level = input("Ingrese 'in' para acercar o 'out' para alejar: ")
zoom(zoom_level)
