# TABLE OF CONTENTS

|Day|Topic|
|---|---|
|01|[What is Programming and Python?](#day-1---what-is-programming-and-python)|
|02|[Why I love python (And you will too...)](#day-2---why-i-love-python-and-you-will-too)|
|03|[Modules and pip in Python!](#day-3---modules-and-pip-in-python)|
|04|[Our First Program](#day-4---our-first-program)|
|5|[Comments, Escape sequence & Print in Python](#day-5---comments-escape-sequence--print-in-python)|
|6|[Variables and Data Types](#day-6---variables-and-data-types)|
|7|[Exercise 1: Calculator using Python](#day-07---exercise-1-calculator-using-python)|
|8|[Typecasting in python](#day-08---typecasting-in-python)|
|9|[Taking User Input in python](#day-09---taking-user-input-in-python)|
|10|[Strings](#day-10---strings)|
|11|[String Slicing & Operations on String](#day-11---string-slicing--operations-on-string)|
|12|[String methods](#day-12---string-methods)|
|13|[If Else Conditionals](#day-13---if-else-conditionals)|
|14|[Excersice 2: Good Morning Sir](#day-14---excersice-2-good-morning-sir)|
|15|[Match Case Statements](#day-15---match-case-statements)|
|16|[Introduction to Loops](#day-16---introduction-to-loops)|
|17|[Python while Loop](#day-17---python-while-loop)|
|18|[break and continue](#day-18---break-and-continue)|
|19|[Python Functions](#day-19---python-functions)|
|20|[Function Arguments and return statement](#day-20---function-arguments-and-return-statement)|
|21|[Introduction to Lists](#day-21---introduction-to-lists)|
|22|[List Methods](#day-22---list-methods)|
|23|[Introduction to Tuples](#day-23---introduction-to-tuples)|
|24|[Operations on Tuples](#day-24---operations-on-tuples)|
|25|[Exercise 3 : Kaun Banega Crorepati](#day-25---exercise-3--kaun-banega-crorepati)|
|26|[f strings](#day-26---f-strings)|
|27|[Docstrings](#day-27---docstrings)|
|28|[Recursion in python](#day-28---recursion-in-python)|
|29|[Python Sets](#day-29---python-sets)|
|30|[Set Methods in Python](#day-30---set-methods-in-python)|
|31|[Python Dictionaries](#day-31---python-dictionaries)|
|32|[Dictionary Methods](#day-32---dictionary-methods)|
|33|[Python: **else** in Loop](#day-33---python-else-in-loop)|
|34|[Exception Handling](#day-34---exception-handling)|
|35|[Finally keyword](#day-35---finally-keyword)|
|36|[Custom Errors](#day-36---custom-errors)|
|37|[Exercise 4 : Secret Code Language](#day-37---exercise-4--secret-code-language)|
|38|[Short Hand if else](#day-38---short-hand-if-else)|
|39|[Enumerate](#day-39---enumerate)|
|40|[Virtual Environment](#day-40---virtual-environment)|
|41|[How import works](#day-41---how-import-works)|
|42|[```if "__name__ == "__main__"``` in Python](#day-42---if-__name__--__main__-in-python)|
|43|[```os``` Module in Python](#day-43---os-module-in-python)|
|44|[local vs global variables](#day-44---local-vs-global-variables)|
|45|[File IO in Python](#day-45---file-io-in-python)|
|46|[](#day46)|
|47|[](#day47)|
|48|[](#day48)|
|49|[](#day49)|
|50|[](#day50)|
|51|[](#day51)|
|52|[](#day52)|
|53|[](#day53)|
|54|[](#day54)|
|55|[](#day55)|
|56|[](#day56)|
|57|[](#day57)|
|58|[](#day58)|
|59|[](#day59)|
|60|[](#day60)|
|61|[](#day61)|
|62|[](#day62)|
|63|[](#day63)|
|64|[](#day64)|
|65|[](#day65)|
|66|[](#day66)|
|67|[](#day67)|
|68|[](#day68)|
|69|[](#day69)|
|70|[](#day70)|
|71|[](#day71)|
|72|[](#day72)|
|73|[](#day73)|
|74|[](#day74)|
|75|[](#day75)|
|76|[](#day76)|
|77|[](#day77)|
|78|[](#day78)|
|79|[](#day79)|
|80|[](#day80)|
|81|[](#day81)|
|82|[](#day82)|




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

[**Jump to Index**](#table-of-contents)

<br>

# Day 2 - Why I love python (And you will too...)

## What can Python do for you?

I want to show you some python programs which will surely inspire you to create your own versions of the same as we progress through this tutorial. Do not try to recreate them just yet if you are a beginner and just started working on Python. We will make progress gradually trust me. [Link](https://github.com/Aman1337g/Python-notes-and-codes/tree/main/Projects)

[**Jump to Index**](#table-of-contents)

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

[**Jump to Index**](#table-of-contents)

<br>

# Day 4 - Our First Program

Today we will write our first ever python program from scratch. It will consist of a bunch of print statements. **print** can be used to print something on the console in python.

## Quick Quiz

Write a program to print a poem in Python. Choose the poem of your choice.
```py
print("---Your poem here---")
```
Please make sure you attempt this. Might be easy for some of you but please finish each and every task.

[**Jump to Index**](#table-of-contents)

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

[**Jump to Index**](#table-of-contents)

<br>

# Day 6 - Variables and Data Types

## What is a variable?

Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
```py
a = 1
b = True
c = "Aman"
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

[**Jump to Index**](#table-of-contents)

<br>

# Day 07 - Exercise 1: Calculator using Python

## Operators

Python has different types of operators for different operations. To create a calculator we require arithmetic operators.

## Arithmetic operators
Operator|Operator Name|Example
|--|--|--|
+|Addition|15+7
-|Subtraction|15-7
*|Multiplication|	5*7
**|Exponential|5**3
/|Division|5/3
%|Modulus|15%7
//|Floor Division|15//7

### Exercise
```py
n = 15
m = 7
ans1 = n+m
print("Addition of",n,"and",m,"is", ans1)
ans2 = n-m
print("Subtraction of",n,"and",m,"is", ans2)
ans3 = n*m
print("Multiplication of",n,"and",m,"is", ans3)
ans4 = n/m
print("Division of",n,"and",m,"is", ans4)
ans5 = n%m
print("Modulus of",n,"and",m,"is", ans5)
ans6 = n//m
print("Floor Division of",n,"and",m,"is", ans6)
```
### Explaination
Here 'n' and 'm' are two variables in which the integer value is being stored. Variables 'ans1' , 'ans2' ,'ans3', 'ans4','ans5' and 'ans6' contains the outputs corresponding to addition, subtraction,multiplication, division, modulus and floor division respectively.

### Exercise 1 - Create a Calculator
Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!<br>
Do it and create a pull request with your name and add the codes into **Exercise 1** folder.

 [**Jump to Index**](#table-of-contents)

<br>

# Day 08 - Typecasting in python

The conversion of one data type into the other data type is known as **type casting** in python or **type conversion** in python.

Python supports a wide variety of functions or methods like: **int()**, **float()**, **str()**, **ord()**, **hex()**, **oct()**, **tuple()**, **set()**, **list()**, **dict()**, etc. for the type casting in python.

## Two Types of Typecasting:

1. Explicit Conversion (Explicit type casting in python)
2. Implicit Conversion (Implicit type casting in python).

### Explicit typecasting:

The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

### Example of explicit typecasting:
```py
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)
```
Output:
```
The Sum of both the numbers is 22
```

### Implicit type casting:

Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.

### Example of implicit type casting:
```py
# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))
```
Ouput:
```
<class 'int'>
<class 'float'>
10.0
<class 'float'>
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 09 - Taking User Input in python

In python, we can take user input directly by using **input()** function.This input function gives a return value as **string/character** hence we have to pass that into a variable.

## Syntax:
```py
variable=input()
```
But input function returns the value as **string**. Hence we have to typecast them whenever required to another datatype.

### Example: 
```py
variable=int(input())
variable=float(input())
```
We can also display a text using input function. This will make input() function take user input and display a message as well

### Example:
```py
a=input("Enter the name: ")
print(a)
```
Output:
```
Enter the name: Aman Kumar Gupta
Aman Kumar Gupta
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 10 - Strings

## What are strings?

In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

### Example
```py
name = "Aman Kumar Gupta"
print("Hello, " + name)
```
Output
```
Hello, Aman Kumar Gupta
```
> **Note**: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience. Or we can use escape sequence character as we have already studied them.
```py
print('He said, "I want to eat an apple".')
```

## Multiline Strings

If our string has multiple lines, we can create them like this:
```py
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

## Accessing Characters of a String

In Python, string is **like** an array of characters. We can access parts of string by using its index which starts from 0.
Square brackets can be used to access elements of the string.
```py
print(name[0])
print(name[1])
```
## Looping through the string

We can loop through strings using a for loop like this:
```py
for character in name:
    print(character)
```
Above code prints all the characters in the string name one by one!

[**Jump to Index**](#table-of-contents)

<br>

# Day 11 - String Slicing & Operations on String

## Length of a String

We can find the length of a string using **len()** function.

### Example:
```py
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```
Output:
```
Mango is a 5 letter word.
```
## String as an array

A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

### Example:
```py
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index
```
Output:
```
Apple
i
```
> Note: This method of specifying the start and end index to specify a part of a string is called slicing.

### Slicing Example:
```py
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index ( -8 = len(pie)-8 = 8-8 = 0 till full string length )
```
Output:
```
Apple
Pie
pleP
ApplePie
```
## Loop through a String:

Strings are arrays and arrays are iterable. Thus we can loop through strings.

### Example:
```py
alphabets = "ABCDE"
for i in alphabets:
    print(i)
```
Output:
```
A
B
C
D
E
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 12 - String methods

Python provides a set of built-in methods that we can use to alter and modify the strings.

## 1. upper() :
The upper() method converts a string to upper case.

### Example:
```py
str1 = "AbcDEfghIJ"
print(str1.upper())
```
Output:
```
ABCDEFGHIJ
```
## 2. lower()
The lower() method converts a string to lower case.

### Example:
```py
str1 = "AbcDEfghIJ"
print(str1.lower())
```
Output:
```
abcdefghij
```
## 3. strip() :
The strip() method removes any white spaces before and after the string.

### Example:
```py
str2 = " Silver Spoon "
print(str2.strip)
```
Output:
```
Silver Spoon
```
## 4. rstrip() :
The rstrip() removes any trailing characters. 
### Example:
```py
str3 = "Hello !!!"
print(str3.rstrip("!"))
```
Output:
```
Hello
```
## 5. replace() :
The replace() method replaces all occurences of a string with another string. 
### Example:
```py
str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
```
Output:
```
Silver Moon
```
## 6. split() :
The split() method splits the given string at the specified instance and returns the separated strings as list items.
### Example:
```py
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
```
Output:
```
['Silver', 'Spoon']
```
There are various other string methods that we can use to modify our strings.

## 7. capitalize() :
The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
### Example:
```py
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
```
Output:
```
Hello
Hello world
```
## 8. center() :
The center() method aligns the string to the center as per the parameters given by the user.
### Example:
```py
str1 = "Welcome to the Console!!!"
print(str1.center(50))
```
Output:
```
            Welcome to the Console!!!
```
We can also provide padding character. It will fill the rest of the fill characters provided by the user.

### Example:
```py
str1 = "Welcome to the Console!!!"
print(str1.center(50, "."))
```
Output:
```
............Welcome to the Console!!!.............
```
## 9. count() :
The count() method returns the number of times the given value has occurred within the given string.
### Example:
```py
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
```
Output:
```
4
```
## 10. endswith() :
The endswith() method checks if the string ends with a given value. If yes then return True, else return False.
### Example :
```py
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
```
Output:
```
True
```
We can even also check for a value in-between the string by providing start and end index positions.
### Example:
```py
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
```
Output:
```
True
```
## 11. find() :
The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
### Example:
```py
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
```
Output:
```
10
```
As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
### Example:
```py
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))
```
Output:
```
-1
```
## 12. index() :
The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
### Example:
```py
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
```
Output:
```
13
```
As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.
### Example:
```py
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
```
Output:
```
ValueError: substring not found
```
## 13. isalnum() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

### Example 1:
```py
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
```
Output:
```
True
```
## 14. isalpha() :
The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
### Example :
```py
str1 = "Welcome"
print(str1.isalpha())
```
Output:
```
True
```
## 15. islower() :
The islower() method returns True if all the characters in the string are lower case, else it returns False.
### Example:
```py
str1 = "hello world"
print(str1.islower())
```
Output:
```
True
```
## 16. isprintable() :
The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
### Example :
```py
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
```
Output:
```
True
```
## 17. isspace() :
The isspace() method returns True only and only if the string contains white spaces, else returns False.
### Example:
```py
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
Output:
True
True
```
## 18. istitle() :
The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
### Example:
```py
str1 = "World Health Organization" 
print(str1.istitle())
```
Output:
```
True
```
### Example:
```py
str2 = "To kill a Mocking bird"
print(str2.istitle())
```
Output:
```
False
```
## 19. isupper() :
The isupper() method returns True if all the characters in the string are upper case, else it returns False.
### Example :
```py
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
```
Output:
```
True
```
## 20. startswith() :
The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
### Example :
```py
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
```
Output:
```
True
```
## 21. swapcase() :
The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
### Example:
```py
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
```
Output:
```
pYTHON IS A iNTERPRETED lANGUAGE
```
## 22. title() :
The title() method capitalizes each letter of the word within the string.
### Example:
```py
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
```
Output:
```
He'S Name Is Dan. Dan Is An Honest Man.
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 13 - If Else Conditionals

## if-else Statements
Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

Based on this, the conditional statements are further classified into following types:
- if
- if-else
- if-else-elif
- nested if-else-elif.

### An if……else statement evaluates like this:

#### if the expression evaluates True:
Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

#### if the expression evaluates False:
Execute the block of code inside else statement. After execution return to the code out of the if……else block.

Example:
```py
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```
Output:
```
Alexa, do not add Apples to the cart.
```

## elif Statements
Sometimes, the programmer may want to evaluate more than one condition, this can be done using an elif statement.

### Working of an elif statement
Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
.
.
.
Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.

Example:
```py
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")
```
Output:
```
Number is Zero.
```

## Nested if statements
We can use if, if-else, elif statements inside other if statements as well.

Example:
```py
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```
Output:
```
Number is between 11-20
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 14 - Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
```py
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime
```
Likewise Exercise 1, create a pull request with your answers as [ **your_name.py** ] to Exercise 2 folder.😄

[**Jump to Index**](#table-of-contents)

<br>

# Day 15 - Match Case Statements
To implement switch-case like characteristics very similar to if-else functionality, we use a match case in python. If you are coming from a C, C++ or Java like language, you must have heard of switch-case statements. If this is your first language, don't worry as I will tell you everything you need to know about match case statements.

A match statement will compare a given variable’s value to different shapes, also referred to as the pattern. The main idea is to keep on comparing the variable with all the present patterns until it fits into one.

The match case consists of three main entities :

1. The match keyword
2. One or more case clauses
3. Expression for each case

The case clause consists of a pattern to be matched to the variable, a condition to be evaluated if the pattern matches, and a set of statements to be executed if the pattern matches.

## Syntax:
```py
match variable_name:
            case ‘pattern1’ : //statement1
            case ‘pattern2’ : //statement2
            …            
            case ‘pattern n’ : //statement n
```
### Example:
```py
x = 4
# x is the variable to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
```
Output:
```
x % 2 == 0 and case is 4
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 16 - Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loop.Based on this loops are further classified into following main types;

- for loop
- while loop

## The for Loop

for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

### Example: iterating over a string:
```py
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```
Output:
```
A, b, h, i, s, h, e, k,
```

### Example: iterating over a list:
```py
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```
Output:
```
Red
Green
Blue
Yellow
```
Similarly, we can use loops for lists, sets and dictionaries.

### range():
What if we do not want to iterate over a sequence? What if we want to use for loop for a specific number of times?

Here, we can use the range() function.

### Example:
```py
for k in range(5):
    print(k)
```
Output:
```
0
1
2
3
4
```
Here, we can see that the loop *starts from 0 by default* and increments at each iteration.

But we can also loop over a specific range.

### Example:
```py
for k in range(4,9):
    print(k)
```
Output:
```
4
5
6
7
8
```
### Quick Quiz

Explore about third parameter of range (ie range(x, y, z))

[**Jump to Index**](#table-of-contents)

<br>

# Day 17 - Python while Loop

As the name suggests, while loops execute statements while the condition is True. As soon as the condition becomes False, the interpreter comes out of the while loop.

### Example:
```py
count = 5
while (count > 0):
  print(count)
  count = count - 1
```
Output:
```
5
4
3
2
1
```
Here, the count variable is set to 5 which decrements after each iteration. Depending upon the while loop condition, we need to either increment or decrement the counter variable (the variable ```count```, in our case) or the loop will continue forever.

## Else with While Loop
We can even use the else statement with the while loop. Essentially what the else statement does is that as soon as the while loop condition becomes False, the interpreter comes out of the while loop and the else statement is executed.

### Example:
```py
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')
```
Output:
```
5
4
3
2
1
counter is 0
```

## Do-While loop in python
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) and then the repetition of loop's body will depend on the condition passed at the end of the while loop. It is also known as an **exit-controlled** loop.

## How to emulate do-while loop in python?
To create a do-while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do-while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop with a break statement wrapped in an if statement that checks a given condition and breaks the iteration if that condition becomes true:

### Example
```py
while True:
  number = int(input("Enter a positive number: "))
  print(number)
  if not number > 0: # comparsion operator has higher precedence than logical operator
    break
```
Output
```
Enter a positive number: 1
1
Enter a positive number: 4
4
Enter a positive number: -1
-1
```
### Explanation
This loop uses True as its formal condition. This trick turns the loop into an infinite loop. Before the conditional statement, the loop runs all the required processing and updates the breaking condition. If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path.

[**Jump to Index**](#table-of-contents)

<br>

# Day 18 - break and continue

## break statement
The break statement enables a program to skip over a part of the code. A break statement **terminates the very loop it lies within**.

### Example
```py       
for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")
```
Output
```
1 Mississippi
2 Mississippi
3 Mississippi
4 Mississippi
5 Mississippi
.
.
.
50 Thank you
```

## Continue Statement
The continue statement **skips the rest of the loop statements** and causes the next iteration to occur.

### Example
```py
for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)
```
Output
```
2
4
6
8
0
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 19 - Python Functions
A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to create or use existing functions that make the program flow organized and neat.

There are two types of functions:

1. Built-in functions
2. User-defined functions

## Built-in functions:
These functions are defined and pre-coded in python. Some examples of built-in functions are as follows:

**min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print()**, etc.

## User-defined functions:
We can create functions to perform specific tasks as per our needs. Such functions are called user-defined functions.

### Syntax:
```py
def function_name(parameters):
  pass
  # Code and Statements
```
- Create a function using the ```def``` keyword, followed by a **function name**, followed by a **paranthesis** (()) and a **colon**(:).
- Any parameters and arguments should be placed within the parentheses.
- Rules to naming function are similar to that of naming variables.
- Any statements and other code within the function should be indented.

## Calling a function:
We call a function by giving the function name, followed by parameters (if any) in the parenthesis.

### Example:
```py
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
```
Output:
```
Hello, Sam Wilson
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 20 - Function Arguments and return statement
There are four types of arguments that we can provide in a function:

- Default Arguments
- Keyword Arguments
- Variable length Arguments
- Required Arguments

## Default arguments:
We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

### Example:
```py
def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy")
```
Output:
```
Hello, Amy Jhon Whatson
```
## Keyword arguments:
We can provide arguments with **key = value**, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

### Example:
```py
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")
```
Output:
```
Hello, Jade Peter Wesker
```
## Required arguments:
In case we don’t pass the arguments with a **key = value** syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

### Example 1: when number of arguments passed does not match to the actual function definition.
```py
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
```
Output:
```
name("Peter", "Quill")\
TypeError: name() missing 1 required positional argument: 'lname'
```
### Example 2: when number of arguments passed matches to the actual function definition.
```py
def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Ego", "Quill")
```
Output:
```
Hello, Peter Ego Quill
```
## Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

### Arbitrary Arguments:
While creating a function, pass a ```*``` before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.

#### Example:
```py
def name(*name):
    print("Hello,", name[0], name[1], name[2])

name("James", "Buchanan", "Barnes")
```
Output:
```
Hello, James Buchanan Barnes
```
### Keyword Arbitrary Arguments:
While creating a function, pass a ```**``` before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

#### Example:
```py
def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Buchanan", lname = "Barnes", fname = "James")
```
Output:
```
Hello, James Buchanan Barnes
```
## return Statement
The return statement is used to return the value of the expression back to the calling function.

### Example:
```py
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
```
Output:
```
Hello, James Buchanan Barnes
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 21 - Introduction to Lists

## Python Lists
- Lists are ordered collection of data items.
- They store multiple items in a single variable.
- List items are separated by commas and enclosed within square brackets [].
- Lists are changeable meaning we can alter them after creation.

### Example 1:
```py
lst1 = [1,2,2,3,5,4,6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)
```
Output:
```
[1, 2, 2, 3, 5, 4, 6]
['Red', 'Green', 'Blue']
```
### Example 2:
```py
details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)
```
Output:
```
['Abhijeet', 18, 'FYBScIT', 9.8]
```
> As we can see, a single list can contain items of different data types.

## List Index
Each item/element in a list has its own unique index. This index can be used to access any particular item from the list. The first item has index [0], second item has index [1], third item has index [2] and so on.

### Example:
```py
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
```
## Accessing list items
We can access list items by using its index with the square bracket syntax []. For example colors[0] will give "Red", colors[1] will give "Green" and so on...

### Positive Indexing:
As we have seen that list items have index, as such we can access items using these indexes.

### Example:
```py
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [0]      [1]     [2]      [3]      [4]
print(colors[2])
print(colors[4])
print(colors[0])
```
Output:
```
Blue
Green
Red
```
### Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the list. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

### Example:
```py
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
#          [-5]    [-4]    [-3]     [-2]      [-1]
print(colors[-1])
print(colors[-3])
print(colors[-5])
```
Output:
```
Green
Blue
Red
```
### Check whether an item in present in the list?
We can check if a given item is present in the list. This is done using the ```in``` keyword.
```py
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Yellow" in colors:
    print("Yellow is present.")
else:
    print("Yellow is absent.")
```
Output:
```
Yellow is present.
```
```py
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if "Orange" in colors:
    print("Orange is present.")
else:
    print("Orange is absent.")
```
Output:
```
Orange is absent.
```
## Range of Index:
You can print a range of list items by specifying where you want to start, where do you want to end and if you want to skip elements in between the range.

### Syntax:
```py
listName[start : end : jumpIndex]
```
> Note: jump Index is optional. We will see this in later examples.

### Example: printing elements within a particular range:
```py
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	#using positive indexes
print(animals[-7:-2])	#using negative indexes , -7 => len(animals)-7 = 9-7 = 2
```
Output:
```
['mouse', 'pig', 'horse', 'donkey']
['bat', 'mouse', 'pig', 'horse', 'donkey']
```
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.

> Note: The element of the end index provided will not be included.

### Example: printing all element from a given index till the end
```py
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[4:])	#using positive indexes
print(animals[-4:])	#using negative indexes
```
Output:
```
['pig', 'horse', 'donkey', 'goat', 'cow']
['horse', 'donkey', 'goat', 'cow']
```
> When no end index is provided, the interpreter prints all the values till the end.

### Example: printing all elements from start to a given index
```py
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[:6])	#using positive indexes
print(animals[:-3])	#using negative indexes
```
Output:
```
['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
['cat', 'dog', 'bat', 'mouse', 'pig', 'horse']
```
> When no start index is provided, the interpreter prints all the values from start up to the end index provided.

### Example: Printing alternate values
```py
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[::2])		#using positive indexes
print(animals[-8:-1:2])	#using negative indexes
```
Output:
```
['cat', 'bat', 'pig', 'donkey', 'cow']
['dog', 'mouse', 'horse', 'goat']
```
Here, we have not provided start and index, which means all the values will be considered. But as we have provided a jump index of 2, only alternate values will be printed.

### Example: printing every 3rd consecutive value withing a given range
```py
animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])
```
Output:
```
['dog', 'pig', 'goat]
```
Here, jump index is 3. Hence it prints every 3rd element within given index.

## List Comprehension
List comprehensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

### Syntax:
```py
List = [Expression(item) for item in iterable if Condition]
```
- **Expression:** It is the item which is being iterated.
- **Iterable:** It can be list, tuples, dictionaries, sets, and even in arrays and strings.
- **Condition:** Condition checks if the item should be added to the new list or not.

### Example 1: Accepts items with the small letter “o” in the new list
```py
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)
```
Output:
```
['Milo', 'Bruno', 'Rosa']
```
### Example 2: Accepts items which have more than 4 letters
```py
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)
```
Output:
```
['Sarah', 'Bruno', 'Anastasia']
```

[**Jump to Index**](#table-of-contents)
<br>

# Day 22 - List Methods

## list.sort()
This method sorts the list in ascending order. The original list is updated

### Example 1:
```py
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort()
print(num)
```
Output:
```
['blue', 'green', 'indigo', 'voilet']\
[1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
```
> What if you want to print the list in descending order?
We must give **reverse=True** as a parameter in the sort method.

### Example:
```py
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.sort(reverse=True)
print(num)
```
Output:
```
['voilet', 'indigo', 'green', 'blue']
[9, 8, 7, 6, 5, 4, 3, 2, 2, 2, 1, 1]
```
> The reverse parameter is set to False by default.

> Note: Do not mistake the reverse parameter with the reverse method.

## reverse()
This method reverses the order of the list.

### Example:
```py
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4,2,5,3,6,1,2,1,2,8,9,7]
num.reverse()
print(num)
```
Output:
```
['green', 'blue', 'indigo', 'voilet']
[7, 9, 8, 2, 1, 2, 1, 6, 3, 5, 2, 4]
```
## index()
This method returns the index of the first occurrence of the list item.

### Example:
```py
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.index(3))
```
Output:
```
1
3
```
## count()
Returns the count of the number of items with the given value.

Example:
```py
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4,2,5,3,6,1,2,1,3,2,8,9,7]
print(num.count(2))
```
Output:
```
2
3
```
## copy()
Returns copy of the list. This can be done to perform operations on the list without modifying the original list.

### Example:
```py
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
newlist[0] = 1 
print(colors)
print(newlist)
```
Output:
```
['voilet', 'green', 'indigo', 'blue']
[1, 'green', 'indigo', 'blue']
```
## append():
This method appends items to the end of the existing list.

### Example:
```py
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)
```
Output:
```
['voilet', 'indigo', 'blue', 'green']
```
## insert():
This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.

### Example:
```py
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")   #inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)
```
Output:
```
['voilet', 'green', 'indigo', 'blue']
```
## extend():
This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.

### Example 1:
```py
#add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)
print(rainbow)
```
Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
["green", "yellow", "orange", "red"]
```
## Concatenating two lists:
You can simply concatenate two lists to join two lists.

### Example:
```py
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
```
Output:
```
['voilet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 23 - Introduction to Tuples

## Python Tuples
Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are **unchangeable** meaning we can not alter them after creation.

### Example 1:
```PY
tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)
```
Output:
```
(1, 2, 2, 3, 5, 4, 6)
('Red', 'Green', 'Blue')
```
### Example 2:
```py
details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)
```
Output:
```
('Abhijeet', 18, 'FYBScIT', 9.8)
```

## Tuple Indexes
Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on.

### Example:
```py
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]
```
## Accessing tuple items:
### I. Positive Indexing:
As we have seen that tuple items have index, as such we can access items using these indexes.

### Example:
```py
country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]     
print(country[0])
print(country[1])
print(country[2])
```
Output:
```
Spain
Italy
India
```
### II. Negative Indexing:
Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

### Example:
```py
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1]) # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])
```
Output:
```
Germany
India
Italy
```
### III. Check for item:
We can check if a given item is present in the tuple. This is done using the ```in``` keyword.

### Example 1:
```py
country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")
```
Output:
```
Germany is present.
```
### Example 2:
```py
country = ("Spain", "Italy", "India", "England", "Germany")
if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")
```
Output:
```
Russia is absent.
```
### IV. Range of Index:
You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range.

### Syntax:
```py
Tuple[start : end : jumpIndex]
```
> Note: jump Index is optional. We will see this in given examples.

### Example: Printing elements within a particular range:
```py
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes
```
Output:
```
('mouse', 'pig', 'horse', 'donkey')
('bat', 'mouse', 'pig', 'horse', 'donkey')
```
Here, we provide index of the element from where we want to start and the index of the element till which we want to print the values.<br>
> Note: The element of the end index provided will not be included.

### Example: Printing all element from a given index till the end
```py
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[4:])      #using positive indexes
print(animals[-4:])     #using negative indexes
```
Output:
```
('pig', 'horse', 'donkey', 'goat', 'cow')
('horse', 'donkey', 'goat', 'cow')
```
> When no end index is provided, the interpreter prints all the values till the end.

### Example: printing all elements from start to a given index
```py
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[:6])      #using positive indexes
print(animals[:-3])     #using negative indexes
```
Output:
```
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
('cat', 'dog', 'bat', 'mouse', 'pig', 'horse')
```
> When no start index is provided, the interpreter prints all the values from start up to the end index provided.

### Example: Print alternate values
```py
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[::2])     #using positive indexes
print(animals[-8:-1:2]) #using negative indexes
```
Output:
```
('cat', 'bat', 'pig', 'donkey', 'cow')
('dog', 'mouse', 'horse', 'goat')
```
Here, we have not provided start and end index, which means all the values will be considered. But as we have provided a jump index of 2 only alternate values will be printed.

### Example: printing every 3rd consecutive withing given range
```py
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[1:8:3])
```
Output:
```
('dog', 'pig', 'goat')
```
Here, jump index is 3. Hence it prints every 3rd element within given index.

[**Jump to Index**](#table-of-contents)

<br>

# Day 24 - Operations on Tuples

## Manipulating Tuples
Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.

### Example:
```py
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
print(temp)
temp.pop(3)                 #remove item
print(temp)
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)
```
Output:
```
("Spain", "Italy", "India", "England", "Germany", "Russia")
("Spain", "Italy", "India", "Germany", "Russia")
('Spain', 'Italy', 'Finland', 'Germany', 'Russia')
```
Thus, we convert the tuple to a list, manipulate items of the list using list methods, then convert list back to a tuple.

However, we can directly concatenate two tuples without converting them to list.

### Example:
```py
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)
```
Output:
```
('Pakistan', 'Afghanistan', 'Bangladesh', 'ShriLanka', 'Vietnam', 'India', 'China')
```

## Tuple methods
As tuple is immutable type of collection of elements it have limited built in methods.They are explained below

### count() Method
The count() method of Tuple returns the number of times the given element appears in the tuple.

### Syntax:
```py
tuple.count(element)
```
### Example
```py
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)
```
Output
```
Count of 3 in Tuple1 is: 3
```

### index() method
The Index() method returns the first occurrence of the given element from the tuple.

### Syntax:
```py
tuple.index(element, start, end)
```
> Note: This method raises a ValueError if the element is not found in the tuple.

### Example
```py
Tuple = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is at index :', res)
```
Output
```
First occurrence of 3 is at index : 3
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 25 - Exercise 3 : Kaun Banega Crorepati

Create a program capable of displaying questions to the user like KBC(Kaun Banega Crorepati). Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.

Create a pull request in Exercise 3 folder as [ **your_name.py** ] to submit your answers.

<br>

# Day 26 - f strings

## String formatting in python
String formatting can be done in python using the ```format``` method.
```py
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
```
Output:
```
For only 49.00 dollars!
```

## f-strings in python
It is a new string formatting mechanism introduced by the PEP 498. It is also known as **Literal String Interpolation** or more commonly as **F-strings** (f character preceding the string literal). The primary focus of this mechanism is to make the interpolation easier.

When we prefix the string with the letter '**f**', the string becomes the f-string itself. The f-string can be formatted in much same as the ```str.format()``` method. The f-string offers a convenient way to embed Python expression inside string literals for formatting.

### Example
```py
val = 'Geeks'  
print(f"{val}for{val} is a portal for {val}.")  
name = 'Tushar'  
age = 23  
print(f"Hello, My name is {name} and I'm {age} years old.")
```
Output:
```
GeeksforGeeks is a portal for Geeks.
Hello, My name is Tushar and I'm 23 years old.
```
In the above code, we have used the f-string to format the string. It evaluates at runtime; we can put all valid Python expressions in them.

We can use it in a single statement as well.

### Example
```py
print(f"{2 * 30}")
```
Output:
```
60
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 27 - Docstrings

## Docstrings in python
Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
### Example
```py
def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
```
Here,

'''Takes in a number n, returns the square of n''' is a docstring which will not appear in output

Output:
```
25
```
Here is another example:
```PY
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
```
## Python Comments vs Docstrings

### Python Comments
Comments are *descriptions* that help programmers better understand the intent and functionality of the program. They are completely ignored by the Python interpreter.

### Python docstrings
As mentioned above, Python docstrings are *strings* used right after the definition of a function, method, class, or module (like in Example 1). They are used to document our code.

We can access these docstrings using the **doc** attribute.

## Python **doc** attribute
Whenever string literals are present just after the definition of a function, module, class or method, they are associated with the object as their doc attribute. We can later use this attribute to retrieve this docstring.

### Example
```PY
def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)
```
Output:
```
Takes in a number n, returns the square of n
```

# PEP 8
[PEP 8](https://peps.python.org/pep-0008/) is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

PEP stands for **Python Enhancement Proposal**, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

# The Zen of Python
In 1999, Pythoneer [Tim Peters](https://en.wikipedia.org/wiki/Tim_Peters_(software_engineer)) succinctly channels the [BDFL’s](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) guiding principles for Python’s design into 20 aphorisms, only 19 of which have been written down.
```
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```
## Easter egg
```py
import this
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 28 - Recursion in python
Recursion is the process of defining something in terms of itself.

## Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

### Example:
```py
def factorial(num): 
    if (num == 1 or num == 0):
        return 1
    else:
        return (num * factorial(num - 1)) 
  
# Driver Code 
num = 7; 
print("Number: ",num)
print("Factorial: ",factorial(num))
```
Output:
```
number:  7
Factorial:  5040
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 29 - Python Sets
Sets are **unordered collection** of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

### Example:
```py
info = {"Carla", 19, False, 5.9, 19}
print(info)
```
Output:
```
{False, 19, 5.9, 'Carla'}
```
Here we see that the items of set occur in random order and hence they cannot be accessed using index numbers. Also sets **do not allow duplicate values**.

### Quick Quiz: Try to create an empty set. Check using the type() function whether the type of your variable is a set

## Accessing set items:
### Using a For loop
You can access items of set using a for loop.

### Example:
```py
info = {"Carla", 19, False, 5.9}
for item in info:
    print(item)
```
Output:
```
False
Carla
19
5.9
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 30 - Set Methods in Python

## Joining Sets
Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.

### I. union() and update():
The ```union()``` and ```update()``` methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds item into the existing set from another set.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.union(cities2)
print(cities3)
```
Output:
```
{'Tokyo', 'Madrid', 'Kabul', 'Seoul', 'Berlin', 'Delhi'}
```
Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.update(cities2)
print(cities)
```
Output:
```
{'Berlin', 'Madrid', 'Tokyo', 'Delhi', 'Kabul', 'Seoul'}
```

### II. intersection and intersection_update():
The ```intersection()``` and ```intersection_update()``` methods prints only items that are similar to both the sets. The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)
```
Output:
```
{'Madrid', 'Tokyo'}
```
### Example :
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)
```
Output:
```
{'Tokyo', 'Madrid'}
```

### III. symmetric_difference and symmetric_difference_update():
The ```symmetric_difference()``` and ```symmetric_difference_update()``` methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)
```
Output:
```
{'Seoul', 'Kabul', 'Berlin', 'Delhi'}
```
### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)
```
Output:
```
{'Kabul', 'Delhi', 'Berlin', 'Seoul'}
```
### IV. difference() and difference_update():
The ```difference()``` and ```difference_update()``` methods prints only items that are only present in the original set and not in both the sets. The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
```
Output:
```
{'Tokyo', 'Madrid', 'Berlin'}
```
### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
print(cities.difference(cities2))
```
Output:
```
{'Tokyo', 'Berlin', 'Madrid'}
```

There are several in-built methods used for the manipulation of set.They are explained below

### isdisjoint():
The ```isdisjoint()``` method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))
```
Output:
```
False
```

### issuperset():
The ```issuperset()``` method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))
```
Output:
```
False
False
```

### issubset():
The ```issubset()``` method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))
```
Output:
```
True
```

### add()
If you want to add a single item to the set use the ```add()``` method.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)
```
Output:
```
{'Tokyo', 'Helsinki', 'Madrid', 'Berlin', 'Delhi'}
```

### update()
If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the ```update()``` method to add it into the existing set.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)
```
Output:
```
{'Seoul', 'Berlin', 'Delhi', 'Tokyo', 'Warsaw', 'Helsinki', 'Madrid'}
```

### remove()/discard()
We can use ```remove()``` and ```discard()``` methods to remove items form list.

### Example :
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)
```
Output:
```
{'Delhi', 'Berlin', 'Madrid'}
```

The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Seoul")
print(cities)
```
Output:
```
KeyError: 'Seoul'
```

### pop()
This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the ```pop()``` method to a variable.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)
```
Output:
```
{'Tokyo', 'Delhi', 'Berlin'} Madrid
```

### del
```del``` is not a method, rather it is a keyword which deletes the set entirely.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)
```
Output:
```
NameError: name 'cities' is not defined We get an error because our entire set has been deleted and there is no variable called cities which contains a set.
```

What if we don’t want to delete the entire set, we just want to delete all items within that set?

### clear():
This method clears all items in the set and prints an empty set.

### Example:
```py
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)
```
Output:
```
set()
```

### Check if item exists
You can also check if an item exists ```in``` the set or not.

### Example
```py
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
```
Output:
```
Carla is present.
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 31 - Python Dictionaries
Dictionaries are **ordered collection** of data items. They store multiple items in a single variable. Dictionary items are **key-value pairs** that are separated by commas and enclosed within curly brackets {}.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
```
Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
```
## Accessing Dictionary items:
### I. Accessing single values:
Values in a dictionary can be accessed using keys. We can access dictionary values by mentioning **keys either in square brackets** or by using ```get``` method.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['name'])
print(info.get('eligible'))
```
Output:
```
Karan
True
```
### II. Accessing multiple values:
We can print all the values in the dictionary using ```values()``` method.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())
```
Output:
```
dict_values(['Karan', 19, True])
```
### III. Accessing keys:
We can print all the keys in the dictionary using ```keys()``` method.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())
```
Output:
```
dict_keys(['name', 'age', 'eligible'])
```
### IV. Accessing key-value pairs:
We can print all the key-value pairs in the dictionary using ```items()``` method.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())
```
Output:
```
dict_items([('name', 'Karan'), ('age', 19), ('eligible', True)])
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 32 - Dictionary Methods

Dictionary uses several built-in methods for manipulation.They are listed below

## update()
The ```update()``` method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
```
Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
{'name': 'Karan', 'age': 20, 'eligible': True, 'DOB': 2001}
```
## Removing items from dictionary:
There are a few methods that we can use to remove items from dictionary.

## clear():
The ```clear()``` method removes all the items from the list.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
info.clear()
print(info)
```
Output:
```
{}
```
## pop():
The ```pop()``` method removes the key-value pair whose key is passed as a parameter.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True}
info.pop('eligible')
print(info)
```
Output:
```
{'name': 'Karan', 'age': 19}
```
## popitem():
The ```popitem()``` method removes the last key-value pair from the dictionary.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
info.popitem()
print(info)
```
Output:
```
{'name': 'Karan', 'age': 19, 'eligible': True}
```
## del:
we can also use the ```del``` keyword to remove a dictionary item.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info['age']
print(info)
```
Output:
```
{'name': 'Karan', 'eligible': True, 'DOB': 2003}
```
If key is not provided, then the ```del``` keyword will delete the dictionary entirely.

### Example:
```py
info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003}
del info
print(info)
```
Output:
```
NameError: name 'info' is not defined
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 33 - Python: **else** in Loop
As you have learned before, the ```else``` clause is used along with the ```if``` statement.

Python allows the ```else``` keyword to be used with the ```for``` and while ```loops``` too. The ```else``` block appears after the body of the loop. The statements in the ```else``` block will be executed after all iterations are completed. The program exits the loop only after the ```else``` block is executed.

## Syntax
```py
for counter in sequence:
    #Statements inside for loop block
else:
    #Statements inside else block
```
### Example:
```py
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")
```
Output:
```
iteration no 1 in for loop
iteration no 2 in for loop
iteration no 3 in for loop
iteration no 4 in for loop
iteration no 5 in for loop
else block in loop
Out of loop
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 34 - Exception Handling
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to avoid the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

## Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

## Python try...except
```try….. except``` blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

### Syntax:
```py
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception
```
### Example:
```py
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
```
Output:
```
Enter an integer: 6.022
Number entered is not an integer.
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 35 - Finally keyword

## Finally Clause
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The ```finally``` block is always executed, so it is generally used for doing the concluding tasks like **closing file resources** or **closing database connection** or may be **ending the program execution with a delightful message**.

### Syntax:
```py
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation
```
The **finally** block is executed irrespective of the outcome of **try……except…..else** blocks
One of the important use cases of finally block is in a function which returns a value.

### Example:
```py
def fun():
    try:
        num = int(input("Enter an integer: "))
    except ValueError:
        print("Number entered is not an integer.")
        return 1
    else:
        print("Integer Accepted.")
        return 0
    finally:
        print("This block is always executed.")
x = fun()
print(x)
```
Output 1:
```
Enter an integer: 19
Integer Accepted.
This block is always executed.
0
```
Output 2:
```
Enter an integer: aman
Number entered is not an integer.
This block is always executed.
1
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 36 - Custom Errors

## Raising Custom errors
In python, we can raise custom errors by using the ```raise``` keyword.
### Example:
```py
salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")
```
Output 1:
```
Enter salary amount: 3000
```
Output 2:
```
Enter salary amount: 100
Traceback (most recent call last):
  File "c:\Users\ankit\OneDrive\Desktop\GitHub\Python-notes-and-codes\30_Raising-custom-errors-in-Python.py", line 18, in <module>
    raise ValueError("Not a valid salary")
ValueError: Not a valid salary
```
In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

## Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:
```py
class CustomError(Exception):
  # code ...
  pass

try:
  # code ...

except CustomError:
  # code...
```
### Example:
```py
# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
```

Output

If the user input ```input_num``` is greater than 18,
```
Enter a number: 45
Eligible to Vote
```
If the user input ```input_num``` is smaller than 18,
```
Enter a number: 14
Exception occurred: Invalid Age
```
In the above example, we have defined the custom exception ```InvalidAgeException``` by creating a new class that is derived from the built-in ```Exception``` class.

Here, when ```input_num``` is smaller than 18, this code generates an exception.

When an exception occurs, the rest of the code inside the ```try``` block is skipped.

The ```except``` block catches the user-defined ```InvalidAgeException``` exception and statements inside the ```except``` block are executed.

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.

[**Jump to Index**](#table-of-contents)

<br>

# Day 37 - Exercise 4 : Secret Code Language

Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

## Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end else: simply reverse the string

## Decoding:
if the word contains less than 3 characters, reverse it else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

### **Your program should ask whether you want to code or decode**

Create a pull request in Exercise 4 folder as [ **your_name.py** ] to submit your answers.

[**Jump to Index**](#table-of-contents)

<br>

# Day 38 - Short Hand if else

## If ... Else in One Line
There is also a shorthand syntax for the ```if-else``` statement that can be used when the **condition being tested is simple and the code blocks to be executed are short**. Here's an example:
```py
a = 2
b = 330
print("A") if a > b else print("B")
```
Output:
```
B
```
You can also have multiple ```else``` statements on the same line:

### Example
One line if else statement, with 3 conditions:
```py
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
```
Output:
```
=
```
### Another Example
```py
result = value_if_true if condition else value_if_false
```
This syntax is equivalent to the following if-else statement:
```py
if condition:
    result = value_if_true
else:
    result = value_if_false
```

## Conclusion
The shorthand syntax can be a convenient way to write simple ```if-else``` statements, especially when you want to assign a value to a variable based on a condition.
However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, it's best to use the full ```if-else``` syntax.

[**Jump to Index**](#table-of-contents)

<br>

# Day 39 - Enumerate

## Enumerate function in python
The ```enumerate``` function is a built-in function in Python that allows you to loop over a sequence (such as a list, tuple, or string) and get the **index** and **value** of each element **in the sequence** at the same time. Here's a basic example of how it works:
```py
# Loop over a list and print the index and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
The output of this code will be:
```
0 apple
1 banana
2 mango
```
As you can see, the ```enumerate``` function **returns a tuple** containing the index and value of each element in the sequence. You can use the for loop to unpack these tuples and assign them to variables, as shown in the example above.

## Changing the start index
By default, the ```enumerate``` function starts the index at 0, but you can specify a different starting index by passing it as an argument to the ```enumerate``` function:
```py
# Loop over a list and print the index (starting at 1) and value of each element
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```
Output:
```py
1 apple
2 banana
3 mango
```
The ```enumerate``` function is often used when you need to loop over a sequence and perform some action with both the index and value of each element. For example, you might use it to loop over a list of strings and print the index and value of each string in a formatted way:
```py
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index+1}: {fruit}')
```
Output:
```
1: apple
2: banana
3: mango
```
In addition to lists, you can use the enumerate function with any other sequence type in Python, such as tuples and strings. Here's an example with a tuple:
```py
# Loop over a tuple and print the index and value of each element
colors = ('red', 'green', 'blue')
for index, color in enumerate(colors):
    print(index, color)
```
Output:
```
0 red
1 green
2 blue
```
And here's an example with a string:
```py
# Loop over a string and print the index and value of each character
s = 'hello'
for index, c in enumerate(s):
    print(index, c)
```
Output:
```
0 h
1 e
2 l
3 l
4 o
```

[**Jump to Index**](#table-of-contents)

<br>

# Day 40 - Virtual Environment

## Virtual Environment
A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have **conflicting package versions** or **packages that are not compatible with each other**.

To create a virtual environment in Python, you can use the ```venv``` module that comes with Python. Here's an example of how to create a virtual environment and activate it:

### **Install virtualenv**: Once you have the Command Prompt open, you can install the virtualenv package by running the following command:
```py
pip install virtualenv
```
```py
## Create a virtual environment
python -m venv myenv
# or
virtualenv environment_name

# Activate the virtual environment (Linux/macOS)
source myenv/bin/activate

# Activate the virtual environment (Windows)
myenv\Scripts\activate
```
Once the virtual environment is activated, any packages that you install using pip will be installed in the virtual environment, rather than in the global Python environment. This allows you to have a separate set of packages for each project, without affecting the packages installed in the global environment.

To deactivate the virtual environment, you can use the deactivate command:
```py
# Deactivate the virtual environment
deactivate
```
## The "**requirements.txt**" file
In addition to creating and activating a virtual environment, it can be useful to create a **requirements.txt** file that lists the packages and their versions that your project depends on. This file can be used to easily install all the required packages in a new environment.

To create a **requirements.txt** file, you can use the ```pip freeze``` command, which outputs a list of installed packages and their versions. For example:
```py
# Output the list of installed packages and their versions to a file
pip freeze > requirements.txt
```
To install the packages listed in the requirements.txt file, you can use the pip install command with the ``-r`` flag:
```py
# Install the packages listed in the requirements.txt file
pip install -r requirements.txt
```
Using a virtual environment and a **requirements.txt** file can help you manage the dependencies for your Python projects and ensure that your projects are portable and can be easily set up on a new machine.

[**Jump to Index**](#table-of-contents)

<br>

# Day 41 - How import works
## How importing in python works
Importing in Python is the process of loading code from a Python module into the current script. This allows you to use the functions and variables defined in the module in your current script, as well as any additional modules that the imported module may depend on.

To import a module in Python, you use the ```import``` statement followed by the name of the module. For example, to import the math module, which contains a variety of mathematical functions, you would use the following statement:
```py
import math
```
Once a module is imported, you can use any of the functions and variables defined in the module by using the dot notation. For example, to use the ```sqrt``` function from the math module, you would write:
```py
import math

result = math.sqrt(9)
print(result)  # Output: 3.0
```
### ```from``` keyword
You can also import specific functions or variables from a module using the ```from``` keyword. For example, to import only the ```sqrt``` function from the math module, you would write:
```py
from math import sqrt

result = sqrt(9)
print(result)  # Output: 3.0
```
You can also import multiple functions or variables at once by separating them with a comma:
```py
from math import sqrt, pi

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793
```
### importing everything
It's also possible to import all functions and variables from a module using the ```*``` wildcard. However, this is generally not recommended as it can lead to confusion and make it harder to understand where specific functions and variables are coming from.
```py
from math import *

result = sqrt(9)
print(result)  # Output: 3.0

print(pi)  # Output: 3.141592653589793
```
Python also allows you to rename imported modules using the ```as``` keyword. This can be useful if you want to use a shorter or more descriptive name for a module, or if you want to avoid naming conflicts with other modules or variables in your code.

### The "```as```" keyword
```py
import math as m

result = m.sqrt(9)
print(result)  # Output: 3.0

print(m.pi)  # Output: 3.141592653589793
```
### The ```dir``` function
Finally, Python has a built-in function called ```dir``` that you can use to view the names of all the functions and variables defined in a module. This can be helpful for exploring and understanding the contents of a new module.
```py
import math

print(dir(math))
```
This will output a list of all the names defined in the math module, including functions like ```sqrt``` and ```pi```, as well as other variables and constants.

In summary, the import statement in Python allows you to access the functions and variables defined in a module from within your current script. You can import the entire module, specific functions or variables, or use the ```*``` wildcard to import everything. You can also use the ```as``` keyword to rename a module, and the ```dir``` function to view the contents of a module.

[**Jump to Index**](#table-of-contents)

<br>

# Day 42 - ```if "__name__ == "__main__"``` in Python

The ```if __name__ == "__main__"``` idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script.

In Python, the ```__name__``` variable is a built-in variable that is automatically set to the name of the current module. When a Python script is run directly, the ```__name__``` variable is set to the string ```__main__``` When the script is imported as a module into another script, the ```__name__``` variable is set to the name of the module.

Here's an example of how the if ```__name__ == __main__``` idiom can be used:

```py
def main():
    # Code to be run when the script is run directly
    print("Running script directly")
if __name__ == "__main__":
    main()
```
In this example, the main function contains the code that should be run when the script is run directly. The ```if``` statement at the bottom checks whether the ```__name__``` variable is equal to ```__main__```. If it is, the main function is called.

## Why is it useful?
This idiom is useful because it allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script. For example, consider the following script:
```py
def main():
    print("Running script directly")
if __name__ == "__main__":
    main()
```
If you run this script directly, it will output "Running script directly". However, if you import it as a module into another script and call the main function from the imported module, it will not output anything:
```py
import script
script.main()  # Output: "Running script directly"
```
This can be useful if you have code that you want to reuse in multiple scripts, but you only want it to run when the script is run directly and not when it's imported as a module.

## Is it a necessity?
It's important to note that the ```if __name__ == "__main__"``` idiom is not required to run a Python script. You can still run a script without it by simply calling the functions or running the code you want to execute directly. However, the ```if __name__ == "__main__"``` idiom can be a useful tool for organizing and separating code that should be run directly from code that should be imported and used as a module.

In summary, the ```if __name__ == "__main__"``` idiom is a common pattern used in Python scripts to determine whether the script is being run directly or being imported as a module into another script. It allows you to reuse code from a script by importing it as a module into another script, without running the code in the original script.

[**Jump to Index**](#table-of-contents)

<br>

# Day 43 - ```os``` Module in Python

The ```os``` module in Python is a built-in library that provides functions for interacting with the operating system. It allows you to perform a wide variety of tasks, such as reading and writing files, interacting with the file system, and running system commands.

Here are some common tasks you can perform with the ```os``` module:

**Reading and writing files** : The os module provides functions for opening, reading, and writing files. For example, to open a file for reading, you can use the open function:
```py
import os
# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)
# Read the contents of the file
contents = os.read(f, 1024)
# Close the file
os.close(f)
```
To open a file for writing, you can use the ```os.O_WRONLY``` flag:
```py
import os
# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)
# Write to the file
os.write(f, b"Hello, world!")
# Close the file
os.close(f)
```
## Interacting with the file system

The os module also provides functions for interacting with the file system. For example, you can use the ```os.listdir``` function to get a list of the files in a directory:
```py
import os
# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']
```
You can also use the ```os.mkdir``` function to create a new directory:
```py
import os
# Create a new directory
os.mkdir("newdir")
```
## Running system commands

Finally, the ```os``` module provides functions for running system commands. For example, you can use the ```os.system``` function to run a command and get the output:
```py
import os
# Run the "ls" command and print the output
output = os.system("ls")
print(output)  # Output: ['myfile.txt', 'otherfile.txt']
```
You can also use the ```os.popen``` function to run a command and get the output as a file-like object:
```py
import os
# Run the "ls" command and get the output as a file-like object
f = os.popen("ls")
# Read the contents of the output
output = f.read()
print(output)  # Output: ['myfile.txt', 'otherfile.txt']
# Close the file-like object
f.close()
```
In summary, the ```os``` module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system. It allows you to perform tasks such as reading and writing files, interacting with the file system, and running system commands.

[**Jump to Index**](#table-of-contents)

<br>

# Day 44 - local vs global variables

Before we dive into the differences between local and global variables, let's first recall what a variable is in Python.

A variable is a named location in memory that stores a value. In Python, we can assign values to variables using the assignment operator ```=```. For example:
```py
x = 5
y = "Hello, World!"
```
Now, let's talk about local and global variables.

A **local variable** is a variable that is defined within a function and is only accessible within that function. It is created when the function is called and is destroyed when the function returns.

On the other hand, a **global variable** is a variable that is defined outside of a function and is accessible from within any function in your code.

Here's an example to help clarify the difference:
```py
x = 10 # global variable
def my_function():
  y = 5 # local variable
  print(y)
my_function()
print(x) # 10
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
```
In this example, we have a global variable ```x``` and a local variable ```y```. We can access the value of the global variable ```x``` from within the function, but we cannot access the value of the local variable ```y``` outside of the function.

## The ```global``` keyword

Now, what if we want to modify a **global** variable from within a function? This is where the ```global``` keyword comes in.

The ```global``` keyword is used to declare that a variable is a global variable and should be accessed from the global scope. Here's an example:
```py
x = 10 # global variable
def my_function():
  global x
  x = 5 # this will change the value of the global variable x
  y = 5 # local variable
my_function()
print(x) # prints 5
print(y) # this will cause an error because y is a local variable and is not accessible outside of the function
```
In this example, we used the ```global``` keyword to declare that we want to modify the global variable x from within the function. As a result, the value of x is changed to 5.

It's important to note that it's generally considered good practice to avoid modifying global variables from within functions, as it can lead to unexpected behavior and make your code harder to debug.

I hope this tutorial has helped clarify the differences between local and global variables and how to use the ```global``` keyword in Python.

[**Jump to Index**](#table-of-contents)

<br>

# Day 45 - File IO in Python

Python provides several ways to manipulate files. Today, we will discuss how to handle files in Python.

## Opening a File

Before we can perform any operations on a file, we must first open it. Python provides the ```open()``` function to open a file. It takes two arguments: the *name of the file* and the *mode* in which the file should be opened. The mode can be 'r' for reading, 'w' for writing, or 'a' for appending.

Here's an example of how to open a file for reading:
```py
f = open('myfile.txt', 'r')
```
By default, the ```open()``` function returns a file object that can be used to read from or write to the file, depending on the mode.

## Modes in file
There are various modes in which we can open files.

1. **read (r)**: This mode opens the file for reading only and gives an error if the file does not exist. This is the *default mode* if no mode is passed as a parameter.
2. **write (w)**: This mode opens the file for writing only and creates a new file if the file does not exist.
3. **append (a)**: This mode opens the file for appending only and creates a new file if the file does not exist.
4. **create (x)**: This mode creates a file and gives an error if the file already exists.
5. **text (t)**: Apart from these modes we also need to specify how the file must be handled. ```t``` mode is used to handle text files. ```t``` refers to the text mode. There is no difference between ```r``` and ```rt``` or ```w``` and ```wt``` since text mode is the default. The default mode is '```r```' (open for reading text, synonym of 'rt' ).
6. **binary (b)**: used to handle binary files (images, pdfs, etc).

## Reading from a File

Once we have a file object, we can use various methods to read from the file.

The ```read()``` method reads the entire contents of the file and returns it as a string.
```py
f = open('myfile.txt', 'r')
contents = f.read()
print(contents)
```
## Writing to a File
To write to a file, we first need to open it in write mode.
```py
f = open('myfile.txt', 'w')
```
We can then use the ```write()``` method to write to the file.
```py
f = open('myfile.txt', 'w')
f.write('Hello, world!')
```
Keep in mind that writing to a file will overwrite its contents. If you want to append to a file instead of overwriting it, you can open it in append mode.
```py
f = open('myfile.txt', 'a')
f.write('Hello, world!')
```
## Closing a File
It is important to close a file after you are done with it. This releases the resources used by the file and allows other programs to access it.

To close a file, you can use the ```close()``` method.
```py
f = open('myfile.txt', 'r')
# ... do something with the file
f.close()
```
## The 'with' statement
Alternatively, you can use the ```with``` statement to automatically close the file after you are done with it.
```py
with open('myfile.txt', 'r') as f:
    # ... do something with the file
```

[**Jump to Index**](#table-of-contents)

<br>

