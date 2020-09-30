import cv2

if __name__ == '__main__':
    # Путь к данным
    path_video = 'data/video/moscow.mp4'

    # Загрузка видео и инициализация функции вычитания фона
    cap = cv2.VideoCapture(path_video)
    fgbg = cv2.createBackgroundSubtractorKNN(history=200, dist2Threshold=100, detectShadows=True)

    # Обработка видео
    while cap.isOpened():
        # Чтение кадра видео
        ret, frame = cap.read()
        if not ret:
            break

        # Подготовка данных
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Уменьшаем количество шума
        blur = 5
        gray_frame = cv2.blur(gray_frame, (blur, blur))

        # Получаем маску переднего плана
        fgmask = fgbg.apply(gray_frame)

        # Вывод изображения на экран
        cv2.imshow('frame', frame)
        cv2.imshow('fgmask', fgmask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()