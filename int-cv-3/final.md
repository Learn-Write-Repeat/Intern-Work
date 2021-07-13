# LIST OF OPERATIONS & APPLICATIONS

## **BASIC OPERATIONS USING OPENCV**

+ **Capturing Images**
```py
import cv2
import time 

try:
    cam = cv2.VideoCapture(0)  # argument 0 refers to in-built camera and 1 refers to USB port 1 camera
    time.sleep(1)  # wait for proper initialization of the cam
    _, img = cam.read() # reading the frame from cam
    # cam.read returns 2 values--1 is a flag(_ is used to get the frame), other is the frame which stores the image
    cam.release()
    print('Image captured successfully')
    
except:
    print('Ërror while capturing the image')
```

+ **Storing Images**
```py
import cv2
import time 

cam = cv2.VideoCapture (0)  
time.sleep(1)  

_, img = cam.read() 
cv2.imwrite("ImgCam.png",img) # to store the image in the working directory
print('Image stored')
cam.release()
```

+ **Loading Images**
```py
import cv2

try:
    img = cv2.imread(r'C:\Users\hp\aero.png')  # loading the img
    print('Image Loaded successfully')
except:
    print('Ërror while loading the image')
```

+ **Understand the Properties of the Loaded Image**
```py
import cv2 

img = cv2.imread(r'C:\Users\hp\aero.png') 

print('Size: ',img.size)
print('Dimensions: ',img.shape)
print('Datatype: ',img.dtype)
```

+ **Displaying Images**
```py
import cv2 

img = cv2.imread(r'C:\Users\hp\aero.png') 
cv2.imshow("Original Image", img)  
cv2.waitKey(0) 
```

&ensp;

---
---
&ensp;
## **UNDERSTANDING HOW IMAGES ARE STORED**
Each image is represented by pixels - a matrix of pixel values. 
+ For a grayscale image, the pixel values range from 0 to 255 and they represent the intensity of that pixel 
+ An image of 20 x 20 dimensions would be represented by a matrix of 20x20 (a total of 400-pixel values)
+ For a colored image, there will be 3 channels (Red, Green, and Blue - RGB) and thus, would have three such matrices

&ensp;

---
---
&ensp;
## **IMAGE PROCESSING**
The process of performing some operations on images is called Image Processing.
Input for Image processing algorithms is an image and the Ouput is either an image or some important characteristics of that image.

&ensp;
### **IMAGE PROCESSING ALGORITHMS VS COMPUTER VISION ALGORITHMS**

Both Image Processing algorithms and Computer Vision (CV) algorithms take an image as input; however, in image processing, the output is also an image, whereas in computer vision the output can be some features/information about the image.

&ensp;
### **WHY IMAGE PROCESSING?**
Raw data (images) collected for AI models, etc. are usually of different sizes/dimensions, formats, color scales, etc. So, before feeding the data to the models for training, it needs to be analysed and pre-processed to a standard format.

It is usually done:
- for enhancing an image
- for extraction of useful information from the images

&ensp;
### **IMPORTANT CONCEPTS OF IMAGE PROCESSING**

