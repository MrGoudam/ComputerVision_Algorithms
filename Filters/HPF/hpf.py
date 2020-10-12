import cv2
import numpy as np
import matplotlib.pyplot as plt


def autoCanny(image, sigma=0.33):
    # вычисляем среднее значение яркости пикселей
    v = np.median(image)

    # вычисляем ограничивающие значения
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))

    # применяем Канни и возвращаем результат
    return cv2.Canny(image, lower, upper)


if __name__ == '__main__':
    # Путь к данным
    path_image = 'data/image/Lenna.png'

    # Загрузка данных
    img = cv2.imread(path_image)

    # Подготовка данных
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny
    img_canny = cv2.Canny(gray_img, 125, 255)
    img_auto_anny = autoCanny(gray_img)

    # Laplacian
    img_laplacian = cv2.Laplacian(gray_img, -1)

    # Sobel
    img_sobel_x = cv2.Sobel(gray_img, -1, 1, 0)
    img_sobel_y = cv2.Sobel(gray_img, -1, 0, 1)
    img_sobel_xy = cv2.Sobel(gray_img, -1, 1, 1)
    img_sobel = img_sobel_x + img_sobel_y

    # Scharr
    img_scharr_x = cv2.Scharr(gray_img, -1, 1, 0)
    img_scharr_y = cv2.Scharr(gray_img, -1, 0, 1)
    img_scharr = img_scharr_x + img_scharr_y

    # Вывод результата
    cv2.imshow('Image', img)

    fig_canny, axs_canny = plt.subplots(1, 2)
    axs_canny[0].imshow(img_canny, cmap='gray')
    axs_canny[0].set_title('Canny')
    axs_canny[1].imshow(img_auto_anny, cmap='gray')
    axs_canny[1].set_title('Auto Canny')
    fig_canny.canvas.set_window_title('Canny')

    fig_laplacian, axs_laplacian = plt.subplots(1, 1)
    axs_laplacian.imshow(img_laplacian, cmap='gray')
    axs_laplacian.set_title('Laplacian')
    fig_laplacian.canvas.set_window_title('Laplacian')

    fig_sobel, axs_sobel = plt.subplots(1, 4)
    axs_sobel[0].imshow(img_sobel_x, cmap='gray')
    axs_sobel[0].set_title('Sobel X')
    axs_sobel[1].imshow(img_sobel_y, cmap='gray')
    axs_sobel[1].set_title('Sobel Y')
    axs_sobel[2].imshow(img_sobel_xy, cmap='gray')
    axs_sobel[2].set_title('Sobel XY')
    axs_sobel[3].imshow(img_sobel, cmap='gray')
    axs_sobel[3].set_title('Sobel')
    fig_sobel.canvas.set_window_title('Sobel')

    fig_scharr, axs_scharr = plt.subplots(1, 3)
    axs_scharr[0].imshow(img_scharr_x, cmap='gray')
    axs_scharr[0].set_title('Scharr X')
    axs_scharr[1].imshow(img_scharr_y, cmap='gray')
    axs_scharr[1].set_title('Scharr Y')
    axs_scharr[2].imshow(img_scharr, cmap='gray')
    axs_scharr[2].set_title('Scharr')
    fig_scharr.canvas.set_window_title('Scharr')

    plt.show()
    cv2.waitKey()