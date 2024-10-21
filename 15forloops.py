""" th term iterable means you can iterate over the object
for example  you can iterate over every character in a astring .iterate over evry item in a list iterate over every key in a adictionary.
syntax of a for loop
my_iterable =[1,2,3,4]
for item_name in my_iterable:
    print(item_name)

>>1
>>2
>>3        output.

"""
my_list=[1,2,3,4,5,6,7]
for i in my_list:              #i can me named any thing here
    print(i)

for num in my_list:
    #check for evem
    if num %2==0:
        print(num)
    else:
        print(f"odd number:{num}")


list_sum=0
for num in my_list:
    list_sum+=num
print(list_sum)         #gives the sum of the numbers

# you can iterate the string also

list_string='hello wrold!'
for i in list_string:
    print(i,end="")

#tuples unpacking
my_list=[(1,2),(3,4),(5,6),(7,8),(8,9)]

for a,b in my_list:
    print(a)                   
    print(b)

#same can be done to dictionary 