<img src ="https://github.com/sreelakshmig009/Intern-Work/blob/face_detection/int-cv-2/Face%20Detection%20Using%20OpenCV%20and%20Django/images/cover.jpeg" alt="cover">


### Face Detection with OpenCV and Django REST API

Framework requirements : 
```
Django
opencv-python
numpy
requests
```

#### Create a Django Project

* Once the pre-requisites are installed, start setting up your Django project:

```
$ django-admin startproject cv_api
$ cd cv_api
```

These commands create a new Django project, adequately named cv_api.

The cv_api directory now contains all the necessary code and configurations to run our Django project — this code has been auto-generated and includes basic database configurations, project based options, and application settings.

With this in mind, let’s create a new app named face_detector , which will house our code for building a face detection API:

```
$ python manage.py startapp face_detector
```

Our directory structure till now:

```
|--- cv_api
|    |--- cv_api
|        |--- __init__.py
|        |--- settings.py
|        |--- urls.py
|        |--- wsgi.py
|    |--- face_detector
|        |--- __init__.py
|        |--- admin.py
|        |--- migrations
|        |--- models.py
|        |--- tests.py
|        |--- views.py
|    |--- manage.py
```

In our case, all we need is the View portion of the framework. We are not going to be interacting with the database, so the Model is not relevant to us. And we are going to ship the results of our API back to the end-user as a JSON object, so we won’t need the Template to render any HTML for us.

Again, our API is simply going to accept an image from a URL/stream, process it, and return a JSON response.

#### Inserting the face detector into my template API

Open up the cv_api/face_detector/views.py file and insert the following code:

```
# import the necessary packages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import numpy as np
import urllib
import json
import cv2
import os
# define the path to the face detector
FACE_DETECTOR_PATH = "{base_path}/cascades/haarcascade_frontalface_default.xml".format(
	base_path=os.path.abspath(os.path.dirname(__file__)))
@csrf_exempt
def detect(request):
	# initialize the data dictionary to be returned by the request
	data = {"success": False}
	# check to see if this is a post request
	if request.method == "POST":
		# check to see if an image was uploaded
		if request.FILES.get("image", None) is not None:
			# grab the uploaded image
			image = _grab_image(stream=request.FILES["image"])
		# otherwise, assume that a URL was passed in
		else:
			# grab the URL from the request
			url = request.POST.get("url", None)
			# if the URL is None, then return an error
			if url is None:
				data["error"] = "No URL provided."
				return JsonResponse(data)
			# load the image and convert
			image = _grab_image(url=url)
		# convert the image to grayscale, load the face cascade detector,
		# and detect faces in the image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		detector = cv2.CascadeClassifier(FACE_DETECTOR_PATH)
		rects = detector.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5,
			minSize=(30, 30), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
		# construct a list of bounding boxes from the detection
		rects = [(int(x), int(y), int(x + w), int(y + h)) for (x, y, w, h) in rects]
		# update the data dictionary with the faces detected
		data.update({"num_faces": len(rects), "faces": rects, "success": True})
	# return a JSON response
	return JsonResponse(data)
def _grab_image(path=None, stream=None, url=None):
	# if the path is not None, then load the image from disk
	if path is not None:
		image = cv2.imread(path)
	# otherwise, the image does not reside on disk
	else:	
		# if the URL is not None, then download the image
		if url is not None:
			resp = urllib.urlopen(url)
			data = resp.read()
		# if the stream is not None, then the image has been uploaded
		elif stream is not None:
			data = stream.read()
		# convert the image to a NumPy array and then read it into
		# OpenCV format
		image = np.asarray(bytearray(data), dtype="uint8")
		image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
	# return the image
	return image
```

I’m defining the FACE_DETECTOR_PATH (Lines 11 and 12), which is simply the path to where the pre-trained OpenCV face detector lives — in this case, I’ve included the pre-trained face detector inside the face_detector/cascades application.

Now that we have our image in OpenCV format (whether it was uploaded via multi-part form encoded data or via URL), we start by converting our input image to grayscale. We discard any color information since color add little to face detection accuracy.

From there we load our face detector on Line 42, supplying the path to our pre-trained face detector. Now that our face detector is loaded, we can apply the detectMultiScale method and detect the actual faces.

The detectMultiScale function returns a list of bounding boxes, or simply the (x, y)-coordinates, and width and height, of the faces in the image. Given this list of bounding boxes, we package them into our data dictionary and ship them back to the user on Lines 47-53.

#### Update the URLs to include an endpoint to our API

Simply open up the cv_api/cv_api/urls.py file, and update it to include a URL endpoint to our face detection view:

```
from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    url(r'^face_detection/detect/$', 'face_detector.views.detect'),
    # url(r'^$', 'cv_api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
```

#### Run the Django test server

Navigate back to the cv_api project root and fire up the test server:

```
$ python manage.py runserver
```

If you open up your web browser and point it to http://localhost:8000/face_detection/detect/ you should see the JSON response from our face detection API.

#### Test out the face detection API via cURL

Let’s construct the command to interact with our face detection API via cURL:

```
$ curl -X POST 'http://localhost:8000/face_detection/detect/' -d 'url=https://i0.wp.com/www.newsgram.com/wp-content/uploads/2020/04/Narendra-Modi.jpg' ; echo ""
{"num_faces": 1, "success": true, "faces": [[410, 100, 591, 281]]}
```

And sure enough, based on the output we were able to detect Modi’s face (although we can’t yet visualize the bounding box, we’ll do that in the following section).

#### Write some Python code to interact with the face detection API:

Open up a new file, name it test_api.py , and include the following code:

```
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
cv2.imshow("modi.jpg", image)
cv2.waitKey(0)
# load our image and now use the face detection API to find faces in
# images by uploading an image directly
image = cv2.imread("path to image file in system")
payload = {"image": open("path", "rb")}
r = requests.post(url, files=payload).json()
print "name.jpg: {}".format(r)
# loop over the faces and draw them on the image
for (startX, startY, endX, endY) in r["faces"]:
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
# show the output image
cv2.imshow("name.jpg", image)
cv2.waitKey(0)
```

To see our script in action, just execute the following command:

```
$ python test_api.py
```

First, we’ll see the image of the bounding box drawn around Modi’s face followed by the successful detection and bouding box over your custom image.

This is the output I got when I tried with Tom Cruise's image

<img src = "https://github.com/sreelakshmig009/Intern-Work/blob/face_detection/int-cv-2/Face%20Detection%20Using%20OpenCV%20and%20Django/images/tomcruise.jpg">
