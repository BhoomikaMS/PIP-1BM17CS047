li=list(map(int,input("Enter the list:").split()))
newlist=[]
for i in li:
	if i%2==0:
		newlist.append(i)
print(newlist)
