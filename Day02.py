 #Looping Through a String
'''
Since strings are arrays,
 we can loop through the characters in a string, with a for loop.
'''

for x in "fruit":
  print(x)

for x in "banana":
  print(x, end="")

for x in "banana":
  print(x)
  
  

#Check String
'''To check if a certain phrase or character is present
 in a string, we can use the keyword in.'''

txt = "The best things in life are free!"
print("free" in txt)


txt = "The best things in life are free!"
print("expensive" not in txt)


'''Use it in an if statement:'''

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
  
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")
  
  

#An escape character is a backslash \ that allows you 
to use double quotes when you normally would not be allowed
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 


txt = "We are the so-called 'Vikings' from the north."
print(txt) 

txt = 'We are the so-called "Vikings" from the north.'
print(txt)
--------------------------------seven.py---------------------------------

Strings functions
------------------
'''
The upper() method returns the string in upper case.
The lower() method returns the string in lower case.
The swapcase()	Swaps cases, lower case becomes upper case and vice versa
The strip() method removes any whitespace from the beginning or the end.
The replace() method replaces a string with another string.
The split() method returns a list where the text between the specified separator becomes the list items.
'''

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))


#count() : method returns the number of times
 a specified value appears in the string.

txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple"))
print(txt.count("apple", 15, 24))

 #string.count(value, start, end)



#find()
'''
The find() method finds 
the first occurrence of the specified value.
It returns -1 if the value is not found.
It is almost the same as the index() method, the only difference is that 
the index() method raises an exception if the value is not found. 
'''

txt = "Hello, welcome to my world."

print(txt.find("e"))
print(txt.find("e", 5, 10))
print(txt.find("welcome"))
print(txt.find("Hi"))

------------------------------------eight.py-----------------------------------------
#join()
#The join() method takes all items in an iterable 
and joins them into one string.

myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)
 

#When using a dictionary as an iterable, the returned values are the keys, not the values.
myDict = {"name": "Mala", "country": "Sri Lanka"}
x = "#".join(myDict)
print(x)



#format()
'''
we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them,
 and places them in the string where the placeholders {} are.
''' 

age = 25
height=160
txt = "Age is {}. Height is {}"
print(txt.format(age,height))


'''
You can use index numbers {0} to be sure the arguments are placed
 in the correct placeholders
'''

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


#translate()
'''
The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
Use the maketrans() method to create a mapping table.
If a character is not specified in the dictionary/table, the character will not be replaced.
If you use a dictionary, you must use ascii codes instead of characters.

Syntax: string.translate(table)
table: Either a dictionary, or a mapping table describing how to perform the replace
'''

#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


#Use a mapping table to replace "S" with "P"
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))


#Use a mapping table to replace many characters
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))


#The third parameter in the mapping table describes characters 
 that you want to remove from the string:
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))




#maketrans()
'''
The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.

Syntax
string.maketrans(x, y, z)
Parameter Values

Parameter |	Description
----------|------------------------------------------------------------------------------------------------------------------------------------------------------
x		  |	Required. If only one par ameter is specified, this has to be a dictionary describing how to perform the replace.
 If two or more parameters are specified, this parameter has to be a string specifying the characters you want to replace.
y		  |	Optional. A string with the same length as parameter x. 
Each character in the first parameter will be replaced with the corresponding character in this string.
z		  |	Optional. A string describing which characters to remove from the original string.

'''

--------------------------------------nine.py----------------------------------------------
#User Input: input()
--------------------
a=input()
print(a)

a=input("Enter username:")
print(a)

#Function

def my_function():
  print("Hello from a function")

my_function()


#Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")
 

#Arbitrary Arguments, *args
'''
If you do not know how many arguments
 that will be passed into your function,
 add a * before the parameter name in the function definition.
'''
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


#Keyword Arguments : 
'''
You can also send arguments with the key = value syntax.
This way the order of the arguments does not matter.
'''

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


#Arbitrary Keyword Arguments, **kwargs
'''
If you do not know how many keyword arguments
 that will be passed into your function, 
add two asterisk: ** before the parameter name in the function definition.

'''
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


#Default Parameter Value
  
def my_function(country = "Sri Lanka"):
  print("I am from " + country)

my_function("India")
my_function()


#Return Values

def my_function(x):
  return 5 * x


------------------ten.py--------------------------------------------------
#List,Tuple,Set,Dictionary
--------------------------
'''
used to store multiple items(collections of data) in a single variable.

ordered : the items have a defined order (has index)
changeable:  we can change, add, and remove items in a list after it has been created.
allow duplicate:  list can contain multiple same values
 

List,tuple,set,Dictionary Length: len()
 
 A list,tuple,set and Dictionary can contain different data types : 
["abc", 34, True, 40, "male"]
 
 list() constructor is used to create a new list
	list(("apple", "banana", "cherry")) # note the double round-brackets
 
 tuple() Constructor, set() constructor also be like list() constructor.
'''

#List
#List items are ordered, changeable, and allow duplicate values.
List=[1,2,3,4,5]
print(List)


#Tuple :ordered and unchangeable. Allows duplicate members
Tuple=(1,2,3,4,5)
print(Tuple)


#Set :unordered(unindexed) and unchangeable. No duplicate members
Set={1,2,3,4,5}
print(Set)


#Dictionary: ordered* and changeable.
 No duplicate members (cannot have two items with the same key)

Dictionary={"a":1,"b":2,"c":3,"d":4,"e":5}
print(Dictionary)


 ####Constructors###

#List constructor
a=list(("apple", "banana", "cherry"))   
print(a)

#Tuple constructor
a=tuple(("apple", "banana", "cherry"))   
print(a)

#Set constructor
a=set(("apple", "banana", "cherry"))   
print(a)


#Dictionary constructor

a=dict(x=7,y=4)    
print(a)

a=dict([('x',7),('y',4)])
print(a)

a=dict([('x',7),('y',4)],z=11)
print(a)

a=dict(zip(['x','y','z',],[7,4,11]))
print(a)
 