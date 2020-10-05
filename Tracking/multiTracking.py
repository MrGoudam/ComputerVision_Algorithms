import cv2


def getCoordinateObjects(window_name, img):
    # Данная информация будет дублироваться в консоли, так как разработчики функции selectROIs не дали возможности
    # отключать вывод информации
    print("Finish the selection process by pressing ESC button!",
          "Select a ROI and then press SPACE or ENTER button!",
          "Cancel the selection process by pressing c button!",
          sep='\n', end='\n\n')
    return cv2.selectROIs(window_name, img)


if __name__ == '__main__':
    # Путь к данным
    path_video = 'data/video/ball.mp4'

    # Загрузка данных
    cap = cv2.VideoCapture(path_video)

    # Чтение кадра видео
    ret, frame = cap.read()
    if ret:
        # Получение объектов
        bbox = getCoordinateObjects('Get Objects', frame)
        cv2.destroyWindow('Get Objects')

        # Инициализация трекеров
        listTrackers = []
        for i, (x, y, w, h) in enumerate(bbox):
            print('Coordinates of object number {}: ({} {}) ({} {})'.format(i+1, x, y, x+w, y+h))
            tracker = cv2.TrackerCSRT_create()
            tracker.init(frame, (x, y, w, h))
            listTrackers.append(tracker)

    # Обработка видео
    while cap.isOpened():
        # Чтение кадра видео
        ret, frame = cap.read()
        if not ret:
            break

        # Обновление списка трекеров
        res_frame = frame.copy()
        temp_listTrackers = []
        for i, tracker in enumerate(listTrackers):
            success, boxes = tracker.update(frame)
            if success:
                temp_listTrackers.append(tracker)
                (x, y, w, h) = boxes
                p1 = (int(round(x)), int(round(y)))
                p2 = (int(round(x + w)), int(round(y + h)))
                cv2.rectangle(res_frame, p1, p2, (0, 0, 255), 2)
                cv2.putText(res_frame, 'Object ' + str(i + 1), p1, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            else:
                print('Object number {} is lost'.format(i + 1))
        listTrackers = temp_listTrackers

        # Вывод изображения на экран
        cv2.imshow("Result", res_frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
