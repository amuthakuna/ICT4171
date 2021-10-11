"""
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

"""

"""
myDict = {"name": "Mala", "country": "Sri Lanka"}
x = "#".join(myDict)
print(x)

"""

"""
age = 25
height=160
txt = "Age is {0}. Height is {1}"
print(txt.format(age,height))
"""

"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
"""

"""
txt = "Hello Sam!"
mydict = {83:  80}
print(txt.translate(mydict))
"""

"""
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
"""

"""
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))

"""

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))





























