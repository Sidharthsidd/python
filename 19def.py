# Write Python 3 code in this online editor and run it.
def name(n):
    if n==0:
        return
    print(n)
    name(n-1)
    
n=int(input())
name(n)