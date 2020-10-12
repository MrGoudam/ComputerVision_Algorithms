# Ru
## О высокочастотных фильтрах
### Описание
Края(границы) — это такие кривые на изображении, вдоль которых происходит резкое изменение яркости или других видов неоднородностей.

Причины возникновения краёв на изображении могу быть следующие:
* изменение освещенности;
* изменение цвета;
* изменение глубины сцены (ориентации поверхности).

Для того, чтобы находить края на изображениях, используют фильтры высоких частот(HPF).

В OpenCV существуют следующие реализации высокочастотных фильтров:
1. [Оператор Канни](#canny)
2. [Оператор Лапласа](#laplacian)
3. [Оператор Собеля](#sobel)
4. [Scharr](#scharr)

#### <h4 name='canny'>Оператор Канни</h4>
Оператор Канни (или детектор границ Канни) является наиболее популярным методом выделения границ. Не смотря на то, что данный метод был разработан в 1986 году, он до сих пор является одним из лучших методов выделения границ на изображении.

Метод Canny принимает следующие параметры:
+ image - входное изображение (желательно в градации серого);
+ threshold1 - минимальный порог;
+ threshold2 - максимальный порог;
+ edges - выходное изображения;
+ apertureSize - размер для оператора Собеля;
+ L2gradient - флаг, который задает уравнение для определения величины градиента.

В качестве выходных параметров Canny возвращает изображение.

#### <h4 name='laplacian'>Оператор Лапласа</h4>
Дискретный оператор Лапласа часто используется в обработке изображений, например в задаче выделения границ или в приложениях оценки движения. Дискретный лапласиан определяется как сумма вторых производных и вычисляется как сумма перепадов на соседях центрального пиксела.

Метод Laplacian принимает следующие параметры:
+ src - входное изображение;
+ ddepth - глубина выходного изображения;
+ dst - выходное изображения;
+ ksize - размер ядра для вычисления фильтров второй производной;
+ scale - необязательный коэффициент для вычисленных значений лапласиана;
+ delta - необязательное значение дельты, которое добавляется к результатам;
+ borderType - пограничный режим, используемый для экстраполяции пикселей за пределами изображения.

В качестве выходных параметров Laplacian возвращает изображение.

#### <h4 name='sobel'>Оператор Собеля</h4>
Оператор Собеля — дискретный дифференциальный оператор, вычисляющий приближённое значение градиента яркости изображения. Результатом применения оператора Собеля в каждой точке изображения является либо вектор градиента яркости в этой точке, либо его норма.

Метод Sobel принимает следующие параметры:
+ src - входное изображение;
+ ddepth - глубина выходного изображения;
+ dx - порядок производной x;
+ dy - порядок производной y;
+ dst - выходное изображения;
+ ksize - размер ядра Собеля;
+ scale - необязательный коэффициент для вычисленных значений производной;
+ delta - необязательное значение дельты, которое добавляется к результатам;
+ borderType - пограничный режим, используемый для экстраполяции пикселей за пределами изображения.

В качестве выходных параметров Sobel возвращает изображение.

#### <h4 name='scharr'>Scharr</h4>
Когда размер ядра оператора Собеля равен 3, ядро может выдавать некоторые неточности. OpenCV устраняет эту неточность для ядер размером 3x3 с помощью функции Scharr. Это работает так же быстро, но более точно, чем стандартная функция Собеля.

Метод Scharr принимает следующие параметры:
+ src - входное изображение;
+ ddepth - глубина выходного изображения;
+ dx - порядок производной x;
+ dy - порядок производной y;
+ dst - выходное изображения;
+ scale - необязательный коэффициент для вычисленных значений производной;
+ delta - необязательное значение дельты, которое добавляется к результатам;
+ borderType - пограничный режим, используемый для экстраполяции пикселей за пределами изображения.

В качестве выходных параметров Scharr возвращает изображение.

### Ссылки на дополнительные источники
* [Canny Edge Detector](https://docs.opencv.org/3.4/da/d5c/tutorial_canny_detector.html)
* [Оператор Кэнни](https://ru.wikipedia.org/wiki/%D0%9E%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_%D0%9A%D1%8D%D0%BD%D0%BD%D0%B8)
* [Laplace](https://docs.opencv.org/3.4/d5/db5/tutorial_laplace_operator.html)
* [Дискретный оператор Лапласа](https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D1%81%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D1%8B%D0%B9_%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80_%D0%9B%D0%B0%D0%BF%D0%BB%D0%B0%D1%81%D0%B0)
* [Sobel Derivatives](https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html)


# En
## About high-pass filters 
### Description

Edges (borders) are such curves in the image along which there is a sharp change in brightness or other types of inhomogeneities.

The reasons for the appearance of edges in the image can be the following:
* change in illumination;
* color change;
* changing scene depth.

High pass filters (HPF) are used to find edges in images.

The following high-pass filter implementations exist in OpenCV:
1. [Operator Canny](#cannyEn)
2. [Laplace operator](#laplacianEn)
3. [Sobel Derivatives](#sobelEn)
4. [Scharr](#scharrEn)

#### <h4 name='cannyEn'>Operator Canny</h4>
The Canny Operator is the most popular method for extracting borders. Despite the fact that this method was developed in 1986, it is still one of the best methods for extracting borders in an image.

The Canny method accepts the following parameters:
+ image - input image;
+ threshold1 - first threshold for the hysteresis procedure;
+ threshold2 - second threshold for the hysteresis procedure;
+ edges - output image;
+ apertureSize - aperture size for the Sobel operator;
+ L2gradient - flag that specifies the equation for determining the magnitude of the gradient.

Canny returns an image as output parameters.

#### <h4 name='laplacianEn'>Laplace operator</h4>
Discrete Laplace operator is often used in image processing, for example, in the problem of boundary extraction or in motion estimation applications. The discrete Laplacian is defined as the sum of the second derivatives and is calculated as the sum of the differences in the neighbors of the central pixel.

The Laplacian method accepts the following parameters:
+ src - input image;
+ ddepth - desired depth of the destination image;
+ dst - output image;
+ ksize - aperture size used to compute the second-derivative filters;
+ scale - optional scale factor for the computed Laplacian values;
+ delta - optional delta value that is added to the results prior to storing them in dst;
+ borderType - pixel extrapolation method.

Laplacian returns an image as output parameters.

#### <h4 name='sobelEn'>Sobel Derivatives</h4>
The Sobel operator is a discrete differential operator that calculates the approximate value of the image brightness gradient. The result of applying the Sobel operator at each point of the image is either the vector of the brightness gradient at this point, or its norm.

The Sobel method accepts the following parameters:
+ src - input image;
+ ddepth - desired depth of the destination image;
+ dx - order of the derivative x;
+ dy - order of the derivative y;
+ dst - output image;
+ ksize - size of the extended Sobel kernel;
+ scale - optional scale factor for the computed derivative values;
+ delta - optional delta value that is added to the results prior to storing them in ds;
+ borderType - pixel extrapolation method.

Sobel returns an image as output parameters.

#### <h4 name='scharrEn'>Scharr</h4>
When the kernel size of the Sobel operator is 3, the kernel may produce some inaccuracies. OpenCV removes this imprecision for 3x3 kernels with the Scharr function. This works just as quickly, but more accurately than the standard Sobel function.

The Scharr method accepts the following parameters:
+ src - input image;
+ ddepth - desired depth of the destination image;
+ dx - order of the derivative x;
+ dy - order of the derivative y;
+ dst - output image;
+ scale - optional scale factor for the computed derivative values;
+ delta - optional delta value that is added to the results prior to storing them in ds;
+ borderType - pixel extrapolation method.

Scharr returns an image as output parameters.

## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| OpenCV	|   4.3.0
| Numpy     |   1.18.4
| Matplotlib|   3.2.1



