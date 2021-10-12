'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
'''


'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
'''
'''
newlist = [x for x in range(10)]
print(newlist)
'''

'''
newlist = [x for x in range(10) if x < 5]
print(newlist)
'''
'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

'''

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

'''

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
'''

'''
TwoD=[[1,2,3],[4,5,6]]
print(TwoD)
print(TwoD[0])
print(TwoD[0][1])
'''

















