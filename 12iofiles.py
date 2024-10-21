#Files

""" how to perform simple i/o with basic.txt files we ll also discuss file paths on your  computer lets get started
"""
myfile=open('13file.txt')
# if you are getting an error no such file  or directory find then t can be two errors 
# you mayy have typed the wrong file name or you  didnt provide a correct file path


myfile1=myfile.read()     # read from the file we use a read() fuction to retrive the 
                           #data from the file and save too a new variable
print(myfile1)           #to print the myfile data

#if i try to read this file again it prints space this happens because you can imagine that there is a cursor at the beginning after reading to sets to the end so to bring again to the beginnnig we use seek() function
myfile.seek(0)   
#you have to reset it every time if you want  to read file again 
myfile1=myfile.read()
print(myfile1)

myfile.seek(0) 
myfile1=myfile.readlines()   
 #to read a the data lines wise 
print(myfile1)

with open('13file.txt') as my_new_file:      
     # this method closes the cursor starting from the end when reading the file again 
    filedata=my_new_file.read()
print(filedata)


#reading and writing   a file as we read a afile we can write a  file also 

with open('13file.txt',mode='r') as myfile:    
      #to set a file only in one mode read write or append we use r,w,a
    contents =myfile.read()

#lets see the append mode
with open('13file.txt',mode='a') as file:
    file.write('this is forth line ')               
       # this sets cursor to the end of the file data  and append the string 

# if i run the file once again it gives the updated data from the file
with open('13file.txt',mode='r') as myfile:     
    contents =myfile.read()
print(contents)
