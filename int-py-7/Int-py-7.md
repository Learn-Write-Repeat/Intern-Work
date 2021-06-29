# <font color=green>Tuples in Python</font>

### What is tuple?

A tuple is a collection of objects or sequences just like lists.Tuples are used to store multiple items in a single variable. The differences between tuples and lists are lists are mutable, whereas tuples are immutable it means cannot be changed. Unlike lists and tuples use parentheses, whereas lists use square brackets.You can access tuple items by referring to the index number, inside square brackets and index number starts from 0.

### Syntax

**Example1**


```python
tuple1 = ()  #Empty Tuple
print("Output:\n")
print("tuple1 is empty:",tuple1)
```

    Output:
    
    tuple1 is empty: ()
    

**Example2**


```python
tuple2 = ("apple", "banana", "cherry")     #Tuple Items
print("Output:\n ")
print(tuple2)
```

    Output:
     
    ('apple', 'banana', 'cherry')
    

### Tuple Advantages over List
<ol>
<li>Program execution is faster when manipulating a tuple than it is for the equivalent list.</li>

<li>Sometimes you don’t want data to be modified. If the values in the collection are meant to remain constant for the life of the program, using a tuple instead of a list guards against accidental modification.</li>

<li>There is another Python data type that you will encounter shortly called a dictionary, which requires as one of its components a value that is of an immutable type. A tuple can be used for this purpose, whereas a list can’t be.</li>

### How to Access Tuple Items

* Print the second item in the tuple


```python
tuple2 = ("apple", "banana", "cherry")      #Accessing tuple items
print("Output:\n ")
print(tuple2[1])
```

    Output:
     
    banana
    

### Negative Indexing

* Print the last item of the tuple


```python
tuple2 = ("apple", "banana", "cherry")  #Accessing last item
print("Output:\n ")
print(tuple2[-1])
```

    Output:
     
    cherry
    

### Range of Indexes / Slicing

* You can specify a range of indexes by specifying where to start and where to end the range.

* When specifying a range, the return value will be a new tuple with the specified items.

**Example**
* Return the third, fourth, and fifth item


```python
tuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")   #slicing
print("Output:\n ")
print(tuple2[2:5])
```

    Output:
     
    ('cherry', 'orange', 'kiwi')
    

### Change Tuple Values


Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable.
But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

**Convert the tuple into a list to be able to change it**
#### For Example


```python
x = ("apple", "banana", "cherry")  
y = list(x)                                  #Changing tuple to list
y[1] = "kiwi"                                #Adding item in list
x = tuple(y) 
print("Output:\n ")

print(x)
```

    Output:
     
    ('apple', 'kiwi', 'cherry')
    

### Remove Items
* Note: You cannot remove items in a tuple.

Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items.

**Example**




```python
tuple2 = ("apple", "banana", "cherry")
y = list(tuple2)
y.remove("apple")                     #Removing the item 'apple'
tuple2 = tuple(y)
print("Output:\n ")                   #After Removal
print(tuple2)
```

    Output:
     
    ('banana', 'cherry')
    

### Loop Through a Tuple
You can loop through the tuple items by using a <font color=red>for</font> loop.
#### Iterate through the items and print the values
**Example**


```python
tuple2 = ("apple", "banana", "cherry")
print("Output:\n") 
for x in tuple2: 
  print(x)
```

    Output:
    
    apple
    banana
    cherry
    

### Basic Operations of Tuple

|<center>Python Expression|<center>Result|Operation|
|-----------------|-------------|-------------|
|(1,2,3)+(8,9,9)|(1,2,3,8,9,9)|Concatination|
|len((4,5,6))|3|Length|
|7 in (1,4,7)|True|Membership|
|for n in (1,3,5):print (n)|1 3 5|Iteration|




### Built-in Function of Tuple


|<center>Function|<center>Description|
|------------------|----------|
|cmp(tuple1,tuple2)|It compares two tuples and returns true if tuple1 is greater than tuple2 otherwise false.|
|len(tuple)|It calculates the length of the tuple.|
|max(tuple)|It returns the maximum element of the tuple.|
|min(tuple)|It returns the minimum element of the tuple.|
|tuple(seq)|It converts the specified sequence to the tuple.|
