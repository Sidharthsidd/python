"""list comprehensions are a unique way of quickly creating a list with python.
if you find yourself using a for loop along with .append() to create a list,list comprehensions are a good alternative!
to do this lets go to a jupyter notebook"""

mystring='hello'
mylist=[]
for letter in mystring:
    mylist.append(letter)
print(mylist)

#list comprehensions

#syntax
#[ expression for item in iterable  ]
mystring=[letter for letter in mystring]

mylist=[x for x in range(0,11)]
print(mylist)

mylist=[x**2 for x in range(0,11)]
print(mylist)

mylistr=[x for x in range (0,11) if x%2==0]  # for even numbers here
print(mylist)

#by list comprehensions
celcius =[0,10,20,34,5]
fahrenheit=[((9/5)*temp+32) for temp in celcius]
print(fahrenheit)

results=[x if x%2==0 else 'odd' for x in range(0,10)]
print(results)
   # without list comprehensions
mylist=[]
for x in [2,4,6]:
    for y in [0,2,100]:
        mylist.append(y)
print(mylist)


# with list comprehensions
mylist=[x*y for x in [2,3,4,5]  for y in [100,200,300,400] ]
print(mylist)
