
## About contour analysis
### Description
In contour analysis, everything comes down to 2 operations: 
1. Getting the contour of the object 
2. Checking the contour on the block of rules

If the contour of the object complies with the rules, then it is accepted as the desired object.
Otherwise, it is accepted as unknown.

This method is not independent, but is only an approach to the search and classification of objects.

### Advantages
+ Work speed

### Disadvantages
+ It is necessary to clearly form a block of rules

### When to apply
When we know the shape of an object and we need to find this shape. For example, if we know that an object has the shape of a quadrangle, then we can look for that shape in the image


## О контурном анализе
### Описание
В контурном анализ все сводится к 2 операциям:
1. Получение контура объекта
2. Проверка контура на блоке правил

Если контур объекта соответствует правилам, то он принимается как искомый объект. 
В ином случае, принимается как неизвестный.

Данный метод не является самостоятельным, а является лишь подходом к поиску и классификацией объектов.

### Достоинства
+ Скорость работы

### Недостатки
+ Нужно четко формировать блок правил

### Когда применять
Когда мы знаем форму объекта и необходимо эту форму найти. Например, если мы знаем, что объект имеет форму четырехугольника, то мы можем поискать 
ту форму на изображении



## About script
This implementation has a very simplified block of rules and is intended only to demonstrate the approach to finding objects in the image.

### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| Numpy	    |	1.18.4
| OpenCV	|	 4.3.0



