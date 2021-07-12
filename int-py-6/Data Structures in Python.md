<p align="center">
   <img src="https://miro.medium.com/max/1200/1*PPIp7twJJUknfohZqtL8pQ.png" alt="Python Programming"
        width="500" height="150">
   <br />
   <b> DATA STRUCTURES IN PYTHON </b>
</p>

----

## 📋 What is a Data Structure ?
<p align="justify">
Organizing, managing and storing data is important as it enables easier access and efficient modifications. Data Structures allows you to organize your data in such a way that enables you to store collections of data, relate them and perform operations on them accordingly. 
  </p>


### Data Structures in Python can be divided into two types:-
- Built-in data Structures
- User-Defined data Structures


<p align="center">
   <img src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/10/TreeStructure-Data-Structures-in-Python-Edureka1.png" alt="Python Programming"
        width="1000" height="400">
</p>




#### There are 4 Built-in collections or data structure namely:-
- Tuple
- Set
- List
- Dictionary


<p>Now let's look at the Built-in Data Structures : </p>

# Lists
A List is used to store the sequence of various types of data. Data are inclosed inside [ ] brackets seprated by commas(,). Lists are mutable in nature it means data which can be changed when required. Duplicate entries are allowed in list.  A list can also have another list as an item. This is called a nested list.

```
my_list = [] #create empty list
print(my_list)
my_list = [1, 2, 3, 'example', 3.132] #creating list with data
print(my_list)
```
```
Output:
[]
[1, 2, 3, ‘example’, 3.132]
```

### List Methods
##### Python has a set of built-in methods that you can use on lists.
| Method     | Description |
| ----------- | ----------- |
| append()      | Adds an element at the end of the list   |
| clear()  | Removes all the elements from the list       |
| copy()   | Returns a copy of the list       |
| count()   | Returns the number of elements with the specified value     |
| extend()  | Add the elements of a list (or any iterable), to the end of the current list        |
| index()   | Returns the index of the first element with the specified value      |
| insert()   | Adds an element at the specified position       |
| pop()  | Removes the element at the specified position        |
| remove()   |Removes the item with the specified value       |
| reverse()   | Reverses the order of the list        |
| sort()  | Sorts the list      |


# Tuples
A tuple is a collection of objects which ordered and immutable. Tuples are sequences, just like lists. The differences between tuples and lists are mutable, the tuples are immutable it means cannot be changed unlike lists and tuples use parentheses, whereas lists use square brackets.You can access tuple items by referring to the index number, inside square brackets.

```
my_tuple = (1, 2, 3) #create tuple
print(my_tuple) 
```
```
Output:
(1, 2, 3)
```

### Tuple Methods
##### Python has two built-in methods that you can use on Tuples.
| Method     | Description |
| ----------- | ----------- |
|     count()     |    Returns the number of times a specified value occurs in a tuple          |
|        index()  |    Searches the tuple for a specified value and returns the position of where it was found|


# Sets
A set is an unordered collection of items. Every set element is unique and must be immutable it means cannot be changed. The sets remove the duplicate items.
There is no index attached to the elements of the set, i.e., we cannot directly access any element of the set by the index. We can print them all together, or we can get the list of elements by looping through the set.

```
my_set = {1, 2, 3, 4, 5, 5, 5} #create set
print(my_set)
```
```
Output:
{1, 2, 3, 4, 5}
```
### Set Methods
##### Python has a set of built-in methods that you can use on Sets.
| Method     | Description |
| ----------- | ----------- |
|   add()        |   Adds an element to the set            |
|   clear()        |          Removes all the elements from the set     |
|    copy()       |      Returns a copy of the set         |
|      difference()     |     Returns a set containing the difference between two or more sets          |
|       difference_update()    |   Removes the items in this set that are also included in another, specified set            |
|         discard()  |     Remove the specified item          |
|         intersection()  |       	Returns a set, that is the intersection of two other sets        |
|        intersection_update()   |   Removes the items in this set that are not present in other, specified set(s)            |
|         isdisjoint()  |       Returns whether two sets have a intersection or not        |
|          issubset() | Returns whether another set contains this set or not              |
|          issuperset() |        Returns whether this set contains another set or not       |
|         union()  |       Return a set containing the union of sets        |
|     update()      |           Update the set with the union of this set and others    |





# Dictonaries
A dictionaries can be defined as an unordered collection of key-value pairs separated by (:) and enclosed in ({}) braces. The key should be unique and can be of any data type. Keys are used to access elements in dictionary just like index in List. Dictionaries are mutable. i.e. it is possible to add, modify, delete key-value pairs.
```
my_dict = {} #empty dictionary
print(my_dict)
my_dict = {1: 'Python', 2: 'Java'} #dictionary with elements
print(my_dict)
```
```
Output:
{}
{1: ‘Python’, 2: ‘Java’}
```

### Dictionary Methods
##### Python has a set of built-in methods that you can use on Dictionaries.

| Method     | Description |
| ----------- | ----------- |
|  clear()       |   Removes all the elements from the dictionary    |
|    copy()     |   Returns a copy of the dictionary    |
|        fromkeys() |    Returns a dictionary with the specified keys and value   |
|     get()    |  Returns the value of the specified key     |
|      items()   | Returns a list containing a tuple for each key value pair      |
|       keys()  |    Returns a list containing the dictionary's keys   |
|      pop()   |      Removes the element with the specified key |
|       popitem()  |     Removes the last inserted key-value pair  |
|       setdefault()	  |  Returns the value of the specified key. If the key does not exist: insert the key, with the specified value     |
|     update()    | Updates the dictionary with the specified key-value pairs      |
|     values()    |    Returns a list of all the values in the dictionary   |


********************************************************************************************************************
















































