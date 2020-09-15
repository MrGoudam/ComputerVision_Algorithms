# About colorFilter
## Description
The color filters method using OpenCV is reduced to calling the inRange method. This method takes an image and a bounding value, and returns an image as a mask.


## Advantages
+ Fast work


## Disadvantages
+ Highly dependent on lighting


## When to apply
The method of color filters can be used in cases where the object differs significantly from the background in color and the lighting is uniform and does not change



# О цветовом фильтре
## Описание
Метод цветовых фильтров с использованием OpenCV, сводится к вызову метода inRange. Данный метод принимает изображение и ограничивающие значения, и возвращает изображение в виде маски


## Достоинства
+ Быстро работает


## Недостатки
+ Очень зависит от освещения


### Когда применять
Метод цветовых фильтров можно применять в тех случаях, когда объект существенно отличаться от фона по цвету и освещение равномерно и не изменяется

# About script
## Version of libraries
| Lib    		| 	Version
| :-------:	| :-------:
| Numpy	|	1.18.4
| OpenCV	|	 4.3.0
