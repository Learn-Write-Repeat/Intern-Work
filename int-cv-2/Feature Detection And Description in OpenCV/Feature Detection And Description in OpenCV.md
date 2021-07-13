<img src="https://github.com/sreelakshmig009/Intern-Work/blob/feature_detection/int-cv-2/Feature%20Detection%20And%20Description%20in%20OpenCV/Images/DevIncept.jpeg">

# Topic: Feature Detection And Description in OpenCV

*  **What is Feature Detection and Description?**

   * We humans distinguish one thing or object from another flawlessly in our daily lives because we don't pay attention to how this happens; it's all pre-programmed in our brain.
 
   * If we see an image or item, we look at it intently and try to uncover a pattern that will help us distinguish it from others, and this all happens in the background.


<img style="float:center;" src="https://github.com/sreelakshmig009/Intern-Work/blob/feature_detection/int-cv-2/Feature%20Detection%20And%20Description%20in%20OpenCV/Images/reference1.png" > 
   


   * When we look at the above image, our brain begins to notice a pattern, such as the black box representing the sky, the white box representing the building's windows, and the red box representing the building's walls.
   
   * All of these characteristics may be discovered simply by looking at the photograph.We can look for this feature in other photos or objects once we've found it in this one.
   
   * This method is called <b>Feature Detection</b>, and after we locate a feature, we describe it in our own words, such as a black box representing the sky, a white box representing a window, and so on.
 
   * We seek for the same features in other photographs by describing the feature, which is known as Feature Description.

   * The computer does the same thing by describing the region around the box so that it can discover it in other images and objects.
 
*  **There are various algorithm we can use for Feature Detection some as follows:**

   * Harris Corner Detection

   * Shi-Tomasi Corner Detector
   
   * SIFT algorithm(Scale-Invariant Feature Transform)

   * SURF (Speeded-Up Robust Features)

* SIFT is excellent, but it's slower, so people need a faster version for Features detection therefore in early 2006, three people, H. Bay, T. Tuytelaars, and L. Van Gool, released a paper presenting a new algorithm called SURF.
   
* FAST algorithm (Features from Accelerated Segment Test)

   * All of the above algorithms are beneficial in some way, but they aren't very useful in real-world applications, which is why Edward Rosten and Tom Drummond introduced this approach in their work "Machine learning for high-speed corner identification" in 2006, and later refined it in 2010.

   * BRIEF (Binary Robust Independent Elementary Features)

   * SIFT uses floating-point numbers, so its take 512bytes dim vector for descriptors while SURF uses 256 bytes for descriptors. Creating this vector for thousands of features takes a lot of memory, which is challenging for resource-constrained applications like embedded devices. That is why BRIEF was invented in, and it is a faster method for calculating and matching feature descriptors. One disadvantage is that it simply uses features descriptors; to acquire the final output, we must utilise feature detection.

* ORB(Oriented FAST and Rotated BRIEF)

   * SIFT and SURF are useful in their own right, but what if you have to pay a hefty annual fee to use them in your applications. Because they are patented, we must pay to use them. To address this issue, OpenCV developers created ORB(Oriented FAST and Rotated BRIEF), a new free alternative to SIFT and SURF.

<b>Once we learn about feature detection and description we need to know about how that feature is going to match with other images in OpenCV we have two methods to do this task as follows:</b>
      
   * Brute-Force Matcher:

It simply compares the descriptor of one feature in the first set to all other features in the second set, calculates the distance between them, and returns the closest match.

  * FLANN based Matcher:

FLANN stands for Fast Library for Nearest Neighbors. It comprises a number of algorithms for determining Nearest Neighbors and is faster than a brute-force matcher.

<a href="https://github.com/sreelakshmig009/Intern-Work/tree/feature_detection/int-cv-2/Feature%20Detection%20And%20Description%20in%20OpenCV/Source%20Code">
  Get the code example here
</a>
