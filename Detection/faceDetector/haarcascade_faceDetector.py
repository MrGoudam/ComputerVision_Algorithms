import cv2

if __name__ == '__main__':
    # Пути к данным
    path_image = 'data/images/faces.jpg'
    path_cascade = 'data/haarcascade/haarcascade_frontalface_default.xml'

    # Загрузка данных
    img = cv2.imread(path_image)
    face_cascade = cv2.CascadeClassifier(path_cascade)

    # Подготовка данных
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Поиск лиц
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
    print('Количество найденных лиц: {}'.format(len(faces)))

    # Рисуем рамку вокруг найденных лиц
    res_img = img.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(res_img, (x, y), (x+w, y+h), (255, 255, 0), 2)

    # Вывод результата
    cv2.imshow('Image', img)
    cv2.imshow('Result', res_img)
    cv2.waitKey()
