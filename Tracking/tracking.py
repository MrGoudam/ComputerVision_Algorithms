import sys
import cv2


# Словарь всех трекеров в OpenCV
trackers = {'BOOSTING': cv2.TrackerBoosting_create(),
            'MIL': cv2.TrackerMIL_create(),
            'KCF': cv2.TrackerKCF_create(),
            'TLD': cv2.TrackerTLD_create(),
            'MEDIANFLOW': cv2.TrackerMedianFlow_create(),
            'GOTURN': cv2.TrackerGOTURN_create(),
            'MOSSE': cv2.TrackerMOSSE_create(),
            'CSRT': cv2.TrackerCSRT_create()}


def createTrackerByName(tracker_name):
    tracker = None
    if tracker_name in trackers:
        tracker = trackers[tracker_name]
    return tracker


def getCoordinateObject(window_name, img):
    return cv2.selectROI(window_name, img)


if __name__ == '__main__':
    # Путь к данным
    path_video = 'data/video/ball.mp4'

    # Загрузка данных
    cap = cv2.VideoCapture(path_video)

    # Чтение кадра видео
    ret, frame = cap.read()
    if ret:
        # Получение объектов
        bbox = getCoordinateObject('Get Objects', frame)
        cv2.destroyWindow('Get Objects')

        # Инициализация трекеров
        (x, y, w, h) = bbox
        tracker = createTrackerByName('CSRT')
        if tracker is None:
            print('Incorrect tracker name!', 'Available trackers are:', sep='\n')
            for t in trackers:
                print('\t{}'.format(t))
            sys.exit()
        tracker.init(frame, (x, y, w, h))
        print('Object coordinates: ({} {}) ({} {})'.format(x, y, x + w, y + h))

    # Обработка видео
    while cap.isOpened():
        # Чтение кадра видео
        ret, frame = cap.read()
        if not ret:
            break

        # Слежение за объектом
        success, box = tracker.update(frame)

        # Добавляем информаию на изображение
        res_frame = frame.copy()
        if success:
            (x, y, w, h) = box
            p1 = (int(round(x)), int(round(y)))
            p2 = (int(round(x + w)), int(round(y + h)))
            cv2.rectangle(res_frame, p1, p2, (0, 0, 255), 2)
        else:
            print('Object is lost')

        # Вывод изображения на экран
        cv2.imshow("Result", res_frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
