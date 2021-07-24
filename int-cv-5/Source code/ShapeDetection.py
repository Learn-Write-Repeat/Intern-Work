import cv2
def getContours(img):
    contours , heirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >100:
            cv2.drawContours(imgContours,cnt,-1,(0,0,0),2)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            objectCor = len(approx)
            x,y,w,h = cv2.boundingRect(approx)

            if objectCor == 3:
                objectType = "Triangle"

            elif objectCor == 4:
                assRatio = w/float(h)
                if assRatio >0.95 and assRatio<1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objectCor == 5:
                objectType = "Pentagon"

           elif objectCor > 6 and objectCor<=8:

            elif objectCor == 6 :

                objectType = "Hexagon"
            elif objectCor > 6:
                objectType = "Circle"
            else:
                objectType = "None"

            cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContours,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)

path = "path/to/image"
img = cv2.imread(path)
imgContours = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)

cv2.imshow("Shapes",img)
cv2.imshow("output",imgContours)

cv2.waitKey(0)
