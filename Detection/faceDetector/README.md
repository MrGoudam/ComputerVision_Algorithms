# Ru
## О поиске лица с помощью метода Виолы — Джонса
### Описание
Для поиска лица на изображении можно использовать метод Виолы-Джонса. 

Метод Виолы-Джонса — алгоритм, позволяющий обнаруживать объекты на изображениях в реальном времени. Хотя алгоритм может распознавать объекты на изображениях, основной задачей при его создании было обнаружение лиц.

Для того, чтобы использовать данный метод, нам потребуется скачать предварительно обученный каскад Хаара или обучить его самим.

Далее, все сводится к вызову метода detectMultiScale. 

detectMultiScale — общая функция для распознавания как лиц, так и объектов. Чтобы функция искала именно лица, нам необходимо передать ей соответствующий каскад. 

Функция detectMultiScale принимает 4 параметра:
1. Обрабатываемое изображение в градации серого;
2. Параметр scaleFactor. Некоторые лица могут быть больше других, поскольку находятся ближе, чем остальные. Этот параметр компенсирует перспективу;
3. Алгоритм распознавания использует скользящее окно во время распознавания объектов. Параметр minNeighbors определяет количество объектов вокруг лица. То есть чем больше значение этого параметра, тем больше аналогичных объектов необходимо алгоритму, чтобы он определил текущий объект, как лицо. Слишком маленькое значение увеличит количество ложных срабатываний, а слишком большое сделает алгоритм более требовательным;
4. minSize — непосредственно размер этих областей.

Функция detectMultiScale возвращает координаты найденных объектов.

### Достоинства
+ Устойчивость к смене освещения;
+ Устойчивость к шуму;
+ Устойчивость к изменениям размера объекта.

### Недостатки 
+ Не самый точный метод поиска;
+ Не устойчив к поворотам объекта;
+ В случае специфической задачи, нужно будет обучать свой каскад.

### Когда применять
+ Когда необходимо найти лицо на изображении.

### Ссылки на дополнительные источники
* [Download Haar Cascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)
* [Face Detection – OpenCV, Dlib and Deep Learning](https://www.learnopencv.com/face-detection-opencv-dlib-and-deep-learning-c-python/)
* [Выделение объектов на изображении по методу Виолы-Джонса](https://api-2d3d-cad.com/viola-jones-method/)


# En
## About 
### Description
You can use the Viola-Jones method to find a face in an image.

The Viola-Jones method is an algorithm that detects objects in images in real time. Although the algorithm can recognize objects in images, face detection was its primary focus.

In order to use this method, we need to download a pretrained Haar cascade or train it ourselves.

Further, it all boils down to calling the detectMultiScale method.

detectMultiScale is a general function for recognizing both faces and objects. In order for the function to search specifically for faces, we need to pass it the appropriate cascade.

The detectMultiScale function takes 4 parameters:
1. The processed image in grayscale;
2. scaleFactor parameter. Some faces may be larger than others because they are closer than others. This parameter compensates for perspective;
3. The recognition algorithm uses a sliding window during object recognition. The minNeighbors parameter determines the number of objects around the face. That is, the larger the value of this parameter, the more similar objects the algorithm needs in order for it to define the current object as a face. Too small a value will increase the number of false positives, and too large will make the algorithm more demanding;
4. minSize is the actual size of these areas.

The detectMultiScale function returns the coordinates of the found objects.

### Advantages
+ Resistant to changing lighting;
+ Noise resistance;
+ Resistance to changes in the size of the object.

### Disadvantages
+ Not the most accurate search method;
+ Not resistant to object turns;
+ In the case of a specific task, you will need to train your cascade.

### When to apply
+ When you need to find a face in an image.


## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| Numpy	    |	1.18.4
| OpenCV	|	 4.3.0



