# Face detection in OpenCV

In this session,
- We will see what is Haar classifier.
- We will see programming on face and eye detection.

## Haar Classifier

Face and Eye detection works on the algorithm called Haar Classifier which is proposed by Paul Viola and Michael Jones. In their paper, *"Rapid Object Detection using Boosted Cascade of straightforward Features"* in 2001.

Haar Classifier is a machine learning based approach where a function is trained from tons of positive and negative images i.e with face and without face.

Initially the algorithm needs many positive images(with face)and negative images(without face) to coach the classifier(algorithm that sorts data in categories of information). Once all the features and details are extracted, they're stored during a file and if we get any new input image, check the feature from the file, apply it on the input image and if it passes all the stage then **the face is detected**. So this will be done using **Haar Features**.

So briefly , Haar Classifier may be a classifier which is employed to detect the thing that it's been trained for from the source.

##  Program on Face and Eye detection

Before adding face and eye detection on the Haar Cascade files we need to import *OpenCV library*.

### To install OpenCV library on *anaconda prompt* we have to execute the following commands:

```python
pip install opencv-python
pip install opencv-contrib-python
```

## The REQUIREMENTS

  - Jupyter notebook
  
  - Python-OpenCV

### Code for the following-

- First we import the required libraries. 

```
import cv2
```

- Then loading the requirements of the XML classifiers for the face and eye detection.

```python
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
```

- For our example, we will use this image and read it as follows

```python

image = cv2.imread('face.jpg')
cv2.imshow('image',image)
```

Output:

<img src="face.jpg" alt="face" style="zoom:50%;" />

- Then we detect faces and draw a rectangle around the face

```python
#converting the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

#detecting faces and saving x,y,w,h coordinates to 'faces'    
faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

for (x,y,w,h) in faces: 
	#draw a rectangle around the detected face
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)  
    #region of interest around our face, helps speed up the process to find eyes
    roi_gray = gray[y:y+h, x:x+w] 
    
    roi_color = image[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray)  
    
    for (ex,ey,ew,eh) in eyes: 
    
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
#final output
cv2.imshow('image',image)
```

- This is what our final output looks like-

<img src="D:\projects\markdown\Face detection\output.jpg" alt="output" style="zoom:50%;" />



Here is the **full code**: 

```python
#import the requirements
import cv2
from google.colab.patches import cv2_imshow

image = cv2.imread('face.jpg')
cv2_imshow(image)  

# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')   
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

#converting the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

#detecting faces and saving x,y,w,h coordinates to 'faces'    
faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

for (x,y,w,h) in faces: 

    cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)  
    
    roi_gray = gray[y:y+h, x:x+w] 
    
    roi_color = image[y:y+h, x:x+w]
    
    eyes = eye_cascade.detectMultiScale(roi_gray)  
    
    for (ex,ey,ew,eh) in eyes: 
    
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
        
cv2_imshow(image)
```
