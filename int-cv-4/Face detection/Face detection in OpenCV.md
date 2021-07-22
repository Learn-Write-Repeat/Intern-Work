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

  - Webcam system
  
  - Jupyter notebook
  
  - Python-OpenCV

### Code for the following-

```python
   
import cv2  
   
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')   

cap = cv2.VideoCapture(0) 

while 1:  

    ret, img = cap.read() 
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    
    for (x,y,w,h) in faces: 
    
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)  
        
        roi_gray = gray[y:y+h, x:x+w] 
        
        roi_color = img[y:y+h, x:x+w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)  
        
        for (ex,ey,ew,eh) in eyes: 
        
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2) 
            
    cv2.imshow('img',img) 
    
    k = cv2.waitKey(30) & 0xff
    
    if k == 27: 
    
        break
        
cap.release() 

cv2.destroyAllWindows()   
 

```


 ##  Explanation

   - Importing the Opencv library using the *import cv2* statement and then loading the requirements of the XML classifiers for the face and eye detection.

```python
   
         face_cascade=cv2.CascadeClassifier('haarcascade_frontal_face_default.xml')
        
         eye_cascade=cv2.CascadeClassifier('haarcascade_eye_default.xml')
         
```


   #### OR

   -  Specifying the path where XML classifiers are stored:
      
        **Example:**
        ```python
        
          face_cascade=cv2.CascadeClassifier('F:/is setup/haarcascade_frontal_face_default.xml')
          
          eye_cascade=cv2.CascadeClassifier('F:/is setup/haarcascade_eye.xml
          
        ```
        
        
      -  Now initializing the cap variable and capturing the frames from the camera
      ```python
        
          cap=cv2.VideoCapture(0)
      ```
      
 -  Using while loop read each frame from the camera and then perform the next step shown:
     ```python
          
              ret,img=cap.read()
     ```
     
  -  Converting it into gray scale frame.

  ```python
              gray=cv2.cvtcolor(img,cv2.COLOR_BGR2GRAY)
              
  ```

   -   Detecting the faces of different size in the input image

   ```python
   
            faces=face_cascade_detectMultiScale(gray,1.3,5)
    
   ```

   -   Now our work is to draw a rectangle around the face and eye image using the for loop

   ```python
              for (x,y,w,h) in faces:
              
              cv2.rectangle(img(x,y),(x+w,y+h),(255,255,0),2)
              
              roi_gray=gray[y:y+h,x:x+w]
              
              roi_color=img[y:y+h,x:x+w]
              
              eyes=eye_cascade.detectMultiScale(roi_gray)
 
                 for (ex,ey,ew,eh) in eyes:
          
                      cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
   ```

   - Display the camera screen as output

   ```python
          cv2.imshow('img',img)
   ```


   - Last and the final step is to break the loop by pressing the **Esc** button

   ```python
          k=cv2.waitKey(30) & 0xff
        
            if k=27;
          
              break:
        
   ```