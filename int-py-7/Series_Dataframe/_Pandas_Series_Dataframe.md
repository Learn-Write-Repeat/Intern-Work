# <font color ="Purple"> PANDAS SERIES,DATAFRAME</font>
## _Introduction_

### What is a Series?

- A Pandas Series is an one-dimensional array which consists of various types of data (such as integer,float,string,python objects etc.) in a table.


### Syntax
**Example 1:**
Creating a simple Pandas Series using array.
#### In order to create a series from array: 
- First import numpy module.
- Then use array() function.


```python
import pandas as pd        #importing pandas module
import numpy as np         #importing numpy module

data=np.array(['D','E','V','I','N','C','E','P','T'])
series=pd.Series(data)

print("Output:\n")
print(series)
```

    Output:
    
    0    D
    1    E
    2    V
    3    I
    4    N
    5    C
    6    E
    7    P
    8    T
    dtype: object
    

**Example 2:** Creating Pandas Series using lists.
#### In order to create a series from lists:
- First create a list.
- Then create a series from list.




```python
import pandas as pd 
list = ['D','E','V','I','N','C','E','P','T']  #Creating a list
series=pd.Series(list)
print("Output:\n")
print(series)

```

    Output:
    
    0    D
    1    E
    2    V
    3    I
    4    N
    5    C
    6    E
    7    P
    8    T
    dtype: object
    

### Key/Value Objects as Series

We can also use a key/value object, like a dictionary, when creating a Series in Pandas

**Example 3:**



```python
import pandas as pd

marks = {"Physics": 80, "Chemistry": 87, "Mathematics": 95,"English": 86}

data = pd.Series(marks)
print("Output:\n")

print(data)
```

    Output:
    
    Physics        80
    Chemistry      87
    Mathematics    95
    English        86
    dtype: int64
    

## Accessing Element of Series

There are two ways for accessing element from series:
- Accessing Element from series with position.
- Accessing Element from series with label (index).

**Accessing Element from series with position:**

In order to access element using position number we use the index operator[ ]. The index must be an integer value. If we want to access more than one element from a series we use slicing operation.



```python
import pandas as pd 
list = ['D','E','V','I','N','C','E','P','T']
series=pd.Series(list)
print("Output:\n")
print(series[:7])                #printing the first 7 elements from series
```

    Output:
    
    0    D
    1    E
    2    V
    3    I
    4    N
    5    C
    6    E
    dtype: object
    

**Accessing Element from series with label (index):**

In order to access element from series,we have to set values by index label and then accessing single element using index label


```python
import pandas as pd 
list = ['D','E','V','I','N','C','E','P','T']
series=pd.Series(list,index=[2,4,6,8,10,12,14,16,18])
print("Output:\n")
print(series[14]) 
```

    Output:
    
    E
    

## Pandas DataFrames

### What is a DataFrame?

A Pandas DataFrame is a 2 dimensional data structure just like a 2D array in which data are arranged in tabular fashion with rows and columns. Pandas DataFrame are mutable i.e data can be remodified. 

**Example**
- Create a simple Pandas DataFrame:


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"]
}
                                                 
df = pd.DataFrame(data)                            #load data into a DataFrame object:
print("Output:\n")
print(df) 
```

    Output:
    
          Name    Place
    0  Anandhi  Chennai
    1    Rahul   Bolpur
    2   Nikita   Mumbai
    

### Creating a Pandas DataFrame

Like Series,DataFrame can also be created from Lists, dictionary and list of dictionary etc.

### Creating a dataframe using List:

**Example:**






```python
import pandas as pd
 
lst = ['I', 'got', 'internship', 'opportunity', 
            'in', 'devincept']
 
df = pd.DataFrame(lst)          # creating dataframe objects using lists
print("Output:\n")
print(df)
```

    Output:
    
                 0
    0            I
    1          got
    2   internship
    3  opportunity
    4           in
    5    devincept
    

### Creating DataFrame from dict of ndarray/lists:

**Example:**


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"]
}
                                                 
df = pd.DataFrame(data)                            #load data into a DataFrame object using dictionary:
print("Output:\n")
print(df)
```

    Output:
    
          Name    Place
    0  Anandhi  Chennai
    1    Rahul   Bolpur
    2   Nikita   Mumbai
    

