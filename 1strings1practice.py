"""
Exercise 1A: Create a string made of the first, middle and last character
Exercise 1B: Create a string made of the middle three characters
Exercise 2: Append new string in the middle of a given string
Exercise 3: Create a new string made of the first, middle, and last characters of each input string
Exercise 4: Arrange string characters such that lowercase letters should come first
Exercise 5: Count all letters, digits, and special symbols from a given string
Exercise 6: Create a mixed String using the following rules
Exercise 7: String characters balance Test
Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Exercise 9: Calculate the sum and average of the digits present in a string
Exercise 10: Write a program to count occurrences of all characters within a string
Exercise 11: Reverse a given string
Exercise 12: Find the last position of a given substring
Exercise 13: Split a string on hyphens
Exercise 14: Remove empty strings from a list of strings
Exercise 15: Removal all characters from a string except integers
Exercise 16: Find words with both alphabets and numbers
Exercise 17: Replace each special symbol with # in the following string
"""


#Exercise 1A: Create a string made of the first, middle and last character
"""
str1=input('enter the string')
firstLetter=str1[0]
lent=len(str1)
l=int (lent/2)
middletter=str1[l]
res=firstLetter+middletter
res=res+str1[l-1]
print(res)
"""


#======================================================================================================


#Exercise 1B: Create a string made of the middle three characters
"""
str2=input('enter the string to printing middle three characters')
l=len(str2)
middle=int(l/2)
middle2=str2[middle]
middle1=str2[middle-1]
middle3=str2[middle+1]
print('this is the string middle characters {mstr1}{mstr2}{mstr3}'.format(mstr1=middle1,mstr2=middle2,mstr3=middle3))
"""


#======================================================================================================


#Exercise 2: Append new string in the middle of a given string
"""
str1=input('enter the first string \n')
str2=input('enter the number to put in the middle of the string\n')
str1mid=len(str1)
str1mid=int (str1mid/2)
str1strt=str1[:str1mid]
str1last=str1[str1mid:]
new_string=str1strt+str2+str1last
print(str1strt+str2+str1last)
"""

#======================================================================================================


#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
"""
str1=input('enter the first string :')
str2=input('second string:')
str1strt=str1[0]+str2[0]
l1=len(str1)
str1mid=int (l1/2)
str1mid=str1[str1mid]
l2=len(str1)
str2mid=int (l2/2)
str2mid=str2[str2mid]
str2midd=str1mid+str2mid
str1last=str1[l1-1]
str2last=str2[l2-1]
strlaststrg=str1last+str2last
new_string=str1strt+str2midd+strlaststrg
print(new_string)
"""


#======================================================================================================


#Exercise 4: Arrange string characters such that lowercase letters should come first
"""
str1=input('enter the string \n')
str1=list(str1)
lower=''
upper=''
for i in str1:
    if i.islower():
        lower+=i
    else :
        upper+=i
new_string=lower+upper 
print(new_string)
"""



#======================================================================================================


#Exercise 5: Count all letters, digits, and special symbols from a given string
"""
str1=input('enter the string')
alpha1=int(0)
digit1=int(0)
spesyb=int (0)
for i in str1:
    if i.isalpha():
        alpha1+=1
    else :
        if i.isdigit():
            digit1+=1
        else:
            spesyb=+1
print('Alphabets='+str(alpha1)+'\n'+'Digits='+str(digit1)+'\n'+'Specialsymbols='+str(spesyb))
"""

#======================================================================================================


"""Exercise 6: Create a mixed String using the following rules
Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. 
Any leftover chars go at the end of the result."""
"""
s1 = input("enter the string")
s2 = input("enter the string")

# get string length
s1_length = len(s1)
s2_length = len(s2)
length = s1_length if s1_length > s2_length else s2_length
result = ""

s2 = s2[::-1]

for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)
"""


"""Exercise 7: String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are
 balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter."""
"""
str1=input("enter the s1 string")
str2=input("enter the s2 string")
s1=str1.lower()
s2=str2.lower()
char_set=set(s2)

for i in s1:
        if i not in  char_set:
            print("the string is not balanced")
            break
else:
     print("string is  balanced")
"""

#======================================================================================================


"""Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
Write a program to find all occurrences of “USA” in a given string ignoring the case."""
"""
str1=input("enter the sentence")
substring=input("enter the substring")
temper_str=str1.lower()
count_substr=str1.count(substring.lower())
print(count_substr)
"""


#======================================================================================================


"""Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string,
 ignoring all other characters"""

"""
str1 = input("Enter string including digits: ")
str2 = list(str1)
sum_digits = 0
count_digits = 0

for i in str2:
    if i.isdigit():
      sum_digits+=int(i)
      count_digits+=1
if count_digits>0:
    avg=sum_digits/count_digits
else:
    avg=0

print("sum oof the digits is ",sum_digits)
print("average of the number is ",avg)
"""


#=======================================================================================================


"""Exercise 10: Write a program to count occurrences of all characters within a string"""
"""
str1 = input("Enter the string: ")
frequency = {}
for char in str1:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(char + ": " + str(count))
"""


#=======================================================================================================



"""Exercise 11: Reverse a given string"""
"""
str1=input("enter the string to reverse")
str2=str1[::-1]
print(str2)
"""

#=======================================================================================================


"""Exercise 12: Find the last position of a given substring"""
"""
main_string=input("enter the string")
substring=input("enter the substring of find its position")
main_str=main_string.lower()
index=main_str.find(substring.lower())
print("the last occurrance of the substring is ",index)
"""


#======================================================================================================


"""Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring"""
"""
str1=input("enter the string for spliting with hyphen")
split_string=str1.split("-")
for i in split_string:
    print(i)
"""

#========================================================================================================


"""Exercise 14: Remove empty strings from a list of strings"""
"""
str1=["jon",'prashant','','praveen','emma','','enjoy']
tem_list=[]
for i in str1:
    if i:
        tem_list.append(i)
print(tem_list)
"""


#==========================================================================================================



"""Exercise 15: Removal all characters from a string except integers"""
"""
str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)
str1=list(str1)
digits=[]
for item in str1:
    if item.isdigit():
        digits.append(item)
result="".join(digits)
print(result)
"""


#==========================================================================================================


"""Exercise 16: Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string."""
"""
str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)
res = []
temp = str1.split()
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
print("Displaying words with alphabets and numbers")
for i in res:
    print(i)
"""

#==========================================================================================================


"""Exercise 17: Replace each special symbol with # in the following string"""
"""
import string
str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)
replace_char = '#'

for char in string.punctuation:
    str1=str1.replace(char, replace_char)

print("The strings after replacement ", str1)
"""


a=input("entert the number")
for i in range(0,n-1):
    for j in range(0,n-1):
        print(j)