1. [Basic Operations](#basic-operations) 
1. [Arithmetic Operations](#arithmetic-operations) 
1. [Bitwise Operations](#bitwise-operations) 
1. [Splitting & Merging Color Channels](#splitting-and-merging-color-channels)
1. [Understanding Colorspaces](#understanding-colorspaces) 
1. [Masking Operations](#masking-operations) 
1. [Morphological Operations](#morphological-operations) 
1. [Sharpen & Smoothen](#sharpen-and-smoothen) 
1. [Thresholding Images](#thresholding-images) 
1. [Edge  & Contour Detection](#edge-and-contour-detection) 

&ensp;

#### ***BASIC OPERATIONS***


1. **TRANSLATION** : process of shifiting image from one location to another location

   ```py
   import cv2 
   import numpy as np 

   img = cv2.imread(r'C:\Users\hp\aero.png') 
   cv2.imshow("Original Image", img)  
   cv2.waitKey(0) 

   tw,th = 100,50  # shift factors
   h, w = img.shape[0:2] 
   M = np.float32([[1, 0, tw], [0, 1, th]])  # translation matrix 
   tranImg = cv2.warpAffine(img, M, (w, h)) 
  
   cv2.imshow('Translated Image', tranImg) 
   cv2.waitKey(0) 
   ```

2. **ROTATION** : process of rotating image in a desired angle. There are 2 ways to perform rotation:
   
   - Using cv2.rotate():

   ```py
   import cv2

   img = cv2.imread(r'C:\Users\hp\aero.png')
   cv2.imshow('Original Image',img)
   cv2.waitKey(0) 

   imgs = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE) 
   cv2.imshow('Rotated Image',imgs)
   cv2.waitKey(0)  
   ```
   
   - Using  cv2.warpAffine():

   ```py
   import cv2

   img = cv2.imread(r'C:\Users\hp\aero.png')
   cv2.imshow('Original Image',img)
   cv2.waitKey(0) 

   h, w = img.shape[0:2] # shape attribute returns height and width
   rotMat = cv2.getRotationMatrix2D((w/2, h/2), 30, .5)  
   rotImg = cv2.warpAffine(img, rotMat, (w, h)) 

   cv2.imshow('Rotated Image',rotImg)
   cv2.waitKey(0)  
   ```

3. **RESIZE**: process of scaling images to the required size.  OpenCV provides several interpolation methods for resizing an image:

   - cv2.INTER_NEAREST: It is the fastest but there will be substantial loss of information

   - cv2.INTER_LINEAR: It is slower when compared to cv2.INTER_NEAREST and will result in less information loss. It is the default option. This is primarily used when zooming is required

   - cv2.INTER_AREA: This is used when we need to shrink an image

   - cv2.INTER_CUBIC: It is much slower but more efficient in terms of less information loss. Usually used when shrinking images

   ```py
   import cv2

   img = cv2.imread(r'C:\Users\hp\aero.png')
   cv2.imshow('Original Image',img)
   cv2.waitKey(0) 

   h, w = img.shape[0:2]
   resizedImg = cv2.resize(img,(int(w*2),int(h*2)),interpolation = cv2.INTER_LINEAR) # to zoom in 
   cv2.imshow("Resized Image",resizedImg)
   cv2.waitKey(0)

   resizedImg = cv2.resize(img,(int(w/2),int(h/2)),interpolation = cv2.INTER_CUBIC) # to shrink 
   cv2.imshow("Resized Image",resizedImg)
   cv2.waitKey(0)
   ```
   
4. **FLIP**: process of reversing the image vertically or horizontally

   ```py
   import cv2
    
   img = cv2.imread(r'C:\Users\hp\aero.png')
   cv2.imshow('Original Image',img)
   cv2.waitKey(0) 
    
   # flipping the image horizontally
   flipped = cv2.flip(img, 1)
   cv2.imshow("Flipped Horizontally", flipped)
   cv2.waitKey(0)

   # flipping the image vertically
   flipped = cv2.flip(img, 0)
   cv2.imshow("Flipped Vertically", flipped)
   cv2.waitKey(0)

   # flipping the image vertically and horizontally
   flipped = cv2.flip(img, -1)
   cv2.imshow("Flipped Vertically and Horizontally", flipped)
   cv2.waitKey(0)
   ```

5. **CROP**: process of removing umwanted parts of an image

   ```py
   import cv2
    
   img = cv2.imread(r'C:\Users\hp\aero.png')
   cv2.imshow('Original Image',img)
   cv2.waitKey(0) 

   cropImg = img[70:230, 70:800]  # cropping is done using slicing since images are processed as numpy arrays 
   cv2.imshow("Cropped Image", cropImg)
   cv2.waitKey(0)   
   ```
&ensp;

---

&ensp;
#### ***ARITHMETIC OPERATIONS***
Arithmetic Operations are used to enhance and analyse the properties of the input images. The operated images can be further used as an enhanced input image.

*NOTE*: Both images must be of equal size and depth

1. **Add**: adding two image pixel matrices (regular matrix addition)

1. **Subtract**: subtracting two image pixel matrices (regular matrix subtraction)

```py
import cv2    
    
image1 = cv2.imread(r'C:\Users\hp\aero.png')  
image2 = cv2.imread(r'C:\Users\hp\watch.png') 
  
# performing addition and subtraction
weightedSum = cv2.addWeighted(image1, 0.5, image2, 0.4, 0) 
sub = cv2.subtract(image1, image2) 
  
cv2.imshow('Weighted Image', weightedSum) 
cv2.imshow('Subtracted Image', sub) 
cv2.waitKey(0)
```
&ensp;

---

&ensp;
#### ***BITWISE OPERATIONS***
Bitwise Operations are also used in the same way as Arithmetic Operations.

*NOTE*: Both images must be of equal size and depth

1. **AND**: Bit-wise conjunction of input array elements

1. **OR**: Bit-wise disjunction of input array elements

1. **XOR**: Bit-wise exclusive-OR operation on input array elements

1. **NOT**: Bit-wise inversion on input array elements

```py
import cv2 
import numpy as np 

img1 = cv2.imread(r'C:\Users\hp\aero.png')  
img2 = cv2.imread(r'C:\Users\hp\watch.png') 
  
resAnd = cv2.bitwise_and(img2, img1, mask = None)
resOr = cv2.bitwise_or(img2, img1, mask = None) 
resXor = cv2.bitwise_xor(img1, img2, mask = None) 
resNot = cv2.bitwise_not(img1, mask = None) 

cv2.imshow('Bitwise And', resAnd)
cv2.imshow('Bitwise OR', resOr) 
cv2.imshow('Bitwise XOR', resXor)
cv2.imshow('Bitwise NOT on image 1', resNot) 
if cv2.waitKey(0) 
```
&ensp;

---

&ensp;
#### ***SPLITTING AND MERGING COLOR CHANNELS***
As mentioned earlier, a colored image has 3 channels. Splitting refers to the process of separating the 3 channel and merging refers to the process of compiling the 3 separated channels to get back the original image.

```py
import cv2

img = cv2.imread(r'C:\Users\hp\aero.png')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

(B, G, R) = cv2.split(img)
# show each channel individually
cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)

merged = cv2.merge([B, G, R])
cv2.imshow("Merged Image", merged)
cv2.waitKey(0)
```
&ensp;

---

&ensp;
#### ***UNDERSTANDING COLORSPACES***
There are many colorspaces HSV, CMYK, LAB, etc. But here we will be discussing the most common ones: 

1. **RGB**: represents Red, Green and Blue components of an image. Each Red, Green, and Blue channel can have values defined in the range [0, 255]. Most color applications and computer vision/image processing libraries use RGB by default.

1. **HSV**: represents Hue, Saturation and Value of an image. In the RGB colorspace, the “white” or “lightness” of a color is an additive combination of each component but in the HSVcolor space, the lightness is given its own separate dimension - saturation. The Hue value (usually a degree) is defined as the range [0, 179] (for a total of 180 possible values) on the HSV color cylinder. The Saturation and Value are defined in the range [0, 255].

1. **GrayScale**: represents single channel images with pixel values in the range [0, 255] 

```py
 import cv2
 
image = cv2.imread(r'C:\Users\hp\aero.png')
cv2.imshow("Original RGB Image", image)  # displaying the RGB original image
cv2.waitKey(0)

# displaying the image in the HSV colorspace
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)
cv2.waitKey(0)

# conversion of the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
```
&ensp;

---

&ensp;
#### ***MASKING OPERATIONS***
Masking is used in Image Processing to retrieve the Region of Interest or ROI (part of the image that we are interested in)

1. **Using Bitwise-Add Operation**

```py
import cv2
    
img = cv2.imread(r'C:\Users\hp\aero.png')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

# creating a mask with same dimensions of the image where each pixel is valued at 0
mask = np.zeros(img.shape[0:2], dtype="uint8")

# creating a rectangle on the mask where the pixels are valued at 255
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1)  # any other shape can be used too depending on the requirement
cv2.imshow("Mask", mask)

# performing a bitwise_and with the image and the mask
masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask applied to Image", masked)
cv2.waitKey(0)
```

2. **Using HSV Range values to mask an object of specific color**

```py
import cv2
    
img = cv2.imread(r'C:\Users\hp\aero.png')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

Lower = (100,150,0)
Upper = (140,255,255)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
mask = cv2.inRange(hsv, Lower, Upper) # highlighting just the colored object
cv2.imshow('Masked Image',mask)
cv2.waitKey(0)
```
&ensp;

---

&ensp;
#### ***MORPHOLOGICAL OPERATIONS***
Morphological operations are simple transformations applied to binary or grayscale images. Usually, morphological operations are applied to shapes and structures in of images. They are used to increase/decrease the size of objects in images and to close/open gaps between objects. 

1. **Erosion**: process of diminishing the boundaries of the object

1. **Dilation**: process of accentuating the boundaries of the object

1. **Opening**: process of performing erosion followed by dilation. Helps to remove small blobs from an image - first an erosion is applied to remove the small blobs, then a dilation is applied to regrow the size of the original object.

1. **Closing**: process of performing dilation followed by erosion. Helps to close holes inside of objects or for connecting components together.

1. **Gradient**: it gives the difference between a dilation and erosion. It is used to determine the outline of a particular object.

```py
import cv2
    
img = cv2.imread(r'C:\Users\hp\text.png')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# utilization of erosion threefold times
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)

# utilization of dilation threefold times
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)

# creation of three different kernels to use in morphology
kernelSizes = [(3, 3), (5, 5), (7, 7)]

# utilization of the morphological Opening operation
for k in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(k[0], k[1]), opening)
    cv2.waitKey(0)

# utilization of the morphological closing operation
for k in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(k[0], k[1]), closing)
    cv2.waitKey(0)
    
# utilization of the morphological gradient operation
for k in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(k[0], k[1]), gradient)
    cv2.waitKey(0)
```
&ensp;

---

&ensp;
#### ***SHARPEN AND SMOOTHEN***

1. **Sharpen**: process of highlighting features and edges in an image

   ```py
   import cv2
   import numpy as np

   img = cv2.imread(r'C:\Users\hp\aero.png')
   cv2.imshow('Original Image',img)
   cv2.waitKey(0) 

    # creating kernel
   sharpenMat = np.array([[-1,-1,-1],[-1, 9,-1],[-1,-1,-1]])
    # applying the sharpening kernel to the input image & displaying it.
   sharpened = cv2.filter2D(img, -1, sharpenMat)
   cv2.imshow('Sharpened Image', sharpened)
   cv2.waitKey(0)
   ```

1. **Smoothen**: process of removing high frequency content in an image (such as noise, edges, etc.)

    - Average Blur : takes the average of all the pixels under the kernel area and replaces the central element. A normalized box filter is used. Done by the function, cv2.blur() or cv2.boxFilter()

    - Gaussian Blur :  takes the Gaussian weighted average of all the pixels under the kernel area and replaces the central element. Instead of a box filter, a Gaussian kernel is used. Done by the function cv2.getGaussianKernel(). The width and height of the kernel should be specified and must be positive and odd. The standard deviation in the X and Y directions should be specified - sigmaX and sigmaY. If both are given as zeros, they are calculated from the kernel size.
    
    - Median Blur : takes the median of all the pixels under the kernel area and the central element is replaced with this median value. It reduces the noise effectively. Its kernel size should be a positive odd integer. Done by the cv2.medianBlur() function
    
    - Bilateral Filter : highly effective in noise removal while keeping edges sharp but slower when compared to others. It is similar to Gaussian filter. The Gaussian function of space makes sure that only nearby pixels are considered for blurring, while the Gaussian function of intensity difference makes sure that only those pixels with similar intensities to the central pixel are considered for blurring. So it preserves the edges since pixels at edges will have large intensity variation. Done by the cv2.bilateralFilter() function

    ```py
    import cv2

    img = cv2.imread(r'C:\Users\hp\aero.png')
    cv2.imshow('Original Image',img)
    cv2.waitKey(0)

    kernelSizes = [(3, 3), (9, 9), (15, 15)]
    params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

    # displaying the different levels of average blurring with the kernels
    for (kX, kY) in kernelSizes:
        blurred = cv2.blur(img, (kX, kY))
        cv2.imshow("Average ({},{})".format(kX, kY), blurred)
        cv2.waitKey(0)

    # displaying the different levels of gaussian blurring with the kernels
    for (kX, kY) in kernelSizes:
        blurred = cv2.GaussianBlur(img, (kX, kY), 0)
        cv2.imshow("Gaussian ({},{})".format(kX, kY), blurred)
        cv2.waitKey(0)

    # displaying the different levels of median blurring with the kernels
    for k in (3, 9, 15):
        blurred = cv2.medianBlur(img, k)
        cv2.imshow("Median {}".format(k), blurred)
        cv2.waitKey(0)

    # blurring images and reducing noise while preserving edges
    for (diameter, sigmaColor, sigmaSpace) in params:
        blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
        title = "Bilateral Filter d = {}, sc = {}, ss = {}".format(diameter, sigmaColor, sigmaSpace)
        cv2.imshow(title, blurred)
        cv2.waitKey(0)
    ```
&ensp;

---

&ensp;
#### ***THRESHOLDING IMAGES***
Technique to assign values to pixels based on comparison with the threshold value provided. Thresholding is usually done on greyscale images. There are several types of thresholding:

1. **Binary**: If the pixel value is greater than the threshold value, the pixel value is changed to 1. Else, it is changed to 0.

1. **Binary Inverted**: If the pixel value is greater than the threshold value, the pixel value is changed to 0. Else, it is changed to 1.

1. **Truncated**: If the pixel value is greater than the threshold value, the pixel value is truncated (changed to) to the threshold value. Else, it retains its original value.

1. **Set to 0**: If the pixel value is less than the threshold value, the pixel value is changed to 0. Else, it retains its original value.

1. **Set to 0 Inverted**: If the pixel value is less than the threshold value, the pixel value is changed to 1. Else, it retains its original value.

```py
import cv2  

img = cv2.imread(r'C:\Users\hp\aero.png')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

#converting image to greyscale
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# applying different thresholding  
_, thresh1 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY) 
_, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) 
_, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC) 
_, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO) 
_, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV) 
  
# showing all outputs
cv2.imshow('Binary Threshold', thresh1) 
cv2.imshow('Binary Threshold Inverted', thresh2) 
cv2.imshow('Truncated Threshold', thresh3) 
cv2.imshow('Set to 0', thresh4) 
cv2.imshow('Set to 0 Inverted', thresh5) 
cv2.waitKey(0)
```
&ensp;

---

&ensp;
#### ***EDGE AND CONTOUR DETECTION***

1. **Edge Detection**

```py
import cv2

img = cv2.imread(r'C:\Users\hp\aero.png')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

# cv2.Canny(image, minVal, maxVal)
edgeImg = cv2.Canny(img,100,200)
cv2.imshow("Edge Detected Image", edgeImg)
cv2.waitKey(0)
```

2. **Contour Detection**

```py
import cv2

thresh = 100
img = cv2.imread(r'C:\Users\hp\aero.png')
cv2.imshow('Original Image',img)
cv2.waitKey(0)

#convert img to grey
img_grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

#find contours
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# draw the contours on the empty image
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow("Contour Image", img)
cv2.waitKey(0)
```


&ensp;
### **APPLICATIONS OF IMAGE PROCESSING**
+ Medical Imaging Systems - eg: to detect cancer cells based on MRIs, CT Scans, etc.
+ Fault Detection Systems
+ Automated Vehicle Systems - used for automatic identification of number plates and detection of lanes, Traffic signs,etc.
+ Geographical Imaging Systems - eg: Earth Observation System (EOS) to get and analyse images of the Earth 
+ Aerial Surveillance Systems -  used to monitor land and sea, to determine the types and configurations of submarines, etc.

