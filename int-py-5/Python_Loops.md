<p align="center">
  <img src="https://w3points.com/wp-content/uploads/2018/05/Python-Loop-min.jpg">
</p>

### _In computer science, a loop is a programming structure that repeats a sequence of instructions until a specific condition is met. Loops allow programmers to shorten what could be hundreds of lines of code to just a few. They use loops to cycle through values, add sums of numbers, repeat functions, and many other things._
---

# What are Loops?
Loops are a programming element that repeat a portion of code a set number of times until the desired process is complete. Repetitive tasks are common in programming, and loops are essential to save time and minimize errors. Loops are important in Python or in any other programming language as they help you to execute a block of code repeatedly.  
- Loops have set of statements which are executed until the condition becomes false.
- Loops are used for iteration over a sequence of statements.
- We can use loops to iterate over lists, tuples, sets, dictionaries.
- We can iterate over a string too as it has set of characters.
---

# Purpose of Loops
Loops are useful where we need to use a block of code over and over without writing it multiple times. The number of times could be a certain number, or a certain condition being met. Two major uses of loop are producing output and searching for information.
- _Producing output_: You can reduce a long series of repetitive instructions down to one instruction by using a loop. For example, a long series of multiplying numbers can be rewritten and condensed into a For loop. 
- _Searching for information_: Loops are incredibly useful when we want to find a specific piece of information contained in a list, tuple or anyother data structure.
### Two Ways to Implement Loops
1.	Repeating a block of statements with a specified and previously defined number of iterations to be completed. 
2.	Repeating a block of statements where the number of iterations is unknown and is based on other variables or conditions.
---

# Types of Loops
Two major types of loops in Python are _FOR_ loops and _WHILE_ loops. A For loop will run a preset number of times whereas a While loop will run a variable number of times.
- ___FOR:___ For loops are used when you know how many times you want to run an algorithm before stopping. 
- ___WHILE:___ A While loop is similar to a For loop but a While loop runs a variable number of times and uses a _conditional_.

For loop and While loop are _entry-controlled_ loops, that is the test condition is tested before entering the loop body. 

---
# The FOR Loop
<p align="center">
  <img height=400, width=700, src="https://files.realpython.com/media/Python-for-Loops-Definite-Iteration_Watermarked.b38126d495e1.jpg">
</p>

- A for loop is used for iterating over a sequence (list, a tuple, a dictionary, a set, or a string).
- With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

### _Syntax:_ 
```
1. for any_variable in sequence_name:
        Body of the loop
```
```
2. for any_variable in range(start, end, step):
        Body of the loop
```
```
3. for any_variable in xrange(start, end, step):
        Body of the loop
```
1. In the first syntax, for loop is just used to access and print the values from the sequence.
2. In the second syntax, ”range” keyword is used to limit the access of value. Inside the range three parameters are given, 
* 'start': the first one is the start which is the starting index.
* 'end': which is nothing but the ending index 
* 'step': is used to tell the loop about incrementing values.
3. In the third syntax,which is similar to second one but the difference between range and xrange is that the range function returns a new list with numbers of that specified range, whereas xrange returns an iterator, which is more efficient.
- (Python 3 uses the range function, which acts like xrange). Note that the range function is zero based.

## Workflow
 
<p align="center">
  <img src="https://www.tutorialspoint.com/python/images/python_for_loop.jpg">
</p>

> Note: The for loop does not require an indexing variable to be set beforehand and there is no need for iteration; it can be done automatically.

## Example 1
To print values from a list:
```
List_1 = [1,2,3,4,5]
for i in List_1:    #Looping statement to check condition
    print(i)        #body of the loop
```
#### Output:
```
1
2
3
4
5
```
- In the first line, a list is assigned with some values
- Then, in for loop variable i is taken and a list name is given.
- Then, inside the loop, the print statement will be executed.

