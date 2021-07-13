# Blurring and smoothing in OpenCV

In this article, you will learn about smoothing and blurring of image and how it can be achieved using different methods of OpenCV.

## Introduction

**Image blurring** or **Image smoothing** is convolving the image with a low-pass filter, and is used mainly for reducing noise from the image. ***Low pass filter*** is responsible for removing the noise from the image, while keeping the rest of the image unharmed. It smoothens the edges and averages the small complex edges which simplifies our image for better results. 

## Filtering

**Image filtering** is the process of modifying an image by changing its shades or color of the pixel or by increasing the brightness and contrast of that image. In the image processing filters, which are mainly used to suppress either the high frequencies in the image (i.e. image smoothing), or the low frequencies (i.e. enhancing or detecting edges in the image used).
OpenCV provides a function called `cv.filter2D()` to convolute a kernel with an image. 



Blurring (smoothing) can be achieved using these four OpenCV methods:

### 1. Averaging

**Averaging** method is implemented by convolving the image with a normalized box filter. It takes the average of all the pixels under the kernel area and places the average at the place of central element. The kernel i.e. the box filter looks something like this:

![](images\averagefilter.jpg)

where kwidth and kheight are 2d dimensions of kernel.

Averaging can be implemented using some of the useful *OpenCV* functions like **cv2.blur()** or **cv2.boxFilter()**.

Syntax of cv2.blur() is 

```python
blur = cv2.blur(src, ksize, dst, anchor = (-1,-1), borderType)
```

where 

> **src** = image that is to be blurred
>
> **ksize** = A tuple with height and width of kernel
>
> **dst** = output image with same size and type as the source image
>
> **anchor** = integer type variable representing anchor point, has value (-1, -1) as its default value meaning anchor is at the kernel center.
>
> **borderType** = An optional argument to decide what kind of border needs to be added and is defined by flags like cv2.BORDER_CONSTANT, cv2.BORDER_REFLECT, etc.
>
> **returns** a blurred image of same size and type as source image

Let's try this on an example image

<img src="images\download.png" alt="download" style="zoom: 80%;" />

```python
import cv2

image = cv2.imread('devincept.jpg')
# ksize
ksize = (8, 8)  
# Using cv2.blur() method 
image = cv2.blur(image, ksize) 
cv2.imshow(image)
```

Output:

<img src="images\download (3).png" alt="download (1)" style="zoom: 80%;" />

if we increase our size of kernel, our image gets more blurry. lets try `ksize=(15,15)`, we get the image like 

<img src="images\download (2).png" alt="download (2)" style="zoom: 80%;" />

### 2. Gaussian Blurring

In Gaussian Blurring we use a Gaussian kernel instead of using a box filter.It can be implemented using the method **cv2.GaussianBlur()**. Gaussian blurring is very successful in removing Gaussian noise from an image.

Syntax of cv2.GaussianBlur() is

```python
blur = cv.GaussianBlur(src,dst,ksize,sigmaX)
```



where

> **src** = image that is to be blurred
>
> **ksize** = A tuple with height and width of kernel. Note that the kernel width and height 	should be an odd number.
>
> **dst** = output image with same size and type as the source image
>
> **sigmaX** = a double type variable which is used for the Gaussian kernel standard deviation in X direction.

Lets try this on our previous example

```python
blur = cv2.GaussianBlur(image,(9,9),0)
cv2.imshow(blur)
```

<img src="images\download (4).png" alt="download (4)" style="zoom: 80%;" />

### 3. Median Blurring

The Median blur operation is same as the other averaging methods. The function `cv.medianBlur()` takes the median of all the pixels in the kernel area. Then the central element is replaced with the median value. This is very fruitful against salt-and-pepper noise in an image. But in this type of method, the central element is always replaced by some pixel value in the image. this operation reduces the noise effectively. The kernel size given should be a positive odd integer. The process processes the edges while removing the noise.


In this demo, we have added a 50% noise to the original image and applied median blurring. Check the result:


```python
median = cv.medianBlur(img,5)
```

Result:
<img src="https://user-images.githubusercontent.com/78999231/125387969-512a1000-e3bc-11eb-8a8e-40d680a6ced1.jpeg" alt="original" style="zoom: 80%;" />
<img src="https://user-images.githubusercontent.com/78999231/125388271-da414700-e3bc-11eb-9ecf-6fa8a918867f.jpg" alt="medianblur" style="zoom: 80%;" />

### 4. Bilateral Filtering

Till now, we have explained you some filters whose main goal is to smooth an image which a user inputs. However, sometimes these filters not only dissolve the noise, but also smooth the edges. For avoiding this, we use a bilateral filter. `cv.bilateralFilter()` is very fruittul in noise removal by keeping the edges sharp. But this operation is slower as compared to other filters used. It does not consider if a pixel is an edge pixel or not. So, it blurs the edges.

```python
blur = cv.bilateralFilter(img,9,75,75)
```

Result:
<img src="https://user-images.githubusercontent.com/78999231/125387969-512a1000-e3bc-11eb-8a8e-40d680a6ced1.jpeg" alt="original" style="zoom: 80%;" />
<img src="https://user-images.githubusercontent.com/78999231/125388740-aca8cd80-e3bd-11eb-89b6-2777eeb5099b.png" alt="bliateralblur" style="zoom: 80%;" />

