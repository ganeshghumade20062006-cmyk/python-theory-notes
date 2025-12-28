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
# String Slicing & Operations on String
# Length of a String
# We can find the length of a string using len() function.

# Example:
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
# Output:
# Mango is a 5 letter word.


# String as an array
# A string is essentially a sequence of characters also called an array. Thus we can access the elements of this array.

# Example:
pie = "ApplePie"
print(pie[:5])
print(pie[6])	#returns character at specified index
# Output:
# Apple
# i
# Note: This method of specifying the start and end index to specify a part of a string is called slicing.

1.
names="ganesh, ghumade"
print(names[0:6])
# note= pythone treats variable or spling as a 0 first 
# means here name= ganesh so g=0 a=1 n=2 e=3 s4 h=5
#the last number minus(-) 1 
# means here [0:6] last number is 6  then minus 1 [6-1=5]
# means five word count including 0
# output of above code is= ganesh
# 
print("take it anoother exampe ")
name="ghumade, ganesh"
print(name[0:7])
# the output of above code is ghumade
print(name[0:5])
#  the output of above code is ghuma

2.
names="ganesh, ghumade"
print(len(names))
# output=15 [here counting starts from 0 and also consider cuma(,) and paragraphs ]


fruit = "mango"
len1 = len(fruit)
print("mango is a", len1, "letter word.")
# output of above code= mango is a 5 letter word.

# Slicing Example:
# pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index
# Output:
# Apple
# Pie
# pleP
# ApplePie
# Loop through a String:
# Strings are arrays and arrays are iterable. Thus we can loop through strings.

# Example:
alphabets = "ABCDE"
for i in alphabets:
    print(i)
# Output:
# A
# B
# C
# D
# E

1.
fruits="mango"
print(fruits[0:4])
# output= mang
print(fruits[1:4])
# output = ang 
# output is ang beacuase he letter "mango" start from [1:4] a and end with g
# [1:4]👉🏻starting with 1 end with 3 (n-1) (n=4) [4-1=3]
# 0=m 1=a 2=n 3=g 4=o 
print(fruits[:5])
# 👆🏻 here 0 is not written but pythone automatically written 0  in code or output
# then the output of above code is mango


print(fruits[0:-3])
# here total number in letter mango is 5 
# [0:-3]= 5 (-3)=2 ==== [0:2] 👉🏻 n-1 [0::1]
# output of above code is ma 
print("or 👆🏻")
print(fruits[0:len(fruits)-3])
# the output is ma

print(fruits[-3:-1])
# the solution of above is 
# [-3:-1] (5-3=2) (5-1=4  main[2:4]===but n-1= 3) so variabe statrs from 2 and end in 3
# the solution od above code= ng 
nm="harry"
print(nm[-4:-2])

nm="harry"
print(nm[-4:-2])
# [1:3]
# [1:2]
# ar output of above code 
1
2
3
4
5
# ..........
# String methods
# day 13 is littel bit more 
# so  it converts in type

# Python provides a set of built-in methods that we can use to alter and modify the strings.

# 1.upper() :
# The upper() method converts a string to upper case.

# Example:
str1 = "AbcDEfghIJ"
print(str1.upper())
# Output:
# ABCDEFGHIJ

1.
# type 1 upper (letter become capital) lower (letters become small)

a="Ganesh"
print(len(a))
print(a.upper())
# output= GANESH

print(a.lower()) 
# output=ganesh

# 2.lower()
# The lower() method converts a string to lower case.

# Example:
str1 = "AbcDEfghIJ"
print(str1.lower())
# Output:
# abcdefghij

# 3.strip() :
# The strip() method removes any white spaces before and after the string.

# Example:
str2 = " Silver Spoon "
print(str2.strip)
# Output:
# Silver Spoon

# 4.rstrip() :
# the rstrip() removes any trailing characters. Example:

str3 = "Hello !!!"
print(str3.rstrip("!"))
# Output:
# Hello

# type 2 rstrip (?)

b="!!!!!Ganesh!!!!!!!"
print(b.rstrip("!"))
# output !!!!!Ganesh

# 4.replace() :
# The replace() method replaces all occurences of a string with another string. Example:

str2 = "Silver Spoon"
print(str2.replace("Sp", "M"))
# Output:
# Silver Moon

# type 4 replace (replace word)
c="ganesh ghumade"
print(c.replace("ganesh ", "vaishali "))
# output = vaishali ghumade
g="ganeshh ganesh ghumade ganeshh"
print(g.replace("ganesh", "harshall"))
# output= harshallh harshall ghumade harshallh

# 5.split() :
# The split() method splits the given string at the specified instance and returns the separated strings as list items.

# Example:
str2 = "Silver Spoon"
print(str2.split(" "))      #Splits the string at the whitespace " ".
# Output:
# ['Silver', 'Spoon']
# There are various other string methods that we can use to modify our strings.


# type 5 split (split the word)

g="ganeshh ganesh ghumade ganeshh"
print(g.split(" "))
# output= ['ganeshh', 'ganesh', 'ghumade', 'ganeshh']


# 6.capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.

# Example:
str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)
# Output:
# Hello
# Hello world

