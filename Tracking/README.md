# Ru
## О трекинге
### Описание
Использование трекинга с помощью OpenCV сводится к 3 вещам:
1. Создание объекта трекера;
2. Инициализация трекера с ограничивающей рамкой вокруг цели;
3. Обновление трекера.

В OpenCV существует 8 трекеров (см. О трекерах), из которых на практике удается использовать только CSRT. Данный метод имеет не плохую точность, но при этом, не очень быстрый. В задаче мультитрекинга, медленность данного трекера особо хорошо видна.

Для того, чтобы инициализировать трекер, необходимо вызвать для объекта трекер метод <b>init</b> и передать ему изображение и координаты ограничивающей рамки. Данный метод возвращает True, если инициализация прошла успешно и False, в противном случае.

Для того, чтобы найти новое положение цели, необходимо для трекера вызвать метод <b>update</b> и предать в качестве аргумента изображение, для котором нужно найти новое положение цели. Данный метод возвращает в качестве выходных параметров успешность поиска цели и координаты объекта. 

Для решения задачи мультитрекига можно использовать объект MultiTracker, но у данного объекта есть несколько проблем, а именно:
1. Нельзя убрать добавленный трекер из объекта MultiTracker. В случае, если цель не удаться найти на кадре (например, цель выйдет за границу кадра), в MultiTracker останется рудиментальная информация, которая будет потреблять вычислительные ресурсы. Выходом может быть инициализация нового объекта MultiTracker и удаление старого.
2. Функция multiTracker.update вычисляет положение всех отслеживаемых целей, и если одна из целей будет потеряна, то фактор успеха будет равняться False.

### О трекерах
1. BOOSTING - Устаревший метод, нужен только для сравнения с другими методами;
2. MIL - Работает лучше чем BOOSTING, но легко теряет цель и не восстанавливается после ее потери;
3. MEDIANFLOW - Работает, когда объект мало движется и эти движения предсказуемы;
4. GOTURN - Метод основан на глубоком обучении. Требует доп. файл;
5. TLD - Метод склонный к ложно-положительным срабатываниям;
6. CSRT - Имеет низкую скорость работы, но высокую точность;
7. KCF - Имеет среднюю скорость работы и среднюю точность;
8. MOSSE - Имеет высокую скорость, но низкую точность.

### Когда применять
+ Когда есть необходимость находить положение объекта на последующих кадров. 

### Ссылки на дополнительные источники
* [Object Tracking with OpenCV](https://ehsangazar.com/object-tracking-with-opencv-fd18ccdd7369)


# En
## About tracking
### Description
Tracking with OpenCV comes down to 3 things:
1. Creating a tracker object
2. Initializing the tracker object
3. Update

There are 8 trackers in OpenCV (see About trackers), of which only CSRT can be used in practice. This method has not bad accuracy, but at the same time, not very fast. In the task of multitracking, the slowness of this tracker is especially clearly visible.

In order to initialize the tracker, it is necessary to call the <b>init</b> method for the tracker object and pass it the image and coordinates of the bounding box. This method returns True if the initialization was successful and False otherwise.

To find a new position of the target, you need to call the <b>update</b> method for the tracker and pass an image as an argument. This method returns the success of the target search and the target coordinates as output parameters.

To solve the multitrack problem, you can use the MultiTracker object, but this object has several problems, namely:
1. You cannot remove the added tracker from the MultiTracker object. The solution may be to initialize the new MultiTracker object and delete the old one.
2. The multiTracker.update function calculates the position of all tracked targets, and if one of the targets is lost, the success factor will be False.

### About trackers
1. BOOSTING - Deprecated method, only needed for comparison with other methods;
2. MIL - Works better than BOOSTING, but loses target easily and does not recover from loss;
3. MEDIANFLOW - Works when the subject moves little and these movements are predictable;
4. GOTURN - The method is based on deep learning. Requires an additional file;
5. TLD - Method prone to false positives;
6. CSRT - Has a low speed of work, but high accuracy;
7. KCF - Has an average operating speed and average accuracy;
8. MOSSE - Has high speed but low accuracy.

### When to apply
+ When there is a need to find the position of the object on subsequent frames.


## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| OpenCV	|	 4.3.0