## Example 2
To print number from 1 to 5:
```
for i in range(1,6): #Looping statement with condition.
    print(i)         #body of the loop
```
#### Output:
```
1
2
3
4
5
```
## Example 3
```
for x in range(5):
    print(x)
print("end")
for x in range(3, 6):
    print(x)
print("end")
for x in range(3, 8, 2):
    print(x)
```
#### Output:
```
0
1
2
3
4
end
3
4
5
end
3
5
7
```
> Note: In for loop, the end index should be set in such a way that if you want to print till 5, set the end index to 6, then only you will get a result including 5 else it will not.

## _The Pass Statement_ 
- For Loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
### Example
```
for i in [1,2,3,4]:
    pass       # having an empty for loop, would raise an error without the pass statement
```
#### Output:
Returns nothing

## _Nested Loop_
- A nested loop is a loop inside a loop.
- The _inner loop_ will be executed one time for each iteration of the "outer loop".
### Example
```
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)
```
#### Output:
```
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry
```
---

# The WHILE Loop
<p align="center">
  <img height=400, width=700, src="https://files.realpython.com/media/Python-while-Loops-Indefinite-Iteration_Watermarked.ef0b89ed9dae.jpg">
</p>

- While loop repeats a statement or a group of statements while a given condition is TRUE. It tests the condition before executing the loop body.
- It executes a piece of code over and over again while a given condition still holds true.
- We generally use this loop when we don't know the number of times to iterate beforehand.
> The above definition also highlights the three components that you need to construct the while loop in Python: 
1.  The while keyword;
2.  A condition that transacts to either True or False;
3. A block of code that you want to execute repeatedly.

### _Syntax:_ 
```
while(test expression): 
    Executable statements
```
## Workflow
<p align="center">
  <img src="https://www.tutorialspoint.com/python/images/python_while_loop.jpg">
</p>

1. In the while loop, test expression is checked first.
2. The body of the loop is entered only if the test expression evaluates toTrue.
3. After one iteration, the test expression is checked again. This process continues until the test expression evaluates to False.
4. The body of the while loop is determined through indentation.
5. The body starts with indentation and the first unintended line marks the end.

> Note: Python interprets any non-zero value as True, None and Zero as False.

## Incrementation 
- It is very important to increment the values manually by assigning a variable, failing to do so will result in an infinite loop.

## Example
```
# Program to print numbers from 1 to 5:
n = 5
while(n <= 5):   #test condition
    print(n)     #body of the loop
    i = i+1 	 #iteration
```
### Output:
```
1
2
3
4
5
```

- In the first line, a value of 5 is assigned to the variable ‘n’.
- Then, the while loop starts. Here the loop condition is (n<=5, that is n less than or equal to 5). 
- When the condition is true, then it will enter the loop.
- So, the statement inside the loop(print(n)) will be executed and then incrementation occurs by one value.
---
## BREAK & CONTINUE

<p align="center">
  <img height=400, width=250, src="https://files.realpython.com/media/t.899f357dd948.png">
</p>

### _The break Statement_
- With break statement we can stop the loop even if the while condition is true.
#### Example:
Exit the loop when i is 3.
```
i = 1
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
```
#### Output:
```
1
2
3
```
### _The continue Statement_
- With continue statement we can stop the current iteration, and continue with the next.
#### Example:
Continue to the next iteration if i is 3:
```
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
```
#### Output:
```
1
2
4
5
```
> Note that number 3 is missing in the result.
--- 
# _The else Statement_
- With else statement we can run a block of code once when the condition no longer is true.

## else in for loop

<p align="center">
  <img src="https://www.learnbyexample.org/wp-content/uploads/python/Python-for-Loop-Syntax.png">
</p>

### Example
```
colors = ['red', 'green', 'blue', 'yellow']
for x in colors:
    print(x)
else:
    print('Done!')
```
#### Output:
```
red
green
blue
yellow
Done!
```
## else in while loop

<p align="center">
  <img src=https://www.learnbyexample.org/wp-content/uploads/python/Python-while-Loop-Syntax.png>
</p>

### Example
Print a message once the condition is false
```
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print('i is no longer less than 5')
```
#### Output:
```
1
2
3
4
i is no longer less than 5
```
> This is a unique feature of Python, an optional else clause at the end of a loop which is not found in most other programming languages. 
---
