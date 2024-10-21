"""tuples are very simila to lists however they have one diffrence - immutability

one an element is inside a tuple,it can not be reassigned
tuples use parent (1,2,3)"""

#cheak a type of a list AND TYPE 
a=(2,34,5,5,6,6)
b=[1,2,3,4]
print(type(a))
print(type(a))

#can be have a string in a tuple 
t=('one',2)
print(t[0])
print(t[-1])          #element present in a positon of -1 in a tuple
t=('a','a','b')
print(t.count('a'))  #to count  a string 'a' present in a tuple 
print(t.index('a'))  # to find a position of string 'a'
t[0]='new'
print(t)   #it throughs a error that tuple obect does not support item assignment