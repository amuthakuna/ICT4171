Creating a Comment
-------------------
Comments starts with a #, and Python will ignore them

#Single comment

"""
This is multi line comment
written in
more than just one line
"""

'''
This is multi line comment
written in
more than just one line
''' 


Print
------
print("Hello, World!")
print("Hello\nWorld")

#Multiline Strings
#You can assign a multiline string to a variable by using three quotes(double/single quotes)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



Variable Names
---------------
'''
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
'''

Creating Variables
------------------
#Variables do not need to be declared with any particular type, and can even change type after they have been set.
#Variable names are case-sensitive. [a=10, A="Hi"]

x = 10
y = "Priya"		#String variables can be declared either by using single or double quotes
print(x)
print("Name is ",y) 
print("Name is "+y) 


x = 5
y = 10
print(x + y)	#return summation
print(x , y)


Get the Type
------------
#You can get the data type of a variable with the type() function.

y = 'John'
z=1.5
print(type(x))
print(type(y))
print(type(z))


Casting
-------
#If you want to specify the data type of a variable, this can be done with casting.

x=10		  # x will be 10

y = str(x)    # y will be '10'    
z = float(x)  # z will be 10.0

print(x)
print(y)
print(z)



#Python allows you to assign values to multiple variables in one line
x, y, z = 10,20,30 # x=10, y=20, z = 30 wrong

print(x)
print(y)
print(z)


#assign the same value to multiple variables in one line
x = y = z = 10

print(x)
print(y)
print(z)



#If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)




Python Numbers
--------------
'''
There are three numeric types in Python:

int6
float
complex
'''
x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = 35e3	#"e" to indicate the power of 10


Random Number
-------------
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers

import random

print(random.randrange(1, 10))


import random as r

print(r.randrange(10, 100))




Booleans (True or False)
---------

#The bool() function allows you to evaluate any value
print(bool(5>1))
print(bool(5<1))
print(bool("Hello"))


'''
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
'''


#true
print(bool("Hello"))
print(bool(15))
bool(["apple", "cherry", "banana"])

#false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})



isinstance()
------------
#Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type

x = 200
print(isinstance(x, int))

--------------------------


#the floor division // rounds the result down to the nearest whole number

x=11/3
print(x)

x=11//3
print(x)




If condition
-------------

a = 10
b = 20

if b > a:
	print("b is greater than a")a=
elif a == b:
	print("a and b are equal")
else:
	print("a is less than b")
	
	

if b > a: print("b is greater than a")
elif a == b: print("a and b are equal")
else: print("a is less than b")



#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line

print("b is greater than a") if b > a else print("a is less than b")


a = 30
b = 30

print(b) if b > a else print("=") if a == b else print(a)


#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  
  
Nested If
---------

#You can have if statements inside if statements, this is called nested if statements.


g = "female"
a=30

if g is "female":
  if g > 20:
    print("Female above 20")
  else:
    print("Female not above 20.")
else:
	print("Male not above 20.")
	
	
if g == "female":
  if g > 20:
    print("Female above 20")
  else:
    print("Female not above 20.")
else:
	print("Male not above 20.")
	
	
	
if (g == "female"):
    print("Female", end="")
    if a > 20:
        print("above 20")
    else:
        print("Female not above 20.")
else:
    print("Male not above 20.")
	
	

Loops
-----

#while loop

i = 1
while i <= 5:
  print(i)
  i += 1
  
  
#break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#pass
i = 1
while i < 6:
  if i == 3:
    pass
  else:
    print(i)
  i += 1
  
  
#continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)



#for loop
'''
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
'''

#range() Function
'''
To loop through a set of code a specified number of times, we can use the range() function,
The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6),
which means values from 2 to 6 (but not including 6).

The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3).
'''

for x in range(6):
  print(x)
  

for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)
  
  
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
 
#Looping Through a String
for x in "banana":
  print(x)
  
 
#Else in For Loop

for x in range(6):
  print(x)
else:
  print("Finally finished!")
 
 
#Note: The else block will NOT be executed if the loop is stopped by a break statement.
 
 for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


#Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)




				Strings
----------------------------------------

#Strings are Arrays
'''
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
'''

a = "Hello, World!"
print(a[1])


#Looping Through a String
'''
Since strings are arrays, we can loop through the characters in a string, with a for loop.
'''

for x in "banana":
  print(x)



#String Length
'''To get the length of a string, use the len() function.'''

a = "Hello, World!"
print(len(a))


Slicing Strings
---------------
'''
Y ou can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
'''
#Note: The first character has index 0.

b = "Hello, World!"
print(b[2:5]) 	#Get the characters from position 2 to position 5 (not included):
print(b[:5]) 	#Slice From the Start
print(b[2:])	#Slice To the End


'''Negative Indexing'''
#Use negative indexes to start the slice from the end of the string

print(b[-5:-2])
