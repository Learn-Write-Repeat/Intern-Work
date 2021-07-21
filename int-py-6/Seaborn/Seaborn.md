<p align="center">
   <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" alt="Seaborn"
        width="500" height="250">
   <br />
   <b>Seaborn</b>
</p>

----

<img src="https://www.fromthegenesis.com/wp-content/uploads/2018/11/seaborn.jpg" alt="seaborn" width="750" height="700">

<img src="https://miro.medium.com/max/1400/1*3VgCwcZraA0u5hMHpRhJcw.png" alt="Seaborn Plots" width ="800" height="500">

Data Visualization tools are of great importance in the analytics industry as they give a clear idea of the complex data involved. Python is one of the most popular languages for visualization with its variety of tools. 
Two of Python’s greatest visualization tools are Matplotlib and Seaborn. Seaborn library is basically based on Matplotlib.

# Seaborn

#### “If Matplotlib “tries to make easy things easy and hard things possible”, seaborn tries to make a well-defined set of hard things easy too” – Michael Waskom (Creator of Seaborn)."

Seaborn is a data visualization library built on top of Matplotlib. Seaborn is often used because it makes attractive visualizations and works easily with Pandas and NumPy. While with Matplotlib you often have to write multiple lines of code to create a plot, Seaborn makes assumptions on what you want which often translates into getting the same plot with 1 line of code.

### Some of the Seaborn functionalities:
1.	Dataset oriented API to determine the relationship between variables.
2.	Automatic estimation and plotting of linear regression plots.
3.	It supports high-level abstractions for multi-plot grids.
4.	Visualizing univariate and bivariate distribution.


## Install Seaborn
If you have Python and PIP already installed on a system, install it using this command:
```
pip install seaborn
```
Anaconda distribution:
```
conda install seaborn
```

# Matplotlib vs Seaborn
|     | Matplotlib | Seaborn |
|----------|---------------|---------|
|Functionality|  Matplotlib is mainly deployed for basic plotting. Visualization using Matplotlib generally consists of bars, pies, lines, scatter plots and so on.|  Seaborn, on the other hand, provides a variety of visualization patterns. It uses fewer syntax and has easily interesting default themes. It specializes in statistics visualization and is used if one has to summarize data in visualizations and also show the distribution in the data.  |
|     Handling Multiple Figures   |   Matplotlib has multiple figures can be opened, but need to be closed explicitly. plt.close() only closes the current figure. plt.close(‘all’) would close em all.        |    Seaborn automates the creation of multiple figures. This sometimes leads to OOM (out of memory) issues    |
|       Visualization |     Matplotlib is a graphics package for data visualization in Python. It is well integrated with NumPy and Pandas. The pyplot module mirrors the MATLAB plotting commands closely. Hence, MATLAB users can easily transit to plotting with Python.      |      Seaborn is more integrated for working with Pandas data frames. It extends the Matplotlib library for creating beautiful graphics with Python using a more straightforward set of methods  |
|       Data frames and Arrays |     Matplotlib works with data frames and arrays. It has different stateful APIs for plotting. The figures and aces are represented by the object and therefore plot() like calls without parameters suffices, without having to manage parameters.      |     Seaborn works with the dataset as a whole and is much more intuitive than Matplotlib. For Seaborn, replot() is the entry API with ‘kind’ parameter to specify the type of plot which could be line, bar, or many of the other types. Seaborn is not stateful. Hence, plot() would require passing the object.   |
|      Flexibility  |       Matplotlib is highly customizable and powerful    |     : Seaborn avoids a ton of boilerplate by providing default themes which are commonly used.   |
|       Use Cases |     Pandas uses Matplotlib. It is a neat wrapper around Matplotlib.      |   Seaborn is for more specific use cases. Also, it is Matplotlib under the hood. It is specially meant for statistical plotting.     |



# Functions of  Various Plots

## Relational plots
|      Plot |     Function|
|------------|--------------------|
|  relplot  |   Figure-level interface for drawing relational plots onto a FacetGrid.    |
|    scatterplot|    Draw a scatter plot with possibility of several semantic groupings.   |
|    lineplot|Draw line plot with possibility of several semantic groupings.




## Distribution plots
|      Plot |     Function|
|----------------|----------------|
|  displot        |  Figure-level interface for drawing distribution plots onto a FacetGrid.        |
|    histplot      |    Plot univariate or bivariate histograms to show distributions of datasets.      |
|       kdeplot   |      Plot univariate or bivariate distributions using kernel density estimation.    |
|       ecdfplot   |      Plot empirical cumulative distribution functions.    |
|      rugplot    |    Plot marginal distributions by drawing ticks along the x and y axes.      |
|       distplot |  DEPRECATED: Flexibly plot a univariate distribution of observations.|


