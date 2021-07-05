# Shape Detection Using OpenCV

OpenCV is a huge open-source library for computer vision, machine learning, and image processing.OpenCV supports a wide variety of programming languages like Python, C++, Java, etc. It can process images and videos to identify objects, faces, or even the handwriting of a human. 

In this ,we will learn how to detect shapes of objects by finding their contours. Contours are basically outline that bound the shape or form of an object. So we will be detecting multiple shapes and how many corners points each shape has along with its area .

Approach that we have used:

*Created a file called ShapeDetection and written functions to detect the shapes based on the contours and output the shape accordingly

*Imported ShapeDetection inside another file called detect_shapes 

*Preprocessed the image file by applying threshold and GaussianBlur

*Finally printed the output image file
 

### Create a file called ShapeDetection
Open a file in your favorite editor and save it as ShapeDetection.py


### Import open-cv library
```
import cv2
```
### Create a ShapeDetector class and Initialise an _init_ method
```
def __init__(self):
        pass
```
### Within the class ,create another method called detect and define it
```
def detect(self, c):
        # initialize the shape name and approximate the contour
        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
```
### State if conditions to detect the shapes based on the number of vertices
```
 # if the shape is a triangle, it will have 3 vertices
        if len(approx) == 3:
            shape = "Triangle"
            
        elif len(approx) == 10:
            shape = "Star"


        # if the shape has 4 vertices, it is either a square or
        # a rectangle
        elif len(approx) == 4:
            # compute the bounding box of the contour and use the
            # bounding box to compute the aspect ratio
            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)

            # a square will have an aspect ratio that is approximately
            # equal to one, otherwise, the shape is a rectangle
            shape = "Square" if ar >= 0.95 and ar <= 1.05 else "Rectangle"

        # if the shape is a pentagon, it will have 5 vertices
        elif len(approx) == 5:
            shape = "pentagon"

        # otherwise, we assume the shape is a circle
        else:
            shape = "circle"
```
### Return the shape variable's output and save this file
```
return shape
```
### Create another python file called detect_shapes
Create a new file and save it as detect_shapes.py

### Import the neccessary libraries and also the previously created ShapeDetection
```
from ShapeDetection import ShapeDetector
import imutils
import cv2
```
### Read and resize the image accordingly
```
image = cv2.imread(image_path)
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
```
### Apply grayscale and threshold on the image
We will now convert the image into grayscale and apply threshold using cv2.threshold of openCv.Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided. In thresholding, each pixel value of the image is compared with the threshold value.
```
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)S
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh1,thresh2 = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY_INV)
```
### Find contours in the image and call the ShapeDetector() class of ShapeDetection module
To find contours,we will be using cv2.findContours() function of openCV
```
cnts = cv2.findContours(thresh2.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
```
### Loop over the contours
```
for c in cnts:
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detect(c)
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.imshow("Image", image)
    cv2.waitKey(0)
```
cv2 waitkey() allows you to wait for a specific time in milliseconds until you press any button on the keyword. It accepts time in milliseconds as an argument.
### Close all the windows after the output is displayed and viewed 
```
cv2.destroyAllWindows()
```
## We used this image for input
<img src = "https://github.com/sreelakshmig009/Intern-Work/blob/main/int-cv-5/Images/test.jpg">

## And this was the output
<img src = "https://github.com/sreelakshmig009/Intern-Work/blob/main/int-cv-5/Images/Image.png">

Refer this repository for the source code
