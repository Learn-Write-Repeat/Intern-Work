# Edge Detection (Canny Edge Detection)

> The Canny edge detector is an edge detection operator that detects a wide range of edges in images using a multi-stage algorithm. It was created in 1986 by John F. Canny.

- The Canny algorithm, also known as the best detector, aims to meet three main criteria: The different stages of the Canny algorithm are
    - **Noise Reduction**: Because edge detection is sensitive to image noise, the first step is to remove the noise with a 5x5 Gaussian filter.
    - **Finding the Image's Intensity Gradient**: The smoothed image is then filtered in both the horizontal and vertical directions with a Sobel kernel to obtain the first derivative in both the horizontal (Gx) and vertical (Vx) directions (Gy). We can find the edge gradient and direction for each pixel using these two images:

        ![images/equation.png](images/equation.png)

    - **Non-maximum Suppression**: After obtaining the gradient magnitude and direction, the image is fully scanned to remove any unwanted pixels that do not form the edge. For this, each pixel is checked to see if it is a local maximum in its neighborhood in the gradient direction.
    - **Hysteresis Thresholding**: This stage determines which edges are genuine and which are not. We'll need two threshold values, minVal and maxVal, for this. Any edges with an intensity gradient greater than maxVal are certain to be edges, while those with an intensity gradient less than minVal are certain to be non-edges, and should be discarded. Based on their connectivity, those who fall between these two thresholds are classified as edges or non-edges. They are considered to be part of edges if they are connected to "sure-edge" pixels. Otherwise, they are discarded as well.

> All of the above is combined into a single function, cv.Canny, in OpenCV (). Our input image is the first argument. Our minVal and maxVal arguments are the second and third arguments, respectively. Aperture size is the third argument. It refers to the size of the Sobel kernel that is used to locate image gradients. It is set to 3 by default. The last argument is L2gradient, which specifies the gradient magnitude equation. If True, it uses the more accurate equation mentioned above; otherwise, it uses this function: Edge Gradient (G)=|Gx|+|Gy|. It is False by default.

- **The Code**

    ```python
    import cv2 #Import Libraries

    img = cv2.imread("sample.jpg", -1) #Loading the sample image
    cv2.imshow(img) #Displaying the input image
    ```

    ![images/sample.jpg](images/sample.jpg)