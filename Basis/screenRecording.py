import numpy as np
import cv2
from mss import mss
from PIL import Image

if __name__ == "__main__":
    # Настройки окна вывода
    cv2.namedWindow("screen", cv2.WINDOW_KEEPRATIO)
    cv2.resizeWindow("screen", 720, 405)

    # Часть экрана, которую будем снимать
    bbox = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

    # Начало работы с mss
    sct = mss()

    while 1:
        # Делаем скриншот части экрана
        #   P.S.: Для фул скрина используй метод shot
        sct_img = sct.grab(bbox)

        # Конвертируем скриншот для последующей обработки
        image = np.array(sct_img)

        # Выводим результат на экран
        cv2.imshow('screen', image)

        # Выходим из цикла
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()