### Difference Between Series And DataFrame

|Sl.No|<center>Series|<center>Dataframe|
|-----|--------------|-----------------| 
|1|1-Dimensional Datastructure.|2-Dimensional DataStructure.|    
|2|Consists of a single list|Consists of two or more than two series|
|3|To initialize a series,use pd.Series()|To initialize a dataframe,use pd.DataFrame()|    
   

### Accessing Elements In DataFrame

#### Column Selection: 
In Order to select a column in Pandas DataFrame, we can either access the columns by calling them by their columns name.

**Example:**


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"]
}
                                                 
df = pd.DataFrame(data)                            
print("Output:\n")
print(df["Name"])
```

    Output:
    
    0    Anandhi
    1      Rahul
    2     Nikita
    Name: Name, dtype: object
    

#### Row Selection:

In Order to select a specific row in Pandas DataFrame, Pandas use the <font color="red">loc</font> attribute to return one or more specified row.

**Example:**


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"]
}
                                                 
df = pd.DataFrame(data)                            
print("Output:\n")
print(df.loc[0])
```

    Output:
    
    Name     Anandhi
    Place    Chennai
    Name: 0, dtype: object
    

### Named Indexes
With the index argument, we can name our own indexes.

**Example:**


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"],
  "PhoneNo":[667777,987558,687655] 
}
                                                 
df = pd.DataFrame(data,index=["T1","T2","T3"])                            
print("Output:\n")
print(df)
```

    Output:
    
           Name    Place  PhoneNo
    T1  Anandhi  Chennai   667777
    T2    Rahul   Bolpur   987558
    T3   Nikita   Mumbai   687655
    

### Locate named indexes using loc attribute

**Example:**


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"],
  "PhoneNo":[667777,987558,687655] 
}
                                                 
df = pd.DataFrame(data,index=["T1","T2","T3"])                            
print("Output:\n")
print(df.loc["T2"])
```

    Output:
    
    Name        Rahul
    Place      Bolpur
    PhoneNo    987558
    Name: T2, dtype: object
    

### Iterating over rows and columns

Iteration is a general term for taking each item of something, one after another. Pandas DataFrame consists of rows and columns so, in order to iterate over dataframe, we have to iterate a dataframe like a dictionary.

### Iterating over rows :
In order to iterate over rows, we can use three function iteritems(), iterrows(), itertuples() . These three function will help in iteration over rows.

**Example:**


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"],
  "PhoneNo":[667777,987558,687655] 
}
                                                 
df = pd.DataFrame(data)  
print("Output:\n")
for i,j in df.iterrows():
    print(i,j)
    print()
```

    Output:
    
    0 Name       Anandhi
    Place      Chennai
    PhoneNo     667777
    Name: 0, dtype: object
    
    1 Name        Rahul
    Place      Bolpur
    PhoneNo    987558
    Name: 1, dtype: object
    
    2 Name       Nikita
    Place      Mumbai
    PhoneNo    687655
    Name: 2, dtype: object
    
    

### Iterating over Columns :
In order to iterate over columns, we need to create a list of dataframe columns and then iterating through that list to pull out the dataframe columns.

**Example:**


```python
import pandas as pd

data = {
  "Name": ["Anandhi", "Rahul", "Nikita"],
  "Place": ["Chennai","Bolpur","Mumbai"],
  "PhoneNo":[667777,987558,687655] 
}

df = pd.DataFrame(data)
column=list(df)
print("Output:\n")
for i in column:
    print(df[i][2])
```

    Output:
    
    Nikita
    Mumbai
    687655
    

### Inbuilt DataFrame Functions:

|FUNCTION|<center>DESCRIPTION                     |
|--------|----------------------------------------|
|insert()|Method inserts a column into a DataFrame|
|unique()|Method extracts the unique values in the dataframe|
|isnull()|Method creates a Boolean Series for extracting rows with null values|
|notnull()|Method creates a Boolean Series for extracting rows with non-null values|
|rename()|Method is called on a DataFrame to change the names of the index labels or column names|
|shape()|Method returns a tuple representing the dimensionality of the DataFrame|
