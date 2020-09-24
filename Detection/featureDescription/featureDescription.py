import cv2
import numpy as np


def resizeImage(img, scale_percent):
    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation=cv2.INTER_AREA)


def isIntersected(point_1, point_2, point_3, point_4):
    max_val = np.max(np.array([point_1, point_2, point_3, point_4]))
    num_of_char = len(str(max_val))
    div = pow(10, num_of_char)

    ax1 = point_1[0] / div
    ay1 = point_1[1] / div

    ax2 = point_2[0] / div
    ay2 = point_2[1] / div

    bx1 = point_3[0] / div
    by1 = point_3[1] / div

    bx2 = point_4[0] / div
    by2 = point_4[1] / div

    v1 = (bx2 - bx1) * (ay1 - by1) - (by2 - by1) * (ax1 - bx1)
    v2 = (bx2 - bx1) * (ay2 - by1) - (by2 - by1) * (ax2 - bx1)
    v3 = (ax2 - ax1) * (by1 - ay1) - (ay2 - ay1) * (bx1 - ax1)
    v4 = (ax2 - ax1) * (by2 - ay1) - (ay2 - ay1) * (bx2 - ax1)

    return (v1 * v2 < 0.0) and (v3 * v4 < 0.0)


def featureDescription(img, tpl):
    # Инициализация дескриптора
    orb = cv2.ORB_create()

    # Ищем особые точки и вычисляем их дескрипторы
    kp_img, des_img = orb.detectAndCompute(img, None)
    kp_tpl, des_tpl = orb.detectAndCompute(tpl, None)

    # Проверяем наличие дескрипторов особых точек
    if des_img is None:
        return None, -1, None
    elif des_tpl is None:
        return None, None, -1

    # Сопоставляем дескрипторы особых точек
    matcher = cv2.BFMatcher()
    matches = matcher.knnMatch(des_tpl, des_img, k=2)
    return matches, kp_img, kp_tpl


def getGoodPoints(matches, dist_coeff):
    good = []
    if len(matches[0]) == 2:  # matcher.knnMatch возвращает форму данных в зависимости от k. В нашем случае k=2
        for m, n in matches:
            if m.distance < n.distance * dist_coeff:
                good.append(m)
    return good


def main():
    # Пути к данным
    path_image = 'data/images/book_3.jpg'
    path_template = 'data/templates/book.jpg'

    # Загрузка данных
    img = cv2.imread(path_image)
    tpl = cv2.imread(path_template)

    # Подготовка данных
    img = resizeImage(img, 1)
    tpl = resizeImage(tpl, 0.5)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_template = cv2.cvtColor(tpl, cv2.COLOR_BGR2GRAY)

    # Получаем особые точки
    matches, kp_img, kp_tpl = featureDescription(gray_img, gray_template)
    if matches is None:
        if kp_img == -1:
            print("Особые точки на изображении не найдены")
            return
        elif kp_tpl == -1:
            print("Особые точки на шаблоне не найдены")
            return

    # Отсекаем лишние особые точки
    good = getGoodPoints(matches, 0.8)

    # Обработка результата
    img_res = img.copy()
    colorFrame = (0, 255, 255)
    colorLine = (0, 0, 255)
    colorMatch = (0, 255, 0)
    min_match_count = 10

    if len(good) < min_match_count:
        print("Количество совпадений недостаточно - %d/%d" % (len(good), min_match_count))
    else:
        print('Количество совпадений: {}'.format(len(good)))

        # Преобразуем дескрипторы особых точек в точки
        pts_img = np.float32([kp_img[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)  # точки img
        pts_tpl = np.float32([kp_tpl[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)  # точки template

        M, mask = cv2.findHomography(pts_tpl, pts_img, cv2.RANSAC, 5.0)  # матрица преобразования координат точек

        if M is not None:
            # координаты точек рамки шаблона
            h, w = gray_template.shape  # размеры шаблона
            pts = np.asarray([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]], dtype=np.float32).reshape(-1, 1, 2)

            # выполняем преобразования координат точек рамки шаблона
            dst = cv2.perspectiveTransform(pts, M)

            # обрезаем рамку вылезшую за пределы картинки
            dst = [np.int32(np.abs(dst))]

            # проверяем рамку на соответствие правильной формы
            point_1 = dst[0][0][0]
            point_2 = dst[0][1][0]
            point_3 = dst[0][2][0]
            point_4 = dst[0][3][0]

            if isIntersected(point_1, point_3, point_2, point_4):
                # рисуем рамку вокруг найденного объекта
                img_res = cv2.polylines(img_res, dst, True, colorFrame, 2, cv2.LINE_AA)

                # добавляем линии пересечения
                cv2.line(img_res, tuple(point_1), tuple(point_3), colorLine, 1)
                cv2.line(img_res, tuple(point_2), tuple(point_4), colorLine, 1)
            else:
                print("[error] Не удалось создать рамку правильной формы. Возможно ложное срабатывание")

            # рисуем совпадения контрольных точек
            matchesMask = mask.ravel().tolist()
            draw_params = dict(matchColor=colorMatch, singlePointColor=None, matchesMask=matchesMask, flags=2)
            img_res = cv2.drawMatches(tpl, kp_tpl, img_res, kp_img, good, None, **draw_params)
        else:
            print("[error] Не удалось получить матрицу преобразования координат точек")

    # Вывод результата
    cv2.imshow('Image', img)
    cv2.imshow('Template', tpl)
    cv2.imshow('Result', img_res)
    cv2.waitKey()


if __name__ == '__main__':
    main()