## Utility functions
|    load_dataset |     Load an example dataset from the online repository (requires internet).      |
|-------------|---------------|
|        get_dataset_names    |     Report available example datasets, useful for reporting issues.        |
|get_data_home|Return a path to the cache directory for example datasets.|
|despine|Remove the top and right spines from plot(s).|
|desaturate|Decrease the saturation channel of a color by some percent.|

Detailed Description: https://seaborn.pydata.org/api.html

# Customizing Seaborn Plots
Seaborn comes with some customized themes and a high-level interface for customizing the looks of the graphs. where the default of the Seaborn is used. It still looks nice and pretty but we can customize the graph according to our own needs.

### Changing Figure Aesthetic:

**set_style()** method is used to set the aesthetic of the plot. It means it affects things like the color of the axes, whether the grid is active or not, or other aesthetic elements. There are five themes available in Seaborn.

-  darkgrid
 -  whitegrid
  - dark
  - white
  - ticks
 
Syntax:

```set_style(style=None, rc=None)```


### Removal of Spines:

Spines are the lines noting the data boundaries and connecting the axis tick marks. It can be removed using the **despine()** method.


Syntax:

```sns.despine(left = True)```



### Changing the figure Size:

The figure size can be changed using the **figure()** method of Matplotlib. figure() method creates a new figure of the specified size passed in the figsize parameter.

### Scaling the plots:

It can be done using the set_context() method. It allows us to override default parameters. This affects things like the size of the labels, lines, and other elements of the plot, but not the overall style. The base context is “notebook”, and the other contexts are “paper”, “talk”, and “poster”. font_scale sets the font size.

Syntax:

```set_context(context=None, font_scale=1, rc=None)```



# Examples For Various Types of Plots

## Relplot()
This function provides us the access to some other different axes-level functions which shows the relationships between two variables with semantic mappings of subsets. It is plotted using the relplot() method.

Syntax:

```seaborn.relplot(x=None, y=None, data=None, **kwargs) ```

```
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

# crrating the relplot
sns.relplot(x='sepal_width', y='species', data=data)

plt.show()
```
### Output

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210119191304/seaborntutorialrelplot.png">


## Scatter Plot
The scatter plot is a mainstay of statistical visualization. It depicts the joint distribution of two variables using a cloud of points, where each point represents an observation in the dataset. This depiction allows the eye to infer a substantial amount of information about whether there is any meaningful relationship between them. It is plotted using the scatterplot() method.

Syntax:

```seaborn.scatterplot(x=None, y=None, data=None, **kwargs)```

```
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.scatterplot(x='sepal_length', y='sepal_width', data=data)
plt.show()
```

### Output


<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210119192107/seaborntutorialscatterplot.png">


## Line Plot
For certain datasets, you may want to consider changes as a function of time in one variable, or as a similarly continuous variable. In this case, drawing a line-plot is a better option. It is plotted using the lineplot() method.

Syntax:

```seaborn.lineplot(x=None, y=None, data=None, **kwargs)```

```
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.lineplot(x='sepal_length', y='species', data=data)
plt.show()
```
### Output
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210119194211/seaborntutoriallineplot.png">


## Bar Plot
A barplot is basically used to aggregate the categorical data according to some methods and by default its the mean. It can also be understood as a visualization of the group by action. To use this plot we choose a categorical column for the x axis and a numerical column for the y axis and we see that it creates a plot taking a mean per categorical column. It can be created using the barplot() method.

Syntax:

```barplot([x, y, hue, data, order, hue_order, …])```

```
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.barplot(x='species', y='sepal_length', data=data)
plt.show()
```
### Output
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210119200703/seabontutorialbarplot.png">


## Pairplot
Pairplot represents pairwise relation across the entire dataframe and supports an additional argument called hue for categorical separation. What it does basically is create a jointplot between every possible numerical column and takes a while if the dataframe is really huge. It is plotted using the pairplot() method.

Syntax:

```pairplot(data[, hue, hue_order, palette, …])```

```
# importing packages
import seaborn as sns
import matplotlib.pyplot as plt

# loading dataset
data = sns.load_dataset("iris")

sns.pairplot(data=data, hue='species')
plt.show()
```
### Output
<img src="https://media.geeksforgeeks.org/wp-content/uploads/20210120122658/seaborntutorialpairplot.png">


## References
https://seaborn.pydata.org/index.html

https://www.geeksforgeeks.org/python-seaborn-tutorial/
