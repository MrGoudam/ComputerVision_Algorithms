# Ru
## О низкочастотных фильтрах
### Описание
Низкочастотные фильтры позволяют размывать изображения и убирать с них шум. Если шум убрать нельзя, то позволяет уменьшить его влияние.

В OpenCV существуют следующие реализации низкочастотных фильтров:
1. [Сглаживание путем усреднения](#blur)
2. [Гауссово сглаживание](#GaussianBlur)
3. [Медианный фильтр](#medianBlur)
4. [Двустороннее сглаживание](#bilateralFilter)


#### <h4 name='blur'>Сглаживание путем усреднения</h4>
Фильтр, используемый здесь является наиболее простейшим и называется однородным сглаживанием (homogeneous smoothing) или box фильтром.

Данный фильтр, математически говоря, делает операцию свертки на изображении с ядром. В зависимости от того, какое ядро мы применяем к изображению и получается разница в результирующем сглаженном изображении. Все что делает этот фильтр, так это вычисляет средние значение соседей пикселя.

Для того, чтобы использовать сглаживание путем усреднения можно применить один из методов: 
- blur;
- boxFilter.

Метод blur принимает следующие параметры:
+ src — входное изображение; оно может иметь любое количество каналов, которые обрабатываются независимо друг от друга, но глубина должна быть CV_8U, CV_16U, CV_16S, CV_32F или CV_64F;
+ ksize — размер ядра размытия;
+ dst — выходное изображения;
+ anchor — привязка ядра, указывающая относительное положение отфильтрованной точки в ядре;
+ borderType — пограничный режим, используемый для экстраполяции пикселей за пределами изображения.

В качестве выходных параметров blur возвращает изображение.

Метод boxFilter принимает следующие параметры:
+ src - входное изображение;
+ ddepth - глубина выходного изображения;
+ ksize - размер ядра размытия;
+ dst - выходное изображения;
+ anchor - привязка ядра, указывающая относительное положение отфильтрованной точки в ядре;
+ normalize - нормализовано ли ядро по его площади;
+ borderType - пограничный режим, используемый для экстраполяции пикселей за пределами изображения.

В качестве выходных параметров boxFilter возвращает изображение.

#### <h4 name='GaussianBlur'>Гауссово сглаживание</h4>
Фильтр размытия по Гауссу достаточно часто применяется как сам по себе, так и как часть других алгоритмов обработки изображений. Но нам нужно быть очень осторожными в выборе размера ядра и стандартного отклонения распределения Гаусса по X и Y направлению. Они должны быть тщательно подобраны. Так, например, размер ядра не может быть четным числом.

Метод GaussianBlur принимает следующие параметры:
+ src - входное изображение;
+ ksize - размер ядра Гаусса;
+ sigmaX - стандартное отклонение ядра Гаусса в направлении X;
+ dst - выходное изображения;
+ sigmaY - стандартное отклонение ядра Гаусса в направлении Y;
+ borderType - пограничный режим, используемый для экстраполяции пикселей за пределами изображения.

В качестве выходных параметров GaussianBlur возвращает изображение.

#### <h4 name='medianBlur'>Медианный фильтр</h4>
Медианный фильтр представляет собой общий метод для сглаживания. Медианное сглаживание широко используется в алгоритмах обнаружения краев, так как при определенных условиях оно сохраняет края, удаляя шум.

Метод medianBlur принимает следующие параметры:
+ src - входное изображение;
+ ksize - размер ядра;
+ dst - выходное изображения;

В качестве выходных параметров medianBlur возвращает изображение.

#### <h4 name='bilateralFilter'>Двустороннее сглаживание</h4>
Двусторонняя сглаживание является одним из самых современных фильтров для сглаживания изображения и снижения уровня шума. Особенность данного фильтра заключается в том, что он может уменьшать уровень шума с сохранением информации о краях. 
Недостатком данного фильтра заключается в том, что на его работу требуется большее количество времени, чем на остальные алгоритмы сглаживания.

Метод bilateralFilter принимает следующие параметры:
+ src - входное изображение;
+ d - диаметр каждой окрестности пикселя, которая используется при фильтрации. Если он не положительный, то он вычисляется из sigmaSpace;
+ sigmaColor - фильтр сигмы в цветовом пространстве. Большее значение параметра означает, что более дальние цвета в окрестности пикселя (см. SigmaSpace) будут смешиваться вместе, что приведет к появлению больших областей с полу-равным цветом;
+ sigmaSpace - фильтр сигмы в координатном пространстве. Большее значение параметра означает, что более удаленные пиксели будут влиять друг на друга, если их цвета достаточно близки (см. SigmaColor). Когда d > 0, он определяет размер окрестности независимо от sigmaSpace. В противном случае d пропорционален sigmaSpace;
+ dst - выходное изображения;
+ borderType - пограничный режим, используемый для экстраполяции пикселей за пределами изображения.

В качестве выходных параметров bilateralFilter возвращает изображение.

Если установить значения сигм маленьким числом (<10), то фильтр не будет иметь большого эффекта, тогда как большое число (> 150) даст сильный эффект, делая изображение «мультяшным».

### Ссылки на дополнительные источники
* [2D Convolution](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html)
* [Фильтры в OpenCV. MedianBlur и Bilateral](https://techcave.ru/posts/65-filtry-v-opencv-medianblur-i-bilateral.html)
* [Фильтры в OpenCV. Average и GaussianBlur](https://techcave.ru/posts/66-filtry-v-opencv-average-i-gaussianblur.html)
* [Image Filtering](https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html)


# En
## About low-pass filters
### Description
Low pass filters blur images and remove noise from them. If the noise cannot be removed, then it can reduce its influence.

The following low-pass filter implementations exist in OpenCV:
1. [Smoothing by averaging](#blurEn)
2. [Gaussian blur](#GaussianBlurEn)
3. [Median blur](#medianBlurEn)
4. [Bilateral filter](#bilateralFilterEn)

#### <h4 name='blurEn'>Smoothing by averaging</h4>
The filter used here is the simplest one and is called homogeneous smoothing or box filter.

This filter, mathematically speaking, does a convolution operation on an image with a kernel. Depending on which kernel we apply to the image, there is a difference in the resulting smoothed image. All this filter does is calculate the average of the pixel neighbors

In order to use smoothing by averaging, one of the methods can be applied:
- blur;
- boxFilter.

The blur method accepts the following parameters:
+ src — input image;
+ ksize — blurring kernel size;
+ dst — output image;
+ anchor — anchor point;
+ borderType — border mode used to extrapolate pixels outside of the image.

blur returns an image as output.

The boxFilter method accepts the following parameters:
+ src - input image;
+ ddepth - the output image depth;
+ ksize - blurring kernel size;
+ dst - output image;
+ anchor - anchor point;
+ normalize - flag, specifying whether the kernel is normalized by its area or not;
+ borderType - border mode used to extrapolate pixels outside of the image.

boxFilter returns an image as output.

#### <h4 name='GaussianBlurEn'>Gaussian blur</h4>
The Gaussian blur filter is often used both by itself and as part of other image processing algorithms. But we need to be very careful in choosing the kernel size and the standard deviation of the Gaussian distribution in the X and Y direction. They must be carefully selected. So, for example, the kernel size cannot be an even number.

The GaussianBlur method accepts the following parameters:
+ src - input image;
+ ksize - Gaussian kernel size;
+ sigmaX - Gaussian kernel standard deviation in X direction;
+ dst - output image;
+ sigmaY - Gaussian kernel standard deviation in Y direction;
+ borderType - pixel extrapolation method.

GaussianBlur returns an image as output.

#### <h4 name='medianBlurEn'>Median blur</h4>
The median filter is a general technique for anti-aliasing. Median anti-aliasing is widely used in edge detection algorithms because it preserves edges by removing noise under certain conditions.

The medianBlur method accepts the following parameters:
+ src - input image;
+ ksize - aperture linear size;
+ dst - output image;

medianBlur returns an image as output.

#### <h4 name='bilateralFilterEn'>Bilateral filter</h4>
Bilateral filter is one of the most advanced filters for image smoothing and noise reduction. The peculiarity of this filter is that it can reduce the noise level while preserving edge information.
The disadvantage of this filter is that it takes more time to work than other anti-aliasing algorithms.

The bilateralFilter method accepts the following parameters:
+ src - input image;
+ d - diameter of each pixel neighborhood that is used during filtering. If it is non-positive, it is computed from sigmaSpace;
+ sigmaColor - filter sigma in the color space. A larger value of the parameter means that farther colors within the pixel neighborhood (see sigmaSpace) will be mixed together, resulting in larger areas of semi-equal color;
+ sigmaSpace - filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough (see sigmaColor ). When d > 0, it specifies the neighborhood size regardless of sigmaSpace. Otherwise, d is proportional to sigmaSpace;
+ dst - output image;
+ borderType - border mode used to extrapolate pixels outside of the image.

BilateralFilter returns an image as output.

Sigma values: For simplicity, you can set the 2 sigma values to be the same. If they are small (< 10), the filter will not have much effect, whereas if they are large (> 150), they will have a very strong effect, making the image look "cartoonish".

## About script
### Version of libraries
| Lib    	| 	Version
| :-------:	| :-------:
| OpenCV	|	 4.3.0



