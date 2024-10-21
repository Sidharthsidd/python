"""
Exercise 1: Convert two lists into a dictionary
Exercise 2: Merge two Python dictionaries into one
Exercise 3: Print the value of key ‘history’ from the below
Exercise 4: Initialize dictionary with default values
Exercise 5: Create a dictionary by extracting the keys from a given dictionary
Exercise 6: Delete a list of keys from a dictionary
Exercise 7: Check if a value exists in a dictionary
Exercise 8: Rename key of a dictionary
Exercise 9: Get the key of a minimum value from the following dictionary
Exercise 10: Change value of a key in a nested dictionary
Write a Python program to change Brad’s salary to 8500 in the following dictionary"""


#Exercise 1: Convert two lists into a dictionary
n=[1,2,3,4,5]
p=["sasf'f,'sdfs",'sf']
dic=[(n,p) for n,p in zip(n,p)]   #list conprehension methods can be used to convert two list to dic
print(dic)

keys = [1, 2, 3, 4, 5]
values = ["sasf'f,'sdfs", 'sf']
dic = {k: v for k, v in zip(keys, values)}
print(dic)
 


#Exercise 2: Merge two Python dictionaries into one
n={'i1':'v1','i2':'v2'}
p={'k1':'i1','k2':'i2','k3':'i3'}
n.update(p)
print(n)


#Exercise 3: Print the value of key ‘history’ from the below
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict['class']['student']['marks']['history'])    #we can print nested dictionaries values by this method  each [] goes inside the nested { } 

#Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

res = dict.fromkeys(employees, defaults)  # makes the employees values as defaults for dictionaries value 
print(res)

# Individual data
print(res["Kelly"])

#Exercise 5: Create a dictionary by extracting the keys from a given dictionary
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ['name','city']

newDict = {k: sampleDict[k] for k in keys}
print(newDict)

#Exercise 6: Delete a list of keys from a dictionary
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ['name','city']
for i in keys:
    sampleDict.pop(i)
print(sampleDict)




#Exercise 7: Check if a value exists in a dictionary
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

  #solution 
for i in sampleDict:
    if 25 in sampleDict.values():
        print('25 exitsin  sampledict')
        break

#Exercise 8: Rename key of a dictionary   
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}                                           #pop city and rename to location 

sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

#Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
    "name": 78,
    "age": 25,
    "salary": 8000,
    "city": 1000
}  

print(min(sample_dict,key=sample_dict.get))

#Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)