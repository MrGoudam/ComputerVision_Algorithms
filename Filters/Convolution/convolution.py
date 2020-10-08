import cv2
import numpy as np

kernels = {'identity': np.array([[0, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 0]]),

           'edge_1': np.array([[1,  0, -1],
                               [0,  0,  0],
                               [-1, 0,  1]]),
           'edge_2': np.array([[ 0, -1., 0],
                               [-1,  4, -1],
                               [ 0, -1,  0]]),
           'edge_3': np.array([[-1, -1, -1],
                               [-1,  8, -1],
                               [-1, -1, -1]]),

           'sobel_x': np.array([[-1, 0, 1],
                                [-2, 0, 2],
                                [-1, 0, 1]]),
           'sobel_y': np.array([[ 1,  2,  1],
                                [ 0,  0,  0],
                                [-1, -2, -1]]),

           'boxBlur': 1/25 * np.ones((5, 5), dtype=np.float32)
           }


if __name__ == '__main__':
    # Путь к данным
    path_image = 'data/image/Lenna.png'

    # Загрузка данных
    img = cv2.imread(path_image)

    # Создаем фильтр для изображения
    kernel = kernels['boxBlur']

    # Проводим операцию свертки
    test = np.zeros_like(img)
    img_res = cv2.filter2D(img, -1, kernel, test)

    # Вывод результата
    cv2.imshow('Image', img)
    cv2.imshow('Result', img_res)
    cv2.imshow('test', test)
    cv2.waitKey()
