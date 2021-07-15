# BOX PLOT
It is an another way to represent the data graphically , which basically helps us to measure that how well distributed the data in a dataset is . 
It displays the distribution of data in 5 number summary as follows:

1. Minimum
2. First Quartile (Q1 - 25th Percentile)
3. Median (Mid-value)
4. Third Quartile(Q3- 75th Percentile)
5. Maximum
 ![Image of boxplot](https://miro.medium.com/max/1838/1*2c21SkzJMf3frPXPAR_gZA.png)
It can also tell you if your data is symmetrical, how tightly your data is grouped, and if and how your data is skewed.

## FUNCTIONS OF BOX PLOT
 - Tell you the values of outliers .
 - Identify if data is symmetrical .
 - Determine how tightly data is grouped .
 - See if your data is skewed.

OUTLIERS
A value that "lies outside" (is much smaller or larger than) most of the other values in a set of data.
For example in the scores 25,29,3,32,85,33,27,28 both 3 and 85 are "outliers".

### BOX PLOT CHART

- importing the required liabraries

      import pandas as pd
      import numpy as np
      import matplotlib.pyplot as plt
      %matplotlib inline

      data= np.array([10,30,65,80,90])
      data

  array([10,30,65,80,90])

      plt.boxplot(data)
      plt.show()

![box chart](https://miro.medium.com/max/350/1*JJSEEZ6cWNHJiYkb-y7lKg.png)









#  WORKING WITH IMAGES
 
 There are different ways of Reading/inserting and working with images .
 We can import the Pillow(PIL) liabrary to work with images.
 ## Opening the image

    from PIL import Image
    DS= Image.open('rose.jpg')
    DS
![IMAGE OPPENING](https://www.imgonline.com.ua/examples/rose-mini.jpg)

## Image size
    DS.size
(500, 282)

## File name
    DS.filename

'rose.jpg'
## Image description
    DS.format_description
'JPEG (ISO 10918)'

## Cropping the image

    DS.crop((0,0,250,142))
![crop Image](https://www.imgonline.com.ua/examples/image_part_001.jpg)
