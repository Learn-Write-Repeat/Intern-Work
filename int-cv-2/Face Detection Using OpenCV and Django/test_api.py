# import the necessary packages
import requests
import cv2
 
# define the URL to our face detection API
url = "http://localhost:8000/face_detection/detect/"
 
# use our face detection API to find faces in images via image URL
image = cv2.imread("modi.jpg")
payload = {"url": "https://i0.wp.com/www.newsgram.com/wp-content/uploads/2020/04/Narendra-Modi.jpg"}
r = requests.post(url, data=payload).json()
print "modi.jpg: {}".format(r)
 
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
 
# show the output image
cv2.imshow("obama.jpg", image)
cv2.waitKey(0)
 
# load our image and now use the face detection API to find faces 
# images by uploading an image directly
# image = cv2.imread("custom-image.jpg")
# payload = {"image": open("adrian.jpg", "rb")}
# r = requests.post(url, files=payload).json()
# print "name.jpg: {}".format(r)

# image = cv2.imread("mamata.jpg")
# payload = {"image": open("path to image file in local system", "rb")}
# r = requests.post(url, files=payload).json()
# print "mamata.jpg: {}".format(r)
 
# loop over the faces and draw them on the image
# for (startX, startY, endX, endY) in r["faces"]:
# 	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
 
# # show the output image
# cv2.imshow("mamata.jpg", image)
# cv2.waitKey(0)