# type 6 capitalize (letter capital 1st one )

h="introduction to pythone"
print(h.capitalize())
# output= Introduction to pythone
bloghead="introduction to c"
print(bloghead.capitalize())
# output= Introduction to c

bloghead="introDucTion to c"
print(bloghead.capitalize())
# output= Introduction to c


7.
# center() :
# The center() method aligns the string to the center as per the parameters given by the user.

# Example:
str1 = "Welcome to the Console!!!"
print(str1.center(50))
# Output:
#             Welcome to the Console!!!
# We can also provide padding character. It will fill the rest of the fill characters provided by the user.

# Example:
# str1 = "Welcome to the Console!!!"
# print(str1.center(50, "."))
# Output:
# ............Welcome to the Console!!!.............

# type 7 centre (centre space)

str1 = "welcome to home !!!!!"
print(str1. center(25))
# output=   welcome to home !!!!!
str2 = "welcome to home !!!!!"
print(str2. center(50))
# output=               welcome to home !!!!!
print(len(str2))
# output= 21

bb = "ganesh" , "ganesh", "mooreshwar", "ghumade"
print(bb.count("ganesh"))
# output= 2
gg= "ghumade", "mooreshwr", "vaishali", "vaishali", "vaishali", "vaishali"
print(gg.count("vaishali"))
# 4 output
gg= "ghumade", "mooreshwr", "vaishali", "vaishali", "vaishali", "vaishali"
print(gg.count("vaishalii"))
# output= 0


# 8.count() :
# The count() method returns the number of times the given value has occurred within the given string.

# Example:
str2 = "Abracadabra"
countStr = str2.count("a")
print(countStr)
# Output:
# 4


# 9.endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False.

# Example :
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
# Output:
# True
# We can even also check for a value in-between the string by providing start and end index positions.

# Example:
str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))
# Output:
# True

# type 9     endswith (identify endswith that leter in tht word)
# if word end with that letter then it is true otherwise false


jj="welcome to the homes !!!"
print(jj.endswith("!!!"))
# output = true
jj="welcome to the homes !!!"
print(jj.endswith("."))
# output = false 
str1="welcome to the consol !!!"
print(str1.endswith("to", 4, 10))
# output = true 
str1="welcome to the consol !!!"
print(str1.endswith("to", 4, 10))
# output= true
str2="welcome to the consol !!!"
print(str2.endswith("to", 4, 8))
# output= false 

# 10.find() :
# The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

# Example:
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
# Output:
# 10
# As we can see, this method is somewhat similar to the index() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# Example:
str1 = "He's name is Dan. He is an honest man."
print(str1.find("Daniel"))
# Output:
# -1

# type 10 find (fins the word)

dd="he's name is ganesh. He is an honest man."
print(dd.find("is"))
# here the output is the length of the number which is to find out 
# if the number is not exist at find out then output is -1

dd="he's name is ganesh. He is an honest man."
print(dd.find("iss"))
# output= -1

# 11.index() :
# The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.

# Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))
# Output:
# 13
# As we can see, this method is somewhat similar to the find() method. The major difference being that index() raises an exception if value is absent whereas find() does not.

# Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Daniel"))
# Output:
# ValueError: substring not found


# 12.isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

# Example 1:
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# Output:
True

# type 12 isalnum (if word consist A-Z, a-z, 0-9) then output is true
ii="WelcomeToTheConsole"
print(ii.isalnum())
# output= true

# 13.isalpha() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

# Example :
str1 = "Welcome"
print(str1.isalpha())
# Output:
# True

# type 13 isalpha (if word consist of A-Z, a-z) then then output is true
# any number is come at this then it show false  
ll="welcome"
print(ll.isalpha())
# output= true
ll="welcome11"
print(ll.isalpha())
# output= false 

# 14.islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.

# Example:
str1 = "hello world"
print(str1.islower())
# Output:
# True

# type 14 islower (the character is in string is lower case then it is true other wise false)
oo="hellow world"
print(oo.islower())
# output= true
kk="Ganesh ghumade"
print(kk.islower())
# output= false

# 15.isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

# Example :
str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
# Output:
# True

# type 15 isprintable (if all value are in string are printible then it show true )
# if not then output is false
uu="we wish you a ganesh"
print(uu.isprintable())
# output= true
u="we wish you a ganesh\n"
print(u.isprintable())
# \n is not the printible example 👇🏻
i="ganesh\nghumade"
print(i)
# output=ganesh
#        ghumade
# that's why the output of lline nummber 493 and 494 iis false

# 16.isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.

# Example:
str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())
# Output:
True
True

# type 16 isspace (the method return true and only if the string contains white spaces, else return false)

tt="       "  
print(tt.isspace())
# output= true 
t="  "  
print(t.isspace())
# output= true

# 17.istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

# Example:
str1 = "World Health Organization" 
print(str1.istitle())
# Output:
True
# Example:
str2 = "To kill a Mocking bird"
print(str2.istitle())
# Output:
False

