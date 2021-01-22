# Ru
## О вычитание фона 
### Описание
Вычитание фона (BS) - это распространенный и широко используемый метод для создания маски переднего плана с помощью статических камер.

Как следует из названия, BS вычисляет маску переднего плана, выполняя вычитание между текущим кадром и моделью фона, содержащей статическую часть сцены или, в более общем смысле, все, что можно рассматривать как фон с учетом характеристик наблюдаемой сцены.

Фоновое моделирование состоит из двух основных этапов:
1. Инициализация фона.
2. Обновление фона.

В OpenCV есть 2 алгоритма инициализации фона:
1. createBackgroundSubtractorMOG2;
2. createBackgroundSubtractorKNN.

Данные алгоритмы принимают следующие аргументы:
1. history - длина истории фона;
2. varThreshold (MOG2) - порог квадрата расстояния Махаланобиса между пикселем и моделью, чтобы определить, хорошо ли описывается пиксель фоновой моделью;<br>
   dist2Threshold (KNN) - пороговое значение квадрата расстояния между пикселем и образцом, чтобы определить, близок ли пиксель к этому образцу;
3. detectShadows - обнаружение теней. Если True, алгоритм обнаруживает и помечает тени серым цветом. Это функция немного снижает скорость работы, поэтому, если она не нужна, установите значение False.

За обновления фона, у объектов BackgroundSubtractorKNN и BackgroundSubtractorMOG2, отвечает метод apply, который принимает в качестве аргумента изображение.

### Требования
+ Статичная камера.
+ Статичный фон. 

### Достоинства
+ Позволяет найти движущиеся объекты на изображении.

### Недостатки 
+ На выходной маске остается информация о фоне.
+ Если движется фон, то движение объекта может затеряться.

### Когда применять
+ Алгоритм вычитания фона следует применять тогда, когда необходимо найти движущиеся объекты на видео и условия съемки удовлетворяют требованиям к применению данного алгоритма. 

### Ссылки на дополнительные источники
* [Documentation Background Subtractor](https://docs.opencv.org/master/de/de1/group__video__motion.html)


# En
## About background subtractor
### Description
Background subtraction (BS) is a common and widely used technique for generating a foreground mask by using static cameras.

As the name suggests, BS calculates the foreground mask performing a subtraction between the current frame and a background model, containing the static part of the scene or, more in general, everything that can be considered as background given the characteristics of the observed scene.

Background modeling consists of two main steps:
1. Background Initialization.
2. Background Update.

OpenCV has 2 background initialization algorithms:
1. createBackgroundSubtractorMOG2;
2. createBackgroundSubtractorKNN.

These algorithms take the following arguments:
1. history - length of the history;
2. varThreshold (MOG2) - threshold on the squared Mahalanobis distance between the pixel and the model to decide whether a pixel is well described by the background model;<br>
   dist2Threshold (KNN) - threshold on the squared distance between the pixel and the sample to decide whether a pixel is close to that sample;
3. detectShadows - if true, the algorithm will detect shadows and mark them. It decreases the speed a bit, so if you do not need this feature, set the parameter to false.

The apply method is responsible for updating the background for the BackgroundSubtractorKNN and BackgroundSubtractorMOG2 objects, which takes an image as an argument.

### Requirements
+ Static chamber.
+ Static background.

### Advantages
+ Finds moving objects in the image.

### Disadvantages
+ The background information remains on the output mask.
+ If the background is moving, then the movement of the subject may be lost.

### When to apply
+ The background subtraction algorithm should be used when it is necessary to find moving objects in the video and the shooting conditions satisfy the requirements for the application of this algorithm.


## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| Numpy	    |	1.18.4
| OpenCV	|	 4.3.0



