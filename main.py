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
