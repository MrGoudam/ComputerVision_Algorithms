import cv2
import numpy as np


def matchTemplate(img, pattern, only_object=True, threshold=0.95, method=cv2.TM_CCOEFF_NORMED):
    # Сопоставление с шаблоном
    res = cv2.matchTemplate(img, pattern, method)

    # Получения координат
    coordinates = []
    if only_object:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            coordinates.append(min_loc)

        else:
            coordinates.append(max_loc)

    else:
        loc = np.where(res >= threshold)

        for (x, y) in zip(*loc[::-1]):
            coordinates.append((x, y))

    return coordinates


def approxCoordinates(coordinates, coefficient=5):
    # Создаем ярлык для координат
    labels = []
    labels_and_coords = []
    for i in range(len(coordinates)):
        x = int(round(coordinates[i][0] / coefficient) * coefficient)
        y = int(round(coordinates[i][1] / coefficient) * coefficient)
        labels.append(x*y)
        labels_and_coords.append([x*y, coordinates[i]])

    # Ищем уникальные ярлыки
    unique_labels = set(labels)

    # Разбиваем координаты на группы по ярлыкам
    coord_group = []
    for unique_label in unique_labels:
        group = []
        for label, coord in labels_and_coords:
            if unique_label == label:
                group.append(coord)
        coord_group.append(group)

    # Находим средние значение координат в группе
    new_coordinates = []
    for coord in coord_group:
        new_x = 0
        new_y = 0
        for x, y in coord:
            new_x += x
            new_y += y
        new_x = int(round(new_x / len(coord)))
        new_y = int(round(new_y / len(coord)))
        new_coordinates.append((new_x, new_y))
    return new_coordinates


if __name__ == '__main__':
    # Пути к данным
    path_image = 'data/images/mario.jpg'
    path_pattern = 'data/pattern/coin.jpg'

    # Загрузка данных
    img = cv2.imread(path_image)
    pattern = cv2.imread(path_pattern)

    # Подготовка данных
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_pattern = cv2.cvtColor(pattern, cv2.COLOR_BGR2GRAY)

    # Сопоставление с шаблоном
    coordinates = matchTemplate(gray_img, gray_pattern, False, 0.9)
    print('Number of objects after matchTemplate: {}'.format(len(coordinates)))

    # Аппроксимирование координат
    coordinates = approxCoordinates(coordinates, 10)
    print('Number of objects after approximation: {}'.format(len(coordinates)))

    # Отображение результата на изображении
    res_img = img.copy()
    w, h = gray_pattern.shape[::-1]

    for loc in coordinates:
        top_left = loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(res_img, top_left, bottom_right, (0, 0, 200), 3)

    # Вывод результата
    cv2.imshow('Image', img)
    cv2.imshow('Pattern', pattern)
    cv2.imshow('Result', res_img)

    cv2.waitKey()