# type 17 istitle (the first letter of each word of the string is capital then it iis true otherwie false)
mm="Ganesh Moreshwar Ghumade"
print(mm.istitle())
# output = true
m="ganesh Moreshwar Ghumade"
print(m.istitle())
# output= false



# 18.isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.

# Example :
str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())
# Output:
True

# type 18 isupper (all character in string is in upper case then it is true otherwise false )
tl="GANESH GHUMADE"
print(tl.isupper())
# output= true
tll="GANESH GHUMaDE"
print(tll.isupper())
# output= false

# 19.startswith() :
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

# Example :
str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))
# Output:
True

# type 19 startswith (this method check if the string starts with a given valu)
oio="pythone is good coding language"
print(oio.startswith("pythone"))
# output= true
opo="pythone is good coding language"
print(opo.startswith("pythone."))
# output= false

# 20.swapcase() :
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

# Example:
str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
# Output:
# pYTHON IS A iNTERPRETED lANGUAGE


# type 20 swapcase (this method change the string into upper case to loower case and lower caseto upper case)
w="Hii my name is ganeshh"
print(w.swapcase())
# output= hII MY NAME IS GANESHH


# 21.title() :
# The title() method capitalizes each letter of the word within the string.

# Example:
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())
# Output:
# He'S Name Is Dan. Dan Is An Honest Man.

# type  21 title ( in this mehode capital each letter of the word within the string)
y="He's name is ganeshh. Ganeshh is a good"
print(y.title())
# output= He'S Name Is Ganeshh. Ganeshh Is A Good
1
2
3
4
5
# ...........
# if-else Statements

# Working of an elif statement
# Execute the block of code inside if statement if the initial expression evaluates to True. After execution return to the code out of the if block.

# Execute the block of code inside the first elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

# Execute the block of code inside the second elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.
# .
# .
# .
# Execute the block of code inside the nth elif statement if the expression inside it evaluates True. After execution return to the code out of the if block.

# Execute the block of code inside else statement if none of the expression evaluates to True. After execution return to the code out of the if block.


# Sometimes the programmer needs to check the evaluation of certain expression(s), whether the expression(s) evaluate to True or False. If the expression evaluates to False, then the program execution follows a different path than it would have if the expression had evaluated to True.

# Based on this, the conditional statements are further classified into following types:

# if
# if-else
# if-else-elif
# nested if-else-elif.
# An if……else statement evaluates like this:
# if the expression evaluates True:
# Execute the block of code inside if statement. After execution return to the code out of the if……else block.\

# if the expression evaluates False:
# Execute the block of code inside else statement. After execution return to the code out of the if……else block.

# 1st example of if-else statement

a= int(input("enter your age:"))
print("your age is:",a)
if(a>18):
    print("you can drive")

else:
    print("you cannot drive")  

#output= enter your age:20
# your age is: 20
# you can drive  
a= int(input("enter your age:"))
print("your age is:",a)
if(a>18):
    print("you can drive")

else:
    print("you cannot drive") 

# output= enter your age:15
# your age is: 15
# you cannot drive

# note= conditional operator
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
# == (equal to)
# != (not equal to)

# print(a>18)
# print(a<18)
# print(a>=18)
# print(a<=18)
# print(a==18)
# print(a!=18)

# 2nd example of if-else statement

applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

# Output:
# Alexa, do not add Apples to the cart.

# 3rd example of if-else statement

applePrice=10
budget=200
if(budget-applePrice>50):
    print("alexa add 1 kg apple to the cart")
elif(budget-applePrice>70):  
    print("its ookk you can buy ")  
else: 
    print("alexa do not add apple to the cart")
    
# # output= alexa add 1 kg apple to the cart


applePrice=10
budget=200
if(budget-applePrice>70):
    print("alexa add 1 kg apple to the cart")
elif(budget-applePrice>50):  
    print("its ookk you can buy ")  
else: 
    print("alexa do not add apple to the cart")

# output= alexa add 1 kg apple to the cart


# 4th example of if-else statement

num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
    print("i am happy")  


# # output= enter the value of num: 7
# the number is positive
# i am happy



num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
    print("i am happy")  


 # output=enter the value of num: -8
# the number is negative
   

num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
    print("i am happy")  


#  output= enter the value of num: 0
# the number is zero

num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
    print("i am happy")  

# output= enter the value of num: 999
# the number is special 


#if 10th line of my statement of string num (print("i am happy")) is in else, elif and if string or command  
# if i write this line sepreate means not line of else then every outout it show i am happy


num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
print("i am happy") 


# # output= enter the value of num: 7
# the number is positive
# i am happy



num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
print("i am happy")   


 # output=enter the value of num: -8
# the number is negative
# i am happy   

num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
print("i am happy")     


#  output= enter the value of num: 0
# the number is zero
# i am happy

num= int(input("enter the value of num: "))
if(num<0):
    print("the number is negative")
elif(num==0):
    print("the number is zero")
elif(num==999):
    print("the number is special ")
else:
    print("the number is positive")
print("i am happy")     

# output= enter the value of num: 999
# the number is special 
# i am happy





# Nested if statements
# We can use if, if-else, elif statements inside other if statements as well.
# Example:

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

# Output:

# Number is between 11-20
# ..........

