import cv2


def getContours(img, area_range=None):
    # Получение контуров объекта
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Отсечение лишних контуров исходя из их площади
    if area_range:
        new_contours = []
        min_area = area_range[0]
        max_area = area_range[1]

        for cnt in contours:
            area = cv2.contourArea(cnt)
            print(area)
            if min_area <= area <= max_area:
                new_contours.append(cnt)

        contours = new_contours

    return contours


def approxContours(contours, truth=0.01):
    approx_contours = []
    for cnt in contours:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, truth * peri, True)
        approx_contours.append(approx)
    return approx_contours


def contourAnalysis(img, contours, name_figures):
    for cnt in contours:
        # Задаем имя объекта
        num_corners = len(cnt)
        name_object = name_figures.get(num_corners)

        if name_object == None:
            if num_corners > 10:
                name_object = 'Circuit'
            else:
                name_object = 'Unknown'

        # Получаем координаты области объекта
        x, y, w, h = cv2.boundingRect(cnt)
        p1 = (int(round(x)), int(round(y)))
        p2 = (int(round(x + w)), int(round(y + h)))

        # Добавляем дополнительную информацию
        cv2.rectangle(img, p1, p2, (200, 0, 100), 2)
        cv2.putText(img, name_object, (x+5, y+15), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)


if __name__ == '__main__':
    # Путь к данным
    path = 'data/images/figures.jpg'

    # Загрузка данных
    img = cv2.imread(path)

    # Предобработка данных
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    blur = cv2.GaussianBlur(gray, (5, 5), 1)
    edges = cv2.Canny(blur, 200, 255)

    # Получение и аппроксимирование контуров объектов
    contours = getContours(edges)
    contours = approxContours(contours)

    # Отрисовываем контур объектов на изображение
    img_contours = img.copy()
    cv2.drawContours(img_contours, contours, -1, (0, 0, 0), 3)

    # Проводим контурный анализ
    res_img = img.copy()
    name_figures = {3: 'Triangle',
                    4: 'Quadrilateral',
                    5: 'Pentagon',
                    6: 'Hexagon'}

    contourAnalysis(res_img, contours, name_figures)

    # Выводим изображения на экран
    cv2.imshow('image', img)
    cv2.imshow('edges', edges)
    cv2.imshow('contours', img_contours)
    cv2.imshow('result', res_img)
    cv2.waitKey()

