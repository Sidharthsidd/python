"""lists are ordered  sequences that can hold a variety of objectt types 
they use [] brackets and commas to separate objects in the list [1,2,3,4,5]
lists support indexing and sliceing .list can be nested and also hae a variety  of useful methods that can be called of them """






my_list =[1,2,3,4,5]
my_list=['string',100,2,3,2]  
print(my_list)               #can be a multiple datatype 
len_list=len(my_list)     #to print a len of the list
print(len_list)
my_list2=['one','two','three']
print (my_list[0])   #indexing of  a list 
print(my_list[1:])
# concatenation of a list 
another_list=['four','five','six']
new_list=my_list2+another_list
print(new_list)

#to hcange the value in list  from index example
another_list[0]='one all caps'
print(another_list)

#append method for the appending the value to the list 
another_list.append("seven")    # allows you to append at the end of the list 
print(another_list)
#to remove the  value from the end of the list 

another_list.pop()
print(another_list)

#  to diplay popped item 
popped_item=another_list.pop()
print(popped_item)

#to remove from the index position from the list 
another_list.pop(1)
print(another_list)

new_list=['a','e','x','b']
new_list.sort()          # sort function to sort a give list 
print(new_list)

my_sorted_list=new_list.sort()   #this returns nonetyoe  actually this does nt return anything to sign the value 
type(my_sorted_list)

#if you want to sign a value of sorted 
#list you have to sign it separately for example 

new_list.sort()
my_sorted_list=new_list
print(my_sorted_list)

num_list=[1,3,4,2,5]
num_list.sort()
print(num_list)


#to reverse a list 
num_list.reverse()
print(num_list)

#nested dictionaries 

neslist=[[1,2,3,],[4,5,6],[7,8,9]]
print(neslist[1])  # output[4,5,6]
print(neslist[1][2])  #ouput[6]


neslist2 = [[2,3,6,[4,8,24,67],6],4]   
print(neslist2[0][3])
