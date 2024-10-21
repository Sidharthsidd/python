# # Python3 program to implement direct index 
# # mapping with negative values allowed.

# # Searching if X is Present in the 
# # given array or not.
# def search(X):

# 	if X >= 0:
# 		return has[X][0] == 1

# 	# if X is negative take the absolute
# 	# value of X.
# 	X = abs(X)
# 	return has[X][1] == 1

# def insert(a, n):

# 	for i in range(0, n):
# 		if a[i] >= 0:
# 			has[a[i]][0] = 1
# 		else:
# 			has[abs(a[i])][1] = 1

# # Driver code
# if __name__ == "__main__":

# 	a = [-1, 9, -5, -8, -5, -2]
# 	n = len(a)

# 	MAX = 1000
	
# 	# Since array is global, it is
# 	# initialized as 0.
# 	has = [[0 for i in range(2)] 
# 			for j in range(MAX + 1)]
# 	insert(a, n)

# 	X = -5
# 	if search(X) == True:
# 		print("Present")
# 	else:
# 		print("Not Present")

# # This code is contributed by Rituraj Jain


# a = [1,3,3,4,1,4,4,4,4] 
# n = len(a) 
# b = [0]*n
    
# for i in range(0, n):
#     y = a[i]
#     b[y]+=1
    
    
    
    
    
# q = int(input());    

# for l in range(0, q):
#     qry = int(input());
#     frq = 0 ;
    
#     print(qry,end = " ")
#     print("-> number occurs",end = " ")
#     print(b[qry], end =" ")
#     print("->times in the array given")

# n = 6
# arr = [1, 1, 2, 3, 3, 3]

# mp={}
# minifreq=float("inf")  
# maxiele=float("-inf")
# mini=n+1
# maxifreq=0
# for i in range(n):
#     if arr[i] in mp:
#         mp[arr[i]]+=1
#     else:
#         mp[arr[i]]=1
#     if i< mp[arr[i]]:
#         maxifreq=i
#         maxiele=arr[i]
#     if i>mp[arr[i]]:
#         minifreq=mp[arr[i]]
#         miniele=arr[i]

# print(f"maax electment {maxiele}  with freqency of : {maxifreq}")
# print(f"mini number of elemet : {miniele} with freqeny of : {minifreq}")

# n = 6
# n = 10
# arr = [1,1,8,6,8,4,3,5,6,4,3]

# mp = {}
# # this is for to cheak if number is in infiniity in negative value 
# maxiFreq = float('-inf')
# maxiElement = arr[0]
# miniFreq = float('inf')# same as in positive value 
# miniElement = arr[0]

# for i  in arr:
# 	mp[i]=mp.get(i,0)+1 # this will count the number of frequency in the arr 
# for num,freq in mp.items(): # this output would be [(1,2),(2,3)]  this for loop used to uncap the list
#     if freq>=maxiFreq:
#         maxiFreq=freq
#         maxiElement=num
#     if freq<=miniFreq:
#         miniFreq=freq
#         miniElement=num
# print(f"the maxinumer of {maxiElement} occurs times :{maxiFreq}")
# print(f"the maxinumer of {miniElement} occurs times :{miniFreq}")



# def countkvalue(arr,k):
#     num_indices={}
#     for i,num in enumerate(arr):
#         if num in num_indices and i-num_indices[i]<=k:
#             return True
#         num_indices[num]=i
#     return false
# arr=[1,3,4,5,6,3,4]
# k=2
# if countkvalue(arr,k):
#     print("two indices are found ")
# else :
#     print("no two indices are not found ")


# arr=[1,3,4,5,6,3,4]
# k=6
# mp={}
# count=0
# for i in arr:
#     compleele=k-arr[i]
#     if compleele in mp:
#         count+=1
#     mp[i]=True
# print(count)


# b = [1, 2, 3, 4, 5]
# k = 6
# def countk_value_ele(b,k):
#     mp = {}
#     count=0
#     for i in b:
#         complement=k-i
#         if complement in mp:
#             count+=1
#         else:
#             mp[i]=True
#     return count
# hi=countk_value_ele(b,k)
# print(hi)



# def countt(k,b):
#     count=0
#     freq ={}
#     for j in range(len(b)):
#         if b[j] - k in freq:
#             count+=freq[b[j]-k]
#         if k!=0 and b[j]+k in freq:
#             count+=freq[b[j]+k]
#         if b[j] in freq:
#             freq[b[j]]+=1
#         else:
#             freq[b[j]]=1
#     return count
# b=[1,5,3,4,2]
# k=2
# print(countt(k,b))

"""
Find Sum of Range  [l……….r] where(l<=r) using Prefix sum. 

l=int(input("enter the starting numeber"))
r=int(input("enter the ending number"))
arr=input("")
arr=[int(x) for x in arr]
print(arr)
prefix=[0]*(len(arr)+1)
for i in range(0,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
    print(prefix[i])
print("the sum of number in the given range is :",prefix[r]-prefix[l-1])"""

#session6 
#Find count of number of subarrays with sum ==  k 
"""
from collections import defaultdict
def count_subarrays(arr,k):
    prefix=defaultdict(int)
    print(arr)
    sum=0
    count=0
    prefix[0]=1
    for i in arr:
        sum+=i
        if (sum-k) in prefix:
            count+=prefix[sum-k]
        prefix[sum]+=1
    return count 
k=4
arr=[3,1,2,1,5]   # this can contain negative also like [3,1,2,-2]  so 3+1+-2=4
arr=[int(x) for x in arr]
print("number of subarrays with sum {}:{} ".format(k,count_subarrays(arr,k)))"""

#Find largest/smallest subarray with sum k in Given Array
