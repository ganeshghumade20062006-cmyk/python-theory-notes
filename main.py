# BASICS OF PYTHON
# My First Program
1
2
3
4
5
print("hello world")
print("ganesh ghumade moreshwar")
print(458*455)
print(455+4588)
print("ganesh ghumde \nmoreshwar \"ghumade\"")
# OUTPUT= ganesh ghumde 
# moreshwar "ghumade"
print("yavatmal", "chanddrapur", sep="~")
# OUTPIT= yavatmal~chanddrapur
print("yavatmal from ganesh ghumade\nand chandrapur is a good city")
# OUTPUT= yavatmal from ganesh ghumade
# and chandrapur is a good city
print("ganesh  ghumade")
a="ganesh ghumade"
b="ghumade ganesh"
c=5656
d="vaishali ghuamde"
print("the type of a is", type(a))
print("the type of b is", type(b))
print("the type of c is", type(c))
print("thr type of d is ", type(d))
# OUTPUT= he type of a is <class 'str'>
# the type of b is <class 'str'>
# the type of c is <class 'int'>
# # thr type of d is  <class 'str'>
print("today is holiday")
1
2
3
4
5
# ..........

# Basic of python
# Today I will write my first ever python program from scratch. It will consist of a bunch of print statements. print can be used to print something on the console in python

print("hello world", 44)
# OUTPUT= hello world 44
print(4)
# OUTPUT= 4
print(455*444)
# OUTPUT= 202020
print(55+62)
# OUTPUT= 117
1
2
3
4
5
# ..........

# Comments, Escape sequence & Print in Python

#  (\n example are as follow)
print("1.st example=hello my name is\nGanesh ghumade\nthis is my sister \"Gauri\"")
print("2nd. example=hello my name is ganesh ghumade\ni am in \"chandrapur\"\nthhis city is also famous for \'tigar living\'\ni am also live in yavatmal")
#1. output= hello my name is
# Ganesh ghumade
# this is my sister "Gauri"

# 2. output= hello my name is ganesh ghumade
# i am in "chandrapur"
# thhis city is also famous for 'tigar living'
# i am also live in yavatmal


# # Single-Line Comments:
# To write a comment just add a ‘#’ at the start of the line

# hello my name is ganesh ghumade 
# hello my name is yash narad 
# hii my name is gauri narad  

# Multi-Line Comments:
# To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

#  1.It will execute a block of code if a specified condition is true.
#If the condition is false then it will execute another block of code.


# 2."""This is an if-else statement.
# It will execute a block of code if a specified condition is true.
# If the condition is false then it will execute another block of code."""



# Escape Sequence Characters


# To insert characters that cannot be directly used in a string, we use an escape sequence character.

# An escape sequence character is a backslash \ followed by the character you want to insert.

# An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

# print("This doesnt "execute")
# print("This will \" execute") 



# More on Print statement
# The syntax of a print statement looks something like this:

# print(object(s), sep=separator, end=end, file=file, flush=flush)

# Other Parameters of Print Statement
# 1.object(s): Any object, and as many as you like. Will be converted to string before printed
# 2.sep='separator': Specify how to separate the objects, if there is more than one. Default is ' '
# 3.end='end': Specify what to print at the end. Default is '\n' (line feed)
# 4.file: An object with a write method. Default is sys.stdout

# Parameters 2 to 4 are optional

# 1.sep=(....)
# example=   1.print("ganesh ghumade", 8308606736, sep="~")
#            OUTPUT= ganesh ghumade~8308606736
# 2.print("lakshmi narad", 8669674135, sep="~")
#            OUTPUT= lakshmi narad~8669674135


# 2. end=(....)

# example 1.=
print("my moobile number is", 8308606736, sep="~", end="458")
# output= my moobile number is~8308606736458
1
2
3
4
5
# ..........

# Variables and Data Types


# What is a variable?
# Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:
a = 1
b = True
c = "Harry"
d = None
# These are four variables of different data types.


# What is a Data Type?
# Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
# In python, we can print the type of any operator using type function:

a = 1
print(type(a))
b = "1"
print(type(b))

# By default, python provides the following built-in data types:
# 1. Numeric data: int, float, complex
# int: 3, -8, 0
# float: 7.349, -9.0, 0.0000001
# complex: 6 + 2i
# 2. Text data: str
# str: "Hello World!!!", "Python Programming"

# 3. Boolean data:
# Boolean data consists of values True or False.

# 4. Sequenced data: list, tuple
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

# example:

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

# Output:

# [8, 2.3, [-4, 5], ['apple', 'banana']]

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

# Example:

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

# Output:

# (('parrot', 'sparrow'), ('Lion', 'Tiger'))

# 5. Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

# Example:

dict1 = {"name":"Harshal", "age":20, "canVote":True}
print(dict1)

# Output:

# {'name': 'Harshal', 'age': 20, 'canVote': True}


# some example of it
a="ganesh ghumade"
b=1556
c="tigar"
d="none"
e="True"
f="false"
print("the type of a is",(a))
# output= the type of a is ganesh ghumade
print("the type of b is", type(b))
# outut= the type of b is <class 'int'>
print("the type of c is", type (c))
# output= the type of c is <class 'str'>
print("the type of d is", type(d))
# output= the type of d is <class 'str'>
print("the type of e is", type(e))
# output= the type of e is <class 'str'>
print("the type of f is", type(f))
# output= the type of f is <class 'str'>
s=complex(45,5)
# output= the type of s is <class 'complex'>
print("the type of s is", type(s))
# output= the type of s is <class 'complex'>
1
2
3
4
5
#..........

