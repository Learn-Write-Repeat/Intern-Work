# Feature detection , description and Matching using Brout-Force matching method
import cv2 as cv
import numpy as np

img1 = cv.imread("path",cv.IMREAD_GRAYSCALE)
img2 = cv.imread("path",cv.IMREAD_GRAYSCALE)

# ORB Detector
orb = cv.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

#Brute Force Matching
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)
matches = bf.match(des1,des2)
matches = sorted(matches,key = lambda x:x.distance)

# Draw the macthing features
matchesing_result = cv.drawMatches(img1, kp1, img2, kp2, matches[:50], None,flags=2)

# Display the Output
cv.imshow("Img1",img1)
cv.imshow("Img2",img2)
cv.imshow("Result",matchesing_result)
cv.waitKey(0)
cv.destroyAllWindows()
