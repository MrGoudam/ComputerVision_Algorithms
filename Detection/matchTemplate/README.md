# Ru
## О сопоставлении с шаблоном 
### Описание

Метод сопоставление с шаблоном с использованием OpenCV, сводится к вызову метода matchTemplate. 
В качестве входных параметров, данный метод принимает изображение для обработки, изображение шаблон и ID метода сопоставления.
В качестве выходных параметров, данный метод возвращает карту кросс-корреляции.

### Достоинства
+ Быстро находит объекты в случае одного шаблона.

### Недостатки
+ Ищет конкретный объект (шаблон), а не класс / категорию объектов.
+ Работает, если только объект на изображении имеет такое же освещение, размер и угол поворота, что и шаблон.
+ Ресурсозатратный метод в случае большого количества шаблонов.

### Когда применять
Метод сопоставление с шаблоном можно применять, когда искомый объект имеет фиксированную форму и размер. Например, в случае съемки со спутника или при написании ботов для игр с простенькой графикой.

### Как улучшить результат поиска
+ Использовать только контура объектов, но это требует тщательной настройки контуров на входном изображении и на шаблоне. 


# En
## About Template Matching
### Description

Template Matching using OpenCV boils down to calling the matchTemplate method. 
As input parameters, this method accepts an image for processing, an image template and the ID of the matching method. 
As output parameters, this method returns a cross-correlation map.

### Advantages
+ Finds objects quickly in case of one template.

### Disadvantages
+ Searches for a specific object, not a class / category of objects.
+ Works if only the object in the image has the same lighting, size and rotation as the template.
+ Resource-intensive method in case of a large number of templates.

### When to apply
Template Matching can be used when the object to search for has a fixed shape and size. For example, in the case of shooting from a satellite or when writing bots for games with simple graphics.


## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| Numpy	    |	1.18.4
| OpenCV	|	 4.3.0



