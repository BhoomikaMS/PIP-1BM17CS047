n=int(input("Enter number n to generate n fibonacci numbers:"))
li=[0,1]
def fib(n):
	if n==1:
		pass
	else:
		for i in range(2,n):
			li.append(li[i-2]+li[i-1])
fib(n)
print(li)
