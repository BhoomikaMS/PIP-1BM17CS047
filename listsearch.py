li=list(map(int,input("Enter the list: ").split()))
key=int(input("Enter a number to be searched: "))
def func(olist,key):
    if key in olist:
        return True
    else:
        return False
result=func(li,key)
print("Found: ",result)
