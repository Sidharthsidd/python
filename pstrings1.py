#string and indexing 

my_string = "Hello World!"
print(my_string[-8]) 
# Access the first character ('H')

#slicing of a string 

mystring3='abcdefghijk'
print(mystring3[3:])  #start and go to the last of the string by appliing colon
print(mystring3[:3]) #start from the leaving first 3 letter 
print(mystring3[3:6]) #start from 3 and end for 6 
print(mystring3[::4]) #step size jump 2  letter means a even number 
print(mystring3[::-1]) #reverse and for print from last to first 





#string properties and methods 

#immutability
name="sam"
#name[0]='p' #cant do like this beacause strings a immutable
#use string concatenation for changing any string  
last_letters=name[1:]   #goes from 1 index to last and stores in the new string
lastletter='P'+last_letters
print(lastletter)

#multiple string concatination 
x='hello world'
x=x.upper()                   #convert string into upper case 
print(x)
x=x.lower()                   #convert string into lowercase 
print(x)
x=x.split()
print(x)                      # convert into a list by spliting  
x='hi this is a string'
print(x.split("i"))           #removes the i and separates the string 


#string formatting for printing 

my_name="jose"
print("hello"+my_name)

# there are two methods to string formatting those are 
#.format()
#f -string 


""".format method  syntax
string here {}then also {} '.format()('something1','something2')"""

#example

print('this is a string {}'.format('inserted'))
#string are inseerted in index positions

print ('the {} {} {}'.format('fox','brown','quick'))

#if i want the quick in the first of the string than specify the index possition in the curly braces 

print('the {2} {1} {0}'.format('fox','brown','quick'))

#one more method is to specify a key in the braces
print('the {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

#floating point  method 
result =100/777
print(result)
print("the result was {r}".format(r=result))

#floating formatting "{value:width.precision f}"  to display the value of floating point 
print("the result was{r:1.3f}".format(r=result))

#to skip the .format method use the f string leterals just specify the  f in before the string 
name='jose'
age=3
print(f'hello,his name is {name}')
#als0 works on multiple variables 
print(f'{name}  is {age} years old')