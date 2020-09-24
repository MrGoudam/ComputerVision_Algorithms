# Ru
## О методе особых точек
### Описание
Для того, чтобы использовать метод особых точек, нам необходимо иметь изображение-шаблон и исходное изображение (изображение, для которого необходимо выполнять поиск объекта) и выполнить следующие действия:
1. Выбрать дескриптор для вычисления особых точек. Это может быть ORB, SIFT, SURF, FAST и т.д.;
2. Ищем особые точки на шаблоне и вычисляем их дескрипторы;
3. Ищем особые точки на исходном изображении и вычисляем их дескрипторы;
4. Сопоставляем дескрипторы особых точек, найденных на шаблоне и дескрипторы особых точек, найденных на исходном изображении;
5. Отсекаем ложные сопоставления;
6. Если найдено достаточное количество соответствий, то помечаем область с соответствующими точками.

### Достоинства
+ Устойчивость к поворотам объекта;
+ Устойчивость к изменениям размера объекта;
+ Устойчивость к изменению цвета объекта.

### Недостатки 
+ Запатентованность дескрипторов SIFT и SURF;
+ Сложность алгоритма.

### Недостатки в реализации
+ Не всегда удается корректно создать рамку объекта.

### Когда применять
+ Когда требуется соотнести локальные особенности из разных изображений. Например, при склейки панорамы;
+ Когда требуется найти объект, который имеет большое количество локальных особенностей (например, углов или блобов). Это может быть книга, журнал или упаковка с каким-либо товаром.

### Ссылки на дополнительные источники
* [Видео-лекция об особых точках](https://www.youtube.com/watch?v=vFseUICis-s)
* [Документация OpenCV](https://docs.opencv.org/master/db/d27/tutorial_py_table_of_contents_feature2d.html)
* [Сравнительный анализ методов нахождения особых точек на изображении](https://nauchkor.ru/pubs/sravnitelnyy-analiz-metodov-nahozhdeniya-osobyh-tochek-na-izobrazhenii-587d363a5f1be77c40d589ec)
* [Детекторы углов](https://habr.com/ru/post/244541/)

### Дополнительная информация
Для работы SIFT и SURF версия библиотеки opencv-python и opencv-contrib-python не должна превышать 3.4.2.16.


# En
## About Feature Detection
### Description
In order to use the Feature Detection, we need to have a template image and a source image (an image for which an object is to be searched for) and perform the following actions: 
1. Select a descriptor for calculating key points. It can be ORB, SIFT, SURF, FAST, etc.;
2. We look for the key points on the template and calculate their descriptors;
3. We look for the key points on the original image and calculate their descriptors ;
4. Compare the descriptors of the singular points found on the template and the descriptors of the singular points found on the original image;
5. Cut off false matches;
6. If found a sufficient number of matches, then we mark the area with the corresponding points.

### Advantages
+ Resistance to object turns;
+ Resistance to changes in object size;
+ Resistant to object color change.

### Disadvantages
+ Patented SIFT and SURF descriptors;
+ The algorithm is complex.

### Implementation flaws
It is not always possible to correctly create an object frame.

### When to apply
+ When it is required to correlate local features from different images. For example, when gluing a panorama;
+ When you need to find an object that has a large number of local features (for example, corners or blobs). It can be a book, magazine or packaging with some product.


## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| Numpy	    |	1.18.4
| OpenCV	|	 4.3.0



