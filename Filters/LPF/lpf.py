import cv2


def isIdentically(img_1, img_2):
    return (img_1 == img_2).all()


if __name__ == '__main__':
    # Путь к данным
    path_image = 'data/image/Lenna.png'

    # Загрузка данных
    img = cv2.imread(path_image)

    # Сглаживание путем усреднения
    filter_size = 9
    img_blur = cv2.blur(img, (filter_size, filter_size))
    img_boxFilter = cv2.boxFilter(img, -1, (filter_size, filter_size))
    print('Are blur and boxFilter the same? \n - {}'.format(isIdentically(img_blur, img_boxFilter)))

    # Гауссово сглаживание
    img_GaussianBlur = cv2.GaussianBlur(img, (filter_size, filter_size), 0)

    # Медианный фильтр
    img_medianBlur = cv2.medianBlur(img, filter_size)

    # Двустороннее сглаживание
    img_bilateralFilter = cv2.bilateralFilter(img, filter_size, 80, 80)

    # Вывод результата
    cv2.imshow('Image', img)
    cv2.imshow('Blur', img_blur)
    cv2.imshow('Box Filter', img_boxFilter)
    cv2.imshow('Gaussian Blur', img_GaussianBlur)
    cv2.imshow('Median Blur', img_medianBlur)
    cv2.imshow('Bilateral Filter', img_bilateralFilter)
    cv2.waitKey()
