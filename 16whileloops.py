"""syntax of a while loop
while some_boolean_condition:
    #do something

else:
    #do something diffrent """

x=0
while x<5:
    print(f'the current value of x is {x}')
    x+=1                 # if you forget the line code the while loops runs to infinety because it does not increment x value automatically
else:
    print('x is not less than 5')

#break ,continue ,and pass key words
x=[1,2,3,4,5]
for item in x :
    pass   #do nothing at all  just pass 

print('end of my script')

mystring='prateek'
for letter in mystring:
    if letter =='a':
        continue      #  goes to the top of the closet enclosing loop
    print(letter)

x=0
while x<5:
    if x==2:      #to break loop when 2 appears
        break
    print(x)
    x+=1
