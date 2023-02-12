# Day 1 - What is Programming and Python?
## What is Programming
Programming is a way for us to tell computers what to do. Computer is a very dumb machine and it only does what we tell it to do. Hence we learn programming and tell computers to do what we are very slow at - computation. 
If I ask you to calculate 5+6, you will immediately say 11. 
How about 23453453 X 56456?

You will start searching for a calculator or jump to a new tab to calculate the same. <br>
This 100 days of code series will help you learn python from starting to the end. We will start from 0 and by the time we end this course, I promise you will be a Job ready Python developer!

## What is Python?

-   Python is a dynamically typed, general purpose programming language that supports an object-oriented programming approach as well as a functional programming approach.
-   Python is an interpreted and a high-level programming language.
-   It was created by Guido Van Rossum in 1989. 

## Features of Python

-   Python is simple and easy to understand.
-   It is Interpreted and platform-independent which makes debugging very easy.
-   Python is an open-source programming language.
-   Python provides very big library support. Some of the popular libraries include NumPy, Tensorflow, Selenium, OpenCV, etc.
-   It is possible to integrate other programming languages within python.

## What is Python used for

-   Python is used in Data Visualization to create plots and graphical representations.
-   Python helps in Data Analytics to analyze and understand raw data for insights and trends.
-   It is used in AI and Machine Learning to simulate human behavior and to learn from past data without hard coding.
-   It is used to create web applications.
-   It can be used to handle databases.
-   It is used in business and accounting to perform complex mathematical operations along with quantitative and qualitative analysis.

<br>

# Day 2 - Why I love python (And you will too...)

## What can Python do for you?

I want to show you some python programs which will surely inspire you to create your own versions of the same as we progress through this tutorial. Do not try to recreate them just yet if you are a beginner and just started working on Python. We will make progress gradually trust me. [Link](https://github.com/Aman1337g/Python-notes-and-codes/tree/main/Projects)

<br>

# Day 3 - Modules and pip in Python!

Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:

1. **Built in Modules** - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
2. **External Modules** - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

## The pip command

It can be used as a package manager [pip](https://pip.pypa.io/en/stable/) to install a python module. Lets install a module called pandas using the following command

```py
pip install pandas
```

## Using a module in Python (Usage)

We use the import syntax to import a module in Python. Here is an example code:
```py
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file
```
Similarly we can install other modules and look into their documentations for usage instructions.<br>
We will find ourselves doing this often in the later part of this course.

<br>

# Day 4 - Our First Program

Today we will write our first ever python program from scratch. It will consist of a bunch of print statements. **print** can be used to print something on the console in python.

## Quick Quiz

Write a program to print a poem in Python. Choose the poem of your choice.
```py
print("---Your poem here---")
```
Please make sure you attempt this. Might be easy for some of you but please finish each and every task.

<br>

# Day 5 - Comments, Escape sequence & Print in Python

Welcome to Day 5 of 100DaysOfCode. Today we will talk about Comments, Escape Sequences and little bit more about print statement in Python. We will also throw some light on Escape Sequences.

## Python Comments

A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

## Single-Line Comments:

To write a comment just add a ‘**#**’ at the start of the line.

### Example 1
```py
#This is a 'Single-Line Comment'
print("This is a print statement.")
```
Output:
```
This is a print statement.
```
### Example 2
```py
print("Hello World !!!") #Printing Hello World
```
Output:
```
Hello World !!!
```
Example 3:
```py
print("Python Program")
#print("Python Program")
```
Output:
```
Python Program
```
## Multi-Line Comments:

To write multi-line comments you can use ‘**#**’ at each line or you can use the **multiline string**.

### Example 1: The use of ‘#’.
```py
#It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
Output:
```
p is greater than 5.
```
### Example 2: The use of multiline string.
```py
"""This is an if-else statement.
It will execute a block of code if a specified condition is true.
If the condition is false then it will execute another block of code."""
p = 7
if (p > 5):
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```
Output
```
p is greater than 5.
```
## Escape Sequence Characters

To insert characters that cannot be directly used in a string, we use an escape sequence character.<br>
An escape sequence character is a backslash ```\``` followed by the character you want to insert.

An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:
```py
print("This doesn't "execute")
print("This will \" execute")
```

## More on Print statement

The syntax of a print statement looks something like this:
```py
print(object(s), sep=separator, end=end, file=file, flush=flush)
```
### Other Parameters of Print Statement

1. **object(s):** Any object, and as many as you like. Will be converted to string before printed.
2. **sep='separator':** Specify how to separate the objects, if there is more than one. Default is ' '.
3. **end='end':** Specify what to print at the end. Default is '\n' (line feed).
4. **file:** An object with a write method. Default is sys.stdout.<br>

**Parameters 2 to 4 are optional**.

<br>

# Day 6 - Variables and Data Types

## What is a variable?

Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
```py
a = 1
b = True
c = "Harry"
d = None
```
These are four variables of different data types.

## What is a Data Type?

Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.<br>
In python, we can print the type of any operator using **type** function:
```py
a = 1
print(type(a))
b = "1"
print(type(b))
```
By default, python provides the following built-in data types:

### 1. Numeric data: int, float, complex
- **int**: 3, -8, 0
- **float**: 7.349, -9.0, 0.0000001
- **complex**: 6 + 2i

### 2. Text data: str
- **str**: "Hello World!!!", "Python Programming"

### 3. Boolean data:
- Boolean data consists of values True or False.

### 4. Sequenced data: list, tuple
- **list**: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:
```py
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
```
Output:
```
[8, 2.3, [-4, 5], ['apple', 'banana']]
```
- **Tuple**: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

Example:
```py
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
```
Output:
```
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
```
### 5. Mapped data: dict

- **dict**: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

Example:
```py
dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
```
Output:
```
{'name': 'Sakshi', 'age': 20, 'canVote': True}
```