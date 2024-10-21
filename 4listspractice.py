"""
Exercise 1: Reverse a list in Python
Exercise 2: Turn every item of a list into its square
Exercise 3: Concatenate two lists in the following order
Exercise 4: Iterate both lists simultaneously
Exercise 5: Remove empty strings from the list of strings
Exercise 6: Add new item to list after a specified item
Exercise 7: Extend nested list by adding the sublist
Exercise 8: Replace list’s item with new value if found
Exercise 9: Remove all occurrences of a specific item from a list.
"""

#Exercise 1: Reverse a list in Python
list1=[1,7,4,3,5,9]
list1.reverse()
print(list1)

#2method 
def reverse_string(s):
    reversed_str=''
    for char in s :
        reversed_str=char+reversed_str
    return reversed_str
my_string='hello,world!'
reversed_string =reverse_string(my_string)
print(reversed_string)

#Exercise 2:Turn every item of a list into its square
list2=[1,2,3,4,5,6,7]
new_list=[]
for i in list2:
    new_list.append(i*i)
print(new_list)

#Exercise 3: Concatenate two lists in the following order
#list1 = ["Hello ", "take "]
#list2 = ["Dear", "Sir"]
# output  ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
new_list1=[]
for i in list1:
    for j in list2:
        new_list1.append(i+j)
print(new_list1)

#Exercise 4: Iterate both lists simultaneously
list11=[100,200,300,400,500]
list22=[10,20,30,40,50,60]
for i  in list11,list22:
    print(i)
    
#Remove empty strings from the list of strings
"""list1=['string1','string2','','string3','','string4']
list2=[]
for i in list1:
    if i =='':
        i+1
    else:
        list2=i
print(list2)"""

#Exercise 6: Add new item to list after a specified item
list1=['string1','string2','string3','string4']
list1.append('string5')
print(list1)


#Exercise 7: Extend nested list by adding the sublist
list1=["string1",'string2','string3','string4','string5']





#Exercise 8: Replace list’s item with new value if found
