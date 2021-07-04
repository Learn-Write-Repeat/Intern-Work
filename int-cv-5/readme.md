# Shape Detection Using OpenCV

OpenCV is a huge open-source library for computer vision, machine learning, and image processing.OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human. 

In this article we are going to see how to smoothen the noise and detect shapes in an image using OpenCV. For this we need cv2.findContours() function of OpenCV, and also we are going to use cv2.drawContours() function to draw edges on images.

A contour is nothing but an outline or a boundary of shape.

Approach that I have used:

- Reading the image and converting from RGB to Gray scale
- Removing Gaussian Noise via Gaussian Blur
- Applying Inverse Binary Adaptive Thresholding
- Finding all Countours in the processed image
- Filtering countours based on their area
- Initializing a new image and drawing the filtered contours

### Import the Libraries
```
import numpy as np
import cv2
import random
```

### Reading the noisy image
```
img = cv2.imread("fuzzy.png",1)
```
### Displaying to see how it looks
```
cv2.imshow("Original",img)
#if you're running it in colab,use from google.colab.patches import cv2_imshow statement before cv2.imshow 
```
[!github image]https://github.com/sreelakshmig009/Intern-Work/blob/main/int-cv-5/Original.png

### Converting the image to Gray Scale
```
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
```

### Removing Gaussian Noise
```
blur = cv2.GaussianBlur(gray, (3,3),0)
```

### Applying inverse binary due to white background and adapting thresholding for better results
```
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 205, 1)
```
### Printing the grayscale pre-processed image
```
cv2.imshow("Binary",thresh)
```
### Finding contours with simple retrieval (no hierarchy) and simple/compressed end points
```
_, contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
```
### Checking to see how many contours were found
```
print(len(contours))
```
### An empty list to store filtered contours
```
filtered = []
```
### Looping over all found contours
```
for c in contours:
	#If it has significant area, add to list
	if cv2.contourArea(c) < 1000:continue
	filtered.append(c)
```
 ### Checking the number of filtered contours
 ```
 print(len(filtered))
 ```
 ### Initialize an equally shaped image
 ```
 objects = np.zeros([img.shape[0],img.shape[1],3], 'uint8')
 ```
 ### Looping over filtered contours
 ```
 for c in filtered:
	#Select a random color to draw the contour
	col = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
	#Draw the contour on the image with above color
	cv2.drawContours(objects,[c], -1, col, -1)
	#Fetch contour area
	area = cv2.contourArea(c)
	#Fetch the perimeter
	p = cv2.arcLength(c,True)
	print(area,p)
```
### Output the completely processed image
```
cv2.imshow("Contours",objects)
```
### Destroy all open windows and release functions
```
cv2.waitKey(0)
cv2.destroyAllWindows
```
~G Sreelakshmi

