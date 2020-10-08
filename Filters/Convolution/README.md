# Ru
## О свертке
### Описание
Для того, чтобы отфильтровать изображение можно использовать свертку. Свертка (англ. convolution) — это операция вычисления нового значения выбранного пикселя, учитывающая значения окружающих его пикселей. Свертка происходит между исходным изображением и ядром (фильтром).
Обычно ядро свертки является квадратной матрицей N*N, где N — нечетное число. Ядро свертки может быть высокочастотным, низкочастотным или настраиваемым. Для высокочастотных и низкочастотных ядер в OpenCV существуют уже готовые реализации (см. HPF и LPF). Если ядро является настраиваемым, то можно применить метод filter2D.

filter2D принимает следующие аргументы:
+ src - входное изображение;
+ ddepth - желаемая глубина целевого изображения. Когда ddepth = -1, выходное изображение будет иметь ту же глубину, что и исходное;
+ kernel - ядро свертки;
+ dst - выходное изображение;
+ anchor - привязка ядра, указывающая относительное положение отфильтрованной точки в ядре;
+ delta - необязательное значение, добавляемое к отфильтрованным пикселям;
+ borderType - метод экстраполяции пикселей.

filter2D возвращает отфильтрованное изображение в качестве выходного параметра.

### Когда применять
+ Свертка применяется тогда, когда есть необходимость обработать изображение. Например, составить карту признаков, найти локальные особенности, размыть изображения, найти края объектов и т.д.;
+ filter2D нужно применять тогда, когда ядро свертки является нестандартным или нет соответствующего реализованного метода.

### Ссылки на дополнительные источники
* [Making your own linear filters!](https://docs.opencv.org/3.4/d4/dbd/tutorial_filter_2d.html)
* [Kernel](https://en.wikipedia.org/wiki/Kernel_(image_processing))
* [Image Filtering](https://cs.nyu.edu/~fergus/teaching/vision/3_filtering.pdf)
* [Функция Свертка](https://desktop.arcgis.com/ru/arcmap/10.3/manage-data/raster-and-images/convolution-function.htm)


# En
## About convolution
### Description
Convolution can be used to filter the image. Convolution is the operation of calculating the new value of the selected pixel, taking into account the values ​​of the surrounding pixels. Convolution occurs between the original image and the kernel (filter).
Usually the kernel of the convolution is a square matrix N * N, where N is an odd number. The convolution kernel can be high frequency, low frequency, or customizable. For high-frequency and low-frequency kernels in OpenCV there are ready-made implementations (see HPF and LPF). If the kernel is customizable, then the filter2D method can be used.

filter2D takes the following arguments:
+ src - input image.;
+ ddepth - desired depth of the destination image. When ddepth=-1, the output image will have the same depth as the source;
+ kernel - convolution kernel;
+ dst - output image;
+ anchor - anchor of the kernel that indicates the relative position of a filtered point within the kernel;
+ delta - optional value added to the filtered pixels;
+ borderType - pixel extrapolation method.

filter2D returns the filtered image as an output parameter.

### When to apply
+ Convolution is used when there is a need to process an image. For example, make a feature map, find local features, blur images, find the edge of objects, etc.;
+ filter2D should be used when the convolution kernel is non-standard or there is no corresponding implemented method.


## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| OpenCV	|   4.3.0
| Numpy     |   1.18.4
