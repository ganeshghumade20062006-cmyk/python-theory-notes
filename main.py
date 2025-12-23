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
# Typecasting in python

# The conversion of one data type into the other data type is known as type casting in python or type conversion in python.

# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

# Two Types of Typecasting:
# Explicit Conversion (Explicit type casting in python)
# Implicit Conversion (Implicit type casting in python).
# Explicit typecasting:
# The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion.

# It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc .

# Example of explicit typecasting:
string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)

# Output:
# The Sum of both the numbers is 22

# Implicit type casting:

# Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. Some of the data types have higher-order, and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. According to the level, one data type is converted into other by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

# Python converts a smaller data type to a higher data type to prevent data loss.

# Example of implicit type casting:
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

# Ouput:
# <class 'int'>
# <class 'float'>
# 10.0
# <class 'float'>


a="1"
b='2'
print( a + b )
# output=12
# the output of above code is 12 not 3

a="ganesh "
b="ghumade" 
print(a+b)
# output=the output of above code is ganesh ghumade like adding the number

a=1
b=2
# output=the soulton of above code is 3
print(a+b)
print("or")
a=1
b=2
print(int (a) + int(b))
print("the solutin of above code is 3")
c=1.9
d=8
print(c+d)
print("the solution of above code is 9.9")
print("the above solution called implicit typecasting")
print("the system add 1  and 8 noot adding 0.9 in answer")
1
2
3
4
5
#..........
#  Taking User Input in python
# In python, we can take user input directly by using input() function.This input function gives a return value as string/character hence we have to pass that into a variable
# Syntax:
variable=input()
a=input("Enter the name: ")
print(a)
# Output:
# Enter the name: Ganesh
# Ganesh



a=input ()
print(a)
# output:
# whhen the value of a is ganesh then the output ia ganesh



b= input()
print("my name is", b)
# output:
# b=Ganesh
# my name is ganesh 

c=input("enter your name: ")
print("my name is", c)
# output:
# vaishhali 
#  my name is vaishhal 

x=input ("enter first number: ")
y=("enter second number: ")
print(x + y)
# ("if x=12 and y=100 then te output  is 12100")
# then to write in proper way or do additon then follow this steps ↓

x=input ("enter first number: ")
y=("enter second number: ")
print("if x=12 and y=100 ↓ ")
print (int(x) + int(y))
# output=112

a=input("enter your name :")
print(a)
# enter your name :yash 
# yash
1
2
3
4
5
# ..........
# What are strings?
# In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.

# Example
name = "Ganesh"
print("Hello, " + name)
# Output
# Hello, Ganesh
# Note: It does not matter whether you enclose your strings in single or double quotes, the output remains the same.

# Sometimes, the user might need to put quotation marks in between the strings. Example, consider the sentence: He said, “I want to eat an apple”.

# How will you print this statement in python?: He said, "I want to eat an apple". We will definitely use single quotes for our convenience

print('He said, "I want to eat an apple".')

apple = "he said, \"I want to eat an apple"
print(apple)
# he said, "I want to eat an apple

1.
name="ganesh"
friend="yash"
sister="gauri"


print("hello," + name)
print("hello + friend")
print("hello + sisiter")
# hello,ganesh
# hello + friend
# hello + sisiter
2.
apple = "he said, \"I want to eat an apple"
print(apple)
# he said, "I want to eat an apple

# Multiline Strings
# If our string has multiple lines, we can create them like this:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.
1.
banana = """"he said,
hii ganesh
i am good
"i want go to study""" 
print(banana)
# "he said,
# hii ganesh
# i am good
# "i want go to study


# Accessing Characters of a String
# In Python, string is like an array of characters. We can access parts of string by using its index which starts from 0.
# Square brackets can be used to access elements of the string.

print(name[0])
print(name[1])
# Looping through the string
# We can loop through strings using a for loop like this:

for character in name:
    print(character)
# Above code prints all the characters in the string name one by one!

name = "GANESH"
print(name[0])
print(name[1])
for character in name:
    print(character)
# G
# A
# G
# A
# N
# E
# S
# H
# H

1.
ga="ganesh"
print(ga[0])
print(ga[1])
print(ga[2])
print(ga[3])
print(ga[4])
print(ga[5])
# note= in ganesh letter there are 6 letter but in pythone g=0 a=1 n=3......
# the ans is ↓
# g
# a
# n
# e
# s
# h
# if i print ga[6] then these is error because in ganesh there is nno 6th name
print("the easy way to write these sequence is ")
for character in ga:
    print(character)
# the ans is also same

# g
# a
# n
# e
# s
# h
# for example 

st=""""hey ia am ganesh,
wahat is your name,
hii my name is gauri"
i am fine"""
for character in st:
    print(character)
    # the ans is ↓
# h
# e
# y

# i
# a

# a
# m

# g
# a
# n
# e
# s
# h
# ,


# w
# a
# h
# a
# t

# i
# s

# y
# o
# u
# r

# n
# a
# m
# e
# ,


# h
# i
# i

# m
# y

# n
# a
# m
# e

# i
# s

# g
# a
# u
# r
# i
# "


# i

# a
# m

# f
# i
# n
# e
1
2
3
4
5
# ..........

