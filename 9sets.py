"""sets ae unordered collections of unique elements 
meaning there can only be one representative of the saame object.
lets see some examples!
you cant have a character more than one time"""

myset=set()
print(myset)
myset.add(1)
print(myset)
myset.add(2)
print(myset)
#if i want to add another items with same it give the error 
myset.add(2)
print(myset)

#it looks like set as print the values in ordered but  sets does not have an orderd
mylist=[1,3,3,9,9,3,3,3,3,2,2,2,1,1,1,1,4,4,4]
print(set(mylist))

