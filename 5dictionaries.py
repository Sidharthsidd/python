"""dictionaries are the unordered mappings for storing objects.previously we saw how lists store objects in an ordered sequence,dictionaries use a key value pairing instead
this key value pair allows users to quickly grab objects without needing to know an index location
"""
# syntax:   {'key':'value1},{'key2':'value2'}
#so when to choose a list and when to choose a dictionary
#dictionary is unordered and can not be sorted when you want to grab a value without its location and by the key value than use dictionaries




my_dict={'key1':'value1','key2':'value2','key3':'value3'}
# so retrive the vlaue in the dictionary 
mydic_value=my_dict['key2']
print(mydic_value)

prices_lookup={'apple':200,'orange':100,'milk':20}
price=prices_lookup['apple']
print(price)

#dictionary can have a list of values
d={'k1':123,'k2':[1,2,3,4],'k3':{'insideKey':100,'insidekey2':'a'}}
d1=d['k3']['insideKey']       # to grab a key inside a list value as another dictionary
d1=d['k2'][1]
print(d1)
d2=d['k3']['insidekey2'].upper()
print(d2)

#can be add or assign a value to a key 
d['k3']=5000
print(d)

#to grab all the keys 

print(d.keys())

#to grab the only values of the keys 
print(d.values())
# to grab the all keys and values from the dictionaries
print(d.items())
